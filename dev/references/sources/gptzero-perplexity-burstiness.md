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

## Matched patterns / rules

- G9 `sentence-length-variance`: partly covered conceptual adjacency only. `human-eyes/scripts/grade.py::check_sentence_variance` computes sentence-word-count standard deviation and passes above 4; it does not measure perplexity, syntax, diction, or GPTZero's proprietary burstiness. Its live eligibility logic skips only when both fewer than six sentences and fewer than 100 whitespace-split words are present; six sentences under 100 words are evaluated, while fewer than three measurable sentences can hard-fail. That conflicts with the catalogue wording that the check skips prose under 100 words and six sentences.
- B5 `vocabulary-diversity`: partly covered conceptual adjacency only. `human-eyes/scripts/grade.py::check_type_token_ratio` flags lowercased type-token ratio at or below 0.40 for 150+ words; it does not measure GPTZero burstiness and the page provides no TTR direction or threshold.
- H22 `Long-tail compression and grammatical standardisation`: an appropriate pending research home, with GPTZero contributing vendor framing rather than empirical support.
- H3 `Drop detection framing entirely`: relevant to keeping the commercial detector threshold and authorship language out of human-eyes.
- Focused surface-only run on the snapshot's `Full text` Markdown after removing the figure line, caption, and bold subheading while retaining link markup: `sentence-length-variance` passed with SD 8.8 against target greater than 4; `vocabulary-diversity` passed with TTR 0.483, 268 unique of 555 stripped tokens, against target greater than 0.40. This is deterministic coverage evidence only, not a complete Audit and not validation of the source's claims.

## Associated hypotheses

- H3 `Drop detection framing entirely`
- H22 `Long-tail compression and grammatical standardisation`
