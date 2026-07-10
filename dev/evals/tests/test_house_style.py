#!/usr/bin/env python3
"""Lint shipped human-eyes prose with the checks it instructs users to apply."""

import importlib.util
import json
import re
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


def instructional_prose(text):
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"(?m)^>.*$", "", text)
    text = re.sub(r"(?m)^\|.*\|\s*$", "", text)
    text = re.sub(r"`[^`]+`", "", text)
    return grade._mask_double_quoted_text(text)


files = [
    HUMAN_EYES / "references" / "voice.md",
    HUMAN_EYES / "references" / "process.md",
    HUMAN_EYES / "references" / "alternatives.md",
]
check_ids = {
    "no-performed-candour",
    "no-parenthetical-headings",
    "no-filler-phrases",
    "no-manufactured-insight",
    "no-formulaic-openers",
    "no-signposted-conclusions",
}
assert check_ids <= set(grade.ALL_CHECKS)

failures = []
for path in files:
    prose = instructional_prose(path.read_text())
    for check_id in check_ids:
        result = grade.ALL_CHECKS[check_id](prose)
        if not result["passed"]:
            failures.append(f"{path.name}: {check_id}: {result['evidence']}")

vocabulary = json.loads((HUMAN_EYES / "scripts" / "vocabulary.json").read_text())
template_prose = "\n".join(vocabulary["templates"].values())
for check_id in check_ids:
    result = grade.ALL_CHECKS[check_id](template_prose)
    if not result["passed"]:
        failures.append(f"vocabulary.json: {check_id}: {result['evidence']}")

combined = "\n".join(instructional_prose(path.read_text()).lower() for path in files)
for forbidden in (
    "introduce at least one register shift",
    "parenthetical doubt",
    "manufacture uncertainty",
    "invent personal",
):
    if forbidden in combined:
        failures.append(f"instructional prose contains forbidden directive: {forbidden}")

if failures:
    print("\n".join(f"FAIL: {failure}" for failure in failures))
    raise SystemExit(1)
print("ALL PASSED")
