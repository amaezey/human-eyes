# Decision walkthrough: approach and pickup guide

How the 2026-07-17 source-evaluation walkthrough works, for any agent continuing it. Read this whole file before touching anything.

## The mission

The source library (100+ cards under `human-eyes/references/sources/`) was re-reviewed against preserved source text. Every resulting recommendation is a pending decision for Mae: what each source says the product should **add, change, or remove**. The job is to bring her those decisions one at a time, implement her answers, and keep every record consistent.

## Non-negotiable rules

1. **human-eyes audits prose habits. It is not an authorship detector.** Humans fail checks too, by design; the writer decides what to keep. Never gate an addition behind authorship-grade evidence, never add authorship caveats or look-alike disclaimers to checks or user-facing docs, never design machinery to spare "legitimate human uses". Practitioner phrase lists are sufficient evidence for watch-list additions. Heavyweight evaluation is reserved for numeric direction/threshold questions (see the #53 flip) and severity changes.
2. **The audit reads text. It never interviews writers** (writer-process questions were explicitly rejected).
3. **User-facing docs (root README pattern table, patterns.md) state neutrally what a source supports.** No caveats, no negations. A source that doesn't support a row is removed from the row, not cited with a disclaimer.
4. **One decision file:** `dev/decision-register.md`. Numbered rows DR-01 upward (plus POS-01... for the POS-dependent list). Nothing pending lives anywhere else. Never invent new queues, lanes, groups, or orderings. Decision statuses are exactly four — `pending`, `approved <date>`, `rejected <date>`, `pos-dependent-pattern <date>` — use them verbatim and never coin new ones ("record-only", "parked", etc.) in rows or in chat; parked-for-evaluation was removed by Mae 2026-07-17. `pos-dependent-pattern` (added by Mae the same day) is reserved solely for patterns blocked on her POS tagger; nothing buildable right now may carry it. An approved evaluation or deferred design stays `pending` until its concrete result is ruled on.
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

   Options are always a labelled list (a, b, c...), one decision surface per question; never a prose paragraph ending in a bare yes/no (Mae, 2026-07-17). Name product actions by their exact names (Audit, Suggestions, Rewrite, Write, Save report), never coinages like "run".

   Report closures in plain product terms. Never narrate register mechanics in chat — extends links, closing precedents, stamp bookkeeping, which cells were touched. That is agent-facing record keeping; surface it only when it changes something Mae must rule on, and then say it in one plain sentence about the product, not the files.
6. **Closing a decision is one indivisible action, same turn:** implement (test-first for any `grade.py`/`judgement.json` change) → run the full test loop → stamp the register row (decision, commit, validation) → write the outcome into every cited source card's claim row (User decision / Implementation status cells, dated Decision history line, `- CXX: passed - <verification>` evaluation line for implemented rows) → orphan sweep: every claim cited by the row and by its Extends target must now carry a ruling or its own queue row; anything unruled gets a new row and gets asked, never silently dropped → commit. Cards must pass `python3 .agents/skills/source-ingest/scripts/validate_source.py <card>`; the only standing validator exceptions are `aranya-poetly-ai-poetry.md` (authorised partial capture) and `spero-emi-pangram-classifier.md` (retirement tombstone).
7. **Verify defect claims against the code before believing them** (reproduce live), and **never gate work on assumed session limits or the clock** — always launch; retry on visible failure.

## The files

- `dev/decision-register.md` — the one decision file. 153 DR rows + POS list, one uniform seven-column layout (ID | Change | Evidence | Extends | Decision | Commit | Validation) across every section; its own "How to read this file" header is canonical. Sections group by origin only: checker behaviour, product documentation, retirements, residue-mapping groups (DR-14..29), imported working-list candidates (DR-30..105), recovered items and orphan re-queues (DR-106..153).
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

## Position (2026-07-18, after DR-123)

Decided and closed: DR-01..11, DR-30 (via DR-106), DR-39/40, DR-43..49 (via their recovered rows), DR-106, DR-111..123, DR-116, and orphan rows DR-141..152 except DR-144. Standing rulings recorded in the rules above: plain pattern numbers only (catalogue now runs to #61); four statuses verbatim; two detector types named in every option; labelled option lists in question order; product action names used exactly (Audit, Suggestions, Rewrite, Write, Save report); closures reported in product terms; the orphan sweep is part of every close.

Built today across DR-111..123 and DR-150: the journalism and poetry watchlists, five #19 residue families, #39 platform-residue additions, #58 `no-paragraph-anaphora`, #59 `no-heading-one-liners`, #60 `no-modal-stacks`, #61 `unprompted_caveats` (agent), unnumbered agent judgement `change_narration`, the #53 windowed flip, six #22 generalisations plus new entries, six #23 hedge cues plus `can potentially`, three #7 intensifiers, the #24 peppy-ending shape trigger, five #41 fiction dialogue dimensions, and prompt extensions to tonal_uniformity, neutrality_collapse, underspecified_language, vacuous_connection, and semantic_redundancy. DR-116 closed: the emoji-threshold calibration could not test the question (no emoji-bearing corpus); threshold unchanged per Mae. DR-120 closed with no personal/social baseline comparison. DR-121 added only `change_narration`; its five process/report components made no product change under the standing rules. DR-122's five distinct factual-integrity and citation-validation components were all rejected; no product change. DR-123 added the five dialogue dimensions only; no Elara/Kael name rule or new metaphor mechanism.

The register was normalised 2026-07-18 (commit 8e99aab): one seven-column layout, statuses clean, link-closures visible, truncations repaired, "How to read this file" header canonical. Current counts after DR-123: 106 open, 46 decided, 3 pos-dependent-pattern (POS-01, POS-02, DR-144 wait on Mae's tagger).

Next: DR-124, then DR-125..140 in row order, then retirements DR-12/13/29 (verify against their cards before asking), the residue groups DR-14..28, the imported rows DR-31..105, and DR-153 (SWBST). A like-for-like social/chat corpus for any future emoji rerun is noted in the DR-116 record but not queued.
