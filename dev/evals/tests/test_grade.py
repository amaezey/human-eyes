#!/usr/bin/env python3
"""Self-tests for grade.py checks.

Each check gets known-bad text (must fail) and known-clean text (must pass).
If any assertion is wrong, the check's regex/logic has a bug.

Run: python3 evals/test_grade.py
"""

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
_spec = importlib.util.spec_from_file_location("grade", ROOT / "human-eyes" / "scripts" / "grade.py")
_grade = importlib.util.module_from_spec(_spec)
if _spec.loader is None:
    raise RuntimeError("Could not load human-eyes/scripts/grade.py")
_spec.loader.exec_module(_grade)

ALL_CHECKS = _grade.ALL_CHECKS

# CHECK_METADATA was removed from grade.py in U7 (audit-report redesign).
# Reconstruct the four-field metadata view from human-eyes/scripts/patterns.json so the
# severity-propagation and failure-mode meta-tests below keep working.
import json as _json
_patterns_data = _json.loads((ROOT / "human-eyes" / "scripts" / "patterns.json").read_text())
CHECK_METADATA = {
    _cid: {k: _rec[k] for k in ("severity", "failure_modes", "evidence_role", "guidance")}
    for _cid, _rec in _patterns_data.items()
    if not _cid.startswith("_")  # skip _meta, _extra_entries (page-level content)
}
annotate_result = _grade.annotate_result
failure_mode_results = _grade.failure_mode_results
format_two_layer = _grade.format_two_layer
friendly_evidence = _grade.friendly_evidence
human_report = _grade.human_report
depth_results = _grade.depth_results
score_summary = _grade.score_summary
triggered_checks = _grade.triggered_checks

FAILURES = 0


def expect_fail(check_name, text, reason):
    """Assert that the check FAILS on this text."""
    global FAILURES
    result = ALL_CHECKS[check_name](text)
    if result["passed"]:
        FAILURES += 1
        print(f"FAIL: {check_name} should have failed on: {reason}")
        print(f"  Evidence: {result['evidence']}")
    else:
        print(f"  ok: {check_name} correctly fails on: {reason}")


def expect_pass(check_name, text, reason):
    """Assert that the check PASSES on this text."""
    global FAILURES
    result = ALL_CHECKS[check_name](text)
    if not result["passed"]:
        FAILURES += 1
        print(f"FAIL: {check_name} should have passed on: {reason}")
        print(f"  Evidence: {result['evidence']}")
    else:
        print(f"  ok: {check_name} correctly passes on: {reason}")


def expect_depth_status(results, depth, status, reason):
    """Assert depth_results reports the expected status."""
    global FAILURES
    actual = depth_results(results)[depth]["check_status"]
    if actual != status:
        FAILURES += 1
        print(f"FAIL: {depth} check_status should be {status} for {reason}; got {actual}")
    else:
        print(f"  ok: {depth} check_status is {status} for {reason}")


def expect_depth_actions(results, depth, required_fixes, preservable, reason):
    """Assert depth_results reports the expected action buckets."""
    global FAILURES
    actual = depth_results(results)[depth]
    failed = False
    if actual["required_fixes"] != required_fixes:
        FAILURES += 1
        failed = True
        print(f"FAIL: {depth} required_fixes should be {required_fixes} for {reason}; got {actual['required_fixes']}")
    if actual["preservable_with_disclosure"] != preservable:
        FAILURES += 1
        failed = True
        print(f"FAIL: {depth} preservable_with_disclosure should be {preservable} for {reason}; got {actual['preservable_with_disclosure']}")
    if actual["user_decision_needed"] != preservable:
        FAILURES += 1
        failed = True
        print(f"FAIL: {depth} user_decision_needed should be {preservable} for {reason}; got {actual['user_decision_needed']}")
    if not failed:
        print(f"  ok: {depth} action buckets match for {reason}")


# --- no-em-dashes ---

print("\n=== no-em-dashes ===")
expect_fail("no-em-dashes",
    "I'm still keen to connect\u2014would Tuesday work?",
    "em dash in sentence")
expect_pass("no-em-dashes",
    "I'm still keen to connect - would Tuesday work?",
    "hyphen, not em dash")
em_dash_results = [
    annotate_result(ALL_CHECKS["no-em-dashes"]("I'm still keen to connect\u2014would Tuesday work?"))
]
expect_depth_status(em_dash_results, "balanced", "fail", "em dash is a strong 2026 signal at Balanced depth")
expect_depth_status(em_dash_results, "all", "fail", "em dash is never allowed at All depth")


# --- no-ai-vocabulary-clustering ---

print("\n=== no-ai-vocabulary-clustering ===")
expect_fail("no-ai-vocabulary-clustering",
    "The intricate landscape fosters a vibrant tapestry of culture.",
    "5 AI words in one paragraph")
expect_fail("no-ai-vocabulary-clustering",
    "This aligns with the broader landscape of fostering innovation.",
    "'aligns with' (inflected) + landscape + fostering = 3")
expect_pass("no-ai-vocabulary-clustering",
    "The project improves access to clean water in rural areas.",
    "no AI vocabulary")
expect_pass("no-ai-vocabulary-clustering",
    "This aligns with our goals. In a separate paragraph.\n\nThe landscape is flat.",
    "'aligns with' and 'landscape' in different paragraphs (max 1 per para)")
expect_fail("no-ai-vocabulary-clustering",
    "The seamless integration genuinely fosters a transformative experience.",
    "'seamless' + 'genuinely' + 'fosters' + 'transformative' = 4 AI words")
expect_fail("no-ai-vocabulary-clustering",
    "The study will provide a valuable insight, offer a valuable framework, and leave a lasting mark.",
    "3 GPTZero high-ratio phrases in one paragraph")
expect_pass("no-ai-vocabulary-clustering",
    "I actually went to the store and bought some hidden gems of local produce.",
    "'actually' without filler pattern and 'hidden' without significance pattern are not flagged")
expect_fail("no-ai-vocabulary-clustering",
    "The argument landed flat, and what surfaces in the discussion is a nuanced understanding of trust.",
    "nonliteral landed + surface + nuanced")
expect_pass("no-ai-vocabulary-clustering",
    "The plane landed safely on the island, and the table surface was scratched.",
    "literal land/surface usage")


# --- no-nonliteral-land-surface ---

print("\n=== no-nonliteral-land-surface ===")
expect_fail("no-nonliteral-land-surface",
    "The lesson shows students where their thinking landed and what to revise.",
    "nonliteral thinking landed")
expect_fail("no-nonliteral-land-surface",
    "What surfaced in the draft was a clearer argument.",
    "nonliteral surfaced in draft")
expect_fail("no-nonliteral-land-surface",
    "The grade tells students where they landed in the mark scheme.",
    "nonliteral pronoun landed in abstract scale")
expect_fail("no-nonliteral-land-surface",
    "The paper landed on the marking scale, but the student still needed advice.",
    "nonliteral paper landed on marking scale")
expect_fail("no-nonliteral-land-surface",
    "A grade tells a learner where a piece of work landed on a scale.",
    "nonliteral piece of work landed on scale")
expect_fail("no-nonliteral-land-surface",
    "Student work landed against the rubric, but the comment gave no next step.",
    "nonliteral student work landed against rubric")
expect_fail("no-nonliteral-land-surface",
    "A grade tells a student where a piece of work landed in the scoring system.",
    "nonliteral piece of work landed in scoring system")
expect_fail("no-nonliteral-land-surface",
    "The joke lands with the audience because the setup is familiar.",
    "nonliteral lands with audience")
expect_fail("no-nonliteral-land-surface",
    "I kept the manual open beside me as if it were a map out of the wilderness.",
    "nonliteral manual as map out of wilderness")
expect_fail("no-nonliteral-land-surface",
    "The framework provides a roadmap through regulatory uncertainty.",
    "nonliteral framework as roadmap through uncertainty")
expect_fail("no-nonliteral-land-surface",
    "The guide became a compass through the administrative maze.",
    "nonliteral guide as compass through maze")
expect_pass("no-nonliteral-land-surface",
    "The plane landed safely on the island, and the table surface was scratched.",
    "literal landed and physical surface")
expect_pass("no-nonliteral-land-surface",
    "The paper landed on the desk and slid under the notebook.",
    "literal paper landed on desk")
expect_pass("no-nonliteral-land-surface",
    "The map showed a route through the wilderness, and the compass pointed north.",
    "literal navigation through wilderness")
expect_pass("no-nonliteral-land-surface",
    "The manual included a map of the national park.",
    "manual containing a literal map")
expect_pass("no-nonliteral-land-surface",
    "The product roadmap lists three scheduled releases.",
    "literal planning roadmap")


# --- overall-signal-stacking ---

print("\n=== overall-signal-stacking ===")
expect_pass("overall-signal-stacking",
    (
        "This clinical covid antiviral study additionally aims to address "
        "challenges and enhance outcomes. The analysis underscores advancements, "
        "acknowledges limitations, and offers a comprehensive approach for "
        "patients receiving therapeutic intervention."
    ),
    "Kobak-heavy academic vocabulary alone is supporting evidence, not a failure")
expect_pass("overall-signal-stacking",
    (
        "The clinic tested an antiviral drug in patients with covid. Fever fell "
        "after two days, and three patients left the ward by Friday."
    ),
    "biomedical content without style signal stacking")
expect_pass("overall-signal-stacking",
    (
        "The essay additionally aims to address challenges and enhance outcomes. "
        "The analysis underscores advancements and offers a comprehensive approach "
        "for readers."
    ),
    "style words without other AI-ish structure")
expect_fail("overall-signal-stacking",
    (
        "## Overview\n\n"
        "At its core, this clinical covid antiviral study is not just about "
        "treatment, but about navigating the complex landscape of patient trust. "
        "The analysis underscores advancements, acknowledges limitations, and "
        "offers a comprehensive approach for patients receiving therapeutic "
        "intervention. The takeaway is clear: this marks a pivotal moment.\n\n"
        "## Implications\n\n"
        "At its core, the work is less about data than about transformation. "
        "That is why the findings continue to inspire a deeper understanding."
    ),
    "Kobak signals plus vocabulary, headings, formulaic openers, tidy endings, and reframes")


# --- no-manufactured-insight ---

print("\n=== no-manufactured-insight ===")
expect_fail("no-manufactured-insight",
    "Here's the thing: nobody actually reads the manual.",
    "here's the thing")
expect_fail("no-manufactured-insight",
    "What's really happening is a shift in power.",
    "what's really")
expect_fail("no-manufactured-insight",
    "What no one is talking about is how this changed the market.",
    "what no one is talking about")
expect_fail("no-manufactured-insight",
    "When no one noticed, the tool quietly became the default.",
    "when no one noticed framing")
expect_fail("no-manufactured-insight",
    "The shift nobody noticed was already underway.",
    "shift nobody noticed framing")
expect_fail("no-manufactured-insight",
    "It taught me that not knowing was not a verdict.",
    "explicit it-taught-me lesson frame")
expect_fail("no-manufactured-insight",
    "This experience taught me that preparation matters.",
    "explicit experience-taught-me lesson frame")
expect_fail("no-manufactured-insight",
    "What the failure taught me was that the review came too late.",
    "explicit what-this-taught-me lesson frame")
expect_fail("no-manufactured-insight",
    "The lesson I learned was to ask before changing the corpus.",
    "explicit lesson-learned frame")
expect_fail("no-manufactured-insight",
    "Symmetry is the language of trust.",
    "DR-124 aphorism formula: X is the Y of Z")
expect_fail("no-manufactured-insight",
    "Efficiency becomes a trap when teams forget the goal.",
    "DR-124 aphorism formula: X becomes a trap")
expect_fail("no-manufactured-insight",
    "Trust is the currency of leadership.",
    "DR-124 aphorism formula: the currency of")
expect_fail("no-manufactured-insight",
    "The architecture of belonging shapes the campaign.",
    "DR-124 aphorism formula: the architecture of")
expect_fail("no-manufactured-insight",
    "Teams speak in the language of continuous improvement.",
    "DR-124 aphorism formula: standalone the language of")
expect_fail("no-manufactured-insight",
    "Routine can become a trap.",
    "DR-124 aphorism formula: X become a trap")
aphorism_result = ALL_CHECKS["no-manufactured-insight"](
    "Symmetry is the language of trust."
)
if aphorism_result.get("matches") != ["symmetry is the language of trust"]:
    FAILURES += 1
    print(
        "FAIL: DR-124 overlapping aphorism regexes should keep the longest occurrence, "
        f"got {aphorism_result.get('matches', [])}"
    )
else:
    print("  ok: DR-124 overlapping aphorism regexes keep the longest occurrence")
for phrase in (
    "This is the part most people skip.",
    "Most people won't tell you this.",
    "Nobody's talking about this.",
    "Everyone's sleeping on this.",
    "This flew under the radar.",
    "I wasn't supposed to share this, but here it is.",
    "What they don't want you to know:",
    "The thing nobody tells beginners:",
    "The secret that advertising doesn't want you to know:",
    "I've been sitting on this for weeks.",
):
    expect_fail("no-manufactured-insight", phrase,
        f"DR-135C false-exclusivity hook: {phrase}")
for phrase in (
    "Stop what you're doing.",
    "Drop everything.",
    "Read this before your next meeting.",
    "If you haven't seen this yet...",
    "You're going to want to bookmark this.",
    "Save this before it gets taken down.",
    "This changes everything.",
    "This is bigger than people realize.",
    "Email just changed the game forever.",
):
    expect_fail("no-manufactured-insight", phrase,
        f"DR-135D manufactured-urgency hook: {phrase}")
for phrase in (
    "Sit with that for a second.",
    "I'll say it louder for the people in the back.",
):
    expect_fail("no-manufactured-insight", phrase,
        f"DR-135F performed-emphasis frame: {phrase}")
expect_fail("no-performed-candour",
    "The honest answer is that the data was incomplete from the start.",
    "performed candour — 'the honest answer is'")
expect_fail("no-performed-candour",
    "Here's the honest framing: the project missed every milestone.",
    "performed candour — 'here's the honest framing'")
expect_fail("no-performed-candour",
    "Here's the real truth — most teams skip retros entirely.",
    "performed candour — 'here's the real truth'")
expect_fail("no-performed-candour",
    "If I'm being honest, the proposal needs more work.",
    "performed candour — 'if I'm being honest'")
expect_fail("no-performed-candour",
    "In all honesty, the migration plan has too many unknowns.",
    "performed candour — 'in all honesty'")
for phrase in (
    "I wasn't going to post this, but here it is.",
    "This is scary to share.",
    "Hot take incoming (don't hate me):",
    "Unpopular opinion:",
    "I know I'll get hate for this, but the plan is wrong.",
    "I've never said this publicly before.",
    "This might ruffle some feathers.",
    "I might lose followers for this, but the deadline matters.",
):
    expect_fail("no-performed-candour", phrase,
        f"DR-135G performed-vulnerability frame: {phrase}")
expect_pass("no-manufactured-insight",
    "The manual was updated in 2024 to reflect new safety standards.",
    "plain factual statement")
expect_pass("no-manufactured-insight",
    "We strive to be honest about our limitations and update the docs as we learn.",
    "'to be honest' without leading comma — not the AI tell")
expect_pass("no-manufactured-insight",
    "The teacher taught me algebra.",
    "literal instruction")
expect_pass("no-manufactured-insight",
    "The manual taught me how to replace the battery.",
    "concrete procedural learning")
expect_pass("no-manufactured-insight",
    "The course taught me three statistical methods.",
    "concrete course content")


# --- no-staccato-sequences ---

print("\n=== no-staccato-sequences ===")
expect_fail("no-staccato-sequences",
    "It works. It really works. Trust me. I know this.",
    "4 consecutive short sentences")
expect_pass("no-staccato-sequences",
    "The library was built in 1923 and has served the community ever since.",
    "one long sentence")
for phrase in (
    "Too young. Too single.",
    "The agency told her she was too young. Too single. Too inexperienced.",
    "No family. No calls.",
):
    expect_fail("no-staccato-sequences", phrase,
        f"DR-19A repeated short-fragment opener pair: {phrase}")
expect_pass("no-staccato-sequences",
    "Too young. Still uncertain.",
    "two short fragments with different opening words")
for phrase in (
    "Full stop.",
    "Period.",
    "That's it. That's the tweet.",
    "Trust. That's the word.",
):
    expect_fail("no-staccato-sequences", phrase,
        f"DR-135F exact dramatic-fragment formula: {phrase}")


# --- no-anaphora ---

print("\n=== no-anaphora ===")
expect_fail("no-anaphora",
    "Every morning I run. Every morning I stretch. Every morning I eat.",
    "3 sentences starting with 'every'")
expect_pass("no-anaphora",
    "First I run. Then I stretch. After that I eat breakfast with coffee.",
    "varied sentence starts")


# --- no-collaborative-artifacts ---

print("\n=== no-collaborative-artifacts ===")
expect_fail("no-collaborative-artifacts",
    "I hope this helps with your project!",
    "I hope this helps")
expect_fail("no-collaborative-artifacts",
    "If needed, the explanation can be reframed for a policy audience.",
    "soft offer-to-continue")
expect_fail("no-collaborative-artifacts",
    "Feel free to reach out if you have questions.",
    "feel free to")
expect_fail("no-collaborative-artifacts",
    "Let's break it down so the main idea is clear.",
    "assistant explainer framing")
expect_fail("no-collaborative-artifacts",
    "Would you like me to make this more concise?",
    "assistant follow-up offer")
expect_fail("no-collaborative-artifacts",
    "Let me know if you want a shorter version.",
    "assistant continuation request")
expect_pass("no-collaborative-artifacts",
    "Would you like to know what makes his style such a pleasure to read?",
    "ordinary article question")
expect_pass("no-collaborative-artifacts",
    "The founder is pictured with a glass of champagne, of course!",
    "ordinary aside, not assistant residue")
expect_pass("no-collaborative-artifacts",
    "The bridge was completed in 1937 after four years of construction.",
    "plain factual statement")


# --- no-curly-quotes ---

print("\n=== no-curly-quotes ===")
expect_fail("no-curly-quotes",
    "She said \u201chello\u201d to the crowd.",
    "curly double quotes")
expect_pass("no-curly-quotes",
    'She said "hello" to the crowd.',
    "straight quotes")


# --- sentence-length-variance ---

print("\n=== sentence-length-variance ===")
expect_fail("sentence-length-variance",
    "I went home after work. She went home after work. We all went home after work. They went home after work too. Everyone left work early today. He went home after work as well. They all went home after that. We went together after the meeting. She came along with the team. He tagged along with us too. I drove home alone after. She took the bus home today. We all ended up leaving early. They went to get some food first. Everyone was tired from work today. He walked all the way back home. They caught the train after five.",
    "uniform short sentences, low variance, 17 sentences over 100 words")
expect_pass("sentence-length-variance",
    "I went home. The extraordinarily complex municipal infrastructure project that had been debated for nearly a decade was finally approved by the city council after a marathon session. Yes. The report covered demographic shifts across three continents over a forty-year period using novel statistical methods.",
    "high variance between short and long")
expect_pass("sentence-length-variance",
    "Thanks for the invite. I can't make Tuesday but could do Thursday afternoon.",
    "short-form text skipped (under 100 words, under 6 sentences)")

# DR-79B: #25 gains a mean-sentence-length branch at 15 words, in prose of 300
# words or more. Sentences here are uniformly mid-length, so no run, repeated
# opener, formula, or ten-word-or-fewer rate fires; only the mean does.
_flat_mid_length = (
    "The committee reviewed the revised funding proposal at its ordinary meeting on Tuesday afternoon. "
    "Members asked detailed questions about the delivery timeline and the projected costs over three years. "
    "The chair confirmed that the capital grant had been secured in early March this year. "
    "Several members raised concerns about how the public consultation arrangements had been organised locally. "
    "Officers agreed to publish the full set of written responses at some point next month. "
    "A final vote on the proposal was deferred until the next ordinary council meeting. "
    "Residents across the affected wards will be notified as soon as a date is fixed. "
    "All supporting papers for the item remain available on the council website until then. "
    "A second report on the same subject is expected before the summer recess begins. "
    "The committee will meet again in the autumn to consider that report in detail. "
    "Officers have already started drafting the supporting technical annexes for the second report. "
    "The chair thanked all attending members for sitting through an unusually long evening session. "
    "Minutes of the meeting were circulated to every attendee on the following working morning. "
    "Two members submitted written corrections to those minutes within the agreed seven day window. "
    "The corrected minutes were later approved without any further discussion at the following meeting. "
    "Budget monitoring reports will follow exactly the same publication schedule as in previous years. "
    "The finance officer confirmed the reporting dates for the coming financial year in writing. "
    "No member present objected to the proposed schedule of committee meetings for next year. "
    "The chair formally closed the meeting shortly after four o'clock in the afternoon. "
    "Light refreshments had been provided in the adjoining committee room an hour beforehand. "
    "Each future agenda will be published fourteen clear days before the meeting it covers. "
    "Members were reminded to declare any relevant financial interests well in advance of business. "
    "The clerk will circulate the standing declaration form to all members again shortly. "
    "Late declarations must be made verbally at the very start of the meeting business. "
    "The deputy chair will take the next meeting because of a diary clash. "
    "Apologies for absence had been received from two members before the meeting began."
)
expect_fail("no-staccato-sequences", _flat_mid_length,
    "DR-79B mean sentence length below 15 in prose of 300+ words")

# DR-79A: the old threshold of 4 sat underneath the whole observed range, so
# the check never fired on real prose. At 9 it separates the corpora. These two
# fixtures bracket the new boundary; both were inert under the old threshold.
_narrow_band = (
    "The council met on Tuesday to review the proposal. Members asked about "
    "the budget and the timeline for delivery. The chair explained that "
    "funding had been secured in March. Several members raised concerns about "
    "the consultation process. Officers agreed to publish the responses next "
    "month. The vote was deferred until the next ordinary meeting. Residents "
    "will be notified once a date has been fixed. The papers remain available "
    "on the council website for now. A second report is expected before the "
    "summer recess begins. The committee will meet again in the autumn to "
    "review it. Officers have already begun drafting the supporting annexes. "
    "The chair thanked everyone for attending the long session."
)
expect_fail("sentence-length-variance", _narrow_band,
    "DR-79A sentences clustered in one length band (SD between 4 and 9)")
_varied_band = (
    "The council met. Members asked about the budget, the timeline for "
    "delivery, the consultation process that had run over the winter, and "
    "whether the funding secured in March would still cover the revised "
    "scope of works now that three contractors had withdrawn. The chair "
    "explained. Officers agreed to publish every response received during "
    "the consultation period alongside a summary of the themes raised, and "
    "to circulate that document to all members a fortnight before the next "
    "ordinary meeting so that nobody would arrive unprepared. It was "
    "deferred. Residents will be notified."
)
expect_pass("sentence-length-variance", _varied_band,
    "DR-79A genuinely varied sentence lengths stay clear at the new threshold")


# --- no-promotional-language ---

print("\n=== no-promotional-language ===")
expect_fail("no-promotional-language",
    "The stunning views and vibrant culture make this a must-visit destination.",
    "stunning + vibrant + must-visit")
expect_fail("no-promotional-language",
    "The editor called it one of the best options available.",
    "DR-100 exact one-of-the-best promotional formula")
expect_fail("no-promotional-language",
    "There are so many possibilities for the project.",
    "DR-100 exact so-many-possibilities promotional formula")
for phrase in (
    "Every challenge is an opportunity.",
    "Each setback becomes a lesson.",
    "Every difficulty is a chance.",
    "Every problem has a silver lining.",
    "Each challenge has a silver lining.",
):
    expect_fail("no-promotional-language", phrase,
        f"DR-21D motivational-poster formula: {phrase}")
expect_pass("no-promotional-language",
    "It is one of the best-known examples in the archive.",
    "hyphenated best-known phrase is not the approved formula")
