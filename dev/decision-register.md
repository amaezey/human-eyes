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
| DR-05 | #27 quietness: same substring-count idiom as pre-fix #26 ("quiet" counts inside "quietly"); apply the same token-boundary fix. The Kriss card also records #27 runtime/documentation divergence (documented soft, hum, humming absent from the runtime list) | kriss-nyt-ai-write-like-that:C11 | pending | | |
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
| DR-29 | Retire the Stockton later-post mappings the card records as unsupported | stockton-dont-write-like-ai:C15 | pending | | |

## Candidate evaluations from the residue mapping (2026-07-17)

Grouped from the 96 candidate rows in `source-evaluation-residue-mapping-2026-07-17.csv` (per-claim descriptions live there). Each row is a pending evaluation or correction decision; approval queues the work, it does not change the checker directly.

| ID | Change | Evidence | Decision | Commit | Validation |
|---|---|---|---|---|---|
| DR-14 | Documentation and data-label corrections: README title-case label, transition-phrase doc/code drift, Kobak CSV union relabel, threshold attribution, #7 wording and aggregate-versus-document distinction, dated vocabulary table upkeep, aggregate threshold decision, Guo example provenance and #30 attribution | grammarly-common-ai-words:C02 grammarly-common-ai-words:C04 kobak-llm-excess-vocabulary:C04 kobak-llm-excess-vocabulary:C07 kobak-llm-excess-vocabulary:C09 kobak-llm-excess-vocabulary:C13 kobak-llm-excess-vocabulary:C20 kobak-llm-excess-vocabulary:C21 guo-field-guide-ai-slop:C10 guo-field-guide-ai-slop:C20 | pending | | |
| DR-15 | #5 vague-attribution variant evaluation (exact missed phrasings across four sources) | aidetectors-ai-writing-signs:C09 seoengine-ai-writing-signs:C25 wikipedia-signs-of-ai-writing:C08 sage-ai-detection-peer-reviewers:C03 | pending | | |
| DR-16 | Phrase-variant evaluations for #22/#50/#23/#24 families: missed openers, qualifier hedges, refine/differentiate and scalable-solution buzzphrases, transition overuse fixtures, generic-ending praise variants | ai-lifelong-learners-em-dash:C04 ai-lifelong-learners-em-dash:C06 guo-field-guide-ai-slop:C13 netusai-stylometry:C06 grammarly-common-ai-words:C05 grammarly-common-ai-words:C06 grammarly-common-ai-words:C07 seoengine-ai-writing-signs:C06 vollmer-machine-tell-on-itself:C05 ju-blix-williams-domain-regeneration:C17 | pending | | |
| DR-17 | Mid-line meta-commentary and conclusion-signpost variants near #33/#44/#47 | seoengine-ai-writing-signs:C07 seoengine-ai-writing-signs:C31 seoengine-ai-writing-signs:C33 | pending | | |
| DR-18 | Grammar-construction variant tests for #3 and #8 (sentence-opening participles, copula substitutes) | wikipedia-signs-of-ai-writing:C06 wikipedia-signs-of-ai-writing:C12 seoengine-ai-writing-signs:C17 | pending | | |
| DR-19 | Structure and format variant evaluations: #42 apostrophe normalisation, #31a stylized Unicode variants, proper-noun list leads, triad source fixtures, boldface drift, inline-header variants, emoji fixtures, small-table misuse, curly-quotes context, skipped-heading parsing, list-item symmetry, markdown residue, sentence-level tricolon recognition | guo-field-guide-ai-slop:C11 guo-field-guide-ai-slop:C15 wikipedia-signs-of-ai-writing:C10 wikipedia-signs-of-ai-writing:C15 wikipedia-signs-of-ai-writing:C18 wikipedia-signs-of-ai-writing:C19 wikipedia-signs-of-ai-writing:C21 wikipedia-signs-of-ai-writing:C22 wikipedia-signs-of-ai-writing:C23 wikipedia-signs-of-ai-writing:C24 seoengine-ai-writing-signs:C23 seoengine-ai-writing-signs:C27 kriss-nyt-ai-write-like-that:C14 | pending | | |
| DR-20 | Residue and disclaimer fixture evaluations near #19/#20/#39: Insert-Table publishing placeholder, cutoff-disclaimer controls, provenance-residue family, historical residue fixtures | sage-ai-detection-peer-reviewers:C14 wikipedia-signs-of-ai-writing:C26 wikipedia-signs-of-ai-writing:C27 wikipedia-signs-of-ai-writing:C29 wikipedia-signs-of-ai-writing:C42 | pending | | |
| DR-21 | Register and tone evaluations adjacent to #35/#37/#29: positive-tone register, sales-register/news mismatch, hedge-and-reassure arc, machine-cleanliness distribution, stiff substitution, conversational question beats | seoengine-ai-writing-signs:C21 ju-blix-williams-domain-regeneration:C19 vollmer-machine-tell-on-itself:C09 vollmer-machine-tell-on-itself:C14 wikipedia-signs-of-ai-writing:C13 kriss-nyt-ai-write-like-that:C13 | pending | | |
| DR-22 | Wikipedia branch evaluation set for #41: significance frames, notability enumeration, promotional genre mismatch, challenges-section composite, comment-specific composites, edit-summary mode, platform composites, positive-human controls, ineffective-indicator look-alikes | wikipedia-signs-of-ai-writing:C04 wikipedia-signs-of-ai-writing:C05 wikipedia-signs-of-ai-writing:C07 wikipedia-signs-of-ai-writing:C09 wikipedia-signs-of-ai-writing:C32 wikipedia-signs-of-ai-writing:C34 wikipedia-signs-of-ai-writing:C36 wikipedia-signs-of-ai-writing:C37 wikipedia-signs-of-ai-writing:C40 wikipedia-signs-of-ai-writing:C41 | pending | | |
| DR-23 | Fiction evaluation set for #41: tense/POV stability, redemption-arc and false-balance fixtures, Dhillon rationale-coding study, Guo ukulele passage fixture | guo-field-guide-ai-slop:C19 guo-field-guide-ai-slop:C03 vara-confessions-viral-ai-writer:C07 vara-confessions-viral-ai-writer:C18 dhillon-mfa-students-llms-fiction:C16 | pending | | |
| DR-24 | Rewrite-fidelity evaluations: ArgRewrite corpus use, cliché substitution, no-list compliance, classroom-exercise rewrites | abdulhai-llms-distort-written-language:C07 vara-confessions-viral-ai-writer:C04 vara-confessions-viral-ai-writer:C17 vollmer-machine-tell-on-itself:C28 | pending | | |
| DR-25 | Stylometry replications: Rudnicka delta replication, trigram tables, diabetes phrase controls; Shankar short-list ratio behaviour | rudnicka-chatbot-writing-style:C05 rudnicka-chatbot-writing-style:C07 rudnicka-chatbot-writing-style:C08 shankar-ai-writing:C03 | pending | | |
| DR-26 | Signal-stacking context audit against Vollmer's stacked-tell account | vollmer-machine-tell-on-itself:C02 | pending | | |
| DR-27 | Guidance additions for #41 branches and process: journalism provenance prompts, engagement-marker pedagogy, Shankar craft guidance, through-this-lens guidance, evidence-preserving review steps, metadata/full-text ingest gate | futurism-sports-illustrated-ai-writers:C02 futurism-sports-illustrated-ai-writers:C07 futurism-sports-illustrated-ai-writers:C08 futurism-sports-illustrated-ai-writers:C15 jiang-hyland-engagement-markers:C07 jiang-hyland-engagement-markers:C08 jiang-hyland-engagement-markers:C14 shankar-ai-writing:C18 shankar-ai-writing:C19 shankar-ai-writing:C21 shankar-ai-writing:C22 ai-lifelong-learners-em-dash:C07 seoengine-ai-writing-signs:C45 ju-blix-williams-domain-regeneration:C01 | pending | | |
| DR-28 | New source ingestions cited indirectly by Fairbanks: Cheng et al. (sycophancy) and Yakura et al. (vocabulary transfer) | fairbanks-atlantic-ai-writing:C14 fairbanks-atlantic-ai-writing:C17 | pending | | |

## Backlog

The pattern-opportunities restructure populates this register from the eleven dated pending-decision sections and from the 933 classification rows with an additive or evaluate component. Until then, `reconcile_register.py` reports the outstanding count. Already-applied evidence-layer retirements (Copy Posse #43, Csutoras #39, Hsu #37/H8, Sussman-Carter #4/#24, Jiang-Hyland #37 adjacency) are verified against their cards during that restructure rather than ratified as a batch.
