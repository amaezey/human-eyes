# David J. Germain: Writing Dialog with ChatGPT

## Metadata

- **URL:** https://medium.com/@dave.germain.79/writing-dialog-with-chatgpt-bd8024a69eb3
- **Author / owner:** David J. Germain
- **Published:** 2023-02-18T14:13:00Z
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** practitioner observation and fiction-writing process commentary
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** Medium post ID `bd8024a69eb3`
- **Version / revision:** live page state retrieved 2026-07-15; prior Jina capture extracted 2026-05-05; Medium exposes no publisher revision number
- **Full-text status:** complete
- **Snapshot:** `snapshots/germain-chatgpt-dialog.md`
- **Extraction method:** complete Jina Reader URL-to-Markdown capture fetched with `curl`, checked against the rendered canonical Medium page at the beginning, middle, and end; command-line requests for canonical HTML and `?format=json` returned HTTP 403
- **Snapshot SHA-256:** `2f7fb7d79d9b4b4930baab85ee8c453858bcf51ecd0d59a171a12c6278f09c9a`
- **Model / corpus scope:** unspecified February 2023 ChatGPT model and product surface; English fiction dialogue; one practitioner, one canonical trunk scene, one seven-turn vanilla generation, an unspecified number of Elmore Leonard dialogue samples analysed through ChatGPT, and 16 preserved turns from the first two chunks of one iterative generation sequence; generation settings, full analysis outputs, exact sample count, repeated trials, and comparison corpus are not supplied
- **Access limitations:** none for the complete substantive article text. The canonical rendered page and current Jina capture agree on all seven substantive sections, prompts, dialogue examples, and conclusion takeaways. Medium account and newsletter chrome were removed. Seven decorative article-image URLs and captions are preserved without image bytes. The quoted *Out of Sight* passage is cited evidence, not Germain's direct experimental material.

## Summary

Germain gives a dated practitioner account of using ChatGPT to analyse an Elmore Leonard passage and turn the resulting discourse categories into dialogue instructions. One vanilla generation displays explicit role exposition and undifferentiated voices. A later, iteratively prompted generation shows some differentiation, but Bob and Tony still blend while Officer is recognisable; parenthetical stage directions and blunt ethics/bravery exposition remain. The article contributes concrete fiction-review prompts for rhythm, diction, speech acts, register, discourse markers, prosody, fragments, and role-explaining dialogue. It does not measure prevalence, compare current models, validate a detector, or establish that demographic prompting, short-sentence targets, or the full recipe improve dialogue generally.

## Main insights

- Germain avoids a direct “write in the style of” request. He asks ChatGPT to analyse Leonard dialogue, asks for a second AI-facing instruction, combines topics across several unspecified samples, and uses the resulting paragraph as a generation prompt.
- The seven-turn vanilla output states occupations and motivations directly. Germain calls it on-the-nose and says Karen and Jack have no difference in voice.
- The author-reported analysis categories include sentence length, parts of speech, declaratives versus questions, word choice, grammar, register, speech acts, discourse markers, prosody, fragments, instructions, and dialogue tags.
- The resulting prescription calls for informal colloquial register, mostly four-to-five-word sentences with some ten-to-fifteen-word sentences, one-to-three clauses, simple and compound structures, fragments, contractions, second-person pronouns, mixed sentence functions, and discourse markers. These are practitioner instructions, not measured Leonard statistics in the preserved article.
- Germain supplies demographic information to prompt colloquial differentiation and says it must be repeated. He reports no stereotyping controls, alternative prompt conditions, or comparison without demographics.
- He withholds the science-fiction setting at first to avoid prompt misalignment, improvises rewrites, renames a model-introduced character, and supplies more demographic information. The complete prompt history and intermediate outputs are not preserved.
- Bob and Tony still blend in the reported result, while Officer is easier to identify without dialogue tags. This is a direct counterexample to any claim that the instruction or demographics guarantee distinct voices.
- One of seven vanilla turns and 11 of 16 final-result turns contain parenthetical stage directions. The article neither criticises nor tests them, so it cannot support treating parentheticals as an AI-writing defect.
- The improved output still contains repeated `I'm telling` turns, explicit ethics and bravery exposition, and the contrast `with pride, not fear`. The colloquial instruction did not eliminate every role-explaining or formulaic construction.
- A focused surface-only comparison is incomplete by design. The 113-word vanilla excerpt stayed clear on B3 and G9 with sentence-length standard deviation 5.1; the 180-word prompted result added one B3 finding and flagged G9 at standard deviation 2.5. E5 stayed clear in both; C5 reported 19 curly glyphs in vanilla and 18 in the result. These are project-coverage observations, not a complete Audit or validation of the source's recipe.
- The source is model-version stale and narrow: one 2023 practitioner workflow, one scene, unknown ChatGPT version, unknown generation parameters, unspecified analysis-sample count, selected outputs, no blinding, no rates, and no matched human or model control.

