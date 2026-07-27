# GPTZero: Perplexity, burstiness, and statistical AI detection

## Metadata

- **URL:** https://gptzero.me/news/perplexity-and-burstiness-what-is-it/
- **Author / owner:** Edward Tian / GPTZero
- **Published:** 2023-03-01T00:07:00.000-05:00
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** vendor explainer of a commercial AI detector
- **Evidence tier:** Vendor / detector pages
- **Review mode:** update
- **Stable identifier:** Ghost post 64aa3ff8ad12370001cbc4be; UUID c2c9760b-4ff6-4aa1-9eb6-50ab81ed609d
- **Version / revision:** updated 2025-10-13T21:09:00.000-04:00; prior capture retrieved 2026-05-05 without a recorded source revision
- **Full-text status:** complete
- **Snapshot:** `snapshots/gptzero-perplexity-burstiness.md`
- **Extraction method:** first-party Ghost Content API HTML field converted to Markdown; direct HTML and rendered-page text cross-checked
- **Snapshot SHA-256:** `de06735971639cb2f1b156b47a039164dc486d5126e5e32a6adc1eab2c0b7a40`
- **Model / corpus scope:** GPTZero's first public detector and a later upgraded model as described by the vendor; the page names no detector model version, language-model version, training or evaluation corpus, corpus dates, language, genre, comparison sample, feature formula, calibration set, or independent benchmark; it discusses documents of hundreds of words
- **Access limitations:** none for the complete substantive article text; the non-substantive television screenshot was not copied, but its URL and caption are preserved

## Summary

Edward Tian's ten-paragraph GPTZero explainer describes perplexity and burstiness as the statistical layer of the company's original detector and as one indicator family in a later multi-signal system. It defines burstiness broadly as document-level variation in writing patterns and sentence perplexities, then asserts that humans vary sentence construction and diction more than language models. The page is direct evidence of GPTZero's product framing and examples, not independent validation of the mechanism, the `above 85` perplexity threshold, detector effectiveness, cross-vendor adoption, or human-versus-model differences. It supplies no corpus, feature formula, model version, rates, ablation, calibration, uncertainty, subgroup analysis, or measured human comparison.

## Main insights

- GPTZero frames perplexity and burstiness as a statistical detector layer and says upgraded GPTZero also uses text search and deep-learning approaches.
- The page defines per-sentence perplexity through next-word predictability and uses `assistant` versus `potato` as an illustrative low/high-perplexity contrast.
- It states that perplexity has no absolute scale, then gives an unvalidated vendor rule of thumb that values above 85 are more likely than not human.
- It defines burstiness across the whole document, not as sentence-length variance or type-token ratio alone.
- The page includes an important human look-alike qualification: a person can write an AI-like sentence by accident.
- Its human-memory mechanism, model-consistency account, effectiveness claims, cross-detector adoption claim, and improved-performance-with-more-input claim are assertions without supporting methods or results on the page.
- The current source body is substantively unchanged from the archived 2026-05-05 capture; the refresh replaces a chrome-heavy reader capture with complete first-party article text and contract provenance.

## Evidence and claims to extract

- **Direct source reviewed:** First-party GPTZero Ghost post `64aa3ff8ad12370001cbc4be`, UUID `c2c9760b-4ff6-4aa1-9eb6-50ab81ed609d`, updated `2025-10-13T21:09:00.000-04:00`; all ten body paragraphs, the one figure caption, and all four body links were checked at the beginning, middle, and end against direct HTML and the rendered page.
- **Method and sample:** Vendor narrative and constructed next-word example; no empirical method, sample, comparison group, exact model, language, genre, corpus dates, feature computation, evaluation protocol, uncertainty, or results table. The page says probabilities compound over hundreds of words but does not define a minimum length.
- **Direct versus cited evidence:** C01-C11 are statements made directly by the GPTZero page, but C01, C03, C07, C09, C10, and C11 are unsupported vendor assertions rather than measurements reported there. The linked GPTZero technology and deep-learning pages and Chiara Campagnola technical explainer were not ingested; no claim from them is upgraded to direct evidence here.
- **Important limits and counterexamples:** No null results are reported. The page says there is no absolute perplexity scale and that a human can accidentally write an AI-like sentence. It supplies no human baseline, false-positive analysis, false-negative analysis, calibration, feature ablation, model/version drift, genre or language boundary, adversarial test, independent validation, or evidence that its proprietary burstiness construct equals human-eyes' sentence-length or vocabulary metrics.

