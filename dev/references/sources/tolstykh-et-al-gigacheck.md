# GigaCheck: Detecting LLM-generated Content via Object-Centric Span Localization

## Metadata

- **URL:** https://aclanthology.org/2026.findings-acl.213/
- **Author / owner:** Irina Tolstykh, Aleksandra Tsybina, Sergey Yakubson, Aleksandr Gordeev, Vladimir Dokholyan, and Maksim Kuprashevich
- **Published:** 2026-07
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** peer-reviewed empirical study
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** new
- **Stable identifier:** DOI 10.18653/v1/2026.findings-acl.213; ACL Anthology ID 2026.findings-acl.213
- **Version / revision:** Findings of ACL 2026 proceedings version, pages 4349-4364
- **Full-text status:** complete
- **Snapshot:** `snapshots/tolstykh-et-al-gigacheck.md`
- **Extraction method:** official ACL proceedings PDF and Responsible NLP Checklist PDF downloaded with `curl`; all pages extracted with Poppler `pdftotext -layout`; structure inspected with `pdfinfo` and `pdfimages -list`; paper pages 1, 2, 8, and 16 and both checklist pages rendered with `pdftoppm` and visually checked
- **Snapshot SHA-256:** `01a8b8e2117832cd205dc3ea45a5704f48acc5a0379f6f70987c9255048d8b98`
- **Model / corpus scope:** English; Mistral-7B-v0.3 with LoRA for the main document classifier and span-localisation backbone; DN-DAB-DETR span head; additional Mistral 12B and 24B and Qwen2.5-72B backbone comparison on MAGE; classification benchmarks TuringBench, TweepFake, and MAGE; mixed-authorship localisation benchmarks RoFT, RoFT-ChatGPT, and TriBERT; source datasets cover news, tweets, Reddit opinions, reviews, question answering, stories, commonsense reasoning, Wikipedia paragraphs, scientific writing, speeches, recipes, short stories, and educational essays; maximum model inputs of 512 or 1024 tokens depending on experiment
- **Access limitations:** no source text was inaccessible. Figure pixels, bold interval markings in Tables 15 and 16, checkbox typography, and exact page layout are preserved only in the attached official PDFs. The cited GitHub repository was not used as evidence and was not recursively ingested.

## Summary

This Findings of ACL 2026 paper presents GigaCheck, a learned detector with separate document-level classification and character-level mixed-authorship span-localisation heads. The authors evaluate a LoRA-tuned Mistral backbone on three classification and three localisation benchmarks and report strong benchmark results, including out-of-domain, out-of-model, and paraphrase conditions. For human-eyes, the useful evidence concerns evaluation design, local versus document-level evidence, and detector limitations rather than prose-pattern validity. The authors limit the study to English, truncate or chunk long inputs, report single-run results without variance estimates, warn that small benchmarks may be saturated, and state that the detector should assist human verification rather than decide high-stakes cases by itself. The user queue title, `GigaCheck`, is a shortened title; the authoritative work's full title is recorded above.

## Main insights

- GigaCheck separates document-level binary authorship classification from character-level localisation of machine-generated intervals in mixed-authorship texts.
- The span head treats intervals as one-dimensional objects and predicts continuous character spans before benchmark-specific projection to sentence boundaries.
- Fine-tuned Mistral embeddings materially outperform frozen pre-trained embeddings on the two RoFT localisation benchmarks, although the frozen variants remain viable and the TriBERT experiment uses frozen embeddings because that dataset is small.
- Reported classification scores are high in the evaluated benchmarks, but the authors warn that near-perfect results on smaller corpora may reflect limited diversity and persistent artefacts.
- Paraphrase attacks cause a substantial drop in machine recall even though the paper reports stronger results in its unseen-domain and unseen-model settings.
- Performance depends on generator model, domain, text length, and training condition; English-only evaluation and input-window chunking constrain transfer claims.
- Increasing backbone size is not monotonically beneficial: the Qwen 72B variant performs worse than the smaller Mistral variants on the MAGE full set.
- The paper's ethical guidance favours span-level transparency and human verification over sole reliance on a black-box document verdict in high-stakes decisions.
- The Responsible NLP Checklist discloses that every model was trained once and that the results have no error bars or variance estimates.

