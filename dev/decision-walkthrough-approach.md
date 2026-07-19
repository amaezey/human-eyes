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

## Position (2026-07-19, after DR-135 closure)

Decided and closed: DR-01..11, DR-30 (via DR-106), DR-39/40, DR-43..49 (via their recovered rows), DR-106, DR-111..127, DR-135, and orphan rows DR-141..152 except DR-144. Standing rulings recorded in the rules above: plain pattern numbers only (catalogue now runs to #62); four statuses verbatim; two detector types named in every option; deterministic routing first and agent judgement last; labelled option lists in question order; product action names used exactly (Audit, Suggestions, Rewrite, Write, Save report); closures reported in product terms; the orphan sweep is part of every close.

Built today across DR-111..125 and DR-150: the journalism and poetry watchlists, five #19 residue families, #39 platform-residue additions, #58 `no-paragraph-anaphora`, #59 `no-heading-one-liners`, #60 `no-modal-stacks`, #61 `unprompted_caveats` (agent), unnumbered agent judgement `change_narration`, the #53 windowed flip, six #22 generalisations plus new entries, six #23 hedge cues plus `can potentially`, three #7 intensifiers plus 38 exact vocabulary forms, the #24 peppy-ending shape trigger, five #41 fiction dialogue dimensions, and prompt extensions to tonal_uniformity, neutrality_collapse, underspecified_language, vacuous_connection, semantic_redundancy, and formulaic_parallelism. DR-116 closed: the emoji-threshold calibration could not test the question (no emoji-bearing corpus); threshold unchanged per Mae. DR-120 closed with no personal/social baseline comparison. DR-121 added only `change_narration`; its five process/report components made no product change under the standing rules. DR-122's five distinct factual-integrity and citation-validation components were all rejected; no product change. DR-123 added the five dialogue dimensions only; no Elara/Kael name rule or new metaphor mechanism. DR-124 added programmatic aphorism-formula detection to #42 and the `an X with Y and Z` family to `formulaic_parallelism`; generic professional-content personification was rejected. DR-125 added all 38 approved exact forms to programmatic #7 without changing its paragraph threshold.

DR-126 is closed. Its claimed `valuable`-inside-`invaluable` threshold bug was already closed by DR-02's span-based longest-match counting (`13e235f`). Mae rejected adding a separate repetition-versus-distinct-family statistic to #7 evidence: both shapes already fail programmatically at the existing occurrence threshold, and the emitted match list already shows whether one term repeats or several terms cluster. Mae approved deterministic document-wide co-occurrence for Kousha and Thelwall C13: #7 now also fails when two distinct source-defined families appear anywhere in the document, even across paragraphs, and reports each canonical family with its exact matched occurrences. The existing three-occurrences-in-one-paragraph condition remains unchanged. Mae also approved the GPTZero C05 integrity test: the runtime's ordered 100-phrase list must exactly equal the preserved client payload after normalising its one curly apostrophe. This is a test-only drift guard and does not change runtime detection. Mae rejected dedicated grader fixtures for the four Juzek-Ward appendix abstracts: all four are manipulated GPT-3.5 experimental stimuli, they provide no legitimate-writing control or clear desired output, and the source card already preserves the current focused results.

DR-127 is closed. Mae chose concise GPTZero provenance: the false `April 2026` revision month is removed, and #7 identifies GPTZero's 100-row AI Vocabulary client payload. The page's `Top 50` mismatch and viewer-clock date behavior remain in the GPTZero source record rather than the catalogue. The programmatic matcher, thresholds, and severity are unchanged. All other row components made no product change under standing rule 1. Next unresolved row: DR-128, Kobak citation scope corrections.

DR-136A is implemented. Mae chose a separate source-bound `rewrite_stance_drift` agent judgement: it flags a rewrite that adds a prescription, recommendation, solution, or call to action; intensifies or reverses source stance; or erases or neutralises it. `neutrality_collapse` is unchanged. DR-136 stays pending only for its lower-priority fixture-licensing, mapping-retirement, and dated spelling-candidate components; continue the significance queue before returning to them.

DR-135A is implemented. Mae approved all four remaining C04 X-to-Y reversal shapes for programmatic #9: stop/start, future-replacement, dead/next, and forget/focus. The live matcher now recognises all ten catalogue forms with #9's existing severity and one-occurrence failure condition. DR-135 remains pending for its independent social-post families.

DR-135B is implemented. Mae approved the six previously uncovered C01 throat-clearer openers for programmatic #50. Together with the three manufactured-insight forms already caught by #42 and `I'll be honest` in #56, all ten catalogue throat-clearers now produce deterministic findings. DR-135 remains pending for its other independent social-post families.

DR-135C is implemented. Mae approved all ten C02 false-exclusivity hooks for programmatic #42. The exact hidden-, suppressed-, secrecy-, and insider-knowledge structures now fail with #42's existing severity and one-occurrence condition. DR-135 remains pending for its other independent social-post families.

DR-135D is implemented. Mae chose to fold all nine C03 manufactured-urgency hooks into programmatic #42 rather than create a separate pattern number. They use #42's existing severity and one-occurrence failure condition. DR-135 remains pending for its other independent social-post families.

DR-135E is implemented. Mae chose to fold all six C05 numbered-list hook structures into programmatic #50 rather than create a separate pattern number. The regex branches recognise plain paragraph openers and Markdown headings and use #50's existing severity and one-occurrence failure condition. #31 and #38 remain separate list-density and repeated-scaffolding checks. DR-135 remains pending for its other independent social-post families.

DR-135F is implemented. Mae chose split programmatic routing for the six previously uncovered C06 dramatic-fragment forms. `Full stop`, `Period`, `That's it. That's the tweet`, and `[One word]. That's the word` are exact one-match branches in #25; `Sit with that for a second` and the louder-for-the-back command are in #42. Together with the three forms already covered, all nine C06 forms now produce findings. No new pattern was created. DR-135 remains pending for its other independent social-post families.

DR-135G is implemented. Mae chose to fold all eight previously uncovered C07 vulnerability and anticipated-backlash frames into programmatic #56. Its label is now performed candour and vulnerability; its severity and one-occurrence failure condition are unchanged. Together with the form already covered, all nine C07 forms now fail #56.

Mae corrected the remaining walkthrough granularity: source C-labels are evidence-taxonomy rows, not separate product decisions. Present the rest of DR-135 in one consolidated analysis that maps every family to existing programmatic rules or genuinely necessary new mechanisms. Ask separately only where the proposed product action materially differs, not once per source family.

DR-135 is closed. Mae approved the remaining source families as one consolidated product decision. C08, C10, C11, C13, C14, and C23-C26 now route programmatically across existing #1, #4, #7, #9, #22, #23a, #24, #42, #43, and #50 mechanisms; C09 was already covered and required no behaviour change. New #62 `no-formulaic-social-posts` catches complete engagement-request, agreement-comment, engagement-comment, credential-preface, AI-wrapper, time-compression, and scarcity-hook formulas, reports their subtype, and issues a strong warning on one complete matched frame. No remaining DR-135 family was assigned to agent judgement.

DR-132 is closed. Mae approved the six exact marketing hype formulas for #4, the three exact adjective-noun phrases as #7 clustering candidates, and two email opener templates for #50. Mae rejected a new #63 dense-paragraph check and rejected every proposed #41 marketing-email addition, so those mechanisms remain unchanged. The shorter greeting variant stays with DR-134; source-control and provenance rows make no product change.

DR-133 is closed. Mae approved all executable gaps as existing-rule regex expansions: #1 significance phrases, #4 `rich cultural heritage`, two #7 clustering candidates, two #22 editorial frames, the #2 multi-outlet list shape, the #24 challenge-ending formula, and bare `studies show` under #5. Three source phrases were already covered and required no change; Russell's broader tidy-conclusion category produced no separate surface rule. No agent-judgement mechanism was added.

DR-134 is closed with option B. Mae approved the exact #50 transition, signposting, and email openers; the exact #56 candour frames; and `straightforward` as a #7 clustering candidate. Mae rejected a content-bearing exception for #44 and rejected connector-density logic, so #44 and all density mechanisms remain unchanged.

DR-15 is closed with option A. Mae approved every remaining exact vague-attribution and research-boilerplate form: five #5 variants and two #22 formulas. The other source-listed attribution forms were already covered. No agent-judgement mechanism was added.

DR-16 is closed with option A. Mae approved every remaining exact phrase variant through the existing #7, #22, #23, #24, #42, and #50 programmatic mechanisms. Previously implemented transitions, qualifiers, and filler forms required no duplicate changes. No new checker or agent-judgement mechanism was added.

DR-17 is rejected. The current evaluation did not show the proposed sentence-position variants occurring more often in generated prose: only one newly relevant structural-narration form appeared in the five matched AI-rewrite samples, no newly relevant mid-line conclusion form appeared, and the broader sample folders did not favour the generated set. #44 and #47 remain unchanged; the register's unrelated #33 reference was removed.

The register was normalised 2026-07-18 (commit 8e99aab): one seven-column layout, statuses clean, link-closures visible, truncations repaired, "How to read this file" header canonical. Current counts after DR-17: 95 open, 57 decided, 3 pos-dependent-pattern (POS-01, POS-02, DR-144 wait on Mae's tagger).

Next by current product significance: the remaining executable variant groups DR-18..20 and DR-93. Re-scan the full pending register after each closure rather than treating this as a fixed row-order queue. Agent-judgement branches and product-unlocking evaluations follow the executable programmatic gaps. Documentation, provenance, caveats, citation mappings, and source-record-only rows are last. A like-for-like social/chat corpus for any future emoji rerun is noted in the DR-116 record but not queued.
