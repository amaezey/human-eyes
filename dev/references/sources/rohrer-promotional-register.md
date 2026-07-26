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

## Skill-use audit

- **Good use:** candidate discovery for promotional phrasing; test fixtures for assistant, cutoff, placeholder, citation, and platform residue; a checklist of statistical feature families; a direct reminder to keep model variation and non-foolproof limits attached.
- **Misuse / overclaim:** treating any phrase, punctuation mark, metric, feature-image score, or combination as validated evidence of LLM authorship; repeating the article's mechanisms, comparative directions, or `particularly effective` language as empirical findings.
- **Unsupported use:** severity, thresholds, current model behavior, prevalence, causality, representative human differences, detector accuracy, probability calibration, genre transfer, language transfer, or a claim that an identifier's checksum alone proves validity or invalidity.
- **Underused evidence:** exact platform residue and citation-validity examples are more concrete review targets than the article's broad detector framing, while the live placeholder checker misses both exact bracketed examples.
- **Patterns left on the table:** named connectors, the free-text placeholder, citation-validity workflow, and richer structural/lexical metrics.

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

## Questions / follow-up

- What input, software, formulas, scaling, training data, and validation produced the feature image's `56.3%` value and component scores?
- Are the statistical directions and `particularly effective` statements based on Rohrer data, code, another source, or an illustrative hypothesis?
- Should exact platform tokens, tracking parameters, placeholder variants, and identifier checks be evaluated as provenance/factual-integrity tooling rather than prose-pattern checks?
- Can matched, length-controlled human and model corpora test any of the entropy, transition, n-gram, MTLD, hapax, AUC, or repetition proposals within register?

## Update provenance

The prior card and manifest recorded no snapshot digest. Before replacement, the exact prior 10,490-byte snapshot was hashed as `26c07ee01be373c80626ecb4be8dcec6a2d8444176da675f9aace4c92d049e18`, verified byte-for-byte against both the committed `c42b145` version and the bytes on disk, and archived without transformation. The current source has the same article title, canonical URL, publication timestamp, headings, paragraphs, and final sentence; the update adds first-party revision metadata, the omitted feature image, complete provenance, explicit evidence boundaries, and contract sections.

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none found; pre-contract Jina capture | `snapshots/archive/rohrer-promotional-register/2026-05-05-26c07ee01be.md` | 2026-05-05 | `26c07ee01be373c80626ecb4be8dcec6a2d8444176da675f9aace4c92d049e18` |
| current | Ghost post ID `6a22e56c0a8fb3000174b6c1`; UUID `871b44d3-c117-4eee-a6da-6835e54ee822` | `snapshots/rohrer-promotional-register.md` | 2026-07-17 | `a1bda3a7d040a5447957032ae52b3ce7a138bb2e51e4187b6032d4f9787d7e8c` |

## Decision history

- The prior card had no claim IDs, user-decision states, implementation statuses, or recorded approvals. It broadly mapped the essay to A4, E1, C7, G9, and B5, called platform artifacts underused, and asked which should become deterministic checks. This update reopens every mapping as C01-C19 because the complete source and live implementation review expose evidence gaps, missed exact examples, legitimate contexts, and a previously omitted unvalidated numeric image. No prior recommendation is treated as approved or implemented.
- C11 approved 2026-07-17 via DR-113: commit 340ea99 added `here's a detailed breakdown` and AI-identity disclaimer patterns to D1 `no-collaborative-artifacts`, covering both forms the focused run missed; the surrounding-text authorship boundary is unchanged.
- C12 and C13 approved 2026-07-17 via DR-114 components 1-2: commit d986dd5 added `citeturn` tokens, `contentReference[oaicite:...]` tokens, `utm_source=chatgpt.com` trackers, and possessive bracket labels such as `[Subject's Name]` to H8 `no-placeholder-residue`. DR-114 components 3 (quoted-example over-fire fix) and 4 (private-person gap-filling filler phrases) were declined, so H8 remains quote-unaware; C12's “unambiguous evidence” authorship claim stays non-promoted.
- C10 rejected 2026-07-18 via DR-122: DOI syntax and resolution, ISBN validity, reference existence, and repeated-citation syntax were all declined. No citation-integrity checker or external resolver was added.
- C03-C05 approved 2026-07-19 via DR-133: A1 now recognises `underscores its importance` and `enduring legacy`; A4 recognises `rich cultural heritage`; E1 recognises contracted `it's important to note` and `no discussion would be complete without`; and `defining feature` plus `powerful tools` are B1 clustering candidates. Existing A1/B2 coverage already handled `stands as a testament`, `plays a vital role`, and `breathtaking landscapes`.
- C06 approved 2026-07-19 via DR-134 option B: `moreover`, `furthermore`, and `on the other hand` joined E8 as exact paragraph openers. Mae rejected connector-density logic.

