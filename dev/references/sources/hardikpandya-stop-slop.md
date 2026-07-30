# hardikpandya/stop-slop

## Metadata

- **URL:** https://github.com/hardikpandya/stop-slop
- **Author / owner:** Hardik Pandya / hardikpandya
- **Published:** No reliable fixed publication date; the preserved changelog claims an initial release on 2025-01-12 and later entries on 2026-01-12 and 2026-01-13, while the reviewed commit is dated 2026-03-17
- **Retrieved:** 2026-07-14
- **Extracted:** 2026-07-14
- **Source type:** Practitioner-authored prose-editing skill repository
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** Git commit 8da1f030185bdfe8471220585162991eaeb970e9
- **Version / revision:** `main` at `8da1f030185bdfe8471220585162991eaeb970e9`; unchanged from the pre-contract snapshot
- **Full-text status:** complete
- **Snapshot:** `snapshots/hardikpandya-stop-slop.md`
- **Extraction method:** existing raw.githubusercontent.com repository-file snapshot at the reviewed commit; the independent review fetched only the linked README image to assess the recorded omission and did not alter the snapshot
- **Snapshot SHA-256:** `6bfa512c1adffdae20a3c8f8bacda1b736d69184eb657215bb70f8304dedb9c8`
- **Model / corpus scope:** No evaluated model, corpus, comparison group, language sample, text-length sample or collection period; the repository names Claude and other LLMs only as deployment contexts
- **Access limitations:** The snapshot omits the MIT licence text and the bytes of the linked README image. The licence does not bear on the prose claims. During independent review, the image at the URL preserved in the snapshot was fetched and visually inspected as PNG SHA-256 `0d7e66eb08138d14bb644485a936f2d7ad9762fc1189891789bdf4c7b3c813bc`; it contains a promotional title and cropped variants of C06, C10, C15/C16, C23 and C27 already present in the preserved prose, with no unique claim. The image bytes remain unpreserved. All six prose-bearing repository files are preserved. The publication-date conflict remains unresolved.

## Summary

`stop-slop` is a prescriptive editing skill that bans or rewrites phrase families, structural templates, rhythm habits and distancing constructions it associates with predictable AI prose. Its six preserved content files supply 49 relevant claims and examples, especially around contrast, negation, fragmentation and rhetorical setup. The source offers no corpus, human comparison, model-version study, frequency estimate, accuracy result or authorship evidence, so it can support candidate generation and editing prompts but cannot set project severity, thresholds or universal bans.

## Main insights

- The source contributes a dense practitioner inventory of structural constructions, not an empirical estimate of how often AI or human writers use them.
- Literal phrases, punctuation and templates can support deterministic candidate recognition. Semantic ideas such as false agency, specificity, trust and quotability require contextual judgement.
- The source treats several legitimate devices as absolute faults, including all adverbs, passive voice, Wh- openers, em dashes and three-item lists. Human-eyes requires controls for genre, quotation and deliberate use instead.
- Each of the five worked rewrites retains or introduces at least one construction the repository rejects elsewhere, and some discard source meaning. They are examples of the author's preference, not validated demonstrations of safe editing.
- The five-dimension score and 35/50 revision threshold are subjective and unvalidated. They do not support a detector or product threshold.

## Evidence and claims to extract

- **Direct source reviewed:** The preserved snapshot of `README.md`, `SKILL.md`, `CHANGELOG.md`, `references/phrases.md`, `references/structures.md` and `references/examples.md` from Git commit `8da1f030185bdfe8471220585162991eaeb970e9`.
- **Method and sample:** Practitioner rules, inventories and five worked rewrites. No text corpus, comparison group, model/version test, date-bounded sample, genre sample, language sample, frequency analysis or validation set is supplied.
- **Direct versus cited evidence:** C01 to C49 are direct practitioner prescriptions or examples from the repository. The source cites no external studies or datasets.
- **Important limits and counterexamples:** The source provides no human baseline and no evidence that a single pattern or cluster establishes authorship. All five worked rewrites conflict with at least one source rule: Example 1 creates a three-sentence staccato run; Example 2 retains the banned extreme `Nobody` and removes qualified or motivational meaning; Example 3 deletes most of the source content and uses two clipped sentences, one elliptical; Example 4 retains an em dash; and Example 5 retains a positive-then-negative contrast. Absolute bans, the worked rewrites and the C49 score remain editorial preferences rather than validated findings.

## Matched patterns / rules

- Deterministic checks: `no-manufactured-insight`, `no-formulaic-openers`, `no-ai-vocabulary-clustering`, `no-corporate-ai-speak`, `no-performed-candour`, `no-excessive-hedging`, `no-significance-inflation`, `no-filler-phrases`, `no-soft-scaffolding`, `no-section-scaffolding`, `no-false-concession-hedges`, `no-negative-parallelisms`, `no-countdown-negation`, `no-staccato-sequences`, `no-anaphora`, `no-rhetorical-questions`, `no-forced-triads`, `no-tidy-paragraph-endings`, `paragraph-length-uniformity`, `sentence-length-variance`, `no-em-dashes`, `no-nonliteral-land-surface` and `no-vague-attributions`.
- Agent assessments: `formulaic_parallelism`, `underspecified_language`, `performed_candour`, `referential_clarity`, `semantic_redundancy`, `vacuous_connection` and `genre_specific` in `human-eyes/scripts/judgement.json`.
- Guidance and research: `human-eyes/references/process.md`, H9, H11, H12, H21, H22, H24 and H27 in `dev/hypotheses.md`, plus the non-authorship product boundary in `STRATEGY.md`.

## Associated hypotheses

- H9, field-guide voice with similar-species disambiguation per pattern.
- H11, manufactured insight is register-coded in long-form essay.
- H12, genre-aware threshold calibration.
- H21, low information density and wrong sentence subject.
- H22, long-tail compression and grammatical standardisation.
- H24, register-specific vocabulary density.
- H27, performative profundity and aphoristic closure.
- Proposed follow-up, undecided: test source-specific structural candidates against matched human controls before deciding whether any checker, registry, guidance or hypothesis change is justified.
