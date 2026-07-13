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
    HUMAN_EYES / "SKILL.md",
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
skill_text = (HUMAN_EYES / "SKILL.md").read_text().lower()
process_text = (HUMAN_EYES / "references" / "process.md").read_text().lower()
voice_text = (HUMAN_EYES / "references" / "voice.md").read_text().lower()
for required in (
    "no artefacts means no returned suggestion",
    "finding-count improvement cannot compensate for preservation failure",
    "treat the brief as a closed factual source",
    "never generate a blanket all-clear answer set",
    "the source is also a closed factual record",
):
    if required not in process_text:
        failures.append(f"process.md missing action completion guard: {required}")
for required in (
    "never claim or imply context validation when only the source was audited",
    "plausible standard procedure is still invented detail",
    "an improved finding set does not override failed preservation",
    "never bulk-fill semantic answers as clear",
    "do not insert audit commentary into the rewritten document",
):
    if required not in skill_text:
        failures.append(f"SKILL.md missing action completion guard: {required}")
for required in (
    "generic plausibility is not source support",
    "direct quotations are protected literals",
    "factual modality is protected meaning",
):
    if required not in voice_text:
        failures.append(f"voice.md missing preservation guard: {required}")
for forbidden in (
    "introduce at least one register shift",
    "parenthetical doubt",
    "manufacture uncertainty",
    "invent personal",
):
    for line in combined.splitlines():
        if forbidden in line and "do not" not in line and "never" not in line:
            failures.append(f"instructional prose contains forbidden directive: {forbidden}")

if failures:
    print("\n".join(f"FAIL: {failure}" for failure in failures))
    raise SystemExit(1)
print("ALL PASSED")
