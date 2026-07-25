# Suvanto et al.: Interpretable Text Classification Applied to the Detection of LLM-generated Creative Writing

## Metadata

- **URL:** https://arxiv.org/abs/2601.07368
- **Author / owner:** Minerva Suvanto, Andrea McGlinchey, Mattias Wahde, and Peter J Barclay
- **Published:** arXiv v1 submitted 2026-01-12; accepted for ICAART 2026; proceedings date none found
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** accepted conference paper and academic empirical preprint
- **Evidence tier:** peer-reviewed / academic empirical, reviewed as the accepted arXiv manuscript
- **Review mode:** new
- **Stable identifier:** arXiv:2601.07368v1; DOI 10.48550/arXiv.2601.07368
- **Version / revision:** v1, submitted 2026-01-12
- **Full-text status:** complete
- **Snapshot:** `snapshots/suvanto-interpretable-llm-creative-writing.md`
- **Extraction method:** complete arXiv experimental HTML converted to Markdown, with the official 12-page PDF preserved and checked using pdfinfo, pdftotext -layout, rendered pages, and the arXiv metadata page
- **Snapshot SHA-256:** `c3a80ae02874e6f5380c72e40ded3abbe5629c54fb6f3e0d8324ee9c04b8600e`
- **Model / corpus scope:** GPT-4.1 at temperature 0.7 rewrote 8,068 excerpts from twelve 1920s and 1930s British detective novels by Agatha Christie and Dorothy L. Sayers. The 8,068 human excerpts and 8,068 rewrites are mainly English with some foreign-language passages, were chunked to approximately 100 words using randomly assigned maximums of 92 to 125 words before punctuation tokenisation, and were split 70/15/15 for training, validation, and testing. A separate experiment asked 119 mostly non-native but proficient English readers to identify the generated member of five test-set pairs.
- **Access limitations:** none for the paper. Figure pixels are not embedded in the Markdown snapshot, but all figures remain in the preserved official PDF at `snapshots/attachments/suvanto-interpretable-llm-creative-writing-arxiv-v1.pdf`, SHA-256 `6ea181a5b47738d31a97f4143be38cad50b1c523d3c7c9589540a7670cb5fc4c`, and every caption and surrounding interpretation is in the extraction. The paper links a tokenised Zenodo dataset, but the dataset was not required to extract the paper's reported findings and was not ingested.

## Summary

This accepted ICAART 2026 paper studies why simple classifiers distinguish GPT-4.1 rewrites from source passages in classic British detective fiction. Its linear unigram classifier reaches 0.9814 test accuracy while 119 human evaluators score 0.499 on five paired examples. The paper attributes the machine result to many small lexical differences, especially greater synonym variety, plus modernisation, Americanisms, and removal of foreign-language and colloquial material. It materially challenges human-eyes pattern #53 because that live check treats low vocabulary diversity as the suspicious direction, while this rewrite corpus finds higher generated-text entropy. The work does not establish a general authorship rule: it uses one model, one rewrite prompt, one narrow period and genre, divides a twelve-work corpus without reporting work, author, or original-rewrite pair grouping, and manually explores 190 selected features without multiple-annotator or agreement reporting. The user queue title, "Interpretable Text Classification for LLM-generated Creative Writing", omits "Applied to the Detection of" from the actual title at the authoritative URL.

## Main insights

