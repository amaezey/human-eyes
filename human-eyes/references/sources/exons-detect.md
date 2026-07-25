# Exons-Detect: Identifying and Amplifying Exonic Tokens via Hidden-State Discrepancy for Robust AI-Generated Text Detection

## Metadata

- **URL:** https://aclanthology.org/2026.acl-long.1211/
- **Author / owner:** Xiaowei Zhu, Yubing Ren, Fang Fang, Shi Wang, Yanan Cao, and Li Guo
- **Published:** 2026-07-02 to 2026-07-07
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** peer-reviewed empirical study
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** new
- **Stable identifier:** DOI 10.18653/v1/2026.acl-long.1211; ACL Anthology ID 2026.acl-long.1211
- **Version / revision:** ACL 2026 proceedings version, pages 26324-26336, plus ACL Responsible NLP Checklist
- **Full-text status:** complete
- **Snapshot:** `snapshots/exons-detect.md`
- **Extraction method:** Official ACL paper and checklist PDFs downloaded directly, inspected with `pdfinfo`, converted from embedded text layers with Poppler `pdftotext -layout`, and checked against rendered pages 1, 7, and 13 of the paper and both checklist pages. The two official PDFs are preserved under `snapshots/attachments/`.
- **Snapshot SHA-256:** `290debf30a17baa7ca468ee991c3c239cf57a95d73f3088c1d708963c3a30b66`
- **Model / corpus scope:** Four balanced evaluation settings sampled at 2,000 texts each from M4, DetectRL Multi-LLM, DetectRL Multi-Domain, and RealDet, with a maximum input length of 1,024 tokens. Main training-free experiments use Falcon-7B-Instruct with Falcon-7B; ablations also use LLaMA-2-7B with LLaMA-7B, Mistral-v0.1-7B-Instruct with Mistral-v0.1-7B, and LLaMA-3.2-1B-Instruct with LLaMA-3.2-1B. The polishing attack uses `gpt-4o-2024-11-20`. The paper does not state the evaluated language subset in its setup description.
- **Access limitations:** None for the paper or checklist. Some plot labels in Figures 3 and 4 are garbled in the PDF text layer, but the official PDF attachments retain the complete rendered figures. The Markdown snapshot preserves the extracted text, tables, captions, appendices, references, and the complete checklist, with this transformation recorded.

## Summary

This ACL 2026 long paper presents Exons-Detect, a training-free binary detector that uses discrepancies between paired proxy language models' hidden states to identify and upweight selected tokens before computing a probability-based detection score. Across four balanced settings drawn from three public benchmarks, the authors report stronger average AUROC and F1 than their baselines, plus robustness experiments for paraphrasing, GPT-4o polishing of human text, input length, proxy-model choice, hyperparameters, and runtime. For human-eyes, the paper is detector-method and evaluation evidence, not prose-pattern evidence. Its most useful contribution is a concrete adversarial and length-robustness design, while its binary treatment of lightly AI-polished human text exposes a provenance-category choice that the current project should not leave implicit.

## Main insights

