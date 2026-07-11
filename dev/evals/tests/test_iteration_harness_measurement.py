"""Test the iteration-harness measurement helpers (catalogue_hits).

After the audit-shape rework, the audit body uses bold mini-headers to mark
auto-detected vs agent-assessed flagged items. Pattern names render unbold:
`<glyph> <Name>` or `<glyph> <Name>: "<phrase>"`. The agent-judgement items
land under `**Agent-assessed**` rather than the retired parallel block;
their labels (e.g. "Tonal uniformity") are NOT catalogue patterns and
must not inflate the hit count.
"""

import importlib.util
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
_spec = importlib.util.spec_from_file_location(
    "run_skill_creator_iteration",
    ROOT / "dev" / "evals" / "harness" / "run_skill_creator_iteration.py",
)
iteration = importlib.util.module_from_spec(_spec)
sys.modules["run_skill_creator_iteration"] = iteration
_spec.loader.exec_module(iteration)

FAILURES = 0


def ok(message: str) -> None:
    print(f"  ok: {message}")


def fail(message: str) -> None:
    global FAILURES
    FAILURES += 1
    print(f"FAIL: {message}")


print("=== catalogue_hits ===")

OUTPUT_WITH_LAYER_2_CATALOGUE_ROWS = """
**Audit summary**
Auto-detected: 3 of 48 flagged · Agent-assessed: 0 of 0 flagged
Severity: 1 hard fail · 1 strong warning · 1 context warning
Signal stacking: clear (weaker AI signals are not accumulating)

**Auto-detected**

x Assistant residue: "I hope this helps"
! Em dashes: "EMDASH"
? Rule of three: "participation, resilience, and mobilisation"

**Agent-assessed**

**Next steps**

Want the full coverage report, suggestions for edits, a full rewrite, or to save this audit as a file?
"""

hits = iteration.catalogue_hits(OUTPUT_WITH_LAYER_2_CATALOGUE_ROWS)
expected = {"no-collaborative-artifacts", "no-em-dashes", "no-forced-triads"}
if hits == expected:
    ok("counts only Layer 1 flagged blocks and maps aliases")
else:
    fail(f"expected {sorted(expected)}, got {sorted(hits)}")

if "overall-signal-stacking" not in hits and "no-manufactured-insight" not in hits:
    ok("ignores Layer 2 catalogue rows and suppressed aggregate rows")
else:
    fail(f"Layer 2-only rows leaked into hits: {sorted(hits)}")

if iteration.catalogue_hits("No audit rendered here.") == set():
    ok("returns empty set when no Audit section exists")
else:
    fail("expected empty hit set without an Audit section")

with tempfile.TemporaryDirectory() as tmp:
    run_dir = Path(tmp)
    outputs = run_dir / "outputs"
    outputs.mkdir()
    (outputs / "response.md").write_text("ERROR: codex run failed\n")
    (outputs / "metrics.json").write_text(json.dumps({"errors_encountered": 1}))
    grading = iteration.grade_run({
        "files": [],
        "assertions": [{
            "name": "manual-check",
            "type": "qualitative",
            "description": "A qualitative expectation",
        }],
    }, run_dir)
    if grading["summary"]["pass_rate"] == 0 and grading["execution_metrics"]["errors_encountered"] == 1:
        ok("executor failures cannot receive deferred qualitative passes")
    else:
        fail("executor failure was not reflected in grading")

    (outputs / "response.md").write_text("A plausible but unreviewed response.\n")
    (outputs / "metrics.json").write_text(json.dumps({"errors_encountered": 0}))
    grading = iteration.grade_run({
        "files": [],
        "assertions": [{
            "name": "manual-check",
            "type": "qualitative",
            "description": "A qualitative expectation",
        }],
    }, run_dir)
    if grading["summary"]["pass_rate"] == 0:
        ok("pending qualitative review cannot count as an automatic pass")
    else:
        fail("qualitative assertion was counted as passed without review")


# Mixed auto-detected + agent-assessed audit body. Agent-assessed labels
# must NOT inflate the hit count — they're not catalogue patterns.

OUTPUT_NEW_AUDIT_SHAPE_BOTH_BLOCKS_IN_AUDIT = """
**Audit summary**
Auto-detected: 2 of 12 flagged · Agent-assessed: 1 of 8 flagged
Severity: 0 hard fail · 2 strong warning · 1 context warning
Signal stacking: clear (weaker AI signals are not accumulating)

**Auto-detected**

! Em dashes: "EMDASH"
! Rule of three: "participation, resilience, and mobilisation"

**Agent-assessed**

? Tonal uniformity
  - "register holds without breaks": single tonal arc

**Next steps**

Want the full coverage report, suggestions for edits, a full rewrite, or to save this audit as a file?
"""

hits = iteration.catalogue_hits(OUTPUT_NEW_AUDIT_SHAPE_BOTH_BLOCKS_IN_AUDIT)
expected = {"no-em-dashes", "no-forced-triads"}
if hits == expected:
    ok("counts new-shape Layer 1 openers and ignores agent-judgement-label openers in the audit body")
else:
    fail(f"expected {sorted(expected)} on new-shape audit body, got {sorted(hits)}")

if FAILURES:
    raise SystemExit(1)

print("\n========================================")
print("ALL PASSED")