- Five unigram classifiers reach 0.9310 to 0.9814 test accuracy on held-out passages from the same DET12 corpus, while human pairwise classification is at chance.
- The strongest project-relevant result is directional: GPT-4.1 rewrites have higher unigram entropy and greater synonym variety than the human originals. This supports manual review of over-rephrasing but contradicts #53's one-way low-diversity framing.
- Rewriting affects dialogue verbs, other verbs, adverbs, adjectives, nouns, prepositions, grammar, discourse markers, and conjunction choices. The paper finds more present and past participles and gives a nominalisation example, but does not reduce these shifts to the current superficial -ing regex.
- The rewrites modernise 1920s and 1930s language, favour American forms over British ones, and remove foreign-language passages and colloquialisms. These are style-fidelity and register effects, not universal defects or safe word lists.
- Punctuation normalisation, removal of punctuation and capitalisation, and letter-frequency checks did not materially alter classifier accuracy. The paper also reports similarities in common words, proper nouns, pronouns, and several verb tenses.
- Classification remains high after frequency-ordered and weight-filtered unigram removal, supporting a multivariate account. This aligns with human-eyes signal stacking in principle but does not validate its current components or threshold.
- The authors explicitly warn that black-box detection without trustworthy reasons can support unjustified accusations. That position aligns with the project's existing non-authorship boundary.
- The paper acknowledges that asking for a rewrite may itself invite synonyms. Preliminary outline and continuation experiments are not sufficient evidence for transfer to fresh generation, other models, contemporary fiction, other languages, longer works, or unseen authors and books.

## Evidence and claims to extract

- **Direct source reviewed:** arXiv:2601.07368v1 in complete experimental HTML and the official 12-page PDF, submitted 2026-01-12 and accepted for ICAART 2026.
- **Method and sample:** DET12 contains 8,068 original excerpts and 8,068 GPT-4.1 rewrites from twelve public-domain Christie and Sayers novels. Rewrites used one fixed prompt, temperature 0.7, and approximately 100-word inputs. The paper uses a 70/15/15 split without a reported grouping procedure, five unigram classifiers, a 119-person paired reading experiment, Biber-feature analysis, manual inspection of 190 frequent high-ratio unigrams, feature ablation, and whole-corpus unigram entropy.
- **Direct versus cited evidence:** C01 through C13 and C15 through C17 are direct results, author-reported experiments, figure evidence, or explicit source limitations. C14 is the authors' interpretation and design position; the broader claim that post-hoc explanation methods can be unreliable is supported by cited work rather than measured in DET12. Related-work detector scores and rewriting findings are indirect and are not used as product recommendations here.
- **Important limits and counterexamples:** the twelve-work corpus is divided 70/15/15 without a reported work-, author-, or original-rewrite pair-grouping procedure; no work-held-out or author-held-out result is reported. GPT-4.1 and one rewrite prompt may produce task-specific synonym expansion. The human task covers only five pairs under a 90-second limit, and most evaluators are not native English speakers. Manual explanation coding covers only 190 of 30,302 features, has no multiple-annotator or agreement reporting, and admits it is not comprehensive. Length differs modestly between classes. Several linguistic features remain similar, punctuation and case do not explain the reported performance, and alternative generation methods have only preliminary support.

## Skill-use audit

- **Good use:** treat the source as narrow, direct evidence that generated rewrites can increase lexical variety; support style-fidelity review for synonym expansion, modernisation, locale drift, and loss of colloquial or multilingual texture; support multivariate and interpretable evaluation rather than one-word verdicts.
- **Misuse / overclaim:** do not transfer the 0.9814 classifier accuracy to human-eyes, to whole documents, to unseen books or authors, or to other models and genres. Do not treat one unigram, American spelling, modern wording, a participle, or absence of French as proof of authorship.
- **Unsupported use:** the source does not validate current human-eyes thresholds, current signal-stacking components, #3's tacked-on -ing regex, a universal high-diversity direction, a British-versus-American language rule, or a document-level authorship conclusion.
- **Underused evidence:** #53 currently encodes the opposite lexical-diversity direction; referent cycling has no live record after DR-156 removed former #11; #41 fiction does not inspect period, locale, multilingual, or colloquial fidelity; H23 lacks this creative-fiction corroboration.
- **Patterns left on the table:** dialogue-verb substitution, over-rephrasing across parts of speech, period modernisation, locale drift, removal of code-switching and colloquial texture, and task-specific lexical entropy are not represented together in the live project.

## Matched patterns / rules

