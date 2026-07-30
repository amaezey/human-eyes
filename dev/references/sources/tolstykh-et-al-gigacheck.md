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
