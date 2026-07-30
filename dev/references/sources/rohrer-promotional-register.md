# Fred Rohrer: promotional register and n-gram analysis

## Metadata

- **URL:** https://blog.frohrer.com/how-to-detect-llm-writing-in-text/
- **Author / owner:** Fred Rohrer
- **Published:** 2025-07-28T20:04:04.000Z
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** practitioner observation / technical essay
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** Ghost post ID `6a22e56c0a8fb3000174b6c1`; UUID `871b44d3-c117-4eee-a6da-6835e54ee822`
- **Version / revision:** Ghost `updated_at` `2025-07-28T20:13:35.000+00:00`; prior 2026-05-05 Jina capture archived by hash
- **Full-text status:** complete
- **Snapshot:** `snapshots/rohrer-promotional-register.md`
- **Extraction method:** direct HTML and first-party Ghost Content API JSON fetched with `curl`; API HTML/plaintext and RSS item cross-checked against the rendered page; complete first-party feature image preserved and visually transcribed
- **Snapshot SHA-256:** `a1bda3a7d040a5447957032ae52b3ce7a138bb2e51e4187b6032d4f9787d7e8c`
- **Model / corpus scope:** no model family, model version, corpus, language sample, text sample, comparison group, software, code, or validation set identified; the English-language blog post makes generic LLM and human-writing claims and shows one dashboard image for an unidentified input
- **Access limitations:** none for the substantive article or feature image. Page chrome was omitted. The source itself omits the image input, model, method, software, formulas, combination rule, validation data, sample sizes, dates, citations, uncertainty, and reproducible code.

## Summary

Rohrer supplies a 39-paragraph practitioner taxonomy of alleged LLM-writing cues and statistical approaches, plus an unlabeled feature-image dashboard. It covers promotional and editorial register, connectors and summaries, formatting, citation and chat residue, placeholders, platform artifacts, entropy, perplexity, Markov transitions, n-grams, lexical diversity, AUC, and repetition. It also says detection varies by model and is not foolproof. The article reports no study, sample, matched human comparison, model version, test set, code, citations, error rates, or validation, so it is useful for candidate discovery and manual provenance checks, not threshold selection, mechanism claims, a detector score, or document-level authorship inference.

## Main insights

- The opening warning is load-bearing: the article calls its methods non-foolproof and model-variable, but does not operationalize that uncertainty.
- The strongest source-to-project overlap is its exact promotional phrase set. DR-133 completes C03-C05 coverage across A1, A4, B1, B2, and E1.
- Remaining exact gaps include the three named connectors and the free-text `[URL of source]` placeholder; earlier decisions already resolved the other placeholder and platform-residue forms.
- `In summary` is recognized by G8 and `Overall, the ...` by E4, but the source's broader section-summary claim is not measured and has an explicit formal-academic countercontext.
- C5 recognizes curly punctuation, but the source provides no evidence for calling it a strong machine indicator; the live catalogue's typography and quotation exceptions are more cautious than the article.
- False references, invalid identifiers, malformed citation reuse, chat residue, unfilled placeholders, and platform tokens are provenance or factual-verification issues. Their presence can show workflow residue or an invalid reference, not who authored the surrounding prose.
- G9 and B5 implement sentence-length standard deviation and unigram type-token ratio only. They do not implement entropy, perplexity, Markov, n-gram, MTLD, hapax, AUC, Zipf-slope, phrase-repetition, or syntactic-pattern methods.
- The feature image's `56.3%` likelihood and component values cannot be interpreted or reproduced because the input, tool, formulas, scaling, and validation are absent.
- Every mechanism statement about training content, optimization objectives, homogenized data, and probabilistic word selection is author explanation without cited or measured support in this source.
- None of the article's comparative claims supplies a null result, uncertainty interval, human sample, model/date boundary, or validated threshold; those absences constrain all recommendations.

## Evidence and claims to extract