- synonym cycling: no live record, former #11 removed 2026-07-25 through DR-156
- #53 vocabulary diversity in `human-eyes/scripts/grade.py:2034` and `human-eyes/references/patterns.md:399`
- #3 superficial -ing analysis in `human-eyes/scripts/grade.py:1453` and `human-eyes/references/patterns.md:85`
- #35 tonal uniformity as weak adjacent register coverage in `human-eyes/scripts/judgement.json`
- #41 fiction branch in `human-eyes/scripts/judgement.json:253`
- `overall-signal-stacking` in `human-eyes/scripts/grade.py:830`
- product boundary in `STRATEGY.md:14` and `human-eyes/references/process.md:75`

## Associated hypotheses

- H1 continuous calibrated register-distance score per pattern
- H3 drop detection framing entirely
- H12 genre-aware threshold calibration
- H22 long-tail compression and grammatical standardisation
- H23 nominalization and noun-heavy style
- H24 register-specific vocabulary density
- H25 model-family versus generic-AI residue
- Proposed evaluation question: does rewrite-conditioned lexical expansion persist under work-held-out, author-held-out, contemporary-fiction, fresh-generation, continuation, model, and prompt controls?

## Questions / follow-up

- Does the Zenodo dataset preserve pair identifiers well enough to audit whether an original passage and its rewrite can land in different splits?
- Does the reported lexical-entropy direction survive corrected TTR or MTLD, matched lengths, work-held-out splits, and non-rewrite generation?
- Which of the 190 annotated features remain stable under multiple annotators and contemporary human fiction controls?
- Answered 2026-07-25 by DR-156: synonym cycling gets no registered assessment and no catalogue entry. Style-fidelity changes live only inside #41 fiction.
- Should #53 be bidirectional, descriptive, or suspended until the direction is calibrated by genre and task?
- The linked Zenodo dataset and directly cited upstream papers remain separate sources. Ask before ingesting any of them.

## Update provenance

Not applicable: initial ingestion.

## Decision history

- DR-87B implemented 2026-07-26: the six LLM-preferred dialogue verbs the paper names (`remarked`, `responded`, `mentioned`, `replied`, `exclaimed`, `chuckled`) are now in the fiction branch of the `genre_specific` agent-judgement record, framed as the avoidance of plain `said`. The paper reports 17 dialogue verbs with 14 favouring the model but publishes no full feature list, so the other eight are not recoverable from the preserved text; the Zenodo deposit was not fetched. No programmatic check was built and no pattern number was added.
- DR-87A implemented 2026-07-26: `exited` is now an #7 clustering candidate, on the source's 61-versus-zero count across the GPT-4.1 rewrites and their source passages. It contributes to #7's paragraph threshold and never fails alone. The project corpora contain no occurrence in either sample set. DR-87's rewrite-fidelity components stay open.

- 2026-07-17: Mae approved and implemented the #53 direction flip: windowed 150-word lexical diversity flagging high values, two-tier (0.71 flag, 0.74 above-observed-human-range note), commit b199a6d.
- None: initial review.
- C03 approved 2026-07-17: flip #53's direction; implementation is pending a plan, so the status stays `not started`. All other rows remain pending.

## Project coverage

