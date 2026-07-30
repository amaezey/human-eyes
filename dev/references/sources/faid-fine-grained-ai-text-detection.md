# FAID: Fine-Grained AI-Generated Text Detection Using Multi-Task Auxiliary and Multi-Level Contrastive Learning

## Metadata

- **URL:** https://aclanthology.org/2026.eacl-long.151/
- **Author / owner:** Minh Ngoc Ta, Dong Cao Van, Duc-Anh Hoang, Minh Le-Anh, Truong Nguyen, My Anh Tran Nguyen, Yuxia Wang, Preslav Nakov, and Dinh Viet Sang
- **Published:** March 2026
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** peer-reviewed empirical conference paper
- **Evidence tier:** peer-reviewed / academic empirical
- **Review mode:** new
- **Stable identifier:** DOI 10.18653/v1/2026.eacl-long.151; ACL Anthology ID 2026.eacl-long.151
- **Version / revision:** EACL 2026 final proceedings version, pages 3275-3296
- **Full-text status:** complete
- **Snapshot:** `snapshots/faid-fine-grained-ai-text-detection.md`
- **Extraction method:** official ACL paper and Responsible NLP Checklist PDFs downloaded with `curl`; all 22 paper pages and both checklist pages extracted with Poppler `pdftotext -layout`; structure checked with `pdfinfo`; paper pages 1, 11, and 22 rendered with `pdftoppm` and compared visually
- **Snapshot SHA-256:** `f5cd67a72607965547246d891909390ef774a9e811417dd5f200a591b6e707e6`
- **Model / corpus scope:** FAIDSet has 83,350 academic texts in English and Vietnamese from arXiv abstracts, Vietnam Journals Online abstracts, and Hanoi University of Science and Technology theses. Generated and collaborative texts use GPT-4/4o, Llama 3.x, Gemini 2.x, and DeepSeek V3/R1 families; held-out generator tests use Qwen, Mistral, and Gemma. The three main labels are human-written, LLM-generated, and human-LLM collaborative, with collaborative data including polishing, continuation, and paraphrasing. Corpus acquisition and generation dates are not reported.
- **Access limitations:** None for the paper or official checklist. The text extraction is mechanically interleaved in places because of the two-column PDF, and raster chart labels are most reliably preserved in the attached official PDF. The user queue title, "FAID: Fine-grained AI-generated Text Detection", omits the subtitle "Using Multi-Task Auxiliary and Multi-Level Contrastive Learning" found in the authoritative work.

## Summary

Ta et al. introduce FAIDSet, an 83,350-item English and Vietnamese academic-text dataset, and FAID, an XLM-RoBERTa-based three-way authorship classifier with multi-level contrastive learning, an auxiliary classification objective, and fuzzy k-nearest-neighbor retrieval. The study tests fully human, fully LLM-generated, and several human-LLM collaborative categories across known and held-out domains and model families. It adds direct evidence about academic Gemini phrase clusters, model-family variation, edited collaborative text, and the difference between frozen out-of-distribution classification and test-time retrieval adaptation. Its strongest relevance to human-eyes is evaluation design and source-scoped pattern evidence, not a transferable authorship detector or product threshold.

## Main insights

