#!/usr/bin/env python3
"""Property and context tests for the deterministic prose catalogue."""

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CORPUS = ROOT / "dev" / "evals" / "samples" / "regex-blind" / "claude-blind-seed.jsonl"
spec = importlib.util.spec_from_file_location("grade", ROOT / "human-eyes" / "scripts" / "grade.py")
grade = importlib.util.module_from_spec(spec)
if spec.loader is None:
    raise RuntimeError("Could not load human-eyes/scripts/grade.py")
spec.loader.exec_module(grade)


def assert_equal(actual, expected, message):
    if actual != expected:
        raise AssertionError(f"{message}: expected {expected!r}, got {actual!r}")


rows = [json.loads(line) for line in CORPUS.read_text(encoding="utf-8").splitlines() if line]

# Case is not a prose-style signal. Every check must make the same decision for
# the original sample and an aggressively case-mutated version of that sample.
for row in rows:
    for check_id, check in grade.ALL_CHECKS.items():
        original = check(row["text"])
        mutated = check(row["text"].swapcase())
        assert_equal(mutated["passed"], original["passed"], f"{check_id} case invariance on {row['id']}")
        assert_equal(
            mutated["candidate_count"],
            original["candidate_count"],
            f"{check_id} candidate-count case invariance on {row['id']}",
        )
        assert_equal(
            mutated["context_suppressed"],
            original["context_suppressed"],
            f"{check_id} context case invariance on {row['id']}",
        )

# Every result separates recognition metadata from the final threshold decision.
for check_id, check in grade.ALL_CHECKS.items():
    result = check("A plain sentence used to inspect the result contract.")
    required = {
        "candidate_count", "candidates", "aggregate_finding", "threshold",
        "threshold_met", "context_suppressed",
    }
    missing = required - result.keys()
    if missing:
        raise AssertionError(f"{check_id} missing result-contract fields: {sorted(missing)}")
    assert_equal(result["threshold_met"], not result["passed"], f"{check_id} threshold consistency")

# Shared masking excludes examples and machine-readable material from lexical checks.
masked_examples = (
    'The style guide quotes "Here is what is really happening" as an example.\n\n'
    "The literal token `I hope this helps` appears in the test fixture.\n\n"
    "See https://example.test/it-is-important-to-note for the archived slug."
)
assert grade.ALL_CHECKS["no-manufactured-insight"](masked_examples)["passed"]
assert grade.ALL_CHECKS["no-collaborative-artifacts"](masked_examples)["passed"]

# High-confidence genre gates suppress formatting look-alikes but retain candidates.
recipe = "## Ingredients\n\n- Flour\n- Salt\n\n## Method\n\n1. Mix.\n2. Knead.\n3. Bake."
heading = grade.ALL_CHECKS["no-markdown-headings"](recipe)
assert heading["passed"] and heading["context_suppressed"] and heading["candidate_count"] > 0

report = "Revenue rose 6 percent year over year—driven by renewals—while operating margin held flat."
em_dash = grade.ALL_CHECKS["no-em-dashes"](report)
assert em_dash["passed"] and em_dash["context_suppressed"] and em_dash["candidate_count"] > 0

# Mutation families exercise the grammatical surface without exposing detector
# internals to the generators that created the blind corpus.
mutation_cases = {
    "no-performed-candour": [
        "I'll be honest, the battery is mediocre.",
        "Let us be real: the battery is mediocre.",
    ],
    "no-filler-phrases": [
        "It is worth recognising the contractual limit.",
        "It is worth recognizing the contractual limit.",
        "It is worth\nrecognizing the contractual limit.",
    ],
    "no-false-concession-hedges": [
        "On one hand, vegetables are nutritious; on the other hand, pizza tastes better.",
        "On the other hand, pizza tastes better; on the one hand, vegetables are nutritious.",
    ],
    "no-corporate-ai-speak": [
        "Let's circle back and move the needle on delivery.",
        "We can leverage cross-team synergies before the review.",
        "The plan leverages a cross-team synergy before the review.",
    ],
    "no-rhetorical-questions": [
        "Why does this matter? Because costs doubled. What changed? The supplier withdrew.",
        "Why does this matter?\nBecause costs doubled.\nWhat changed?\nThe supplier withdrew.",
    ],
    "no-markdown-headings": [
        "## Background\n\nGeneric prose follows.",
        "Background\n==========\n\nGeneric prose follows.",
    ],
}
for check_id, variants in mutation_cases.items():
    for variant in variants:
        result = grade.ALL_CHECKS[check_id](variant)
        if result["passed"] and not result["context_suppressed"]:
            raise AssertionError(f"{check_id} missed mutation variant: {variant!r}; {result['evidence']}")

print(f"ALL PASSED: {len(rows)} corpus samples x {len(grade.ALL_CHECKS)} checks are case invariant")