This is the authoritative review table. Every row separates the source finding, evidence strength, live coverage, gap, and pending decision.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Five unigram classifiers score 0.9310 to 0.9814 on the DET12 test split; the interpretable linear classifier scores 0.9814. | Direct test-split passage result from a corpus of 16,136 labelled samples drawn from twelve source novels and one GPT-4.1 rewrite condition. The paper reports accuracy, not grouped cross-work or cross-model transfer. | `STRATEGY.md:16` rejects authorship classification, and human-eyes has no comparable trained classifier; **not covered** as product behaviour. | No human-eyes model, feature representation, or validation supports these accuracy values. | Record the metrics only as upstream, corpus-specific evidence. Do not present them as human-eyes performance. Any adoption would require work-held-out, author-held-out, model, prompt, genre, and language evaluation. | pending | not started |
| C02: In a five-pair experiment, 119 evaluators produce 297 correct answers out of 595, or 0.499 accuracy. | Direct result under a 90-second paired-choice task. Most evaluators were proficient but not native English speakers, and only five pairs were shown. | `waltzer-teachers-detect-ai-essays.md` and `russell-karpinska-iyyer-detectors.md` already show that human classification results depend on the reader population and corpus, while `STRATEGY.md:16` rejects authorship classification; the DET12 empirical result itself is **not covered**. | The project has no corresponding fiction-reader experiment and should not generalise from five pairs. | Record as narrow human-evaluation context only. Do not use chance performance to justify automated document verdicts. | pending | not started |
| C03: GPT-4.1 rewrites use more varied vocabulary. Whole-corpus unigram entropy is 9.164 versus 8.875, a 0.29-bit increase; the authors interpret this as about 22% greater word-choice variation. | Direct aggregate corpus calculation plus the authors' derived interpretation. It is specific to one rewrite prompt and may be inflated by the instruction to make the passage structurally different. | Nothing recognises excessive synonym substitution after DR-156 removed former #11, and #53 fails only for low type-token ratio at 150+ words in `grade.py:2034-2053`; **challenges current behaviour**. Both Table 1 examples are below 150 words, and focused execution skipped #53 for both. | #53 presents a universal one-way direction that this source and the existing Wikipedia W12 review contradict. Raw TTR also differs from whole-corpus entropy. | Re-evaluate #53 using corrected TTR or MTLD and entropy across matched fresh-write, rewrite, and continuation conditions before retaining a direction. Include genre, length, model, prompt, and human repetition controls. | approved | implemented |
| C04: Rephrasing spans dialogue verbs, other verbs, adverbs, adjectives, nouns, prepositions, grammar, discourse markers, and conjunctions. Fourteen of seventeen selected dialogue verbs favour GPT-4.1, with `said` replaced by choices such as `remarked`, `responded`, and `mentioned`. | Direct exploratory annotation of 190 selected frequent high-ratio unigrams, with paired contexts. The source states that the analysis is not comprehensive and supplies no multi-annotator agreement. | #41 fiction dialogue review; **partly covered**. Repeated referents have no live record after DR-156 removed former #11, while #41 checks voice differentiation, exposition, and broad source-style fidelity but not explicit over-rephrasing or dialogue-verb substitution. | Current coverage does not distinguish useful lexical precision from needless synonym expansion, nor dialogue attribution from referent cycling. | Evaluate a contextual fiction style-fidelity prompt for unnecessary rephrasing across parts of speech. Require deliberate diction, dialogue rhythm, quotation, and source-author controls; do not add a synonym blacklist. | pending | not started |
| C05: Present and past participles are more prominent in the GPT-4.1 rewrites. | Direct aggregate Biber-feature comparison shown in Figure 2, but no numeric effect size is stated in the prose and the result remains corpus-specific. | #3 and `check_superficial_ing` at `grade.py:1453-1474`; **partly covered**. The live regex only catches a short list of tacked-on comma-led analysis clauses. Focused execution found no #3 match in either Table 1 excerpt. | The source concerns participial frequency broadly, not only superficial analysis clauses. Treating it as support for the current regex would overclaim. | Add this source to H23 and evaluate participial-clause density separately from #3 on matched fiction and non-fiction controls before any check or guidance change. | pending | not started |
| C06: GPT-4.1 sometimes nominalises phrases, as in changing an investigated car route into a route being `under investigation`; other grammar changes occur but are less frequent in the selected subset. | Direct paired example and exploratory feature annotation. The paper explicitly says larger study is needed for syntax. | H23 names nominalisation and noun-heavy style; `underspecified_language` can flag nominalisations that leave a relevant property, actor, or action unspecified; **partly covered** as hypothesis and contextual review, not a dedicated measure. | No current check measures nominalisation density or distinguishes precise nominalisation from actor-hiding or vague abstraction. | Add the creative-fiction example as corroborating H23 evidence and test candidate measures with actor, genre, and clarity controls before deciding on a product home. | pending | not started |
| C07: Rewrites modernise period language, including `to-day` to `today`; `exited` occurs 61 times in generated training samples and zero times in source samples. | Direct corpus observation with an illustrative Google Ngram trend. The broader temporal explanation is based on 1920s and 1930s originals. | H24 and H25 require time and model metadata, but no fiction period-fidelity review exists; **not covered**. | Modern language is appropriate in contemporary fiction, so a universal token rule would be wrong. The issue is mismatch to an intended period or source style. | Evaluate temporal-style fidelity only when a source period or target voice is known. Use contemporary fiction and intentional modernisation as controls. | pending | not started |
| C08: GPT-4.1 favours American forms and phrases over the British forms in these novels. | Direct annotation category with examples such as `realise` to `realize` and `round` to `around`, but only four of the 190 selected features were annotated E3 and all originals are British period fiction. | #35 register review and H12 genre calibration are adjacent; **not covered** for locale fidelity. | The project has no locale-aware source comparison. A spelling rule would penalise legitimate American English. | Evaluate locale drift as source-to-rewrite fidelity, never as a standalone AI tell. Require declared locale and mixed-dialect controls. | pending | not started |
| C09: GPT-4.1 mostly removes short foreign-language passages and colloquialisms such as `mon ami` and `'em`. | Direct exploratory annotation: two of the 190 selected features were annotated E4 and one was annotated E5, with category overlap allowed. The source offers a plausible interpretation rather than a comprehensive rate. | #35 and #41 fiction weakly address register and source oddities; **not covered** for multilingual or colloquial preservation. | Current review cannot name code-switching loss, dialect smoothing, or colloquial texture removal. The tiny selected-feature counts do not justify a detector rule. | Evaluate these as rewrite-fidelity questions inside fiction review, with intentional standardisation, translation, dialect, and accessibility controls. | pending | not started |
| C10: Normalising dashes and quotes, removing punctuation and capitalisation, and checking letter frequencies produced no discernible classification change; word choice carried the reported signal. | Direct author-reported null experiments, though detailed run values are not tabulated. | Punctuation checks remain craft findings with tolerance notes, and `STRATEGY.md:14-16` says checks inspect writing rather than authorship; **partly covered** in interpretation, not as a recorded domain-specific null. | This result does not invalidate punctuation as a craft concern, but it challenges any transfer from punctuation flags to detector confidence in this setup. | Record the null result and retain the non-authorship boundary. If punctuation is evaluated as comparative evidence, require generation-condition and genre-specific tests rather than transferring current style checks. | pending | not started |
| C11: Classification remains high under two unigram-ablation sequences. In the weight-filtered sequence, removing 100 features with magnitude at least 0.1 reduces accuracy from about 0.98 to about 0.88. The authors also conclude that nullifying roughly 80 of the features that most help the classifier would still leave accuracy around 0.90. | Direct Figure 5 ablation plus the authors' conclusion. The blue curve removes features in descending total-frequency order regardless of weight. The orange curve walks the same frequency order but removes only features with weight magnitude at least 0.1; the 0.1 cutoff is arbitrary. The paper's prose states the 0.88 endpoint for 100 large-magnitude removals, while the roughly 80 most-helpful framing is its looser conclusion. The result remains DET12-specific. | `overall-signal-stacking` and `STRATEGY.md:10-16`; **fully covered** as a multivariate principle, not as the same components or score. | The paper's unigram weights differ from human-eyes craft-pattern components, so its accuracy and ablation threshold cannot transfer. | Record support for constellation-based interpretation. Do not change the current stacking threshold or claim robustness without human-eyes evaluation. | pending | not started |
| C12: Common words and copied proper nouns are similar across the two classes. Figure 1's ten smallest Biber-feature differences are third-person pronouns, attributive adjectives, past tense, second-person pronouns, infinitives, synthetic negation, other nouns, present tense, agentless passives, and first-person pronouns; the authors say these similarities help explain human difficulty. | Direct frequency-list observations and direct training-set relative-frequency directions from Figure 1, plus the authors' interpretation that these similarities help explain human difficulty. The plot identifies the smallest class differences, not evidence that the features are identical or generally non-discriminative. | No explicit positive or null-feature inventory; **not covered**. | A source card that records only differences would overstate how much the generated passages diverge. | Preserve these null results as controls. Take no product action unless a future evaluation proposes positive human evidence or absence-based scoring. | pending | not started |
| C13: The rewrite instruction may cause synonym expansion. Preliminary outline-only and continuation experiments appear detectable, but further work is required. | The rewrite confound is an explicit source limitation. Alternative-generation findings are preliminary author reports without a full method or results table. | `dev/TESTING.md` distinguishes fresh writes and rewrites, requires varied prompts, and records model provenance; it does not require a multi-model creative-fiction transfer stratum. The specific transfer question is **not covered**. | The current paper cannot establish that its lexical directions generalise beyond rewrite-conditioned GPT-4.1 passages. | Require separate fresh-write, rewrite, continuation, and style-imitation strata before promoting any lexical or fidelity feature. Treat the preliminary alternatives as unresolved. | pending | not started |
| C14: The authors prefer an inherently interpretable classifier and warn that black-box decisions without trustworthy reasons can contribute to unjustified accusations. | Direct author interpretation and design position. Claims about post-hoc explanation unreliability are inherited from cited work, not measured by DET12. | `STRATEGY.md:14-28` and `process.md:73-77`; **fully covered**. Human-eyes reports inspectable patterns and does not infer who wrote a document. | No gap in the product boundary. The source's classifier framing should not pull the project back toward authorship verdicts. | Retain the existing boundary and evidence-led explanations. Record the source as alignment evidence only; no behaviour change. | pending | not started |
| C15: The evidence is limited to one GPT-4.1 version, one prompt, one narrow classic-fiction corpus, short passages, a 70/15/15 division without a reported work-, author-, or original-rewrite pair-grouping procedure, and manual exploratory analysis of 190 out of 30,302 features without multiple-annotator or agreement reporting. Generated samples are modestly shorter on average, and text length was excluded as an explicit classifier feature. | Direct method facts and source-stated annotation limits. Reviewer inference: because no grouping procedure is reported, work-specific and paired-sample leakage risks remain unresolved. The length difference remains relevant to comparative lexical measures even though length was not a classifier feature. | Source metadata practice and H12/H24/H25 capture some dimensions, but no DET12 reproduction or grouped split exists; **not covered** empirically. | The paper cannot set thresholds or prove cross-domain robustness for human-eyes. | Require pair-grouped, work-held-out, author-held-out, length-matched, contemporary and period fiction, multiple models, multiple prompts, and multiple annotators before any product change based on these features. | pending | not started |
| C16: Figure 2 reports additional Biber-feature directions beyond participles and nominalisations. GPT-4.1 rewrites have higher frequencies for place adverbials, suasive verbs, `though`, gerunds, and indefinite pronouns, while the source passages have higher frequencies for wh-object constructions, pied-piping, discourse particles, that-object constructions, `because`, pro-verb `do`, stranded prepositions, wh-subject constructions, that-verb complements, and analytic negation. | Direct aggregate training-set directions from Figure 2. The figure supplies relative-frequency bars but the prose gives no numeric effect sizes or independent interpretation for these additional labels. The results remain specific to DET12 and its rewrite condition. | H22 and H23 cover structural variation and grammar-feature research broadly; `judgement.json` reviews a few contextual discourse and grammar problems but does not measure these Biber rates. **Not covered** as implemented or validated feature directions. | The project has no agreed mapping from these linguistic labels to prose problems, no direction calibration, and no matched cross-domain evidence. | Record the omitted figure evidence as scoped research context. Any evaluation of these feature directions remains pending Mae's decision and would require clear label definitions, matched human controls, multiple genres, generation tasks, prompts, and models before any product recommendation. | pending | not started |
| C17: Adding n-grams above one token, TF-IDF features, or Biber linguistic features had only a very minor effect on classification accuracy compared with unigrams. | Direct author-reported null comparison, but detailed configurations and accuracy values are not tabulated. It shows little incremental effect in DET12, not that complex features are generally useless. | Human-eyes has no trained-classifier feature-complexity comparison; **not covered**. | The result cannot compare the paper's learned features with human-eyes checks or agent assessments, and it supplies no transferable feature-selection rule. | Preserve the null result. Take no product action unless Mae approves a separate feature-family ablation on human-eyes evaluation data. | pending | not started |