## Skill-use audit

- **Good use:** Product-history and uncertainty-framing context; a candidate prompt to examine document-level structural and diction variation; support for explicitly warning that one sentence is insufficient.
- **Misuse / overclaim:** Treating `above 85`, low burstiness, low sentence-length variance, or low type-token ratio as authorship proof; importing GPTZero's product threshold or feature name into human-eyes severity.
- **Unsupported use:** Claiming that GPTZero's mechanism is unique, more effective with longer input, used by named competitors, caused by human short-term memory, or independently validated; claiming that G9 or B5 implements GPTZero burstiness.
- **Underused evidence:** The source's clearest useful boundary is broader than the existing mapping: burstiness covers variation in writing patterns and perplexities across a document, while G9 measures only sentence-word-count standard deviation and B5 only lowercased type-token ratio.
- **Patterns left on the table:** None ready for promotion. H22 can retain GPTZero as a weak vendor prior only if matched-register evaluation determines whether richer structural tails add value beyond G9.

## Matched patterns / rules

- G9 `sentence-length-variance`: partly covered conceptual adjacency only. `human-eyes/scripts/grade.py::check_sentence_variance` computes sentence-word-count standard deviation and passes above 4; it does not measure perplexity, syntax, diction, or GPTZero's proprietary burstiness. Its live eligibility logic skips only when both fewer than six sentences and fewer than 100 whitespace-split words are present; six sentences under 100 words are evaluated, while fewer than three measurable sentences can hard-fail. That conflicts with the catalogue wording that the check skips prose under 100 words and six sentences.
- B5 `vocabulary-diversity`: partly covered conceptual adjacency only. `human-eyes/scripts/grade.py::check_type_token_ratio` flags lowercased type-token ratio at or below 0.40 for 150+ words; it does not measure GPTZero burstiness and the page provides no TTR direction or threshold.
- H22 `Long-tail compression and grammatical standardisation`: an appropriate pending research home, with GPTZero contributing vendor framing rather than empirical support.
- H3 `Drop detection framing entirely`: relevant to keeping the commercial detector threshold and authorship language out of human-eyes.
- Focused surface-only run on the snapshot's `Full text` Markdown after removing the figure line, caption, and bold subheading while retaining link markup: `sentence-length-variance` passed with SD 8.8 against target greater than 4; `vocabulary-diversity` passed with TTR 0.483, 268 unique of 555 stripped tokens, against target greater than 0.40. This is deterministic coverage evidence only, not a complete Audit and not validation of the source's claims.

## Associated hypotheses

- H3 `Drop detection framing entirely`
- H22 `Long-tail compression and grammatical standardisation`

## Questions / follow-up

- User decision needed on whether to revise the existing `pattern-opportunities.md` mapping from “confirmed” B5 support to conceptual adjacency across G9, B5, and H22.
- A separate product decision is needed to reconcile G9's live eligibility logic with its catalogue wording and add boundary tests; this source does not decide which behaviour is correct.
- Any future threshold, mechanism, or performance use requires a separately reviewed empirical source with disclosed methods and matched human controls.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | no source revision recorded; archived content hash 8ae9f902 | `snapshots/archive/gptzero-perplexity-burstiness/2026-05-05-8ae9f902.md` | 2026-05-05 | `8ae9f902b3eb1825f56d977f1f85589198c588aab737a950ac8530bf6f308dae` |
| current | Ghost post 64aa3ff8ad12370001cbc4be; UUID c2c9760b-4ff6-4aa1-9eb6-50ab81ed609d | `snapshots/gptzero-perplexity-burstiness.md` | 2026-07-15 | `de06735971639cb2f1b156b47a039164dc486d5126e5e32a6adc1eab2c0b7a40` |

## Decision history

- The prior legacy card contained no claim IDs, user decisions, or implementation statuses. Its broad conceptual G9/B5 and H3/H4 mappings are reopened. H4 is retired from this card because source-registry architecture is a project concern not supported by the article. All current claim rows begin at `pending` / `not started`; no product change is treated as approved or implemented.