## Evidence and claims to extract

- **Direct source reviewed:** Complete Medium post `bd8024a69eb3` as rendered and captured on 2026-07-15, including seven substantive sections, one Leonard comparison passage, three analysis/development prompts, one derived instruction paragraph, three generation-prompt excerpts (one complete vanilla prompt and visibly ellipsised Tony/Bob and Officer prompts), a seven-turn vanilla dialogue, 16 reported result turns, seven illustration references/captions, and three conclusion takeaways. The exact prior 2026-05-05 snapshot bytes were verified and archived before replacement.
- **Method and sample:** Practitioner self-report and selected examples. Germain gives one vanilla prompt/output, quotes one passage from Leonard's *Out of Sight*, says he ran an analysis prompt against several dialogue samples, derives an instruction paragraph, supplies character demographics, iterates through unspecified rewrites, and reproduces the first two result chunks. No model/version, temperature, seed, interface, complete prompt log, count of analysed samples, full analysis outputs, repeated generations, blinded ratings, or comparison corpus appears.
- **Direct versus cited evidence:** C01-C03 and C05-C17 come directly from Germain's described process, selected prompts, outputs, interpretations, or this review's source-bound project comparison. C04 is a cited Leonard passage and Germain's craft judgement, not measured evidence produced by the article. C06-C10 and C17 separate author interpretation or reviewer inference from visible examples. C16 is this review's focused live-project result, not a claim made by Germain.
- **Important limits and counterexamples:** Bob and Tony remain hard to distinguish after the intervention; parenthetical stage directions remain but are not criticised; the improved output retains explicit role/ethics exposition and a negative parallelism; the numerical sentence recipe is not shown as a measured property of the Leonard samples; no evidence supports current-model generalisation, an authorship inference, a severity threshold, mandatory demographic prompting, or a universal dialogue formula.

## Matched patterns / rules

- H10 `genre_specific`, fiction branch in `human-eyes/scripts/judgement.json`: `dialogue voices not differentiated by rhythm, diction, or speech act`; `"as-you-know" exposition or role-explaining dialogue`; style imitation that misses a source's oddities
- H10 rendered catalogue description in `human-eyes/references/patterns.md`: flattened dialogue, weak voice differentiation, parenthetical stage directions, and generic target-style fidelity; the parenthetical wording is broader than the executable fiction watchlist
- G9 `sentence-length-variance`: the focused result dialogue flags at sentence-length standard deviation 2.5, while the catalogue expressly names dialogue as a legitimate uniformity control
- E5 `no-staccato-sequences`: focused result dialogue stays clear; its catalogue tolerance preserves dialogue and character voice
- B3 `no-negative-parallelisms`: focused result dialogue flags `I enter these chambers with pride, not fear`; the checker surfaces the construction without deciding that it is unjustified or artificial
- H3 `tonal_uniformity`: adjacent whole-text register review only; it is not equivalent to character-to-character voice differentiation and should not be cited as direct coverage
- `human-eyes/references/process.md`: preserve genre, deliberate devices, source facts, and character voice; do not infer authorship
- `dev/TESTING.md`: complete-Audit requirement, register variation, matched controls, and separation of deterministic from agent-assessed results
- H12 genre-aware threshold calibration and H25 model-family versus generic-AI residue
- `dev/references/sources/pattern-opportunities.md` row `Fiction dialogue and style-fidelity review`

## Associated hypotheses

- H12: Genre-aware threshold calibration
- H25: Model-family versus generic-AI residue
- Proposed evaluation question only: whether source-listed dialogue dimensions add useful treatment-in-context evidence beyond the current H10 rhythm/diction/speech-act watchlist without rewarding stereotypes or fixed sentence targets
