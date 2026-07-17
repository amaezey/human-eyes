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
EXPECTED_PATTERN_REFS = {
    "structural_monotony": None,
    "tonal_uniformity": 35,
    "faux_specificity": 36,
    "neutrality_collapse": 37,
    "even_jargon_distribution": None,
    "forced_synesthesia": 28,
    "generic_metaphors": 30,
    "referential_clarity": 35,
    "formulaic_parallelism": 10,
    "semantic_redundancy": 34,
    "underspecified_language": 43,
    "context_leakage": 19,
    "performed_candour": 42,
    "vacuous_connection": 22,
    "genre_specific": 41,
    "unprompted_caveats": None,
    "change_narration": None,
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

caveats = records_by_id.get("unprompted_caveats")
if not caveats:
    fail("unprompted_caveats record missing (DR-119)")
elif caveats.get("pattern_ref") is not None or not caveats.get("flagged_when"):
    fail("unprompted_caveats record misconfigured (pattern_ref None per agent-only convention; #61 maps via the render fallback)")
else:
    ok("unprompted_caveats record present as #61")

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


# --- JSON round-trip stability ---

print("\n=== judgement.json round-trip ===")
roundtripped = json.loads(json.dumps(data))
if roundtripped != data:
    fail("json.loads(json.dumps(data)) does not equal original data")
else:
    ok("data round-trips through JSON cleanly")


# --- Summary ---

print(f"\n{'='*40}")
if FAILURES:
    print(f"FAILED: {FAILURES} assertion(s) broken")
    sys.exit(1)
else:
    print("ALL PASSED")
    sys.exit(0)
