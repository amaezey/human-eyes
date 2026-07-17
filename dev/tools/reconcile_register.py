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


def main():
    by_source = "--by-source" in sys.argv
    pending = list(action_rows())
    covered = register_keys()
    missing = [(s, c) for s, c in pending if (s, c) not in covered]
    print(f"classification rows with an additive/evaluate component: {len(pending)}")
    print(f"cited by a decision-register row: {len(pending) - len(missing)}")
    print(f"not yet accounted for: {len(missing)}")
    if by_source and missing:
        from collections import Counter
        for slug, n in Counter(s for s, _ in missing).most_common():
            print(f"  {slug}: {n}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