## Project coverage

This is the authoritative review table. The source is a vendor explainer, so direct statements about GPTZero remain vendor assertions unless the page reports methods and results.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: GPTZero publicly released its first detector in January and reports seven million views, half a million first-week users, international coverage, and a New York Times front-page feature. | Direct vendor historical and reach assertions; no analytics, dates beyond “January,” links, or independent verification are supplied in the article. | not covered; no project pattern or hypothesis needs these popularity claims. | Reach is not prose evidence and cannot support validity, prevalence, or severity. | Record only as dated vendor context; make no product or index change beyond this claim record. | pending | not started |
| C02: The original GPTZero model used a statistical approach that converted words to numbers for calculation. | Direct high-level vendor architecture description; no formula, code, model version, training data, or evaluation is disclosed. | not covered; H3 concerns avoiding detector framing, not implementing detector internals. | The description is too coarse to reproduce or evaluate. | Record as product-history context and do not implement a statistical detector layer. | pending | not started |
| C03: Numerical methods are efficient and least computationally expensive, power dozens of other detector apps while naming four, remain effective, and are one of seven indicators alongside text search and deep learning. | Direct vendor assertions; the named cross-vendor adoption, computational ranking, effectiveness, and seven-indicator architecture are unsupported on this page. Linked product pages are indirect and not ingested here. | not covered; human-eyes has no commercial-detector architecture or efficiency comparison. | No cost measure, competitor implementation evidence, indicator definitions, ablation, benchmark, or version boundary. | Take no further action unless each adoption, cost, or performance claim is directly reviewed from suitable evidence. | pending | not started |
| C04: Perplexity and burstiness form the statistical layer and first layer of GPTZero's detector. | Direct vendor product description at the reviewed revision; no implementation detail or validation. | not covered; G9 and B5 are transparent prose metrics, not GPTZero layers. | The proprietary layer cannot be reproduced from the article. | Keep as product-framing context; do not relabel G9 or B5 as the GPTZero statistical layer. | pending | not started |
| C05: Per-sentence perplexity represents how likely a similar AI model would choose the same words, and GPTZero uses an unspecified model similar to ChatGPT to measure it. | Direct simplified vendor interpretation; exact probability definition, tokenizer, model, aggregation, and version are absent. | not covered; human-eyes computes no language-model perplexity. | “Similar to ChatGPT” is not a model identity or reproducible method. | Record only; do not add perplexity scoring without a separately specified and evaluated proposal. | pending | not started |
| C06: In the constructed prompt `Hi there, I am an AI _`, `assistant` illustrates low perplexity and `potato` high perplexity plus greater human likelihood. | Direct constructed example, not an observed human/model comparison; it illustrates predictability but supplies no score, repeated trial, or base rate. | not covered; no current check scores next-token probability. | A single invented continuation cannot establish authorship or a detector threshold. | Retain as an attributed illustration only; do not turn either word or surprise alone into a pattern. | pending | not started |
| C07: Probabilities compound over hundreds of words; perplexity has no absolute scale; nevertheless, values above 85 are generally more likely than not human. | Direct vendor threshold assertion with an internal qualification; no corpus, model, length protocol, calibration curve, confusion matrix, uncertainty, or subgroup analysis. The linked external explainer is not direct support for this product threshold. | challenges current behaviour only at the framing boundary: H3 and the detector-score non-promotion row in `pattern-opportunities.md` already reject commercial scores as human-eyes thresholds. | The article cannot substantiate the value 85 or any individual-document authorship conclusion. | Preserve the no-absolute-scale qualification and continue to exclude the threshold, probability, and origin verdict from human-eyes. | pending | not started |
| C08: Burstiness measures how writing patterns and text perplexities vary over an entire document. | Direct vendor definition; broad and proprietary, with no formula or empirical validation. | partly covered: G9 measures only sentence-word-count SD; B5 measures only type-token ratio; H22 proposes richer structural-variation tests. | Current checks omit perplexity, syntax, clause shape, construction diversity, joint variation, and any GPTZero-specific aggregation. G9's live skip and hard-fail boundaries also conflict with its catalogue wording. | Replace the current “confirmed B5” mapping with conceptual adjacency across G9, B5, and H22; require matched-register evaluation plus an G9 eligibility-boundary test and documentation reconciliation before any implementation. | pending | not started |
| C09: Humans tend to vary sentence construction and diction, language models maintain a consistent AI-like level, and a person can accidentally write an AI-like sentence. | Direct vendor generalization plus an explicit human look-alike qualification; no human or model sample, genres, languages, model versions, rates, or statistical comparison. | partly covered: G9 and B5 operationalize narrow variation metrics with genre cautions; H22 proposes richer tests. A focused surface-only run of this article passed both checks, which does not test the human/model claim. | The source does not validate either live direction or threshold and does not show that variation separates origins within register. G9's implemented eligibility boundary is not the one described in its catalogue. | Retain only as weak candidate framing and as a warning against sentence-level origin inference; evaluate with matched human/model controls and reconcile G9 eligibility and documentation before relying on it. | pending | not started |
| C10: Human short-term memory dissuades repeated writing and thereby contributes to burstiness. | Direct author interpretation introduced as philosophical explanation; no experiment, citation, mechanism test, or boundary. | not covered; no project hypothesis depends on this memory mechanism. | Causal mechanism is unsupported and may conflate repetition, lexical choice, syntax, and perplexity. | Take no further action and do not repeat the mechanism as established fact. | pending | not started |
| C11: Formulaic next-word choice causes low model burstiness; burstiness is a key factor unique to GPTZero, evaluates long-term context, and performs better with more input. | Direct vendor causal, uniqueness, capability, and performance assertions; no comparator definition, ablation, metric, length curve, benchmark, uncertainty, or external validation. | not covered; H22 is a research question, not confirmation; no live check claims uniqueness or detector performance. | The article cannot establish causality, uniqueness, or improved performance with length. | Take no further action unless a directly reviewed technical evaluation supplies the missing ablation, length analysis, and matched controls. | pending | not started |