- FAIDSet contains 83,350 examples: 20,252 human-written, 17,252 LLM-generated, and 45,846 human-LLM collaborative items across train, validation, and test splits.
- The data covers only two academic domains, paper abstracts and student theses, and two languages, English and Vietnamese. Human sources include 2,000 arXiv abstracts, 2,195 VJOL abstracts, 4,898 English HUST thesis passages, and 11,159 Vietnamese HUST thesis passages.
- The collaboration label collapses polishing, continuation, and paraphrasing into one class. The authors state that this does not exhaust deeply mixed or more complex workflows.
- FAID reports 95.58% accuracy on FAIDSet, 96.99% on the adapted LLM-DetectAIve dataset, and 96.73% on HART for three-label classification. These are benchmark classifier results, not human-eyes metrics.
- Out-of-distribution results are uneven. Accuracy is 62.78% for an unseen IELTS domain, 93.31% for unseen Qwen, Mistral, and Gemma generators on known-domain abstracts, and 66.55% when both domain and generator are unseen.
- A manually revised set of 400 unseen collaboration samples yields 84.8% accuracy. Five annotators corrected spelling, replaced words, and refined fluency while retaining source meaning, so the result is evidence that this detector retained some signal after light human editing in this specific academic setup.
- A five-volunteer user study reports 88.5% accuracy on 200 allegedly authentic co-writing samples produced with ChatGPT, Gemini, DeepSeek, and Llama 3.1. The paper's stated arithmetic is unclear: five volunteers times four systems times five outputs per model gives 100, not 200, unless an unstated second factor is counted.
- The method treats each LLM family as an author. Appendix D supports this with limited length, trigram, and embedding analyses, strongest for three Gemini variants and a Gemini-versus-GPT comparison, rather than a comprehensive causal demonstration across every named family.
- Figure 5 directly reports recurrent academic trigrams in 500 arXiv-prompted outputs from each of three Gemini variants. Repeated items include "the efficacy of", "this work presents", "presents a novel", "introduces a novel", "a significant advancement", "the proposed method", and "empirical evaluations demonstrate".
- Gemini variants produced shorter, more tightly clustered output lengths than GPT-4o/4o-mini and Llama-3.3 on 2,000 arXiv prompt seeds per model. Length is therefore model-family and prompt/domain scoped here, not a general AI-versus-human rule.
- Generation prompts explicitly request formal, compelling, impactful, professional, information-dense, and significance-forward academic prose. The authors also acknowledge that FAIDSet under-represents in-the-wild tool chains. These prompts can create the very phrase and style distributions later attributed to generators.
- Generation quality control samples only 10-20 items per domain, source, and generator combination. Observed repetition, incomplete reasoning, and formal-expression overuse led to prompt or parameter changes, but the paper does not report a fixed blind protocol, rejection counts, or before-and-after distributions.
- The classifier alone loses 15-30% on unseen data. The final system then embeds unseen items and adds them to a temporary vector database for fuzzy-neighbor inference. This is test-time adaptation using the evaluation distribution, not a strictly frozen detector generalizing without access to unseen test items.
- The paper's limitations name synthetic construction, narrow low-resource and niche-domain coverage, and failure when one text blends several LLM families. Its ethics section warns against high-stakes use without human oversight and calls for continuing fairness audits.
- English accuracy is 96.41% and Vietnamese accuracy is 94.42% on FAIDSet, but two languages and no uncertainty estimates cannot establish broad multilingual robustness.
- The official checklist says the authors used GitHub Copilot and Cursor for code optimization but did not mention that use in the paper. The checklist also identifies human annotation and consent, while reporting no external recruitment and no ethics-review approval or exemption.

## Evidence and claims to extract

- **Direct source reviewed:** EACL 2026 final proceedings paper, DOI 10.18653/v1/2026.eacl-long.151, pages 3275-3296, plus the official two-page Responsible NLP Checklist.
- **Method and sample:** Three-way authorship classification over 83,350 English and Vietnamese academic texts. FAID uses an unsupervised SimCSE XLM-RoBERTa-base encoder, multi-level contrastive loss, auxiliary binary classification, a vector database, and fuzzy k-nearest neighbors. Main evaluation covers FAIDSet, adapted LLM-DetectAIve, HART, a 150-source IELTS unseen-domain set, a 150-source unseen-generator abstract set, 400 manually revised collaboration items, and a reported 200-item five-volunteer user study. Training uses 50 epochs on one NVIDIA A100, with one reported result per setting and no error bars.
- **Direct versus cited evidence:** C01-C14 are based on this paper's dataset, prompts, experiments, appendices, limitations, ethics text, and official checklist. Background claims about prior detector failures, authorship accountability, transparency, and other datasets are cited evidence and are not promoted from this card without direct review of the cited work.
- **Important limits and counterexamples:** The dataset is synthetic by construction, academic-only, two-language, and built from prompt templates that impose target styles. Corpus dates and independent verification that all human-source text is free of undisclosed AI assistance are absent. Quality control changed prompts after observed failures. The real-world-study sample count is not reconcilable from the stated factors. Family-level analysis is narrow, test-time vector adaptation is transductive, mixed use of several LLM families remains difficult, and the paper supplies no uncertainty estimates across repeated runs.

## Matched patterns / rules

- `STRATEGY.md`: rejects document authorship classification and treats patterns as writing evidence, not provenance verdicts.
- `dev/TESTING.md`: requires prompt and source provenance, register variation, length controls, packaging normalization, complete Audits, explicit version references, and separate treatment of coached or humanized samples.
- `no-ai-vocabulary-clustering`, `no-significance-inflation`, `no-copula-avoidance`, `no-forced-triads`, `no-filler-phrases`, `no-superficial-ing`, and `overall-signal-stacking`: adjacent current checks that fired on the paper or its reproduced prompts in a surface-only run, but they do not directly cover Figure 5's recurrent Gemini trigrams.
- `sentence-length-variance`, `paragraph-length-uniformity`, and `vocabulary-diversity`: document-level distribution checks, not equivalents of model-family output-length distributions or trigram frequencies.
- `genre_specific` academic assessment: checks source integrity, citations, and evidence quality; it does not classify collaboration or model family.

## Associated hypotheses

- H3, drop detection framing entirely.
- H9, field-guide voice with similar-species disambiguation.
- H12, genre-aware threshold calibration.
- H19, bootstrap confidence intervals on corpus claims.
- H21, low information density and wrong sentence subject.
- H22, long-tail compression and grammatical standardisation.
- H24, register-specific vocabulary density.
- H25, model-family versus generic-AI residue.
- Proposed extension to H25: distinguish frozen generalization from transductive or retrieval-based test-time adaptation, and require family claims to name the specific variants, prompts, domains, and dates observed.