## Evidence and claims to extract

- **Direct source reviewed:** the Findings of ACL 2026 proceedings paper at DOI 10.18653/v1/2026.findings-acl.213, pages 4349-4364, plus its official two-page Responsible NLP Checklist
- **Method and sample:** GigaCheck uses a LoRA-tuned Mistral-7B-v0.3 backbone. A two-layer MLP classifies whole documents, while a DN-DAB-DETR head predicts normalised one-dimensional character intervals from token embeddings. Classification uses TuringBench FAIR wmt20 and GPT-3 subsets, TweepFake, and MAGE. Localisation uses RoFT, RoFT-ChatGPT, and TriBERT. The study follows original train-test splits and reports accuracy, F1, AUROC, average recall, boundary MSE and accuracy, F1@3, and one-dimensional mAP. Text inputs are capped at 512 or 1024 tokens depending on the experiment. All model training results are single runs.
- **Direct versus cited evidence:** C01-C09 are direct methods, results, limitations, or checklist disclosures from this work. Background statements about harms, detector history, statistical versus neural methods, and other detectors are cited evidence and are not used here as independent project support.
- **Important limits and counterexamples:** results are English-only and benchmark-specific; longer documents are chunked; several benchmark comparisons use old or limited generator sets; character predictions are projected to sentence boundaries for some published metrics; MAGE paraphrase machine recall falls to 58.24%; the 72B backbone underperforms smaller variants; benchmark saturation may inflate apparent real-world performance; no repeated-run variance is reported; no result establishes an individual-document rule for human-eyes.

## Skill-use audit

- **Good use:** distinguish local evidence from whole-document verdicts; design future detector-evaluation research that reports domain, generator, length, attack, and metric granularity; preserve benchmark saturation and single-run uncertainty; support an assistive rather than punitive interpretation of detector output.
- **Misuse / overclaim:** treat GigaCheck benchmark accuracy as validation of human-eyes checks, thresholds, pattern severities, or authorship conclusions.
- **Unsupported use:** infer that any human-eyes phrase or construction marks a machine-authored interval; claim multilingual performance; claim production reliability; generalise results beyond the tested models, datasets, input lengths, and English text; treat span localisation as causal explanation of why prose reads as machine-generated.
- **Underused evidence:** the distinction between native character-level localisation and sentence-projected metrics; weak leave-one-domain-out performance on RoFT-ChatGPT Recipes; degradation under paraphrasing; non-monotonic backbone scaling; benchmark saturation; single-run uncertainty.
- **Patterns left on the table:** none. This source evaluates learned authorship detectors and does not measure a reusable phrase, construction, vocabulary item, formatting habit, rhythm, tone, or writing-quality pattern for promotion into the human-eyes catalogue.

## Matched patterns / rules

- `human-eyes/scripts/grade.py`: exact programmatic candidates and exact evidence spans are retained for named writing constructions; the grader does not classify machine authorship or localise machine-authored intervals.
- `human-eyes/scripts/judgement.json`: list-shaped agent findings require exact input substrings, but they assess writing problems rather than machine authorship.
- `human-eyes/SKILL.md`, `STRATEGY.md`, and `human-eyes/references/process.md`: the current product boundary prohibits provenance estimates and authorship classification.
- `dev/TESTING.md`: current comparison guidance already requires generation provenance, broader genres and registers, weak and reversed cases, and a no-authorship-classification statement, but it has no span-localisation benchmark or repeated-training-run requirement.
- No prose-pattern rule is directly supported by this source.

## Associated hypotheses

