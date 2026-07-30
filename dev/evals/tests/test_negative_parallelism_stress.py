#!/usr/bin/env python3
"""Focused stress test for the negative-parallelism detector."""

import importlib.util
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GRADE_PATH = ROOT.parent / "human-eyes" / "scripts" / "grade.py"
FIXTURE_PATH = Path(__file__).with_name("fixtures") / "negative_parallelism_stress.json"

spec = importlib.util.spec_from_file_location("human_eyes_grade", GRADE_PATH)
grade = importlib.util.module_from_spec(spec)
spec.loader.exec_module(grade)

fixture = json.loads(FIXTURE_PATH.read_text())
failures = []
category_totals = Counter()
category_passes = Counter()

for case in fixture["cases"]:
    category_totals[case["category"]] += 1
    result = grade.check_negative_parallelisms(case["text"])
    detected = not result["passed"]
    if detected == case["expected"]:
        category_passes[case["category"]] += 1
        continue
    failures.append(
        {
            "id": case["id"],
            "category": case["category"],
            "expected": case["expected"],
            "detected": detected,
            "text": case["text"],
            "matches": result.get("matches", []),
        }
    )

print(f"Cases: {len(fixture['cases'])}")
for category in sorted(category_totals):
    print(f"  {category}: {category_passes[category]}/{category_totals[category]}")

if failures:
    print(f"\nFAILED: {len(failures)} case(s)")
    for failure in failures:
        print(
            f"  {failure['id']} [{failure['category']}] "
            f"expected={failure['expected']} detected={failure['detected']}"
        )
        print(f"    text: {failure['text']}")
        print(f"    matches: {failure['matches']}")
    raise SystemExit(1)

print("\nALL PASSED")