## Recommendations

- C01: Record only as dated vendor context; no product change.
- C02: Record only as high-level product history; do not implement a detector layer.
- C03: Require direct cost, adoption, architecture, and performance evidence before reuse; otherwise take no further action.
- C04: Keep as product framing and do not relabel G9 or B5 as GPTZero layers.
- C05: Do not add perplexity scoring from this underspecified description.
- C06: Retain the constructed continuation only as an attributed illustration, not a pattern or authorship rule.
- C07: Preserve the qualification and continue excluding the `above 85` threshold and origin verdict.
- C08: Revise `pattern-opportunities.md` from confirmed B5 support to conceptual adjacency across G9, B5, and H22; require matched-register evaluation and G9 eligibility-boundary reconciliation.
- C09: Retain only as weak candidate framing and a human-look-alike warning; require matched controls and G9 eligibility/documentation reconciliation before reliance.
- C10: Take no further action on the unsupported short-term-memory mechanism.
- C11: Take no further action on causality, uniqueness, long-context, or performance claims without a technical evaluation.

## Evaluation of approved changes

- C01: not applicable - pending record-only decision; no product change made.
- C02: not applicable - pending record-only decision; no product change made.
- C03: not applicable - pending no-action decision; no product change made.
- C04: not applicable - pending framing decision; no product change made.
- C05: not applicable - pending no-action decision; no product change made.
- C06: not applicable - pending illustration-use decision; no product change made.
- C07: not applicable - pending non-promotion decision; no product change made.
- C08: not applicable - pending index-wording decision; shared index not edited.
- C09: not applicable - pending evaluation decision; no product change made.
- C10: not applicable - pending no-action decision; no product change made.
- C11: not applicable - pending no-action decision; no product change made.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/gptzero_review_2` (fresh source-dedicated final reviewer; initial reviewer `/root/gptzero_review_1` was not reused)
- **Findings resolved:** Initial reviewer `/root/gptzero_review_1` identified five findings. The candidate manifest row is supplied for serial application; G9's live eligibility discrepancy was added to coverage and recommendations; the focused-check selection and TTR result were corrected; C03 now distinguishes “dozens” from the four named apps; and C11 now preserves the source's “key factor unique to GPTZero” wording.
- **Unresolved findings:** none