expect_pass("no-promotional-language",
    "The team treated the challenge as an opportunity to revise the plan.",
    "ordinary challenge and opportunity wording outside the formula")
expect_pass("no-promotional-language",
    "The report describes the silver lining around the storm cloud.",
    "literal silver-lining discussion outside the formula")
expect_pass("no-promotional-language",
    "The hotel is on a quiet street near the old quarter.",
    "neutral description")


# --- no-significance-inflation ---

print("\n=== no-significance-inflation ===")
expect_fail("no-significance-inflation",
    "This marked a pivotal moment in the evolving landscape of regional policy.",
    "pivotal + evolving landscape")
expect_fail("no-significance-inflation",
    "The findings underline the value of regular primary-care relationships.",
    "underline the value of")
expect_fail("no-significance-inflation",
    "The report underscores the importance of local knowledge.",
    "underscores the importance of")
expect_fail("no-significance-inflation",
    "The results highlight the significance of the timing.",
    "highlight the significance of")
expect_fail("no-significance-inflation",
    "The review emphasises the importance of clear ownership.",
    "British emphasises the importance of")
for phrase in (
    "The phenomenon generated debate about authenticity and consent.",
    "These works shaped emerging policy discussions about ownership.",
    "The project contributes to the broader history of aviation.",
    "The studies demonstrate ongoing relevance and lasting influence.",
    "The policy had enduring impacts on the region.",
):
    expect_fail("no-significance-inflation", phrase,
        f"DR-22A significance formula: {phrase}")
expect_pass("no-significance-inflation",
    "The policy was introduced in 2019 and applied to three regions.",
    "plain factual")
expect_pass("no-significance-inflation",
    "Underline the heading and highlight the affected row.",
    "literal document-formatting instructions")
expect_pass("no-significance-inflation",
    "The report uses underlining for new terms.",
    "literal typographic description")


# --- no-negative-parallelisms ---

print("\n=== no-negative-parallelisms ===")
expect_fail("no-negative-parallelisms",
    "It's not just about money, but about dignity.",
    "not just...but")
expect_fail("no-negative-parallelisms",
    "Learning to cook is not about becoming a chef. It is about reclaiming a fundamental capability.",
    "cross-sentence not about X. It is about Y")
expect_fail("no-negative-parallelisms",
    "Travel is less about new places than about testing yourself.",
    "is less about X than about Y")
expect_fail("no-negative-parallelisms",
    "The essay is a question of identity, not logistics.",
    "reversed Y, not X reframe")
expect_fail("no-negative-parallelisms",
    "The app is more about trust than convenience.",
    "more about Y than X reframe")
expect_fail("no-negative-parallelisms",
    "Not so much a tool as a partner.",
    "not so much X as Y")
expect_fail("no-negative-parallelisms",
    "You might think this is about speed. Actually, it is about trust.",
    "correction frame with abstract reveal")
expect_fail("no-negative-parallelisms",
    "No polish. No gimmicks. Just substance.",
    "No X. No Y. Just Z countdown")
expect_fail("no-negative-parallelisms",
    "Beyond convenience, the product is about connection.",
    "beyond X, about Y reframe")
expect_fail("no-negative-parallelisms",
    "It isn't merely a song; it's a statement.",
    "contraction plus merely variant")
expect_fail("no-negative-parallelisms",
    "It's not delivery. It's DiGiorno.",
    "canonical contraction split across two sentences")
expect_fail("no-negative-parallelisms",
    "The target was never a man. The target was the truth.",
    "repeated-subject negative parallelism across two sentences")
expect_fail("no-negative-parallelisms",
    "This isn't a feature. It is a relationship.",
    "deictic-pronoun negative parallelism across two sentences")
expect_fail("no-negative-parallelisms",
    "No bag, no things, no armor, just me.",
    "comma-separated no-X no-Y just-Z")
expect_fail("no-negative-parallelisms",
    "The fault is not in our stars, but in ourselves.",
    "not-X but-Y parallel contrast")
expect_fail("no-negative-parallelisms",
    "I come to bury Caesar, not to praise him.",
    "affirmative-negative infinitive parallelism")
expect_fail("no-negative-parallelisms",
    "Stop thinking of it as a tool. Start thinking of it as a partner.",
    "stop-X start-Y reversal")
expect_fail("no-negative-parallelisms",
    "Email isn't the future. Messaging is.",
    "X-is-not-the-future Y-is reversal")
expect_fail("no-negative-parallelisms",
    "SEO is dead. Community is what's next.",
    "X-is-dead Y-is-next reversal")
expect_fail("no-negative-parallelisms",
    "Forget reach. Focus on retention.",
    "forget-X focus-on-Y reversal")
_dr137_source_structures = (
    "Credit card fraud isn’t just evolving—it’s accelerating!",
    "The teams who will thrive now aren’t just using AI for speed. They’re combining it with judgment.",
    "Atlas didn’t shrug. He drilled.",
    "*AI doesn’t eliminate labor; it redistributes it.*",
    "Not performative updates—but real transparency that restores confidence.",
    "The strategy prioritizes empirical consolidation rather than ideological purity.",
)
for phrase in _dr137_source_structures:
    result = ALL_CHECKS["no-negative-parallelisms"](phrase)
    if result.get("passed") or result.get("candidate_count") != 1:
        FAILURES += 1
        print(
            "FAIL: DR-137 source structure should return one #9 candidate; "
            f"got {result} for {phrase}"
        )
    else:
        print(f"  ok: DR-137 source structure returns one #9 candidate: {phrase}")
for separator in (",", ":", ";", "-", "–", "—"):
    expect_fail(
        "no-negative-parallelisms",
        f"Not performative updates{separator} but real transparency.",
        f"DR-137 not-X-but-Y separator variant: {separator}",
    )
_two_rather_than_frames = ALL_CHECKS["no-negative-parallelisms"](
    "Choose evidence rather than polish. Prefer specifics rather than slogans."
)
if _two_rather_than_frames.get("candidate_count") != 2:
    FAILURES += 1
    print(
        "FAIL: DR-137 should count each rather-than frame; "
        f"got {_two_rather_than_frames}"
    )
else:
    print("  ok: DR-137 counts each rather-than frame")
_repeated_negative_reversals = (
    "I may not have a husband. I may not have money. But I have love.",
    "I cannot promise speed. I may not guarantee certainty. Yet I can deliver a tested result.",
    "The team did not win the contract. The team never received the endorsement. "
    "But the team changed the market.",
)
for phrase in _repeated_negative_reversals:
    expect_fail("no-negative-parallelisms", phrase,
        f"DR-19B repeated negative-to-affirmative reversal: {phrase}")
_negative_reversal_prefix = "I may not have a husband. I may not have money. "
for affirmative_turn in (
    "However, I have love.",
    "Still, I have love.",
    "Nevertheless, I have love.",
    "Nonetheless, I have love.",
    "Even so, I have love.",
    "That said, I have love.",
    "Instead, I have love.",
    "In contrast, I have love.",
    "On the other hand, I have love.",
    "I do have love.",
    "What I have is love.",
    "What I do have is love.",
):
    expect_fail(
        "no-negative-parallelisms",
        _negative_reversal_prefix + affirmative_turn,
        f"DR-19B affirmative reversal variant: {affirmative_turn}",
    )
_source_reversal = ALL_CHECKS["no-negative-parallelisms"](
    _repeated_negative_reversals[0]
)
if (
    _source_reversal.get("candidate_count") != 1
    or not _source_reversal.get("matches")
    or "But I have love" not in _source_reversal["matches"][0]
):
    FAILURES += 1
    print(
        "FAIL: DR-19B should return the complete negative-to-affirmative frame "
        f"as one candidate; got {_source_reversal}"
    )
else:
    print("  ok: DR-19B returns the complete reversal as one candidate")
for phrase in (
    "I may not have a husband. But I have love.",
    "I may not have a husband. I may not have money. But she has love.",
    "I may not have a husband. I may not have money. I have love.",
):
    expect_pass("no-negative-parallelisms", phrase,
        f"DR-19B incomplete reversal frame: {phrase}")
expect_fail("no-negative-parallelisms",
    "The building was not damaged in the fire. It was inspected the following day.",
    "negative clause followed by an it-resumption")
expect_fail("no-negative-parallelisms",
    "It's not the best display in its class, but it's good enough for professional work.",
    "same-subject negative-positive comparison")
expect_fail("no-negative-parallelisms",
    "The laptop is powerful, not cheap.",
    "positive-negative adjectival parallelism")
expect_fail("no-negative-parallelisms",
    "It was not raining, but the road was still wet.",
    "not-X-but-Y structure")
expect_pass("no-negative-parallelisms",
    "This is more expensive than the older model.",
    "ordinary price comparison")
expect_pass("no-negative-parallelisms",
    "The issue was not reported until Monday.",
    "plain factual negation")

# DR-25A: the reversal frame survives three decorations that previously broke
# the matcher. Each pair below is the bare frame (already caught) followed by
# the decorated form that must now be caught too.
expect_fail("no-negative-parallelisms",
    "The Moon landing, in this context, is not a moment of transcendence "
    "in the usual sense. It is quieter, more ambiguous.",
    "DR-25A comma parenthetical inside the negative clause's subject")
expect_fail("no-negative-parallelisms",
    "It has reminded me that design judgement is not a private talent. "
    "It is a practice formed through examples.",
    "DR-25A negative clause embedded under a subordinator")
expect_fail("no-negative-parallelisms",
    "That is not a lesser outcome. In many organisations, that is the work "
    "nobody has been able to do.",
    "DR-25A adverbial opener before the affirmative turn")
expect_pass("no-negative-parallelisms",
    "The council, meeting on Tuesday, did not publish the report. "
    "Residents waited another week.",
    "DR-25A parenthetical subject with no resumption")
expect_pass("no-negative-parallelisms",
    "She said that the road was not closed. Traffic moved slowly all morning.",
    "DR-25A subordinated negation with no resumption")
expect_pass("no-negative-parallelisms",
    "That is not a lesser outcome. In many organisations, budgets decide "
    "which work happens.",
    "DR-25A adverbial opener with no repeated subject")
expect_pass("no-negative-parallelisms",
    "What if the heat does not bother the camels?\n\nAs humans, it is hard "
    "to imagine that.",
    "DR-25A adverbial bridge does not span a question or a paragraph break")

_overlapping_negative_parallelism = ALL_CHECKS["no-negative-parallelisms"](
    "To leave the earth was not merely to extend human capability but to trespass into a forbidden domain."
)
if _overlapping_negative_parallelism.get("candidate_count") != 1:
    FAILURES += 1
    print(
        "FAIL: overlapping negative-parallelism regexes should yield one occurrence; "
        f"got {_overlapping_negative_parallelism}"
    )
else:
    print("  ok: overlapping negative-parallelism regexes yield one occurrence")

_one_negative_parallelism = ALL_CHECKS["overall-signal-stacking"](
    "The target was never a man. The target was the truth."
)
_two_negative_parallelisms = ALL_CHECKS["overall-signal-stacking"](
    "The target was never a man. The target was the truth. "
    "The result was not a delay. The result was a reset."
)
_three_negative_parallelisms = ALL_CHECKS["overall-signal-stacking"](
    "The target was never a man. The target was the truth. "
    "The result was not a delay. The result was a reset. "
    "The outcome was not a loss. The outcome was a lesson."
)
_negative_parallelism_scores = [
    _one_negative_parallelism.get("score"),
    _two_negative_parallelisms.get("score"),
    _three_negative_parallelisms.get("score"),
]
if _negative_parallelism_scores != [2, 3, 4]:
    FAILURES += 1
    print(
        "FAIL: repeated negative parallelism should increase stacking evidence "
        f"from 2 to 3 to 4 points; got {_negative_parallelism_scores}"
    )
elif _one_negative_parallelism["passed"] is not True or _three_negative_parallelisms["passed"] is not False:
    FAILURES += 1
    print("FAIL: one occurrence should remain a signal while three occurrences trigger stacking")
else:
    print("  ok: repeated negative parallelism increases stacking evidence")


# --- no-copula-avoidance ---

print("\n=== no-copula-avoidance ===")
expect_fail("no-copula-avoidance",
    "The library serves as a community hub.",
    "serves as (singular)")
expect_fail("no-copula-avoidance",
    "Libraries serve as trusted institutions.",
    "serve as (plural)")
expect_fail("no-copula-avoidance",
    "They function as informal education infrastructure.",
    "function as (plural)")
expect_pass("no-copula-avoidance",
    "The library is a community hub.",
    "plain copula 'is'")
expect_pass("no-copula-avoidance",
    "This is a feature, not a bug.",
    "noun 'feature' is not copula avoidance")
expect_fail("no-copula-avoidance",
    "The gallery features four separate spaces.",
    "verb 'features' as copula avoidance")
expect_fail("no-copula-avoidance",
    "The frontier operates as a unifying thread.",
    "DR-18A operates as")
expect_fail("no-copula-avoidance",
    "The film offers a different entry point.",
    "DR-18A offers plus article")
expect_fail("no-copula-avoidance",
    "The organisation maintains a strong digital presence.",
    "DR-18A third-person maintains plus article")
expect_pass("no-copula-avoidance",
    "Maintain a visible list of open questions.",
    "DR-18A imperative maintain is not a copula substitute")
expect_fail("no-copula-avoidance",
    "Widgetry refers to the practice of making widgets.",
    "DR-18A lead-opening refers to")
expect_pass("no-copula-avoidance",
    "The guide discusses what Brown refers to as the second phase.",
    "DR-18A embedded refers to is not the lead formula")
expect_fail("no-copula-avoidance",
    "She ventured into politics as a candidate in 2018.",
    "DR-18A elaborate candidate substitute")
expect_fail("no-copula-avoidance",
    "He began his career as a teacher.",
    "DR-18A elaborate career substitute")


# --- no-filler-phrases ---

print("\n=== no-filler-phrases ===")
expect_fail("no-filler-phrases",
    "In order to succeed, you must plan carefully.",
    "in order to")
expect_fail("no-filler-phrases",
    "It is worth recognising that this takes time.",
    "it is worth recognising")
expect_fail("no-filler-phrases",
    "Cooking is often framed as a chore.",
    "is often framed as")
expect_pass("no-filler-phrases",
    "Planning helps you succeed.",
    "clean rewrite")


# --- no-generic-conclusions ---

print("\n=== no-generic-conclusions ===")
expect_fail("no-generic-conclusions",
    "The future looks bright for renewable energy.",
    "the future looks bright")
expect_pass("no-generic-conclusions",
    "Solar capacity is projected to double by 2030.",
    "specific factual conclusion")


# --- no-false-concession-hedges ---

print("\n=== no-false-concession-hedges ===")
expect_fail("no-false-concession-hedges",
    "While critics argue the policy is too expensive, supporters say it is necessary. The truth lies somewhere in the middle.",
    "fake both-sides middle")
expect_pass("no-false-concession-hedges",
    "Critics focused on the policy's cost. Supporters pointed to the emissions data from 2023.",
    "concrete positions without tidy middle")


# --- no-placeholder-residue ---

print("\n=== no-placeholder-residue ===")
expect_fail("no-placeholder-residue",
    "Hi {client_name}, thanks for meeting with [Company Name] on [insert date].",
    "unfilled placeholders")
for residue in (
    "Insert Table 1 here",
    "turn0search0",
    "turn0image4",
    "turn0news2",
    "turn1file0",
    "0",
    "_generated-reference-identifier_",
    '<ref name="0search12">',
    "oai_citation:0",
    "Wikipedia+1",
    "[attached_file:1]",
    "[web:1]",
    '<grok-card data-id="e8ff4f">',
    'grok_render_citation_card_json={"cardIds":["3bb883"]}',
    "【85†L261-269】",
    "[cite: 3, 12, 13]",
    '({"attribution":{"attributableIndex":"1009-1"}})',
    ':::writing{variant="document" id="51724"}',
):
    expect_fail("no-placeholder-residue", residue,
        f"DR-20A platform or publishing residue: {residue}")
expect_pass("no-placeholder-residue",
    "Hi Mara, thanks for meeting with Northline on Tuesday.",
    "filled-in email")
expect_pass("no-placeholder-residue",
    "The web team attached the file after checking x + 1 examples.",
    "ordinary words and spaced arithmetic are not platform residue")


# --- no-soft-scaffolding ---

print("\n=== no-soft-scaffolding ===")
expect_fail("no-soft-scaffolding",
    "One useful area is explanation. Another useful area is test writing. The main risk is over-trusting the output.",
    "generated explainer scaffolding")
expect_fail("no-soft-scaffolding",
    "A major priority was research translation.\n\nAnother area of work was patient capital.\n\nThe committee also examined regional access.",
    "repeated report paragraph scaffolding")
expect_pass("no-soft-scaffolding",
    "The tool explains unfamiliar modules and can draft tests when the project already has clear examples.",
    "direct explanation without scaffold labels")
expect_pass("no-soft-scaffolding",
    "A major priority was research translation. The report then gives the three funding decisions made in June.",
    "single necessary report transition stays below threshold")
expect_pass("no-soft-scaffolding",
    "The minutes record that another area of work was patient capital.",
    "report phrase inside a sentence is not a paragraph opener")


# --- no-orphaned-demonstratives ---

print("\n=== no-orphaned-demonstratives ===")
expect_fail("no-orphaned-demonstratives",
    "The report was released on Monday. This highlights a gap in planning. This underscores the need for action. This demonstrates the importance of governance.",
    "3 vague demonstrative subject starts")
expect_pass("no-orphaned-demonstratives",
    "The report was released on Monday. Its missing appendix left the budget question unanswered.",
    "concrete subject")


# --- no-forced-triads ---

print("\n=== no-forced-triads ===")


def expect_triad(text, reason, recognized=True):
    """Assert extractor coverage. #10 judges the rate, not any single triad."""
    global FAILURES
    found = bool(_grade.extract_triad_candidates(text))
    if found != recognized:
        FAILURES += 1
        verb = "recognize" if recognized else "ignore"
        print(f"FAIL: extract_triad_candidates should {verb}: {reason}")
    else:
        print(f"  ok: extract_triad_candidates correctly handles: {reason}")


expect_triad("It supports equity, participation, and resilience.",
    "equity doesn't match but participation (-tion) and resilience (-ence) do")
expect_triad("The program builds curation, classification, and neutrality.",
    "all three match -tion/-ity")
expect_triad("The store sells apples, bread, and milk.",
    "concrete triad is still a triad")
expect_triad("They know when to engage, how to respond, and when a decision closes.",
    "parallel clause triad")
expect_triad("They have to risk receiving, admitting limits, or letting someone else do it.",
    "parallel verb-phrase triad")
expect_triad("Pleasure softens my edges, which makes service kinder and less controlling.",
    "three-part rhetorical coordination")
expect_triad("She answers quickly, smooths things over, and then wonders why life feels tight.",
    "narrative sequence rather than a parallel triad", recognized=False)


# --- no-superficial-ing ---

print("\n=== no-superficial-ing ===")
expect_fail("no-superficial-ing",
    "The temple uses blue and gold, reflecting the community's deep connection to the land.",
    "tacked-on reflecting clause")
expect_pass("no-superficial-ing",
    "The temple uses blue and gold. According to the architect, these reference local flora.",
    "no tacked-on -ing")

for _verb, _tail in (
    ("creating", "a generic sense of importance"),
    ("enhancing", "its significance"),
    ("facilitating", "regional development"),
    ("shaping", "the wider conversation"),
    ("driving", "a commitment to change"),
    ("embodying", "the spirit of unity"),
):
    expect_fail(
        "no-superficial-ing",
        f"The project expanded rapidly, {_verb} {_tail}.",
        f"DR-18B trailing {_verb} clause",
    )

expect_fail("no-superficial-ing",
    "Drawing on earlier research, the report proposes a new model.",
    "DR-18B sentence-opening participial clause")
expect_fail("no-superficial-ing",
    "Recognising the unresolved problem, I sought advice.",
    "DR-18B sentence-opening participial clause before first person")
expect_pass("no-superficial-ing",
    "Writing this essay was difficult, but I finished it.",
    "DR-18B gerund subject is not an opening participial clause")
expect_pass("no-superficial-ing",
    "According to the report, the rate increased.",
    "DR-18B According opener is excluded")
expect_pass("no-superficial-ing",
    "During the review, the team found an error.",
    "DR-18B During opener is excluded")
expect_pass("no-superficial-ing",
    "Consulting work should support a decision, even if it takes time.",
    "DR-18B noun modifier with finite verb is excluded")


# --- no-ghost-spectral-density ---

print("\n=== no-ghost-spectral-density ===")
expect_fail("no-ghost-spectral-density",
    "The ghost of memory whispers through the shadows of the old house, echoes lingering.",
    "ghost + whispers + shadows + echoes")
expect_pass("no-ghost-spectral-density",
    "The house was built in 1890 and renovated twice since.",
    "no spectral language")


# --- no-quietness-obsession ---

print("\n=== no-quietness-obsession ===")
expect_fail("no-quietness-obsession",
    "A quiet stillness settled over the room. She spoke softly, gently, in hushed tones.",
    "quiet + stillness + softly + gently + hushed = 5")
expect_fail("no-quietness-obsession",
    "The silent room quietly settled into a soft, hushed stillness.",
    "silent + quietly + soft + hushed + stillness")
expect_pass("no-quietness-obsession",
    "The meeting ended at three. Everyone left quickly.",
    "no quietness words")


# --- no-rhetorical-questions ---

print("\n=== no-rhetorical-questions ===")
expect_fail("no-rhetorical-questions",
    "You made a strong point. And honestly? That's amazing.",
    "DR-21C source-shaped non-question fragment and emphatic answer")
expect_fail("no-rhetorical-questions",
    "The result? It’s remarkable.",
    "DR-21C noun-fragment beat with smart-apostrophe answer")
expect_fail("no-rhetorical-questions",
    "Best part? It actually works.",
    "DR-21C bare noun-fragment beat")
expect_fail("no-rhetorical-questions",
    "The problem? That's only the beginning.",
    "DR-21C noun-fragment beat with direct evaluation")
expect_pass("no-rhetorical-questions",
    "What makes the advert persuasive? The repeated product name keeps the claim memorable. Why carry on? This question remains unresolved.",
    "ordinary interrogative questions are not the approved fragment beat")
expect_pass("no-rhetorical-questions",
    "What's next? That's explained in the final section. What’s missing? It is listed in the appendix.",
    "contracted interrogative starters are not the approved fragment beat")
expect_pass("no-rhetorical-questions",
    "## Can We Fix This?\n\nThe team can fix it by replacing the broken parser.",
    "question-form Markdown heading")
expect_pass("no-rhetorical-questions",
    "She asked, \"Why, how can I, dear?\" Then she closed the door.",
    "literary dialogue")
expect_pass("no-rhetorical-questions",
    "The project was completed on time and under budget.",
    "no questions at all")


# --- no-excessive-lists ---

print("\n=== no-excessive-lists ===")
expect_fail("no-excessive-lists",
    "Key points:\n- First item\n- Second item\n- Third item\n- Fourth item\n- Fifth item\n- Sixth item\n- Seventh item\n- Eighth item\n- Ninth item\nDone.",
    "9/11 lines are bullets = 81%")
expect_pass("no-excessive-lists",
    "The bridge was built in two phases. First, the foundations were laid. Then the span was constructed. A small ceremony marked completion.",
    "no list markers")


# --- no-unicode-flair ---

print("\n=== no-unicode-flair ===")
expect_fail("no-unicode-flair",
    "Next steps → draft the plan ✓ review the risks ★ ship the update.",
    "decorative Unicode symbols")
expect_fail("no-unicode-flair",
    "Use 𝗯𝗼𝗹𝗱 for the title and 𝘪𝘵𝘢𝘭𝘪𝘤 for the subtitle.",
    "two contiguous stylized-Unicode runs")
expect_fail("no-unicode-flair",
    "Use 𝗯𝗼𝗹𝗱 for the title and practise 5 minutes × day.",
    "one stylized-Unicode run plus a multiplication sign")