## Prior-to-current comparison

- **Added:** first-party Ghost identity and revision, complete feature-image preservation and transcription, exact prior/current digests, archive provenance, 19 claim IDs, direct-versus-interpretive boundaries, focused live-check results, recommendations, decisions, evaluation states, and independent-review fields.
- **Corrected:** the old `article/search excerpt` status is replaced by complete direct HTML/API/RSS/image acquisition. The statistical families are now separated from the two live coarse metrics, and the article's generic causal/comparative wording is identified as unsupported practitioner interpretation.
- **Removed:** no source text or earlier caution. Broad support claims for G9/B5 and `more concrete` platform checks are replaced by exact partial/not-covered mappings and evaluation prerequisites.
- **Unchanged:** canonical URL, Fred Rohrer authorship, publication date, article body, non-foolproof/model-variation warning, broad promotional examples, and the list of statistical feature families.

## Project coverage

This is the authoritative review table. Focused results use the live `human-eyes/scripts/grade.py` implementations on 2026-07-17 and are surface-only coverage checks, not complete Audits.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Detection is becoming harder, varies by model, and the article's methods are not foolproof. | Direct author caveat, but no model/version, date, corpus, metric, error rate, or validation supports the broader detection framing. | fully covered by `human-eyes/references/process.md` no-authorship boundary and H3/H12/H25; no runtime detector applies. | Shared summaries must not turn the rest of the essay into calibrated or current detection evidence. | **adopt:** retain the non-foolproof, model-variable, no-authorship boundary wherever this source is summarized; documentation verification only. | pending | not started |
| C02: The feature image reports `AI Likelihood: 56.3%`, component values, and `MODERATE signs of AI generation`. | Direct visible output for an unidentified input. No tool, model, formulas, scale, combination rule, sample, date, validation, uncertainty, or error rate is disclosed. | not covered; human-eyes deliberately reports pattern findings rather than an AI-likelihood probability. | The image was omitted before this refresh and cannot support any score, threshold, or product comparison. | **do not adopt:** preserve the image as provenance, explicitly non-promote its score, and seek reproducible method details before any further use. | pending | not started |
| C03: Rohrer says the discussed linguistic patterns emerge from how models construct responses and often reflect training methodologies and optimization objectives; he says LLMs overemphasize significance with `stands as a testament`, `plays a vital role`, and `underscores its importance`, attributing this instance to promotional training content. | Broad author mechanism interpretation plus three examples; no model architecture, training or optimization evidence, sample, counts, model/date scope, human comparison, or citation. | fully covered for the exact phrases: A1 recognises all three and B2 additionally recognises `stands as`; DR-133 added the previously missed `underscores its importance` frame. | Candidate coverage is distributed across the matching surface mechanisms. | **adopt:** retain all three exact phrases as programmatic A1/B2 candidates. | approved | implemented |
| C04: Promotional language is especially common for culture, locations, and history; examples are `rich cultural heritage`, `breathtaking landscapes`, and `enduring legacy`; humans allegedly vary more and avoid superlatives. | Author register comparison with three examples and an explicit human generalization; no corpus, frequency, coding, genre control, or model/date boundary. | fully covered for the exact phrases: A4 recognises `rich cultural heritage` and `breathtaking landscapes`; A1 recognises `enduring legacy`. | The phrase family spans promotional and significance mechanisms rather than one checker. | **adopt:** route the exact phrases through A4 and A1. | approved | implemented |
| C05: LLMs inject editorial voice through `it's important to note`, `no discussion would be complete without`, `defining feature`, and `powerful tools`; Rohrer attributes this to mixed training sources and says humans separate fact from interpretation more clearly. | Author observation, mechanism, and human comparison with no measured examples, attribution study, coding, or counterexamples. | fully covered for the exact phrases: E1 recognises both editorial frames, including straight and smart apostrophes; `defining feature` and `powerful tools` contribute to B1 clustering. | The exact phrases require two existing mechanisms because the adjective-noun forms are vocabulary candidates rather than filler frames. | **adopt:** route the editorial frames through E1 and the adjective-noun phrases through B1 clustering. | approved | implemented |
| C06: `moreover`, `furthermore`, and `on the other hand` become cues when used with mechanical regularity, although humans also use them. | Author frequency/regularity claim with a human counterexample; no count, density, span, sample, model/date, or threshold. | Covered for the three exact paragraph-opening forms by E8. | No density or distribution mechanism exists; Mae rejected adding one in DR-134. | Keep the exact E8 openers; add no connector-density mechanism. | approved | implemented |
| C07: LLM sections often end with `In summary` or `Overall`; Rohrer says this structure is rare outside formal academic prose. | Author observation with an explicit genre qualification; no frequency, sample, coding, model/date, or human baseline. | partly covered: focused `In summary` and `## Conclusion` fixtures trigger G8; `Overall, the ...` triggers E4 but not G8. G8 has formal-report/technical/recipe context gates; H12 is adjacent. | Section position is not evaluated by E4, and neither check validates the source's frequency or `rare` claim. | **test-adapt:** retain candidate recognition and academic/formal controls; evaluate section-end location and genre before any threshold or severity change. | pending | review required |
| C08: Rohrer calls technical indicators “some of the most reliable detection signals” and names Markdown emphasis rather than target-platform HTML or wiki markup. | Strong author platform-fit and detection claim; no platform sample, rate, model/version, task instruction, validation, or human comparison. Markdown is correct on many platforms. | partly covered: C1 finds four Markdown bold spans in prose but passes one; C2 checks bold inline list headers. Neither determines the requested target markup. | The source does not support its reliability claim. Formatting mismatch depends on the destination and instruction, not Markdown syntax alone. | **test-adapt:** treat target-markup mismatch as a workflow validation question; do not make Markdown itself an AI-writing cue or repeat the reliability claim. | pending | not started |
| C09: Curly quotes and apostrophes are frequent in AI text and a strong indicator because human typists allegedly default to straight punctuation. | Author comparison with no platform, editor, locale, publication, device, corpus, or model controls. | challenges current behavior in C5: the exact fixture fails on any curly character, but the catalogue says typography is not inherently AI writing and preserves sourced, literary, publication, and quoted uses. | The source cannot justify `strong indicator`; smart punctuation is common human publishing and device behavior. | **do not adopt:** do not use Rohrer to strengthen C5 or infer authorship; retain only context-aware typography normalization. | pending | review required |
| C10: Rohrer calls citation problems clear detection signals, says LLMs frequently generate plausible nonexistent references and invalid DOI/ISBN identifiers appear regularly, and says malformed citation-reuse syntax is characteristic. | Strong author provenance, frequency, and detection claims; no examples, rates, model/date scope, identifier validation method, or cited study. DOI resolution and ISBN checksums test different properties. | partly covered by H10 source-grounding and process guidance; focused fake DOI/ISBN text triggers no deterministic citation check. | No direct reference-existence, DOI resolution, ISBN validity, or repeated-citation syntax tool exists. The source supplies no basis for `frequently`, `regularly`, or `clear detection signals`, and invalidity does not prove authorship. | **test-adapt:** evaluate reference and identifier validation as factual-integrity tooling with format, resolution, and claim-support controls; keep it separate from prose attribution and do not adopt the frequency/detection wording. | rejected | not applicable |
| C11: Chatbot residue includes `I hope this helps`, `let me know if you need more information`, `here's a detailed breakdown`, training-cutoff language, refusals, and `an AI language model`. | Author artifact taxonomy with exact examples but no prevalence or false-positive study; these are workflow-residue candidates, not surrounding-text authorship proof. | partly covered: focused text triggers D1 on the first two phrases and D2 on `as of my last training update`; it misses `here's a detailed breakdown` and `I am an AI language model`. `context_leakage` is adjacent. | Coverage does not include every source form, and legitimate quoted/discussed uses require context. | **test-adapt:** evaluate the two missed forms with quoted, instructional, and analytical controls before extending existing residue checks. | approved | implemented |
| C12: Unfilled `[Subject's Name]` and `[URL of source]` placeholders are incomplete template residue; Rohrer calls them “unambiguous evidence of AI generation.” | Direct examples plus a categorical authorship interpretation. No model-specific evidence is needed to identify an unfilled placeholder, but no study, provenance check, or false-positive control supports the categorical origin claim. | challenges current H8 coverage: the exact two-example focused fixture passes; H8 catches constrained forms such as `[insert date]` and `{client_name}`. | Apostrophe-bearing subject labels and free-form URL labels fall outside the current regex; documentation, quotations, human-authored templates, and other generators are look-alikes, so residue cannot establish authorship. | **test-adapt:** add exact fixtures only after testing quoted documentation, templates, code, and literal instructional controls; **do not adopt** the “unambiguous” authorship claim. | approved | implemented |
| C13: Broken ChatGPT citation tokens such as `citeturn0search0` and `contentReference[oaicite:0]`, plus `utm_source=chatgpt.com`, are platform fingerprints that will change over time. | Author platform observation with three exact forms and a correct drift qualification; no incident counts, generation route, date sample, or false-positive analysis. | not covered: the exact focused fixture passes D1, D2, H8, and the broader registry. H25 and process provenance review are relevant. | No platform-residue registry or tracking-parameter check exists; ordinary discussion/quotation and manually copied URLs are look-alikes. | **test-adapt:** evaluate a dated provenance-residue check with exact-token, URL-parsing, quoted-text, code, and documentation controls; record platform/version metadata. | approved | implemented |
| C14: Human writing has higher entropy and LLM writing lower entropy/perplexity because models favor probable common combinations. | Author comparative and causal interpretation with a textbook-style perplexity explanation; no language model used for scoring, sample, normalization, length control, matched corpus, or validation. | not covered directly. G9 and B5 are coarse sentence-length and unigram-diversity metrics; H1/H12/H22 are adjacent. | Perplexity is relative to a scoring model and can vary by language, domain, fluency, and writer background; the source supplies no usable direction or threshold. | **do not adopt:** do not infer authorship or add an entropy/perplexity rule from this essay; require directly reviewed, matched, bias-aware evaluation. | pending | not started |
| C15: Human word-pair/triplet transitions vary more, LLM transitions are more uniform, and second-order Markov analysis is particularly effective. | Author method proposal, comparison, and effectiveness claim with no transition definition, smoothing, sample, code, metric, result, baseline, or citation. The source contradicts itself: prose says high transition uniformity suggests AI and irregularity suggests human authorship, while the image reports `Uniformity 0.000`, `Predictability 1.000`, a maximal Markov value on a “Higher = More AI-like” radar, and says low uniformity indicates predictable transitions. | not covered; H14 recognizes repeated starts and G9 sentence-length variance, neither measures word-transition matrices. H22 is conceptually adjacent. | `particularly effective` is unsupported, and the direct prose/image direction conflict prevents a stable interpretation of the proposed feature. | **do not adopt:** record as an internally contradictory, unvalidated research candidate only; require source clarification, reproducible code, and matched evaluation before project mapping. | pending | not started |
| C16: Human text follows Zipf's law more closely and has higher n-gram TTR; LLM text has lower n-gram TTR; trigram variance is useful. | Author statistical-direction claims with no sample, tokenizer, n range, length control, fitted model, metric, result, or citation. | partly covered only by B5's unigram TTR on 150-plus-word text; no n-gram TTR, Zipf fit, or trigram-variance implementation exists. | Unigram TTR is length-sensitive and not evidence that the source's n-gram directions hold; the image's trigram values lack an input and method. | **test-adapt:** keep B5 separate, and evaluate n-gram/Zipf candidates only with matched length, register, language, tokenizer, and held-out controls. | pending | review required |
| C17: Humans maintain higher MTLD and more hapax legomena, while AI text loses lexical diversity and repeats vocabulary. | Author comparative claims plus a threshold description of MTLD; no sample, length control, tokenization, model/date, human baseline, result, or citation. | partly covered by B5 unigram TTR only; no MTLD or hapax implementation. H12/H24 are relevant to length, register, and dated vocabulary. | The article's generic direction may invert by task or register, and its `typically 0.72` parameter is not validated here. | **test-adapt:** compare MTLD, hapax ratio, and live TTR under matched length/register/model conditions before choosing any implementation. | pending | review required |
| C18: Human word-frequency curves follow Zipf slopes near -1, while AI curves differ; AUC deviations can indicate generation. | Author method proposal and comparative direction with no curve definition, fitting range, AUC definition, tolerance, data, code, validation, or citation. | not covered; no live AUC or Zipf-slope check exists. H1 is only conceptually adjacent. | `AUC` is underspecified and no expected distribution or false-positive control is given. | **do not adopt:** preserve as a follow-up question, not source-backed project evidence, until a primary empirical source and reproducible method are reviewed. | pending | not started |
| C19: AI repeats phrases, sentence openings, vocabulary cycles, and syntactic shapes more than humans; repetition scores should be normalized by length. | Author feature-family comparison with no algorithm, sample, model/date, human baseline, result, or threshold. | partly covered: H14 flags three consecutive identical nontrivial sentence openings; G9 measures sentence-length variation; `structural_monotony` and `semantic_redundancy` are manual. No phrase-repetition, vocabulary-cycle, or syntactic-pattern score exists. | A repeated-start fixture proves only narrow candidate coverage; deliberate rhetoric, terminology, dialogue, and genre create human look-alikes. | **test-adapt:** evaluate separate repetition families with quotation, deliberate anaphora, technical-term, dialogue, and length controls before adding or broadening checks. | pending | review required |

