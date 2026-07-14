#!/usr/bin/env python3
"""Run fresh, preserved agent Audits on both corpora and review every judgment.

The annotator and reviewer run in separate, non-persistent model contexts with
no repository tools. Source cohort labels are withheld from both prompts. Raw
model events, instantiated prompts, source hashes, native work bundles, Audit
outputs, and independent reviews are retained for forensic inspection.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
import threading
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
GRADER = ROOT / "human-eyes/scripts/grade.py"
REGISTRY = ROOT / "human-eyes/scripts/judgement.json"
ESTABLISHED = ROOT / "dev/evals/corpus.json"
PILOT = ROOT / "dev/evals/samples/pilot-additions-01/manifest.json"
DEFAULT_OUTPUT = ROOT / "dev/evals/preserved-agent-audits-2026-07-14"

ANNOTATOR_SYSTEM = "You are a careful whole-document prose auditor. Follow the user contract exactly."
REVIEWER_SYSTEM = "You are an independent prose-audit reviewer. Re-read the document and verify every judgment yourself."

ANNOTATOR_WRAPPER = """Perform a complete agent-assessed Audit of the document below.

Rules:
1. Read the whole document before answering. Do not guess who wrote it and do not classify authorship.
2. Apply every registry record exactly as written and return exactly one answer per record in registry order.
3. The document is raw Markdown. Every quoted list-item phrase must be a byte-for-byte substring of that raw Markdown, including capitalization, punctuation, and any Markdown delimiters. Prefer spans without links or emphasis markup; if markup is unavoidable, copy it exactly. Never quote the rendered form of a Markdown link.
4. Base whole-document state or distribution judgments on multiple parts of the document when enough material exists. One sentence alone cannot prove a whole-document state.
5. For list judgments, report every material instance you can support, not just the first. An empty list means you inspected the whole document and found none.
6. Treat genre-appropriate consistency, repetition, terminology, formatting, and rhetoric in context. A construction is not defective merely because it is detectable.
7. The `evidence` array must always be empty; the current native contract uses exact phrase fields inside list answers for source evidence. Status must be mechanically consistent with flagged_when. Do not add commentary outside the JSON object.

REGISTRY:
{registry}

DOCUMENT:
<document>
{document}
</document>
"""

REVIEWER_WRAPPER = """Independently review a preserved agent-assessed Audit.

Rules:
1. Re-read the whole document and apply every registry record yourself before deciding whether the annotator was right.
2. Do not guess who wrote the document and do not classify authorship.
3. Review all 15 judgments, including clear judgments that may hide false negatives.
4. A whole-document or distribution judgment needs evidence from multiple parts of the document when enough material exists.
5. Treat genre-appropriate consistency, repetition, terminology, formatting, and rhetoric in context.
6. Use verdict `supported` only when the annotator's answer and evidence are adequate; `overcall` when it flags a defect that is not present; `undercall` when it clears a defect that is present; `misclassified` when the status may be right but the selected category, genre, scope, or answer is materially wrong; and `insufficient_evidence` when the conclusion may be plausible but the supplied evidence does not establish it.
7. Evidence strings in your review must be literal exact substrings from the document. Return exactly one review per registry record in registry order. Do not add commentary outside the JSON object.

REGISTRY:
{registry}

DOCUMENT:
<document>
{document}
</document>

