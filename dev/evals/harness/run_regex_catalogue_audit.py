#!/usr/bin/env python3
"""Measure per-check recall and false positives on the blind regex corpus."""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CORPUS = ROOT / "dev" / "evals" / "samples" / "regex-blind" / "claude-blind-seed.jsonl"
DEFAULT_REPORT = ROOT / "dev" / "evals" / "regex-catalogue-report.json"

TENDENCY_CHECKS = {
    "inflated significance": ("no-significance-inflation",),
    "hype": ("no-promotional-language",),
    "corporate jargon": ("no-corporate-ai-speak",),
    "vague authorities": ("no-vague-attributions",),
    "model knowledge disclaimers": ("no-knowledge-cutoff-disclaimers",),
    "filler": ("no-filler-phrases",),
    "hedging": ("no-excessive-hedging",),
    "fake balance": ("no-false-concession-hedges",),
    "manufactured profundity": ("no-manufactured-insight",),
    "performed candour": ("no-performed-candour",),
    "formulaic transitions/openers/endings": (
        "no-dramatic-transitions", "no-formulaic-openers", "no-signposted-conclusions",
    ),
    "contrastive/countdown negation": ("no-negative-parallelisms", "no-countdown-negation"),
    'repeated "This" openings': ("no-this-chains", "no-anaphora"),
    "shallow participial analysis": ("no-superficial-ing",),
    "vague demonstratives": ("no-orphaned-demonstratives",),
    "staccato": ("no-staccato-sequences",),
    "anaphora": ("no-anaphora",),
    "rhetorical questions": ("no-rhetorical-questions",),
    "triads": ("no-forced-triads", "no-triad-density"),
    "uniform rhythm and vocabulary": ("sentence-length-variance", "vocabulary-diversity"),
    "em dashes": ("no-em-dashes",),
    "em dash": ("no-em-dashes",),
    "decorative Unicode": ("no-unicode-flair",),
    "bold emphasis": ("no-boldface-overuse",),
    "bold-label lists": ("no-inline-header-lists",),
    "markdown headings": ("no-markdown-headings",),
    "heading in short text": ("no-markdown-headings",),
    "parenthetical headings": ("no-parenthetical-headings",),
    "repeated labels": ("no-section-scaffolding",),
    "excessive lists": ("no-excessive-lists",),
    "excessive list": ("no-excessive-lists",),
    "uniform paragraphs": ("paragraph-length-uniformity",),
    "tidy mini-conclusions": ("no-tidy-paragraph-endings",),
    "tidy conclusion": ("no-tidy-paragraph-endings", "no-signposted-conclusions"),
    "placeholders": ("no-placeholder-residue",),
    "assistant collaboration residue": ("no-collaborative-artifacts",),
}


def load_grade():
    spec = importlib.util.spec_from_file_location("grade", ROOT / "human-eyes" / "scripts" / "grade.py")
    grade = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise RuntimeError("Could not load human-eyes/scripts/grade.py")
    spec.loader.exec_module(grade)
    return grade


def ratio(numerator: int, denominator: int) -> float | None:
    return round(numerator / denominator, 3) if denominator else None


def audit(corpus: Path) -> dict:
    grade = load_grade()
    rows = [json.loads(line) for line in corpus.read_text(encoding="utf-8").splitlines() if line]
    per_check = defaultdict(lambda: {"violation_total": 0, "violation_detected": 0, "control_total": 0, "control_clear": 0})
    overall = {"violation_total": 0, "violation_detected": 0, "control_total": 0, "control_clear": 0}
    samples = []

    for row in rows:
        results = {check_id: check(row["text"]) for check_id, check in grade.ALL_CHECKS.items()}
        failed = sorted(check_id for check_id, result in results.items() if not result["passed"])
        expected = TENDENCY_CHECKS.get(row["primary_tendency"], ())
        target_hit = any(not results[check_id]["passed"] for check_id in expected)
        any_hit = any(check_id != "overall-signal-stacking" for check_id in failed)
        if row["label"] == "violation":
            overall["violation_total"] += 1
            overall["violation_detected"] += int(any_hit)
            for check_id in expected:
                per_check[check_id]["violation_total"] += 1
                per_check[check_id]["violation_detected"] += int(not results[check_id]["passed"])
        else:
            overall["control_total"] += 1
            overall["control_clear"] += int(not any_hit)
            for check_id in expected:
                per_check[check_id]["control_total"] += 1
                per_check[check_id]["control_clear"] += int(results[check_id]["passed"])
        samples.append({
            "id": row["id"], "label": row["label"], "primary_tendency": row["primary_tendency"],
            "expected_checks": list(expected), "target_detected": target_hit, "failed_checks": failed,
        })

    for metrics in per_check.values():
        metrics["recall"] = ratio(metrics["violation_detected"], metrics["violation_total"])
        metrics["specificity"] = ratio(metrics["control_clear"], metrics["control_total"])
        metrics["false_positive_rate"] = (
            round(1 - metrics["specificity"], 3) if metrics["specificity"] is not None else None
        )
    overall["recall"] = ratio(overall["violation_detected"], overall["violation_total"])
    overall["specificity"] = ratio(overall["control_clear"], overall["control_total"])
    overall["false_positive_rate"] = round(1 - overall["specificity"], 3)
    return {
        "corpus": str(corpus.relative_to(ROOT)),
        "note": "Seed corpus: one sample per tendency in many cells; rates are directional, not release gates.",
        "overall": overall,
        "per_check": dict(sorted(per_check.items())),
        "unmapped_tendencies": sorted({
            row["primary_tendency"]
            for row in rows
            if row["label"] == "violation" and row["primary_tendency"] not in TENDENCY_CHECKS
        }),
        "samples": samples,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--output", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    report = audit(args.corpus.resolve())
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"overall": report["overall"], "per_check": report["per_check"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