expect_pass("no-unicode-flair",
    "Use 𝗯𝗼𝗹𝗱 for the title.",
    "one stylized word counts as one candidate, not one per letter")
expect_pass("no-unicode-flair",
    "Use **bold** for the title and *italic* for the subtitle.",
    "ordinary Markdown bold and italics are not Unicode flair")
expect_pass("no-unicode-flair",
    "Next steps: draft the plan, review the risks, and ship the update.",
    "plain punctuation")


# --- no-dramatic-transitions ---

print("\n=== no-dramatic-transitions ===")
expect_fail("no-dramatic-transitions",
    "And then something shifted. I saw the world differently.",
    "something shifted")
expect_pass("no-dramatic-transitions",
    "After the meeting, I revised the proposal based on their feedback.",
    "factual transition")


# --- no-formulaic-openers ---

print("\n=== no-formulaic-openers ===")
expect_fail("no-formulaic-openers",
    "At a foundational level, libraries provide access to information.\n\nBeyond this, they also serve communities.",
    "two formulaic openers")
expect_fail("no-formulaic-openers",
    "At its core, cooking is about autonomy.",
    "at its core")
expect_fail("no-formulaic-openers",
    "There is also a practical dimension that is difficult to ignore.",
    "there is also a")
expect_fail("no-formulaic-openers",
    "From a governance perspective, libraries support democratic participation.",
    "from a X perspective")
expect_fail("no-formulaic-openers",
    "Here's what nobody's talking about: the renewal deadline.",
    "nobody-is-talking throat-clearer")
expect_fail("no-formulaic-openers",
    "Let me be clear: the renewal deadline is Friday.",
    "let-me-be-clear throat-clearer")
expect_fail("no-formulaic-openers",
    "Can we talk about the renewal deadline for a second?",
    "can-we-talk throat-clearer")
expect_fail("no-formulaic-openers",
    "Let's talk about the renewal deadline.",
    "lets-talk throat-clearer")
expect_fail("no-formulaic-openers",
    "We need to talk about the renewal deadline.",
    "we-need-to-talk throat-clearer")
expect_fail("no-formulaic-openers",
    "I need to say something about the renewal deadline.",
    "i-need-to-say throat-clearer")
for hook in (
    "5 things I learned from running a studio:",
    "3 mistakes I see everyone making:",
    "7 lessons from launching a product nobody talks about:",
    "The 3 pillars of incident response:",
    "10 things I wish I knew before managing a team:",
    "Here are 6 frameworks that changed how I think about planning:",
):
    for heading_prefix in ("", "## "):
        expect_fail("no-formulaic-openers", heading_prefix + hook,
            f"DR-135E numbered-hook opener: {heading_prefix + hook}")
expect_pass("no-formulaic-openers",
    "Libraries provide access to information.\n\nThey also serve communities.",
    "plain direct openers")


# --- no-signposted-conclusions ---

print("\n=== no-signposted-conclusions ===")
expect_fail("no-signposted-conclusions",
    "The data supports this view.\n\nIn summary, the project was a success.",
    "In summary")
expect_fail("no-signposted-conclusions",
    "Some more text here.\n\n## Conclusion\n\nThe results were clear.",
    "Conclusion heading")
expect_fail("no-signposted-conclusions",
    "First point.\n\nTo summarise, the evidence is strong.",
    "To summarise")
expect_pass("no-signposted-conclusions",
    "The evidence points in one direction. I doubt this will change.",
    "natural ending without signpost")


# --- no-corporate-ai-speak ---

print("\n=== no-corporate-ai-speak ===")
expect_fail("no-corporate-ai-speak",
    "I deliver impact quickly and drive measurable outcomes across cross-functional teams.",
    "deliver impact + measurable outcomes + cross-functional")
expect_fail("no-corporate-ai-speak",
    "I translate ambiguous requirements into deliverable outcomes.",
    "translate requirements into deliverable outcomes")
expect_fail("no-corporate-ai-speak",
    "I have led end-to-end development across backend services.",
    "end-to-end development")
expect_pass("no-corporate-ai-speak",
    "I built the payment service and mentored two junior engineers.",
    "plain description of work")


# --- no-this-chains ---

print("\n=== no-this-chains ===")
expect_fail("no-this-chains",
    "The policy changed in 2020. This exposed gaps in planning. This shifted the debate. This forced a rethink of priorities.",
    "3 consecutive This [verb] sentences")
expect_pass("no-this-chains",
    "The policy changed in 2020. This exposed gaps in planning. The government responded with new funding.",
    "only 1 This [verb], then a different subject")


# --- no-excessive-hedging ---

print("\n=== no-excessive-hedging ===")
expect_fail("no-excessive-hedging",
    "The impact is often framed as transformative. The role is widely regarded as essential. The outcome cannot be overstated. Success is contingent on execution.",
    "4 hedging constructions in one text")
expect_pass("no-excessive-hedging",
    "The bridge was built in 1937. It cost twelve million dollars. Construction took four years.",
    "no hedging")
expect_pass("no-excessive-hedging",
    "Cooking is often framed as a chore. The value is increasingly recognised. But most people just want dinner.",
    "2 hedging constructions (under threshold)")


# --- no-countdown-negation ---

print("\n=== no-countdown-negation ===")
expect_fail("no-countdown-negation",
    "It wasn't the data. It wasn't the model. It was the prompt.",
    "classic countdown negation: two negations then reveal")
expect_fail("no-countdown-negation",
    "This isn't about money. This isn't about power. This is about principle.",
    "countdown with 'this isn't'")
expect_pass("no-countdown-negation",
    "It wasn't ready on Monday. The team finished it by Wednesday.",
    "single negation followed by unrelated statement")
expect_pass("no-countdown-negation",
    "The building was not damaged. It was inspected the following day.",
    "factual negation, not a countdown pattern")
expect_fail("no-countdown-negation",
    "You can't rush this. You can't shortcut it. You can't fake it.",
    "Branch 2: 3 consecutive same-subject negation sentences")
expect_pass("no-countdown-negation",
    "You can't rush this. You can't shortcut it.",
    "Branch 2: only 2 consecutive, below threshold")
expect_fail("no-countdown-negation",
    "It wasn't the data. It wasn't the model. It was the prompt.",
    "Branch 1 regression: classic countdown still detected")
expect_pass("no-countdown-negation",
    "You can't rush this. We can't shortcut it. They can't fake it.",
    "mixed pronouns: not consecutive same-subject")
expect_fail("no-countdown-negation",
    "People cannot rush this. People cannot shortcut it. People cannot fake it.",
    "Branch 2: 'people cannot' full form, 3 consecutive")


# --- no-negation-density ---

print("\n=== no-negation-density ===")
_negation_heavy = (
    "This is not simple. It is not quick. It does not scale. It does not explain itself. "
    "The team does not know who owns it. The system is not reliable. The data is not complete. "
    "The process is not documented. The goal is not clear. The owner is not named. "
    "The timeline is not credible. " + "Plain filler sentence for length. " * 55
)
expect_fail("no-negation-density",
    _negation_heavy,
    "10+ explanatory negation markers at high density in a long text")
expect_pass("no-negation-density",
    "Most meetings waste time, but written decisions make teams clearer. " * 45,
    "long text without dense negation")


# --- paragraph-length-uniformity ---

print("\n=== paragraph-length-uniformity ===")
_uniform_paragraphs = "\n\n".join(
    "This paragraph has a deliberately similar length because generated articles often settle into an even block size with the same amount of explanation each time."
    for _ in range(8)
)
expect_fail("paragraph-length-uniformity",
    _uniform_paragraphs,
    "8 near-identical paragraph lengths")
_varied_paragraphs = "\n\n".join([
    "Short paragraph with enough words to qualify for this structural check now.",
    "This paragraph is much longer because it adds a concrete story, a qualification, and a little extra mess in the middle so the architecture does not fall into identical blocks across the piece.",
    "Another short paragraph has enough words to count while still changing the rhythm clearly.",
    "Here the writer slows down and spends more time on a specific example, adding dates, details, and a partial objection that changes the shape of the paragraph rather than landing at the same predictable length.",
    "This one is compact but still above the minimum word threshold for substantial prose paragraphs.",
    "The next paragraph wanders longer than expected, which is exactly the point for this test because human drafts often have uneven pressure from one paragraph to the next.",
    "A final qualifying short paragraph closes the sample without becoming another identical block."
])
expect_pass("paragraph-length-uniformity",
    _varied_paragraphs,
    "varied paragraph lengths")


# --- no-tidy-paragraph-endings ---

print("\n=== no-tidy-paragraph-endings ===")
expect_fail("no-tidy-paragraph-endings",
    "The team missed the deadline. That is why planning matters.\n\nThe data was incomplete. The takeaway is clear.\n\nThe user flow confused people. In the end, clarity wins.",
    "three generic miniature conclusions")
expect_pass("no-tidy-paragraph-endings",
    "The team missed the deadline after the API changed.\n\nThe data was incomplete, so the analyst reran the survey.\n\nThe user flow confused people on the payment screen.",
    "specific endings without tidy summary labels")
expect_fail("no-tidy-paragraph-endings",
    "The translators selected only the short lyrics. The selection was already an interpretation.\n\n"
    "The syntax was regularised and the irony softened. Difficulty became refinement; irony could sound sincere.\n\n"
    "The practices did not erase inequality. These practices were not romantic solutions; they were ways of living within it.",
    "three compact structural paragraph closures")

_two_structural_endings = ALL_CHECKS["no-tidy-paragraph-endings"](
    "The translators selected only the short lyrics. The selection was already an interpretation.\n\n"
    "The syntax was regularised and the irony softened. Difficulty became refinement; irony could sound sincere."
)
assert _two_structural_endings["passed"]
assert _two_structural_endings["candidate_count"] == 2

_literal_and_subordinate_controls = ALL_CHECKS["no-tidy-paragraph-endings"](
    "The archivist arrived before lunch. The manuscript was already on the desk.\n\n"
    "I chose a loaf tin if I felt cautious; a tray if I felt brave."
)
assert _literal_and_subordinate_controls["passed"]
assert _literal_and_subordinate_controls["candidate_count"] == 0

_quoted_structural_ending = ALL_CHECKS["no-tidy-paragraph-endings"](
    'The critic called the ending reductive: “The selection was already an interpretation.”'
)
assert _quoted_structural_ending["candidate_count"] == 1
assert _quoted_structural_ending["candidates"][0]["quoted"] is True


# --- no-bland-critical-template ---

print("\n=== no-bland-critical-template ===")
expect_fail("no-bland-critical-template",
    "The novel is the kind of contemporary novel that does several familiar things at once. Its emotional range is difficult to dismiss, and its field of sympathy earns much of its weight.",
    "generic review vocabulary")
expect_pass("no-bland-critical-template",
    "The second chapter works because Murray lets PJ misunderstand the adult conversation before the reader does.",
    "concrete critical claim")


# --- no-rubric-echoing ---

print("\n=== no-rubric-echoing ===")
expect_fail("no-rubric-echoing",
    "The author creates a serious tone. I can tell because the quote shows that the character is sad. This evidence shows that the text demonstrates the author's use of imagery.",
    "rubric/assignment boilerplate")
expect_pass("no-rubric-echoing",
    "The second paragraph slows down after the argument, and the shorter sentence at the end changes the pressure.",
    "specific textual analysis")


# --- vocabulary-diversity ---

print("\n=== vocabulary-diversity ===")
expect_pass("vocabulary-diversity",
    "Short text with only a few words.",
    "short text skipped (under 150 words)")
# Direction flipped 2026-07-17 (Mae): high windowed diversity is the AI
# direction, so repetition is no longer flagged by this check.
expect_pass("vocabulary-diversity",
    " ".join(["the system is very good and the system is very effective and the system is very reliable"] * 20),
    "extremely repetitive text with low TTR (clear under flipped direction)")
# Flipped 2026-07-17: this fixture was engineered for maximal diversity and
# now sits above the observed human range, so it flags.
expect_fail("vocabulary-diversity",
    "The cathedral was built between 1163 and 1345 on the Ile de la Cite in Paris. "
    "Its flying buttresses were among the first in Gothic architecture, allowing thinner walls "
    "and larger stained glass windows. During the French Revolution, much of the religious imagery "
    "was damaged or destroyed, and the building served briefly as a warehouse. Victor Hugo's 1831 "
    "novel drew public attention to its deteriorating condition, prompting a major restoration led "
    "by architect Eugene Viollet-le-Duc. The spire he added collapsed during the 2019 fire, which "
    "also destroyed the oak roof frame known as 'the forest' because of the number of trees used "
    "in its construction. Rebuilding efforts have drawn craftspeople from across Europe using both "
    "traditional and modern techniques. The limestone facade has been cleaned for the first time in "
    "decades, revealing the original pale colour beneath centuries of pollution. Historians debate "
    "whether the restoration should preserve Viollet-le-Duc's additions or return to an earlier "
    "medieval form. The cathedral reopened in December 2024 after five years of intensive work.",
    "engineered maximal-diversity fixture (0.773, above the observed human range)")


# --- new vocabulary items ---

print("\n=== new vocabulary items (spot check) ===")
expect_fail("no-ai-vocabulary-clustering",
    "The unparalleled results were invaluable to the meticulous research team.",
    "'unparalleled' + 'invaluable' + 'meticulous' = 3 new AI vocab items")


# --- no-forced-triads density (#10) ---

print("\n=== no-forced-triads density ===")

# Build a 400+ word text with 5 triads
_triad_heavy = (
    "The team needed apples, bananas, and oranges for the project. "
    "They also brought cats, dogs, and birds to the demonstration event. "
    "The walls were painted red, blue, and green to match the brand. "
    "Options came in small, medium, or large depending on the client. "
    "The pace was fast, slow, and steady throughout the quarter. "
    + "This is filler text to reach the word count threshold. " * 30
)
expect_fail("no-forced-triads",
    _triad_heavy,
    "5 triads in 400+ words is above 4.0 per 1000")

# 1 triad in 400+ words should pass
_triad_light = (
    "The team needed apples, bananas, and oranges for the project. "
    + "This is filler text to reach the word count threshold. " * 30
)
expect_pass("no-forced-triads",
    _triad_light,
    "1 triad in 400+ words is below 4.0 per 1000")

# Short text with 5 triads should skip (pass)
_triad_short = (
    "Apples, bananas, and oranges. Cats, dogs, and birds. "
    "Red, blue, and green. Small, medium, or large. Fast, slow, and steady."
)
expect_pass("no-forced-triads",
    _triad_short,
    "short text (under 300 words) with 5 triads should skip")

# Empty/minimal text should pass
expect_pass("no-forced-triads",
    "",
    "empty text")
expect_pass("no-forced-triads",
    "A single sentence.",
    "minimal text")


# --- no-section-scaffolding ---

print("\n=== no-section-scaffolding ===")
expect_fail("no-section-scaffolding",
    "How to make this work:\nSome content here.\n\nHow to make this work:\nMore content.\n\nHow to make this work:\nEven more.",
    "3 repeated labels")
expect_pass("no-section-scaffolding",
    "Step 1:\nFirst thing to do.\n\nStep 2:\nSecond thing to do.\n\nStep 3:\nThird thing to do.",
    "different labels")
expect_pass("no-section-scaffolding",
    "How to make this work:\nSome content here.\n\nHow to make this work:\nMore content.\n\nSomething else entirely:\nDifferent content.",
    "label appears only 2 times")
expect_pass("no-section-scaffolding",
    "This is a long sentence that repeats because the writer needed to fill space in the document for some reason or another.\nSome content.\n\nThis is a long sentence that repeats because the writer needed to fill space in the document for some reason or another.\nMore content.\n\nThis is a long sentence that repeats because the writer needed to fill space in the document for some reason or another.\nEven more.",
    "repeated line over 60 characters (prose, not a label)")
expect_fail("no-section-scaffolding",
    "### How to apply:\nContent.\n\n### How to apply:\nContent.\n\nHow to apply:\nContent.",
    "markdown heading stripped, matches plain version")
expect_fail("no-section-scaffolding",
    "### First section\nContent.",
    "first Markdown heading starts below level 2")
expect_fail("no-section-scaffolding",
    "## Parent section\nContent.\n\n#### Skipped child level\nMore content.",
    "later Markdown heading skips a level")
expect_fail("no-section-scaffolding",
    "## First section\nContent.\n\n----\n\n## Second section\nMore content.",
    "thematic break immediately precedes a Markdown heading")
expect_pass("no-section-scaffolding",
    "## Parent section\nContent.\n\n### Child section\nMore content.\n\n## Next section\nDone.",
    "heading hierarchy changes one level at a time")
expect_pass("no-section-scaffolding",
    "---\ntitle: Example document\n---\n# Example document\nContent.",
    "YAML frontmatter delimiter before a title is not a thematic break")


# --- no-notability-claims (pattern 2) ---

print("\n=== no-notability-claims ===")
expect_fail("no-notability-claims",
    "She maintains an active social media presence with over 500,000 followers.",
    "active social media presence + follower count")
expect_fail("no-notability-claims",
    "He has gained widespread media attention and was profiled in several major outlets.",
    "gained widespread media attention + profiled in several major outlets")
expect_fail("no-notability-claims",
    "The artist's work has received independent coverage from regional media outlets across the country.",
    "independent coverage + regional media outlets")
for phrase in (
    "The company was covered in trade publications.",
    "The artist was profiled in Vogue.",
    "The launch appeared in music and tech outlets.",
    "Her insights appeared in other prominent media outlets.",
):
    expect_fail("no-notability-claims", phrase,
        f"DR-22A notability formula: {phrase}")
expect_pass("no-notability-claims",
    "In a 2024 New York Times interview, she argued that AI regulation should focus on outcomes rather than methods.",
    "named source + specific date and claim")
expect_pass("no-notability-claims",
    "The town held its weekly market on Saturday, drawing roughly 200 traders from neighbouring villages.",
    "concrete description, no notability framing")


# --- no-vague-attributions (pattern 5) ---

print("\n=== no-vague-attributions ===")
expect_fail("no-vague-attributions",
    "Experts argue that the policy will reshape the industry within a decade.",
    "experts argue, no source")
expect_fail("no-vague-attributions",
    "Industry reports suggest a downturn is imminent across the sector.",
    "industry reports suggest, no source")
expect_fail("no-vague-attributions",
    "Several critics argue the design prioritises form over function.",
    "several critics argue, no source")
expect_fail("no-vague-attributions",
    "It is widely believed that remote work harms culture.",
    "impersonal it is widely believed")
expect_pass("no-vague-attributions",
    "According to the 2024 Stanford Owl Labs survey, productivity rose by 13% among remote knowledge workers.",
    "named source with date and figure")
expect_pass("no-vague-attributions",
    "The Haolai River supports several endemic fish species, according to a 2019 survey by the Chinese Academy of Sciences.",
    "patterns.md After example — clearly attributed")


# --- no-boldface-overuse (pattern 13) ---

print("\n=== no-boldface-overuse ===")
expect_fail("no-boldface-overuse",
    "It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.",
    "patterns.md Before — four bold spans in one prose sentence")
expect_fail("no-boldface-overuse",
    "The team will deliver **product strategy**, **roadmap planning**, **stakeholder alignment**, and **executive reporting**.",
    "four bold spans in prose")
expect_pass("no-boldface-overuse",
    "It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.",
    "patterns.md After — no bold")
expect_pass("no-boldface-overuse",
    "- **Apples:** sweet\n- **Bananas:** also sweet\n- **Carrots:** not a fruit\n- **Daikon:** also not a fruit",
    "bold spans only inside list items — caught by no-inline-header-lists, ignored here")
expect_pass("no-boldface-overuse",
    "The **important** distinction is between **public** and **private** keys.",
    "three bolded terms in prose — under threshold of 4")


# --- no-inline-header-lists (pattern 14) ---

print("\n=== no-inline-header-lists ===")
expect_fail("no-inline-header-lists",
    "- **User Experience:** The user experience has been significantly improved.\n- **Performance:** Performance has been enhanced through optimised algorithms.\n- **Security:** Security has been strengthened with end-to-end encryption.",
    "patterns.md Before — three bolded-header bullets")
expect_fail("no-inline-header-lists",
    "1. **First step:** Do this thing.\n2. **Second step:** Do that thing.",
    "two bolded-header numbered items")
expect_fail("no-inline-header-lists",
    "- **First step**: Do this thing.\n- **Second step**: Do that thing.",
    "colon appears after the closing bold marker")
expect_fail("no-inline-header-lists",
    "1) **First step:** Do this thing.\n2) **Second step:** Do that thing.",
    "numbered items use a closing parenthesis")
expect_fail("no-inline-header-lists",
    "‣ **First step:** Do this thing.\n◦ **Second step:** Do that thing.",
    "items use Unicode bullet markers")
expect_fail("no-inline-header-lists",
    "- **Time: Cost:** Compare both.\n- **Risk: Impact:** Compare both.",
    "existing labels may contain an internal colon")
expect_fail("no-inline-header-lists",
    "**Speed:** Fast. **Cost:** Low.",
    "two bold-label segments on one input line")
expect_pass("no-inline-header-lists",
    "The update improves the interface, speeds up load times through optimised algorithms, and adds end-to-end encryption.",
    "patterns.md After — flowing prose")
expect_pass("no-inline-header-lists",
    "- Apples are sweet\n- Bananas are also sweet\n- Carrots are not a fruit",
    "plain bullets without bolded headers")
expect_pass("no-inline-header-lists",
    "- **One bolded header:** definition only",
    "single bolded-header item — under threshold of 2")
expect_pass("no-inline-header-lists",
    "**Speed:** Fast.\n**Cost:** Low.",
    "one unmarked bold-label segment per input line")


# --- no-compound-modifier-density (pattern 18) ---

print("\n=== no-compound-modifier-density ===")
expect_fail("no-compound-modifier-density",
    "The cross-functional team delivered a high-quality, data-driven report on our client-facing tools.",
    "patterns.md Before — four AI compounds in one sentence")
expect_fail("no-compound-modifier-density",
    "Our real-time, end-to-end, mission-critical platform handles every workload.",
    "three compounds in one sentence")
expect_pass("no-compound-modifier-density",
    "The team, drawn from several departments, delivered a report grounded in usage data for our client-facing tools.",
    "patterns.md After — single client-facing in prose")
expect_pass("no-compound-modifier-density",
    "She explained the long-term plan and the short-term tradeoffs in plain language.",
    "two compounds in prose — under threshold of 3")


# --- no-knowledge-cutoff-disclaimers (pattern 20) ---

print("\n=== no-knowledge-cutoff-disclaimers ===")
expect_fail("no-knowledge-cutoff-disclaimers",
    "While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established in the 1990s.",
    "patterns.md Before — limited-information hedge")
expect_fail("no-knowledge-cutoff-disclaimers",
    "Up to my last training update, the policy had not been amended.",
    "up to my last training update")
expect_fail("no-knowledge-cutoff-disclaimers",
    "Based on publicly available information, the company employs roughly 200 people.",
    "based on publicly available information")
expect_fail("no-knowledge-cutoff-disclaimers",
    "I am unable to verify the exact figure for 2024.",
    "I am unable to verify")
expect_pass("no-knowledge-cutoff-disclaimers",
    "The company was founded in 1994, according to its registration documents.",
    "patterns.md After — concrete claim with source")
expect_pass("no-knowledge-cutoff-disclaimers",
    "As of October 2025, the project had completed three pilot deployments.",
    "as of [date] used to anchor a fact, not as a model-meta hedge")


# --- no-unicode-flair extension (pattern 16 fold) ---

print("\n=== no-unicode-flair (pattern 16 fold) ===")
expect_fail("no-unicode-flair",
    ":rocket: Launch Phase: The product launches in Q3.\n:bulb: Key Insight: Users prefer simplicity.",
    "two emoji shortcodes in headings")
expect_fail("no-unicode-flair",
    "We've shipped 🎉 the new release 🚀 with confidence.",
    "two supplemental-plane emojis in prose (broader range)")