## Recommendations

- C01: **adopt** the source's non-foolproof/model-variable boundary in all summaries; make no checker change.
- C02: **do not adopt** the unexplained `56.3%` image score; preserve it only as source provenance.
- C03: **adopt** the three exact significance phrases under existing A1/B2 coverage.
- C04: **adopt** `rich cultural heritage`, `breathtaking landscapes`, and `enduring legacy` under A4/A1.
- C05: **adopt** the two editorial frames under E1 and the two adjective-noun phrases as B1 clustering candidates.
- C06: Keep the three exact paragraph openers in E8; add no connector-density or distribution measure.
- C07: **test-adapt** conclusion forms with section-position and formal-genre controls.
- C08: **test-adapt** target-platform mismatch as workflow validation; do not treat Markdown itself as a cue.
- C09: **do not adopt** the claim that curly punctuation is a strong machine indicator.
- C10: **test-adapt** citation and identifier validity as factual-integrity tooling, separate from authorship.
- C11: **test-adapt** the two missed chatbot-residue forms with quotation and discussion controls.
- C12: **test-adapt** the exact missed placeholders with template, documentation, quotation, and code controls.
- C13: **test-adapt** dated platform tokens and tracking parameters as provenance residue with URL and quotation controls.
- C14: **do not adopt** entropy/perplexity directions or thresholds without direct matched empirical evidence.
- C15: **do not adopt** the Markov effectiveness claim without a reproducible method and evaluation.
- C16: **test-adapt** n-gram and Zipf features separately from live unigram TTR under matched conditions.
- C17: **test-adapt** MTLD and hapax against live TTR with length, register, language, and model controls.
- C18: **do not adopt** the underspecified AUC/Zipf proposal until a primary source and method are reviewed.
- C19: **test-adapt** each repetition family separately with deliberate-use and genre controls.

