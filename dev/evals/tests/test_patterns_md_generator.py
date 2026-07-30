#!/usr/bin/env python3
"""Asserts human-eyes/references/patterns.md equals the generator output from
dev/tools/render_patterns_md.py. Catches drift between the YAML registry
(authoritative source) and the on-disk markdown (generated transparency view).

Run: python3 dev/evals/tests/test_patterns_md_generator.py
"""

import re
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

UNCHECKED = set()
actual = {n for n, e in extras.items() if e["kind"] in ("manual", "unknown")}
if actual != UNCHECKED:
    print(f"FAIL: entries nothing checks changed from {sorted(UNCHECKED)} to {sorted(actual)}.")
    print("      Adding one needs a decision: every pattern belongs to a programmatic")
    print("      or an agent-judgement check. Removing one means it was resolved; update this set.")
    sys.exit(1)
print(f"  ok: exactly {sorted(UNCHECKED)} are unchecked, awaiting a lane decision")

# --- preamble count and TOC ranges must match the data (DR-158) ---
# These were stored strings before DR-158 and went stale twice, then a third time
# when H18 changed category. render() computes them now; this pins that.
print()
print("=== preamble count and TOC ranges ===")
import collections
_md = (ROOT / "human-eyes" / "references" / "patterns.md").read_text()
_ids = re.findall(r"^### ([A-Z])(\d+)\. ", _md, re.M)
_m = re.search(r"^(\d+) patterns\b", _md, re.M)
if not _m:
    print(f"FAIL: preamble has no count sentence")
    sys.exit(1)
if int(_m.group(1)) != len(_ids):
    print(f"FAIL: preamble says {_m.group(1)} patterns; {len(_ids)} entries exist")
    sys.exit(1)
print(f"  ok: preamble count {len(_ids)} matches the entries")
# Compare against the highest id present, not the entry count: a category is not
# guaranteed gapless, and counting would pass a range that hides its top entry.
_max_pos = {}
_min_pos = {}
for _l, _n in _ids:
    _n = int(_n)
    _max_pos[_l] = max(_max_pos.get(_l, 0), _n)
    _min_pos[_l] = min(_min_pos.get(_l, 10**9), _n)
_toc_lines = re.findall(r"^- \[([^\]]+) \(([A-Z])(\d+)(?:-[A-Z](\d+))?\)\]", _md, re.M)
if len(_toc_lines) != len(_max_pos):
    print(f"FAIL: TOC lists {len(_toc_lines)} categories; {len(_max_pos)} letters have entries")
    sys.exit(1)
for _cat, _letter, _lo, _hi in _toc_lines:
    _got_hi = int(_hi) if _hi else int(_lo)
    if int(_lo) != _min_pos[_letter] or _got_hi != _max_pos[_letter]:
        print(f"FAIL: TOC says {_cat} runs {_letter}{_lo}-{_letter}{_got_hi}; "
              f"entries run {_letter}{_min_pos[_letter]}-{_letter}{_max_pos[_letter]}")
        sys.exit(1)
    print(f"  ok: {_cat} TOC range matches entries {_letter}{_min_pos[_letter]}-{_letter}{_max_pos[_letter]}")

print()
print("========================================")
print("ALL PASSED")