- C01: Exons-Detect uses paired proxy LLM hidden-state discrepancies to select and upweight high-discrepancy tokens before computing a translation score.
- C02: The paper's empirical observation and Appendix A analysis say the selected tokens are enriched for label-consistent contributions that move near-boundary scores towards the expected class.
- C03: Across M4, two DetectRL settings, and RealDet, Exons-Detect reports average AUROC 92.14 and F1 87.72, compared with 90.86 and 87.02 for DNA-DetectLLM.
- C04: Exons-Detect is the only reported method above 90 AUROC in all four evaluation settings, but this is a benchmark-specific comparison rather than a universal generalisation result.
- C05: The method remains the strongest plotted system under DIPPER paraphrasing of AI text and GPT-4o polishing of human text; polishing is the harder attack for several baselines.
- C06: All methods improve with longer inputs, while Exons-Detect retains the strongest results from 40 to 240 tokens and reports average improvements of 2.7 percent over DNA-DetectLLM and 6.4 percent over IRM across the tested lengths.
- C07: Removing nonlinear discrepancy mapping or mutation-repair produces reported average AUROC drops of 1.0 percent and 4.4 percent, respectively.
- C08: Four proxy-model pairings all exceed 90 average AUROC, although results still vary by dataset and pair.
- C09: Reported performance changes by less than about one point across much of the tested alpha and theta range, but extreme thresholds are worse, 32 hidden layers outperform smaller subsets, and linear mapping is less stable across datasets.
- C10: On 1,000 RealDet samples truncated to 300 tokens, Exons-Detect takes 0.79 seconds per text on one NVIDIA A100 in FP32, with two model forward passes and no detector training.
- C11: The robustness setup treats lightly GPT-4o-polished human text as the human class even though the text contains AI intervention, showing that binary labels depend on the chosen provenance definition.
- C12: The paper reports point estimates without run-level variability or error bars. The checklist marks descriptive-statistics reporting, potential-risk discussion, and data-identifiability or offensive-content safeguards as not applicable; it reports no human annotators and no AI-assistant use.
- C13: The study evaluates detector scores, not reusable surface prose cues, writing quality, or individual-document certainty for human-eyes.

## Evidence and claims to extract

- **Direct source reviewed:** ACL 2026 proceedings paper, DOI 10.18653/v1/2026.acl-long.1211, pages 26324-26336, and the associated ACL Responsible NLP Checklist.
- **Method and sample:** Training-free dual-model detection evaluated on random balanced samples of 2,000 texts from each of four settings: M4, DetectRL Multi-LLM, DetectRL Multi-Domain, and RealDet. Inputs are capped at 1,024 tokens. Main proxy models are Falcon-7B-Instruct and Falcon-7B, with three other family pairings in ablation. Training-based baselines were trained on HC3, which is disjoint from the evaluation benchmarks. The comparison standardised the Falcon-7B-Instruct reference model and Falcon-7B paired model for the named two-model training-free methods. Metrics are AUROC and F1. Attacks use DIPPER for paraphrasing and `gpt-4o-2024-11-20` for light polishing. Efficiency uses 1,000 RealDet texts truncated to 300 tokens on one 80 GB NVIDIA A100 with FP32.
- **Direct versus cited evidence:** C01-C10 are direct method descriptions, experiments, and ablations from this source. C11 combines the direct polishing-attack design with a project inference about its binary class convention. C12 combines direct checklist disclosures with a review of reporting omissions. The introductory statement that humans perform marginally above chance is inherited from Clark et al. 2021 and is not used as a direct finding here. C13 is the project comparison implied by the paper's measured outcome and the human-eyes product boundary.
- **Important limits and counterexamples:** The benchmark uses balanced experimental samples, not natural prevalence. The paper does not report the language subset, run-to-run variability, confidence intervals, a full risk analysis, or human evaluation. Exact detector threshold selection for reported F1 is not explained. The model needs access to paired proxy-model probabilities and hidden states. Attack robustness is shown with one paraphraser and one GPT-4o version. All methods improve with length. Proxy pairs and hyperparameters still change results. The authors identify cosine distance as a coarse limitation. Binary labels for AI-polished human text depend on a task-specific provenance convention.

## Skill-use audit

- **Good use:** Use the paper to design a separate detector-research robustness lane covering model pairs, domains, attacks, input length, ablations, runtime, and explicit provenance labels.
- **Misuse / overclaim:** Do not import its AUROC, F1, discrepancy threshold, or token weights as human-eyes performance or pattern severity.
- **Unsupported use:** The paper cannot support a surface wording rule, an individual-document authorship verdict, a universal human-versus-AI threshold, or a claim that AI-polished human text has one objectively correct binary class.
- **Underused evidence:** The current project records length and provenance but does not run a controlled length curve, pairwise proxy-model ablation, or human-polish versus machine-paraphrase attack matrix.
- **Patterns left on the table:** None. The paper's tokens are model-state features, not lexical, grammatical, rhetorical, or formatting patterns that can be promoted to the catalogue.

## Matched patterns / rules