- H1, continuous calibrated register-distance score per pattern, is relevant to uncertainty but measures writing-pattern distance rather than detector authorship.
- H3, drop detection framing entirely, is supported by the need to keep human-eyes distinct from authorship classifiers even when learned detectors report strong benchmark results.
- H12, genre-aware threshold calibration, and H25, model-family versus generic-AI residue, align with the paper's domain and generator dependence.
- H19, bootstrap confidence intervals on corpus claims, aligns with the paper's missing uncertainty reporting but does not by itself solve repeated-training-run variance.
- Proposed follow-up: any future learned-detector comparison should preserve native span metrics, repeated-run uncertainty, attack conditions, and direction-specific domain and generator transfer without changing the human-eyes product boundary.

## Questions / follow-up

- Should the pending detector-research lane in `dev/TESTING.md` require repeated training seeds and variance estimates before benchmark differences are treated as decision-relevant?
- Should native character-span localisation be recorded as a separate research surface from the current pattern-specific evidence spans, with an explicit rule that it cannot become a human-eyes authorship feature without a product-scope decision?
- The public code repository could be reviewed in a separate ingestion if implementation reproducibility becomes decision-relevant. It was not needed for the present paper ingestion.

## Update provenance

Not applicable: initial ingestion.

## Decision history

None: initial review.

## Project coverage

This is the authoritative review table. Give every relevant source claim or example a stable claim ID in the first cell.

