#!/usr/bin/env python3
"""Run the paired evidence benchmark with explicit completeness checks."""

from __future__ import annotations

import argparse
import importlib.util
import json
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_MANIFEST = ROOT / "dev" / "evals" / "corpus.json"
DEFAULT_REPORT = ROOT / "dev" / "evals" / "evidence-benchmark-report.json"
HOUSE_STYLE_CHECKS = {"no-curly-quotes"}


def load_grade():
    path = ROOT / "human-eyes" / "scripts" / "grade.py"
    spec = importlib.util.spec_from_file_location("grade_evidence_benchmark", path)
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    spec.loader.exec_module(module)
    return module


def resolve_sample(path: str) -> Path:
    candidate = ROOT / "dev" / path
    return candidate if candidate.exists() else ROOT / path


def validate_semantic_audit(audit, registry_ids):
    if not isinstance(audit, dict):
        return "missing semantic audit"
    if audit.get("coverage_mode") != "full" or audit.get("audit_status") != "complete":
        return "semantic audit is not complete/full"
    answers = audit.get("answers", audit.get("semantic_answers", []))
    ids = {answer.get("id") for answer in answers if isinstance(answer, dict)}
    if ids != set(registry_ids):
        return "semantic audit IDs do not exactly match the registry"
    return None


def grade_document(grade, path, semantic=None, registry_ids=()):
    text = path.read_text(encoding="utf-8")
    words = len(text.split())
    started = time.perf_counter()
    checks = {}
    for check_id, check in grade.ALL_CHECKS.items():
        result = check(text)
        evidence = {
            "evidence_type": result["evidence_type"],
            "candidate_count": result["candidate_count"],
            "candidates_per_1000_words": round(result["candidate_count"] * 1000 / max(words, 1), 3),
            "threshold_met": result["threshold_met"],
            "context_suppressed": result["context_suppressed"],
            "threshold": result["threshold"],
            "explanation": result.get("evidence"),
            "context_gate": result["context_gate"],
        }
        if result["evidence_type"] == "lexical":
            evidence.update(match_count=result["match_count"], spans=result["spans"])
        elif result["evidence_type"] == "statistical":
            evidence.update(metric_value=result["metric_value"], sample_size=result["sample_size"])
        else:
            evidence.update(
                component_signals=result["component_signals"],
                component_count=result["component_count"],
            )
        checks[check_id] = evidence
    runtime_ms = round((time.perf_counter() - started) * 1000, 3)
    surface = sum(x["threshold_met"] for key, x in checks.items() if key not in HOUSE_STYLE_CHECKS and key != "overall-signal-stacking")
    house = sum(checks[key]["threshold_met"] for key in HOUSE_STYLE_CHECKS if key in checks)
    semantic_error = validate_semantic_audit(semantic, registry_ids)
    semantic_findings = None if semantic_error else sum(bool(a.get("flagged")) for a in semantic.get("answers", []))
    return {
        "path": str(path.relative_to(ROOT)), "word_count": words,
        "surface_findings": surface, "house_style_findings": house,
        "checks": checks, "runtime_ms": runtime_ms,
        "semantic": semantic, "semantic_findings": semantic_findings,
    }, semantic_error


def summarize(pairs, cohort):
    deltas = [pair[cohort]["surface_findings"] - pair["human"]["surface_findings"] for pair in pairs]
    per_check = {}
    check_ids = next(iter(pairs))["human"]["checks"] if pairs else []
    for check_id in check_ids:
        if check_id in HOUSE_STYLE_CHECKS or check_id == "overall-signal-stacking":
            continue
        human_flags = sum(pair["human"]["checks"][check_id]["threshold_met"] for pair in pairs)
        ai_flags = sum(pair[cohort]["checks"][check_id]["threshold_met"] for pair in pairs)
        candidate_delta = sum(
            pair[cohort]["checks"][check_id]["candidates_per_1000_words"]
            - pair["human"]["checks"][check_id]["candidates_per_1000_words"]
            for pair in pairs
        ) / max(len(pairs), 1)
        per_check[check_id] = {
            "human_flags": human_flags, "ai_flags": ai_flags,
            "candidate_delta": round(candidate_delta, 3), "flag_gap": ai_flags - human_flags,
        }
    return {
        "n_pairs": len(pairs), "mean_surface_gap": round(sum(deltas) / max(len(deltas), 1), 3),
        "ai_higher": sum(delta > 0 for delta in deltas), "ties": sum(delta == 0 for delta in deltas),
        "human_higher": sum(delta < 0 for delta in deltas), "pair_deltas": deltas,
        "per_check": per_check,
    }


def run(manifest_path=DEFAULT_MANIFEST):
    grade = load_grade()
    manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    registry_ids = tuple(item["id"] for item in grade.registries.load_judgement()["records"])
    provenance_issues, semantic_issues, pairs = [], [], []
    started = time.perf_counter()
    for pair in manifest["pairs"]:
        output = {"topic": pair["topic"]}
        for cohort in ("human", "ai_fresh", "ai_rewrite"):
            meta = pair.get(f"{cohort}_metadata", {})
            if cohort != "human" and not meta.get("model"):
                provenance_issues.append(f"{pair['topic']}:{cohort}: model unspecified")
            semantic = pair.get(f"{cohort}_semantic")
            graded, error = grade_document(grade, resolve_sample(pair[cohort]), semantic, registry_ids)
            if error:
                semantic_issues.append(f"{pair['topic']}:{cohort}: {error}")
            output[cohort] = graded
        pairs.append(output)
    report = {
        "benchmark_status": "complete" if not provenance_issues and not semantic_issues else "incomplete",
        "manifest": str(Path(manifest_path).relative_to(ROOT)),
        "house_style_checks_excluded_from_separation": sorted(HOUSE_STYLE_CHECKS),
        "provenance_issues": provenance_issues, "semantic_issues": semantic_issues,
        "surface": {cohort: summarize(pairs, cohort) for cohort in ("ai_fresh", "ai_rewrite")},
        "semantic": None if semantic_issues else {},
        "performance": {"documents": len(pairs) * 3, "total_runtime_ms": round((time.perf_counter() - started) * 1000, 3)},
        "pairs": pairs,
    }
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    report = run(args.manifest.resolve())
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"benchmark_status": report["benchmark_status"], "surface": report["surface"], "performance": report["performance"]}, indent=2))
    return 0 if report["benchmark_status"] == "complete" else 2


if __name__ == "__main__":
    raise SystemExit(main())
