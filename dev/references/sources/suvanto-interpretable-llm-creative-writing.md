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

This accepted ICAART 2026 paper studies why simple classifiers distinguish GPT-4.1 rewrites from source passages in classic British detective fiction. Its linear unigram classifier reaches 0.9814 test accuracy while 119 human evaluators score 0.499 on five paired examples. The paper attributes the machine result to many small lexical differences, especially greater synonym variety, plus modernisation, Americanisms, and removal of foreign-language and colloquial material. It materially challenges human-eyes pattern B5 because that live check treats low vocabulary diversity as the suspicious direction, while this rewrite corpus finds higher generated-text entropy. The work does not establish a general authorship rule: it uses one model, one rewrite prompt, one narrow period and genre, divides a twelve-work corpus without reporting work, author, or original-rewrite pair grouping, and manually explores 190 selected features without multiple-annotator or agreement reporting. The user queue title, "Interpretable Text Classification for LLM-generated Creative Writing", omits "Applied to the Detection of" from the actual title at the authoritative URL.

## Main insights

- Five unigram classifiers reach 0.9310 to 0.9814 test accuracy on held-out passages from the same DET12 corpus, while human pairwise classification is at chance.
- The strongest project-relevant result is directional: GPT-4.1 rewrites have higher unigram entropy and greater synonym variety than the human originals. This supports manual review of over-rephrasing but contradicts B5's one-way low-diversity framing.
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

## Matched patterns / rules

- synonym cycling: no live record, former #11 removed 2026-07-25 through DR-156
- B5 vocabulary diversity in `human-eyes/scripts/grade.py:2034` and `human-eyes/references/patterns.md:399`
- A3 superficial -ing analysis in `human-eyes/scripts/grade.py:1453` and `human-eyes/references/patterns.md:85`
- H3 tonal uniformity as weak adjacent register coverage in `human-eyes/scripts/judgement.json`
- H10 fiction branch in `human-eyes/scripts/judgement.json:253`
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