expect_pass("no-unicode-flair",
    "The product launches in Q3. User research showed a preference for simplicity.",
    "patterns.md After — plain prose, no symbols")
expect_pass("no-unicode-flair",
    "Visit https://example.com:8080 for the latest build.",
    "URL with colon — not a shortcode")
expect_pass("no-unicode-flair",
    "The build finished at 12:30:45.",
    "timestamp colons — not a shortcode")


# --- Group A resolution markers (U1 meta-test) ---

print("\n=== group-a-resolution-markers ===")
import re as _re_meta
_patterns_md = (ROOT / "human-eyes" / "references" / "patterns.md").read_text()
_pattern_sections = _re_meta.split(r"(?=^### \d+[a-z]?\.\s)", _patterns_md, flags=_re_meta.MULTILINE)
# #6 and #11 were removed from the catalogue by DR-155 and DR-156: each carried a
# pattern number with no check behind it, which the two-detector-type rule forbids.
_GROUP_A = [2, 5, 12, 13, 14, 15, 16, 18, 20, 21, 28, 30, 35, 36, 37, 41]
_resolution_seen = {}
for _sec in _pattern_sections:
    _h = _re_meta.match(r"^### (\d+)([a-z])?\.\s", _sec)
    if not _h or _h.group(2):
        continue
    _resolution_seen[int(_h.group(1))] = "**Detection:**" in _sec
for _n in _GROUP_A:
    if not _resolution_seen.get(_n):
        FAILURES += 1
        print(f"FAIL: pattern #{_n} is in Group A but missing **Detection:** marker in patterns.md")
    else:
        print(f"  ok: pattern #{_n} carries a Detection marker")


# --- Group B resolution coverage (U2 meta-test) ---

print("\n=== group-b-resolution-coverage ===")
_GROUP_B_CHECKS = [
    "no-manufactured-insight",
    "no-performed-candour",
    "no-formulaic-social-posts",
    "no-corporate-ai-speak",
    "no-signposted-conclusions",
    "no-nonliteral-land-surface",
    "no-bland-critical-template",
    "no-soft-scaffolding",
    "no-negation-density",
    "overall-signal-stacking",
]
for _check in _GROUP_B_CHECKS:
    if f"`{_check}`" not in _patterns_md:
        FAILURES += 1
        print(f"FAIL: Group B check `{_check}` not referenced anywhere in patterns.md")
    else:
        print(f"  ok: Group B check `{_check}` documented in patterns.md")


# --- Severity propagation: patterns.md ↔ CHECK_METADATA (U3 meta-test) ---

print("\n=== severity-propagation ===")

# Parse every Severity line in patterns.md. Format options:
#   **Severity:** <tier> · `check-id` [trailing prose]
#   **Severity:** <tier> · `check-id` and <tier> · `check-id` ...   (composite patterns)
#   **Severity:** inherits <tier> from `parent-check-id` ...        (folded patterns)
#   **Severity:** N/A · ...                                          (manual / agent-judgement)
#
# For each (tier, check-id) pair pulled from a programmatic-check Severity line,
# assert it matches CHECK_METADATA[check-id]["severity"].
#
# The audit-report redesign closed the orphan-table escape hatch: every check
# in CHECK_METADATA must reach a real numbered or sub-lettered pattern entry's
# **Severity:** line. A separate orphan table no longer counts as coverage.

_severity_pairs = []  # list of (tier, check_id, source_label)
for _i, _line in enumerate(_patterns_md.splitlines(), 1):
    if _line.startswith("**Severity:**"):
        # Direct: "**Severity:** <tier> · `check-id`"
        for _tier, _cid in _re_meta.findall(r"(hard_fail|strong_warning|context_warning)\s*·\s*`([\w-]+)`", _line):
            _severity_pairs.append((_tier, _cid, f"line {_i}"))
        # Inherits: "**Severity:** inherits <tier> from `parent`"
        for _tier, _cid in _re_meta.findall(r"inherits\s+(hard_fail|strong_warning|context_warning)\s+from\s+`([\w-]+)`", _line):
            _severity_pairs.append((_tier, _cid, f"line {_i} (inherited)"))

# Regression guard: the "Severity for unnumbered checks" section was a known
# escape hatch — it let new checks land without a real pattern entry. The
# audit-report redesign removed it. If anyone reintroduces a section heading
# that matches that shape, fail loudly so we don't grow a parallel registry.
_orphan_section_re = _re_meta.compile(r"^##\s+severity\s+for\s+unnumbered", _re_meta.IGNORECASE)
for _i, _line in enumerate(_patterns_md.splitlines(), 1):
    if _orphan_section_re.match(_line):
        FAILURES += 1
        print(f"FAIL: patterns.md line {_i} reintroduces the orphan 'Severity for unnumbered checks' section. Every check must live in a numbered or sub-lettered pattern entry.")

_seen_checks = set()
for _tier, _cid, _src in _severity_pairs:
    _seen_checks.add(_cid)
    _expected = CHECK_METADATA.get(_cid, {}).get("severity")
    if _expected is None:
        FAILURES += 1
        print(f"FAIL: patterns.md {_src} references unknown check `{_cid}`")
    elif _expected != _tier:
        FAILURES += 1
        print(f"FAIL: patterns.md {_src} declares {_cid}={_tier} but CHECK_METADATA says {_expected}")

# Every check in CHECK_METADATA must appear at least once in a Severity declaration.
_missing = sorted(set(CHECK_METADATA) - _seen_checks)
if _missing:
    FAILURES += 1
    print(f"FAIL: {len(_missing)} check(s) in CHECK_METADATA have no Severity declaration in patterns.md: {_missing}")
else:
    print(f"  ok: every check in CHECK_METADATA ({len(CHECK_METADATA)}) carries a Severity declaration in patterns.md")


# --- severity and mode architecture ---

print("\n=== severity-and-mode-architecture ===")
expected_checks = {
    "no-em-dashes",
    "no-ai-vocabulary-clustering",
    "no-nonliteral-land-surface",
    "overall-signal-stacking",
    "no-manufactured-insight",
    "no-performed-candour",
    "no-formulaic-social-posts",
    "no-staccato-sequences",
    "no-anaphora",
    "no-paragraph-anaphora",
    "no-heading-one-liners",
    "no-modal-stacks",
    "no-collaborative-artifacts",
    "no-curly-quotes",
    "sentence-length-variance",
    "no-promotional-language",
    "no-significance-inflation",
    "no-negative-parallelisms",
    "no-copula-avoidance",
    "no-filler-phrases",
    "no-generic-conclusions",
    "no-false-concession-hedges",
    "no-placeholder-residue",
    "no-soft-scaffolding",
    "no-orphaned-demonstratives",
    "no-forced-triads",
    "no-nominalisation-rate",
    "no-that-relative-rate",
    "no-participial-clause-rate",
    "no-passive-voice-rate",
    "no-it-pronoun-rate",
    "no-superficial-ing",
    "no-ghost-spectral-density",
    "no-quietness-obsession",
    "no-rhetorical-questions",
    "no-excessive-lists",
    "no-symmetric-list-items",
    "no-title-case-headings",
    "no-mixed-spelling-conventions",
    "no-false-ranges",
    "no-unicode-flair",
    "no-dramatic-transitions",
    "no-formulaic-openers",
    "no-signposted-conclusions",
    "no-parenthetical-headings",
    "no-corporate-ai-speak",
    "no-this-chains",
    "no-excessive-hedging",
    "no-countdown-negation",
    "no-negation-density",
    "paragraph-length-uniformity",
    "no-tidy-paragraph-endings",
    "no-bland-critical-template",
    "no-rubric-echoing",
    "vocabulary-diversity",
    "no-section-scaffolding",
    # U1 (audit-report redesign): Group A patterns 2, 5, 13, 14, 18, 20.
    "no-notability-claims",
    "no-vague-attributions",
    "no-boldface-overuse",
    "no-inline-header-lists",
    "no-compound-modifier-density",
    "no-knowledge-cutoff-disclaimers",
}
actual_checks = set(ALL_CHECKS)
if actual_checks != expected_checks:
    FAILURES += 1
    print(f"FAIL: check registry changed. missing={sorted(expected_checks - actual_checks)} extra={sorted(actual_checks - expected_checks)}")
else:
    print(f"  ok: all {len(expected_checks)} expected checks are registered")

allowed_failure_modes = {
    "provenance_residue",
    "synthetic_significance",
    "frictionless_structure",
    "generic_abstraction",
    "voice_erasure",
    "genre_misfit",
}
for check_name in ALL_CHECKS:
    if check_name not in CHECK_METADATA:
        FAILURES += 1
        print(f"FAIL: missing severity metadata for {check_name}")
        continue
    modes = CHECK_METADATA[check_name].get("failure_modes", [])
    if not modes:
        FAILURES += 1
        print(f"FAIL: missing failure mode metadata for {check_name}")
    elif not set(modes).issubset(allowed_failure_modes):
        FAILURES += 1
        print(f"FAIL: invalid failure mode metadata for {check_name}: {modes}")
    if not CHECK_METADATA[check_name].get("evidence_role"):
        FAILURES += 1
        print(f"FAIL: missing evidence role metadata for {check_name}")

_annotated = annotate_result({"text": "no-em-dashes", "passed": False, "evidence": "example"})
if _annotated.get("failure_modes") != ["genre_misfit"]:
    FAILURES += 1
    print(f"FAIL: annotate_result should include failure modes; got {_annotated.get('failure_modes')}")
else:
    print("  ok: annotated results include failure modes")

_failure_mode_report = failure_mode_results([
    annotate_result({"text": "no-collaborative-artifacts", "passed": False, "evidence": "assistant residue"}),
    annotate_result({"text": "no-formulaic-openers", "passed": False, "evidence": "formulaic opener"}),
    annotate_result({"text": "no-em-dashes", "passed": True, "evidence": "clean"}),
])
_triggered_report = triggered_checks([
    annotate_result({"text": "no-collaborative-artifacts", "passed": False, "evidence": "assistant residue"}),
    annotate_result({"text": "no-formulaic-openers", "passed": False, "evidence": "formulaic opener"}),
    annotate_result({"text": "no-em-dashes", "passed": True, "evidence": "clean"}),
])
_score_report = score_summary([
    annotate_result({
        "text": "overall-signal-stacking",
        "passed": False,
        "evidence": "Overall signal stacking 5/4",
        "score": 5,
        "threshold": 4,
        "components": ["paragraph length uniformity", "headings in prose"],
        "vocabulary_signal_stacking": {
            "points": 1,
            "reasons": ["generic cluster"],
            "worst_generic": 2,
            "gptzero_matches": ["play a pivotal role"],
            "kobak_style_distinct": 4,
            "kobak_style_density": 7.5,
            "kobak_style_sample": ["valuable"],
        },
    }),
    annotate_result({"text": "no-formulaic-openers", "passed": False, "evidence": "formulaic opener"}),
    annotate_result({"text": "no-em-dashes", "passed": True, "evidence": "clean"}),
])
_human_report = human_report([
    annotate_result({
        "text": "overall-signal-stacking",
        "passed": False,
        "evidence": "Overall signal stacking 5/4",
        "score": 5,
        "threshold": 4,
        "components": ["paragraph length uniformity", "headings in prose"],
        "vocabulary_signal_stacking": {
            "points": 1,
            "reasons": ["generic cluster"],
            "worst_generic": 2,
            "gptzero_matches": ["play a pivotal role"],
            "kobak_style_distinct": 4,
            "kobak_style_density": 7.5,
            "kobak_style_sample": ["valuable"],
        },
    }),
    annotate_result({"text": "no-formulaic-openers", "passed": False, "evidence": "formulaic opener"}),
    annotate_result({"text": "no-em-dashes", "passed": True, "evidence": "clean"}),
])
_triggered_names = [item["check"] for item in _triggered_report]
if _triggered_names != ["no-collaborative-artifacts", "no-formulaic-openers"]:
    FAILURES += 1
    print(f"FAIL: triggered_checks should list each failed check once; got {_triggered_names}")
else:
    print("  ok: triggered checks list each failed check once")

_triggered_formulaic = _triggered_report[1]
if _triggered_formulaic["failure_modes"] != ["frictionless_structure", "generic_abstraction"]:
    FAILURES += 1
    print(f"FAIL: triggered check should carry all failure modes; got {_triggered_formulaic['failure_modes']}")
else:
    print("  ok: triggered checks carry all failure modes without duplicating evidence")

if _score_report["check_status"] != "fail" or _score_report["pass_rate"] != "1/3":
    FAILURES += 1
    print(f"FAIL: score_summary should expose check totals; got {_score_report}")
else:
    print("  ok: score summary exposes check totals")

_signal_stacking = _score_report["signal_stacking"]
if not _signal_stacking or _signal_stacking["score"] != 5 or _signal_stacking["threshold"] != 4 or not _signal_stacking["triggered"]:
    FAILURES += 1
    print(f"FAIL: score_summary should expose signal stacking; got {_signal_stacking}")
else:
    print("  ok: score summary exposes signal stacking")

# U8: human_report now returns the audit-format-v1 contract (structured-only).
# The OLD assertions on overview/all_checks/signal_stacking_explanation/confidence
# moved to the contract's aggregates + programmatic_checks shape.

_failed_count = sum(1 for c in _human_report["programmatic_checks"] if c["status"] == "flagged")
_total = len(_human_report["programmatic_checks"])
if _failed_count != 2 or _total != 3:
    FAILURES += 1
    print(f"FAIL: contract should report 2 of 3 flagged; got {_failed_count} of {_total}")
else:
    print("  ok: contract programmatic_checks reports failed/total counts")

_signal_stacking_check = next(
    (c for c in _human_report["programmatic_checks"] if c["id"] == "overall-signal-stacking"),
    None,
)
if not _signal_stacking_check or _signal_stacking_check["status"] != "flagged":
    FAILURES += 1
    print(f"FAIL: contract should include flagged signal-stacking check; got {_signal_stacking_check}")
else:
    print("  ok: signal stacking is reported as one programmatic check")

_signal_stacking_aggr = _human_report["aggregates"]["signal_stacking"]
if "paragraph length uniformity" not in _signal_stacking_aggr["components"]:
    FAILURES += 1
    print(f"FAIL: aggregates.signal_stacking should list components; got {_signal_stacking_aggr['components']}")
else:
    print("  ok: aggregates.signal_stacking lists components")

if "confidence" in _human_report:
    FAILURES += 1
    print("FAIL: U8/R14 removed the labelled confidence block; contract should not include 'confidence'")
else:
    print("  ok: contract has no confidence block (R14 removal)")

# Vocab-only signal-stacking branch: aggregates.signal_stacking.vocabulary_points carries
# the signal that the OLD signal_stacking_explanation prose used to mention.
_human_report_vocab_only = human_report([
    annotate_result({
        "text": "overall-signal-stacking",
        "passed": False,
        "evidence": "Overall signal stacking 4/4",
        "score": 4,
        "threshold": 4,
        "components": [],
        "vocabulary_signal_stacking": {
            "points": 4,
            "reasons": ["generic cluster x4"],
            "worst_generic": 4,
            "gptzero_matches": [],
            "kobak_style_distinct": 8,
            "kobak_style_density": 12.0,
            "kobak_style_sample": ["valuable", "pivotal"],
        },
    }),
])
_vocab_signal_stacking = _human_report_vocab_only["aggregates"]["signal_stacking"]
if _vocab_signal_stacking["vocabulary_points"] != 4 or _vocab_signal_stacking["components"]:
    FAILURES += 1
    print(f"FAIL: vocab-only branch should expose vocabulary_points without components; got {_vocab_signal_stacking}")
else:
    print("  ok: contract aggregates handle vocab-only signal stacking")

_friendly_vocab_only = friendly_evidence({
    "text": "overall-signal-stacking",
    "passed": False,
    "score": 4,
    "threshold": 4,
    "components": [],
    "vocabulary_signal_stacking": {
        "points": 4,
        "reasons": ["generic cluster x4"],
        "worst_generic": 4,
        "gptzero_matches": [],
        "kobak_style_distinct": 8,
        "kobak_style_density": 12.0,
        "kobak_style_sample": [],
    },
})
if "no stacked weak signals" in _friendly_vocab_only or "Clustered AI vocabulary alone" not in _friendly_vocab_only:
    FAILURES += 1
    print(f"FAIL: friendly_evidence vocab-only branch should not contradict itself; got {_friendly_vocab_only}")
else:
    print("  ok: friendly_evidence handles vocab-only signal stacking cleanly")

_total_checks = len(ALL_CHECKS)
_full_table_report = human_report([
    annotate_result({"text": name, "passed": True, "evidence": "clean"})
    for name in ALL_CHECKS
])
if len(_full_table_report["programmatic_checks"]) != _total_checks:
    FAILURES += 1
    print(f"FAIL: full contract should include {_total_checks} programmatic_checks; got {len(_full_table_report['programmatic_checks'])}")
else:
    print(f"  ok: full contract includes all {_total_checks} programmatic checks")

# format_two_layer is the renderer. Deep coverage lives in
# dev/evals/test_two_layer_render.py; this is a smoke test only.
_two_layer_smoke = format_two_layer([
    annotate_result({"text": "no-formulaic-openers", "passed": False, "evidence": "formulaic opener"}),
    annotate_result({"text": "no-em-dashes", "passed": True, "evidence": "clean"}),
], depth="balanced")
if not isinstance(_two_layer_smoke, str) or "**Audit summary**\n" not in _two_layer_smoke:
    FAILURES += 1
    print(f"FAIL: format_two_layer should return a string opening with the **Audit summary** heading; got:\n{_two_layer_smoke[:400]}")
elif "**Next steps**" not in _two_layer_smoke:
    FAILURES += 1
    print(f"FAIL: format_two_layer default-mode output should end with **Next steps** + prompt; got:\n{_two_layer_smoke[:400]}")
elif "pressure" in _two_layer_smoke.lower():
    FAILURES += 1
    print("FAIL: format_two_layer should not contain 'pressure' (renamed to 'signal stacking')")
elif "—" in _two_layer_smoke.split("**Next steps**", 1)[0]:
    FAILURES += 1
    print("FAIL: audit format must be em-dash-free (em dashes are flagged as AI tells)")
else:
    print("  ok: format_two_layer smoke test renders the new audit shape (Audit summary + mini-headers + Next steps, em-dash-free)")

if set(_failure_mode_report) != allowed_failure_modes:
    FAILURES += 1
    print(f"FAIL: failure_mode_results should expose all canonical modes; got {sorted(_failure_mode_report)}")
else:
    print("  ok: failure mode report exposes all canonical modes")

_provenance_checks = [item["check"] for item in _failure_mode_report["provenance_residue"]["failed_checks"]]
if _provenance_checks != ["no-collaborative-artifacts"]:
    FAILURES += 1
    print(f"FAIL: provenance failure grouping wrong; got {_provenance_checks}")
else:
    print("  ok: provenance failures are grouped without losing check identity")

_structure_checks = [item["check"] for item in _failure_mode_report["frictionless_structure"]["failed_checks"]]
_abstraction_checks = [item["check"] for item in _failure_mode_report["generic_abstraction"]["failed_checks"]]
if _structure_checks != ["no-formulaic-openers"] or _abstraction_checks != ["no-formulaic-openers"]:
    FAILURES += 1
    print(f"FAIL: multi-mode failure grouping wrong; structure={_structure_checks} abstraction={_abstraction_checks}")
else:
    print("  ok: multi-mode failures remain visible in every applicable group")

_structure_action = _failure_mode_report["frictionless_structure"]["failed_checks"][0]["depth_actions"]
if _structure_action != {"balanced": "fix", "all": "fix"}:
    FAILURES += 1
    print(f"FAIL: strong warning actions should require fixes at every depth; got {_structure_action}")
else:
    print("  ok: strong warning depth actions require fixes at every depth")

_context_action = failure_mode_results([
    annotate_result({"text": "no-anaphora", "passed": False, "evidence": "context warning"}),
])["genre_misfit"]["failed_checks"][0]["depth_actions"]
if _context_action != {
    "balanced": "preserve_with_disclosure_or_user_decision",
    "all": "fix",
}:
    FAILURES += 1
    print(f"FAIL: context warning actions should preserve at Balanced and fix at All; got {_context_action}")
else:
    print("  ok: context warning depth actions preserve at Balanced and fix at All")

if _failure_mode_report["genre_misfit"]["failed_checks"]:
    FAILURES += 1
    print("FAIL: passed checks should not appear in failure mode groups")
else:
    print("  ok: passed checks are excluded from failure mode groups")

_clean_results = [
    annotate_result({"text": "no-em-dashes", "passed": True, "evidence": "clean"}),
    annotate_result({"text": "no-collaborative-artifacts", "passed": True, "evidence": "clean"}),
]
expect_depth_status(_clean_results, "balanced", "pass", "clean text")
expect_depth_status(_clean_results, "all", "pass", "clean text")

_context_only = [
    annotate_result({"text": "no-anaphora", "passed": False, "evidence": "context warning"}),
]
expect_depth_status(_context_only, "balanced", "fail", "context warning only")
expect_depth_status(_context_only, "all", "fail", "context warning only")
expect_depth_actions(_context_only, "balanced", [], ["no-anaphora"], "context warning only")
expect_depth_actions(_context_only, "all", ["no-anaphora"], [], "context warning only")

_strong_only = [
    annotate_result({"text": "no-negative-parallelisms", "passed": False, "evidence": "strong warning"}),
]
expect_depth_status(_strong_only, "balanced", "fail", "strong warning only")
expect_depth_status(_strong_only, "all", "fail", "strong warning only")
expect_depth_actions(_strong_only, "balanced", ["no-negative-parallelisms"], [], "strong warning only")
expect_depth_actions(_strong_only, "all", ["no-negative-parallelisms"], [], "strong warning only")

_hard_only = [
    annotate_result({"text": "no-collaborative-artifacts", "passed": False, "evidence": "hard failure"}),
]
expect_depth_status(_hard_only, "balanced", "fail", "hard failure")
expect_depth_status(_hard_only, "all", "fail", "hard failure")


# --- Audit-shape: U5 dual-block assertions ---

print("\n=== audit-shape U5 (dual-block assertions) ===")
check_audit_shape = _grade.check_audit_shape

# U6 default-mode shape: agent-flagged item rendered inline in the audit body,
# no parallel **Agent-judgement reading** section, R8 next-step prompt.
_BOTH_BLOCKS = """**Audit summary**
Auto-detected: 1 of 48 flagged · Agent-assessed: 1 of 8 flagged
Severity: 0 hard fail · 2 strong warning · 0 context warning
Signal stacking: clear (weaker AI signals are not accumulating)

**Auto-detected**

! Em dashes: "still—keen"

**Agent-assessed**

! Structural monotony: every section follows the same arc

**Next steps**

Want the full coverage report, suggestions for edits, a full rewrite, or to save this audit as a file?"""

_PROGRAMMATIC_ONLY = """**Audit summary**
Auto-detected: 1 of 48 flagged · Agent-assessed: 0 of 0 flagged
Severity: 0 hard fail · 1 strong warning · 0 context warning
Signal stacking: clear (weaker AI signals are not accumulating)

**Auto-detected**

! Em dashes: "still—keen"

**Agent-assessed**

**Next steps**

Want suggestions?"""

_NEITHER_BLOCK_NOR_CLEAR = """**Some other report**

Nothing recognisable here.

Want help?"""

# Regression fixture for Finding #1 from PR #14 review (LAYER_1_BLOCK_RE
# previously required a middle clause and silently dropped no-quote
# structural-pattern blocks). The fixture mixes one quoted block with two
# no-quote structural blocks (now in U6 shape — no Action clause); the
# combined audit-body counter must enumerate all three.
_LAYER_1_NO_QUOTE_BLOCKS = """**Audit summary**
Auto-detected: 3 of 48 flagged · Agent-assessed: 0 of 0 flagged
Severity: 1 hard fail · 2 strong warning · 0 context warning
Signal stacking: clear (weaker AI signals are not accumulating)

**Auto-detected**

x Em dashes: "still—keen"
! Paragraph length uniformity
! Section scaffolding

**Agent-assessed**

**Next steps**

Want the full coverage report, suggestions for edits, a full rewrite, or to save this audit as a file?"""

