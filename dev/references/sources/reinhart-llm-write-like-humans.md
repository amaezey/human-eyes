# Reinhart et al.: Do LLMs write like humans?

## Metadata

- **URL:** https://doi.org/10.1073/pnas.2422455122
- **Author / owner:** Alex Reinhart, Ben Markey, Michael Laudenbach, Kachatad Pantusen, Ronald Yurko, Gordon Weinberg, and David West Brown
- **Published:** 2025-02-18 online; PNAS issue date 2025-02-25
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** peer-reviewed empirical corpus study
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** DOI 10.1073/pnas.2422455122; PMCID PMC11874169; no PMID found
- **Version / revision:** PNAS version of record, volume 122, issue 8, e2422455122, six-page article plus 22-page Supporting Information; compared with arXiv:2410.16107v2 and the prior 2026-05-05 web-page capture
- **Full-text status:** complete
- **Snapshot:** `snapshots/reinhart-llm-write-like-humans.md`
- **Extraction method:** complete publisher-version main and Supporting Information PDFs downloaded from PubMed Central, converted from embedded text layers with Poppler `pdftotext -layout`, checked with `pdfinfo`, and compared with rendered beginning, middle, and end pages; PMC HTML and Europe PMC XML used for identity and structure cross-checks
- **Snapshot SHA-256:** `b6712fb0f226139db0d0e8660c5af97d10923e9a3b39fc40232700296e37c9e0`
- **Model / corpus scope:** English continuations of roughly 500 words generated in 2024 from roughly 500-word human prompts; GPT-4o `2024-08-06`, GPT-4o Mini `2024-07-18`, Llama 3 8B, Llama 3 70B, Llama 3 8B Instruct, and Llama 3 70B Instruct; HAP-E spans academic, blog, fiction, news, spoken, and TV/movie-script material, while CAP spans eight COCA registers; final complete-case samples contain 8,290 HAP-E and 9,615 CAP prompt documents, eight chunks per document
- **Access limitations:** none for the six-page article, four figures, Table 1, footnote, 35 references, 22-page Supporting Information, Fig. S1, Tables S1-S12, or 24 SI references; raw corpora, parsed features, and analysis code are linked but were not recursively ingested, and several HAP-E source corpora are only described at category level in the paper

## Summary

This study compares matched human continuations with six LLM continuations across two large, multi-register English corpora. It measures 66 Biber lexical, grammatical, and rhetorical features, vocabulary frequencies, and classifier performance. In these 2024 models and prompts, instruction-tuned GPT-4o and Llama 3 variants diverged more from human register variation than Llama 3 base models: they overused several clause and noun-phrase features, showed strong model-specific vocabulary preferences, and were easier to separate from human continuations within the study corpora. The external GPT-3.5/arXiv test sharply reduced accuracy, the authors explicitly reject using this work to police student authorship, and the design supplies no safe document-level threshold. For human-eyes, the paper is strong aggregate evidence for testing register- and model-specific structural features and vocabulary density. It only partly covers live B1, challenges the claim that A3 detects the paper's present-participial construction, and does not directly support G9 sentence-length variance.

## Main insights

- The final complete-case datasets contain 8,290 HAP-E and 9,615 CAP prompt documents. Each contributes two human chunks and six LLM chunks, for 66,320 and 76,920 roughly 500-word chunks respectively.
- GPT-4o used present participial clauses 5.3 times as often as paired human continuations, “that” clauses as subject 2.6 times as often, nominalizations 2.1 times as often, and phrasal coordination 1.9 times as often. The corresponding paired Cohen's d values were 1.38, 0.77, 1.23, and 0.81.
- Direction and magnitude vary by model and feature. GPT-4o models used less clausal coordination while all Llama 3 variants used more; GPT-4o models used more downtoners while all Llama variants used fewer. Llama base models often stayed nearer the paired human rate.
- Larger paired models were not consistently more human-like than smaller ones. In the Llama comparison, instruction-tuned variants diverged more than base variants, but the undisclosed tuning processes prevent a precise causal account and no untuned GPT control exists.
- GPT-4o and GPT-4o Mini used several words more than 100 times as often as paired human continuations. `tapestry` appeared in 23% and 24% of their outputs, and `amidst` in 27% of both. The authors stress that humans use these words and that conspicuousness depends on genre.
- Vocabulary is model-specific. The instruction-tuned Llama variants share some preferences with GPT-4o at lower rates, while the base Llama lists include names and corpus-specific tokens. Some extreme ratios arise from generation artifacts or a single repeating document.
- A seven-class random forest reached 66% accuracy against 14% chance on the HAP-E holdout, with 4.2% of LLM texts labelled human and 9.8% of human texts labelled LLM. Most errors confused sizes of the same model family.
- Pairwise human-versus-one-model random forests transferred between HAP-E and CAP at 89.1% to 98.4% accuracy. Lasso models were above 90% for instruction-tuned systems but about 73% to 75% for Llama base systems.
- On M4 arXiv abstracts generated by a different model and task, random-forest accuracy fell to 57.95% to 70.68% for instruction-tuned models and roughly 51% for Llama base models. The paper concludes that generalization across models or registers is difficult.
- The authors use classification to describe writing differences, not to propose a detector. They argue for expert, genre-aware revision and against policing students; their learner and productivity discussion is interpretation rather than a tested intervention.
- Supporting Information Table S2 literally prints `5550,463` for the HAP-E academic word count of Llama 3 8B Instruct, while the row total and arithmetic require `550,463`. The typo is preserved and must not be treated as a measured 5.55-million-word cell.

