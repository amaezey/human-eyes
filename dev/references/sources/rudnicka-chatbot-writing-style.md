# Karolina Rudnicka: Each AI Chatbot Has Its Own Distinctive Writing Style—Just as Humans Do

## Metadata

- **URL:** https://www.scientificamerican.com/article/chatgpt-and-gemini-ai-have-uniquely-different-writing-styles/
- **Author / owner:** Karolina Rudnicka; edited by Madhusree Mukerjee; published by Scientific American
- **Published:** 2025-07-09
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** first-person science journalism reporting an author-run exploratory stylometric comparison
- **Evidence tier:** Journalism / reported cases
- **Review mode:** update
- **Stable identifier:** Scientific American article ID 1309411; Contentful ID `3MPLDwXrQZYNJY9I2LsWUB`
- **Version / revision:** canonical article record updated 2025-07-10T17:52:31.284000+00:00; prior pre-contract Jina capture retrieved 2026-05-05
- **Full-text status:** complete
- **Snapshot:** `snapshots/rudnicka-chatbot-writing-style.md`
- **Extraction method:** canonical HTML downloaded with `curl --compressed`, preserved losslessly with `gzip -n`, and parsed from the original bytes; rendered `<article>` and embedded structured article data parsed with Python 3 and Beautiful Soup; complete body cross-checked against two Jina Reader routes; original chart and lead image downloaded and visually inspected; cited Zenodo dataset metadata and complete ZIP inspected for scope and literal-count verification
- **Snapshot SHA-256:** `0e2085da539e84d9e8cd891c970027b2259f8e794f670746730d405f441e9337`
- **Model / corpus scope:** product labels ChatGPT and Gemini, model versions and generation settings unspecified; 205 nonempty diabetes texts per product from cited dataset files timestamped January 2024, primarily 590-601 whitespace-separated words; English medical-topic explanatory prose; model-versus-model comparison only; no human comparison
- **Access limitations:** no substantive article material is missing. The page does not provide the Delta/trigram analysis code, random seed, selected 10 percent sample identifiers, preprocessing/tokenization rules, model versions, prompts, settings, human baseline, uncertainty, repeated-split results, or full ranked top-20 trigram lists. The cited dataset is indirect evidence and was inspected, not recursively ingested as a separate source card.

## Summary

Rudnicka reports an exploratory comparison of ChatGPT- and Gemini-labelled diabetes texts from a cited Zenodo dataset. She applies Burrows's Delta to one random 10 percent sample from each product group, reports lower within-product than cross-product distances, and compares frequent trigrams and word choices. The article's useful contribution is model-specific, topic- and date-bound style evidence: the ChatGPT group is more formal and clinical in the published examples, while the Gemini group is more conversational. It does not establish a generic AI voice, a human-versus-AI threshold, a validated model-attribution system, or a causal mechanism. The complete source record also exposes a prose/chart discrepancy, missing generation provenance, an unspecified random split, and no human control.

## Main insights

- The direct analysis compares two product-labelled model corpora with one topic and similar lengths; it does not compare model text with human writing.
- Reported Delta distances are 0.92 from a ChatGPT sample to the ChatGPT dataset versus 1.49 to Gemini, and 0.84 from a Gemini sample to Gemini versus 1.45 to ChatGPT. The article does not say whether sampled texts were excluded from their reference datasets or whether the result repeats across splits.
- The published phrase contrast is specific to diabetes prose: ChatGPT is described as more formal, clinical, and academic; Gemini as more conversational and explanatory.
- The chart and cited dataset support exact large differences for `blood glucose levels` and `high blood sugar`, but no matched human frequency shows that either side is an AI-versus-human tell.
- The prose says `the cascade of`; the chart says `a cascade of`. The cited dataset contains the chart form and no literal instance of the prose form.
- The principle-of-least-effort, self-priming, and emergent-ability explanations are alternatives proposed by the author, not tested mechanisms.
- The article explicitly says model idiolects may change across updates or versions. Missing model build identifiers make the reported January 2024 product labels non-portable to current systems.
- The article's possible authorship/model-identification application is interpretation, not evaluated detection evidence. No threshold, held-out human control, error rate, confidence interval, or mixed/editing test is reported.

## Evidence and claims to extract