Escape any literal pipe within a table cell as `\|`; an unescaped extra pipe makes the row invalid.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: GigaCheck separates a binary document classifier from a DN-DAB-DETR head that predicts continuous character-level machine-generated intervals in mixed-authorship text. | Direct peer-reviewed method contribution. It localises predicted authorship intervals, not named prose patterns or causal stylistic evidence. The native output is character-level, although several benchmark metrics require deterministic sentence projection. | partly covered: `human-eyes/scripts/grade.py` returns exact candidate spans for named deterministic constructions, and list answers in `human-eyes/scripts/judgement.json` require exact evidence substrings. `human-eyes/SKILL.md` and `STRATEGY.md` explicitly prohibit authorship classification. | Human-eyes has local evidence for writing problems but no machine-authorship span model. Treating exact pattern evidence as authorship localisation would cross the current product boundary. | Record the architectural distinction only. Do not add an authorship-span feature to `human-eyes/scripts/grade.py` or `human-eyes/scripts/judgement.json`. If future research is approved, specify it separately in `dev/TESTING.md` and verify native character-span metrics plus false-positive controls. | pending | not started |
| C02: On RoFT and RoFT-ChatGPT, GigaCheck reports boundary accuracy of 0.65 and 0.68 versus 0.50 and 0.55 for RoBERTa plus SEP, with MSE of 1.51 and 1.03. In leave-one-domain-out RoFT-ChatGPT testing, accuracy falls to 0.33 on Recipes, compared with 0.50, 0.55, and 0.64 on the other domains. On TriBERT, full-set F1@3 is 0.646 versus 0.575. | Direct benchmark results across three mixed-authorship datasets. Baseline values are inherited from the cited benchmark papers. Sentence-level metrics include character-to-sentence projection; mAP@0.5-0.95 is the direct interval metric. The low Recipes result qualifies the paper's cross-domain generalisation claim. Results are single runs without uncertainty estimates. | not covered: neither `dev/TESTING.md` nor the current evaluation harness measures machine-authorship boundary localisation, and human-eyes does not expose an authorship score. | The reported gains cannot validate the catalogue, and projected sentence metrics should not be confused with native span accuracy. The lack of repeated runs makes small ranking differences uncertain. | Record as detector-research background only. If a detector research lane is approved, require native span metrics, projected metrics reported separately, repeated seeds, variance, and error analysis. Make no checker, registry, guidance, or test change from these scores. | pending | not started |
| C03: Fine-tuned Mistral embeddings outperform frozen pre-trained embeddings on both RoFT datasets, including RoFT-ChatGPT accuracy of 67.65% versus 51.37% and MSE of 1.03 versus 1.93. The frozen setup still reaches 60.10% accuracy on RoFT, and the TriBERT experiment uses frozen Mistral embeddings because that dataset is small. | Direct ablation and experimental setup in Table 10 and Section 5.1. The results support task-specific representation learning in this architecture while showing that frozen embeddings remain viable. They do not isolate which linguistic properties drive the difference. | not covered: human-eyes uses deterministic checks and source-bound agent judgement rather than a learned authorship representation. | The result does not map to any phrase, construction, pattern threshold, or semantic registry item. Importing it would change the product from writing-pattern audit to learned authorship detection. | Take no product action. Preserve the ablation as a boundary on what surface-pattern evidence can claim. Any learned-representation experiment requires a separate product-scope decision and evaluation plan. | pending | not started |
| C04: The document classifier reports 0.943 TweepFake accuracy, machine F1 of 0.9966 and 0.9709 on two TuringBench subsets, and MAGE full-set average recall of 0.9611 with AUROC 0.9923. | Direct benchmark results for fine-tuned Mistral-7B. The authors warn that near-perfect TuringBench scores may reflect limited diversity and persistent artefacts rather than real-world detection reliability. | not covered: `STRATEGY.md` defines catalogue coverage and check accuracy around named writing constructions, not authorship AUROC or document classification. H3 explicitly questions detection framing. | These benchmark scores are not human-eyes metrics and cannot set pattern severity, thresholds, release gates, or document-level conclusions. | Record the results with the saturation warning and do not promote them into `README.md`, checker thresholds, pattern guidance, or release claims. No further action unless the maintainer separately approves a learned-detector research track. | pending | not started |
| C05: On MAGE, GigaCheck reports average recall of 0.8854 for unseen domains plus unseen models and 0.9232 for unseen models, but only 0.6895 under paraphrase attack, where machine recall falls to 58.24%. | Direct out-of-distribution and attack results. The challenging sets reuse the model trained on the arbitrary-domain and arbitrary-model split. The attack condition remains dataset-specific and does not establish universal evasion resistance. | partly covered: `dev/TESTING.md` requires broader genres, registers, authors, eras, and source types; generation provenance with the model where known; reporting of weak and reversed pairs; and separate labelling of coached, rerolled, or human-rewrite AI samples. It does not require varied generator models. H25 tracks model-family dependence. | There is no dedicated paraphrase or detector-evasion lane, no train-condition versus test-condition matrix, and no authorship-detector metric in human-eyes. | If approved, add a separate adversarial research protocol to `dev/TESTING.md` that preserves the unmodified source, transformation prompt and model, train condition, human and machine recall, and failure examples. Keep it separate from the ordinary literal-first comparison corpus and make no product check change. | pending | not started |
| C06: The study is English-only; inputs are capped at 512 or 1024 tokens; longer documents are independently chunked, which can hide dependencies across chunk boundaries; performance can vary with generator, text length, and domain. | Direct limitations and ethical qualification. The authors say other languages need new training data and do not report multilingual results. | partly covered: source-card metadata records model, language, corpus, and length scope; `dev/TESTING.md` requires model provenance, varied genres and registers, comparable lengths, explicit version refs, and cautious comparison reporting. H12 and H25 cover genre and model dependence. | Current evaluation records do not consistently preserve evaluator context windows, truncation, overlap, or chunk-boundary behaviour. | If approved, add evaluator input limit, truncation, chunk size, overlap, and language fields to future model-backed comparison reports in `dev/TESTING.md`. Do not change active checks or claim multilingual support. | pending | not started |
| C07: On the MAGE full set, average recall rises from 0.9611 for Mistral-7B to 0.9685 for Mistral-24B, then falls to 0.8338 for Qwen2.5-72B; the authors suggest overfitting. | Direct backbone-size comparison from one dataset and one training setup. The overfitting explanation is author interpretation rather than a demonstrated causal result. | not covered: human-eyes has no learned detector backbone or scaling study. H25 records model-family dependence but not parameter-count scaling. | The result cannot support a general rule that larger or smaller evaluators are more reliable, and it does not justify changing the agent model or checker behaviour. | Record only as a counterexample to monotonic scale assumptions. Take no product action and require repeated runs plus controlled model-family comparisons before any evaluator-selection conclusion. | pending | not started |
| C08: The Ethical Statement says performance varies by generator, length, and domain and recommends using GigaCheck as an assistive tool for human verification rather than the sole basis for high-stakes decisions. | Direct author guidance tied to the detector's non-perfect accuracy. Span localisation is presented as more transparent than a black-box document verdict, but it remains a prediction rather than proof. | fully covered: `human-eyes/SKILL.md`, `STRATEGY.md`, and `human-eyes/references/process.md` prohibit authorship classification, provenance probability, accusation, and proof language. `dev/TESTING.md` requires a statement that human-eyes measures prose patterns rather than authorship. | No gap in current product behaviour. The paper reinforces the existing boundary but does not validate current pattern checks. | Preserve the current product boundary unchanged. Record this source as corroborating detector-caution context and do not present its span predictions as proof. | pending | not started |
| C09: The Responsible NLP Checklist states that every model was trained once and reports no error bars or variance estimates because of the cost of fine-tuning 7B-parameter models. | Direct checklist disclosure and central uncertainty limit. Reported tables are point estimates, so close comparisons may be seed-sensitive even where benchmark protocols match. | partly covered: H19 in `dev/hypotheses.md` calls for confidence intervals on corpus claims, and `dev/TESTING.md` requires weak cases and honest interpretation. Neither file requires repeated model-training runs or seed variance for learned-detector comparisons. | A future learned-detector lane could overstate point-estimate gains without a repeated-run or uncertainty standard. | If approved, add a repeated-seed and uncertainty requirement to the pending detector-research protocol in `dev/TESTING.md`, or require an explicit single-run limitation when repetition is infeasible. Do not change pattern checks, severities, or active release gates. | pending | not started |