## Evidence and claims to extract

- **Direct source reviewed:** complete PNAS version-of-record article for DOI 10.1073/pnas.2422455122 and its complete Supporting Information, preserved as final PDFs and full Poppler text extractions; PMC HTML, Europe PMC XML, and arXiv v2 were used for identity and version comparison only.
- **Method and sample:** two corpora each began from 12,000 English documents. A roughly 500-word first chunk prompted six models to continue for roughly 500 words, and each continuation was paired with the next human chunk. Responses under 100 words, refusals, and nonsense outputs caused the entire prompt set to be removed from the complete-case analysis. HAP-E retained 8,290 documents across six genres; CAP retained 9,615 across eight COCA registers. Features were counted per 1,000 words with `pseudobibeR`; paired Wilcoxon tests used Bonferroni correction; paired Cohen's d, random forests, lasso logistic regression, cross-corpus tests, and an external M4/arXiv test were reported.
- **Direct versus cited evidence:** C01-C17 and C19-C22 are direct methods, results, source limitations, author interpretations, or record-integrity findings from the article and supplement. C18 separates claims inherited from cited studies. None of the cited studies was promoted through this card without its own direct review.
- **Important limits and counterexamples:** only English roughly 500-word continuations and six dated 2024 models were generated; no untuned GPT comparison exists; default GPT settings and one fixed instruction prompt limit prompt generality; refusals and short outputs were complete-case exclusions; COCA removes 10 words per 200 for licensing, which can damage parsing; HAP-E construction draws from heterogeneous corpora, including OCR-converted scripts; feature counts depend on dependency parsing and `pseudobibeR`; reported classifiers are closed-task descriptive models without subgroup fairness, calibration, or authorship-decision analysis; external transfer falls sharply; larger models do not eliminate the differences; human prose contains the named words and structures; author pedagogy and productivity claims were not intervention-tested; Table S2 has an internal numeric typo; and Table S4's 66-row feature inventory disagrees with the 66 result rows in Tables S5-S6 on type-token ratio versus time adverbials.

## Matched patterns / rules

- A3 `no-superficial-ing`: the implementation matches a closed list of comma-led trailing verbs such as `highlighting`, `reflecting`, and `ensuring`. It does not parse present-participial clauses and returned clear on the paper's exact `leaning ... evading ...` example. The source measures grammatical frequency, not superficiality or information content, so coverage is only adjacent and current README support is overstated.
- B1 `no-ai-vocabulary-clustering`: partly covered. The live list contains `intricate`, `tapestry`, `vibrant`, and `unspoken`; a focused four-paragraph surface-only run flagged a synthetic paragraph containing those four. It does not contain source-high words including `amidst`, `camaraderie`, `palpable`, `fleeting`, `solace`, `unravel`, `cacophony`, `unease`, and `reminder`, and its three-per-paragraph threshold is not evaluated by this paper.
- H3 `tonal_uniformity` and H10 `genre_specific`: conceptually cover register lock and genre misfit, but the live assessments are qualitative. They do not measure Biber-feature distance or preserve model/date baselines.
- G9 `sentence-length-variance` and B5 `vocabulary-diversity`: inspected implementations measure sentence-word-count standard deviation and punctuation-stripped document type-token ratio. The paper does not measure sentence-length variance. Its supplement lists punctuation-inclusive type-token ratio among the 66 intended Biber features, but the visible Tables S5-S6 report no TTR row, effect, or threshold. Neither live check is directly validated.
- H12 `Genre-aware threshold calibration`, H23 `Nominalization and noun-heavy style`, H24 `Register-specific vocabulary density`, and H25 `Model-family versus generic-AI residue`: directly relevant open evaluation paths; none is implemented by this source review.
- `human-eyes/references/process.md` product boundary: aligned with the authors' explicit statement that their aim is description and revision, not a detector or student policing.
- `pattern-opportunities.md` row `Nominalization and noun-heavy style`: relevant but currently overstates A3 as covering present-participial clauses and lacks the source's model, effect-size, external-transfer, and no-threshold qualifications.

## Associated hypotheses

- H12: Genre-aware threshold calibration.
- H23: Nominalization and noun-heavy style.
- H24: Register-specific vocabulary density.
- H25: Model-family versus generic-AI residue.
- H3: Drop detection framing entirely, supported only as product-boundary context by the paper's explicit non-detector aim and external-transfer limits.
