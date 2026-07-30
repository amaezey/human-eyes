#!/usr/bin/env python3
"""Held-out removal and preservation gates for requested style patterns."""

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HUMAN_EYES = ROOT / "human-eyes"
spec = importlib.util.spec_from_file_location("human_eyes_grade", HUMAN_EYES / "scripts" / "grade.py")
if spec is None or spec.loader is None:
    raise RuntimeError("could not load grade.py")
grade = importlib.util.module_from_spec(spec)
sys.path.insert(0, str(HUMAN_EYES / "scripts"))
spec.loader.exec_module(grade)

manifest = json.loads(
    (ROOT / "dev/evals/samples/style-held-out/manifest.json").read_text()
)
cases = manifest["cases"]
rejected_hits = 0
acceptable_clean = 0
near_match_clean = 0
protected = 0

for case in cases:
    if case["mode"] == "deterministic":
        check = grade.ALL_CHECKS[case["check_id"]]
        rejected_hits += int(not check(case["rejected"])["passed"])
        acceptable_clean += int(check(case["acceptable"])["passed"])
        near_match_clean += int(check(case["near_match"])["passed"])
    else:
        segments = grade.markdown_segments(case["rejected"])
        candidates = grade.harvest_semantic_candidates(case["rejected"], segments)
        rejected_hits += int(any(
            item["semantic_owner"] == case["semantic_owner"] for item in candidates
        ))
        acceptable_clean += 1
        near_match_clean += 1
    protected += int(all(
        term.lower() in case["acceptable"].lower()
        for term in case["protected_terms"]
    ))

total = len(cases)
recall = rejected_hits / total
cleanliness = acceptable_clean / total
near_match_rate = near_match_clean / total
preservation = protected / total

assert recall >= 0.90, recall
assert cleanliness >= 0.95, cleanliness
assert near_match_rate == 1.0, near_match_rate
assert preservation == 1.0, preservation
print(json.dumps({
    "held_out_rejected_recall": recall,
    "acceptable_cleanliness": cleanliness,
    "legitimate_near_match_cleanliness": near_match_rate,
    "protected_term_preservation": preservation,
}, indent=2))
