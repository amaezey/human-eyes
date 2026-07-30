# Kobak et al.: Delving into LLM-assisted writing in biomedical publications through excess vocabulary

## Metadata

- **URL:** https://doi.org/10.1126/sciadv.adt3813
- **Author / owner:** Dmitry Kobak, Rita González-Márquez, Emőke-Ágnes Horvát, and Jan Lause
- **Published:** 2025-07-02 online; Science Advances 11(27), 2025-07-04
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** peer-reviewed corpus study
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** DOI 10.1126/sciadv.adt3813
- **Version / revision:** current peer-reviewed Science Advances version, PMCID PMC12219543; previous snapshot retrieved 2026-05-05
- **Full-text status:** complete
- **Snapshot:** `snapshots/kobak-llm-excess-vocabulary.md`
- **Extraction method:** PMC HTML article body checked against Europe PMC JATS XML; 16-page supplementary PDF extracted with pdftotext and preserved with five main figure images
- **Snapshot SHA-256:** `f537bcadb8a80388aaf30fbeeb1327d34f3ee559f6c8852e075a515471483f3c`
- **Model / corpus scope:** no named LLM family or version; 15,103,888 complete English PubMed abstracts from 2010-2024, each 250-4000 characters, analysed at corpus and subcorpus level against 2021-2022 frequency trends
- **Access limitations:** none for substantive material; direct PMC PDF links returned a JavaScript proof-of-work page, but complete HTML/JATS text, the complete supplementary PDF, five main figures, and linked code/data routes were accessible

## Summary

This peer-reviewed corpus study measures abrupt post-ChatGPT changes in word occurrence across 15.1 million English biomedical abstracts. Its excess-frequency method uses historical counterfactuals rather than labelled human and LLM text, identifies a 2024 shift dominated by style words, and estimates a 13.5% lower bound for abstracts processed with LLMs. It supports time-bound, biomedical-register vocabulary monitoring at corpus scale. It does not identify individual abstracts, distinguish model families, separate direct LLM assistance from later human adoption of LLM-preferred vocabulary, or validate human-eyes' document-level density thresholds.

## Main insights

- The direct method measures annual abstract-level word occurrence against a conservative 2021-2022 extrapolation. It does not train on prompted LLM samples or use a black-box detector.
- The main corpus has 15,103,888 English PubMed abstracts from 2010-2024 after length, language, contamination, correction, and retraction-notice filtering.
- In 2024, 454 word forms, or 343 unique lemmas, crossed the study's excess thresholds. The analogous 2021 COVID peak was 190 forms or 180 lemmas.
- The 2024 excess set was dominated by style words. The direct examples include rare high-ratio forms such as `delves`, `underscores`, and `showcasing`, and common high-gap words such as `potential`, `findings`, and `crucial`.
- Two nonoverlapping marker sets gave similar corpus-level lower bounds: 291 rare style words gave 13.6%, while ten manually selected common words gave 13.4%; the authors averaged them to 13.5%.
- A four-word 2021 COVID content set had a 0.069 gap. The authors call the 0.135 LLM-associated gap at least twice the peak COVID-literature share, while the displayed rounded values imply about 1.96 times. They extrapolate the 13.5% lower bound to at least about 200,000 PubMed papers per year from a roughly 1.5-million-paper annual flow; that is a derived estimate, not an observed document count.
- The result is heterogeneous by field, affiliation country, journal, and intersections, but those differences can reflect editing behaviour, publication lag, or detectability as well as adoption.
- The authors speculate that true use may be nearer their highest subgroup lower bounds above 30% and expect lower bounds to rise after more publication cycles. Those are interpretations, not measured overall rates.
- The study explicitly cannot identify individual LLM-processed abstracts, infer authorship, distinguish LLM families, or separate direct use from diffusion of LLM-preferred vocabulary into human writing.
- The three real-abstract passages in the Discussion illustrate the observed style but are not validated single-document classifications.
- The 900-row repository CSV is a union of excess words from 2013-2024. It has no year column. Human-eyes loads 414 style-labelled terms after exclusions, whereas the paper reports 379 excess style words specifically for 2024.
- Focused inspection shows the live aggregate check can fail from vocabulary points alone or structural points alone, contrary to generated documentation saying vocabulary and structural signals are both required. Neither the paper nor its dataset validates the live document thresholds.

## Evidence and claims to extract

- **Direct source reviewed:** the peer-reviewed Science Advances article at DOI 10.1126/sciadv.adt3813, complete PMC/Europe PMC full text, all five main figures and captions, the complete 16-page Supplementary Materials with figures S1-S7 and references, and the linked repository/data record needed to verify the bundled CSV
- **Method and sample:** 15,103,888 complete English abstracts dated 2010-2024 from the early-2025 PubMed baseline, restricted to 250-4000 characters; binary occurrence matrix over 273,112 four-or-more-letter alphabetic word forms; main analysis over 26,657 words above 0.0001 frequency in both 2023 and 2024; conservative extrapolation from 2021-2022
- **Direct versus cited evidence:** C01-C16 and C18 are direct article or supplement evidence; C17 separates the paper's own proposed future use from demonstrated scope; C19 is direct repository/data provenance checked against the project file; C20-C22 are this review's live-project comparisons, not paper findings. Claims about LLM benefits, factual errors, bias, plagiarism, diversity, policy, and spoken-language transfer in the Discussion are cited context rather than findings measured by this study.
- **Important limits and counterexamples:** historical content-word spikes such as Ebola, Zika, and COVID show that abrupt vocabulary change need not be an LLM signal; the method is corpus-level, cannot assign individual abstracts, may miss careful editing, cannot separate models or human lexical uptake, uses approximate first-name gender inference for only 55% of authors, and has no demonstrated threshold for arbitrary documents or non-biomedical genres

## Matched patterns / rules

- B1 `no-ai-vocabulary-clustering`: related vocabulary guidance, but this check uses the local generic and GPTZero lists rather than the Kobak CSV.
- `overall-signal-stacking`: loads Kobak style-labelled terms and applies document-level distinct-count and density thresholds in `human-eyes/scripts/grade.py`.
- `human-eyes/references/kobak-excess-words.csv`: byte-identical to upstream `results/excess_words.csv` at repository head `53db991afc251782106cd817a1c3fa47a4d41781`; that data file last changed at commit `3345a2eea967ecc14e5d5f7b56c8249c65c82257` on 2025-02-12.
- `human-eyes/references/patterns.md` and `human-eyes/scripts/patterns.json`: state the corpus-level and no-single-word boundary, but overstate the live aggregate's vocabulary-plus-structure conjunction.
- Product boundary and `human-eyes/references/process.md`: correctly prohibit authorship inference.

## Associated hypotheses

- H1 Continuous calibrated register-distance score per pattern
- H3 Drop detection framing entirely
- H7 Five-check gating grader plus advisory catalogue
- H12 Genre-aware threshold calibration
- H24 Register-specific vocabulary density
- H25 Model-family versus generic-AI residue
