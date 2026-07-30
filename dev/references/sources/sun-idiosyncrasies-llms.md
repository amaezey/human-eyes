# Sun et al.: Idiosyncrasies in Large Language Models

## Metadata

- **URL:** https://arxiv.org/abs/2502.12150v2
- **Author / owner:** Mingjie Sun, Yida Yin, Zhiqiu Xu, J. Zico Kolter, and Zhuang Liu
- **Published:** submitted to arXiv 2025-02-17; arXiv v2 revised 2025-06-16; ICML 2025 / PMLR 267:57854-57885
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** peer-reviewed conference paper
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** arXiv:2502.12150v2; DOI 10.48550/arXiv.2502.12150; PMLR paper ID pmlr-v267-sun25z; OpenReview FCZ3jVzmTZ; linked implementation Git commit e5333d01493963e5af44288fe2b9343ae6f13b9f
- **Version / revision:** arXiv v2 dated 2025-06-16, compared with the 32-page PMLR version of record, the prior abstract-only snapshot, and the linked implementation commit dated 2025-07-21
- **Full-text status:** complete
- **Snapshot:** `snapshots/sun-idiosyncrasies-llms.md`
- **Extraction method:** official arXiv v2 and PMLR PDFs downloaded with curl; both inspected with pdfinfo and converted from embedded text layers with Poppler pdftotext -layout; arXiv pages 1, 16, and 32 rendered with pdftoppm and visually compared; arXiv HTML and PMLR metadata pages used for structure and bibliographic checks; linked GitHub repository cloned, all seven tracked files read, and commit e5333d01493963e5af44288fe2b9343ae6f13b9f preserved with git archive
- **Snapshot SHA-256:** `b140c388bafb6601f186d420923341c93cac83533ed405ad304d6fe796b764e4`
- **Model / corpus scope:** English outputs from GPT-4o-2024-08-06, Claude-3.5-Sonnet-20241022, Grok-Beta, Gemini-1.5-Pro-002, and DeepSeek-Chat; instruct/base pairs for Meta-Llama-3.1-8B-Instruct and Meta-Llama-3.1-8B, gemma-2-9b-it and gemma-2-9b, Qwen2.5-7B-Instruct and Qwen2.5-7B, and Mistral-7B-Instruct-v0.3 and Mistral-7B-v0.3; plus Phi-4 in preliminary analysis. API responses were generated 2024-11-28 through 2025-02-06; prompt sets are UltraChat, Cosmopedia, LmsysChat, WildChat, and FineWeb; 11,000 sequences per model and prompt set where specified are split into 10,000 training and 1,000 validation sequences; classifier inputs are capped at 512 tokens.
- **Access limitations:** none for the complete paper or the complete tracked tree at the reviewed linked implementation commit. Plain-text extraction flattens two-column order and visual encodings, but both authoritative PDFs preserve them. Linked response datasets, pretrained classifier weights, and external dependency repositories were not preserved or executed; no paper-time software tag exists, so the later linked commit is not asserted to reproduce the exact paper run. The linked repository covers response generation, four classifier backbones, and transformations, but it supplies no ELMo, top-k/top-p control, TF-IDF, similarity, LLM-judge, synthetic-data SFT, or leave-one-model-out analysis script.

## Summary

This ICML 2025 paper measures whether closed-set classifiers can distinguish outputs from named LLMs. It trains sequence classifiers on matched-prompt response sets, then probes model family, prompt distribution, length, formatting, sampling, lexical distributions, semantics, synthetic-data inheritance, and qualitative LLM-judge descriptions. The linked seven-file implementation was also read and preserved at its current two-commit repository head. The strongest contribution to human-eyes is not an authorship rule: it is evidence that some lexical, structural, and semantic distributions are model- and version-specific, survive several surface transformations, and therefore need dated provenance and comparison controls. The paper has no human-written comparison group, no open-world attribution test, and no basis for deciding who wrote an individual document.

## Main insights