## Recommendations

- C01: Record the classifier metrics only as upstream, corpus-specific evidence; do not present them as human-eyes performance.
- C02: Record the five-pair human result as narrow evaluation context; do not use it to justify automated verdicts.
- C03: Re-evaluate #53 with length-corrected and task-stratified lexical measures before retaining a direction.
- C04: Evaluate contextual over-rephrasing and dialogue attribution within fiction style-fidelity review; do not add a synonym blacklist.
- C05: Evaluate broad participial density separately from the current superficial -ing regex under H23.
- C06: Add nominalisation in creative-fiction rewriting as H23 evidence and test it with actor, genre, and clarity controls.
- C07: Evaluate temporal drift only when the source period or target voice is known.
- C08: Evaluate locale drift as rewrite fidelity, not as an American-English rule.
- C09: Evaluate loss of multilingual and colloquial texture as rewrite fidelity with deliberate-use controls.
- C10: Record the punctuation, case, and letter-frequency null result without changing craft checks.
- C11: Record support for multivariate interpretation without transferring the classifier or ablation threshold.
- C12: Preserve the similarity and null findings as controls; take no current product action.
- C13: Require fresh-write, rewrite, continuation, and style-imitation strata before promoting lexical directions.
- C14: Retain the existing inspectable-evidence and non-authorship boundary; no behaviour change.
- C15: Require grouped splits, broader fiction, multiple models and prompts, and multiple annotators before product adoption.
- C16: Record the additional Figure 2 directions as scoped research context; any feature evaluation remains pending Mae and requires defined labels plus matched cross-condition controls.
- C17: Preserve the minor-effect feature-complexity null; take no product action unless Mae approves a human-eyes feature-family ablation.

