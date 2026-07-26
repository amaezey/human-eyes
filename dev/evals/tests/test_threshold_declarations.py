#!/usr/bin/env python3
"""Every declared cut-off must be the one the check actually enforces (DR-170).

`CHECK_THRESHOLDS` in grade.py is attached to each result as `result["threshold"]`
and reaches the audit report, but only `no-excessive-lists` and
`no-heading-one-liners` read it when deciding whether to flag. The other 17
checks carry the number as a literal in their own body, so a report can name a
cut-off the check is not using and nothing would notice.

This test does not read those literals. It sweeps the sample corpus, records
where each check actually flips from clear to flagged, and compares that
observed flip point against the declared number. A contradiction fails.

Where the corpus does not happen to supply documents either side of a cut-off,
the check is reported UNVERIFIED rather than passing quietly: DR-79 found #52
firing on nothing while its test passed, and silence must not read as agreement.
The unverifiable set is pinned below, so a check joining it fails this test.
"""
import ast
import importlib.util
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("grade", ROOT / "human-eyes/scripts/grade.py")
grade = importlib.util.module_from_spec(spec)
spec.loader.exec_module(grade)

FAILURES = 0


def fail(msg):
    global FAILURES
    FAILURES += 1
    print(f"FAIL: {msg}")


def ok(msg):
    print(f"  ok: {msg}")


# Checks whose flip point this corpus cannot pin, with the reason. A check may
# only be here because the corpus lacks documents either side of its cut-off, or
# because the cut-off is one of several gates and no document isolates it.
# Adding to this set is a decision: it means one more reported number nobody has
# verified against behaviour.
UNVERIFIABLE = {
    "overall-signal-stacking": "aggregate over other checks; its 4 is a count of "
                               "component findings, not a candidate count",
    "no-staccato-sequences": "five interacting gates; no corpus document isolates one",
    "no-excessive-lists": "three interacting gates, and it is one of the two checks "
                          "that already reads the declared value",
    "no-symmetric-list-items": "minimum_items and maximum_deviation apply together",
    "no-forced-triads": "rate per 1000 words behind a 300-word floor",
    "no-compound-modifier-density": "per-sentence gate, not a document-level count",
    "no-inline-header-lists": "no document in the sample corpus flags it, so the "
                              "cut-off has no observed flip point",
    "no-rubric-echoing": "no document in the sample corpus flags it, so the cut-off "
                         "has no observed flip point",
}


def declared_thresholds():
    src = (ROOT / "human-eyes/scripts/grade.py").read_text()
    block = re.search(r"CHECK_THRESHOLDS = (\{.*?\n\})\n", src, re.S).group(1)
    return ast.literal_eval(block)


def corpus_documents():
    docs = []
    base = ROOT / "dev/evals/samples"
    for p in sorted(base.rglob("*")):
        if p.suffix in (".md", ".txt") and p.is_file():
            docs.append(p)
    return docs


def sweep(docs, thresholds):
    """check id -> list of (candidate_count, flagged) over every document."""
    observed = {cid: [] for cid in thresholds}
    for p in docs:
        try:
            text = p.read_text()
        except Exception:
            continue
        for cid in thresholds:
            fn = grade.ALL_CHECKS.get(cid)
            if fn is None:
                continue
            try:
                raw = grade.annotate_result(fn(text))
            except Exception:
                continue
            if raw.get("context_suppressed"):
                continue
            observed[cid].append((candidate_count(raw), bool(raw.get("threshold_met"))))
    return observed


def candidate_count(raw):
    """The check's real candidate count.

    `annotate_result` defaults `candidate_count` to `len(candidates)`, so a check
    that populates neither `candidates` nor `matches` reports 0 while naming its
    hits in the evidence string. Read the evidence in that case rather than
    trusting the zero.
    """
    n = raw.get("candidate_count")
    if n:
        return n
    m = re.search(r"\bFound (\d+)\b", str(raw.get("evidence", "")))
    return int(m.group(1)) if m else n


