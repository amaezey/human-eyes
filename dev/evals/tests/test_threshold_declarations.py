#!/usr/bin/env python3
"""Every declared cut-off must be the number that governs behaviour (DR-170).

`CHECK_THRESHOLDS` in grade.py is attached to each result as `result["threshold"]`
and reaches the audit report, so a reader is told which cut-off produced a
finding. This test exists to stop that number drifting away from the one the
check enforces.

The first version compared the table against itself. It assumed only two checks
read the table and the rest carried literals, so for the sixteen checks that read
their value through `threshold_value(check_id, key, default)` it asserted nothing
at all, and it could not fail.

It now tests the property directly. For each declared number, mutate it in an
in-memory copy of the table, re-run the check across the corpus, and require that
some document's flag/clear outcome moves. If nothing moves, the check is not
reading its declaration: the report names one number, the check enforces another,
and the two can diverge without notice.

A declared key that no check reads fails rather than being skipped. Renaming a
key inside a threshold entry, or adding one, used to drop that check out of
verification silently; now it is reported, because the check falls back to its
own default and the orphaned key moves nothing.

Seven numbers used to be unreachable this way, because their checks carried the
value as a literal while the table declared it for the report only. Rather than
verify those by a second mechanism, the checks were wired through
`threshold_value` so one mechanism covers all of them. The wiring was
behaviour-preserving: across 66 checks and 153 corpus documents no flag or clear
outcome changed.

Pins are validated, not trusted. Every pinned id must exist in `grade.ALL_CHECKS`
and its stated reason must be checked wherever the reason is checkable, so a pin
cannot assert something false and print it as fact. DR-79's lesson holds: a
cut-off this suite cannot verify is named out loud, and silence never reads as
agreement.

This test asks whether a cut-off is wired, not whether it is set well. Whether
each boundary sits sensibly inside the range real prose produces is DR-164's
question, measured against the corpus.
"""
import copy
import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("grade", ROOT / "human-eyes/scripts/grade.py")
grade = importlib.util.module_from_spec(spec)
spec.loader.exec_module(grade)

# The authoritative table, captured before any mutation so every probe restores
# to a known state. grade.py is never written to; only this in-memory copy moves.
BASELINE = copy.deepcopy(grade.CHECK_THRESHOLDS)

FAILURES = 0


def fail(msg):
    global FAILURES
    FAILURES += 1
    print(f"FAIL: {msg}")


def ok(msg):
    print(f"  ok: {msg}")


# ---------------------------------------------------------------------------
# Pins. A cut-off may only be here because neither route can reach it. Each
# reason is checked below, so a pin that stops being true fails this test.
# Adding to either dict is a decision: it means one more reported number nobody
# has verified against behaviour.
# ---------------------------------------------------------------------------

# Whether a flagged finding reaches a reader with something to look at is not a
# threshold question, and it already has a test: test_phrase_capture_coverage.py
# gates exactly that, and additionally checks the captured phrases occur in the
# input. A second copy lived here briefly; it was removed rather than kept in
# parallel, and that test's corpus was widened instead.

# Cut-offs no mutation can reach, keyed by (check id, key). Empty: every declared
# key is read by its check. A key landing here must carry a reason, and the
# reason is checked below.
UNVERIFIABLE = {}


def declared_keys():
    """(check_id, key, value) for every declared cut-off. key is None for scalars."""
    for cid, spec_ in sorted(BASELINE.items()):
        if isinstance(spec_, dict):
            for key, value in sorted(spec_.items()):
                yield cid, key, value
        else:
            yield cid, None, spec_


def corpus_documents():
    base = ROOT / "dev/evals/samples"
    docs = []
    for p in sorted(base.rglob("*")):
        if p.suffix in (".md", ".txt") and p.is_file():
            try:
                docs.append((p, p.read_text()))
            except Exception:
                continue
    return docs


class CheckRaised(Exception):
    """A check raised. Never silently treated as an outcome."""


def run_check(cid, text):
    try:
        return grade.ALL_CHECKS[cid](text)
    except Exception as exc:
        raise CheckRaised(f"{cid} raised {type(exc).__name__}: {exc}") from exc


def flagged(result):
    return None if result is None else bool(result.get("threshold_met"))


