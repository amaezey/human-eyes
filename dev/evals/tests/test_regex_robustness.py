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
        "And honestly? That's amazing.",
        "The result?\nIt’s remarkable.",
    ],
}
for check_id, variants in mutation_cases.items():
    for variant in variants:
        result = grade.ALL_CHECKS[check_id](variant)
        if result["passed"] and not result["context_suppressed"]:
            raise AssertionError(f"{check_id} missed mutation variant: {variant!r}; {result['evidence']}")

navigation_metaphors = (
    "I kept the manual open as if it were a map out of the wilderness.",
    "The framework provides a roadmap through regulatory uncertainty.",
    "The guide became a compass through the administrative maze.",
)
for variant in navigation_metaphors:
    result = grade.ALL_CHECKS["no-nonliteral-land-surface"](variant)
    if result["passed"]:
        raise AssertionError(f"no-nonliteral-land-surface missed navigation metaphor: {variant!r}")
    assert_equal(result["candidate_count"], 1, f"navigation candidate evidence: {variant}")
    assert result["candidates"][0]["text"] in variant

lesson_frames = (
    "It taught me that not knowing was not a verdict.",
    "This experience taught me that preparation matters.",
    "What the failure taught me was that the review came too late.",
    "The lesson I learned was to ask before changing the corpus.",
)
for variant in lesson_frames:
    result = grade.ALL_CHECKS["no-manufactured-insight"](variant)
    if result["passed"]:
        raise AssertionError(f"no-manufactured-insight missed explicit lesson frame: {variant!r}")
    assert result["candidate_count"] >= 1

report_scaffolding = (
    "A major priority was research translation.\n\nAnother area of work was patient capital.",
    "The committee also examined regional access.\n\nThroughout the reporting period, members met monthly.",
)
for variant in report_scaffolding:
    result = grade.ALL_CHECKS["no-soft-scaffolding"](variant)
    if result["passed"]:
        raise AssertionError(f"no-soft-scaffolding missed repeated report openers: {variant!r}")
    assert result["candidate_count"] >= 2

importance_frames = (
    "The findings underline the value of regular relationships.",
    "The report underscores the importance of local knowledge.",
    "The results highlight the significance of the timing.",
    "The review emphasizes the importance of ownership.",
    "The review emphasises the importance of ownership.",
)
for variant in importance_frames:
    result = grade.ALL_CHECKS["no-significance-inflation"](variant)
    if result["passed"]:
        raise AssertionError(f"no-significance-inflation missed emphasis frame: {variant!r}")
    assert result["candidate_count"] >= 1

# Recognition is measured before document-level thresholds. A short sample can
# contain a valid triad candidate without constituting excessive triad density.
short_triad = "The plan covers research, design, and delivery."
triad_density = grade.ALL_CHECKS["no-triad-density"](short_triad)
assert triad_density["passed"]
assert_equal(triad_density["candidate_count"], 1, "short triad candidate extraction")
assert not triad_density["threshold_met"]
assert not grade.ALL_CHECKS["no-forced-triads"](short_triad)["passed"]

quoted_triad = 'The report quotes "research, design, and delivery" verbatim.'
quoted_result = grade.ALL_CHECKS["no-forced-triads"](quoted_triad)
assert not quoted_result["passed"]
assert_equal(quoted_result["candidate_count"], 1, "quoted triad remains detectable")
assert quoted_result["candidates"][0]["quoted"] is True

for variant in (
    "The work supports belonging, intimacy, and connection.",
    "The format relies on improvisation, sparring and discussion.",
    "The practice is designed, practised, and maintained.",
    "The process should be visible, versioned, and easy.",
    "Not perfectly, but more often, and with less hesitation.",
    "They know when to engage, how to respond, and when a decision closes.",
    "The constraints are cultural, social, and technical.",
    "They have to risk receiving, admitting limits, or letting someone else do it.",
    "Pleasure softens my edges, which makes service kinder and less controlling.",
    "We will travel less often, stay longer when we do, and use trains where they are practical.",
    "This is care for our relatives, for our budget, and for a climate every gathering depends on.",
):
    assert_equal(len(grade.extract_triad_candidates(variant)), 1, f"triad extraction: {variant}")