def main():
    thresholds = declared_thresholds()
    docs = corpus_documents()
    print(f"declared cut-offs: {len(thresholds)}   corpus documents: {len(docs)}")

    observed = sweep(docs, thresholds)

    print("\n=== count cut-offs: does the check flip where the report says? ===")
    unverified = {}
    for cid, spec_ in sorted(thresholds.items()):
        if cid in UNVERIFIABLE:
            continue
        if not (isinstance(spec_, dict) and set(spec_) == {"minimum_candidates"}):
            continue
        want = spec_["minimum_candidates"]
        pairs = [(c, f) for c, f in observed[cid] if isinstance(c, int)]
        flagged = [c for c, f in pairs if f]
        clear = [c for c, f in pairs if not f]
        if not flagged or not clear:
            unverified[cid] = (f"corpus gives only {'flagged' if flagged else 'clear'} "
                               f"results ({len(pairs)} documents)")
            continue
        # Separation, not adjacency: the corpus need not contain exactly `want`
        # and `want - 1`, only no document on the wrong side of the line.
        clear_at_or_above = [c for c in clear if c >= want]
        flagged_below = [c for c in flagged if c < want]
        if clear_at_or_above or flagged_below:
            fail(f"{cid}: report declares {want}, but "
                 f"{len(clear_at_or_above)} document(s) with {want}+ candidates were clear "
                 f"and {len(flagged_below)} with fewer were flagged "
                 f"(clear up to {max(clear)}, flagged from {min(flagged)})")
        else:
            ok(f"{cid}: declared {want} separates all {len(pairs)} documents "
               f"(clear up to {max(clear)}, flagged from {min(flagged)})")

    print("\n=== statistic cut-offs ===")
    for cid, key, direction in (("paragraph-length-uniformity", "maximum_cv", "below"),
                                ("sentence-length-variance", "minimum_stdev", "below")):
        want = thresholds[cid][key]
        seen = []
        for p in docs:
            try:
                raw = grade.annotate_result(grade.ALL_CHECKS[cid](p.read_text()))
            except Exception:
                continue
            if raw.get("context_suppressed"):
                continue
            ev = str(raw.get("evidence", ""))
            m = re.search(r"(?:CV|stdev|std ?dev|deviation|SD)\D*([0-9]+(?:\.[0-9]+)?)",
                          ev, re.I)
            if m:
                # The evidence string is rounded for display, so allow half a
                # unit of the printed precision when comparing against the
                # declared cut-off. Without this a value printed as 0.18 but
                # really 0.1758 reads as a contradiction that is not one.
                digits = len((m.group(1).split(".") + [""])[1])
                tol = 0.5 * (10 ** -digits) if digits else 0.5
                seen.append((float(m.group(1)), tol, bool(raw.get("threshold_met"))))
        flagged = [v for v, _t, f in seen if f]
        clear = [v for v, _t, f in seen if not f]
        if not flagged or not clear:
            unverified[cid] = f"corpus never straddles {want} ({len(seen)} measured)"
            continue
        wrong = [(v, f) for v, tol, f in seen
                 if (f and v - tol >= want) or (not f and v + tol < want)]
        if wrong:
            fail(f"{cid}: declared {want} does not separate flagged from clear even "
                 f"allowing for display rounding; e.g. {wrong[:3]} "
                 f"(value, flagged)")
        else:
            ok(f"{cid}: declared {want} separates all {len(seen)} measured documents "
               f"(flagged up to {max(flagged)}, clear from {min(clear)})")

    print("\n=== unverified by this corpus ===")
    for cid, why in sorted(UNVERIFIABLE.items()):
        print(f"  pinned: {cid} — {why}")
    for cid, why in sorted(unverified.items()):
        print(f"  UNVERIFIED: {cid} — {why}")
    new = set(unverified) - set(UNVERIFIABLE)
    if new:
        fail(f"these cut-offs became unverifiable and are not pinned: {sorted(new)}. "
             f"Either give the corpus a document either side, or pin them with a reason.")

    print()
    if FAILURES:
        print(f"FAILED: {FAILURES} assertion(s) broken")
        sys.exit(1)
    print("ALL PASSED")


if __name__ == "__main__":
    main()