- **Direct source reviewed:** Scientific American canonical article ID 1309411, updated 2025-07-10T17:52:31.284000+00:00, including display headline, standfirst, byline/editor, all 12 substantive body paragraphs, two substantive headings, one content-bearing chart, lead illustration, links, and structured asset metadata.
- **Method and sample:** Burrows's Delta over frequencies of common function and content words; one unspecified random 10 percent sample from each full product-labelled diabetes group; comparison against both complete product groups; top-20 trigram extraction for each group; published chart of ten selected phrase contrasts. The cited ZIP contains 205 nonempty texts per group, 15 additional empty ChatGPT placeholders, January 2024 file timestamps, and similar text lengths. Model versions, prompts, settings, generation route, random seed, sample IDs, tokenization, code, and human controls are absent.
- **Direct versus cited evidence:** C04-C10 are the article's direct dataset description, method, reported results, examples, chart, and interpretations, with the snapshot's mechanical dataset cross-check clearly marked as reviewer verification. C01-C03 report background claims inherited from cited studies. C11-C14 are author interpretations, limitations, or proposed applications rather than measured detector results. The Zenodo metadata and files are cited-source context, not a second ingestion.
- **Important limits and counterexamples:** one medical topic; one product-labelled corpus per side; undisclosed model versions and prompts; no humans; possible sample-to-reference overlap not resolved; one random split; no uncertainty, statistical test, replication, or held-out classifier; only ten of the stated top 20 trigrams per product are published as contrasts; no exact chart data table; `cascade` prose/chart conflict; lexical choice is interpreted as accessibility without a readability or reader study; causal explanations untested; later model drift acknowledged; model/document attribution unvalidated.

## Skill-use audit

- **Good use:** support H25's distinction between model-family residue and generic AI residue; support H24's model/date/register metadata requirement; supply bounded research examples of model-specific word and trigram distributions; reinforce the need for matched topic, length, prompt, model-version, and human controls.
- **Misuse / overclaim:** treating the ten phrases, four Delta distances, formal-versus-conversational contrast, or one source product label as a generic AI detector, a current-model fingerprint, or proof of authorship.
- **Unsupported use:** #46 bland critical template; #35 tonal uniformity within a document; a formal-language or colloquial-language violation; a phrase blacklist; a severity or document threshold; causal claims about training, least effort, priming, or emergent abilities; a claim about current ChatGPT or Gemini builds.
- **Underused evidence:** exact January 2024 corpus timing; missing build/prompt provenance; one-split and possible reference-overlap limits; the chart/prose `cascade` discrepancy; the model-versus-model rather than model-versus-human boundary.
- **Patterns left on the table:** no new active pattern. The ten phrase contrasts are H24/H25 evaluation candidates only; future work would need exact source data, model versions, repeated held-out splits, matched prompts and humans, preprocessing rules, and uncertainty before a project rule or model-attribution dimension could be considered.

## Matched patterns / rules

- H25 `Model-family versus generic-AI residue`: fully covers the correct research framing but is an open hypothesis, not runtime behavior.
- H24 `Register-specific vocabulary density`: partly covers the need for dated, register-specific lexical comparison but does not implement product-family trigram profiles.
- H1 `Continuous calibrated register-distance score per pattern`: adjacent to the distance framing, but Rudnicka reports uncalibrated source-corpus Delta distances, not human-register z-scores or project reliability curves.
- H3 `Drop detection framing entirely`, `human-eyes/references/process.md`, and `dev/TESTING.md`: fully cover the no-authorship, matched-register, candidate-versus-threshold, provenance, and complete-Audit boundaries.
- #7 `no-ai-vocabulary-clustering`: partly recognizes the cited background list, not the direct diabetes result. Focused execution found `delve`, `underscore`, and `commendable` among the six cited examples, while bare `align`, `noteworthy`, and `versatile` were not #7 matches. Each of the ten direct diabetes phrases returned zero #7 candidates.
- #35 `tonal_uniformity`: not covered and not supported. Its agent assessment asks whether one whole text holds a register without breaks; Rudnicka compares aggregate phrase frequencies between corpora and supplies no within-document or human-register result.
- #46 `no-bland-critical-template`: not covered and explicitly not supported; the project already records Rudnicka only as model-specific context, not template evidence.

## Associated hypotheses

