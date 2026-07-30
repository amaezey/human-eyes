# A Systematic Analysis of Linguistic Features in AI-Generated Text Detection Across Domains and Models

## Metadata

- **URL:** https://arxiv.org/abs/2606.04177
- **Author / owner:** Yassir El Attar, Esra Dönmez, Maximilian Maurer, and Agnieszka Falenska
- **Published:** 2026-06-02
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** academic preprint with large-scale empirical corpus analysis
- **Evidence tier:** Peer-reviewed / academic empirical; this version is a preprint and is not identified as peer reviewed
- **Review mode:** new
- **Stable identifier:** arXiv:2606.04177v1; DOI 10.48550/arXiv.2606.04177
- **Version / revision:** v1, submitted 2026-06-02
- **Full-text status:** complete
- **Snapshot:** `snapshots/el-attar-linguistic-features-ai-text-detection.md`
- **Extraction method:** official arXiv v1 PDF downloaded and preserved; all 30 pages extracted from the embedded text layer with `pdftotext -layout`; pages 1, 15, 24, 25, and 30 rendered and visually checked
- **Snapshot SHA-256:** `c554e78921648b6a498fa559a9c65818355eed1bb42c6b1acb4bad1125abdc07`
- **Model / corpus scope:** English MAGE benchmark continuations from 27 models in seven families (OpenAI GPT, LLaMA, GLM-130B, FLAN-T5, OPT, BigScience, and EleutherAI) across ten domains, with a GPT-4 test set from four additional domains; 284 interpretable linguistic features; separate ChangeMyView data from GPT, LLaMA, and Mistral for a prompt and model-alignment pilot
- **Access limitations:** none for full text; arXiv HTML returned 404, so the official PDF was used. Multi-column text and chart labels are mechanically interleaved in places, and some symbol fonts are transformed. The preserved PDF is authoritative for layout and figures.
- **Queue title note:** the user queue title, "A Systematic Analysis of Linguistic Features", is an abbreviated form. The authoritative URL carries the longer title used for this card.

## Summary

This arXiv preprint tests whether 284 interpretable linguistic features can distinguish human and AI-generated English text across models and domains. It trains linear SVM classifiers on the MAGE benchmark, evaluates eight in-domain and out-of-domain testbeds, and uses feature-area ablations to study robustness. Its strongest contribution to human-eyes is twofold. It reinforces the need for model- and domain-aware evaluation, and it directly challenges the live `vocabulary-diversity` check's one-way assumption that AI prose has lower type-token ratio. Lexical-richness features are highly informative as a group, but their direction, usefulness, and interaction with other features vary with text length, domain, model family, and evaluation setting.

## Main insights

- A linear classifier using only linguistic features achieves 0.827 Macro F1 in the mixed in-domain setting and 0.808 on the four-domain GPT-4 test, but falls to 0.588 on unseen text-domain and model-family pairs. Aggregate success therefore hides substantial transfer failures.
- Model-family and text-domain effects are large. In the most difficult paired transfer test, Macro F1 ranges from 0.345 to 0.889 across the 70 held-out domain-model combinations.
- Appendix E reports near-zero pairwise TTR correlations across model families. Those results show weak co-variation across domains, but they do not by themselves establish distance or clustering between family distributions. The paper uses the same near-zero pattern to support both distinct family regions and similar LLaMA-OpenAI patterns, so that interpretation needs caution.
- Lexical richness is the most consistently important feature area. Removing its three features drops Macro F1 from 0.827 to 0.696 in the mixed in-domain test and from 0.808 to 0.531 in the four-domain GPT-4 test.
- The paper's TTR results challenge the current project direction. Its aggregate plots place human text around 0.6 and AI text around 0.8, and its three XSum examples report human TTR from 0.271 to 0.292 versus AI TTR from 0.558 to 0.694. The live check flags only low TTR.
- The paper also contains an internal contradiction: it says humans have higher values across all three lexical-richness features and calls that greater diversity, then immediately reports higher TTR for AI. Its figures and qualitative examples support the higher-AI-TTR direction, while hapax counts are higher for the much longer human passages.
- Length is a major confound in the selected XSum examples. Human passages contain 822 to 1,191 tokens while AI continuations contain 108 to 190, so raw TTR and absolute hapax counts cannot be imported as fixed document thresholds.
- Lexical-only classifiers can outperform the full 284-feature set in some out-of-domain settings, yet they underperform the full set on nearly all matched in-domain domain-model pairs. Other feature groups sometimes add signal and sometimes add noise.
- SQuAD is an important counterexample: removing lexical richness barely changes or slightly improves performance in several settings. DialogSum is another, with morphology and information features actively reducing performance while semantic features help.
- A small ChangeMyView pilot suggests model-family alignment matters more than prompt formulation. The reverse cross-dataset Macro F1 rises from 0.435 to 0.850 when training and test data are restricted to shared OpenAI and LLaMA families. This is a limited pilot, not a general prompt-effect estimate.
- The source is English-only, excludes the newest models, does not factorially test prompt variation in the main MAGE experiments, and relies on one feature toolkit plus linear SVMs. The findings are aggregate classifier evidence, not individual-document authorship rules.
- Background claims about prior stylometric cues remain cited evidence unless this paper measures them directly. The ablation results support feature groups and condition dependence, not universal directions for every surface, syntactic, emotion, readability, or psycholinguistic feature.
- The paper discloses GitHub Copilot use for code completion and Grammarly use for spelling and grammar correction. This is provenance information, not evidence that the paper's prose or results are AI-generated.

