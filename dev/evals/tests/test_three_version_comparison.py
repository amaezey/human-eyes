#!/usr/bin/env python3
"""Focused contract tests for the three-version comparison harness."""

import importlib.util
import json
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "dev/evals/harness/run_three_version_comparison.py"
spec = importlib.util.spec_from_file_location("three_versions", RUNNER)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


assert module.extract_native_checks({"programmatic_checks": []}, "audit-surface-only") == []
assert module.extract_native_checks(
    {"human_report": {"programmatic_checks": []}}, "legacy-direct-file"
) == []
assert module.normalize_check({"id": "x", "status": "flagged", "severity": "warning"})["flagged"]
assert not module.normalize_check({"id": "x", "status": "clear"})["flagged"]

documents = [
    {"pair_id": "a", "cohort": "human", "surface_findings": 2},
    {"pair_id": "a", "cohort": "ai", "surface_findings": 4},
    {"pair_id": "b", "cohort": "human", "surface_findings": 3},
    {"pair_id": "b", "cohort": "ai", "surface_findings": 1},
]
summary = module.paired_summary(documents)
assert summary["pair_deltas"] == [2, -2]
assert summary["mean_ai_minus_human"] == 0

check_documents = [
    {"cohort": "human", "checks": [{"id": "x", "flagged": True, "evidence": {"raw": {"candidate_count": 1, "threshold_met": True}}}]},
    {"cohort": "ai", "checks": [
        {"id": "x", "flagged": False, "evidence": {"raw": {"candidate_count": 2, "threshold_met": False}}},
        {"id": "new", "flagged": True, "evidence": {"raw": {"candidate_count": 3, "threshold_met": True}}},
    ]},
]
rows = {row["check_id"]: row for row in module.per_check_summary(check_documents)}
assert rows["x"]["flag_gap_ai_minus_human"] == -1
assert rows["x"]["human_candidate_count"] == 1
assert rows["x"]["ai_candidate_count"] == 2
assert rows["x"]["ai_documents_with_candidates"] == 1
assert rows["x"]["ai_documents_threshold_met"] == 0
assert rows["new"]["human_documents_checked"] == 0

with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    human = root / "human.md"
    ai = root / "ai.md"
    human.write_text("Human text.")
    ai.write_text("AI text.")
    rich = {"pairs": [{
        "id": "rich", "human": {"path": str(human), "sha256": module.sha256(human)},
        "ai": {"path": str(ai), "sha256": module.sha256(ai)},
    }]}
    compact = {"pairs": [{"topic": "compact", "human": str(human), "ai_fresh": str(ai)}]}
    rich_docs, _ = module.load_corpus(rich, root / "manifest.json")
    compact_docs, _ = module.load_corpus(compact, root / "manifest.json")
    assert [(doc["pair_id"], doc["cohort"]) for doc in rich_docs] == [("rich", "human"), ("rich", "ai")]
    assert [(doc["pair_id"], doc["cohort"]) for doc in compact_docs] == [("compact", "human"), ("compact", "ai")]

with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    semantic = root / "semantic.json"
    semantic.write_text(json.dumps({
        "version_id": "current", "version_commit": "abc", "manifest_sha256": "manifest",
        "documents": [{"document_id": "pair::human", "document_sha256": "doc", "native_output": {"x": 1}}],
    }))
    loaded = module.load_semantic_input(
        semantic, "current", "abc", "manifest", {"pair::human": "doc"}
    )
    assert loaded["payload"]["documents"][0]["native_output"] == {"x": 1}
    bad = json.loads(semantic.read_text())
    bad["documents"][0]["document_sha256"] = "wrong"
    semantic.write_text(json.dumps(bad))
    try:
        module.load_semantic_input(semantic, "current", "abc", "manifest", {"pair::human": "doc"})
    except ValueError as exc:
        assert "document hash mismatch" in str(exc)
    else:
        raise AssertionError("semantic hash mismatch was accepted")

print("three-version comparison tests passed")
