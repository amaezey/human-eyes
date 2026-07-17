#!/usr/bin/env python3
"""Reconcile the decision register against the recommendation classification.

Every classification row with an additive or evaluate component (label
ADDITIVE, EVALUATE, or MIXED, or flag secondary-add / secondary-evaluate)
must be cited by a decision-register row as ``slug:CNN`` or explicitly
listed as no-action. Reports the outstanding count; exits 1 while any
row is unaccounted for.

Run: python3 dev/tools/reconcile_register.py [--by-source]
"""

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "dev" / "source-ingest-hygiene-recommendation-classification-2026-07-17.csv"
REGISTER_PATH = ROOT / "dev" / "decision-register.md"
MAPPING_PATH = ROOT / "dev" / "source-evaluation-residue-mapping-2026-07-17.csv"
PO_PATH = ROOT / "human-eyes" / "references" / "sources" / "pattern-opportunities.md"

ACTION_LABELS = {"ADDITIVE", "EVALUATE", "MIXED"}
ACTION_FLAGS = {"secondary-add", "secondary-evaluate"}
CLAIM_KEY_RE = re.compile(r"([a-z0-9][a-z0-9-]*):(C\d{2,})")


def action_rows():
    with CSV_PATH.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if row["label"] in ACTION_LABELS or row["flag"] in ACTION_FLAGS:
                yield row["slug"], row["claim"]


def register_keys():
    text = REGISTER_PATH.read_text(encoding="utf-8")
    return {(slug, claim) for slug, claim in CLAIM_KEY_RE.findall(text)}


def pattern_opportunities_keys():
    """Claim keys cited by a pattern-opportunities candidate row."""
    text = PO_PATH.read_text(encoding="utf-8")
    keys = set()
    for m in re.finditer(r"\]\(([a-z0-9-]+)\.md\), claims? ([^|;\[]+?)(?=[|;\[])", text):
        slug, claims = m.group(1), m.group(2)
        for c in re.finditer(r"C(\d{2,})(?:-C(\d{2,}))?", claims):
            lo, hi = int(c.group(1)), int(c.group(2) or c.group(1))
            for n in range(lo, hi + 1):
                keys.add((slug, f"C{n:02d}"))
    return keys


def mapped_keys():
    """Rows dispositioned no-action or covered in the residue mapping.

    Candidate rows must graduate to a register row to count, so they are
    deliberately excluded here.
    """
    if not MAPPING_PATH.exists():
        return set()
    with MAPPING_PATH.open(encoding="utf-8") as fh:
        return {(r["slug"], r["claim"]) for r in csv.DictReader(fh)
                if r["disposition"] in ("no-action", "covered")}


def main():
    by_source = "--by-source" in sys.argv
    pending = list(action_rows())
    reg = register_keys()
    po = pattern_opportunities_keys()
    mapped = mapped_keys()
    accounted = reg | po | mapped
    missing = [r for r in pending if r not in accounted]
    print(f"classification rows with an additive/evaluate component: {len(pending)}")
    print(f"cited by a decision-register row: {sum(1 for r in pending if r in reg)}")
    print(f"cited by a pattern-opportunities candidate row: {sum(1 for r in pending if r not in reg and r in po)}")
    print(f"dispositioned no-action/covered in the residue mapping: {sum(1 for r in pending if r not in reg and r not in po and r in mapped)}")
    print(f"not yet accounted for: {len(missing)}")
    if by_source and missing:
        from collections import Counter
        for slug, n in Counter(s for s, _ in missing).most_common():
            print(f"  {slug}: {n}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
