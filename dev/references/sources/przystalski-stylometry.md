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

## Skill-use audit

- **Good use:** source-bound evaluation of interpretable lexical, POS, dependency, morphology, punctuation, and function-word features; evidence for H12/H22/H24/H25 robustness and calibration work; a concrete warning that in-domain headline scores can hide domain and model transfer failures.
- **Misuse / overclaim:** treating a word, type-token ratio, sentence-length statistic, SHAP feature, or classifier score as proof of who wrote a document; applying the paper's thresholds to fiction, email, student work, journalism, another language, mixed-authorship text, or an unseen open set.
- **Unsupported use:** adding bare `significant`, `notable`, or `despite` to a universal blacklist; treating G9 sentence-length SD as the paper's grammatical-standardisation measure; treating B5's low-TTR direction or 0.40 threshold as source-validated.
- **Underused evidence:** the severe cross-domain drop, one-class robustness-test design, sample/protocol inconsistencies, multi-author human baseline, and separation of machine-generation detection from trustworthiness or malice.
- **Patterns left on the table:** POS-n-gram distribution tails, domain/model/prompt factorial evaluation, and explanation stability are credible research candidates, but they need matched controls before any product rule.

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

## Questions / follow-up

- Can the preserved dataset support a preregistered, length-matched comparison of B1, G9, B5, POS-n-gram dispersion, and false positives without tuning on the same rows?
- Which exact dated GPT-3.5/GPT-4 API snapshots and open-model files generated the corpus? The paper and released repository do not fully answer this.
- Can the OSF analysis tree be preserved later through a stable complete archive route, and does it resolve the paper/repository prompt and split-description discrepancies?
- No product change should proceed until Mae decides whether to add this source to a separate robustness lane.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | arXiv:2507.00838v2 abstract-page wrapper; no digest was recorded in the old card or manifest | `snapshots/archive/przystalski-stylometry/2026-05-05-35f81903.md` | 2026-05-05 | `35f81903d5f75049f8430fd6a8ff8b71029b0c46488245fddaa5de249258b8af` |
| current | DOI 10.1016/j.eswa.2025.129001; arXiv:2507.00838v2; supporting OSF DOI 10.17605/OSF.IO/DFZ6K; linked repository commit a3f819d65b340985ca411142e52cb36dabd3783b | `snapshots/przystalski-stylometry.md` | 2026-07-17 | `540072d204aa1bb3dd91578feecc3d3498b5538db92ebe81a820faf6d700268d` |

The prior snapshot's computed digest matches both the archived bytes and the pre-refresh working-tree bytes. The prior manifest recorded no digest to compare. The update replaces an abstract-page wrapper with the complete accepted manuscript and complete linked GitHub tree; it adds methods, all results, nulls, robustness failures, source-code limitations, disclosure, and references. The title, authors, arXiv identifier, abstract figures, and journal DOI remain unchanged.

## Decision history

- DR-88 closed 2026-07-26: the low-TTR direction this claim questions was reversed by DR-06; B5 flags high windowed lexical diversity. Verified against the live checker; no check changed.

- 2026-07-17: Mae approved and implemented the B5 direction flip: windowed 150-word lexical diversity flagging high values, two-tier (0.71 flag, 0.74 above-observed-human-range note), commit b199a6d.
- The prior 2026-05-05 card had no claim IDs, user decisions, implementation statuses, or evaluation records. Its broad H1/H2/B1/G9/B5 associations are reopened as C01-C25 below; none is carried forward as approved or implemented.
- C24 approved 2026-07-17: flip B5's direction; implementation is pending a plan, so the status stays `not started`. Recorded on C24 because its live run specifically challenges B5's low-TTR direction. C05 was named in the decision batch but records StyloMetrix feature families rather than TTR direction or eligibility, so it stays pending.

- C14 approved 2026-07-18 via DR-125: B1 now recognises `significant`, `notable`, and `despite` as clustering candidates under the existing paragraph threshold.

