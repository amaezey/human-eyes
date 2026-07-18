# Decision walkthrough: approach and pickup guide

How the 2026-07-17 source-evaluation walkthrough works, for any agent continuing it. Read this whole file before touching anything.

## The mission

The source library (100+ cards under `human-eyes/references/sources/`) was re-reviewed against preserved source text. Every resulting recommendation is a pending decision for Mae: what each source says the product should **add, change, or remove**. The job is to bring her those decisions one at a time, implement her answers, and keep every record consistent.

## Non-negotiable rules

1. **human-eyes audits prose habits. It is not an authorship detector.** Humans fail checks too, by design; the writer decides what to keep. Never evaluate whether a finding or its wording proves or implies authorship: that question is outside the product. Never ask whether a source establishes a project-owned programmatic threshold; the product chooses useful thresholds for surfacing and rewriting patterns AI overuses. Never gate an addition behind authorship-grade evidence, add authorship caveats or look-alike disclaimers to checks or user-facing docs, or design machinery to spare "legitimate human uses". Practitioner phrase lists are sufficient evidence for watch-list additions. Heavyweight evaluation is reserved for deciding a genuinely uncertain numeric direction or threshold (see the #53 flip) and severity changes, not for demanding that a source supply the chosen cutoff.
2. **The audit reads text. It never interviews writers** (writer-process questions were explicitly rejected).
3. **User-facing docs (root README pattern table, patterns.md) state neutrally what a source supports.** No caveats, no negations. A source that doesn't support a row is removed from the row, not cited with a disclaimer.
4. **One decision file:** `dev/decision-register.md`. Numbered rows DR-01 upward (plus POS-01... for the POS-dependent list). Nothing pending lives anywhere else. Never invent new queues, lanes, groups, or orderings. Decision statuses are exactly four — `pending`, `approved <date>`, `rejected <date>`, `pos-dependent-pattern <date>` — use them verbatim and never coin new ones ("record-only", "parked", etc.) in rows or in chat; parked-for-evaluation was removed by Mae 2026-07-17. `pos-dependent-pattern` (added by Mae the same day) is reserved solely for patterns blocked on her POS tagger; nothing buildable right now may carry it. An approved evaluation or deferred design stays `pending` until its concrete result is ruled on.
5. **Markdown files are for agents, not for Mae.** Decisions are presented in chat, one at a time, in this exact template, no exceptions:

   ```
   X of [TOTAL]: [PATTERN NUMBER] DESCRIPTION OF ISSUE
   <description of the issue raised by the source, with analysis>
   <the options>
   ```

   X counts decided rows + 1; TOTAL is the row count of the register. Cite the DR row. Select the next pending decision by product significance, never by row number or source-review order. Prioritise core Rewrite and Audit correctness, then broad programmatic coverage, narrow programmatic variants, agent-judgement coverage, product-unlocking evaluation, and finally documentation, provenance, caveats, mappings, and source-record-only work. Re-scan all pending rows after every closure because a newly exposed product decision may outrank the saved queue. Before presenting, screen the row: strip components that contradict rules 1-3 and say so; verify every claim against its source card first (never present half-described components).

   The product has exactly two detector types. Every option that proposes a product change must name which one it lands in and state the concrete mechanism:
   - **programmatic** — a check function in `grade.py`'s registry, severity declared in `human-eyes/scripts/patterns.json` (`hard_fail` / `strong_warning` / `context_warning`). State what is matched or counted and the exact fail condition.
   - **agent-judgement** — a record in `human-eyes/scripts/judgement.json` (prompt + answer schema + `flagged_when` answers). State the prompt question and which answers flag.

   **Routing order is deterministic first, agent judgement last.** If a surface form can be matched or counted with regex or another deterministic text operation, propose it as programmatic. Do not reroute it to agent judgement because a person could also use the form, because an occurrence might be intentional, or because the rule may produce many findings. Those are not product objections: Audit surfaces AI-overused habits so the writer can revise them or keep them intentionally. Agent judgement is reserved for failures whose defining condition is not available from the text's surface form.

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

## Position (2026-07-18, after DR-136A)

Decided and closed: DR-01..11, DR-30 (via DR-106), DR-39/40, DR-43..49 (via their recovered rows), DR-106, DR-111..127, and orphan rows DR-141..152 except DR-144. Standing rulings recorded in the rules above: plain pattern numbers only (catalogue now runs to #61); four statuses verbatim; two detector types named in every option; deterministic routing first and agent judgement last; labelled option lists in question order; product action names used exactly (Audit, Suggestions, Rewrite, Write, Save report); closures reported in product terms; the orphan sweep is part of every close.

Built today across DR-111..125 and DR-150: the journalism and poetry watchlists, five #19 residue families, #39 platform-residue additions, #58 `no-paragraph-anaphora`, #59 `no-heading-one-liners`, #60 `no-modal-stacks`, #61 `unprompted_caveats` (agent), unnumbered agent judgement `change_narration`, the #53 windowed flip, six #22 generalisations plus new entries, six #23 hedge cues plus `can potentially`, three #7 intensifiers plus 38 exact vocabulary forms, the #24 peppy-ending shape trigger, five #41 fiction dialogue dimensions, and prompt extensions to tonal_uniformity, neutrality_collapse, underspecified_language, vacuous_connection, semantic_redundancy, and formulaic_parallelism. DR-116 closed: the emoji-threshold calibration could not test the question (no emoji-bearing corpus); threshold unchanged per Mae. DR-120 closed with no personal/social baseline comparison. DR-121 added only `change_narration`; its five process/report components made no product change under the standing rules. DR-122's five distinct factual-integrity and citation-validation components were all rejected; no product change. DR-123 added the five dialogue dimensions only; no Elara/Kael name rule or new metaphor mechanism. DR-124 added programmatic aphorism-formula detection to #42 and the `an X with Y and Z` family to `formulaic_parallelism`; generic professional-content personification was rejected. DR-125 added all 38 approved exact forms to programmatic #7 without changing its paragraph threshold.

DR-126 is closed. Its claimed `valuable`-inside-`invaluable` threshold bug was already closed by DR-02's span-based longest-match counting (`13e235f`). Mae rejected adding a separate repetition-versus-distinct-family statistic to #7 evidence: both shapes already fail programmatically at the existing occurrence threshold, and the emitted match list already shows whether one term repeats or several terms cluster. Mae approved deterministic document-wide co-occurrence for Kousha and Thelwall C13: #7 now also fails when two distinct source-defined families appear anywhere in the document, even across paragraphs, and reports each canonical family with its exact matched occurrences. The existing three-occurrences-in-one-paragraph condition remains unchanged. Mae also approved the GPTZero C05 integrity test: the runtime's ordered 100-phrase list must exactly equal the preserved client payload after normalising its one curly apostrophe. This is a test-only drift guard and does not change runtime detection. Mae rejected dedicated grader fixtures for the four Juzek-Ward appendix abstracts: all four are manipulated GPT-3.5 experimental stimuli, they provide no legitimate-writing control or clear desired output, and the source card already preserves the current focused results.

DR-127 is closed. Mae chose concise GPTZero provenance: the false `April 2026` revision month is removed, and #7 identifies GPTZero's 100-row AI Vocabulary client payload. The page's `Top 50` mismatch and viewer-clock date behavior remain in the GPTZero source record rather than the catalogue. The programmatic matcher, thresholds, and severity are unchanged. All other row components made no product change under standing rule 1. Next unresolved row: DR-128, Kobak citation scope corrections.

DR-136A is implemented. Mae chose a separate source-bound `rewrite_stance_drift` agent judgement: it flags a rewrite that adds a prescription, recommendation, solution, or call to action; intensifies or reverses source stance; or erases or neutralises it. `neutrality_collapse` is unchanged. DR-136 stays pending only for its lower-priority fixture-licensing, mapping-retirement, and dated spelling-candidate components; continue the significance queue before returning to them.

The register was normalised 2026-07-18 (commit 8e99aab): one seven-column layout, statuses clean, link-closures visible, truncations repaired, "How to read this file" header canonical. Current counts after DR-127: 102 open, 50 decided, 3 pos-dependent-pattern (POS-01, POS-02, DR-144 wait on Mae's tagger).

Next by current product significance: DR-135 social-post coverage; DR-132 marketing-email coverage; DR-133 promotional and conclusion variants; DR-134 transition and opener variants; then the executable variant groups DR-15..20 and DR-93. Re-scan the full pending register after each closure rather than treating this as a fixed row-order queue. Agent-judgement branches and product-unlocking evaluations follow the executable programmatic gaps. Documentation, provenance, caveats, citation mappings, and source-record-only rows are last. A like-for-like social/chat corpus for any future emoji rerun is noted in the DR-116 record but not queued.