- H25 `Model-family versus generic-AI residue`: directly informed and materially bounded by missing model/version and prompt provenance.
- H24 `Register-specific vocabulary density`: directly informed by the diabetes-only phrase distributions and lack of human/register controls.
- H1 `Continuous calibrated register-distance score per pattern`: methodologically adjacent, but the source supplies no project calibration or human distribution.
- H3 `Drop detection framing entirely`: informed by the gap between a source-corpus distance result and the article's proposed authorship application.

## Questions / follow-up

- Which ChatGPT and Gemini model builds, interfaces, prompts, sampling settings, and dates produced the cited files?
- Were each 10 percent sample's texts excluded from the corresponding full reference dataset before Delta was calculated, and what happens across repeated seeded splits?
- What tokenization, case, punctuation, normalization, and trigram-ranking rules produced the top-20 lists and chart?
- Can the author supply the analysis code, selected sample IDs, complete trigram tables, exact chart values, and uncertainty?
- Do the same phrase differences persist with matched human diabetes prose, current model versions, other topics, and controlled prompts?
- If a future recommendation needs the cited slang, colloquialism, or adjective findings, ingest and independently review the specific upstream studies first.

## Update provenance

The prior card and manifest recorded no snapshot digest. Before replacement, the exact prior snapshot was hashed as `0b545413213ba8955a2b3af0eec02d0ef9c13641032958a0a91e5fc351409cf8`, verified byte-for-byte against commit `f28a3706816d0ca5107196955a5d14418732a5af`, and archived without transformation.

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none recorded; pre-contract Jina capture | `snapshots/archive/rudnicka-chatbot-writing-style/2026-05-05-0b545413.md` | 2026-05-05 | `0b545413213ba8955a2b3af0eec02d0ef9c13641032958a0a91e5fc351409cf8` |
| current | Scientific American article ID 1309411; Contentful ID `3MPLDwXrQZYNJY9I2LsWUB` | `snapshots/rudnicka-chatbot-writing-style.md` | 2026-07-17 | `0e2085da539e84d9e8cd891c970027b2259f8e794f670746730d405f441e9337` |

## Decision history

- 2026-07-26: C05, C07, and C08 rejected via DR-25. Mae declined the ten published diabetes trigrams as phrase candidates and declined a Burrows's Delta evaluation. The trigrams were measured against the project corpora before the ruling: nine of the ten (`individuals with diabetes`, `blood glucose levels`, `the development of`, `characterized by elevated`, `an increased risk`, `the way for`, `a cascade of`, `high blood sugar`, `blood sugar control`) occur zero times across 137k words of human and 49k words of generated prose, with the counter verified against a control term that does occur. The tenth, `is not a`, runs 0.79 per 1000 words in generated prose against 0.20 in human, but it is a syntactic fragment rather than a phrase habit, and reading its 39 generated occurrences showed nearly all of them are the negative-to-affirmative reversal that #9 `no-negative-parallelisms` already covers. That reading is what produced DR-25A, a #9 matcher repair recorded on the register row rather than against any claim here.

- The pre-contract card had no claim IDs, user decisions, implementation statuses, snapshot digest, update provenance, or independent-review gate. It mapped the source to model drift, model-specific idiolect context, H1, H12, and a metadata question, and explicitly rejected #46 as unsupported. Those notes were not user approvals or implemented changes. This update replaces them with C01-C14, retains the #46 non-promotion, narrows H1 to methodological adjacency, moves the primary mapping to H24/H25, and leaves every recommendation pending.

## Prior-to-current comparison

- **Added:** complete current provenance; article and Contentful identifiers; editor and update timestamp; original HTML, chart, and lead-image attachments; exact prior archive and digest; beginning/middle/end structure checks; cited-dataset scope verification; 14 claim IDs; deterministic #7 checks; source-to-project coverage; recommendation states; decision history; and independent-review fields.
- **Corrected:** the current display headline differs from the old internal/Jina title; the direct corpus is 205 nonempty files per product, not only “hundreds”; the analysis is model-versus-model with no human control; model versions, prompts, random split, and code are unspecified; the article's `the cascade of` differs from its chart and cited data's `a cascade of`.
- **Removed:** the unrelated fundraising module and page chrome from the active snapshot. No substantive article claim was removed.
- **Unchanged:** canonical URL, author, publication date, direct article body, four Delta values, core diabetes phrase contrasts, model-update warning, rejection of #46 support, and the source's main use as model-specific rather than universal-AI context.

