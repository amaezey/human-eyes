# Decision walkthrough: approach and pickup guide

How the 2026-07-17 source-evaluation walkthrough works, for any agent continuing it. Read this whole file before touching anything.

## The mission

The source library (100+ cards under `human-eyes/references/sources/`) was re-reviewed against preserved source text. Every resulting recommendation is a pending decision for Mae: what each source says the product should **add, change, or remove**. The job is to bring her those decisions one at a time, implement her answers, and keep every record consistent.

## Non-negotiable rules

1. **human-eyes audits prose habits. It is not an authorship detector.** Humans fail checks too, by design; the writer decides what to keep. Never gate an addition behind authorship-grade evidence, never add authorship caveats or look-alike disclaimers to checks or user-facing docs, never design machinery to spare "legitimate human uses". Practitioner phrase lists are sufficient evidence for watch-list additions. Heavyweight evaluation is reserved for numeric direction/threshold questions (see the #53 flip) and severity changes.
2. **The audit reads text. It never interviews writers** (writer-process questions were explicitly rejected).
3. **User-facing docs (root README pattern table, patterns.md) state neutrally what a source supports.** No caveats, no negations. A source that doesn't support a row is removed from the row, not cited with a disclaimer.
4. **One decision file:** `dev/decision-register.md`. Numbered rows DR-01 upward (plus POS-01... for the POS-dependent list). Nothing pending lives anywhere else. Never invent new queues, lanes, groups, or orderings.
5. **Markdown files are for agents, not for Mae.** Decisions are presented in chat, one at a time, in this exact template, no exceptions:

   ```
   X of [TOTAL]: [PATTERN NUMBER] DESCRIPTION OF ISSUE
   <description of the issue raised by the source, with analysis>
   <the options>
   ```

   X counts decided rows + 1; TOTAL is the row count of the register. Cite the DR row. Before presenting, screen the row: strip components that contradict rules 1-3 and say so; verify every claim against its source card first (never present half-described components).

   The product has exactly two detector types. Every option that proposes a product change must name which one it lands in and state the concrete mechanism:
   - **programmatic** — a check function in `grade.py`'s registry, severity declared in `human-eyes/scripts/patterns.json` (`hard_fail` / `strong_warning` / `context_warning`). State what is matched or counted and the exact fail condition.
   - **agent-judgement** — a record in `human-eyes/scripts/judgement.json` (prompt + answer schema + `flagged_when` answers). State the prompt question and which answers flag.

   There is no third lane. "Manual guidance", "manual review", process notes, and similar card phrasing map to the judgement lane or to nothing; never present them as an option type. If a component is not viable as either type, say so and why. When a register row bundles multiple components, number them and give each component its own typed proposal so Mae can rule per component (as DR-114 was ruled).

   Report closures in plain product terms. Never narrate register mechanics in chat — extends links, closing precedents, stamp bookkeeping, which cells were touched. That is agent-facing record keeping; surface it only when it changes something Mae must rule on, and then say it in one plain sentence about the product, not the files.
6. **Closing a decision is one indivisible action, same turn:** implement (test-first for any `grade.py`/`judgement.json` change) → run the full test loop → stamp the register row (decision, commit, validation) → write the outcome into every cited source card's claim row (User decision / Implementation status cells, dated Decision history line, `- CXX: passed - <verification>` evaluation line for implemented rows) → commit. Cards must pass `python3 .agents/skills/source-ingest/scripts/validate_source.py <card>`; the only standing validator exceptions are `aranya-poetly-ai-poetry.md` (authorised partial capture) and `spero-emi-pangram-classifier.md` (retirement tombstone).
7. **Verify defect claims against the code before believing them** (reproduce live), and **never gate work on assumed session limits or the clock** — always launch; retry on visible failure.

## The files

- `dev/decision-register.md` — the one decision file. 140 DR rows + POS list. Sections: checker behaviour, product documentation, retirements, residue-mapping groups (DR-14..29), imported working-list candidates (DR-30..105, original pattern-opportunities order), recovered items (DR-106..140).
- `dev/source-ingest-hygiene-recommendation-classification-2026-07-17.csv` — all 1,636 recommendation rows, labelled by the original pass.
- `dev/source-evaluation-residue-mapping-2026-07-17.csv` — first mapping sweep (440 rows).
- `dev/source-evaluation-corrected-framing-2026-07-17.csv` — the corrected-framing sweep's 243 action items with per-claim descriptions (the "nothing" dispositions are recoverable from the classification CSV minus these).
- `dev/tools/reconcile_register.py` — completeness check; must exit 0 (every add/evaluate recommendation row accounted for by the register, pattern-opportunities citations, or the mapping CSV).
- `dev/evals/ttr-calibration-2026-07-17.md` — the #53 threshold calibration record.
- `human-eyes/references/sources/pattern-opportunities.md` — settled evidence detail only; holds no pending decisions.

## Test loop

```bash
for t in dev/evals/tests/test_*.py; do python3 "$t" >/dev/null 2>&1 || python3 -m unittest "$(echo "$t" | sed 's|/|.|g; s|\.py$||')" >/dev/null 2>&1 || echo "FAIL $t"; done
```

`patterns.md` is generated: edit `human-eyes/scripts/patterns.json`, then `python3 dev/tools/render_patterns_md.py --write`. Detection markers in it are derived from `grade.py`'s check registry and `judgement.json`; the README Check column is tested against the same derivation (`test_detection_markers.py`).

## Position (2026-07-17, after DR-115)

Decided and fully closed through question 20: rows DR-01..11, DR-39/40, DR-43, DR-106 (with DR-30), DR-111 (journalism watchlist), DR-112 (poetry watchlist), DR-113 (#19 residue families), DR-114 (components 1-2 implemented, 3-4 declined), DR-115 (with DR-44: components 4 and 6 built as #58 `no-paragraph-anaphora` and #59 `no-heading-one-liners`, commit e1002ca; components 1, 2, 3, 5 declined). Numbering ruling from DR-115: new patterns take the next plain number (58, 59, ...); never add new letter-suffixed variants — the five existing ones (10a, 23a, 31a, 35a, 35b) are grandfathered. Closing precedent: an imported row closed through a recovered row's Extends link keeps its imported text (see DR-30/DR-106); only the recovered row's cited claims get card stamps. Next open row: DR-116 (emoji density thresholds). Retirements DR-12/13/29 need verification against their cards before being asked. The POS-01/POS-02 list waits on Mae's tagger from another project.