def baseline_results(cid, texts):
    """Every result for one check under the declared table, computed once and reused."""
    results = []
    for text in texts:
        try:
            results.append(run_check(cid, text))
        except CheckRaised as exc:
            fail(f"{cid}: raised on an unmutated corpus document — {exc}")
            results.append(None)
    return results


def moves_any_document(cid, key, probe, texts, base):
    """Does replacing one declared number change any document's outcome?

    Stops at the first document that moves. A consumed cut-off usually moves one
    within a handful of documents; only a decorative one pays for the full sweep.
    """
    table = copy.deepcopy(BASELINE)
    if key is None:
        table[cid] = probe
    else:
        table[cid][key] = probe
    grade.CHECK_THRESHOLDS = table
    try:
        for text, was in zip(texts, base):
            # A check that crashes under mutation has not demonstrated that it
            # reads the declaration; it has demonstrated a bug. Never count it
            # as movement.
            if flagged(run_check(cid, text)) != was:
                return True
        return False
    except CheckRaised as exc:
        fail(f"{cid}.{key or '(value)'}: moving the declared number to {probe:g} "
             f"made the check crash — {exc}")
        return False
    finally:
        grade.CHECK_THRESHOLDS = BASELINE


# ---------------------------------------------------------------------------
# Assertions
# ---------------------------------------------------------------------------

def check_route_a(texts, baseline):
    """Declared numbers the check reads: moving one must move the corpus."""
    consumed = set()
    print("\n=== Route A: does moving the declared number move the corpus? ===")
    for cid, key, value in declared_keys():
        if cid not in grade.ALL_CHECKS:
            fail(f"{cid}: declares a cut-off but is not a registered check")
            continue
        base = [flagged(r) for r in baseline[cid]]
        probes = (0, 10 ** 6) if isinstance(value, int) else (0.0, 1e6)
        hit = next((p for p in probes if moves_any_document(cid, key, p, texts, base)), None)
        if hit is not None:
            consumed.add((cid, key))
            ok(f"{cid}.{key or '(value)'} = {value!r} governs behaviour "
               f"(moving it to {hit:g} changes the corpus)")
    return consumed


# A declared key paired with the result field that should govern it. Where both
# are present the exact boundary can be asserted, not merely its consumption.
GOVERNING_METRIC = {
    "minimum_candidates": "candidate_count",
    None: "score",
}

# Boundaries no corpus document sits either side of. The exact-predicate
# assertion still runs for these, but with no document at the cut-off itself an
# off-by-one in the comparison would be invisible, so the correspondence is
# weaker than it looks. Named rather than passed over (DR-79): a cut-off joining
# this set fails until someone states why the corpus cannot witness it.
BOUNDARY_UNWITNESSED = {
    ("no-bland-critical-template", "minimum_candidates"):
        "no document holds 2 or 3 of these phrases; the one that flags holds 11",
    ("no-boldface-overuse", "minimum_candidates"):
        "documents cluster at 3 and below or 5 and above, never at 4",
    ("no-heading-one-liners", "minimum_candidates"):
        "no document holds exactly 1, so the clear side of the cut-off is empty",
    ("no-inline-header-lists", "minimum_candidates"):
        "no corpus document holds one of these at all",
    ("no-rubric-echoing", "minimum_candidates"):
        "no corpus document holds one of these at all",
    ("no-soft-scaffolding", "minimum_candidates"):
        "documents hold 1 or fewer, or 6 or more, never 2 to 5",
}