# Suggestion-parity fixtures for PR #14 review Finding #8: the rewritten
# check now sums programmatic + agent-judgement flagged counts. Both fixtures
# extend _BOTH_BLOCKS (1 programmatic + 1 agent-judgement = 2 expected flags).
# _PARITY_BALANCED has two Try blocks (parity); _PARITY_MISMATCH has one.
_PARITY_BALANCED = _BOTH_BLOCKS + """

**Suggestions**

- "still—keen"
  Where: paragraph 1
  Why: Em-dash-set-off subordinate clauses are a high-signal AI tell.
  Try: keen and still

- Structural monotony: every section follows the same arc
  Where: across the piece
  Why: Uniform section shape signals templated production.
  Try: vary one section's pacing or omit the closing summary."""

_PARITY_MISMATCH = _BOTH_BLOCKS + """

**Suggestions**

- "still—keen"
  Where: paragraph 1
  Why: Em-dash-set-off subordinate clauses are a high-signal AI tell.
  Try: keen and still"""

# has-programmatic-block: U6 simplified the check to a single positive
# (Audit header present). The retired `has-agent-judgement-block` and
# `all-clear-line-format` checks are gone — the parallel agent-judgement
# block was retired by U6, and R9 retired the all-clear collapse.
_r = check_audit_shape("audit-shape-has-programmatic-block", _BOTH_BLOCKS)
if _r["passed"]:
    print("  ok: has-programmatic-block passes on the U6 default-mode shape")
else:
    FAILURES += 1; print(f"FAIL: has-programmatic-block on U6 default shape: {_r['evidence']}")

_r = check_audit_shape("audit-shape-has-programmatic-block", _PROGRAMMATIC_ONLY)
if _r["passed"]:
    print("  ok: has-programmatic-block passes on programmatic-only output")
else:
    FAILURES += 1; print(f"FAIL: has-programmatic-block on programmatic-only: {_r['evidence']}")

_r = check_audit_shape("audit-shape-has-programmatic-block", _NEITHER_BLOCK_NOR_CLEAR)
if not _r["passed"]:
    print("  ok: has-programmatic-block fails when no Audit header present")
else:
    FAILURES += 1; print("FAIL: has-programmatic-block should fail when no Audit header present")

# Legacy all-clear collapse must now fail has-programmatic-block (R9 retired
# the collapse — a real audit always carries the Audit header even on
# zero-flag drafts).
_LEGACY_ALL_CLEAR = "48 of 48 clear · agent reading clean · signal stacking: clear.\nWant suggestions?"
_r = check_audit_shape("audit-shape-has-programmatic-block", _LEGACY_ALL_CLEAR)
if not _r["passed"]:
    print("  ok: has-programmatic-block fails on legacy all-clear single-line shape (R9 retired)")
else:
    FAILURES += 1; print("FAIL: has-programmatic-block should fail on legacy all-clear shape")


# --- PR #14 review regressions: no-quote Layer 1, clean-form agent block,
# missing-Action candidate, suggestion-parity ---

print("\n--- PR #14 review regressions ---")

# Finding #1: LAYER_1_BLOCK_RE no-quote variant. _flag_blocks must return
# all three lines (one quoted + two no-quote structural).
_audit = _grade._audit_section(_LAYER_1_NO_QUOTE_BLOCKS)
_blocks = _grade._flag_blocks(_audit)
if len(_blocks) == 3:
    print(f"  ok: Finding #1 — _flag_blocks returns 3 blocks for 1-quoted + 2-no-quote fixture")
else:
    FAILURES += 1
    print(f"FAIL: Finding #1 — _flag_blocks should return 3 blocks; got {len(_blocks)}: {_blocks}")

# Finding #1: parity check counts the no-quote blocks too. Layer 1 = 3
# programmatic flags + 0 agent-judgement flags. Suggestions section is
# absent so the count is 0 — the assertion checks that _flag_blocks
# correctly enumerates 3, exposing any silent drop.
_r = check_audit_shape("suggestion-block-count-equals-flag-count", _LAYER_1_NO_QUOTE_BLOCKS)
if not _r["passed"] and "3 audit-body flag(s)" in _r["evidence"]:
    print(f"  ok: Finding #1 — suggestion-block-count counts 3 no-quote-aware audit-body flags")
else:
    FAILURES += 1
    print(f"FAIL: Finding #1 — suggestion-block-count should count 3 flags from no-quote fixture (got: {_r['evidence']})")

# Finding #4 (PR #14): programmatic + clean-form-agent shape. Retired by U6 —
# the parallel **Agent-judgement reading** block doesn't exist any more, so
# the dual-block fixture is gone too. The U6 _BOTH_BLOCKS fixture above
# (audit-body with inline agent-flagged item) covers the modern shape.

# Finding #9 (PR #14): the every-flag-block-has-explanation check enforced
# the Phase-3 trailing `Action: <verb>` clause on every Layer 1 candidate.
# U5 (R6) retired the Action clause — the check (and this fixture) were
# removed in lockstep. R6/R7 enforcement now lives in
# audit-shape-flagged-items-glyph-shape (covered above).

# Finding #8: suggestion-block-count-equals-flag-count must sum programmatic
# + agent-judgement flagged counts. Balanced fixture passes (2 flags = 2 Try);
# mismatch fixture fails (2 flags vs 1 Try).
_r = check_audit_shape("suggestion-block-count-equals-flag-count", _PARITY_BALANCED)
if _r["passed"]:
    print(f"  ok: Finding #8 — suggestion-parity passes when 2 flags (1 prog + 1 agent) match 2 suggestions")
else:
    FAILURES += 1
    print(f"FAIL: Finding #8 — suggestion-parity should pass on balanced dual-block fixture (got: {_r['evidence']})")

_r = check_audit_shape("suggestion-block-count-equals-flag-count", _PARITY_MISMATCH)
if not _r["passed"] and "2 audit-body flag(s)" in _r["evidence"] and "1 suggestion" in _r["evidence"]:
    print(f"  ok: Finding #8 — suggestion-parity fails when agent-judgement flag has no matching suggestion")
else:
    FAILURES += 1
    print(f"FAIL: Finding #8 — suggestion-parity should fail when 2 flags vs 1 Try (got: {_r['evidence']})")


# --- Audit-shape: U3 measurement-lock checks (audit-output redesign) ---
#
# These six checks land before the U4–U7 renderer changes ship. Synthetic
# new-shape fixtures pass; pre-U4 old-shape fixtures fail (the integration
# baseline is intentionally red on iteration-6 outputs and flips green as
# each renderer unit lands).

print("\n=== audit-shape U3 (measurement lock for new audit shape) ===")

_NEW_SHAPE_BOTH_BLOCKS = """**Audit summary**
Auto-detected: 2 of 12 flagged · Agent-assessed: 1 of 8 flagged
Severity: 0 hard fail · 2 strong warning · 1 context warning
Signal stacking: clear (weaker AI signals are not accumulating)

**Auto-detected**

! Em dashes: "EMDASH"

**Agent-assessed**

! Tonal uniformity
  - "register holds without breaks": single tonal arc

**Next steps**

Want the full coverage report, suggestions for edits, a full rewrite, or to save this audit as a file?"""

# Same shape but with a triggered signal-stacking line (for the R3 triggered branch).
_NEW_SHAPE_STACKING_TRIGGERED = """**Audit summary**
Auto-detected: 1 of 12 flagged · Agent-assessed: 0 of 8 flagged
Severity: 0 hard fail · 1 strong warning · 0 context warning
Signal stacking triggered: 5 of 4 threshold (em dashes, rule of three, tonal uniformity)

**Auto-detected**

! Em dashes: "EMDASH"

**Agent-assessed**

**Next steps**

Want the full coverage report, suggestions for edits, a full rewrite, or to save this audit as a file?"""

# Full-report shape with the new 4-column coverage table (for R15 / R18 checks).
_NEW_SHAPE_WITH_COVERAGE_TABLE = _NEW_SHAPE_BOTH_BLOCKS + """

**Auto-detected patterns** — 2 flagged of 12

| Pattern | Severity | Result | Detail |
| --- | --- | --- | --- |
| Em dashes | strong warning | Flagged | em dash detected |
| Curly quotes | context warning | Clear |  |
"""

# Pre-rework shape: audit header + old-shape body content (severity line carries
# inline signal-stacking suffix; coverage table is 3-column with Action). Used
# to verify the new-shape audit-shape checks reject pre-rework body content.
# Header is the new bold heading so the checks treat it as an audit (rather
# than vacuously passing on a missing header).
_OLD_SHAPE_FULL = """**Audit summary**
Severity: 0 hard fail · 1 strong warning · 0 context warning · signal stacking: clear
Signal stacking clear: no weaker AI-writing signals stacked.

! **Em dashes** — "still—keen" — Action: Fix

---

**Style** — 1 flagged of 6

| Pattern | Result | Action |
| --- | --- | --- |
| Em dashes | Flagged | Fix |
| Curly quotes | Clear |  |

**Next steps**

Want suggestions?"""

# Audit body that has merged the pre-U5 agent-judgement shape into the audit
# section — the regression case that flagged-items-glyph-shape catches.
_NEW_SHAPE_WITH_OLD_AGENT_LEAKAGE = """**Audit summary**
Auto-detected: 1 of 12 flagged · Agent-assessed: 1 of 8 flagged
Severity: 0 hard fail · 2 strong warning · 0 context warning
Signal stacking: clear (weaker AI signals are not accumulating)

**Auto-detected**

! Em dashes: "EMDASH"

**Agent-assessed**

- Tonal uniformity — Flagged: register holds without breaks

**Next steps**

Want the full coverage report, suggestions for edits, a full rewrite, or to save this audit as a file?"""

# No audit section at all — vacuous-true baseline for every U3 check.
_NO_AUDIT_AT_ALL = """**Some other report**

Nothing recognisable here.

Want help?"""

# Audit header present but no flagged items in body — vacuous-true for the
# glyph-shape predicate (it has nothing to assert against).
_NEW_SHAPE_NO_FLAG_BLOCKS = """**Audit summary**
Auto-detected: 0 of 12 flagged · Agent-assessed: 0 of 8 flagged
Severity: 0 hard fail · 0 strong warning · 0 context warning
Signal stacking: clear (weaker AI signals are not accumulating)

**Auto-detected**

**Agent-assessed**

**Next steps**

Want the full coverage report, suggestions for edits, a full rewrite, or to save this audit as a file?"""

# --- audit-shape-counts-line (R1) ---
print("\n--- audit-shape-counts-line ---")
_r = check_audit_shape("audit-shape-counts-line", _NEW_SHAPE_BOTH_BLOCKS)
if _r["passed"]:
    print("  ok: counts-line passes on synthetic new-shape audit body")
else:
    FAILURES += 1; print(f"FAIL: counts-line on new shape: {_r['evidence']}")

_r = check_audit_shape("audit-shape-counts-line", _OLD_SHAPE_FULL)
if not _r["passed"]:
    print("  ok: counts-line fails on pre-U4 old-shape audit body (intentionally red)")
else:
    FAILURES += 1; print("FAIL: counts-line should fail on pre-U4 old shape")

_r = check_audit_shape("audit-shape-counts-line", _NO_AUDIT_AT_ALL)
if _r["passed"] and "vacuously" in _r["evidence"]:
    print("  ok: counts-line vacuously passes when no audit section is present")
else:
    FAILURES += 1; print(f"FAIL: counts-line should vacuously pass with no audit section (got: {_r['evidence']})")

# --- audit-shape-severity-line (R2) ---
print("\n--- audit-shape-severity-line ---")
_r = check_audit_shape("audit-shape-severity-line", _NEW_SHAPE_BOTH_BLOCKS)
if _r["passed"]:
    print("  ok: severity-line passes on synthetic new-shape (no inline signal-stacking suffix)")
else:
    FAILURES += 1; print(f"FAIL: severity-line on new shape: {_r['evidence']}")

_r = check_audit_shape("audit-shape-severity-line", _OLD_SHAPE_FULL)
if not _r["passed"]:
    print("  ok: severity-line fails on pre-U4 shape (line carries inline signal-stacking suffix)")
else:
    FAILURES += 1; print("FAIL: severity-line should fail when line carries the inline signal-stacking suffix")

_r = check_audit_shape("audit-shape-severity-line", _NO_AUDIT_AT_ALL)
if _r["passed"] and "vacuously" in _r["evidence"]:
    print("  ok: severity-line vacuously passes when no audit section is present")
else:
    FAILURES += 1; print(f"FAIL: severity-line should vacuously pass with no audit section (got: {_r['evidence']})")

# --- audit-shape-signal-stacking-line (R3) ---
print("\n--- audit-shape-signal-stacking-line ---")
_r = check_audit_shape("audit-shape-signal-stacking-line", _NEW_SHAPE_BOTH_BLOCKS)
if _r["passed"]:
    print("  ok: signal-stacking-line passes on the clear shape")
else:
    FAILURES += 1; print(f"FAIL: signal-stacking-line on clear new shape: {_r['evidence']}")

_r = check_audit_shape("audit-shape-signal-stacking-line", _NEW_SHAPE_STACKING_TRIGGERED)
if _r["passed"]:
    print("  ok: signal-stacking-line passes on the triggered + threshold shape")
else:
    FAILURES += 1; print(f"FAIL: signal-stacking-line on triggered shape: {_r['evidence']}")

_r = check_audit_shape("audit-shape-signal-stacking-line", _OLD_SHAPE_FULL)
if not _r["passed"]:
    print("  ok: signal-stacking-line fails on pre-U4 shape (no stand-alone R3 line)")
else:
    FAILURES += 1; print("FAIL: signal-stacking-line should fail when no stand-alone R3 line is present")

_r = check_audit_shape("audit-shape-signal-stacking-line", _NO_AUDIT_AT_ALL)
if _r["passed"] and "vacuously" in _r["evidence"]:
    print("  ok: signal-stacking-line vacuously passes when no audit section is present")
else:
    FAILURES += 1; print(f"FAIL: signal-stacking-line should vacuously pass with no audit section (got: {_r['evidence']})")

# --- audit-shape-flagged-items-glyph-shape (R6, R7) ---
print("\n--- audit-shape-flagged-items-glyph-shape ---")
_r = check_audit_shape("audit-shape-flagged-items-glyph-shape", _NEW_SHAPE_BOTH_BLOCKS)
if _r["passed"]:
    print("  ok: glyph-shape passes when both blocks use glyph + bold-name openers")
else:
    FAILURES += 1; print(f"FAIL: glyph-shape on new shape: {_r['evidence']}")

_r = check_audit_shape("audit-shape-flagged-items-glyph-shape", _NEW_SHAPE_WITH_OLD_AGENT_LEAKAGE)
if not _r["passed"] and "Label — Flagged" in _r["evidence"]:
    print("  ok: glyph-shape fails when pre-U5 '- Label — Flagged:' shape leaks into the audit section")
else:
    FAILURES += 1; print(f"FAIL: glyph-shape should fail on old-agent-leakage fixture (got: {_r['evidence']})")

_r = check_audit_shape("audit-shape-flagged-items-glyph-shape", _NEW_SHAPE_NO_FLAG_BLOCKS)
if _r["passed"] and "vacuously" in _r["evidence"]:
    print("  ok: glyph-shape vacuously passes when audit body has no flagged items")
else:
    FAILURES += 1; print(f"FAIL: glyph-shape should vacuously pass with no flag blocks (got: {_r['evidence']})")

_r = check_audit_shape("audit-shape-flagged-items-glyph-shape", _NO_AUDIT_AT_ALL)
if _r["passed"] and "vacuously" in _r["evidence"]:
    print("  ok: glyph-shape vacuously passes when no audit section is present")
else:
    FAILURES += 1; print(f"FAIL: glyph-shape should vacuously pass with no audit section (got: {_r['evidence']})")

# --- audit-shape-severity-in-coverage-table (R15) ---
print("\n--- audit-shape-severity-in-coverage-table ---")
_r = check_audit_shape("audit-shape-severity-in-coverage-table", _NEW_SHAPE_WITH_COVERAGE_TABLE)
if _r["passed"]:
    print("  ok: severity-in-coverage-table passes on the new 4-column header")
else:
    FAILURES += 1; print(f"FAIL: severity-in-coverage-table on new 4-column header: {_r['evidence']}")

_r = check_audit_shape("audit-shape-severity-in-coverage-table", _OLD_SHAPE_FULL)
if not _r["passed"]:
    print("  ok: severity-in-coverage-table fails on pre-U4 3-column header")
else:
    FAILURES += 1; print("FAIL: severity-in-coverage-table should fail on pre-U4 3-column header")

_r = check_audit_shape("audit-shape-severity-in-coverage-table", _NEW_SHAPE_BOTH_BLOCKS)
if _r["passed"] and "vacuously" in _r["evidence"]:
    print("  ok: severity-in-coverage-table vacuously passes when no coverage tables are rendered (default-mode audit)")
else:
    FAILURES += 1; print(f"FAIL: severity-in-coverage-table should vacuously pass without coverage tables (got: {_r['evidence']})")

# --- audit-shape-no-action-column (R18) ---
print("\n--- audit-shape-no-action-column ---")
_r = check_audit_shape("audit-shape-no-action-column", _NEW_SHAPE_WITH_COVERAGE_TABLE)
if _r["passed"]:
    print("  ok: no-action-column passes on the new 4-column header (Action removed)")
else:
    FAILURES += 1; print(f"FAIL: no-action-column on new 4-column header: {_r['evidence']}")

_r = check_audit_shape("audit-shape-no-action-column", _OLD_SHAPE_FULL)
if not _r["passed"]:
    print("  ok: no-action-column fails on pre-U4 3-column header (Action present)")
else:
    FAILURES += 1; print("FAIL: no-action-column should fail when Action column is present")

_r = check_audit_shape("audit-shape-no-action-column", _NEW_SHAPE_BOTH_BLOCKS)
if _r["passed"] and "vacuously" in _r["evidence"]:
    print("  ok: no-action-column vacuously passes when no coverage tables are rendered")
else:
    FAILURES += 1; print(f"FAIL: no-action-column should vacuously pass without coverage tables (got: {_r['evidence']})")


# --- Human passthrough: opinion piece ---
print("\n=== human-opinion-passthrough ===")
opinion_text = Path(__file__).resolve().parents[1].joinpath("samples/human-sourced/legacy/10-human-opinion.md").read_text()
for check_name in ALL_CHECKS:
    if check_name in {
        "no-staccato-sequences",
        "no-negative-parallelisms",
        # DR-159 rate checks. These flag a calibrated share of human prose by
        # design (24%, 27%, and 37% of the human corpus respectively). This
        # 476-word opinion piece runs 39.9 nominalisations and 4.2 subject
        # relatives per 1000 words, so it sits in that share. Excluded here
        # rather than raising the thresholds, which would fit the instrument
        # to two fixtures.
        "no-nominalisation-rate",
        "no-that-relative-rate",
        # DR-66: the same principle. This piece runs 8.4 passive verbs per 1000
        # words, inside the 29% of human prose #68 flags by design.
        "no-passive-voice-rate",
        # DR-79A: the same principle again. This piece's sentence-length spread
        # is 7.56 across 36 sentences, inside the 11% of human prose #52 flags
        # at its calibrated threshold of 9.
        "sentence-length-variance",
    }:
        continue
    expect_pass(check_name, opinion_text, f"human opinion piece ({check_name})")
expect_fail(
    "no-negative-parallelisms",
    opinion_text,
    "human opinion contains a negative-positive because/not-because construction",
)

# --- Human passthrough: instructional piece ---
print("\n=== human-instructional-passthrough ===")
instructional_text = Path(__file__).resolve().parents[1].joinpath("samples/human-sourced/legacy/11-human-instructional.md").read_text()
for check_name in ALL_CHECKS:
    if check_name in {
        "no-staccato-sequences",
        "no-performed-candour",
        # DR-159: this instructional fixture runs 6.7 subject relatives per
        # 1000 words, inside the 27% of human prose the check flags by design.
        "no-that-relative-rate",
        # DR-66: this piece runs 25.6 `it` pronouns per 1000 words, inside the
        # 18% of human prose #69 flags by design.
        "no-it-pronoun-rate",
        "no-negative-parallelisms",
        "overall-signal-stacking",
    }:
        continue
    expect_pass(check_name, instructional_text, f"human instructional piece ({check_name})")
expect_fail(
    "no-negative-parallelisms",
    instructional_text,
    "human instructional prose contains cross-sentence negative parallelism",
)
expect_fail("overall-signal-stacking", instructional_text, "human instructional prose reaches the aggregate signal threshold")


# --- U7: --judgement-file CLI flag + agent_judgement overlay validation ---

print("\n=== U7 --judgement-file overlay loader ===")

import json as _u7_json
import subprocess as _u7_subprocess
import tempfile as _u7_tempfile

JudgementOverlayError = _grade.JudgementOverlayError
load_agent_judgement_overlay = _grade.load_agent_judgement_overlay


def _u7_write_overlay(payload):
    """Write a JSON payload to a temp file and return its path."""
    handle = _u7_tempfile.NamedTemporaryFile(
        "w", suffix=".json", delete=False, encoding="utf-8",
    )
    _u7_json.dump(payload, handle)
    handle.close()
    return handle.name


def _u7_expect_overlay_error(payload_or_text, fragment, reason, raw_text=False):
    """Write payload to a temp file, expect JudgementOverlayError containing fragment."""
    global FAILURES
    if raw_text:
        handle = _u7_tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8",
        )
        handle.write(payload_or_text)
        handle.close()
        path = handle.name
    else:
        path = _u7_write_overlay(payload_or_text)
    try:
        load_agent_judgement_overlay(path)
    except JudgementOverlayError as exc:
        if fragment in str(exc):
            print(f"  ok: {reason} → {exc}")
        else:
            FAILURES += 1
            print(f"FAIL: {reason}: error did not mention {fragment!r}; got: {exc}")
    else:
        FAILURES += 1
        print(f"FAIL: {reason}: expected JudgementOverlayError, none raised")


# Happy path: valid wrapped overlay loads cleanly.
_u7_valid = {
    "agent_judgement": [
        {
            "id": "tonal_uniformity",
            "status": "flagged",
            "severity": "strong_warning",
            "answer": "register holds without breaks",
            "evidence": {},
        },
    ],
}
_u7_loaded = load_agent_judgement_overlay(_u7_write_overlay(_u7_valid))
if _u7_loaded == _u7_valid["agent_judgement"]:
    print("  ok: happy path — wrapped overlay loads to a single cleaned record")
else:
    FAILURES += 1
    print(f"FAIL: happy path: expected {_u7_valid['agent_judgement']}, got {_u7_loaded}")


# Severity defaulting: agent omits severity → registry value is filled in.
_u7_no_severity = {
    "agent_judgement": [
        {
            "id": "tonal_uniformity",  # registry severity = strong_warning
            "status": "flagged",
            "answer": "register holds without breaks",
            "evidence": {},
        },
    ],
}
_u7_defaulted = load_agent_judgement_overlay(_u7_write_overlay(_u7_no_severity))
if _u7_defaulted[0]["severity"] == "strong_warning":
    print("  ok: omitted severity defaults from judgement.json registry")
else:
    FAILURES += 1
    print(f"FAIL: severity default: expected 'strong_warning', got {_u7_defaulted[0]['severity']!r}")


# Permissive on extras: extra item fields are accepted but stripped from the cleaned record.
_u7_with_extras = {
    "agent_judgement": [
        {
            "id": "tonal_uniformity",
            "status": "flagged",
            "severity": "strong_warning",
            "answer": "register holds without breaks",
            "evidence": {},
            "agent_notes": "internal scratch the agent wanted to keep",
            "confidence": 0.85,
        },
    ],
}
_u7_cleaned = load_agent_judgement_overlay(_u7_write_overlay(_u7_with_extras))
if set(_u7_cleaned[0]) == {"id", "status", "severity", "answer", "evidence"}:
    print("  ok: extra item fields are accepted and stripped from the cleaned record")
