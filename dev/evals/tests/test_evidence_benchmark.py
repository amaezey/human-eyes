#!/usr/bin/env python3
"""Contract tests for the paired evidence benchmark."""

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
path = ROOT / "dev" / "evals" / "harness" / "run_evidence_benchmark.py"
spec = importlib.util.spec_from_file_location("evidence_benchmark", path)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

report = module.run()
assert report["benchmark_status"] == "incomplete"
assert report["performance"]["documents"] == 15
assert len(report["pairs"]) == 5
assert len(report["provenance_issues"]) == 10
assert len(report["semantic_issues"]) == 15
assert "no-curly-quotes" in report["house_style_checks_excluded_from_separation"]
for cohort in ("ai_fresh", "ai_rewrite"):
    summary = report["surface"][cohort]
    assert summary["n_pairs"] == 5
    assert len(summary["pair_deltas"]) == 5
    assert summary["ai_higher"] + summary["ties"] + summary["human_higher"] == 5
for pair in report["pairs"]:
    for cohort in ("human", "ai_fresh", "ai_rewrite"):
        document = pair[cohort]
        assert document["word_count"] > 0
        for result in document["checks"].values():
            assert result["evidence_type"] in {"lexical", "statistical", "aggregate"}
            assert result["candidate_count"] >= 0
            assert result["candidates_per_1000_words"] >= 0

lexical = module.grade_document(module.load_grade(), ROOT / "dev/evals/samples/synthetic/synthetic-all-clear.md")[0]["checks"]["no-em-dashes"]
assert lexical["evidence_type"] == "lexical"
assert "spans" in lexical

statistical = module.grade_document(module.load_grade(), ROOT / "dev/evals/samples/synthetic/synthetic-all-clear.md")[0]["checks"]["vocabulary-diversity"]
assert statistical["evidence_type"] == "statistical"
assert "metric_value" in statistical
assert "sample_size" in statistical

aggregate = module.grade_document(module.load_grade(), ROOT / "dev/evals/samples/synthetic/synthetic-all-clear.md")[0]["checks"]["overall-signal-stacking"]
assert aggregate["evidence_type"] == "aggregate"
assert "component_signals" in aggregate

ids = ("a", "b")
complete = {"coverage_mode": "full", "audit_status": "complete", "answers": [{"id": "a", "flagged": False}, {"id": "b", "flagged": True}]}
assert module.validate_semantic_audit(complete, ids) is None
assert module.validate_semantic_audit(None, ids)
assert module.validate_semantic_audit({**complete, "answers": complete["answers"][:1]}, ids)
print("ALL PASSED: evidence benchmark contracts and completeness gates")
