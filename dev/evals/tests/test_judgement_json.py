#!/usr/bin/env python3
"""Self-tests for human-eyes/scripts/judgement.json.

Independent of the U7 registry loader. Loads the JSON directly so the
file's shape can be validated without going through the loader.

Run: python3 dev/evals/tests/test_judgement_json.py
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
JUDGEMENT_PATH = ROOT / "human-eyes" / "scripts" / "judgement.json"

FAILURES = 0


def fail(msg):
    global FAILURES
    FAILURES += 1
    print(f"FAIL: {msg}")


def ok(msg):
    print(f"  ok: {msg}")


# --- file exists and parses cleanly ---

print("\n=== judgement.json load ===")
if not JUDGEMENT_PATH.exists():
    fail(f"judgement.json missing at {JUDGEMENT_PATH}")
    sys.exit(1)

with JUDGEMENT_PATH.open() as f:
    data = json.load(f)

if not isinstance(data, dict):
    fail(f"top-level JSON should be a mapping, got {type(data).__name__}")
    sys.exit(1)
ok("judgement.json parses as a mapping")


# --- top-level shape ---

print("\n=== judgement.json top-level keys ===")
for key in ("schema_version", "records"):
    if key not in data:
        fail(f"top-level key '{key}' missing")
    else:
        ok(f"top-level key '{key}' present")

if data.get("schema_version") != "1":
    fail(f"schema_version should be '1', got {data.get('schema_version')!r}")
else:
    ok("schema_version pinned to '1'")


# --- records list ---

print("\n=== judgement.json records ===")
records = data.get("records", [])
if not isinstance(records, list):
    fail(f"'records' should be a list, got {type(records).__name__}")
    sys.exit(1)

EXPECTED_IDS = [
    "structural_monotony",
    "tonal_uniformity",
    "faux_specificity",
    "neutrality_collapse",
    "rewrite_stance_drift",
    "even_jargon_distribution",
    "forced_synesthesia",
    "generic_metaphors",
    "referential_clarity",
    "formulaic_parallelism",
    "semantic_redundancy",
    "underspecified_language",
    "context_leakage",
    "performed_candour",
    "vacuous_connection",
    "genre_specific",
    # Shankar additions, approved 2026-07-17
    "audience_knowledge_mismatch",
    # DR-119, approved 2026-07-17
    "unprompted_caveats",
    # DR-121, approved 2026-07-18
    "change_narration",
    # DR-76, approved 2026-07-26
    "internal_consistency",
]
actual_ids = [r.get("id") for r in records]
if actual_ids != EXPECTED_IDS:
    fail(f"records order/ids mismatch.\n  expected: {EXPECTED_IDS}\n  got:      {actual_ids}")
else:
    ok(f"all {len(EXPECTED_IDS)} records present in canonical order")


# --- each record has required fields ---

REQUIRED_FIELDS = ("id", "pattern_ref", "severity", "prompt", "answer_schema", "flagged_when")
VALID_SEVERITIES = {"hard_fail", "strong_warning", "context_warning"}
for record in records:
    rid = record.get("id", "<unknown>")
    for field in REQUIRED_FIELDS:
        if field not in record:
            fail(f"record `{rid}` missing required field `{field}`")
    if record.get("severity") not in VALID_SEVERITIES:
        fail(f"record `{rid}` severity {record.get('severity')!r} not in {sorted(VALID_SEVERITIES)}")
    schema = record.get("answer_schema") or {}
    if "type" not in schema:
        fail(f"record `{rid}` answer_schema missing `type`")
    elif schema["type"] not in ("trichotomy", "state", "list", "presence", "composite"):
        fail(f"record `{rid}` answer_schema.type unrecognised: {schema['type']!r}")
    else:
        ok(f"record `{rid}` has type={schema['type']}, severity={record.get('severity')}")


# --- pattern_ref values ---

print("\n=== judgement.json pattern_ref values ===")
# Pattern ids under the DR-158 category-letter scheme. `rewrite_stance_drift`
# is the one record with no id: it reads a rewrite against its source document,
# so it has no draft-level catalogue entry (membership rule, DR-158).
# `performed_candour` -> H15 was corrected under DR-167; it had pointed at the
# Manufactured insight entry since before DR-158. The other five refs naming a
# check-backed pattern were each checked against their record's prompt and left.
EXPECTED_PATTERN_REFS = {
    "structural_monotony": "G13",
    "tonal_uniformity": "H3",
    "faux_specificity": "H6",
    "neutrality_collapse": "H7",
    "rewrite_stance_drift": None,
    "even_jargon_distribution": "B15",
    "forced_synesthesia": "F3",
    "generic_metaphors": "G2",
    "referential_clarity": "H3",
    "formulaic_parallelism": "B4",
    "semantic_redundancy": "H2",
    "underspecified_language": "H11",
    "context_leakage": "D1",
    "performed_candour": "H15",
    "vacuous_connection": "E1",
    "genre_specific": "H10",
    "audience_knowledge_mismatch": "D6",
    "unprompted_caveats": "D5",
    "change_narration": "H17",
    "internal_consistency": "A7",
}
for record in records:
    rid = record.get("id")
    expected = EXPECTED_PATTERN_REFS.get(rid)
    actual = record.get("pattern_ref")
    if actual != expected:
        fail(f"record `{rid}` pattern_ref should be {expected!r}, got {actual!r}")
    else:
        ok(f"record `{rid}` pattern_ref={expected!r}")


# --- targeted semantic contracts ---

print("\n=== judgement.json targeted semantic contracts ===")
records_by_id = {record.get("id"): record for record in records}

jargon_record = records_by_id.get("even_jargon_distribution", {})
jargon_values = jargon_record.get("answer_schema", {}).get("values")
expected_jargon_values = [
    "jargon is not suspiciously uniform",
    "jargon spreads suspiciously uniformly across the text",
]
if jargon_record.get("answer_schema", {}).get("type") != "state":
    fail("even_jargon_distribution should use a two-state answer schema")
elif jargon_values != expected_jargon_values:
    fail(
        "even_jargon_distribution should expose one non-flagged state and one "
        f"flagged state; got {jargon_values!r}"
    )
else:
    ok("even_jargon_distribution does not classify harmless non-flagged distributions")
if jargon_record.get("flagged_when") != [expected_jargon_values[1]]:
    fail("even_jargon_distribution should flag only suspiciously uniform distribution")
else:
    ok("even_jargon_distribution keeps harmless distributions non-flagged")

metaphor_prompt = records_by_id.get("generic_metaphors", {}).get("prompt", "")
required_metaphor_guidance = (
    "journey",
    "portal",
    "operating-system",
    "superpower",
    "under-the-hood",
    "each listed metaphor must independently meet this threshold",
)
missing_metaphor_guidance = [
    phrase for phrase in required_metaphor_guidance if phrase not in metaphor_prompt.lower()
]
if missing_metaphor_guidance:
    fail(f"generic_metaphors prompt missing approved guidance: {missing_metaphor_guidance}")
else:
    ok("generic_metaphors prompt covers common low-information families and list precision")


tonal_prompt = records_by_id.get("tonal_uniformity", {}).get("prompt", "")
required_tonal_guidance = (
    "abstraction",
    "concrete",
    "breezy and grandiose",
)
missing_tonal_guidance = [
    phrase for phrase in required_tonal_guidance if phrase not in tonal_prompt.lower()
]
if missing_tonal_guidance:
    fail(f"tonal_uniformity prompt missing DR-117 guidance: {missing_tonal_guidance}")
else:
    ok("tonal_uniformity prompt covers abstraction movement and the breezy-grandiose cue")

under_prompt = records_by_id.get("underspecified_language", {}).get("prompt", "")
missing_under = [p for p in ("develop no claim", "telling rather than showing")
                 if p not in under_prompt.lower()]
if missing_under:
    fail(f"underspecified_language prompt missing DR-119 guidance: {missing_under}")
else:
    ok("underspecified_language prompt covers dead-end sentences and telling-not-showing")

vac_prompt = records_by_id.get("vacuous_connection", {}).get("prompt", "")
if "highlights" not in vac_prompt.lower():
    fail("vacuous_connection prompt missing DR-119 causal-verb guidance")
else:
    ok("vacuous_connection prompt covers causal-verb misuse")

sem_prompt = records_by_id.get("semantic_redundancy", {}).get("prompt", "")
if "re-explain" not in sem_prompt.lower():
    fail("semantic_redundancy prompt missing DR-119 over-explaining guidance")
else:
    ok("semantic_redundancy prompt covers over-explaining")

parallel_prompt = records_by_id.get("formulaic_parallelism", {}).get("prompt", "").lower()
required_roast_guidance = (
    "an x with y and z",
    "already implies",
    "does not make sense",
)
missing_roast_guidance = [
    phrase for phrase in required_roast_guidance if phrase not in parallel_prompt
]
if missing_roast_guidance:
    fail(f"formulaic_parallelism prompt missing DR-124 roast-formula guidance: {missing_roast_guidance}")
else:
    ok("formulaic_parallelism covers the DR-124 an-X-with-Y-and-Z roast formula")

caveats = records_by_id.get("unprompted_caveats")
if not caveats:
    fail("unprompted_caveats record missing (DR-119)")
elif caveats.get("pattern_ref") != "D5" or not caveats.get("flagged_when"):
    fail("unprompted_caveats record misconfigured (pattern_ref must be D5; it carries its own catalogue entry since DR-158)")
else:
    ok("unprompted_caveats record present as D5")

change_narration = records_by_id.get("change_narration", {})
change_prompt = change_narration.get("prompt", "").lower()
required_change_guidance = (
    "documentation or code comments",
    "current behaviour",
    "changelogs",
    "release notes",
    "migration guides",
    "deprecation notices",
    "historical analysis",
)
missing_change_guidance = [
    phrase for phrase in required_change_guidance if phrase not in change_prompt
]
if change_narration.get("answer_schema") != {
    "type": "list",
    "items": ["phrase", "missing_current_state"],
}:
    fail("change_narration should return phrase and missing_current_state list items")
elif change_narration.get("flagged_when") != "non_empty":
    fail("change_narration should flag any non-empty finding list")
elif missing_change_guidance:
    fail(f"change_narration prompt missing DR-121 guidance: {missing_change_guidance}")
else:
    ok("change_narration describes current-state prose and all version-scoped exclusions")

neutrality_prompt = records_by_id.get("neutrality_collapse", {}).get("prompt", "")
if "genre-required neutrality" not in neutrality_prompt.lower():
    fail("neutrality_collapse prompt missing DR-117 genre-neutrality guidance")
else:
    ok("neutrality_collapse prompt covers genre-required neutrality")

stance_drift = records_by_id.get("rewrite_stance_drift", {})
expected_stance_values = [
    "source comparison unavailable",
    "preserves source stance",
    "adds a prescription, recommendation, solution, or call to action",
    "intensifies source stance",
    "reverses source stance",
    "erases or neutralises source stance",
]
expected_stance_flags = expected_stance_values[2:]
stance_prompt = stance_drift.get("prompt", "").lower()
missing_stance_guidance = [
    phrase
    for phrase in (
        "compare the supplied source",
        "adds",
        "intensifies",
        "reverses",
        "erases or neutralises",
        "judge meaning",
    )
    if phrase not in stance_prompt
]
if stance_drift.get("answer_schema") != {
    "type": "state",
    "values": expected_stance_values,
}:
    fail("rewrite_stance_drift should expose the six approved source-comparison states")
elif stance_drift.get("flagged_when") != expected_stance_flags:
    fail("rewrite_stance_drift should flag only the four approved stance-drift states")
elif stance_drift.get("pattern_ref") is not None or stance_drift.get("severity") != "strong_warning":
    fail("rewrite_stance_drift should be an unnumbered strong-warning agent judgement")
elif missing_stance_guidance:
    fail(f"rewrite_stance_drift prompt missing DR-136A guidance: {missing_stance_guidance}")
else:
    ok("rewrite_stance_drift implements the approved source-bound comparison")


# --- polymorphic genre slot ---

print("\n=== judgement.json genre_specific sub_records ===")
genre_record = next((r for r in records if r.get("id") == "genre_specific"), None)
if genre_record is None:
    fail("genre_specific record missing")
else:
    sub = genre_record.get("sub_records", {})
    EXPECTED_GENRES = {
        "academic",
        "student_essay",
        "poetry",
        "fiction",
        "journalism",
        "marketing_email",
        "default",
    }
    actual_genres = set(sub.keys())
    if actual_genres != EXPECTED_GENRES:
        fail(f"genre_specific sub_records mismatch.\n  expected: {sorted(EXPECTED_GENRES)}\n  got:      {sorted(actual_genres)}")
    else:
        ok(f"genre_specific has all {len(EXPECTED_GENRES)} sub_records: {sorted(EXPECTED_GENRES)}")
    # Each sub-record carries a watchlist.
    for genre, sub_record in sub.items():
        if "watchlist" not in sub_record:
            fail(f"genre_specific.sub_records.{genre} missing `watchlist`")
        elif not isinstance(sub_record["watchlist"], list):
            fail(f"genre_specific.sub_records.{genre}.watchlist should be a list, got {type(sub_record['watchlist']).__name__}")
        else:
            ok(f"genre_specific.sub_records.{genre}.watchlist is a list (size={len(sub_record['watchlist'])})")

    fiction_watchlist = sub.get("fiction", {}).get("watchlist", [])
    expected_dialogue_dimensions = [
        "dialogue speakers use indistinguishable levels of formality, technicality, politeness, or colloquial language",
        "dialogue speakers reuse the same discourse markers, hesitation markers, acknowledgements, and turn-taking cues",
        "dialogue speakers have indistinguishable cadence, stress patterns, pauses, and punctuation rhythm",
        "dialogue speakers use complete sentences and fragments in the same mechanical balance",
        "dialogue speakers use the same mix of statements, questions, commands, exclamations, and interruptions",
    ]
    missing_dialogue_dimensions = [
        item for item in expected_dialogue_dimensions if item not in fiction_watchlist
    ]
    if missing_dialogue_dimensions:
        fail(f"fiction watchlist missing DR-123 dialogue dimensions: {missing_dialogue_dimensions}")
    else:
        ok("fiction watchlist carries all five DR-123 dialogue dimensions separately")


# --- DR-136C: rewrite_stance_drift evaluation fixtures ---

print("\n=== DR-136C rewrite_stance_drift fixtures ===")

FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "rewrite_stance_drift_pairs.json"

if not FIXTURE_PATH.exists():
    fail("rewrite_stance_drift_pairs.json is missing")
else:
    fixture = json.loads(FIXTURE_PATH.read_text())
    if "rewrite_stance_drift" not in {r.get("id") for r in data["records"]}:
        fail("fixtures reference rewrite_stance_drift but the record is absent")
    else:
        ok("rewrite_stance_drift record exists for the fixtures to evaluate")

    source = fixture.get("source", {})
    for field in ("card", "claim", "citation", "prompt", "model_as_reported", "reuse_note"):
        if not source.get(field):
            fail(f"fixture source is missing {field}")
    if all(source.get(f) for f in ("card", "claim", "citation", "reuse_note")):
        ok("fixture carries its card, claim, citation, and reuse note")

    pairs = fixture.get("pairs", [])
    if len(pairs) != 2:
        fail(f"expected the paper's two pairs, found {len(pairs)}")
    else:
        ok("fixture carries both published pairs")

    incomplete = [p.get("id") for p in pairs
                  if not (p.get("original") and p.get("rewrite") and p.get("drift"))]
    if incomplete:
        fail(f"pairs missing original, rewrite, or drift note: {incomplete}")
    else:
        ok("every pair carries an original, a rewrite, and its drift note")

    unchanged = [p.get("id") for p in pairs if p.get("original") == p.get("rewrite")]
    if unchanged:
        fail(f"pairs whose rewrite equals the original: {unchanged}")
    else:
        ok("every rewrite differs from its original")


# --- JSON round-trip stability ---

print("\n=== judgement.json round-trip ===")
roundtripped = json.loads(json.dumps(data))
if roundtripped != data:
    fail("json.loads(json.dumps(data)) does not equal original data")
else:
    ok("data round-trips through JSON cleanly")


# --- DR-87B: said-bookisms in the fiction watchlist ---
print("\n=== DR-87B fiction dialogue verbs ===")
_fiction = (genre_record or {}).get("sub_records", {}).get("fiction", {})
_watch = " ".join(_fiction.get("watchlist", []))
_desc = _fiction.get("description", "")
_prompt = (genre_record or {}).get("prompt", "")
if "said" not in _watch.lower():
    fail("DR-87B fiction watchlist should name the avoidance of `said`")
else:
    ok("DR-87B fiction watchlist names the avoidance of `said`")
for _verb in ("remarked", "responded", "mentioned", "replied", "exclaimed", "chuckled"):
    if _verb not in _watch.lower() and _verb not in _desc.lower():
        fail(f"DR-87B fiction watchlist should cite `{_verb}` as a source-named example")
    else:
        ok(f"DR-87B fiction watchlist cites `{_verb}`")
if "said" not in _prompt.lower():
    fail("DR-87B genre_specific prompt should carry the fiction dialogue-verb cue")
else:
    ok("DR-87B genre_specific prompt carries the fiction dialogue-verb cue")

# --- Summary ---

print(f"\n{'='*40}")
if FAILURES:
    print(f"FAILED: {FAILURES} assertion(s) broken")
    sys.exit(1)
else:
    print("ALL PASSED")
    sys.exit(0)