ANNOTATOR ANSWERS:
{answers}
"""

REVIEW_SCHEMA = {
    "type": "object",
    "properties": {
        "reviews": {
            "type": "array",
            "minItems": 15,
            "maxItems": 15,
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "verdict": {
                        "type": "string",
                        "enum": [
                            "supported", "overcall", "undercall",
                            "misclassified", "insufficient_evidence",
                        ],
                    },
                    "rationale": {"type": "string"},
                    "evidence": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["id", "verdict", "rationale", "evidence"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["reviews"],
    "additionalProperties": False,
}

PRINT_LOCK = threading.Lock()


def build_annotator_schema(registry: dict) -> dict:
    """Build a structured-output schema that makes status derivation exact."""
    variants = []
    base_required = ["id", "status", "answer", "evidence"]
    for record in registry["records"]:
        answer_schema = record["answer_schema"]
        schema_type = answer_schema["type"]
        common = {
            "id": {"const": record["id"]},
            "evidence": {"type": "array", "maxItems": 0},
        }
        if schema_type in {"state", "trichotomy"}:
            flagged = set(record["flagged_when"])
            for value in answer_schema["values"]:
                variants.append({
                    "type": "object",
                    "properties": {
                        **common,
                        "status": {"const": "flagged" if value in flagged else "clear"},
                        "answer": {"const": value},
                    },
                    "required": base_required,
                    "additionalProperties": False,
                })
        elif schema_type == "list":
            fields = answer_schema["items"]
            item_schema = {
                "type": "object",
                "properties": {field: {"type": "string"} for field in fields},
                "required": fields,
                "additionalProperties": False,
            }
            for status, bounds in (("clear", {"maxItems": 0}), ("flagged", {"minItems": 1})):
                variants.append({
                    "type": "object",
                    "properties": {
                        **common,
                        "status": {"const": status},
                        "answer": {"type": "array", "items": item_schema, **bounds},
                    },
                    "required": base_required,
                    "additionalProperties": False,
                })
        elif schema_type == "composite":
            fields = answer_schema["fields"]
            finding_fields = fields["watchlist_findings"]["items"]
            finding_schema = {
                "type": "object",
                "properties": {field: {"type": "string"} for field in finding_fields},
                "required": finding_fields,
                "additionalProperties": False,
            }
            for status, bounds in (("clear", {"maxItems": 0}), ("flagged", {"minItems": 1})):
                variants.append({
                    "type": "object",
                    "properties": {
                        **common,
                        "status": {"const": status},
                        "answer": {
                            "type": "object",
                            "properties": {
                                "genre_detected": {"enum": fields["genre_detected"]["values"]},
                                "watchlist_findings": {
                                    "type": "array", "items": finding_schema, **bounds,
                                },
                            },
                            "required": ["genre_detected", "watchlist_findings"],
                            "additionalProperties": False,
                        },
                    },
                    "required": base_required,
                    "additionalProperties": False,
                })
        else:
            raise ValueError(f"unsupported answer schema: {schema_type}")
    return {
        "type": "object",
        "properties": {
            "semantic_answers": {
                "type": "array", "minItems": len(registry["records"]),
                "maxItems": len(registry["records"]), "items": {"oneOf": variants},
            }
        },
        "required": ["semantic_answers"],
        "additionalProperties": False,
    }


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_documents() -> list[dict]:
    established = json.loads(ESTABLISHED.read_text(encoding="utf-8"))
    pilot = json.loads(PILOT.read_text(encoding="utf-8"))
    documents = []
    number = 0
    for cohort in ("human", "ai_fresh", "ai_rewrite"):
        for cohort_index, relative in enumerate(established["groups"][cohort], start=1):
            number += 1
            path = (ROOT / "dev" / relative).resolve()
            documents.append({
                "anonymous_id": f"D{number:02d}",
                "corpus": "established",
                "cohort": cohort,
                "cohort_index": cohort_index,
                "source_path": str(path.relative_to(ROOT)),
            })
    for pair_index, pair in enumerate(pilot["pairs"], start=1):
        for cohort in ("human", "ai"):
            number += 1
            path = (PILOT.parent / pair[cohort]["path"]).resolve()
            documents.append({
                "anonymous_id": f"D{number:02d}",
                "corpus": "pilot_additions",
                "cohort": cohort,
                "cohort_index": pair_index,
                "pair_id": pair["id"],
                "source_path": str(path.relative_to(ROOT)),
            })
    for document in documents:
        path = ROOT / document["source_path"]
        if not path.is_file():
            raise FileNotFoundError(path)
        document["content_sha256"] = sha256_bytes(path.read_bytes())
        document["bytes"] = path.stat().st_size
    return documents


def parse_claude_output(stdout: str) -> dict:
    events = json.loads(stdout)
    for event in reversed(events):
        structured = event.get("structured_output") if isinstance(event, dict) else None
        if structured is not None:
            return structured
    raise ValueError("Claude output did not contain structured_output")


def parse_codex_output(stdout: str) -> dict:
    messages = []
    for line in stdout.splitlines():
        if not line.strip().startswith("{"):
            continue
        event = json.loads(line)
        item = event.get("item", {})
        if event.get("type") == "item.completed" and item.get("type") == "agent_message":
            messages.append(item.get("text", ""))
    if not messages:
        raise ValueError("Codex output did not contain an agent message")
    return json.loads(messages[-1])


def run_claude(prompt: str, schema: dict) -> tuple[dict, dict]:
    env = dict(os.environ)
    env.pop("ANTHROPIC_API_KEY", None)
    command = [
        "claude", "-p", "--safe-mode", "--disable-slash-commands",
        "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
        "--tools", "", "--no-session-persistence",
        "--system-prompt", ANNOTATOR_SYSTEM,
        "--model", "sonnet", "--effort", "medium",
        "--output-format", "json", "--json-schema", json.dumps(schema),
        prompt,
    ]
    completed = subprocess.run(
        command, cwd=ROOT, env=env, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, timeout=900,
    )
    raw = {
        "command": command[:-1] + ["<prompt omitted; see prompt.txt>"],
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }
    if completed.returncode:
        raise RuntimeError(f"Claude exited {completed.returncode}: {completed.stderr[-1000:]}")
    return parse_claude_output(completed.stdout), raw


def run_codex(prompt: str, schema_path: Path) -> tuple[dict, dict]:
    env = dict(os.environ)
    env["PATH"] = "/usr/bin:/bin:/usr/sbin:/sbin"
    command = [
        "/opt/homebrew/bin/codex", "exec", "--ignore-user-config",
        "--skip-git-repo-check", "-s", "read-only", "-C", "/tmp",
        "--ephemeral", "--json", "-m", "gpt-5.4",
        "-c", 'model_reasoning_effort="medium"',
        "--output-schema", str(schema_path), "-",
    ]
    completed = subprocess.run(
        command, cwd="/tmp", env=env, text=True, input=prompt,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=900,
    )
    raw = {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }
    if completed.returncode:
        raise RuntimeError(f"Codex exited {completed.returncode}: {completed.stderr[-1000:]}")
    return parse_codex_output(completed.stdout), raw


def validate_review(review: dict, text: str, registry_ids: list[str]) -> list[dict]:
    items = review.get("reviews")
    if not isinstance(items, list) or [item.get("id") for item in items] != registry_ids:
        raise ValueError("review does not contain all registry ids in order")
    issues = []
    for item in items:
        for phrase in item.get("evidence", []):
            if phrase not in text:
                issues.append({
                    "id": item["id"],
                    "issue": "evidence_not_exact_source_substring",
                    "phrase": phrase,
                })
    return issues


def document_dir(output: Path, document: dict) -> Path:
    return output / "documents" / document["anonymous_id"]


def annotate_one(output: Path, document: dict, registry_text: str, registry_ids: list[str], schema: dict, retries: int) -> None:
    directory = document_dir(output, document)
    audit_path = directory / "audit.json"
    if audit_path.is_file():
        return
    text = (ROOT / document["source_path"]).read_text(encoding="utf-8")
    prompt = ANNOTATOR_WRAPPER.format(registry=registry_text, document=text)
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "annotator-prompt.txt").write_text(prompt, encoding="utf-8")
    errors = []
    for attempt in range(1, retries + 1):
        try:
            result, raw = run_claude(prompt, schema)
            write_json(directory / f"annotator-raw-attempt-{attempt}.json", raw)
            answers = result["semantic_answers"]
            if [item.get("id") for item in answers] != registry_ids:
                raise ValueError("annotator did not return registry ids in order")
            bundle_path = directory / "work-bundle.json"
            subprocess.run(
                [sys.executable, str(GRADER), "preflight", str(ROOT / document["source_path"]),
                 "--work-bundle", str(bundle_path)],
                cwd=ROOT, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
            )
            bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
            bundle["semantic_answers"] = answers
            write_json(bundle_path, bundle)
            audited = subprocess.run(
                [sys.executable, str(GRADER), "audit", str(ROOT / document["source_path"]),
                 "--work-bundle", str(bundle_path), "--format", "json"],
                cwd=ROOT, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
            )
            audit = json.loads(audited.stdout)
            if audit.get("coverage_mode") != "full" or audit.get("audit_status") != "complete":
                raise ValueError("native Audit is not full and complete")
            write_json(directory / "annotator-answer.json", result)
            write_json(audit_path, audit)
            write_json(directory / "annotator-metadata.json", {
                "anonymous_id": document["anonymous_id"],
                "content_sha256": document["content_sha256"],
                "prompt_sha256": sha256_text(prompt),
                "registry_sha256": sha256_text(registry_text),
                "attempt": attempt,
                "model_requested": "claude-sonnet-5",
                "effort": "medium",
                "tools": [],
            })
            with PRINT_LOCK:
                print(f"annotated {document['anonymous_id']} ({attempt=})", flush=True)
            return
        except Exception as exc:  # preserve failures; repeat identical prompt
            errors.append(str(exc))
            write_json(directory / f"annotator-error-attempt-{attempt}.json", {"error": str(exc)})
    raise RuntimeError(f"{document['anonymous_id']} annotation failed: {errors[-1]}")


def review_one(output: Path, document: dict, registry_text: str, registry_ids: list[str], retries: int) -> None:
    directory = document_dir(output, document)
    review_path = directory / "review.json"
    if review_path.is_file():
        return
    text = (ROOT / document["source_path"]).read_text(encoding="utf-8")
    answers = json.loads((directory / "annotator-answer.json").read_text(encoding="utf-8"))
    prompt = REVIEWER_SYSTEM + "\n\n" + REVIEWER_WRAPPER.format(
        registry=registry_text,
        document=text,
        answers=json.dumps(answers, indent=2, ensure_ascii=False),
    )
    (directory / "reviewer-prompt.txt").write_text(prompt, encoding="utf-8")
    schema_path = output / "review-schema.json"
    errors = []
    for attempt in range(1, retries + 1):
        try:
            result, raw = run_codex(prompt, schema_path)
            write_json(directory / f"reviewer-raw-attempt-{attempt}.json", raw)
            validation_issues = validate_review(result, text, registry_ids)
            write_json(review_path, result)
            write_json(directory / "review-validation.json", {
                "valid_registry_coverage": True,
                "citation_issues": validation_issues,
            })
            write_json(directory / "reviewer-metadata.json", {
                "anonymous_id": document["anonymous_id"],
                "content_sha256": document["content_sha256"],
                "prompt_sha256": sha256_text(prompt),
                "registry_sha256": sha256_text(registry_text),
                "attempt": attempt,
                "model_requested": "gpt-5.4",
                "reasoning_effort": "medium",
                "sandbox": "read-only",
                "working_directory": "/tmp",
                "path": "/usr/bin:/bin:/usr/sbin:/sbin",
            })
            with PRINT_LOCK:
                print(f"reviewed {document['anonymous_id']} ({attempt=})", flush=True)
            return
        except Exception as exc:  # preserve failures; repeat identical prompt
            errors.append(str(exc))
            write_json(directory / f"reviewer-error-attempt-{attempt}.json", {"error": str(exc)})
    raise RuntimeError(f"{document['anonymous_id']} review failed: {errors[-1]}")


def run_parallel(label: str, documents: list[dict], workers: int, function) -> None:
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(function, document): document for document in documents}
        for future in concurrent.futures.as_completed(futures):
            document = futures[future]
            try:
                future.result()
            except Exception as exc:
                failures.append((document["anonymous_id"], str(exc)))
                with PRINT_LOCK:
                    print(f"FAILED {label} {document['anonymous_id']}: {exc}", file=sys.stderr, flush=True)
    if failures:
        raise RuntimeError(f"{label} failures: {failures}")


def summarize(output: Path, documents: list[dict], registry_ids: list[str]) -> dict:
    cohort_counts = defaultdict(lambda: {
        "documents": 0, "judgments": 0, "flagged": 0,
        "review_determinate_flagged": 0, "review_unresolved": 0,
        "review_verdicts": Counter(),
    })
    record_counts = defaultdict(Counter)
    verdict_counts = Counter()
    reviewed = 0
    review_citation_issues = 0
    for document in documents:
        directory = document_dir(output, document)
        audit = json.loads((directory / "audit.json").read_text(encoding="utf-8"))
        review = json.loads((directory / "review.json").read_text(encoding="utf-8"))
        review_validation = json.loads(
            (directory / "review-validation.json").read_text(encoding="utf-8")
        )
        review_citation_issues += len(review_validation["citation_issues"])
        key = f"{document['corpus']}::{document['cohort']}"
        audit_by_id = {item["id"]: item for item in audit["semantic_findings"]}
        cohort_counts[key]["documents"] += 1
        cohort_counts[key]["judgments"] += len(audit["semantic_findings"])
        cohort_counts[key]["flagged"] += sum(
            item["status"] == "flagged" for item in audit["semantic_findings"]
        )
        for item in audit["semantic_findings"]:
            record_counts[item["id"]][f"{key}::flagged"] += item["status"] == "flagged"
        for item in review["reviews"]:
            verdict_counts[item["verdict"]] += 1
            cohort_counts[key]["review_verdicts"][item["verdict"]] += 1
            record_counts[item["id"]][f"review::{item['verdict']}"] += 1
            original_flagged = audit_by_id[item["id"]]["status"] == "flagged"
            if item["verdict"] == "supported":
                adjusted_flagged = original_flagged
            elif item["verdict"] == "overcall":
                adjusted_flagged = False
            elif item["verdict"] == "undercall":
                adjusted_flagged = True
            else:
                adjusted_flagged = None
            if adjusted_flagged is None:
                cohort_counts[key]["review_unresolved"] += 1
            else:
                cohort_counts[key]["review_determinate_flagged"] += adjusted_flagged
            reviewed += 1
    serializable_cohorts = {}
    for key, counts in cohort_counts.items():
        serializable_cohorts[key] = {
            **{field: value for field, value in counts.items() if field != "review_verdicts"},
            "review_verdicts": dict(counts["review_verdicts"]),
        }
    summary = {
        "schema_version": 1,
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "documents": len(documents),
        "judgments": len(documents) * len(registry_ids),
        "reviewed_judgments": reviewed,
        "review_citation_issues": review_citation_issues,
        "cohorts": serializable_cohorts,
        "review_verdicts": dict(verdict_counts),
        "records": {record_id: dict(record_counts[record_id]) for record_id in registry_ids},
    }
    write_json(output / "summary.json", summary)
    lines = [
        "# Preserved agent-assessed Audit and independent review",
        "",
        f"Date: {dt.date.today().isoformat()}",
        "",
        f"All {len(documents)} documents received a fresh 15-record Audit under one fixed instruction wrapper. "
        f"All {reviewed} judgments were then reviewed in separate Codex contexts.",
        "",
        "## Agent-assessed flags",
        "",
        "| Corpus cohort | Documents | Agent flags | Determinate reviewed flags | Unresolved reviews | Total judgments |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for key, counts in cohort_counts.items():
        lines.append(
            f"| {key} | {counts['documents']} | {counts['flagged']} | "
            f"{counts['review_determinate_flagged']} | {counts['review_unresolved']} | "
            f"{counts['judgments']} |"
        )
    lines += ["", "## Independent-review verdicts", "", "| Verdict | Count |", "|---|---:|"]
    for verdict in ["supported", "overcall", "undercall", "misclassified", "insufficient_evidence"]:
        lines.append(f"| {verdict} | {verdict_counts[verdict]} |")
    lines += [
        "",
        "Determinate reviewed flags apply supported judgments, remove overcalls, and add undercalls. "
        "They are a lower bound, not a replacement score: misclassified and insufficient-evidence judgments remain unresolved.",
        "",
        "## Judgment reliability by record",
        "",
        "| Record | Agent flags | Supported | Overcall | Undercall | Misclassified | Insufficient evidence |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for record_id in registry_ids:
        counts = record_counts[record_id]
        original_flags = sum(value for key, value in counts.items() if key.endswith("::flagged"))
        lines.append(
            f"| {record_id} | {original_flags} | {counts['review::supported']} | "
            f"{counts['review::overcall']} | {counts['review::undercall']} | "
            f"{counts['review::misclassified']} | {counts['review::insufficient_evidence']} |"
        )
    established_human = cohort_counts["established::human"]["flagged"]
    pilot_human = cohort_counts["pilot_additions::human"]["flagged"]
    lines += [
        "",
        "## Interpretation",
        "",
        f"- The raw agent run flags established AI-fresh prose {cohort_counts['established::ai_fresh']['flagged'] - established_human:+d} "
        f"more times than established human prose, and AI rewrites {cohort_counts['established::ai_rewrite']['flagged'] - established_human:+d} more times.",
        f"- The raw agent run flags pilot AI prose {cohort_counts['pilot_additions::ai']['flagged'] - pilot_human:+d} more times than pilot human prose.",
        "- Independent review does not validate those gaps as a performance score. Insufficient-evidence judgments are intentionally unresolved, and overcalls are concentrated in broad semantic categories such as redundancy and formulaic parallelism.",
        "- The largest category-definition problem is even_jargon_distribution; most disagreements concern the registry's forced choice between clumped, natural, and uniform distribution.",
        "- Tonal_uniformity remains unstable: reviewers both removed genre-appropriate uniformity flags and found missed uniformity, while many answers lacked enough preserved evidence to adjudicate.",
    ]
    lines += [
        "",
        "## Preservation and limitations",
        "",
        "- Annotator prompts, raw events, native work bundles, and full Audit JSON are retained per document.",
        "- Reviewer prompts, raw events, and one verdict for every registry judgment are retained per document.",
        f"- Reviewer citation validation found {review_citation_issues} non-exact evidence strings; these are retained as quality issues and were not silently repaired.",
        "- Corpus and cohort labels were absent from model prompts; `index.json` restores the mapping for analysis.",
        "- These are model judgments, not authorship ground truth. Review disagreement is evidence about judgment reliability.",
    ]
    (output / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--stage", choices=["all", "annotate", "review", "summarize"], default="all")
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--retries", type=int, default=3)
    args = parser.parse_args()

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    registry_text = REGISTRY.read_text(encoding="utf-8")
    registry = json.loads(registry_text)
    registry_ids = [record["id"] for record in registry["records"]]
    annotator_schema = build_annotator_schema(registry)
    documents = load_documents()
    write_json(output / "annotator-schema.json", annotator_schema)
    write_json(output / "review-schema.json", REVIEW_SCHEMA)
    write_json(output / "index.json", {"schema_version": 1, "documents": documents})
    write_json(output / "contract.json", {
        "schema_version": 1,
        "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "annotator": {
            "model_requested": "claude-sonnet-5",
            "effort": "medium",
            "system_prompt": ANNOTATOR_SYSTEM,
            "wrapper": ANNOTATOR_WRAPPER,
            "wrapper_sha256": sha256_text(ANNOTATOR_WRAPPER),
            "tools": [],
        },
        "reviewer": {
            "model_requested": "gpt-5.4",
            "reasoning_effort": "medium",
            "instruction_prefix": REVIEWER_SYSTEM,
            "wrapper": REVIEWER_WRAPPER,
            "wrapper_sha256": sha256_text(REVIEWER_WRAPPER),
            "sandbox": "read-only",
            "path_excludes_homebrew": True,
        },
        "registry_path": str(REGISTRY.relative_to(ROOT)),
        "registry_sha256": sha256_text(registry_text),
        "established_manifest": str(ESTABLISHED.relative_to(ROOT)),
        "pilot_manifest": str(PILOT.relative_to(ROOT)),
        "source_labels_withheld_from_prompts": True,
        "retry_policy": "repeat the identical instantiated prompt; never repair answers by hand",
    })

    if args.stage in {"all", "annotate"}:
        run_parallel(
            "annotation", documents, args.workers,
            lambda document: annotate_one(
                output, document, registry_text, registry_ids, annotator_schema, args.retries
            ),
        )
    if args.stage in {"all", "review"}:
        run_parallel(
            "review", documents, args.workers,
            lambda document: review_one(output, document, registry_text, registry_ids, args.retries),
        )
    if args.stage in {"all", "summarize"}:
        summary = summarize(output, documents, registry_ids)
        print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