not_a_triad = "She answers quickly, smooths things over, and then wonders why life feels tight."
assert_equal(len(grade.extract_triad_candidates(not_a_triad)), 0, "narrative sequence exclusion")
modal_false_start = (
    "The proposal could work in theory, but fails to get sold in and implemented "
    "or is too generic for the context."
)
assert_equal(len(grade.extract_triad_candidates(modal_false_start)), 0, "modal clause boundary exclusion")
modal_relative_clause = (
    "The browser will detect if memory is running low, which we define as below 400MB, "
    "and suspend unused tabs."
)
assert_equal(len(grade.extract_triad_candidates(modal_relative_clause)), 0, "modal relative-clause exclusion")

# List recognition uses list blocks and item counts rather than allowing blank
# and prose lines to dilute a list-heavy document below an arbitrary ratio.
list_heavy_email = """Subject: Pilot feedback

Hello everyone,

The pilot includes:

- one named contact;
- current guides;
- a fortnightly session;
- equipment requests; and
- onboarding support.

Please consider:

1. What takes the most time?
2. Are the arrangements practical?
3. Which resources come first?
4. Could this create barriers?
5. Should the pilot continue?

Thank you.
"""
list_result = grade.ALL_CHECKS["no-excessive-lists"](list_heavy_email)
assert not list_result["passed"]
assert_equal(list_result["candidate_count"], 10, "list item recognition")

single_spaced_list = """Options:

- alpha

- beta

- gamma

- delta

- epsilon

- zeta

- eta

- theta

Choose one after the review.
"""
single_list_result = grade.ALL_CHECKS["no-excessive-lists"](single_spaced_list)
assert_equal(single_list_result["candidate_count"], 8, "spaced list item recognition")
assert "1 block(s)" in single_list_result["evidence"]

# Product-release performance promotion belongs to the promotional candidate
# surface even though the older vocabulary was mostly tourism-oriented.
product_promotion = (
    "The update makes browsing faster and more responsive, uses memory more efficiently, "
    "and produces smoother scrolling."
)
promotion_result = grade.ALL_CHECKS["no-promotional-language"](product_promotion)
assert not promotion_result["passed"]
assert promotion_result["candidate_count"] >= 3

# Compact interpretive paragraph closures are recognised structurally.  Two
# candidates remain visible below the existing three-ending document threshold.
tidy_structural = (
    "The editors omitted the longer work. The selection was already an interpretation.\n\n"
    "The translators polished the syntax. Difficulty became refinement; irony could sound sincere."
)
tidy_result = grade.ALL_CHECKS["no-tidy-paragraph-endings"](tidy_structural)
assert tidy_result["passed"]
assert_equal(tidy_result["candidate_count"], 2, "structural tidy-ending candidates")
assert_equal(
    grade.ALL_CHECKS["no-tidy-paragraph-endings"](tidy_structural.swapcase())["candidate_count"],
    2,
    "structural tidy-ending case invariance",
)

tidy_literal_control = (
    "The archivist checked the room. The manuscript was already on the desk.\n\n"
    "I chose a loaf tin if I felt cautious; a tray if I felt brave."
)
assert_equal(
    grade.ALL_CHECKS["no-tidy-paragraph-endings"](tidy_literal_control)["candidate_count"],
    0,
    "literal and subordinate tidy-ending controls",
)

# The shared extractor accepts punctuation and conjunction variants without
# allowing a single coordination to be counted more than once.
triad_variants = (
    "Research, design and delivery.",
    "Research, design, or delivery.",
    "RESEARCH, DESIGN, AND DELIVERY.",
)
for variant in triad_variants:
    assert_equal(len(grade.extract_triad_candidates(variant)), 1, f"triad extraction: {variant}")

# Thresholded checks consume the public catalogue rather than private literals.
for check_id in (
    "no-soft-scaffolding", "no-orphaned-demonstratives", "no-rhetorical-questions",
    "no-unicode-flair", "no-excessive-hedging", "no-tidy-paragraph-endings",
    "no-bland-critical-template", "no-rubric-echoing", "no-triad-density",
    "no-boldface-overuse", "no-inline-header-lists",
):
    assert check_id in grade.CHECK_THRESHOLDS

print(f"ALL PASSED: {len(rows)} corpus samples x {len(grade.ALL_CHECKS)} checks are case invariant")