## Project coverage

This is the authoritative review table. Focused #7 results below came from the live `human-eyes/scripts/grade.py::check_ai_vocabulary` implementation on 2026-07-17; they are surface-only coverage checks, not complete Audits. Every recommendation remains a pending decision for Mae.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Comparing one ChatGPT voice with many human writers can confound a model-specific voice with ordinary between-person variation; the article proposes an idiolect-like model framing. | Author motivation and conceptual framing, not a direct human-versus-model test in this article. No human sample enters the reported diabetes analysis. | **fully covered conceptually:** H25 separates model-family from generic-AI residue; H3 and `process.md` reject authorship inference. | The article does not show that an LLM has one stable idiolect across prompts, users, sessions, or versions, or that its variation is comparable to a person's idiolect. | **adopt:** preserve the asymmetric-comparison and model-specific boundary whenever this source is cited; no runtime change. | pending | not started |
| C02: Cited studies are said to show that ChatGPT favors standard grammar and academic expressions and shuns slang or colloquialisms. | Indirect background claim inherited from two linked papers; neither is directly reviewed in this card. Scope, models, languages, genres, measures, and counterexamples are not recoverable from the article summary. | **partly covered:** #35 assesses whole-text register lock, #41 has genre-specific review, and H24 asks for register controls, but none implements this cited result. | Treating formal language or absent colloquialism as a violation would confuse register fit with provenance and exceed the source. | **do not adopt:** make no pattern or severity change from this secondary summary; ingest the exact upstream paper before any project recommendation depends on it. | pending | not started |
| C03: Cited work is said to show overuse of `delve`, `align`, `underscore`, `noteworthy`, `versatile`, and `commendable` relative to humans. | Indirect background synthesis across a directly linked Juzek paper and a Scientific American report. The article supplies no counts, common comparison corpus, or shared model/version scope for the six examples. | **partly covered:** focused #7 execution matched `delve`, `underscore`, and `commendable`, and missed bare `align`, `noteworthy`, and `versatile`. The complete Juzek card is authoritative for its own dated biomedical forms and nulls. | This article cannot validate the live three-item paragraph threshold, equal weighting, the missed items, or a current generic blacklist. | **do not adopt:** route direct claims to the upstream source cards and retain this list only as attributed context; no #7 expansion or threshold claim. | pending | not started |
| C04: The cited diabetes corpus contains 205 nonempty ChatGPT-labelled and 205 nonempty Gemini-labelled texts of similar length; it is English medical-topic prose with January 2024 file timestamps, while model versions, prompts, settings, and generation route are absent. | Article description plus reviewer inspection of Zenodo record revision 3 and the complete cited ZIP. Fifteen extra ChatGPT placeholders are empty; nonempty texts are usually 590-601 whitespace-separated words, with one 754-word Gemini file. ZIP timestamps are not proof of generation time. | **fully covered as a source-record boundary:** H24/H25 and `dev/TESTING.md` require model, date, register, prompt, length, and provenance controls. | The old card omitted exact nonempty counts, empty files, timing, length distribution, and missing-generation metadata. | **adopt:** retain these corpus and missing-provenance limits in every use of the direct results; no product change. | pending | not started |
| C05: One random 10 percent ChatGPT sample has Delta 0.92 to the ChatGPT dataset and 1.49 to Gemini; one random 10 percent Gemini sample has 0.84 to Gemini and 1.45 to ChatGPT. | Direct article result. No sample IDs, seed, rounding rule, preprocessing, code, repeated splits, uncertainty, significance test, or statement that sampled texts were removed from the reference datasets. | **partly covered:** H1 proposes calibrated register-distance scores; `dev/TESTING.md` requires reproducible provenance and matched comparisons. No live check computes Burrows's Delta. | The four values cannot establish robustness, calibration, generalization, or held-out attribution. Possible sample/reference overlap remains unresolved. | **test-adapt:** request code and sample IDs, then repeat seeded held-out splits with sample exclusion and uncertainty before considering any distance-based project feature. | rejected | not applicable |
| C06: The lower within-product than cross-product distances indicate distinct ChatGPT and Gemini writing styles in this diabetes dataset. | Author interpretation of C05. It is consistent with the reported direction but based on one undisclosed split and no human, topic-transfer, version-transfer, or prompt control. | **fully covered as bounded framing:** H25 already treats Rudnicka as model-family context rather than generic AI evidence. | The article's “idiolect” and “authorship turns out to be quite clear” wording is stronger than a single unreplicated, possibly non-held-out comparison supports. | **adopt with a boundary:** record a dataset-specific product-label separation result only; do not claim a stable idiolect, current-model fingerprint, or general attribution accuracy. | pending | not started |
| C07: The author extracted each product group's 20 most frequent trigrams and compared them, but publishes only ten selected contrast rows in the chart and ten phrase examples in prose. | Direct method description plus incomplete published result. No complete top-20 lists, ranks, preprocessing, punctuation/case rules, code, or selection criterion for “most striking” differences. | **not covered:** no live n-gram profile or product-family phrase registry exists; H24/H25 provide only research framing. | The published selection cannot establish which phrases are most frequent, how selection affected effect sizes, or how a future implementation should tokenize them. | **test-adapt:** obtain the complete ranked tables and method before evaluating n-gram profiles; add no phrase rule from the selected chart alone. | rejected | not applicable |
| C08: ChatGPT's five examples are described as formal, clinical, and academic; Gemini's five examples as conversational and explanatory. | Direct aggregate phrase examples and author interpretation within one diabetes corpus. No human comparison, per-document distribution, reader rating, or control for prompt or factual content. | **not covered by active rules:** each of the ten direct phrases returned zero #7 candidates; #35 asks a different within-document question. H24/H25 partly cover the research need. | A product-wide register label or phrase blacklist would overgeneralize one topic and unknown model builds. | **test-adapt:** preserve the ten phrases as dated model/register research candidates and compare matched prompts, topics, versions, and human diabetes prose before any project mapping. | rejected | not applicable |
| C09: Gemini uses `blood glucose levels` once; `high blood sugar` occurs 25 times in ChatGPT and 158 times in Gemini; ChatGPT uses `glucose` more than twice as often as `sugar`, with the reverse for Gemini. | Direct article counts and ratio statements; the three exact phrase counts reproduce by case-insensitive literal scan of the cited files. The broad word ratios were not independently recalculated here. | **not covered by active rules, appropriately:** the direct phrases return zero #7 candidates; H24/H25 frame source-specific density and model metadata. | Counts are corpus totals without document normalization, uncertainty, human baseline, or model-version provenance. Frequency direction does not imply that either term is defective. | **do not adopt:** keep the counts as bounded distribution evidence; do not add `glucose`, `sugar`, or either phrase as a violation. | pending | not started |
| C10: The chart displays ten phrase-frequency contrasts, but its `a cascade of` label conflicts with the prose's `the cascade of`; the cited files contain 12/52 literal `a cascade of` occurrences and zero `the cascade of` occurrences. | Direct source-internal discrepancy plus reviewer literal-substring verification of the cited files. The mechanical count does not reproduce the author's trigram preprocessing or full ranking. | **fully covered by the refreshed source record:** the snapshot preserves the original chart, both forms, and the verification boundary. No runtime rule applies. | Uncorrected prose could seed a nonexistent example into a phrase catalogue or test fixture. | **adopt:** cite the chart form when describing the measured example, retain the prose discrepancy, and take no product action from the typo. | pending | not started |
| C11: Choosing `sugar` rather than `glucose` is interpreted as a preference for simple, accessible language. | Author interpretation grounded in lexical contrast, not a readability, comprehension, patient, or reader study. Medical precision and audience fit are not evaluated. | **partly covered as process discipline:** `process.md` requires context and meaning preservation; no rule treats a simpler synonym as universally better. | Accessibility may depend on audience and medical precision; the source supplies no human response or task-fit evidence. | **do not adopt:** record the interpretation only; require audience and accuracy evaluation before any rewrite guidance. | pending | not started |
| C12: Least effort, self-priming, and emergent abilities are proposed as possible explanations for model idiolects. | Three explicit alternative hypotheses in the article, with no intervention, training-data access, model-internal measure, or causal comparison. | **fully covered as a non-promotion boundary:** source-ingest and `process.md` separate measured result from interpretation; no live mechanism claim implements these hypotheses. | Choosing one explanation would exceed the evidence, and the alternatives are not shown to be exhaustive. | **do not adopt:** preserve all three as speculative author interpretation and make no causal product claim. | pending | not started |
| C13: Model idiolects may change and develop across updates or new versions. | Author qualification consistent with the missing build identifiers and broader project drift evidence, but not measured longitudinally in this article. | **fully covered conceptually:** H25 and existing `pattern-opportunities.md` rows require model/version/date metadata and separate model-family from generic residue. | Open hypotheses do not make the direct result portable to current ChatGPT or Gemini products. | **adopt:** date-stamp the January 2024 source files, record product labels as version-unspecified, and require fresh versioned evidence before current-model claims. | pending | not started |
| C14: Knowing model idiolects could help determine whether an essay or article was produced by a model or individual. | Proposed application and analogy, not a validated result. The direct analysis has no human group, held-out classifier, threshold, confidence, sensitivity, specificity, false-positive rate, mixed/edited texts, or current models. | **fully covered at the project boundary:** H3, `process.md`, and `dev/TESTING.md` prohibit authorship claims and distinguish candidate recognition from complete evaluation. | The article does not establish human-versus-AI detection, individual human attribution, or operational model attribution. | **do not adopt:** make no authorship or source-model verdict from this source; any future attribution research needs held-out humans, multiple topics/versions/prompts, mixed/edit controls, calibration, and error analysis. | pending | not started |

