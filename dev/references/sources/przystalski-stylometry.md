# Przystalski et al.: Stylometry recognizes human and LLM-generated texts in short samples

## Metadata

- **URL:** https://doi.org/10.1016/j.eswa.2025.129001
- **Author / owner:** Karol Przystalski, Jan K. Argasiński, Iwona Grabska-Gradzińska, and Jeremi K. Ochab
- **Published:** arXiv v1 submitted 2025-07-01; arXiv v2 revised 2025-07-15; Expert Systems with Applications 296 (January 2026), article 129001
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** peer-reviewed empirical study; complete arXiv accepted manuscript plus linked data/code repository
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** DOI 10.1016/j.eswa.2025.129001; arXiv:2507.00838v2; supporting OSF DOI 10.17605/OSF.IO/DFZ6K; linked repository commit a3f819d65b340985ca411142e52cb36dabd3783b
- **Version / revision:** current review: complete 19-page arXiv v2 accepted manuscript; prior record: arXiv v2 abstract-page wrapper only
- **Full-text status:** complete
- **Snapshot:** `snapshots/przystalski-stylometry.md`
- **Extraction method:** official arXiv v2 PDF downloaded with curl; 19 embedded-text pages extracted with Poppler pdftotext; pdfinfo, pdfimages, and rendered pages 1, 10, 12, and 19 checked; complete linked GitHub tree cloned and archived at commit a3f819d65b340985ca411142e52cb36dabd3783b
- **Snapshot SHA-256:** `540072d204aa1bb3dd91578feecc3d3498b5538db92ebe81a820faf6d700268d`
- **Model / corpus scope:** 2,439 English term descriptions drawn from Simple English Wikipedia 20220301 and Wikipedia-API; two 10-sentence prompt forms; GPT-3.5-turbo, GPT-4, LLaMA 2 7B, LLaMA 3 8B, Orca 8B, and Falcon 11B as reported in the manuscript, with the repository instead naming an Orca 13B file; Gensim, Sumy, T5, and BART summaries; DIPPER 11B and Parrot/T5 paraphrases; 10-fold topic-grouped evaluation; exact API model snapshots and generation dates are not reported. The cross-domain AuTexTification experiment uses roughly 28,000 English human and 28,000 machine texts from BLOOM and GPT-3 models, but the manuscript's BLOOM-1B7 prose versus BLOOM-1B1 table label and its train/test-domain ordering are internally inconsistent.
- **Access limitations:** The complete arXiv v2 manuscript is authoritative for this review. The Elsevier text-mining endpoint returned HTTP 400 without an API key and the direct ScienceDirect PDF route returned HTTP 403. OSF metadata and the complete 82-file inventory were accessible, but later file downloads returned intermittent HTTP 403/502; the complete linked GitHub repository was preserved instead. No claim relies on an incomplete OSF download.

## Summary

This study trains decision trees and LightGBM classifiers on interpretable stylometric features to separate English Wikipedia introductions from six families of prompted model output and to attribute output within that closed seven-class set. The strongest in-domain results are high, but the complete paper materially narrows the earlier abstract-only record: cross-domain macro-F1 falls below a logistic-regression baseline, unseen GPT-4 and LLaMA 3 recall drops, the multiclass task is closed-set, mixed human/AI text is excluded, and many important features encode topic, preprocessing, truncation, or model-specific artefacts. The paper supports source-bound feature comparison and robustness research, not universal prose thresholds or authorship verdicts.

## Main insights

- The direct experiment is a supervised, topic-grouped classification study of one English encyclopaedic task, not a validation of generic human-versus-AI prose rules.
- Frequency features outperform the 196-feature StyloMetrix set in the seven-class experiment (MCC 0.87 versus 0.72), while the multi-domain AuTexTification test reverses the headline: macro-F1 is 0.54 and 0.48, below the 0.66 logistic-regression baseline and 0.81 top system.
- High in-domain accuracy coexists with model confusion, open-set limits, prompt/model drift, missing mixed-text evaluation, and recall-only robustness tests that cannot measure false positives.
- SHAP explanations identify model- and corpus-specific differences: Wikipedia has more dates and proper nouns; GPT-4 overuses `significant`, `notable`, and `despite` in this task; LLaMA 2 contains whitespace artefacts; and GPT grammar-feature distributions are more standardised than the multi-author Wikipedia comparison.
- Type-token ratio is important to one multiclass model, but the paper gives no universal direction or threshold. A focused live-project run on all 17,073 rows in the released prompt-1 Wikipedia/model file set found the current low-TTR rule almost never fires and flags more human rows than several model sets; the second prompt-specific set was not run.
- The paper itself says detection does not imply that a text is malicious or untrustworthy and does not cover mixed human/AI texts.
- The authors disclose GPT and Writefull use for readability, style, and grammar, followed by author review and editing.

## Evidence and claims to extract

- **Direct source reviewed:** complete 19-page arXiv v2 accepted manuscript, its 11 tables, 6 figures/captions, references, disclosure, and the complete 75-file linked GitHub repository at commit a3f819d65b340985ca411142e52cb36dabd3783b.
- **Method and sample:** English Wikipedia introductions and six model families under two prompts; tree models over 196 StyloMetrix or 3,000 frequency features; topic-grouped 10-fold cross-validation; unseen-model, single-pass paraphrase, cross-domain, summariser, and two commercial-detector comparisons.
- **Direct versus cited evidence:** C01-C22 and C24 are direct paper, released-repository, or live-project comparisons. C23 separates literature-review statements from this study's measurements. C25 records author-proposed future work rather than a demonstrated result.
- **Important limits and counterexamples:** single English encyclopaedic domain; multi-author and differently edited human comparison; prompt and model snapshots underreported; 2,439/2,424 sample-count inconsistency; manuscript Orca 8B versus repository Orca 13B conflict; paper/repository prompt mismatch; repository generation path visibly selects only 1,000 terms, contains no LLaMA 3 or second-prompt generation path, and has an undefined GPT prompt variable on a fresh linear run; 70/30 versus grouped-10-fold description tension; repository lacks named setup/config files; no mixed-text or open-set multiclass evaluation; cross-domain scores below baseline and ambiguous train/test-domain ordering; recall-only attack tests; commercial random samples have no seed or detector build.

## Matched patterns / rules

- B1 `no-ai-vocabulary-clustering`: partly covered only as a candidate lexical-family comparison; the paper's three named GPT-4 words are model/task-specific and are not direct validation of the live clustering list or threshold.
- G9 `sentence-length-variance`: partly covered by the released corpus and H22, but not by the paper's grammatical-standardisation result, which concerns distributions of POS n-grams across samples rather than within-document sentence-length SD.
- B5 `vocabulary-diversity`: partly covered as a feature-family reference and challenged as a directional rule; type-token ratio appears among model features without a universal low-is-AI direction or threshold.
- Product boundary in `human-eyes/references/process.md` and `dev/TESTING.md`: fully covered; both already forbid authorship claims and require genre-/register-aware comparative evidence.

## Associated hypotheses

- H1 continuous calibrated register-distance score: source supports comparison and calibration framing, not a deployable score.
- H2 comparison-engine product reframe: source supports matched-reference comparison and non-universal interpretation.
- H12 genre-aware threshold calibration: directly supported by the cross-domain failure and single-domain limitation.
- H22 long-tail compression and grammatical standardisation: directly informed, but the current G9 statistic is not the measured construct.
- H24 register-specific vocabulary density: directly informed by model/task-specific word and TTR features.
- H25 model-family versus generic-AI residue: directly informed by model-specific confusions and explanations.