## Evaluation of approved changes

- C01: not applicable - pending documentation recommendation; no product change implemented.
- C02: not applicable - pending explicit non-promotion; no product change implemented.
- C03: passed - DR-133A assertions confirm A1 recognises `underscores its importance`; existing A1/B2 coverage handles the other two exact phrases.
- C04: passed - DR-133A assertions confirm A4 recognises `rich cultural heritage` and A1 recognises `enduring legacy`; `breathtaking landscapes` was already covered.
- C05: passed - DR-133A assertions confirm both E1 editorial frames, both apostrophe variants, both B1 candidates, and their clustering behaviour.
- C06: passed - DR-134B asserts that all three exact paragraph openers fail E8; no density mechanism was added.
- C07: not applicable - pending evaluation recommendation; no product change implemented.
- C08: not applicable - pending workflow-evaluation recommendation; no product change implemented.
- C09: not applicable - pending explicit non-promotion; no product change implemented.
- C10: not applicable - rejected 2026-07-18 via DR-122; all citation-integrity components were declined and no product change was made.
- C11: passed - commit 340ea99 (DR-113) added `here's a detailed breakdown` and AI-identity disclaimer patterns to D1 `no-collaborative-artifacts`; `python3 dev/evals/tests/test_grade.py` passes the DR-113 assertions on 2026-07-17.
- C12: passed - commit d986dd5 (DR-114 components 1-2) added the possessive bracket-label pattern covering `[Subject's Name]` to H8 `no-placeholder-residue`; `python3 dev/evals/tests/test_grade.py` passes the DR-114 assertions, including the editorial-bracket control, on 2026-07-17. Free-text `[URL of source]` remains outside deterministic coverage, and the “unambiguous” authorship claim was not adopted.
- C13: passed - commit d986dd5 (DR-114 components 1-2) added `citeturn`, `contentReference[oaicite:...]`, and `utm_source=chatgpt.com` patterns to H8 `no-placeholder-residue`; `python3 dev/evals/tests/test_grade.py` passes the DR-114 assertions on 2026-07-17.
- C14: not applicable - pending explicit non-promotion; no product change implemented.
- C15: not applicable - pending explicit non-promotion; no product change implemented.
- C16: not applicable - pending evaluation recommendation; no product change implemented.
- C17: not applicable - pending evaluation recommendation; no product change implemented.
- C18: not applicable - pending explicit non-promotion; no product change implemented.
- C19: not applicable - pending evaluation recommendation; no product change implemented.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/rohrer_source_review`; full five-lens source review followed by a focused re-check of all materially changed provenance, source-fidelity, completeness, and project-coverage text
- **Findings resolved:** five material findings covering the prior snapshot byte count, claim-specific B1 coverage for C03, restoration of load-bearing source wording in C08/C10/C12, the omitted response-construction/training/optimization mechanism claim, and the source-internal Markov direction contradiction in C15
- **Unresolved findings:** none
