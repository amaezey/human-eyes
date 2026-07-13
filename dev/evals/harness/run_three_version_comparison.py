#!/usr/bin/env python3
"""Run one manifest-bound corpus through three native grader versions.

This harness deliberately invokes each checkout's own ``grade.py`` in a
subprocess.  It does not import the current grader into historical runs and it
does not assume that the May and July report envelopes are identical.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import statistics
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DEFAULT_MANIFEST = ROOT / "dev/evals/samples/pilot-additions-01/manifest.json"
DEFAULT_OUTPUT = ROOT / "dev/evals/three-version-pilot-additions-comparison.json"

VERSIONS = {
    "current": {
        "root": ROOT,
        "commit": None,  # resolved from git at run time
        "interface": "audit-surface-only",
    },
    "pre-refactor-56f262a": {
        "root": Path("/tmp/human-eyes-56f262a"),
        "commit": "56f262a18ba1271268ae98d7a49cba1e7a33a168",
        "interface": "audit-surface-only",
    },
    "may-f28a370": {
        "root": Path("/tmp/human-eyes-f28a370"),
        "commit": "f28a3706816d0ca5107196955a5d14418732a5af",
        "interface": "legacy-direct-file",
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_path(value: str, manifest_path: Path) -> Path:
    path = Path(value)
    candidates = (path, manifest_path.parent / path, ROOT / path, ROOT / "dev" / path)
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    raise FileNotFoundError(f"cannot resolve manifest path: {value}")


def current_grader_commit() -> str:
    result = subprocess.run(
        ["git", "log", "-1", "--format=%H", "--", "human-eyes/scripts/grade.py"],
        cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
    )
    return result.stdout.strip()


def native_command(version: dict, document: Path) -> list[str]:
    grader = version["root"] / "human-eyes/scripts/grade.py"
    if version["interface"] == "audit-surface-only":
        return [sys.executable, str(grader), "audit", str(document),
                "--surface-only", "--format", "json"]
    if version["interface"] == "legacy-direct-file":
        return [sys.executable, str(grader), "--format", "json", str(document)]
    raise ValueError(f"unknown grader interface: {version['interface']}")


def extract_native_checks(payload: dict, interface: str) -> list[dict]:
    if interface == "audit-surface-only":
        checks = payload.get("programmatic_checks")
    elif interface == "legacy-direct-file":
        checks = payload.get("human_report", {}).get("programmatic_checks")
    else:
        checks = None
    if not isinstance(checks, list):
        raise ValueError(f"native {interface} output has no programmatic check list")
    return checks


def normalize_check(item: dict) -> dict:
    if not isinstance(item.get("id"), str) or item.get("status") not in {"clear", "flagged"}:
        raise ValueError("native check is missing a valid id or status")
    return {
        "id": item["id"],
        "flagged": item["status"] == "flagged",
        "native_status": item["status"],
        "severity": item.get("severity"),
        "category": item.get("category"),
        "evidence": item.get("evidence"),
    }


def grade(version: dict, document: Path) -> tuple[list[dict], dict]:
    grader = version["root"] / "human-eyes/scripts/grade.py"
    if not grader.is_file():
        raise FileNotFoundError(f"grader missing: {grader}")
    command = native_command(version, document)
    result = subprocess.run(
        command, cwd=version["root"], text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if result.returncode:
        raise RuntimeError(
            f"grader failed ({result.returncode}): {' '.join(command)}\n{result.stderr.strip()}"
        )
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise ValueError(f"grader returned invalid JSON: {exc}") from exc
    checks = [normalize_check(item) for item in extract_native_checks(payload, version["interface"])]
    if len({item["id"] for item in checks}) != len(checks):
        raise ValueError("native output contains duplicate check ids")
    return checks, payload


def load_semantic_input(path: Path, version_id: str, commit: str,
                        manifest_hash: str, document_hashes: dict[str, str]) -> dict:
    """Validate and preserve a version's native semantic audit without translating it.

    The only common contract is identity binding. The version-specific payload
    remains under ``native_output`` so this runner does not invent equivalence
    between semantic registries or schemas.
    """
    data = json.loads(path.read_text(encoding="utf-8"))
    expected = {
        "version_id": version_id,
        "version_commit": commit,
        "manifest_sha256": manifest_hash,
    }
    for key, value in expected.items():
        if data.get(key) != value:
            raise ValueError(f"semantic input {path}: {key} does not match {value}")
    records = data.get("documents")
    if not isinstance(records, list) or len(records) != len(document_hashes):
        raise ValueError(f"semantic input {path}: expected {len(document_hashes)} documents")
    seen = set()
    for record in records:
        doc_id = record.get("document_id")
        if doc_id in seen or doc_id not in document_hashes:
            raise ValueError(f"semantic input {path}: invalid or duplicate document_id {doc_id}")
        seen.add(doc_id)
        if record.get("document_sha256") != document_hashes[doc_id]:
            raise ValueError(f"semantic input {path}: document hash mismatch for {doc_id}")
        if "native_output" not in record:
            raise ValueError(f"semantic input {path}: missing native_output for {doc_id}")
    return {"path": str(path.resolve()), "sha256": sha256(path), "payload": data}


def paired_summary(documents: list[dict]) -> dict:
    human = sum(doc["cohort"] == "human" and doc["surface_findings"] for doc in documents)
    ai = sum(doc["cohort"] == "ai" and doc["surface_findings"] for doc in documents)
    by_pair: dict[str, dict] = {}
    for doc in documents:
        by_pair.setdefault(doc["pair_id"], {})[doc["cohort"]] = doc["surface_findings"]
    deltas = [pair["ai"] - pair["human"] for pair in by_pair.values()]
    return {
        "human_findings": human,
        "ai_findings": ai,
        "mean_ai_minus_human": statistics.fmean(deltas),
        "ai_higher_pairs": sum(delta > 0 for delta in deltas),
        "ties": sum(delta == 0 for delta in deltas),
        "human_higher_pairs": sum(delta < 0 for delta in deltas),
        "pair_deltas": deltas,
    }


def per_check_summary(documents: list[dict]) -> list[dict]:
    ids = sorted({check["id"] for document in documents for check in document["checks"]})
    rows = []
    for check_id in ids:
        counts = {}
        availability = {}
        candidate_counts = {}
        candidate_documents = {}
        threshold_documents = {}
        for cohort in ("human", "ai"):
            matches = [check for document in documents if document["cohort"] == cohort
                       for check in document["checks"] if check["id"] == check_id]
            availability[cohort] = len(matches)
            counts[cohort] = sum(check["flagged"] for check in matches)
            raw_evidence = [
                check.get("evidence", {}).get("raw", {})
                if isinstance(check.get("evidence"), dict) else {}
                for check in matches
            ]
            candidate_counts[cohort] = sum(
                evidence.get("candidate_count", 0)
                for evidence in raw_evidence
                if isinstance(evidence.get("candidate_count", 0), int)
            )
            candidate_documents[cohort] = sum(
                evidence.get("candidate_count", 0) > 0 for evidence in raw_evidence
            )
            threshold_documents[cohort] = sum(
                evidence.get("threshold_met") is True for evidence in raw_evidence
            )
        rows.append({"check_id": check_id,
                     "human_documents_checked": availability["human"],
                     "ai_documents_checked": availability["ai"],
                     "human_flags": counts["human"], "ai_flags": counts["ai"],
                     "human_candidate_count": candidate_counts["human"],
                     "ai_candidate_count": candidate_counts["ai"],
                     "human_documents_with_candidates": candidate_documents["human"],
                     "ai_documents_with_candidates": candidate_documents["ai"],
                     "human_documents_threshold_met": threshold_documents["human"],
                     "ai_documents_threshold_met": threshold_documents["ai"],
                     "flag_gap_ai_minus_human": counts["ai"] - counts["human"]})
    return rows


def load_corpus(manifest: dict, manifest_path: Path) -> tuple[list[dict], dict[str, str]]:
    """Load either the established compact corpus or a richer pilot manifest."""
    pairs = manifest.get("pairs")
    if not isinstance(pairs, list) or not pairs:
        raise ValueError("comparison manifest requires at least one pair")
    corpus = []
    hashes = {}
    for index, pair in enumerate(pairs, 1):
        pair_id = pair.get("id") or pair.get("topic") or f"pair-{index:02d}"
        for cohort, source_key in (("human", "human"), ("ai", "ai" if "ai" in pair else "ai_fresh")):
            record = pair.get(source_key)
            if isinstance(record, dict):
                path_value = record.get("path")
                expected_hash = record.get("sha256")
            elif isinstance(record, str):
                path_value = record
                expected_hash = None
            else:
                raise ValueError(f"{pair_id}: missing {source_key} record")
            path = resolve_path(path_value, manifest_path)
            digest = sha256(path)
            if expected_hash is not None and digest != expected_hash:
                raise ValueError(f"{pair_id} {cohort}: manifest hash mismatch")
            doc_id = f"{pair_id}::{cohort}"
            hashes[doc_id] = digest
            corpus.append({"document_id": doc_id, "pair_id": pair_id,
                           "cohort": cohort, "path": path, "sha256": digest})
    return corpus, hashes


def run(manifest_path: Path = DEFAULT_MANIFEST,
        semantic_inputs: dict[str, Path] | None = None) -> dict:
    manifest_path = manifest_path.resolve()
    manifest_hash = sha256(manifest_path)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    corpus, hashes = load_corpus(manifest, manifest_path)

    output = {"schema_version": 1, "manifest": str(manifest_path),
              "manifest_sha256": manifest_hash, "document_count": len(corpus), "versions": {}}
    semantic_inputs = semantic_inputs or {}
    for version_id, base in VERSIONS.items():
        version = dict(base)
        commit = current_grader_commit() if version["commit"] is None else version["commit"]
        grader = version["root"] / "human-eyes/scripts/grade.py"
        documents = []
        for source in corpus:
            checks, native = grade(version, source["path"])
            documents.append({
                **{key: (str(value) if key == "path" else value) for key, value in source.items()},
                "surface_findings": sum(check["flagged"] for check in checks),
                "checks": checks,
                "native_schema_version": native.get("schema_version") or native.get("human_report", {}).get("schema_version"),
            })
        version_output = {
            "commit": commit,
            "grader_path": str(grader),
            "grader_sha256": sha256(grader),
            "native_interface": version["interface"],
            "documents": documents,
            "paired_surface": paired_summary(documents),
            "per_check_surface": per_check_summary(documents),
        }
        if version_id in semantic_inputs:
            version_output["native_semantic_audit"] = load_semantic_input(
                semantic_inputs[version_id], version_id, commit, manifest_hash, hashes
            )
        else:
            version_output["native_semantic_audit"] = None
        output["versions"][version_id] = version_output
    return output


def parse_semantic(values: list[str]) -> dict[str, Path]:
    result = {}
    for value in values:
        if "=" not in value:
            raise ValueError("--semantic-input must be VERSION=PATH")
        version, path = value.split("=", 1)
        if version not in VERSIONS or version in result:
            raise ValueError(f"invalid or duplicate semantic version: {version}")
        result[version] = Path(path).resolve()
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--semantic-input", action="append", default=[], metavar="VERSION=PATH")
    args = parser.parse_args()
    try:
        report = run(args.manifest, parse_semantic(args.semantic_input))
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "manifest_sha256": report["manifest_sha256"],
                      "versions": {key: value["paired_surface"] for key, value in report["versions"].items()}}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
