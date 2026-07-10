#!/usr/bin/env python3
"""Tests the repository-owned action lifecycle runner."""

import importlib.util
import os
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
path = ROOT / "dev/evals/harness/run_action_evals.py"
spec = importlib.util.spec_from_file_location("run_action_evals", path)
if spec is None or spec.loader is None:
    raise RuntimeError("could not load run_action_evals.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

expected = {
    "audit-requires-complete-judgement",
    "surface-only-blocks-actions",
    "suggestion-rejects-new-slop",
    "rewrite-rebinds-audit",
    "write-fresh-audit",
    "revision-limit-reports-residuals",
    "installed-path-resolution",
    "revision-convergence",
}
assert set(runner.SUITES["action-lifecycle"]) == expected
assert runner.evaluate_convergence([{"a", "b"}, {"b"}, set()])["passed"]
assert runner.evaluate_convergence([{"a"}, {"b"}, {"a"}])["reason"] == "finding sets oscillate"
assert runner.evaluate_convergence([{"a"}, {"a", "b"}])["reason"] == "required-finding count increased"
assert not runner.evaluate_convergence([{"a"}, {"a"}])["passed"]

old = os.environ.get("HUMAN_EYES_SKILL_CREATOR_PATH")
with tempfile.TemporaryDirectory() as tmp:
    skill = Path(tmp) / "skills/skill-creator"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("# Skill Creator\n")
    os.environ["HUMAN_EYES_SKILL_CREATOR_PATH"] = str(skill)
    assert runner.resolve_skill_creator() == skill.resolve()
    assert runner.main(["--print-command", "--workers", "2"]) == 0
if old is None:
    os.environ.pop("HUMAN_EYES_SKILL_CREATOR_PATH", None)
else:
    os.environ["HUMAN_EYES_SKILL_CREATOR_PATH"] = old

print("ALL PASSED")
