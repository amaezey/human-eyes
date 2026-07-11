#!/usr/bin/env python3
"""Contract tests for the per-check regex catalogue report."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
path = ROOT / "dev" / "evals" / "harness" / "run_regex_catalogue_audit.py"
spec = importlib.util.spec_from_file_location("run_regex_catalogue_audit", path)
audit_module = importlib.util.module_from_spec(spec)
if spec.loader is None:
    raise RuntimeError(f"Could not load {path}")
spec.loader.exec_module(audit_module)

report = audit_module.audit(audit_module.DEFAULT_CORPUS)
overall = report["overall"]
assert overall["violation_total"] == 32
assert overall["control_total"] == 28
assert overall["violation_detected"] >= 24
assert overall["control_clear"] >= 23
assert not report["unmapped_tendencies"]

for check_id, metrics in report["per_check"].items():
    if metrics["violation_total"]:
        assert metrics["recall"] is not None, check_id
    if metrics["control_total"]:
        assert metrics["specificity"] is not None, check_id

assert all(sample["expected_checks"] for sample in report["samples"] if sample["label"] == "violation")
print("ALL PASSED: regex catalogue report contract and seed floor")