- Closed-set model attribution is highly accurate across the tested chat, instruct, and base groups, but accuracy falls within one model family and depends on classifier capacity, training-set size, response length, and the candidate set.
- Model-specific information remains after length and format instructions, special-character removal, word shuffling, paraphrasing, translation, and even summarization; letter distributions alone contribute much less.
- The source directly measures characteristic unigram and bigram choices, first-word distributions, and Markdown-element distributions. Named examples are model- and period-bound, not universal AI vocabulary.
- A null result matters: outputs from one Llama model under different sampling schemes were only weakly separable, so not every generation setting creates a strong signature.
- Post-trained models carry stronger Markdown signatures than base models. The source's ChatGPT and Claude examples overlap some live formatting checks, but the current checks do not measure model-specific distributions.
- Synthetic-data experiments show convergence when two base models receive the same ChatGPT-produced SFT data and separation when a base model is tuned on outputs from different source models.
- The LLM-judge descriptions are qualitative summaries of 35 paired comparisons per pairing. Multiple judges broadly reproduce the ChatGPT-versus-Claude contrast, but these are judge-mediated descriptions rather than human annotations.
- Table 1 reports 97.1% for the five-way chat task, while Tables 10 and 12 use a 97.8% `original` chat baseline; Tables 10 and 12 also report different GPT-4o-mini rewritten-output accuracies. The direction is consistent, but exact baseline and rewrite magnitudes are not internally reconciled or stable enough to promote as thresholds.
- The paper supplies point accuracies without confidence intervals or repeated-seed variance and does not test humans, non-English original generation, unknown-source rejection, or non-Transformer generators.
- The current linked code uses seeded per-label train/test splitting and exact API model names, but does not pin dataset revisions. Its generation CLI defaults temperature to 0 even though the paper specifies 0.6 for base models and the README only recommends passing 0.6. Its pretrained-classifier README reports 95.9%, 87.6%, and 91.9% for instruct, base, and ten-model classifiers, differing from the paper's 96.3%, 87.3%, and 92.2%; the repository does not explain the differences.

## Evidence and claims to extract

- **Direct source reviewed:** the complete 32-page arXiv v2 paper dated 2025-06-16, checked against the 32-page ICML/PMLR paper, arXiv HTML, PMLR metadata, and OpenReview identity; every tracked file in the linked implementation at commit `e5333d01493963e5af44288fe2b9343ae6f13b9f` was read and preserved.
- **Method and sample:** matched prompts are sent to each source model; 11,000 outputs per model and prompt set are split into 10,000 training and 1,000 held-out validation sequences using the same split across models. LLM2vec with a linear classification head and LoRA is the main classifier; ELMo, BERT, T5, and GPT-2 are controls. Chat and instruct models use UltraChat prompts, base models use FineWeb, and OOD tests add Cosmopedia, LmsysChat, and WildChat. API versions and dates are recorded in C02.
- **Direct versus cited evidence:** C02-C20 and the measurements and limits in C22-C25 are direct paper or linked-implementation evidence. C21's proposed leaderboard vulnerability follows from the paper's attribution results, but the claimed simulation feasibility is explicitly attributed to Huang et al. 2025 and remains indirect here. Related-work claims are not promoted as Sun et al. findings.
- **Important limits and counterexamples:** no human comparison; a closed and known candidate set; point estimates without uncertainty intervals; no non-Transformer test; training causes remain open; sampling-method separation is weak; base-model Markdown attribution is near chance; summarization causes a large accuracy drop; qualitative model descriptions are LLM-judge mediated; the main chat baseline, two rewrite tables, and the code README disagree numerically with paper results; main-text model labels differ from Appendix API identifiers; datasets and model weights are linked but not pinned into the code repository; the code does not implement every paper analysis and its temperature default does not reproduce the stated base-model setting without an explicit flag; exact surface phrases may drift with model versions, dates, prompts, language, genre, and post-training.

## Matched patterns / rules

- `no-ai-vocabulary-clustering`, `overall-signal-stacking`, and pattern B1 for aggregate lexical overlap, with substantial scope mismatch.
- `no-collaborative-artifacts`, `no-formulaic-openers`, and `no-soft-scaffolding` for a few named openings and transition phrases, with incomplete coverage.
- `no-boldface-overuse`, `no-inline-header-lists`, `no-excessive-lists`, and patterns C1, C2, and G3 for some Markdown/list behavior.
- `structural_monotony` and `tonal_uniformity` agent assessments for high-level structure and register, not model attribution.
- `human-eyes/references/process.md` Product boundary and `dev/TESTING.md` provenance, matched-register, complete-audit, and cross-version requirements.

## Associated hypotheses

- H24: Register-specific vocabulary density.
- H25: Model-family versus generic-AI residue.
- H12: Genre-aware threshold calibration, as a necessary control rather than evidence supplied by this source.