else:
    FAILURES += 1
    print(f"FAIL: extras: cleaned record keys {sorted(_u7_cleaned[0])} should be the contract set")


# All-clear file → all items injected with status=clear; renderer shows no flagged items.
_u7_all_clear = {
    "agent_judgement": [
        {"id": "tonal_uniformity", "status": "clear", "severity": "strong_warning",
         "answer": "register breaks at least once", "evidence": {}},
        {"id": "structural_monotony", "status": "clear", "severity": "context_warning",
         "answer": "sections vary", "evidence": {}},
    ],
}
_u7_all_clear_items = load_agent_judgement_overlay(_u7_write_overlay(_u7_all_clear))
_u7_clean_render = format_two_layer(
    [], depth="balanced", mode="default",
    agent_judgement_items=_u7_all_clear_items,
)
if "Agent-assessed: 0 of 2 flagged" in _u7_clean_render:
    print("  ok: all-clear overlay renders 'Agent-assessed: 0 of 2 flagged' (no collapse)")
else:
    FAILURES += 1
    print(f"FAIL: all-clear overlay counts line wrong; got:\n{_u7_clean_render[:400]}")


# --- Error paths: every failure mode names the offending input clearly. ---

# Missing path → clear error citing the path.
try:
    load_agent_judgement_overlay("/nonexistent/path-9999.json")
except JudgementOverlayError as exc:
    if "/nonexistent/path-9999.json" in str(exc):
        print(f"  ok: missing-path error names the path → {exc}")
    else:
        FAILURES += 1
        print(f"FAIL: missing-path error did not include the path; got: {exc}")
else:
    FAILURES += 1
    print("FAIL: missing-path: expected JudgementOverlayError, none raised")

# Malformed JSON → parse error.
_u7_expect_overlay_error(
    "{not json at all", "invalid JSON", "malformed JSON",
    raw_text=True,
)

# Bare-array form rejected (must be wrapped).
_u7_expect_overlay_error(
    [], "must be an object", "bare-array top level",
)

# Missing 'agent_judgement' key.
_u7_expect_overlay_error(
    {"items": []}, "agent_judgement", "missing top-level 'agent_judgement' key",
)

# 'agent_judgement' is not a list.
_u7_expect_overlay_error(
    {"agent_judgement": {"id": "x"}}, "must be a list",
    "'agent_judgement' is an object instead of a list",
)

# Item missing required field — message names the item id and the missing field.
_u7_expect_overlay_error(
    {"agent_judgement": [
        {"id": "tonal_uniformity", "status": "flagged", "severity": "strong_warning",
         "answer": "x"},  # missing 'evidence'
    ]},
    "tonal_uniformity",
    "missing required field error names the item id",
)
_u7_expect_overlay_error(
    {"agent_judgement": [
        {"id": "tonal_uniformity", "status": "flagged", "severity": "strong_warning",
         "answer": "x"},  # missing 'evidence'
    ]},
    "evidence",
    "missing required field error names the missing field",
)

# Invalid status value.
_u7_expect_overlay_error(
    {"agent_judgement": [
        {"id": "tonal_uniformity", "status": "maybe", "severity": "strong_warning",
         "answer": "x", "evidence": {}},
    ]},
    "invalid status",
    "invalid status names the bad value",
)

# Invalid severity value.
_u7_expect_overlay_error(
    {"agent_judgement": [
        {"id": "tonal_uniformity", "status": "flagged", "severity": "medium",
         "answer": "x", "evidence": {}},
    ]},
    "invalid severity",
    "invalid severity names the bad value",
)

# Severity omitted on an unknown id (cannot default from registry).
_u7_expect_overlay_error(
    {"agent_judgement": [
        {"id": "made_up_item_id", "status": "flagged",
         "answer": "x", "evidence": {}},
    ]},
    "cannot default",
    "missing severity on unknown id surfaces a clear error",
)

# Evidence must be an object.
_u7_expect_overlay_error(
    {"agent_judgement": [
        {"id": "tonal_uniformity", "status": "flagged", "severity": "strong_warning",
         "answer": "x", "evidence": "not an object"},
    ]},
    "evidence",
    "evidence-not-an-object names the evidence field",
)


# --- Integration: human_report and format_two_layer accept the overlay. ---

print("\n=== U7 contract + renderer integration with overlay ===")

_u7_overlay_items = load_agent_judgement_overlay(_u7_write_overlay(_u7_valid))
_u7_contract = human_report([], agent_judgement_items=_u7_overlay_items)
if _u7_contract["agent_judgement"] == _u7_overlay_items:
    print("  ok: human_report(overlay) injects items into contract.agent_judgement[]")
else:
    FAILURES += 1
    print(f"FAIL: contract.agent_judgement should match overlay; got {_u7_contract['agent_judgement']}")

# Backward-compat: human_report() with no overlay still returns []. Diff baselines depend on this.
_u7_default_contract = human_report([])
if _u7_default_contract["agent_judgement"] == []:
    print("  ok: human_report() with no overlay still returns agent_judgement=[] (diff-baseline stable)")
else:
    FAILURES += 1
    print(f"FAIL: default contract.agent_judgement should be []; got {_u7_default_contract['agent_judgement']}")

# Renderer: overlay items appear in default-mode markdown.
_u7_markdown = format_two_layer(
    [], depth="balanced", mode="default",
    agent_judgement_items=_u7_overlay_items,
)
if "Tonal uniformity" in _u7_markdown and "register holds without breaks" in _u7_markdown:
    print("  ok: format_two_layer(overlay) renders the agent-judgement item inline")
else:
    FAILURES += 1
    print(f"FAIL: overlay item not rendered in markdown; got:\n{_u7_markdown[:400]}")


# --- CLI subprocess smoke tests: --judgement-file is wired into main(). ---

print("\n=== U7 --judgement-file CLI subprocess smoke tests ===")

_u7_grade_path = ROOT / "human-eyes" / "scripts" / "grade.py"
_u7_sample_path = ROOT / "dev" / "evals" / "samples" / "synthetic" / "synthetic-hard-fail-only.md"

# Legacy overlay invocations fail with the migration command.
_u7_overlay_path = _u7_write_overlay(_u7_valid)
_u7_md = _u7_subprocess.run(
    ["python3", str(_u7_grade_path), "--format", "markdown", "--depth", "balanced",
     "--judgement-file", _u7_overlay_path, str(_u7_sample_path)],
    capture_output=True, text=True,
)
if _u7_md.returncode == 2 and "Legacy grader invocation" in _u7_md.stderr:
    print("  ok: legacy markdown --judgement-file invocation returns migration guidance")
else:
    FAILURES += 1
    print(f"FAIL: CLI markdown mode: rc={_u7_md.returncode}; stderr={_u7_md.stderr[:300]}")

# JSON uses the same fail-closed migration behavior.
_u7_js = _u7_subprocess.run(
    ["python3", str(_u7_grade_path), "--format", "json",
     "--judgement-file", _u7_overlay_path, str(_u7_sample_path)],
    capture_output=True, text=True,
)
if _u7_js.returncode == 2 and "Legacy grader invocation" in _u7_js.stderr:
    print("  ok: legacy JSON --judgement-file invocation returns migration guidance")
else:
    FAILURES += 1
    print(f"FAIL: CLI json mode: rc={_u7_js.returncode}; stderr={_u7_js.stderr[:300]}")

# Missing file path exits non-zero with a clear stderr message.
_u7_missing = _u7_subprocess.run(
    ["python3", str(_u7_grade_path), "--format", "markdown",
     "--judgement-file", "/nonexistent/u7-test.json", str(_u7_sample_path)],
    capture_output=True, text=True,
)
if _u7_missing.returncode == 2 and "Legacy grader invocation" in _u7_missing.stderr:
    print("  ok: legacy missing --judgement-file invocation returns migration guidance")
else:
    FAILURES += 1
    print(f"FAIL: CLI missing path: rc={_u7_missing.returncode}; stderr={_u7_missing.stderr[:300]}")

# Legacy no-subcommand invocation is never reinterpreted as a surface scan.
_u7_no_overlay = _u7_subprocess.run(
    ["python3", str(_u7_grade_path), "--format", "json", str(_u7_sample_path)],
    capture_output=True, text=True,
)
if _u7_no_overlay.returncode == 2 and "Legacy grader invocation" in _u7_no_overlay.stderr:
    print("  ok: legacy no-subcommand invocation returns migration guidance")
else:
    FAILURES += 1
    print(f"FAIL: CLI no overlay: rc={_u7_no_overlay.returncode}; stderr={_u7_no_overlay.stderr[:300]}")


# --- 2026-07-17 hygiene-pass checker-finding regressions ---
# Source-card focused checks exposed counting and eligibility defects.
# Each assertion below encodes the corrected behaviour.

print("\n=== hygiene-pass regressions ===")

# #26: singular+plural list entries must not double-count one occurrence.
expect_pass("no-ghost-spectral-density",
    "The echoes faded across the valley before dawn. The whispers stopped.",
    "#26: two spectral words must count as 2, not 4")

# #7: a repeated word must count once per occurrence, not once per entry.
expect_fail("no-ai-vocabulary-clustering",
    "We delve into the data. We delve into the code. We delve into the tests.",
    "#7: 'delve' three times in one paragraph is a cluster of 3")

# #7: nested entries (word inside a longer phrase) must count one span once.
expect_pass("no-ai-vocabulary-clustering",
    "They offer a valuable insight and provide a valuable insight.",
    "#7: two phrases containing two nested words must count as 2, not 4")

# #52: documented eligibility skips prose under 100 words or under 6 sentences.
expect_pass("sentence-length-variance",
    ("The committee reviewed every submission that arrived before the posted "
     "deadline and sorted all of them into three separate piles organised by "
     "their primary topic area. Each reviewer then read through the complete "
     "pile assigned to them and wrote one short structured report on every "
     "single entry that the pile contained. The finished reports were then "
     "collated into a single shared document that the committee chair "
     "circulated to the whole committee two days before the meeting. All the "
     "members arrived at the meeting having read the document and voted on "
     "every entry in one long session that ran for roughly four hours."),
    "#52: 100+ words but only 4 sentences must be skipped, not scored")

# #27: singular+inflected list entries must not double-count one occurrence.
expect_pass("no-quietness-obsession",
    "The quietly confident team settled in for the afternoon meeting.",
    "#27: two quietness words must count as 2, not 4")

# #27: documented words hum/humming, soft, and settle must be counted.
expect_fail("no-quietness-obsession",
    "The hum of the fans went soft. A low hum settled over the room as "
    "things settle into stillness.",
    "#27: six documented quietness words including hum and soft")

# #27: 'hum' must not match inside unrelated words like 'human'.
expect_pass("no-quietness-obsession",
    "Every human on the humid subcontinent heard the announcement clearly.",
    "#27: human/humid must not count as hum")

# #31a: lightning bolt, rightwards arrow, and recycling glyphs are candidates.
expect_fail("no-unicode-flair",
    "Ship fast ⚡ iterate ➡ recycle wins ♻",
    "#31a: three decorative glyphs missed by the prior character class")

# --- 2026-07-17 defect-sweep family-1 regressions ---
# Documented phrases the runtime never fired on. Approved as additions.

print("\n=== defect-sweep family-1 regressions ===")

# #21 documents the excellent-point family as its own example.
expect_fail("no-collaborative-artifacts",
    "Excellent point! That framing works much better.",
    "family-1: excellent-point praise is a documented #21 artifact")
expect_fail("no-collaborative-artifacts",
    "You raise an excellent point about the deadline.",
    "family-1: raised-excellent-point variant")

# #19/#21 document the ASCII form; curly apostrophes must match too.
expect_fail("no-collaborative-artifacts",
    "You’re absolutely right about that.",
    "family-1: curly-apostrophe you're absolutely right")

# #42 documents 'here's the thing'; curly apostrophe must match too.
expect_fail("no-manufactured-insight",
    "But here’s the thing about all of it.",
    "family-1: curly-apostrophe here's the thing")

# Family 1: documented filler transitions must fire on #22.
expect_fail("no-filler-phrases",
    "In today’s fast-paced world, teams move quickly.",
    "family-1: README's own #22 example, curly apostrophe")
expect_fail("no-filler-phrases",
    "That being said, the plan still works as designed.",
    "family-1: Grammarly transition 'That being said'")
expect_fail("no-filler-phrases",
    "From a broader perspective, the results hold.",
    "family-1: documented transition 'From a broader perspective'")
expect_fail("no-filler-phrases",
    "As technology continues to evolve, our tooling adapts.",
    "family-1: Guo transition 'As technology continues to evolve'")

# Family 1: documented qualifiers count toward #23 density; singles stay clear.
expect_fail("no-excessive-hedging",
    "Generally speaking, results vary. Arguably, they typically improve to some extent.",
    "family-1: four stacked documented qualifiers")
expect_pass("no-excessive-hedging",
    "Typically, the build finishes in about ten minutes.",
    "family-1: one qualifier alone must not flag")

# Family 1: #9 comma-form two-clause contrastive negation (Stockton C01).
expect_fail("no-negative-parallelisms",
    "We're not just building a product, we're creating an experience.",
    "family-1: comma-form not-just contrast with repeated subject")
expect_fail("no-negative-parallelisms",
    "They aren't just using AI, they're restructuring the whole team around it.",
    "family-1: comma-form aren't-just contrast")
# Controls: single-clause forms are ordinary usage and must stay clear.
expect_pass("no-negative-parallelisms",
    "The fee isn't just about administration costs.",
    "family-1 control: bare isn't-just-about with no contrast clause")
expect_pass("no-negative-parallelisms",
    "The grant covers more than just travel.",
    "family-1 control: more-than-just as ordinary quantification")

# #9 bare-noun subject resuming with a deictic (Stockton example shape).
expect_fail("no-negative-parallelisms",
    "AI isn’t just evolving—it’s accelerating!",
    "#9: bare-noun subject with deictic resumption")

# Single-clause contrast stand-ins feed stacking only (Mae, 2026-07-17).
expect_pass("no-negative-parallelisms",
    "The grant covers more than just travel.",
    "single-clause form must not fail #9 directly")
expect_pass("overall-signal-stacking",
    "At its core, the summary works. I hope this helps!",
    "three stacked points stay under the threshold")
expect_fail("overall-signal-stacking",
    "At its core, the summary works. I hope this helps! The offer goes beyond the price.",
    "single-clause contrast stand-in tips stacking to four")

# --- #53 flip: windowed lexical diversity, flag high (Mae, 2026-07-17) ---

print("\n=== #53 windowed diversity regressions ===")

# High-diversity text (every word unique) must flag.
_unique_words = " ".join(f"w{chr(97+i%26)}{chr(97+(i//26)%26)}{chr(97+(i//676)%26)}q" for i in range(200))
expect_fail("vocabulary-diversity", _unique_words,
    "#53: maximal windowed diversity is the AI direction")

# Repetitive long text must stay clear (old rule would have flagged it).
_repetitive = ("The strategy emphasises customer outcomes and the strategy "
               "emphasises operational efficiency for the team. ") * 20
expect_pass("vocabulary-diversity", _repetitive,
    "#53: heavy repetition is no longer the flagged direction")

# Under 150 words stays skipped.
expect_pass("vocabulary-diversity", "Short note. " * 30,
    "#53: sub-window text skipped")

# Two-tier evidence: >=0.74 states the human-range tier.
_r = ALL_CHECKS["vocabulary-diversity"](_unique_words)
if "above the observed human range" not in _r["evidence"]:
    FAILURES += 1
    print(f"FAIL: #53 upper tier missing from evidence: {_r['evidence']}")
else:
    print("  ok: #53 upper-tier evidence present at extreme diversity")

# --- DR-113: #19 pasted-chat residue families (Mae, 2026-07-17) ---
print("\n=== DR-113 #19 residue families ===")
expect_fail("no-collaborative-artifacts",
    "I'm sorry, but I can't help with that request.",
    "DR-113: apology-led refusal")
expect_fail("no-collaborative-artifacts",
    "As an AI language model, I don't have personal opinions.",
    "DR-113: AI-identity disclaimer")
expect_fail("no-collaborative-artifacts",
    "Certainly, here are the main considerations for the rollout.",
    "DR-113: sentence-opening Certainly without exclamation")
expect_fail("no-collaborative-artifacts",
    "Want me to expand on any of these sections?",
    "DR-113: offer-to-continue question")
expect_fail("no-collaborative-artifacts",
    "Here's a detailed breakdown of the quarterly results.",
    "DR-113: here's-a-detailed-breakdown residue")
expect_pass("no-collaborative-artifacts",
    "The certainty of the schedule was never in doubt.",
    "DR-113 control: 'certainty' must not match Certainly")

# --- DR-114 components 1-2: platform residue and possessive bracket labels ---
print("\n=== DR-114 #39 additions ===")
expect_fail("no-placeholder-residue",
    "The market outlook remains positive citeturn0search2 according to analysts.",
    "DR-114: ChatGPT citeturn token")
expect_fail("no-placeholder-residue",
    "See the full report contentReference[oaicite:3] for the methodology.",
    "DR-114: contentReference oaicite token")
expect_fail("no-placeholder-residue",
    "Read more at https://example.com/guide?utm_source=chatgpt.com today.",
    "DR-114: chatgpt.com URL tracker")
expect_fail("no-placeholder-residue",
    "Dear [Subject's Name], thank you for reaching out to our team.",
    "DR-114: possessive bracket label")
expect_pass("no-placeholder-residue",
    "The results [sic] were later replicated [1] in two labs.",
    "DR-114 control: editorial brackets and citation numbers stay clear")

# --- DR-115 components 4 and 6: paragraph anaphora and heading one-liners ---
print("\n=== DR-115 #51a/#38a additions ===")
expect_fail("no-paragraph-anaphora",
    "Customers want faster onboarding and clearer pricing pages.\n\n"
    "Customers also expect the invoice history to export cleanly.\n\n"
    "Customers who churn cite the same three support gaps every quarter.",
    "DR-115: three consecutive paragraphs opening with the same word")
expect_pass("no-paragraph-anaphora",
    "Customers want faster onboarding and clearer pricing pages.\n\n"
    "Billing exports were the second theme in the interviews.\n\n"
    "Customers who churn cite the same three support gaps every quarter.",
    "DR-115 control: no three-paragraph run")
expect_pass("no-paragraph-anaphora",
    "The onboarding flow is slow on the first login.\n\n"
    "The invoices export cleanly once the account is verified.\n\n"
    "The support queue clears within a day.",
    "DR-115 control: trivial opener 'The' is excluded")
expect_fail("no-paragraph-anaphora",
    "Customers want faster onboarding and clearer pricing pages.\n\n"
    "## Billing\n\n"
    "Customers also expect the invoice history to export cleanly.\n\n"
    "Customers who churn cite the same three support gaps every quarter.",
    "DR-115: a heading between paragraphs does not break the run")
expect_pass("no-paragraph-anaphora",
    "- Customers want speed\n- Customers want clarity\n- Customers want exports",
    "DR-115 control: list blocks are not paragraphs")
expect_fail("no-heading-one-liners",
    "## Performance\n\nSpeed matters.\n\n"
    "The benchmark suite covers cold starts, warm paths, and the worst-case joins we see in production telemetry.\n\n"
    "## Security\n\nWe take security seriously.\n\n"
    "Access tokens rotate hourly and the audit log is append-only.",
    "DR-115: two headings each followed by a one-sentence paragraph")
expect_pass("no-heading-one-liners",
    "## Performance\n\nSpeed matters.\n\n"
    "The benchmark suite covers cold starts and warm paths.",
    "DR-115 control: a single occurrence stays clear (Blader fixture)")
expect_pass("no-heading-one-liners",
    "## Performance\n\nThe suite covers cold starts. It also covers warm paths.\n\n"
    "## Security\n\nTokens rotate hourly. The audit log is append-only.",
    "DR-115 control: multi-sentence paragraphs under headings stay clear")
expect_pass("no-heading-one-liners",
    "## Performance\n\n- cold starts\n- warm paths\n\n"
    "## Security\n\n- token rotation\n- audit logging",
    "DR-115 control: a list under a heading is not a one-line paragraph")

# --- DR-150: #23 hedging watch-list expansion ---
print("\n=== DR-150 #23 additions ===")
expect_fail("no-excessive-hedging",
    "Results may vary depending on the configuration you start from. "
    "In most cases the defaults are fine for small teams. "
    "More often than not, the cache hides the real cost until launch.",
    "DR-150: three new hedge cues reach the density threshold")
expect_fail("no-excessive-hedging",
    "Generally speaking, the migration is safe. It depends on the size of the tenant. "
    "In general, the older exports are the risky ones.",
    "DR-150: new cues stack with an existing cue")
expect_pass("no-excessive-hedging",
    "Results may vary between regions. The benchmark covers the four largest tenants "
    "and the deploy finished inside the window.",
    "DR-150 control: a single hedge stays under the threshold")
expect_pass("no-excessive-hedging",
    "As a rule the exports finish overnight. In general, the queue clears by morning. "
    "The alerting has paged twice this quarter.",
    "DR-150 control: two hedges stay under the threshold")

# --- DR-118: modal stacks (#60), can-potentially (#23), intensifiers (#7) ---
print("\n=== DR-118 additions ===")
expect_fail("no-modal-stacks",
    "The new cache can potentially often reduce latency for most tenants.",
    "DR-118: three qualifiers stacked in one sentence")
expect_pass("no-modal-stacks",
    "The cache can often help. Results might improve. Costs may fall.",
    "DR-118 control: qualifiers spread across sentences stay clear")
expect_pass("no-modal-stacks",
    "In May the team can meet to review the typical rollout.",
    "DR-118 control: capitalised May and non-adverb typical do not count")
expect_fail("no-excessive-hedging",
    "This can potentially improve results. It tends to help. Generally speaking, it works.",
    "DR-118: can potentially joins the #23 density list")
expect_fail("no-ai-vocabulary-clustering",
    "The change profoundly reshaped the team. It significantly altered planning and fundamentally moved the roadmap.",
    "DR-118: three AI-leaning intensifiers cluster in one paragraph")
expect_pass("no-ai-vocabulary-clustering",
    "The change profoundly reshaped the team.\n\nPlanning shifted the next quarter.\n\nThe roadmap moved a month later.",
    "DR-118 control: one intensifier per paragraph stays clear")

# --- DR-119: #22 generalisations and #24 peppy-ending shape ---
print("\n=== DR-119 #22/#24 additions ===")
expect_fail("no-filler-phrases",
    "It's important to remember that the queue drains overnight. "
    "As AI continues to evolve, the key takeaway is that at the heart of this debate "
    "we all have the ability to adapt. It must also be noted the exports run late.",
    "DR-119: generalised filler variants are counted")
expect_pass("no-filler-phrases",
    "The queue drains overnight. The exports run late on Fridays.",
    "DR-119 control: plain prose stays clear")
expect_fail("no-generic-conclusions",
    "The migration took three weeks and two rollbacks.\n\nGive it a try today!",
    "DR-119: short imperative exclamation ending")
expect_pass("no-generic-conclusions",
    "The migration took three weeks and two rollbacks.\n\nThe project shipped on time!",
    "DR-119 control: non-imperative exclamation ending stays clear")
expect_pass("no-generic-conclusions",
    "Give it a try today! The trial takes three minutes and needs no card details.",
    "DR-119 control: exclamation mid-document stays clear")

