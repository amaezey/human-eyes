#!/usr/bin/env python3
"""Lightweight coverage test for phrase capture across all flagged checks.

Runs grade.py against the noisy AI samples and verifies every flagged
check exposes either:
  - one or more `quoted_phrases` that substring-match the input, or
  - a `metric` string (for checks whose signal is a draft-wide
    measurement rather than a quotable span — see METRIC_ONLY_CHECKS), or
  - is in the STRUCTURAL_NO_PHRASE allow-list (signal is structural; no
    single span captures it).

Any flagged check outside those buckets is a phrase-capture gap. This
test is the gate that catches the class of bug where a regex-only check
flags but renders as a bare `<glyph> <name>` line with no evidence the
user can act on.

Run: python3 dev/evals/tests/test_phrase_capture_coverage.py
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
# The whole sample tree, not just generated-ai. Scoping this to one directory
# left the gate blind wherever a check only ever flags elsewhere in the corpus:
# `no-this-chains` flagged a pilot-additions document and rendered as a bare
# opener for as long as this test existed, because no generated-ai document
# triggered it.
SAMPLES = sorted(
    p for p in (ROOT / "dev" / "evals" / "samples").rglob("*")
    if p.is_file() and p.suffix in {".md", ".txt"}
)

_spec = importlib.util.spec_from_file_location("grade", ROOT / "human-eyes" / "scripts" / "grade.py")
grade = importlib.util.module_from_spec(_spec)
if _spec.loader is None:
    raise RuntimeError("Could not load human-eyes/scripts/grade.py")
_spec.loader.exec_module(grade)

# Checks whose signal is a draft-wide metric, not a quotable span. Each
# must surface a `metric` string in its result so the renderer shows
# `<glyph> <name>: <metric>` instead of a bare opener.
METRIC_ONLY_CHECKS = {
    "vocabulary-diversity",
    "paragraph-length-uniformity",
    "sentence-length-variance",
    "word-length-average",
    "concreteness-average",
}

# Checks whose signal is genuinely structural — no single phrase or
# scalar metric is informative. Bare-opener rendering is acceptable.
STRUCTURAL_NO_PHRASE: set[str] = set()

# Checks that compose a phrase from two spans instead of quoting one, so the
# verbatim substring rule below does not apply to them. They must still produce
# phrases; only the "occurs in the input" half is waived, with the reason.
COMPOSED_PHRASE_CHECKS = {
    # Renders "<heading>: <the one line under it>" — the pairing is the finding,
    # and neither half alone shows it.
    "no-heading-one-liners",
    # Renders the auxiliary and the participle as one span, so "were also asked"
    # is quoted as "were asked". The construction is the finding, not the words
    # between it.
    "no-passive-voice-rate",
}

# Known defect, named rather than waived quietly (DR-79). Lexical checks read a
# masked copy of the draft in which quoted and machine-readable spans are blanked
# to spaces, and they return matches cut from that copy. Where a match straddles
# a blanked span the quoted phrase carries a run of spaces that is not in the
# draft, so the report shows the reader prose with a hole in it. The fix is to
# recut every lexical match from the source text using the offsets that
# `_candidate_records` already computes; that is a change to the shared wrapper,
# not to this check, and it is not this test's to make.
MASKED_SPAN_ARTEFACT = {
    "no-manufactured-insight": (
        "quotes 'tim kreider is the author of<20 spaces>a collection of essays' "
        "on 21c-nyt-opinionator-i-know-what-you-think-of-me.md, where the gap is "
        "a masked span rather than the author's whitespace"
    ),
}

# Meta checks that the renderer suppresses entirely — they don't surface
# in the audit body so phrase capture is moot.
SUPPRESSED_FROM_RENDER = {
    "overall-signal-stacking",
}

FAILURES = []


def fail(msg: str) -> None:
    FAILURES.append(msg)
    print(f"FAIL: {msg}")


def ok(msg: str) -> None:
    print(f"  ok: {msg}")


def normalise(s: str) -> str:
    import re
    return re.sub(r"\s+", " ", s.lower()).strip()


print(f"=== phrase-capture coverage across {len(SAMPLES)} corpus samples ===\n")

flagged_seen: dict[str, list[str]] = {}
checks_without_phrases: dict[str, list[str]] = {}
artefact_seen: dict[str, list[str]] = {}

for sample in SAMPLES:
    text = sample.read_text(encoding="utf-8")
    norm_text = normalise(text)
    results = [grade.annotate_result(fn(text)) for fn in grade.ALL_CHECKS.values()]
    contract = grade.human_report(results)
    for c in contract["programmatic_checks"]:
        if c["status"] != "flagged":
            continue
        cid = c["id"]
        if cid in SUPPRESSED_FROM_RENDER:
            continue
        flagged_seen.setdefault(cid, []).append(sample.name)
        ev = c.get("evidence") or {}
        phrases = ev.get("quoted_phrases") or []
        metric = ev.get("metric")

        if cid in METRIC_ONLY_CHECKS:
            if not metric:
                fail(f"{cid} (metric-only) flagged on {sample.name} but no metric string in evidence")
            continue
        if cid in STRUCTURAL_NO_PHRASE:
            continue
        if not phrases:
            checks_without_phrases.setdefault(cid, []).append(sample.name)
            continue
        if cid in COMPOSED_PHRASE_CHECKS:
            continue
        # Verify at least one captured phrase substring-matches the input.
        if not any(normalise(p) in norm_text for p in phrases):
            if cid in MASKED_SPAN_ARTEFACT:
                artefact_seen.setdefault(cid, []).append(sample.name)
                continue
            fail(
                f"{cid} flagged on {sample.name}: phrases captured but none "
                f"substring-match input. First phrase: {phrases[0][:80]!r}"
            )

if checks_without_phrases:
    for cid, samples in sorted(checks_without_phrases.items()):
        fail(
            f"{cid} flagged but exposes no phrases on {len(samples)} sample(s) "
            f"(e.g. {samples[0]}). Either add phrase capture, or add to "
            f"METRIC_ONLY_CHECKS / STRUCTURAL_NO_PHRASE allow-list."
        )

# A pin only holds while it is still needed. One that stops firing is stale and
# fails, so the list cannot quietly outlive the defect it describes.
for cid, why in sorted(MASKED_SPAN_ARTEFACT.items()):
    if cid not in artefact_seen:
        fail(
            f"{cid} is pinned as quoting a masked span, but no sample shows it now. "
            f"Remove the pin. Stated reason was: {why}"
        )
    else:
        print(f"  pinned defect: {cid} on {len(artefact_seen[cid])} sample(s) — {why}")

if not FAILURES:
    print(f"\n{len(flagged_seen)} distinct check IDs flagged across the corpus; all carry phrases or metrics or are allow-listed.")

print("\n========================================")
if FAILURES:
    print(f"{len(FAILURES)} FAILURE(S)")
    sys.exit(1)
print("ALL PASSED")