def check_boundary_correspondence(baseline, texts):
    """Where the check exposes its metric, the declared number must BE the boundary.

    Route A proves a declared number is read. It does not prove the check uses it
    unchanged: a check enforcing `declared + 5`, or flipping the comparison, still
    moves when the declaration moves and still passes Route A. Where a check
    exposes the metric its decision turns on, that gap closes — the flag must
    equal the predicate stated in terms of the declaration.

    Keys with no exposed metric (multi-gate and statistical cut-offs) are named
    below rather than passed over, so the limit of this assertion is visible.
    """
    print("\n=== boundary: is the declared number the boundary itself? ===")
    unchecked = []
    for cid, key, value in declared_keys():
        field = GOVERNING_METRIC.get(key)
        if field is None:
            unchecked.append((cid, key))
            continue
        wrong, seen, metrics = [], 0, []
        for (path, _text), result in zip(texts, baseline[cid]):
            if result is None or result.get("context_suppressed"):
                continue
            metric = result.get(field)
            if metric is None:
                continue
            seen += 1
            metrics.append(metric)
            if bool(result.get("threshold_met")) != (metric >= value):
                wrong.append((path.name, metric, bool(result.get("threshold_met"))))
        witnessed = any(m == value for m in metrics) and any(m == value - 1 for m in metrics)
        pin = BOUNDARY_UNWITNESSED.get((cid, key))
        if witnessed and pin:
            fail(f"{cid}.{key or '(value)'} is pinned as unwitnessed, but the corpus "
                 f"now holds documents at {value!r} and {value - 1!r}. Remove the pin: "
                 f"the boundary is verifiable.")
        elif not witnessed and not pin:
            fail(f"{cid}.{key or '(value)'}: no document sits at {value!r} and none at "
                 f"{value - 1!r}, so an off-by-one in this comparison would not show. "
                 f"Give the corpus a document either side, or pin it with a reason.")

        if not seen:
            unchecked.append((cid, key))
        elif wrong:
            fail(f"{cid}.{key or '(value)'}: the report declares {value!r}, but the "
                 f"check does not flag exactly when {field} reaches it — "
                 f"{len(wrong)} document(s) disagree, e.g. {wrong[:3]} "
                 f"(document, {field}, flagged). The declared number is read but "
                 f"is not the boundary being enforced.")
        else:
            note = "" if witnessed else " (no document sits at the cut-off itself)"
            ok(f"{cid}.{key or '(value)'} = {value!r} is exactly where {field} "
               f"flips the flag, across {seen} documents{note}")
    for cid, key in unchecked:
        print(f"  consumption only: {cid}.{key or '(value)'} — no single exposed "
              f"metric governs it, so Route A is the whole assurance")


def check_every_key_covered(consumed):
    """A declared key no check reads is reported, never skipped."""
    print("\n=== coverage: is every declared cut-off read by its check? ===")
    declared = {(cid, key) for cid, key, _v in declared_keys()}
    orphans = sorted(declared - consumed)
    reported = False
    for cid, key in orphans:
        if (cid, key) in UNVERIFIABLE:
            continue
        reported = True
        fail(f"{cid}.{key or '(value)'} is declared and reaches the audit report, but "
             f"no check reads it. Either nothing consumes this key, or it was renamed "
             f"and the check silently fell back to its own default. Wire it through "
             f"threshold_value, or pin it with a reason.")
    if not reported:
        ok(f"every one of the {len(declared)} declared cut-offs is read by its check")


def check_pins():
    """Pins must name real checks and their stated reasons must hold."""
    print("\n=== pins: does each stated reason still hold? ===")
    declared = {(cid, key) for cid, key, _v in declared_keys()}
    for (cid, key), why in sorted(UNVERIFIABLE.items()):
        label = f"{cid}.{key or '(value)'}"
        if cid not in grade.ALL_CHECKS:
            fail(f"unverifiable pin names '{cid}', which is not a registered check. "
                 f"A pin on a check that does not exist verifies nothing.")
        elif (cid, key) not in declared:
            fail(f"unverifiable pin names {label}, which is not a declared cut-off. "
                 f"Remove the stale pin.")
        else:
            print(f"  pinned: {label} — {why}")
    if not UNVERIFIABLE:
        ok("no cut-off is pinned as unverifiable")


def main():
    documents = corpus_documents()
    plain = [text for _p, text in documents]
    declared = list(declared_keys())
    print(f"declared cut-offs: {len({cid for cid, _k, _v in declared})} checks, "
          f"{len(declared)} numbers   corpus documents: {len(documents)}")

    baseline = {cid: baseline_results(cid, plain)
                for cid in sorted({cid for cid, _k, _v in declared})
                if cid in grade.ALL_CHECKS}

    consumed = check_route_a(plain, baseline)
    check_every_key_covered(consumed)
    check_boundary_correspondence(baseline, documents)
    check_pins()

    print()
    if FAILURES:
        print(f"FAILED: {FAILURES} assertion(s) broken")
        sys.exit(1)
    print("ALL PASSED")


if __name__ == "__main__":
    main()
