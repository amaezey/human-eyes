#!/usr/bin/env python3
"""Contract tests for the bound audit-work bundle and fail-closed audit v2."""

import copy
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HUMAN_EYES = ROOT / "human-eyes"

spec = importlib.util.spec_from_file_location(
    "human_eyes_grade", HUMAN_EYES / "scripts" / "grade.py"
)
if spec is None or spec.loader is None:
    raise RuntimeError("could not load grade.py")
grade = importlib.util.module_from_spec(spec)
sys.path.insert(0, str(HUMAN_EYES / "scripts"))
spec.loader.exec_module(grade)


def clear_answer(record):
    schema = record["answer_schema"]
    if schema["type"] in {"state", "trichotomy"}:
        flagged = set(record["flagged_when"])
        return next(value for value in schema["values"] if value not in flagged)
    if schema["type"] == "list":
        return []
    if schema["type"] == "composite":
        return {"genre_detected": "default", "watchlist_findings": []}
    raise AssertionError(schema)


text = "# Heading\n\nThe document names the policy.\n"
results = [grade.annotate_result(check(text)) for check in grade.ALL_CHECKS.values()]
bundle = grade.build_audit_work_bundle(text, results)

assert bundle["schema_version"] == "1"
assert bundle["bindings"]["content_sha256"]
assert bundle["bindings"]["registry_sha256"]
assert bundle["bindings"]["structure_sha256"]
assert [segment["type"] for segment in bundle["segments"]] == ["heading", "paragraph"]
assert all(
    segment["id"] == f"{segment['type']}:{segment['start_byte']}:{segment['end_byte']}"
    for segment in bundle["segments"]
)

records = grade.registries.load_judgement()["records"]
bundle["semantic_answers"] = [
    {
        "id": record["id"],
        "status": "clear",
        "answer": clear_answer(record),
        "evidence": [],
    }
    for record in records
]

validated = grade.validate_audit_work_bundle(text, bundle)
report = grade.audit_report_v2(results, validated, coverage_mode="full")
assert report["schema_version"] == "2"
assert report["coverage_mode"] == "full"
assert report["audit_status"] == "complete"
assert report["aggregates"]["semantic"]["total"] == len(records)

for mutation, fragment in [
    (lambda value: value["semantic_answers"].pop(), "missing semantic id"),
    (lambda value: value["semantic_answers"].append(copy.deepcopy(value["semantic_answers"][0])), "duplicate semantic id"),
    (lambda value: value["bindings"].__setitem__("content_sha256", "0" * 64), "content binding"),
]:
    broken = copy.deepcopy(bundle)
    mutation(broken)
    try:
        grade.validate_audit_work_bundle(text, broken)
    except grade.AuditWorkBundleError as exc:
        assert fragment in str(exc), (fragment, str(exc))
    else:
        raise AssertionError(f"expected AuditWorkBundleError containing {fragment!r}")

surface = grade.audit_report_v2(results, None, coverage_mode="surface_only")
assert surface["audit_status"] == "incomplete"
assert surface["semantic_findings"] == []

with tempfile.TemporaryDirectory() as tmp:
    source = Path(tmp) / "input.md"
    work = Path(tmp) / "work.json"
    structure = Path(tmp) / "structure.json"
    source.write_text(text)
    title_end = len("# Heading\n".encode("utf-8"))
    structure.write_text(json.dumps({
        "segments": [
            {"type": "slide_title", "start_byte": 0, "end_byte": title_end},
        ]
    }))
    assert grade.main([
        "preflight", str(source), "--work-bundle", str(work),
        "--structure-manifest", str(structure),
    ]) == 0
    assert work.exists()
    structured = json.loads(work.read_text())
    assert structured["segments"][0]["type"] == "slide_title"
    assert not any("slide_title structure unavailable" in item for item in structured["limitations"])
    assert grade.main(["audit", str(source), "--surface-only", "--format", "json"]) == 0

    structure.write_text(json.dumps({"segments": [
        {"type": "slide_title", "start_byte": 0, "end_byte": title_end},
        {"type": "caption", "start_byte": 2, "end_byte": title_end},
    ]}))
    try:
        grade.load_structure_manifest(structure, text)
    except grade.AuditWorkBundleError as exc:
        assert "overlap" in str(exc)
    else:
        raise AssertionError("overlapping structure-manifest offsets should fail")

print("ALL PASSED")