# --- DR-125: #7 vocabulary watch-list expansions ---
print("\n=== DR-125 #7 vocabulary expansions ===")
DR125_AI_VOCABULARY = [
    "versatile", "significant", "effectively", "capabilities",
    "advancements", "elucidating", "firstly", "reliance",
    "generalizability", "nuance", "nuances", "nuancing", "delving",
    "unveil", "unveils", "unveiled", "unveiling",
    "heighten", "heightens", "heightened", "heightening",
    "amidst", "camaraderie", "palpable", "fleeting", "solace",
    "unravel", "cacophony", "unease", "reminder", "commence",
    "leverage", "elevate", "align", "dive into", "surpass",
    "notable", "despite",
]
for word in DR125_AI_VOCABULARY:
    matches = _grade._find_ai_words(word)
    if matches != [word]:
        FAILURES += 1
        print(f"FAIL: DR-125 #7 should recognize {word!r} exactly once; got {matches}")
    else:
        print(f"  ok: DR-125 #7 recognizes {word!r} exactly once")

for word in ["realign", "despiteful", "capability"]:
    matches = _grade._find_ai_words(word)
    if matches:
        FAILURES += 1
        print(f"FAIL: DR-125 #7 exact-boundary control {word!r} matched {matches}")
    else:
        print(f"  ok: DR-125 #7 exact-boundary control leaves {word!r} clear")

expect_fail("no-ai-vocabulary-clustering",
    "The response was versatile, significant, and worked effectively.",
    "DR-125: three newly approved vocabulary signals trip the existing threshold")
expect_pass("no-ai-vocabulary-clustering",
    "The response was versatile.\n\nThe result was significant.\n\nThe method worked effectively.",
    "DR-125 control: approved signals in separate paragraphs stay clear")

# --- DR-126B: #7 document-wide Kousha-Thelwall term pairs ---
print("\n=== DR-126B #7 document-wide term pairs ===")
DR126_KOUSHA_TERM_PAIRS = [
    ("delve", "underscore"),
    ("delving", "showcases"),
    ("unveiled", "intricated"),
    ("meticulously", "pivotal"),
    ("heightening", "nuanced"),
    ("bolstered", "fostering"),
    ("interplaying", "underscore"),
]
for first, second in DR126_KOUSHA_TERM_PAIRS:
    expect_fail("no-ai-vocabulary-clustering",
        f"The first section uses {first}.\n\nThe final section uses {second}.",
        f"DR-126B: distinct document-wide families {first!r} and {second!r} fail #7")

dr126_evidence = ALL_CHECKS["no-ai-vocabulary-clustering"](
    "The report will delve into the method.\n\nThe conclusion underscores the result."
)["evidence"]
for expected in ["delve=['delve']", "underscore=['underscores']"]:
    if expected not in dr126_evidence:
        FAILURES += 1
        print(f"FAIL: DR-126B evidence should contain {expected!r}; got {dr126_evidence!r}")
    else:
        print(f"  ok: DR-126B evidence reports canonical family and occurrence {expected!r}")

dr126_same_paragraph = ALL_CHECKS["no-ai-vocabulary-clustering"](
    "We FOSTER careful discussion before we Delve into the evidence."
)
dr126_same_paragraph_phrases = _grade._evidence_envelope(
    dr126_same_paragraph
)["quoted_phrases"]
if dr126_same_paragraph["passed"]:
    FAILURES += 1
    print("FAIL: DR-126B exactly two distinct families in one paragraph should fail #7")
elif dr126_same_paragraph_phrases != ["FOSTER", "Delve"]:
    FAILURES += 1
    print(
        "FAIL: DR-126B structured evidence should preserve every occurrence in "
        f"source order and source casing; got {dr126_same_paragraph_phrases!r}"
    )
else:
    print(
        "  ok: DR-126B exactly two same-paragraph families fail and structured "
        "evidence preserves source order and casing"
    )

dr126_combined = ALL_CHECKS["no-ai-vocabulary-clustering"](
    "We Delve into the evidence, FOSTER discussion, and work effectively."
)
dr126_combined_phrases = _grade._evidence_envelope(dr126_combined)["quoted_phrases"]
if dr126_combined["passed"]:
    FAILURES += 1
    print("FAIL: DR-126B combined paragraph and document-family failure should fail #7")
elif "Worst paragraph has 3 AI words" not in dr126_combined["evidence"]:
    FAILURES += 1
    print(
        "FAIL: DR-126B combined failure should retain worst-paragraph evidence; "
        f"got {dr126_combined['evidence']!r}"
    )
elif dr126_combined_phrases != ["Delve", "FOSTER"]:
    FAILURES += 1
    print(
        "FAIL: DR-126B combined failure should retain both family occurrences; "
        f"got {dr126_combined_phrases!r}"
    )
else:
    print(
        "  ok: DR-126B combined failure retains worst-paragraph evidence and "
        "both family occurrences"
    )

dr126_legacy_paragraph = ALL_CHECKS["no-ai-vocabulary-clustering"](
    "The response was versatile, significant, and worked effectively."
)
dr126_legacy_phrases = _grade._evidence_envelope(
    dr126_legacy_paragraph
)["quoted_phrases"]
if "matches" in dr126_legacy_paragraph:
    FAILURES += 1
    print("FAIL: DR-126B should not add an empty matches list to legacy failures")
elif dr126_legacy_phrases != ["versatile", "significant", "effectively"]:
    FAILURES += 1
    print(
        "FAIL: DR-126B should preserve fallback evidence parsing for legacy "
        f"paragraph-only failures; got {dr126_legacy_phrases!r}"
    )
else:
    print("  ok: DR-126B preserves structured evidence for legacy paragraph-only failures")

expect_pass("no-ai-vocabulary-clustering",
    "The first section will delve into the method.\n\nThe final section delves into the result.",
    "DR-126B control: one repeated family across paragraphs stays clear")

# --- DR-126C: GPTZero preserved-payload equality ---
print("\n=== DR-126C GPTZero payload equality ===")
dr126_gptzero_payload = _json.loads(
    (
        ROOT
        / "human-eyes"
        / "references"
        / "sources"
        / "snapshots"
        / "attachments"
        / "gptzero-ai-vocabulary-2026-07-15-client-data.json"
    ).read_text()
)
dr126_source_phrases = [
    row["ngram"].replace("\u2019", "'")
    for row in dr126_gptzero_payload
]
# GPTZERO_AI_PHRASES is a tuple so the frozen payload cannot be appended to or
# mutated at runtime; compare like for like.
if dr126_source_phrases != list(_grade.GPTZERO_AI_PHRASES):
    FAILURES += 1
    print(
        "FAIL: DR-126C runtime GPTZero phrases must equal the preserved 100-row "
        "payload after apostrophe normalization."
    )
    print(
        "      This list is frozen. New #7 clustering candidates go in "
        "AI_VOCABULARY (grade.py), not here."
    )
    print(f"  Source rows: {len(dr126_source_phrases)}")
    print(f"  Runtime rows: {len(_grade.GPTZERO_AI_PHRASES)}")
    for index, (source_phrase, runtime_phrase) in enumerate(
        zip(dr126_source_phrases, _grade.GPTZERO_AI_PHRASES), start=1
    ):
        if source_phrase != runtime_phrase:
            print(
                f"  First mismatch at row {index}: source={source_phrase!r}, "
                f"runtime={runtime_phrase!r}"
            )
            break
else:
    print("  ok: DR-126C runtime list exactly matches all 100 preserved payload rows")

# --- DR-135H: consolidated remaining social-post catalogue ---
print("\n=== DR-135H consolidated social-post catalogue ===")

DR135_EXISTING_RULE_EXPANSIONS = {
    "no-manufactured-insight": [
        "The data speaks for itself.",
        "The market has spoken.",
        "The numbers don't lie.",
        "This technology wants to replace the manager.",
        "AI is coming for your job.",
        "The industry is waking up to the problem.",
        "The results were eye-opening.",
        "This opens up a world of possibilities.",
        "The possibilities are endless.",
        "And here's the kicker: the queue is empty.",
        "But that's not even the best part.",
        "Wait, it gets better.",
        "And that's just the beginning.",
        "But wait, there's more.",
        "The plot thickens.",
        "Enter: the compliance team.",
        "Prompt engineering is the new programming.",
        "Your agent is only as good as your context window.",
    ],
    "no-filler-phrases": [
        "That said, the rollout is delayed.",
        "To be clear, the rollout is delayed.",
        "With the caveat that the sample is small, the result held.",
    ],
    "no-false-concession-hedges": [
        "To be fair, the first version was faster.",
        "Now, I'm not saying the plan is impossible, but it is late.",
        "Don't get me wrong, the team worked hard.",
        "This isn't to say that the result is useless.",
        "Granted, the sample is small, but the trend is clear.",
    ],
    "no-generic-conclusions": [
        "The question isn't whether, but when.",
        "We're still early.",
        "The best time to start was yesterday. The second best time is now.",
        "This is just the beginning.",
        "The genie is out of the bottle.",
        "The cat is out of the bag.",
        "Buckle up.",
        "Welcome to the future.",
        "And we're just getting started.",
        "Think about that.",
        "This is the new normal.",
        "Act accordingly.",
        "Plan accordingly.",
        "Adjust your strategy accordingly.",
        "Hiring will never be the same.",
    ],
    "no-negative-parallelisms": [
        "The best engineers don't write code. They design systems.",
        "I stopped scheduling meetings and started writing memos. The results speak for themselves.",
        "Teams that adapt will thrive. Teams that don't will be left behind.",
    ],
    "no-formulaic-openers": [
        "In 2026, AI literacy won't be optional. It'll be table stakes.",
        "The engineer of 2026 will look nothing like the engineer of 2024.",
    ],
    "no-significance-inflation": [
        "If you're still writing every report by hand, you're already behind.",
    ],
}
for check_id, phrases in DR135_EXISTING_RULE_EXPANSIONS.items():
    for phrase in phrases:
        expect_fail(check_id, phrase,
            f"DR-135H existing-rule routing ({check_id}): {phrase}")

DR135_SOCIAL_POST_FORMULAS = [
    "What do you think? Drop your take below 👇",
    "Agree or disagree? Let me know.",
    "What would you add to this list?",
    "Follow for more writing content.",
    "Repost if this resonated ♻️",
    "Share this with someone who needs to see it.",
    "Save this for later 🔖",
    "Tag someone who needs to hear this.",
    "If this helped, you'll love my newsletter.",
    "Link in comments 👇",
    "This is gold 🔥",
    "Saving this for later!",
    "More people need to see this.",
    "This resonates deeply.",
    "Couldn't agree more.",
    "So well articulated.",
    "You nailed it.",
    "This is spot on.",
    "I'd add a #6 to this list:",
    "Counterpoint:",
    "Hot take: the launch was rushed.",
    "This, but also the budget matters.",
    "Respectfully disagree on point 3.",
    "As someone who runs these audits, I can confirm.",
    "As someone who's been doing this for 10 years, I can confirm this is exactly right.",
    "I literally just had this conversation with my CEO yesterday.",
    "My team and I were just discussing this.",
    "Funny, I was just speaking about this at a conference.",
    "I asked ChatGPT to rewrite the memo and the results shocked me.",
    "I gave Claude my resume and it rewrote every bullet.",
    "I fed my business plan to a model and here's what happened.",
    "I replaced search with AI for a week.",
    "Day 1 of using AI to plan meals:",
    "I built this in 2 hours with a code generator.",
    "From zero to launch in 48 hours.",
    "Went from idea to launch in a weekend.",
    "What used to take 3 months now takes 3 minutes.",
    "Built my first app in a single afternoon. No code.",
    "I curated the top writing tools:",
    "The ultimate list of research prompts:",
    "I spent 100+ hours so you don't have to.",
    "I read 50 papers on automation. Here's the summary:",
    "I analyzed 1,000 posts. Here's what I found:",
    "AI did in two hours what used to take two weeks.",
]
for phrase in DR135_SOCIAL_POST_FORMULAS:
    expect_fail("no-formulaic-social-posts", phrase,
        f"DR-135H #62 formulaic social-post frame: {phrase}")

dr135_subtype_result = ALL_CHECKS["no-formulaic-social-posts"](
    "I asked ChatGPT to draft the post and the results shocked me. Save this for later."
)
if dr135_subtype_result.get("subtypes") != ["ai_wrapper", "engagement_request"]:
    FAILURES += 1
    print(f"FAIL: DR-135H #62 should report matched subtypes; got {dr135_subtype_result.get('subtypes')}")
else:
    print("  ok: DR-135H #62 reports matched social-post subtypes")

DR135_VOCABULARY_ADDITIONS = [
    "literally", "incredibly", "essentially", "arguably", "undeniably",
    "remarkably", "interestingly", "notably", "particularly", "ultimately",
    "groundbreaking", "revolutionary", "next-level", "world-class",
    "double down", "spearhead", "supercharge", "reimagine", "synergize",
]
for phrase in DR135_VOCABULARY_ADDITIONS:
    matches = _grade._find_ai_words(phrase)
    if matches != [phrase]:
        FAILURES += 1
        print(f"FAIL: DR-135H #7 should recognize {phrase!r} exactly once; got {matches}")
    else:
        print(f"  ok: DR-135H #7 recognizes {phrase!r} exactly once")

# --- DR-132A: approved marketing-email regex routes ---
print("\n=== DR-132A marketing-email regex routes ===")

for phrase in (
    "This is a game-changer.",
    "Unlock your true potential.",
    "Make your emails unstoppable.",
    "This is cutting-edge.",
    "This is groundbreaking.",
    "This is unprecedented.",
):
    expect_fail("no-promotional-language", phrase,
        f"DR-132A #4 hype formula: {phrase}")

for phrase in ("thoughtful strategy", "clear messaging", "intentional design"):
    matches = _grade._find_ai_words(phrase)
    if matches != [phrase]:
        FAILURES += 1
        print(f"FAIL: DR-132A #7 should recognize {phrase!r} exactly once; got {matches}")
    else:
        print(f"  ok: DR-132A #7 recognizes {phrase!r} exactly once")
expect_fail(
    "no-ai-vocabulary-clustering",
    "Your thoughtful strategy needs clear messaging and intentional design.",
    "DR-132A #7 clusters the three approved adjective-noun phrases",
)

for phrase in (
    "I hope this email finds you well. The release is ready.",
    "Are you tired of rewriting reports by hand? Look no further than Acme.",
):
    expect_fail("no-formulaic-openers", phrase,
        f"DR-132A #50 email opener: {phrase}")

# --- DR-133A: approved promotional and conclusion variants ---
print("\n=== DR-133A promotional and conclusion variants ===")

for check_id, phrase, label in (
    ("no-significance-inflation", "This underscores its importance.", "#1 significance frame"),
    ("no-significance-inflation", "The policy left an enduring legacy.", "#1 enduring legacy"),
    ("no-promotional-language", "The town has a rich cultural heritage.", "#4 promotional phrase"),
    ("no-filler-phrases", "It's important to note the date.", "#22 contracted editorial phrase"),
    ("no-filler-phrases", "It’s important to note the date.", "#22 smart-apostrophe editorial phrase"),
    ("no-filler-phrases", "No discussion would be complete without the archive.", "#22 editorial phrase"),
    ("no-notability-claims", "She was cited in NYT, BBC, FT, and The Hindu.", "#2 outlet-list shape"),
    ("no-generic-conclusions", "Despite these challenges, the town continues to thrive.", "#24 challenge-ending formula"),
    ("no-vague-attributions", "Studies show that the approach works.", "#5 bare attribution"),
):
    expect_fail(check_id, phrase, f"DR-133A {label}: {phrase}")

for phrase in ("defining feature", "powerful tools"):
    matches = _grade._find_ai_words(phrase)
    if matches != [phrase]:
        FAILURES += 1
        print(f"FAIL: DR-133A #7 should recognize {phrase!r} exactly once; got {matches}")
    else:
        print(f"  ok: DR-133A #7 recognizes {phrase!r} exactly once")
expect_fail(
    "no-ai-vocabulary-clustering",
    "Its defining feature is a suite of powerful tools and clear messaging.",
    "DR-133A #7 clusters the two editorial phrases with an existing candidate",
)

# --- DR-134B: exact transition and candour additions; #44 unchanged ---
print("\n=== DR-134B exact transition and candour additions ===")

for phrase in (
    "Furthermore, the deadline moved.",
    "Moreover, the deadline moved.",
    "Additionally, the deadline moved.",
    "In addition, the deadline moved.",
    "On the other hand, the deadline moved.",
    "Let's dive in. The first issue is cost.",
    "Here's what you need to know: the release moved.",
    "I hope you are well. The release is ready.",
):
    expect_fail("no-formulaic-openers", phrase,
        f"DR-134B #50 exact opener: {phrase}")

for phrase in (
    "Honestly? The estimate is wrong.",
    "Real talk. The estimate is wrong.",
    "I aim to be direct: the estimate is wrong.",
    "I need to be clear: the estimate is wrong.",
):
    expect_fail("no-performed-candour", phrase,
        f"DR-134B #56 exact candour frame: {phrase}")

straightforward_matches = _grade._find_ai_words("straightforward")
if straightforward_matches != ["straightforward"]:
    FAILURES += 1
    print(f"FAIL: DR-134B #7 should recognize 'straightforward' exactly once; got {straightforward_matches}")
else:
    print("  ok: DR-134B #7 recognizes 'straightforward' exactly once")
expect_fail(
    "no-ai-vocabulary-clustering",
    "The straightforward plan is genuinely effective and undeniably clear.",
    "DR-134B #7 clusters straightforward with two existing candidates",
)

expect_fail(
    "no-signposted-conclusions",
    "In summary, LLMs cannot reliably distinguish assumed knowledge from material that needs explanation, so a writer must fill the gap.",
    "DR-134B leaves the rejected #44 content-bearing control unchanged",
)

# --- DR-15A: remaining vague-attribution and research-boilerplate forms ---
print("\n=== DR-15A vague-attribution and research-boilerplate forms ===")

for phrase in (
    "Industry reports support the claim.",
    "Several sources support the claim.",
    "Several publications support the claim.",
    "Data proves the method works.",
    "Studies have shown benefits.",
):
    expect_fail("no-vague-attributions", phrase,
        f"DR-15A #5 exact attribution: {phrase}")

for phrase in (
    "This is an important area of research.",
    "More research is needed.",
):
    expect_fail("no-filler-phrases", phrase,
        f"DR-15A #22 exact research formula: {phrase}")

# --- DR-16A: remaining exact phrase variants through existing checks ---
print("\n=== DR-16A remaining exact phrase variants ===")

dr16_vocab = _grade._find_ai_words(
    "refine differentiate scalable solution"
)
for phrase in ("refine", "differentiate", "scalable solution"):
    if phrase not in dr16_vocab:
        FAILURES += 1
        print(f"FAIL: DR-16A #7 should recognize {phrase!r}; got {dr16_vocab}")
    else:
        print(f"  ok: DR-16A #7 recognizes {phrase!r}")
expect_fail(
    "no-ai-vocabulary-clustering",
    "Refine the plan, differentiate the offer, and build a scalable solution.",
    "DR-16A #7 clusters the three remaining vocabulary forms",
)

expect_fail(
    "no-excessive-hedging",
    "Arguably, it could be said that the result is potentially useful.",
    "DR-16A #23 counts the two missing hedges with an existing candidate",
)

for phrase in (
    "Therefore, we changed the plan.",
    "Let’s break it down.",
    "Let’s unpack this.",
):
    expect_fail("no-formulaic-openers", phrase,
        f"DR-16A #50 exact opener: {phrase}")

expect_fail(
    "no-manufactured-insight",
    "Sit with that for a moment.",
    "DR-16A #42 exact performed-knowingness phrase",
)

for phrase in (
    "Navigating the complexities of procurement takes time.",
    "A deeper understanding of the problem would help.",
    "When it comes to procurement, timing matters.",
    "In the realm of procurement, timing matters.",
    "A nuanced take on the problem would help.",
    "Delve into the intricacies of the proposal.",
    "Dive deep into the proposal.",
):
    expect_fail("no-filler-phrases", phrase,
        f"DR-16A #22 exact filler frame: {phrase}")

for phrase in (
    "Ultimately, the choice is yours.",
    "The journey doesn’t end here.",
    "His legacy endures.",
    "He remains an icon of American values and ideals.",
    "Its legacy will undoubtedly endure for generations to come.",
    "Achilles’ legacy continues to live on.",
    "His story will continue to inspire and captivate audiences.",
    "This is a positive sign for the company’s future prospects.",
    "It is well-positioned to meet changing needs.",
    "Don’t miss your chance to experience the show.",
    "The community remains hopeful that she will be found.",
    "Aristotle’s legacy is a testament to his influence.",
):
    expect_fail("no-generic-conclusions", phrase,
        f"DR-16A #24 exact ending formula: {phrase}")

# --- DR-19E: symmetric list items (#63) ---
print("\n=== DR-19E symmetric list items ===")

DR19E_LEAD = (
    "Our review covered the rollout in some depth and the findings were "
    "consistent across every region we visited.\n\n"
)
DR19E_TAIL = "\n\nWe then interviewed staff about how the rollout changed their week.\n"


def _dr19e(items, marker="-"):
    body = "\n".join(f"{marker} {item}" for item in items)
    return DR19E_LEAD + body + DR19E_TAIL


# Uniform length AND a shared trailing token: the source's own shape.
expect_fail("no-symmetric-list-items", _dr19e([
    "Automated reporting for finance teams",
    "Integrated dashboards for product teams",
    "Streamlined workflows for support teams",
]), "DR-19E shared trailing token with uniform length")

# Uniform length AND a shared opening token.
expect_fail("no-symmetric-list-items", _dr19e([
    "Improved latency across the checkout path",
    "Improved caching inside the search index",
    "Improved logging around the payment queue",
]), "DR-19E shared opening token with uniform length")

# Numbered markers carry the same structure.
expect_fail("no-symmetric-list-items", _dr19e([
    "Faster onboarding for new staff",
    "Clearer reporting for new staff",
    "Simpler approvals for new staff",
], marker="1."), "DR-19E numbered list with shared trailing token")

# Uniform length but no shared opening or trailing token: one condition only.
expect_pass("no-symmetric-list-items", _dr19e([
    "The finance team stopped chasing invoices",
    "Support closed its oldest backlog last month",
    "Product shipped the migration without incident",
]), "DR-19E uniform length alone is not enough")

# Shared trailing token but ragged lengths: one condition only.
expect_pass("no-symmetric-list-items", _dr19e([
    "Finance now gets its numbers automatically each morning without chasing anyone",
    "Support was unchanged",
    "Product asked for one dashboard, then quietly built four more",
]), "DR-19E shared token alone is not enough")

# Two items never qualify.
expect_pass("no-symmetric-list-items", _dr19e([
    "Automated reporting for finance teams",
    "Integrated dashboards for product teams",
]), "DR-19E two-item list is below the minimum")

# Prose with no list at all.
expect_pass("no-symmetric-list-items",
    "The rollout covered three regions and the team reported no incidents.",
    "DR-19E prose without a list")

dr19e_result = ALL_CHECKS["no-symmetric-list-items"](_dr19e([
    "Automated reporting for finance teams",
    "Integrated dashboards for product teams",
    "Streamlined workflows for support teams",
]))
if len(dr19e_result["matches"]) != 3:
    FAILURES += 1
    print(f"FAIL: DR-19E should report the matched items; got {dr19e_result['matches']}")
else:
    print("  ok: DR-19E reports the matched list items")

if _patterns_data["no-symmetric-list-items"]["severity"] != "context_warning":
    FAILURES += 1
    print("FAIL: DR-19E #63 should be a context warning")
else:
    print("  ok: DR-19E #63 carries context_warning severity")

# --- DR-19G: triad density replaces the one-triad verdict (#10) ---
print("\n=== DR-19G triad density ===")

DR19G_FILLER = "The team reviewed the plan carefully and at length again today. "
DR19G_TRIAD = "It was fast, cheap, and reliable. "

# 408 words, 2 triads = 4.90 per 1000: at or above the 4.0 threshold.
expect_fail("no-forced-triads", DR19G_FILLER * 36 + DR19G_TRIAD * 2,
    "DR-19G density at 4.90 per 1000 words")