- `STRATEGY.md` product boundary: human-eyes examines writing patterns and does not determine authorship.
- `human-eyes/references/process.md` product boundary: reports describe constructions and edits, not who or what wrote the text.
- `dev/TESTING.md` comparative-baseline, additional-corpus, provenance, length-matching, weak-case, runtime, and no-authorship requirements.
- H1, H3, H12, H19, and H25 in `dev/hypotheses.md`: calibrated scores, detection-framing caution, register-specific thresholds, uncertainty, and model-family specificity.
- `human-eyes/references/sources/wang-et-al-human-like-text-liked-by-humans.md`: separate coached or adversarial evaluation and preserve exact prompt, model, length, and factuality context.
- `human-eyes/references/sources/xia-stanczak-roth-detector-generalization.md`: prompt, generator, domain, evaluator, and truncation robustness as separate axes in detector generalisation.
- No entry in `human-eyes/scripts/patterns.json` or `human-eyes/scripts/judgement.json` implements hidden-state discrepancy, probability scoring, or binary provenance classification.

## Associated hypotheses

- H1: Continuous calibrated register-distance score per pattern.
- H3: Drop detection framing entirely.
- H12: Genre-aware threshold calibration.
- H19: Bootstrap confidence intervals on corpus claims.
- H25: Model-family versus generic-AI residue.
- Proposed research question, pending user decision: whether provenance labels should distinguish untouched human, lightly AI-polished human, AI rewrite of human, and fresh AI generation before any comparison is reported.

## Questions / follow-up

- The queue title was `Exons-Detect`; the authoritative work's full title is `Exons-Detect: Identifying and Amplifying Exonic Tokens via Hidden-State Discrepancy for Robust AI-Generated Text Detection`. This is an abbreviated queue title, not a competing source identity.
- Which languages and generator subsets from M4, DetectRL, and RealDet were included in the sampled evaluation sets? The paper does not say.
- How was the decision threshold for each reported F1 selected, and are the results single runs or aggregates across repeated runs?
- If a robustness lane is approved later, should its provenance taxonomy distinguish light polishing from substantive rewriting before grouping samples?
- The linked code and data repository is a separate first-party artefact and was not recursively ingested in this run. Review it directly before using implementation or reproducibility claims beyond the paper.

## Update provenance

Not applicable: initial ingestion.

## Decision history

None: initial review.

## Project coverage