## Recommendations

- C01: Record the local-evidence versus authorship-localisation distinction; do not add an authorship-span feature. If future research is approved, specify it separately in `dev/TESTING.md`.
- C02: Keep the localisation scores as detector-research background. Any approved research lane should report native and projected span metrics separately, with repeated seeds, variance, and error analysis.
- C03: Take no product action. A learned-representation experiment requires a separate product-scope decision.
- C04: Do not promote benchmark accuracy into human-eyes thresholds, pattern guidance, release gates, or authorship claims.
- C05: If approved, add a separate adversarial paraphrase protocol to `dev/TESTING.md`; keep it outside the ordinary literal-first comparison corpus and make no checker change.
- C06: If approved, add evaluator input-limit, truncation, chunking, overlap, and language metadata to future model-backed comparison reports in `dev/TESTING.md`.
- C07: Record the non-monotonic backbone result only; require controlled repeated comparisons before any evaluator-selection conclusion.
- C08: Preserve the existing no-authorship and assistive-review product boundary unchanged.
- C09: If approved, add repeated-seed and uncertainty reporting to the pending detector-research protocol in `dev/TESTING.md`, with an explicit single-run limitation when repetition is infeasible.

## Evaluation of approved changes

- C01: not applicable - recommendation pending; no product change implemented.
- C02: not applicable - recommendation pending; no product change implemented.
- C03: not applicable - recommendation pending; no product change implemented.
- C04: not applicable - recommendation pending; no product change implemented.
- C05: not applicable - recommendation pending; no product change implemented.
- C06: not applicable - recommendation pending; no product change implemented.
- C07: not applicable - recommendation pending; no product change implemented.
- C08: not applicable - recommendation pending; no product change implemented.
- C09: not applicable - recommendation pending; no product change implemented.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: Codex CLI fresh process, did not perform the extraction
- **Findings resolved:** added the omitted low RoFT-ChatGPT Recipes leave-one-domain-out result to C02; qualified C03 with the viable frozen-backbone results and frozen TriBERT setup; corrected C05's description of current project coverage; normalised authored prose to Australian English
- **Unresolved findings:** none