# 402 words, 1 triad = 2.49 per 1000: below the threshold.
expect_pass("no-forced-triads", DR19G_FILLER * 36 + DR19G_TRIAD,
    "DR-19G density at 2.49 per 1000 words")

# A single triad no longer carries a verdict on its own.
expect_pass("no-forced-triads", "The plan was fast, cheap, and reliable.",
    "DR-19G one triad in a short text")

# Under the 300-word floor the check does not speak, however dense.
expect_pass("no-forced-triads", DR19G_TRIAD * 4,
    "DR-19G below the minimum-length floor")

dr19g_result = ALL_CHECKS["no-forced-triads"](DR19G_FILLER * 36 + DR19G_TRIAD * 2)
if "per 1000" not in dr19g_result["evidence"]:
    FAILURES += 1
    print(f"FAIL: DR-19G evidence should report the rate; got {dr19g_result['evidence']!r}")
else:
    print("  ok: DR-19G evidence reports the measured rate")

if "no-triad-density" in ALL_CHECKS:
    FAILURES += 1
    print("FAIL: DR-19G should retire the redundant #10a density check")
else:
    print("  ok: DR-19G retired #10a no-triad-density")

if "no-triad-density" in _patterns_data:
    FAILURES += 1
    print("FAIL: DR-19G should remove the #10a catalogue entry")
else:
    print("  ok: DR-19G removed the #10a catalogue entry")

if _patterns_data["no-forced-triads"]["severity"] != "context_warning":
    FAILURES += 1
    print("FAIL: DR-19G #10 should stay a context warning")
else:
    print("  ok: DR-19G #10 keeps context_warning severity")

# --- DR-21E: plan-announcement signposting (#47) ---
print("\n=== DR-21E plan-announcement signposting ===")

# Vollmer's own sequence: two announcements clear the aggregate threshold.
expect_fail("no-soft-scaffolding",
    "First, we'll look at the origins of the policy. Second, we'll examine how "
    "it was implemented across the three states. Finally, we'll conclude by "
    "weighing what the evidence supports.",
    "DR-21E ordinal plan announcements in sequence")

expect_fail("no-soft-scaffolding",
    "Next, let's explore what the submissions actually said. Finally, I'll wrap "
    "up with the two recommendations the committee accepted.",
    "DR-21E let's and I'll variants")

# One announcement stays below #47's two-candidate threshold.
expect_pass("no-soft-scaffolding",
    "First, we'll look at the origins of the policy. The department drafted it "
    "in 1998 after two failed attempts at a national scheme.",
    "DR-21E single announcement is below the threshold")

# Ordinals doing ordinary work are not plan announcements.
expect_pass("no-soft-scaffolding",
    "First, the department drafted the policy. Second, the states argued about "
    "funding. Finally, the scheme lapsed without a vote.",
    "DR-21E ordinary ordinal narration")

expect_pass("no-soft-scaffolding",
    "We'll look at the origins of the policy once the archive reopens, and we "
    "will examine the funding papers after that.",
    "DR-21E plan verbs without an ordinal opener")

# --- DR-21F: sales endings and reader address in news copy (#24) ---
print("\n=== DR-21F news sales endings ===")

expect_fail("no-generic-conclusions",
    "Whether you're a tech enthusiast, a developer, or simply someone "
    "interested in the future of technology, ARKit 1.5 demos are worth a look.",
    "DR-21F audience-enumeration reader address")

expect_fail("no-generic-conclusions",
    "As developers continue to explore the potential of this technology, we "
    "can expect to see even more innovative applications in the years ahead.",
    "DR-21F forward-looking expectation closer")

expect_fail("no-generic-conclusions",
    "The demos are rudimentary for now but they are certainly worth keeping an "
    "eye on.",
    "DR-21F certainly-worth-watching closer")

expect_pass("no-generic-conclusions",
    "Whether the scheme survives the next budget is a question the department "
    "would not answer.",
    "DR-21F ordinary whether clause")

expect_pass("no-generic-conclusions",
    "Two councils said they would keep an eye on the trial before committing "
    "their own funds.",
    "DR-21F ordinary keeping-watch wording")

# --- DR-21G: title case headings in surprising places (#64) ---
print("\n=== DR-21G title case headings ===")

expect_fail("no-title-case-headings",
    "## The Impact Of The New Policy On Regional Councils\n\nThe committee met "
    "on Tuesday and approved the budget without amendment.\n",
    "DR-21G minor words capitalised inside a heading")

expect_fail("no-title-case-headings",
    "# Title Case Headings In Surprising Places\n\nThe guide lists this as a "
    "formatting habit worth watching.\n",
    "DR-21G the source's own example heading")

expect_pass("no-title-case-headings",
    "## The impact of the new policy on regional councils\n\nThe committee met "
    "on Tuesday and approved the budget without amendment.\n",
    "DR-21G sentence case heading")

expect_pass("no-title-case-headings",
    "## What This Is For\n\nThe scheme pays for road maintenance in three "
    "shires.\n",
    "DR-21G title case with the minor word last")

expect_pass("no-title-case-headings",
    "## Rollout: The First Year\n\nCouncils reported no incidents in the first "
    "twelve months.\n",
    "DR-21G capital after a colon")

expect_pass("no-title-case-headings",
    "## Regional Council Budgets\n\nThe committee met on Tuesday and approved "
    "the budget.\n",
    "DR-21G title case with no minor words")

expect_pass("no-title-case-headings",
    "The impact of the new policy on regional councils was small.",
    "DR-21G prose without headings")

if _patterns_data["no-title-case-headings"]["severity"] != "context_warning":
    FAILURES += 1
    print("FAIL: DR-21G #15 should be a context warning")
else:
    print("  ok: DR-21G #15 is a context warning")

# --- DR-136B: mixed British and American spelling (#64) ---
print("\n=== DR-136B mixed spelling conventions ===")

expect_fail("no-mixed-spelling-conventions",
    "The council organised the review in March. By June the department had "
    "recognized that the timetable would not hold.",
    "DR-136B organised alongside recognized")

expect_fail("no-mixed-spelling-conventions",
    "Standardisation of the forms began in 2019. The agency later criticized "
    "the rollout in its annual report.",
    "DR-136B -isation noun alongside an -ized verb")

expect_fail("no-mixed-spelling-conventions",
    "Researchers analysed the first cohort, then paralyzed the second by "
    "changing the protocol midway.",
    "DR-136B -yse alongside -yze")

expect_pass("no-mixed-spelling-conventions",
    "The council organised the review in March and recognised by June that "
    "the timetable would not hold. Standardisation followed.",
    "DR-136B consistent British spelling")

expect_pass("no-mixed-spelling-conventions",
    "The council organized the review in March and recognized by June that "
    "the timetable would not hold. Standardization followed.",
    "DR-136B consistent American spelling")

# Words with no American variant must never count as British.
expect_pass("no-mixed-spelling-conventions",
    "The surprise announcement compromised the schedule, so the agency "
    "advertised a revised timetable and organized a briefing.",
    "DR-136B surprise, compromised, advertised, revised are not markers")

expect_pass("no-mixed-spelling-conventions",
    "The enterprise promised to supervise the exercise and televise the "
    "final round, which criticized nobody.",
    "DR-136B franchise-class words alongside an American form")

# The noun 'analyses' is spelled the same in both conventions.
expect_pass("no-mixed-spelling-conventions",
    "The report's analyses were thorough. The team recognized every gap and "
    "organized a follow-up.",
    "DR-136B the noun analyses is not a British marker")

expect_pass("no-mixed-spelling-conventions",
    "The committee met on Tuesday and approved the budget without amendment.",
    "DR-136B prose with no alternating words")

# Every alternating family the check claims to read.
for label, text in (
    ("-our/-or", "The colour of the harbour changed after the labor dispute."),
    ("-re/-er", "The centre reopened; the theater across the road did not."),
    ("-ogue/-og", "The catalogue was reprinted while the dialog box still failed."),
    ("doubled l", "She travelled north and he canceled the meeting."),
    ("-lous/-lous", "A marvellous result, though the modeling was marvelous too."),
    ("ae/oe", "The paediatric ward closed and the pediatric unit reopened."),
    ("one-offs", "The grey walls needed defence; the gray annexe needed defense."),
):
    expect_fail("no-mixed-spelling-conventions", text, f"DR-136B {label} mixture")

for label, text in (
    ("-ogue British only", "The catalogue and the dialogue were reprinted together."),
    ("-ogue American only", "The catalog and the dialog were reprinted together."),
    ("-our American only",
     "The color of the harbor changed after the labor dispute. The center reopened."),
):
    expect_pass("no-mixed-spelling-conventions", text, f"DR-136B {label}")

# Words deliberately left out: their American spelling is ordinary British too.
for label, text in (
    ("tyre", "He changed the tyre and organised the tools."),
    ("cheque", "She wrote a cheque and organised the files."),
    ("practice", "Daily practice organised the week."),
    ("judgement", "The judgment was organised into three parts."),
    ("learnt", "They learned the process and organised a handover."),
    ("programme", "The program was organised around three themes."),
):
    expect_pass("no-mixed-spelling-conventions", text,
                f"DR-136B {label} is not a convention marker")

# British words that keep their spelling across conventions must not count.
for label, text in (
    ("vigorous", "A vigorous defence of the colour scheme."),
    ("laboratory", "The laboratory analysed the colour samples."),
    ("literature", "The literature on behaviour is thin."),
    ("glamorous", "A glamorous parlour with a harbour view."),
):
    expect_pass("no-mixed-spelling-conventions", text,
                f"DR-136B {label} does not create a false mixture")

dr136b = ALL_CHECKS["no-mixed-spelling-conventions"](
    "The council organised the review, then recognized the delay.")
if not ("organised" in dr136b["evidence"] and "recognized" in dr136b["evidence"]):
    FAILURES += 1
    print(f"FAIL: DR-136B evidence should name both spellings; got {dr136b['evidence']!r}")
else:
    print("  ok: DR-136B evidence names both spellings")

if _patterns_data["no-mixed-spelling-conventions"]["severity"] != "context_warning":
    FAILURES += 1
    print("FAIL: DR-136B #64 should be a context warning")
else:
    print("  ok: DR-136B #64 is a context warning")

# --- DR-157: false ranges (#12) ---
print("\n=== DR-157 false ranges ===")

# The catalogue's own example, and the shape it describes.
expect_fail("no-false-ranges",
    "Our journey through the universe has taken us from the singularity of the "
    "Big Bang to the grand cosmic web, from the birth and death of stars to the "
    "enigmatic dance of dark matter.",
    "DR-157 the catalogue's Big Bang example")

expect_fail("no-false-ranges",
    "This guide covers everything from onboarding new staff to scaling your "
    "infrastructure, from managing budgets to building culture.",
    "DR-157 stacked breadth claim")

expect_fail("no-false-ranges",
    "The story moves from fear to mastery, from Sputnik to the Sea of "
    "Tranquillity, and it ends with a kind of secular apotheosis.",
    "DR-157 three stacked pairs")

# A single pair is ordinary English and is slightly more common in human prose.
expect_pass("no-false-ranges",
    "The scheme ran from 1990 to 2005 without amendment.",
    "DR-157 a single date range")

expect_pass("no-false-ranges",
    "She walked from the station to the office in twelve minutes.",
    "DR-157 a single ordinary range")

expect_pass("no-false-ranges",
    "The scheme ran from 1990 to 2005. Funding later moved from the states to "
    "the Commonwealth.",
    "DR-157 one pair each in two sentences")

expect_pass("no-false-ranges",
    "The committee met on Tuesday and approved the budget without amendment.",
    "DR-157 prose with no range at all")

dr157 = ALL_CHECKS["no-false-ranges"](
    "It covers everything from onboarding to scaling, from budgets to culture.")
if "2" not in dr157["evidence"]:
    FAILURES += 1
    print(f"FAIL: DR-157 evidence should report the pair count; got {dr157['evidence']!r}")
else:
    print("  ok: DR-157 evidence reports the pair count")

if _patterns_data["no-false-ranges"]["severity"] != "context_warning":
    FAILURES += 1
    print("FAIL: DR-157 #12 should be a context warning")
else:
    print("  ok: DR-157 #12 is a context warning")

print("\n=== DR-71 FAID academic Gemini trigrams ===")

# Figure 5's novelty and impact openers fire #1 on one match.
expect_fail("no-significance-inflation",
    "This work presents a scheduling layer that sits between the client and the "
    "shard map.",
    "DR-71 this work presents")

expect_fail("no-significance-inflation",
    "The paper presents a novel treatment of write amplification.",
    "DR-71 presents a novel")

expect_fail("no-significance-inflation",
    "The paper introduces a novel eviction policy derived from queue depth.",
    "DR-71 introduces a novel")

expect_fail("no-significance-inflation",
    "The results represent a significant advancement over prior schedulers.",
    "DR-71 a significant advancement")

# The three that could stand alone in honest academic prose only count toward
# #7's existing clustering threshold; one of them on its own stays clear.
expect_pass("no-ai-vocabulary-clustering",
    "The efficacy of the method was measured against three production workloads "
    "over six weeks, and the raw traces are published alongside the paper.",
    "DR-71 one clustering candidate alone does not fail #7")

expect_fail("no-ai-vocabulary-clustering",
    "The efficacy of the proposed method was measured over six weeks. Empirical "
    "evaluations demonstrate consistent gains, and the proposed method holds "
    "under load.",
    "DR-71 three clustering candidates in one paragraph")

for _phrase, _label in [
    ("the efficacy of", "DR-71 the efficacy of"),
    ("the proposed method", "DR-71 the proposed method"),
    ("empirical evaluations demonstrate", "DR-71 empirical evaluations demonstrate"),
]:
    if _grade._find_ai_words(_phrase) != [_phrase]:
        FAILURES += 1
        print(f"FAIL: {_label} should be an #7 clustering candidate")
    else:
        print(f"  ok: {_label} is an #7 clustering candidate")

# The four openers keep #1's existing severity; nothing about the check changes.
if _patterns_data["no-significance-inflation"]["severity"] != "context_warning":
    FAILURES += 1
    print("FAIL: DR-71 #1 should still be a context warning")
else:
    print("  ok: DR-71 #1 keeps its context-warning severity")

print("\n=== DR-159 Biber rate checks (Reinhart) ===")

# Nominalisation rate: nouns formed from verbs or adjectives (development,
# robustness). Fails at 29.0 per 1000 words in prose of 300+ words.
_dr159_nom_fail = (
    "The implementation of the transformation required the development of a new "
    "specification. The assessment of the requirements involved consideration of "
    "the limitations and the identification of dependencies. The establishment of "
    "governance improved the effectiveness of the organisation and the "
    "responsiveness of its administration. The evaluation of performance depends "
    "on the availability of information and the reliability of measurement. "
) * 7
expect_fail("no-nominalisation-rate", _dr159_nom_fail, "DR-159 dense nominalisation")

_dr159_nom_pass = (
    "She walked to the shop and bought bread. The baker had sold out of rye so she "
    "took a white loaf instead. On the way home it began to rain, and by the time "
    "she reached the door her coat was wet through. She put the kettle on and sat "
    "down by the window to watch the street fill with water. "
) * 5
expect_pass("no-nominalisation-rate", _dr159_nom_pass, "DR-159 plain narrative prose")

# That-relatives in subject position ("the dog that bit me"), not object
# position ("the dog that I saw"). Fails at 3.5 per 1000 words.
_dr159_that_fail = (
    "The report that describes the failure was withdrawn. The team that builds the "
    "pipeline has moved on. The tool that generates the summary is slow. The system "
    "that handles payments went down. The process that creates the index runs "
    "nightly. The rule that governs access changed. "
) * 8
expect_fail("no-that-relative-rate", _dr159_that_fail, "DR-159 dense subject relatives")

_dr159_that_pass = (
    "The dog that I saw belonged to the neighbour. The book that she recommended "
    "arrived today. The house that they bought needs work. The film that he "
    "mentioned is showing at the cinema on the corner near the station. "
) * 6
expect_pass("no-that-relative-rate", _dr159_that_pass, "DR-159 object relatives stay clear")

# Present participial clauses: adverbial, per Biber's example "Stuffing his mouth
# with cookies, Joe ran out the door". Fails at 4.4 per 1000 words.
_dr159_part_fail = (
    "Stuffing his mouth with cookies, Joe ran out the door. Leaning on the rail, she "
    "watched the boats, counting them as they passed. Turning the corner, he saw the "
    "lights, wondering what had happened. Holding the letter, she sat down, reading "
    "it twice. "
) * 9
expect_fail("no-participial-clause-rate", _dr159_part_fail, "DR-159 dense participial clauses")

_dr159_part_pass = (
    "She is walking to the shop and he was running late. The building has a ceiling "
    "of glass. During the morning meeting we reviewed the training plan. Something "
    "was wrong with the recording. Nothing in the findings changed the outcome. "
) * 6
expect_pass("no-participial-clause-rate", _dr159_part_pass, "DR-159 progressives and -ing nouns stay clear")

# All three are rate checks: short prose is out of scope whatever the rate.
for _cid in ("no-nominalisation-rate", "no-that-relative-rate", "no-participial-clause-rate"):
    _short = ALL_CHECKS[_cid]("The implementation of the transformation requires consideration.")
    if not _short["passed"]:
        FAILURES += 1
        print(f"FAIL: DR-159 {_cid} should skip prose under 300 words")
    else:
        print(f"  ok: DR-159 {_cid} skips prose under 300 words")
    if _patterns_data[_cid]["severity"] != "context_warning":
        FAILURES += 1
        print(f"FAIL: DR-159 {_cid} should be a context warning")
    else:
        print(f"  ok: DR-159 {_cid} is a context warning")

print("\n=== DR-87A exited ===")

# Suvanto et al.: `exited` occurs 61 times across GPT-4.1 rewrites of twelve
# 1920s-30s British detective novels and zero times in the source passages.
# Added as an #7 clustering candidate, so it never fails on its own.
if _grade._find_ai_words("exited") != ["exited"]:
    FAILURES += 1
    print("FAIL: DR-87A `exited` should be an #7 clustering candidate")
else:
    print("  ok: DR-87A `exited` is an #7 clustering candidate")

expect_pass("no-ai-vocabulary-clustering",
    "He exited the drawing room without another word, and the inspector followed "
    "him into the hall a moment later.",
    "DR-87A `exited` alone does not fail #7")

print("\n=== DR-66 passive voice, 'it' rate, and the #25 short-sentence rate ===")

# Passive voice: be-form plus past participle, per the paper's definition
# ("the frequency of verbs in passive voice"). Fails at 5.0 per 1000 words in
# prose of 300 words or more.
_dr66_passive_fail = (
    "The proposal was rejected by the committee and the minutes were circulated "
    "the following week. The figures had been checked twice before they were "
    "released, and the discrepancy was noticed only after the report was filed. "
    "Staff were told that the decision is being reviewed and that a revised "
    "schedule will be published once the funding is confirmed. "
) * 8
expect_fail("no-passive-voice-rate", _dr66_passive_fail, "DR-66 dense passive voice")

_dr66_passive_pass = (
    "She walked to the shop and bought bread. The baker had sold out of rye so she "
    "took a white loaf instead. On the way home it began to rain, and by the time "
    "she reached the door her coat clung to her shoulders. She put the kettle on "
    "and sat by the window to watch the street fill with water. "
) * 6
expect_pass("no-passive-voice-rate", _dr66_passive_pass, "DR-66 active prose stays clear")

_dr66_passive_controls = (
    "She is writing the letter and he was running late. The room is quiet and the "
    "children are tired. The model is based on the data we collected last spring, "
    "and the team is going to revisit it. She has written three drafts already. "
) * 7
expect_pass(
    "no-passive-voice-rate",
    _dr66_passive_controls,
    "DR-66 progressives, copula adjectives, and active perfects are not passives",
)

# "It" pronoun frequency, StyloMetrix's per-pronoun measure. Fails at 18.0 per
# 1000 words. Possessive "its" is a determiner and is not counted.
_dr66_it_fail = (
    "It works well enough, and it shows in the numbers. It is worth noting that it "
    "took three attempts. It seemed obvious afterwards, though it was not obvious "
    "at the time. It matters because it changes what the team does next. "
) * 9
expect_fail("no-it-pronoun-rate", _dr66_it_fail, "DR-66 dense 'it' pronouns")

_dr66_it_pass = (
    "The committee met on Thursday and reviewed the budget line by line. Members "
    "argued about the depot lease for most of the afternoon. The chair adjourned "
    "the meeting before a vote, and the papers went back to the officers for "
    "redrafting. Its final form will reach the council in March. "
) * 6
expect_pass("no-it-pronoun-rate", _dr66_it_pass, "DR-66 sparse 'it' and possessive 'its' stay clear")

# #25 gains a rate branch: short sentences of ten words or fewer at 30.0 or more
# per 1000 words. Short sentences are interleaved with long ones here, so
# neither the three-in-a-row run nor the repeated-opener pair can fire.
_dr66_staccato_rate = (
    "The tender closed on Friday. Officers spent the weekend reading submissions "
    "that had arrived in the final hour, most of them incomplete. Nobody expected "
    "that many. A second panel was convened on Monday morning to work through the "
    "backlog before the council meeting. Costs had already blown out. Procurement "
    "asked for an extension that the chair was unwilling to grant without a written "
    "case. Everyone knew how that would end. "
) * 7
expect_fail("no-staccato-sequences", _dr66_staccato_rate, "DR-66 #25 short-sentence rate branch")

_dr66_staccato_rate_pass = (
    "The tender closed on Friday afternoon and officers spent the weekend reading "
    "submissions that had arrived in the final hour, most of them incomplete and "
    "several of them addressed to the wrong department entirely. A second panel was "
    "convened on Monday morning to work through the backlog before the council "
    "meeting, by which point the costs had already blown well past the estimate. "
) * 6
expect_pass(
    "no-staccato-sequences",
    _dr66_staccato_rate_pass,
    "DR-66 long-sentence prose does not trip the #25 rate branch",
)

# The same interleaving as the failing fixture, but under 300 words, so the
# rate branch is out of scope. The run and repeated-opener branches cannot fire
# on it either, which is what makes it a clean length-gate test.
_dr66_staccato_short_doc = (
    "The tender closed on Friday. Officers spent the weekend reading submissions "
    "that had arrived in the final hour, most of them incomplete. Nobody expected "
    "that many. A second panel was convened on Monday morning to work through the "
    "backlog before the council meeting. Costs had already blown out. "
)
expect_pass(
    "no-staccato-sequences",
    _dr66_staccato_short_doc,
    "DR-66 the #25 rate branch skips prose under 300 words",
)

# Both new checks are rate checks with the same 300-word gate and severity as
# the #10 and DR-159 family.
for _cid in ("no-passive-voice-rate", "no-it-pronoun-rate"):
    _short = ALL_CHECKS[_cid]("It was rejected by the committee and it was filed.")
    if not _short["passed"]:
        FAILURES += 1
        print(f"FAIL: DR-66 {_cid} should skip prose under 300 words")
    else:
        print(f"  ok: DR-66 {_cid} skips prose under 300 words")
    if _patterns_data[_cid]["severity"] != "context_warning":
        FAILURES += 1
        print(f"FAIL: DR-66 {_cid} should be a context warning")
    else:
        print(f"  ok: DR-66 {_cid} is a context warning")

# Past tense got no check: measured 0.97x aggregate and 0.73x by document
# median, so human prose here carries at least as much of it as generated prose.
if any("past-tense" in _cid or "past_tense" in _cid for _cid in ALL_CHECKS):
    FAILURES += 1
    print("FAIL: DR-66 ruled no past-tense check; one exists")
else:
    print("  ok: DR-66 added no past-tense check")

# --- Summary ---

print(f"\n{'='*40}")
if FAILURES:
    print(f"FAILED: {FAILURES} assertion(s) broken")
    sys.exit(1)
else:
    print("ALL PASSED")
    sys.exit(0)
