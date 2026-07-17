# Decision register

Single decision point for every proposed product change arising from source evidence. One row per change. Nothing in the product layer (`human-eyes/scripts/`, generated `patterns.md`, `SKILL.md`, `process.md`, root `README.md`) changes without a row here carrying Mae's decision.

Columns:

- **Evidence:** claim keys in `slug:CNN` form. These are what the reconciliation tool matches against `source-ingest-hygiene-recommendation-classification-2026-07-17.csv`.
- **Decision:** `pending`, `approved <date>`, `rejected <date>`, or `parked-for-evaluation <date>`.
- **Commit / validation:** filled when implemented; validation names the test or check that holds the change in place.

Run `python3 dev/tools/reconcile_register.py` to see how many classification rows with an additive or evaluate component are not yet accounted for by a register row. The count must reach zero before the source-evaluation pass is considered fully triaged.

## Checker behaviour

| ID | Change | Evidence | Decision | Commit | Validation |
|---|---|---|---|---|---|
| DR-01 | #26 ghost/spectral: token-boundary counting; singular+plural entries no longer double-count one occurrence | walsh-ai-poetry:C08 | approved 2026-07-17 | 13e235f | test_grade.py hygiene-pass regression block |
| DR-02 | #7 AI vocabulary: span-based counting; repeats count per occurrence, nested entries resolve to longest match | gptzero-ai-vocabulary:C13 | approved 2026-07-17 | 13e235f | test_grade.py hygiene-pass regression block |
| DR-03 | #31a unicode flair: recognize U+26A1 U+27A1 U+267B | saboo-aislopopedia:C18 saboo-aislopopedia:C19 | approved 2026-07-17 | 13e235f | test_grade.py hygiene-pass regression block |
| DR-04 | #52 sentence variance: skip under 100 words or under 6 sentences per documented eligibility; drop unmeasurable-text fail | shankar-ai-writing:C17 | approved 2026-07-17 | 13e235f | test_grade.py hygiene-pass regression block |
| DR-05 | #27 quietness: same substring-count idiom as pre-fix #26 ("quiet" counts inside "quietly"); apply the same token-boundary fix | (found during DR-01 verification, not a card recommendation) | pending | | |
| DR-06 | #53 vocabulary diversity: current low-TTR direction is challenged by higher-AI-TTR results in three sources; run the proposed matched, length-controlled evaluation before changing direction, threshold, or eligibility floor | el-attar-linguistic-features-ai-text-detection:C? przystalski-stylometry:C05 przystalski-stylometry:C24 suvanto-interpretable-llm-creative-writing:C? liang-detector-bias:C02 liang-detector-bias:C03 | pending | | |
| DR-07 | #49 em dashes: keep fail-on-any at Balanced/All, or move to density/genre-aware handling given deliberate-human-use and anti-camouflage counterevidence | bailey-em-dash-hyphens:C07 bailey-em-dash-hyphens:C09 bailey-em-dash-hyphens:C14 shankar-ai-writing:C17 ai-lifelong-learners-em-dash:C36 slate-ai-shaming-paranoia:C10 edwards-ars-em-dash:C02 phillips-ringer-em-dash:C06 | pending | | |

## Product documentation

| ID | Change | Evidence | Decision | Commit | Validation |
|---|---|---|---|---|---|
| DR-08 | patterns.json #11: reword "due to repetition-penalty mechanisms" from stated fact to proposed, untested mechanism | blader-humanizer:C17 anthropic-sonnet-prompts:C17 | pending | | |
| DR-09 | patterns.json evidence_body Clarkesworld row: the fiction tells attributed to the NPR link are reportedly absent from that page; verify the NPR page directly, then correct the citation or the attribution | clarke-clarkesworld-concerning-trend:C01 | pending | | |
| DR-10 | Root README pattern table: rewrite all caveated rows to state neutrally what each source supports; caveats move to the evidence layer | (style ruling by Mae 2026-07-17; row-by-row verification against cards during rewrite) | approved 2026-07-17, format pending | | validate against source cards per row |

## Mapping retirements (pending, not yet applied)

| ID | Change | Evidence | Decision | Commit | Validation |
|---|---|---|---|---|---|
| DR-11 | Retire the #47 Shankar mapping (unsupported exact mapping; README row 47 and card) | shankar-ai-writing:C? | pending | | |
| DR-12 | Retire the unsupported #15 mapping recorded in two cards | (claim keys to be pulled during pattern-ops restructure) | pending | | |
| DR-13 | Retire the former #39 grammar-cleanliness mapping (live #39 is placeholder residue) | (claim keys to be pulled during pattern-ops restructure) | pending | | |

## Backlog

The pattern-opportunities restructure populates this register from the eleven dated pending-decision sections and from the 933 classification rows with an additive or evaluate component. Until then, `reconcile_register.py` reports the outstanding count. Already-applied evidence-layer retirements (Copy Posse #43, Csutoras #39, Hsu #37/H8, Sussman-Carter #4/#24, Jiang-Hyland #37 adjacency) are verified against their cards during that restructure rather than ratified as a batch.
