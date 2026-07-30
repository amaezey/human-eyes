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

## Matched patterns / rules

- `STRATEGY.md` product boundary: human-eyes examines writing patterns and does not determine authorship.
- `human-eyes/references/process.md` product boundary: reports describe constructions and edits, not who or what wrote the text.
- `dev/TESTING.md` comparative-baseline, additional-corpus, provenance, length-matching, weak-case, runtime, and no-authorship requirements.
- H1, H3, H12, H19, and H25 in `dev/hypotheses.md`: calibrated scores, detection-framing caution, register-specific thresholds, uncertainty, and model-family specificity.
- `dev/references/sources/wang-et-al-human-like-text-liked-by-humans.md`: separate coached or adversarial evaluation and preserve exact prompt, model, length, and factuality context.
- `dev/references/sources/xia-stanczak-roth-detector-generalization.md`: prompt, generator, domain, evaluator, and truncation robustness as separate axes in detector generalisation.
- No entry in `human-eyes/scripts/patterns.json` or `human-eyes/scripts/judgement.json` implements hidden-state discrepancy, probability scoring, or binary provenance classification.

## Associated hypotheses

- H1: Continuous calibrated register-distance score per pattern.
- H3: Drop detection framing entirely.
- H12: Genre-aware threshold calibration.
- H19: Bootstrap confidence intervals on corpus claims.
- H25: Model-family versus generic-AI residue.
- Proposed research question, pending user decision: whether provenance labels should distinguish untouched human, lightly AI-polished human, AI rewrite of human, and fresh AI generation before any comparison is reported.