## Recommendations

- C01: **adopt** the asymmetric-comparison and model-specific boundary in source summaries; no runtime change.
- C02: **do not adopt** formal-language or missing-colloquialism rules from this secondary summary; review the upstream sources first.
- C03: **do not adopt** a #7 expansion or threshold claim from the six attributed examples; route evidence to direct upstream cards.
- C04: **adopt** the exact corpus and missing-generation-provenance limits in every use of the direct result.
- C05: **test-adapt** Burrows's Delta only after code, sample IDs, held-out sample exclusion, repeated splits, and uncertainty are available.
- C06: **adopt** only the bounded dataset-specific product-label separation result; reject stable/current/general fingerprint wording.
- C07: **test-adapt** n-gram profiles only after obtaining complete ranked tables, preprocessing, and selection rules.
- C08: **test-adapt** the ten phrases with matched prompts, topics, versions, and human controls; add no phrase rule now.
- C09: **do not adopt** `glucose`, `sugar`, or either phrase as a violation; preserve the counts as bounded evidence.
- C10: **adopt** the chart form while retaining the prose discrepancy; take no product action from the typo.
- C11: **do not adopt** generic simplification guidance without audience, comprehension, and medical-accuracy evidence.
- C12: **do not adopt** any causal mechanism; preserve all three possibilities as speculation.
- C13: **adopt** source-file date and version-unspecified metadata; require fresh versioned evidence for current-model claims.
- C14: **do not adopt** an authorship or source-model verdict; require a separate held-out evaluation before any attribution research.