## Project coverage

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: The study compares 2,439 English Wikipedia term descriptions with six prompted model families and four summarisation methods in a narrowly defined encyclopaedic task. | Direct dataset/method claim; 2,439 rows are present in each preserved principal CSV; genre, language, task, and prompt are tightly bounded. | H2 and H12; partly covered as comparison and genre-calibration framing. | No source-bound dataset lane currently records these exact conditions. | Record the study as narrow matched-task evidence; do not generalise its scores or feature directions. | pending | not started |
| C02: The paper also says preprocessing resulted in 2,424 terms, conflicting with its 2,439 final count, the 2,439-row released files, and fold sizes based on 2,439 topics. | Direct internal counterexample; released data and 4,878/17,073 binary/multiclass totals support 2,439. | `dev/TESTING.md` provenance and report-completeness rules; partly covered. | Source cards previously omitted the count conflict. | Preserve the discrepancy as evaluation-hygiene evidence; do not silently choose 2,424. | pending | not started |
| C03: Six model families were generated at stated temperature 0.7 with two 10-sentence prompts, but exact API snapshots/dates are missing. The manuscript reports Orca 8B, while `notebooks/get_data.ipynb` names an Orca 13B file; its prompt text and duplicated system/user placement differ from the quoted prompts, it has no LLaMA 3 or second-prompt generation path, its visible path selects only 1,000 terms with `random.choices`, and its GPT cell records `prompt` even though that variable is undefined in a fresh linear run. | Direct paper plus complete repository comparison; versions are only family/product labels except some open-model filenames. | H25 and comparison-corpus provenance requirements; partly covered. | The notebook does not reproduce the released 2,439-topic, two-prompt corpus, and no mapping ties every row to exact model build, generation date, prompt form, and seed. | Treat model fingerprints as dated candidates only; require exact generation provenance before reuse. | pending | not started |
| C04: Gensim, Sumy, T5, and BART summaries differ sharply in length; T5 has repeated-letter/word/full-stop failures, BART is short, Gensim is longer-sentence, and Sumy is flexible. | Direct Table 1 and discussion; artefacts are method-specific, not generic LLM findings. | No active product rule; not covered. | Summariser artefacts can dominate classifier features. | Record only; do not promote summariser failures into prose rules. | pending | not started |
| C05: StyloMetrix supplies grammatical, lexical, syntactic, punctuation, POS, and text-statistic features; the frequency pipeline uses lemma, POS, dependency, and morphology n-grams. | Direct method claim; the paper says 195 features while Table 6 reports 196. | B1, G9, B5 and H22-H25 cover only small subsets; partly covered. | Human-eyes does not implement POS/dependency/morphology distribution comparison, and the source does not validate universal thresholds. | Keep these as candidate research families; require matched controls and incremental-value tests. | pending | not started |
| C06: Decision trees and LGBM use cross-validation, with topic-grouped folds intended to prevent the same term entering train and test; the prose also mentions a 70/30 split while reported grouped fold sizes imply 90/10. | Direct method plus repository inspection; released notebooks use GroupKFold but depend on absent external feature/config paths. | `dev/TESTING.md` requires explicit immutable protocols; partly covered. | Split description and released reproduction path are not fully reconciled. | Record the protocol tension and avoid calling the release fully reproducible. | pending | not started |
| C07: Four-feature decision trees range from near chance for some model pairs to high accuracy for others; most binary model-pair recognitions are 70-85%. | Direct Table 4 and Results; near-chance failures are material counterexamples. | H25; partly covered as model-family residue. | Prior abstract-only card retained only headline maxima. | Preserve the failures with the successes; take no product action. | pending | not started |
| C08: LGBM binary accuracy spans 0.77-1.00 with StyloMetrix and 0.79-1.00 with frequency features; Wikipedia versus GPT-4 reaches 0.94 and 0.98 respectively. | Direct balanced, topic-grouped in-domain results; accuracy is not calibration or open-set performance. | No classifier in human-eyes; not covered as product behaviour. | No uncertainty intervals, external human false-positive analysis, or probability calibration. | Record as source-bound benchmark context only. | pending | not started |
| C09: Seven-class MCC is 0.72 for 196 StyloMetrix features and 0.87 for 3,000 frequency features. | Direct Table 6; closed-set attribution of known classes. | H25; partly covered as research framing. | Human-eyes does not perform model attribution and must not inherit the closed-set score. | Do not promote to an authorship or model-family verdict. | pending | not started |
| C10: Wikipedia is the best-recognised class; GPT-4 is most often confused with Wikipedia; LLaMA 2/Orca and GPT-family/LLaMA 3 confusions vary by feature set. For the paper's local `The Swarbriggs` example, Wikipedia is classified correctly, GPT-4 is misclassified as Wikipedia, and LLaMA 2 as Orca. | Direct aggregate confusion matrices plus a direct local counterexample; model-specific, prompt-specific, and closed-set. | H25; partly covered. | No open-set rejection or current-model replication; the local examples demonstrate concrete failure modes rather than aggregate rates. | Record model confusions and local failures with date/version limits; no active rule. | pending | not started |
| C11: Leaving one model out reduces test recall most for GPT-4 (88.2%) and LLaMA 3 (94.13%), while the other unseen-model recalls are above 99%. | Direct Table 8; test contains only machine text and reports recall, so it cannot measure human false positives. | Factorial robustness candidates in `pattern-opportunities.md` and H25; partly covered. | No two-class unseen evaluation, precision, specificity, or confidence intervals across regenerated corpora. | Add only to a future separate robustness protocol, pending Mae's decision. | pending | not started |
| C12: Single-pass DIPPER and Parrot paraphrases are detected at 98.81-99.996% recall and usually outperform unparaphrased validation recall. | Direct Table 8; no recursive attack, human paraphrase control, false-positive metric, or attack examples in training; DIPPER quality percentages are cited, not measured here. | Separate coached/adversarial lane proposed in `pattern-opportunities.md`; partly covered. | Recall-only design cannot establish robust authorship classification. | Record as attack-specific evidence; do not infer detector robustness generally. | pending | not started |
| C13: On the English AuTexTification benchmark of roughly 28,000 human and 28,000 machine texts generated by BLOOM and GPT-3 variants, macro-F1 is 0.48 for StyloMetrix and 0.54 for frequency features, below the 0.66 logistic-regression baseline and 0.81 top system. The manuscript names BLOOM-1B7/3B/7B1 and GPT-3 `babbage`, `curie`, and `text-davinci-003` in prose but Table 3 labels the first BLOOM model `BLOOM-1B1`; its prose lists `tweets, how-to, legal, reviews, news` and says the first three are training domains, while Table 3 orders them `tweets, how-to, news, legal, reviews`. | Direct cross-domain benchmark, material generator/domain-accounting ambiguity, and strongest null/challenge in the paper. | H12 and factorial robustness lane; fully covered as a pending evaluation concern, not implemented. | Prior card omitted the cross-domain failure and the manuscript does not reconcile its first BLOOM label or domain ordering. | Use this result to block generic transfer of in-domain feature scores or thresholds; do not claim an exact generator set or train/test-domain split without clarification. | pending | not started |
| C14: In the GPT-4/Wikipedia comparison, GPT-4 uses `significant`, `notable`, and `despite` more heavily. | Direct SHAP/example interpretation for one model, prompt family, and domain; no bare-word effect size, specificity, or universal threshold. | B1 now recognises `significant`, `notable`, and `despite` as exact clustering candidates. | The runtime surfaces paragraph-level use without reproducing the source's model/task comparison. | Add all three exact words to B1 under the existing paragraph threshold. | approved | implemented |
| C15: GPT-4 POS n-gram feature distributions are more standardised than Wikipedia's long-tailed distributions; explanations are model-dependent. | Direct Figure 1 and discussion; across-sample grammatical-feature distributions, not within-document sentence-length variance. | H22 directly names this candidate; G9 measures within-document sentence-word-count SD only. Hypothesis fully covered; executable construct not covered. | Current G9 cannot claim to implement grammatical standardisation. | Test POS/clause-shape tails separately from G9 before any mapping or threshold change. | pending | not started |
| C16: Proper names, dates, punctuation, full stops, whitespace, truncation, and preprocessing artefacts are important features; punctuation was excluded from one pipeline because of artefacts. | Direct SHAP and discussion; includes human encyclopaedic content and model/preprocessing residue. | B1/G9/B5 do not represent these artefact boundaries; not covered. | Feature importance may encode dataset construction rather than stable writing style. | Record as a confound and require artefact ablations in any reuse. | pending | not started |
| C17: Decision-tree summariser/model comparisons span about 0.69-0.98; BART and T5 artefacts help recognition, and the authors infer but do not run similar LGBM results. | Direct Table 10 plus author interpretation; the LGBM extension is untested. | No product coverage. | Earlier card did not distinguish measured decision-tree results from inferred LGBM performance. | Record measured and inferred statements separately; no product change. | pending | not started |
| C18: On random 100-text samples, GPTZero labels 93-100% of generated rows as AI and all 100 human rows as human in Table 11, while HIX mostly labels generated rows human. | Direct commercial comparison plus repository CSVs; detector builds are not identified beyond access date 2025-05-20, random selection has no seed, and released HIX files are incomplete for some cells. | Vendor-source caution and detector-output caveat rows in `pattern-opportunities.md`; fully covered as a caution, not as validation. | Not reproducible as a current vendor benchmark; no uncertainty or version pin. | Do not use these results for human-eyes severity or threshold decisions. | pending | not started |
| C19: Machine-generation detection does not imply untrustworthy or malicious content; mixed human-edited/model-edited texts are not covered. | Direct scope and ethical qualification. | `human-eyes/references/process.md` product boundary and `dev/TESTING.md` non-authorship wording; fully covered. | None in current guidance; source indexes should preserve the boundary. | Retain the boundary and take no further product action. | pending | not started |
| C20: Results are limited to English Wikipedia introductions, a multi-author/edited human baseline, fixed prompts, available NLP tooling, a closed multiclass set, and roughly one million human-training tokens. | Direct limitations; authors call cross-domain robustness debatable. | H12, H22, H25 and corpus-variation guidance; fully covered as pending research constraints. | No source-specific summary currently states all controls. | Require these constraints wherever the source is cited. | pending | not started |
| C21: The authors used GPT and Writefull to improve readability, style, and grammar, then reviewed and edited the manuscript. | Direct disclosure; it identifies assistance, not authorship of individual passages or evidential invalidity. | Optional provenance candidate in `pattern-opportunities.md`; partly covered. | Current card omitted the disclosure. | Record provenance informationally; do not score or penalise it. | pending | not started |
| C22: The paper links OSF data/analysis and a GitHub generation repository, but the GitHub tree has no README/setup/config files promised by the paper and does not reproduce the released corpus: its visible notebook path selects 1,000 rather than 2,439 terms, lacks LLaMA 3 and second-prompt generation, uses an undefined GPT `prompt` variable in a fresh linear run, and includes prompt, model-size, and split-description discrepancies. | Direct paper/repository comparison; complete GitHub tree preserved; OSF inventory seen but full archive not preserved. | Source-ingest provenance gate; partly covered by this refresh. | End-to-end reproduction of the 2,439-topic, two-prompt release remains unresolved. | Preserve the repository commit and concrete gaps; do not label the study fully reproducible. | pending | not started |
| C23: Many broad claims about stylometry, attacks, safety, and other detector performance appear only in Related Works. | Cited evidence, not measured by this paper; no recursive ingestion performed. | Source-card direct-versus-cited boundary; fully covered. | Those inherited claims need their own direct source review before promotion. | Keep them indirect and unresolved; do not use them for product decisions from this card. | pending | review required |
| C24: A focused surface-only run of live B1/G9/B5 over all 17,073 rows in the prompt-1 file set (`stylo_wiki_text.csv`, `stylo_gpt3.csv`, `stylo_gpt4.csv`, `stylo_llama2.csv`, `stylo_llama3.csv`, `stylo_orca.csv`, and `stylo_falcon.csv`) found G9 flags 23/2,439 Wikipedia rows versus 183-982 per model; B5 flags 6 Wikipedia rows and 0-5 per model; B1 flags 4 Wikipedia rows versus 9-614 per model. The second prompt-specific set was not run. | Direct live-project comparison on the named prompt-1 files; candidate/threshold output only, not a complete Audit or held-out benchmark. Length eligibility varies sharply, especially for LLaMA 2, Orca, and Falcon. | Exact implementations in `grade.py` were read and executed; G9 and B1 show source-bound separation, while B5's low-TTR direction is challenged. | Same prompt-1 data informed source analysis; no prompt-2 comparison, held-out claim, genre transfer, or false-positive review beyond Wikipedia rows. | Test-adapt only in a separate preregistered, length-matched robustness lane; do not change thresholds from this run. | approved | implemented |
| C25: Future work proposes more languages, libraries, classifiers, model complexity, long-memory/fractal features, embeddings, and cross-domain explanation-consistency checks. The discussion also interprets its results as showing that more-complex models are harder to distinguish, but model family, generation setup, and complexity vary together. | Author proposals plus author interpretation; no isolated complexity experiment demonstrates a causal complexity effect. | H22-H25 and additional-corpus guidance; partly covered as hypotheses. | No direct evidence establishes that these additions improve human-eyes or that complexity independently explains detection difficulty. | Record the extensions as follow-up ideas and the complexity statement as confounded interpretation; require new evidence before adoption. | pending | not started |

