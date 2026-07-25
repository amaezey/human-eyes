#!/usr/bin/env python3
"""Asserts human-eyes/references/patterns.md equals the generator output from
dev/tools/render_patterns_md.py. Catches drift between the YAML registry
(authoritative source) and the on-disk markdown (generated transparency view).

Run: python3 dev/evals/tests/test_patterns_md_generator.py
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

result = subprocess.run(
    ["python3", str(ROOT / "dev" / "tools" / "render_patterns_md.py"), "--check"],
    capture_output=True,
    text=True,
)
print(result.stdout, end="")
if result.stderr:
    print(result.stderr, file=sys.stderr, end="")

if result.returncode != 0:
    print()
    print("FAIL: human-eyes/references/patterns.md is out of sync with human-eyes/scripts/patterns.json.")
    print("      Edit patterns.json, then regenerate:")
    print("      python3 dev/tools/render_patterns_md.py --write")
    sys.exit(1)

# --- Detector-lane labels on the extra entries ---
#
# The product has two detector types, programmatic and agent-judgement.  A
# catalogue entry labelled `manual` is neither: nothing checks it.  Both
# agent-judgement and manual entries carry `Severity: N/A`, and the generator
# used to call every one of them manual, so six live agent checks were
# mislabelled.  Pin the labels here.
import json

data = json.loads((ROOT / "human-eyes" / "scripts" / "patterns.json").read_text())
extras = {e["pattern_number"]: e for e in data["_extra_entries"]}

import re as _re


def _severity_line(entry):
    m = _re.search(r"\*\*Severity:\*\*[^\n]*", entry["patterns_md_body"])
    return m.group(0) if m else ""


mislabelled = [
    n for n, e in extras.items()
    if "agent-judgement" in _severity_line(e) and e["kind"] != "agent"
]
if mislabelled:
    print(f"FAIL: entries whose body says agent-judgement but are not labelled agent: {mislabelled}")
    sys.exit(1)
print("  ok: every agent-judgement entry is labelled agent")

UNCHECKED = {"6", "11", "12"}
actual = {n for n, e in extras.items() if e["kind"] in ("manual", "unknown")}
if actual != UNCHECKED:
    print(f"FAIL: entries nothing checks changed from {sorted(UNCHECKED)} to {sorted(actual)}.")
    print("      Adding one needs a decision: every pattern belongs to a programmatic")
    print("      or an agent-judgement check. Removing one means it was resolved; update this set.")
    sys.exit(1)
print(f"  ok: exactly {sorted(UNCHECKED)} are unchecked, awaiting a lane decision")

print()
print("========================================")
print("ALL PASSED")