## Evaluation of approved changes

- C01: not applicable - recommendation pending; no product change made.
- C02: not applicable - recommendation pending; no product change made.
- C03: not applicable - recommendation pending; no product change made.
- C04: not applicable - recommendation pending; no product change made.
- C05: not applicable - rejected 2026-07-26 via DR-25. Burrows's Delta scores a document against reference corpora, which is authorship attribution and neither of the two detector types, so no distance feature was built or evaluated.
- C06: not applicable - recommendation pending; no product change made.
- C07: not applicable - rejected 2026-07-26 via DR-25. The ten published trigrams were not adopted as phrase candidates; the complete ranked tables were not pursued.
- C08: not applicable - rejected 2026-07-26 via DR-25. Measured against both project corpora, nine of the ten phrases occur zero times in 186k words and the tenth, `is not a`, is ordinary syntax, so no phrase rule was added.
- C09: not applicable - recommendation pending; no product change made.
- C10: not applicable - recommendation pending; no product change made.
- C11: not applicable - recommendation pending; no product change made.
- C12: not applicable - recommendation pending; no product change made.
- C13: not applicable - recommendation pending; no product change made.
- C14: not applicable - recommendation pending; no product change made.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/rudnicka_source_reviewer`, fresh, source-dedicated, and read-only
- **Findings resolved:** none; the reviewer reported 0 findings in the full five-lens review and 0 findings in the focused provenance re-check after lossless raw-HTML compression
- **Unresolved findings:** none