## Evidence and claims to extract

- **Direct source reviewed:** arXiv:2606.04177v1, all 30 pages, including methods, eight testbeds, full results, limitations, ethical considerations, references, appendices A to F, 16 tables, 22 figures, qualitative examples, and the AI-assistance disclosure.
- **Method and sample:** MAGE continuation-prompt data contains 93,318 human and 194,839 AI training instances, 28,799 human and 24,151 AI validation instances, and 28,741 human and 24,226 AI test instances across ten English domains. The paper evaluates 27 models in seven families and a separate GPT-4 test over CNN/DailyMail, DialogSum, IMDb, and PubMed. It extracts 284 features in 11 areas, standardises them, trains class-weighted linear SVMs, and reports Macro F1, AUROC, and average recall. Feature importance is studied with leave-one-area-out and cumulative ablation. A separate ChangeMyView corpus contains 157,880 human comments and roughly 13,500 outputs from each of GPT, LLaMA, and Mistral.
- **Direct versus cited evidence:** C01 to C12 below are direct design, result, limitation, inconsistency, ethics, or provenance claims from this paper. C13 records related-work claims inherited from cited studies and does not treat them as direct evidence.
- **Important limits and counterexamples:** unseen paired transfer reaches 0.345 Macro F1 in the weakest cell; SQuAD shows little lexical-richness dependence; DialogSum benefits from removing some feature groups; lexical-only models reverse from harmful in matched in-domain evaluation to helpful in some out-of-domain settings; TTR direction is internally described inconsistently; selected human and AI passages differ sharply in length; prompt variation is only piloted on ChangeMyView; the benchmark is English-only and does not include the newest models; near-zero TTR correlations are overinterpreted as feature-space separation and similarity; results are correlational classifier and ablation evidence, not causal proof or individual-document diagnosis.

## Matched patterns / rules

- `vocabulary-diversity` / pattern B5 in `human-eyes/scripts/grade.py`, `human-eyes/scripts/patterns.json`, and `human-eyes/references/patterns.md`: direct conceptual match for TTR, but the paper challenges the fixed low-TTR direction and exposes length, domain, and model dependence.
- `sentence-length-variance` / pattern G9 and `paragraph-length-uniformity`: members of the broader surface and structural feature family, but the paper does not validate their live thresholds and often finds non-lexical areas condition-dependent or noisy.
- `genre_specific` and `even_jargon_distribution` in `human-eyes/scripts/judgement.json`: partial context coverage for genre and within-document terminology distribution; neither supplies the paper's domain-model ablation evidence.
- `overall-signal-stacking`: conceptually compatible with multifeature evidence, but the paper's SVM and ablation results do not validate the project's pattern weights or document-level aggregate threshold.
- `STRATEGY.md`: fully aligned on treating patterns as inspectable writing evidence rather than authorship classification.

## Associated hypotheses

- H1, continuous calibrated register-distance score per pattern.
- H3, drop detection framing entirely.
- H12, genre-aware threshold calibration.
- H22, long-tail compression and grammatical standardisation.
- H24, register-specific vocabulary density.
- H25, model-family versus generic-AI residue.
- Proposed follow-up: length-adjusted lexical richness should be evaluated as a multidimensional, condition-specific feature family before any fixed direction or threshold is retained.