## Recommendations

- C01: record the narrow matched-task scope; do not generalise the scores.
- C02: preserve the 2,439/2,424 discrepancy as evaluation-hygiene evidence.
- C03: require exact prompt, model, date, and seed provenance before reusing model-family findings.
- C04: record summariser artefacts only; do not promote them into prose rules.
- C05: retain the feature families as research candidates pending matched controls.
- C06: record the split/configuration tension and avoid a full-reproducibility claim.
- C07: preserve near-chance decision-tree results alongside higher pairwise scores.
- C08: keep the binary LGBM results as source-bound benchmark context only.
- C09: do not promote the closed-set MCC to an authorship or model-family verdict.
- C10: record the model confusions with date/version limits; add no active rule.
- C11: consider unseen-model testing only in an approved robustness lane with specificity and uncertainty.
- C12: record the single-pass paraphrase result without inferring general detector robustness.
- C13: use the cross-domain failure to block generic score and threshold transfer.
- C14: do not add `significant`, `notable`, or `despite` as bare universal vocabulary rules.
- C15: test POS/clause-shape distribution tails as H22 research; do not relabel G9 as grammatical standardisation.
- C16: require artefact ablations before reusing proper-name, punctuation, whitespace, or truncation features.
- C17: keep measured decision-tree results separate from the untested LGBM inference.
- C18: do not use the unpinned commercial-detector results for human-eyes severity or thresholds.
- C19: retain the non-authorship and non-malice boundary; take no further product action.
- C20: require the language, domain, prompt, closed-set, and training-corpus limits wherever the source is cited.
- C21: record disclosed GPT/Writefull assistance informationally without scoring it.
- C22: preserve the repository commit and reproduction gaps; do not label the study fully reproducible.
- C23: keep literature-review claims indirect until their upstream sources receive direct review.
- C24: evaluate B1/G9/B5 on length-matched, source-bound controls; the current prompt-1-only run is diagnostic and specifically challenges B5's low-TTR direction.
- C25: keep future-work suggestions as hypotheses and the complexity statement as a confounded author interpretation pending new evidence.
- No recommendation is implemented; every decision remains pending for Mae.

## Evaluation of approved changes


- C24: passed - B5 flipped to two-tier windowed lexical diversity (flag 0.71, upper tier 0.74) in commit b199a6d; calibration recorded in dev/evals/ttr-calibration-2026-07-17.md; test_grade.py B5 block passes.
- C14: passed - DR-125 adds exact B1 recognition for `significant`, `notable`, and `despite`; focused tests confirm each is counted once.
- C01-C13, C15-C23, C25: not applicable - no product change approved or implemented for those claims during source review.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: review_przystalski_once
- **Findings resolved:** seven material findings resolved across the initial review and two focused re-checks: model-size provenance; repository reproduction gaps; prompt-1 run scope; AuTexTification sample, generator, and domain accounting; local classification failures; future-work versus confounded interpretation; and removal of unsupported cross-domain generators
- **Unresolved findings:** none