This is the authoritative review table. Every recommendation remains pending, and no product changes were made.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Exons-Detect selects tokens whose paired-model hidden-state cosine discrepancy exceeds theta and upweights them before probability-score aggregation. | Direct peer-reviewed method description and equations 4-9. The feature requires paired proxy-model hidden states and probabilities and is not a visible prose construction. | Not covered: `human-eyes/scripts/grade.py`, `human-eyes/scripts/patterns.json`, and `human-eyes/scripts/judgement.json` contain deterministic surface checks and agent-assessed writing checks, not white-box model-state features. | No hidden-state or probability detector exists, and adding one would change the product from a writing-pattern audit toward authorship classification. | Record as external detector architecture only. Do not add a checker or judgement item. Reconsider only after a separate product-boundary decision and reproducible benchmark. | pending | not started |
| C02: High-discrepancy tokens are empirically enriched for label-consistent contributions, and Appendix A argues that their reweighting moves near-boundary scores towards the expected class. | Direct observation, Figure 2, and analytic sign argument. The paper gives no claim that these tokens map to stable words or constructions, and the enrichment counts are not tabulated. | Not covered: no live project feature corresponds to the paper's token-level latent discrepancies. H1 in `dev/hypotheses.md` concerns calibrated catalogue-pattern scores, not hidden-state tokens. | Treating existing vocabulary or structural candidates as exonic-token proxies would be unsupported. | Record the distinction between latent token importance and visible prose patterns. Take no product action. Any future replication must preserve token-level distributions and near-boundary cases. | pending | not started |
| C03: On four balanced benchmark settings, Exons-Detect reports average AUROC 92.14 and F1 87.72 versus 90.86 and 87.02 for DNA-DetectLLM, including a 2.2 percent relative average AUROC improvement on the two DetectRL settings. | Direct Table 1 results on random balanced samples of 2,000 texts per setting. Training-based baselines were trained on disjoint HC3 data, while the named two-model training-free methods used the same Falcon reference and paired models. These are point estimates under the paper's models, datasets, and implementation, not human-eyes metrics or natural prevalence. | Not covered: `dev/TESTING.md` and `STRATEGY.md` define pattern findings and matched-sample gaps, not binary detector AUROC or F1, and `STRATEGY.md` expressly rejects authorship classification. | The linked code repository and exact runnable environment were not directly reviewed, so independent reproduction is unresolved. | Keep the numbers as detector-background evidence only. Before any adoption discussion, ingest the code artefact separately, record a commit, reproduce Table 1, and audit dataset licences and splits. | pending | not started |
| C04: Exons-Detect is the only reported method above 90 AUROC in all four settings, while baseline performance varies sharply by dataset. | Direct Table 1 comparison. It demonstrates breadth across the chosen settings but is not a fully crossed prompt, generator, language, and domain study. | Partly covered: `dev/TESTING.md` requires varied genres, registers, provenance, weak cases, and explicit version refs. `human-eyes/references/sources/xia-stanczak-roth-detector-generalization.md` already proposes a separate factorial robustness lane. | Current human-eyes evaluation does not reproduce these detector settings, and the paper does not isolate each source of distribution shift. | If approved, add this paper as support for the pending factorial robustness lane, with dataset, domain, language, generator, proxy pair, version, and truncation reported separately. Do not import its aggregate score. | pending | not started |
| C05: Exons-Detect remains the strongest plotted method under DIPPER paraphrasing of AI text and GPT-4o polishing of human text, while polishing causes larger degradation for several baselines. | Direct Section 4.3.1 and Figure 3 result. The attack study uses one paraphraser and one exact polishing model, and the figure supplies curves rather than a numeric result table. | Partly covered: `dev/TESTING.md` keeps coached, rerolled, or human-rewrite AI samples outside the main fresh-write corpus. `human-eyes/references/sources/wang-et-al-human-like-text-liked-by-humans.md` already recommends a separately labelled adversarial track with exact prompt and model provenance. | No committed attack matrix tests both AI paraphrase evasion and AI polishing of human text, and no factuality or meaning-preservation result is reported here. | If approved, extend the pending adversarial lane with separate AI-paraphrase and human-polish cells. Preserve original and attacked pairs, exact prompts and model versions, complete Audits, factuality checks, and meaning-preservation checks. | pending | not started |
| C06: All tested detectors improve with input length; Exons-Detect remains strongest from 40 to 240 tokens and reports average improvements of 2.7 percent over DNA-DetectLLM and 6.4 percent over IRM across tested lengths. | Direct Section 4.3.2 and Figure 4. Exact per-length plotted values are visually available but not tabulated. The paper also caps general evaluation inputs at 1,024 tokens. | Partly covered: `dev/TESTING.md` requires similar prose length or length-normalised results and records word counts. In `human-eyes/scripts/grade.py`, `sentence-length-variance`, `no-negation-density`, `no-forced-triads`, and `vocabulary-diversity` skip short inputs or require minimum lengths. | The project does not run controlled truncation curves, and its word-based checks are not comparable to this token-based binary detector. | If approved, add controlled sentence-boundary length bands to a separate robustness experiment. Report candidate recognition, threshold firing, and complete-Audit findings separately, without using Exons-Detect's curve as a human-eyes threshold. | pending | not started |
| C07: Removing nonlinear discrepancy mapping produces a reported average AUROC drop of 1.0 percent, while removing mutation-repair produces a reported drop of 4.4 percent. | Direct Table 2 ablation. The components are specific to Exons-Detect and DNA-DetectLLM; no uncertainty across reruns is given. | Not covered: `human-eyes/scripts/grade.py`, `human-eyes/scripts/patterns.json`, and `human-eyes/scripts/judgement.json` implement neither mechanism. | Component contributions cannot be transferred to regex, density, or agent-assessed catalogue checks. | Record the ablation as method-specific evidence. Take no product action. Require reproduced component ablations if the external detector is ever evaluated separately. | pending | not started |
| C08: Four proxy-model pairings all exceed 90 average AUROC, with dataset-specific variation and some non-default pairs outperforming Falcon on DetectRL. | Direct Table 2 model-pair ablation. It covers four related open model families but not proprietary proxy access, all sizes, or time drift. | Partly covered: H25 in `dev/hypotheses.md` and source metadata distinguish model-family and version-specific evidence. `dev/TESTING.md` requires exact provenance for compared model outputs. | H25 focuses mainly on generator residue, while this result concerns evaluator proxy pairs and evaluator architecture. | If approved, extend H25 or the pending robustness lane to record evaluator model pairs separately from generators and to preserve direction-specific results. No checker change. | pending | not started |
| C09: Performance is usually stable within about one point across tested alpha and theta values, but extreme thresholds are worse, all 32 hidden layers perform best, higher-layer reverse extraction beats forward extraction at equal layer counts, and linear mapping is less stable by dataset. | Direct Sections 4.5 and Appendices D-F, Tables 3-5. The findings are tied to the tested proxy pairs, benchmark samples, and search ranges. | Not covered: H1, H12, and H19 in `dev/hypotheses.md` call for calibration and uncertainty in human-eyes but do not reproduce these detector hyperparameters or latent layers. | The paper reports best settings and sensitivity point estimates without confidence intervals, repeated-run variation, or a predeclared search protocol. | Record as evidence that external detector results require sensitivity and layer ablations. Do not translate alpha, theta, or layer count into human-eyes thresholds. | pending | not started |
| C10: Exons-Detect takes 0.79 seconds per 300-token RealDet sample on one 80 GB NVIDIA A100 in FP32, using two forward passes and no detector training. | Direct Section 4.6, Figure 6, and Appendix B. The runtime excludes different hardware, model loading, deployment overhead, and energy or memory reporting beyond GPU type. | Partly covered: `dev/TESTING.md` says the evidence-aware paired benchmark records runtime through `dev/evals/harness/run_evidence_benchmark.py`, but that benchmark measures a different local audit pipeline. | No comparable end-to-end cost or hardware-normalised result exists, and the paper's runtime is not portable to the current product. | Record the runtime with its hardware and length scope. If the detector is separately reproduced, report warm and cold latency, memory, energy where feasible, batching, and end-to-end overhead. | pending | not started |
| C11: The polishing attack treats lightly GPT-4o-polished human text as human-class input even though AI changed the text, while the current human-eyes corpus groups an AI rewrite of a human original with AI samples. | The attack construction and prompt are direct Appendix C evidence. The human-class treatment is inferred from the paper's binary attack design; the paper does not discuss alternative class conventions. Compared with the live corpus categories described in `dev/TESTING.md` and `dev/evals/corpus.json`, the two transformations may differ in degree, so neither label scheme is uniquely correct. | Challenges current behaviour: `dev/TESTING.md` and `dev/evals/corpus.json` record human original, AI fresh-write, and AI rewrite groups, but they have no graduated transformation-depth field. The pending StoryScope disclosure row in `human-eyes/references/sources/pattern-opportunities.md` also notes that assistance roles need separation. | Binary group labels can hide whether the evaluated target is origin, intervention, final wording, or editorial ownership. | If approved, define provenance fields for untouched human, light AI polish, substantive AI rewrite, fresh AI generation, and mixed or unknown cases. Preserve transformation prompts and do not collapse these groups in reports without a stated task rationale. | pending | not started |
| C12: Results are point estimates without run-level uncertainty. The checklist marks descriptive-statistics reporting, potential-risk discussion, and data-identifiability or offensive-content safeguards as not applicable; it reports no human annotators and no AI-assistant use. | Direct paper reporting and checklist responses A2, B4, C3, D, and E. The absence of variability, risk, and data-governance reporting does not invalidate the benchmark results, but it limits precision, reproducibility, and deployment-risk claims. The no-human-annotator response also confirms that the study did not test human interpretation. | Partly covered: H19 in `dev/hypotheses.md` proposes bootstrap confidence intervals; `dev/TESTING.md` requires weak cases, provenance, false positives, and careful claim boundaries. `human-eyes/references/sources/stowe-detector-bias.md` and `human-eyes/references/sources/xia-stanczak-roth-detector-generalization.md` add detector-specific fairness and transfer cautions. | Existing testing guidance does not require repeated-run uncertainty for stochastic model-backed evaluations, a risk statement, data-governance disclosure, or human-evaluation scope when evaluating external authorship detectors. | If approved, add repeated-run or justified deterministic-run reporting, uncertainty intervals, threshold-selection provenance, deployment-risk and data-governance sections, and an explicit human-evaluation scope statement to the pending detector-research lane. Keep this separate from checker changes. | pending | not started |
| C13: The paper measures binary detector discrimination and supplies no validated lexical, grammatical, rhetorical, formatting, or writing-quality pattern for human-eyes. | Direct method and outcome scope, plus project comparison. Aggregate detector performance cannot establish individual-document authorship or justify a surface rule. | Fully covered: `STRATEGY.md`, `human-eyes/references/process.md`, `human-eyes/references/patterns.md`, and `dev/TESTING.md` all separate writing-pattern evidence from authorship classification. | The evidence library lacked this exact ACL 2026 detector-method record. | Add the source card and indexes, explicitly do not promote a prose pattern, and make no product-logic change. Any future use must preserve the binary-detector scope and limitations. | pending | not started |

