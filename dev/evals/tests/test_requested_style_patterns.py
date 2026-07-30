#!/usr/bin/env python3
"""Regression tests for the requested writing constraints."""

import importlib.util
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

expected_semantic = {
    "referential_clarity",
    "formulaic_parallelism",
    "semantic_redundancy",
    "underspecified_language",
    "context_leakage",
    "performed_candour",
    "vacuous_connection",
}
actual_semantic = {record["id"] for record in grade.registries.load_judgement()["records"]}
assert expected_semantic <= actual_semantic


def result(check_id, text):
    return grade.annotate_result(grade.ALL_CHECKS[check_id](text))


for bad in [
    "Honestly, the draft is late.",
    "To be honest, the draft is late.",
    "The honest answer is that the draft is late.",
    "Frankly, the draft is late.",
    "Candidly, the draft is late.",
    "Truthfully, the draft is late.",
]:
    assert not result("no-performed-candour", bad)["passed"], bad

for good in [
    "The policy requires an honest account of expenses.",
    'She wrote, "Honestly, the draft is late."',
]:
    assert result("no-performed-candour", good)["passed"], good

assert not result("no-parenthetical-headings", "## Document skills (the steady ones)\n")["passed"]
assert not result("no-parenthetical-headings", "Document skills (the steady ones)\n---\n")["passed"]
assert result("no-parenthetical-headings", "The document skills (the steady ones) need work.\n")["passed"]

assert not result("no-filler-phrases", "It is worth knowing about the exception.")["passed"]
assert not result("no-filler-phrases", "Worth noting, the exception applies.")["passed"]

candidate_text = (
    "# Options\n\n"
    "One method, many shapes.\n\n"
    "The framework uses the distinction, and the document repeats the framework.\n\n"
    "Where it fits, why you would use it, and how big or small it gets.\n"
)
bundle = grade.build_audit_work_bundle(
    candidate_text,
    [grade.annotate_result(check(candidate_text)) for check in grade.ALL_CHECKS.values()],
)
candidates = bundle["semantic_candidates"]
owners = {candidate["semantic_owner"] for candidate in candidates}
assert "formulaic_parallelism" in owners
assert "referential_clarity" in owners
assert "semantic_redundancy" in owners
assert all(candidate["text"] in candidate_text for candidate in candidates)
assert all(candidate["segment_id"] for candidate in candidates)

print("ALL PASSED")