## Evaluation of approved changes

- C01: not applicable - pending review; no product change implemented.
- C02: not applicable - pending review; no product change implemented.
- C03: passed - #53 flipped to two-tier windowed lexical diversity (flag 0.71, upper tier 0.74) in commit b199a6d; calibration recorded in dev/evals/ttr-calibration-2026-07-17.md; test_grade.py #53 block passes.
- C04: not applicable - pending review; no product change implemented.
- C05: not applicable - pending review; no product change implemented.
- C06: not applicable - pending review; no product change implemented.
- C07: not applicable - pending review; no product change implemented.
- C08: not applicable - pending review; no product change implemented.
- C09: not applicable - pending review; no product change implemented.
- C10: not applicable - pending review; no product change implemented.
- C11: not applicable - pending review; no product change implemented.
- C12: not applicable - pending review; no product change implemented.
- C13: not applicable - pending review; no product change implemented.
- C14: not applicable - pending review; no product change implemented.
- C15: not applicable - pending review; no product change implemented.
- C16: not applicable - pending review; no product change implemented.
- C17: not applicable - pending review; no product change implemented.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: Codex CLI fresh process, did not perform the extraction
- **Findings resolved:** completed C12's Figure 1 null-feature inventory and qualified the plot as the ten smallest class differences rather than proof of equivalence
- **Unresolved findings:** none