- **Direct source reviewed:** the canonical rendered article, Ghost post ID `6a22e56c0a8fb3000174b6c1` with `updated_at` `2025-07-28T20:13:35.000+00:00`, first-party API HTML and plaintext, complete RSS item, and the 2000 by 1605 first-party feature image.
- **Method and sample:** no empirical method or sample is disclosed. The article is a practitioner explanation in English, with 39 body paragraphs, two H2 sections, fifteen H3 subsections including the conclusion, and one image. No model/version, prompt, source-text input, human comparison, corpus dates, genre sample, text length, software, code, test set, or statistical evaluation is identified.
- **Direct versus cited evidence:** C01 is Rohrer’s direct caveat. C02 is a directly visible but unexplained image output. C03-C19 are Rohrer assertions, interpretations, examples, or proposed techniques. The article cites no external source and supplies no measured evidence for them. Reviewer statements about gaps, overreach, and live-project behavior are explicitly project comparison, not source findings.
- **Important limits and counterexamples:** the source itself says detection varies by model and is not foolproof; it concedes human use of connectors and formal-academic summaries. It supplies no human corpus, model/date boundary, negative result, uncertainty, threshold validation, error analysis, or counterexample set. Curly punctuation, Markdown, repetition, connectors, summaries, and lexical regularity all have legitimate human, genre, platform, or formatting explanations that the article does not test.

## Matched patterns / rules

- A1 `no-significance-inflation`, A4 `no-promotional-language`, B1 `no-ai-vocabulary-clustering`, and B2 `no-copula-avoidance` recognise the complete C03-C04 exact phrase family.
- E1 `no-filler-phrases` recognises both forms of `it is/it's important to note` and `no discussion would be complete without`; B1 recognises `defining feature` and `powerful tools` as clustering candidates.
- E4 `no-generic-conclusions` recognizes `Overall, the ...`; G8 `no-signposted-conclusions` recognizes `In summary` and conclusion headings with context gates for some formal genres.
- C1 `no-boldface-overuse` counts four or more Markdown bold spans in prose; it does not validate whether markup fits the target platform.
- C5 `no-curly-quotes` recognizes any curly quote/apostrophe, with catalogue tolerance for sourced excerpts, literary fixtures, publication text, and quotations.
- D1 `no-collaborative-artifacts` recognizes `I hope this helps` and `let me know if`; D2 `no-knowledge-cutoff-disclaimers` recognizes `as of my last training update`; the source's detailed-breakdown and AI-language-model examples are not recognized by those checks.
- H8 `no-placeholder-residue` covers constrained bracket, brace, and angle forms plus possessive labels like `[Subject's Name]` (added in d986dd5); the free-text `[URL of source]` fixture remains outside deterministic coverage.
- H10 `genre_specific` and `human-eyes/references/process.md` cover source grounding and the no-authorship product boundary; no deterministic DOI, ISBN, reference-reuse, platform-token, or tracking-parameter validator exists.
- H14 `no-anaphora` recognizes three consecutive nontrivial identical sentence openings; G9 `sentence-length-variance` measures sentence-word-count standard deviation on eligible prose; B5 `vocabulary-diversity` measures unigram type-token ratio on 150 or more words.
- H1, H3, H9, H12, H22, H24, and H25 are relevant to calibration, detector framing, look-alikes, register thresholds, structural metrics, vocabulary density, and model/version drift.

## Associated hypotheses

- H1 `Continuous calibrated register-distance score per pattern`: relevant to uncertainty, but this source supplies no distribution, register baseline, or reliability curve.
- H3 `Drop detection framing entirely`: supported only as practitioner caution; the source's unsupported certainty elsewhere makes it unsuitable as primary detector-limit evidence.
- H9 `Field-guide voice with similar-species disambiguation per pattern`: directly relevant to human connector use, academic summaries, publication typography, Markdown-native platforms, and deliberate repetition.
- H12 `Genre-aware threshold calibration`: relevant to promotional, academic, technical, conversational, and publication contexts; no threshold data are supplied.
- H22 `Long-tail compression and grammatical standardisation`: conceptually adjacent to C15, C16, and C19, but Rohrer supplies no measurement or validation.
- H24 `Register-specific vocabulary density` and H25 `Model-family versus generic-AI residue`: the opening caveat supports the need for register, model, version, and date boundaries, while the article itself omits all of them.

## Prior-to-current comparison

- **Added:** first-party Ghost identity and revision, complete feature-image preservation and transcription, exact prior/current digests, archive provenance, 19 claim IDs, direct-versus-interpretive boundaries, focused live-check results, recommendations, decisions, evaluation states, and independent-review fields.
- **Corrected:** the old `article/search excerpt` status is replaced by complete direct HTML/API/RSS/image acquisition. The statistical families are now separated from the two live coarse metrics, and the article's generic causal/comparative wording is identified as unsupported practitioner interpretation.
- **Removed:** no source text or earlier caution. Broad support claims for G9/B5 and `more concrete` platform checks are replaced by exact partial/not-covered mappings and evaluation prerequisites.
- **Unchanged:** canonical URL, Fred Rohrer authorship, publication date, article body, non-foolproof/model-variation warning, broad promotional examples, and the list of statistical feature families.