## Recommendations

- C01: Record the architecture only. Do not add hidden-state or probability-based product logic without a separate product-boundary decision and replication.
- C02: Preserve the latent-feature versus visible-pattern distinction. Do not treat catalogue candidates as proxies for exonic tokens.
- C03: Keep reported detector metrics as background. Directly review and reproduce the code artefact before any adoption decision.
- C04: If approved, add this source to the pending factorial robustness-lane rationale without importing its aggregate score.
- C05: If approved, add separate AI-paraphrase and human-polish cells to a clearly labelled adversarial evaluation lane with factual and semantic checks.
- C06: If approved, add controlled length-band experiments to the separate robustness lane and keep candidate recognition distinct from threshold firing.
- C07: Record the ablation only and take no product action.
- C08: If approved, distinguish evaluator proxy pairs from generators in H25 or the robustness protocol.
- C09: Require sensitivity and layer ablations for any future external-detector evaluation, but do not import the paper's settings.
- C10: Record hardware-scoped runtime only and require comparable end-to-end cost reporting for any reproduction.
- C11: If approved, add graduated provenance and transformation-depth fields before grouping assisted writing in comparative reports.
- C12: If approved, require uncertainty, repeated-run or deterministic-run justification, threshold-selection provenance, deployment-risk and data-governance sections, and an explicit human-evaluation scope statement in detector-research reports.
- C13: Index the source as detector-method evidence and explicitly do not promote it into prose patterns or product logic.

## Evaluation of approved changes

- C01: not applicable while recommendation is pending.
- C02: not applicable while recommendation is pending.
- C03: not applicable while recommendation is pending.
- C04: not applicable while recommendation is pending.
- C05: not applicable while recommendation is pending.
- C06: not applicable while recommendation is pending.
- C07: not applicable while recommendation is pending.
- C08: not applicable while recommendation is pending.
- C09: not applicable while recommendation is pending.
- C10: not applicable while recommendation is pending.
- C11: not applicable while recommendation is pending.
- C12: not applicable while recommendation is pending.
- C13: not applicable while recommendation is pending.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: Codex CLI fresh process, did not perform the extraction
- **Findings resolved:** clarified that C11's human-class treatment is an inference from the binary attack design; separated direct paper results from project inferences; added omitted checklist disclosures on data safeguards, human annotators, and AI-assistant use
- **Unresolved findings:** none
