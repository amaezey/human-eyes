# Paech et al.: AntiSlop Sampler and Antislop

## Metadata

- **URL:** https://github.com/sam-paech/antislop-sampler; https://arxiv.org/abs/2510.15061
- **Author / owner:** Samuel Paech (repository owner); Samuel Paech, Allen Roush, Judah Goldfeder, and Ravid Shwartz-Ziv (paper authors)
- **Published:** Living GitHub repository; paper v1 submitted 2025-10-16, v2 submitted 2025-10-21, and dated 2025-10-23 in the PDF. The pinned repository README states that the paper was accepted at ICLR 2026.
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** academic empirical preprint plus first-party implementation repository and released JSON data lists
- **Evidence tier:** Peer-reviewed / academic empirical and first-party implementation evidence; the reviewed paper artefact is arXiv v2, while acceptance at ICLR 2026 is stated by the pinned repository README rather than established by the arXiv record alone
- **Review mode:** update
- **Stable identifier:** repository commit 0ae330e98fbe6f09351f2d1063a51956378a44b2; arXiv:2510.15061v2; DOI 10.48550/arXiv.2510.15061
- **Version / revision:** current review pins repository commit 0ae330e98fbe6f09351f2d1063a51956378a44b2 and arXiv v2; previous failed review used an unpinned repository-main extraction and the arXiv v2 abstract only
- **Full-text status:** complete
- **Snapshot:** `snapshots/paech-antislop-sampler.md`
- **Extraction method:** cloned the repository over HTTPS and resolved `main` to the recorded commit; preserved a complete `git archive`; preserved all four JSON lists as full raw attachments and included every tracked file in the snapshot with line endings and trailing spaces normalised; downloaded the authoritative arXiv v2 PDF; extracted all 37 pages from the embedded text layer with Poppler `pdftotext -layout`; checked structure with `pdfinfo` and `pdfimages -list`; rendered and visually checked pages 1, 19, and 37 with `pdftoppm`
- **Snapshot SHA-256:** `e43ac522bc4d396ac68196910e4585a2f8a38b3154ac06b045063568c682586d`
- **Model / corpus scope:** English creative writing. The paper generates 2,000 outputs per profiled model, reports primary suppression experiments on Gemma-3-12B, Mistral-Small-3.2, and Llama-3.3-70B, and reports overlap across 67 AI-model fingerprints. Human baselines use `wordfreq` for words and curated Reddit creative writing plus Project Gutenberg text for n-grams. The sampler repository's older notebook separately uses `ajibawa-2023/General-Stories-Collection`; its released 2025-04-07 lists do not record the generating model.
- **Access limitations:** none for the scoped repository and paper. The Markdown snapshot normalises line endings and trailing spaces; the Git archive, PDF, and raw JSON attachments preserve authoritative bytes. The PDF text layer mechanically interleaves some multi-column text, equations, and graph labels, so the preserved PDF remains authoritative for layout and all 16 figures. The paper links a separate `auto-antislop` code repository; it was identity-checked but not recursively ingested because this card's requested boundary is the sampler repository plus the complete paper.

## Summary

The complete source supplies two related but distinct bodies of evidence. The pinned sampler repository contains a backtracking implementation and four full JSON lists totalling 55,063 entries. The paper provides the missing empirical method: model-specific words, bigrams, and trigrams are ranked against human baselines from 2,000 creative-writing outputs per model, with cross-model overlap and suppression experiments reported in tables and figures. This supports corpus-relative, model-aware, genre-aware density work, not a universal blacklist or authorship verdict. The paper also adds strong cautions that the failed record could not assess: judge-based quality metrics, prompt and domain limits, large inference slowdowns, model sensitivity, legitimate-context preservation, dual-use risks, and a recommendation for human review of production banlists.

## Main insights

- The paper computes `fLLM(p) / fhuman(p)` for words, bigrams, and trigrams. Word baselines come from `wordfreq`; n-gram baselines come from Reddit creative writing and Project Gutenberg, with stopwords removed for n-gram processing.
- A model fingerprint uses the top 120 over-represented words and top 40 bigrams and trigrams, with a pattern required to occur in at least three independent writing prompts. Appendix K compares top-200 fingerprints across 67 models and human authors.
- The method is explicitly model-specific and domain-specific. Fingerprints cluster within model families, differ between families, and would need new prompt sets and human baselines outside creative writing.
- The paper gives direct examples rather than abstract-only claims: for Gemma-3-12B, `elara` is reported at 85,513 times the human baseline and `heart hammered ribs` at 1,192 times. It reports `flickered` in 98.5 per cent of 67 model top-word lists and `voice barely whisper` in 68.7 per cent of top-trigram lists.
- The complete JSON files contain 517 default adjustments, 50,046 full-list adjustments, 2,500 phrase-count pairs, and 2,000 word-count pairs. The adjustment files define probability multipliers, while the two dated count files are released without enough provenance to attribute them to the paper's newer profiling pipeline.
- A configured list is not equivalent to empirical support. The sampler README says the default file is mostly auto-generated but supplemented with enthusiast pet peeves, is not curated, and should be replaced with a user's own list.
- The paper's sampler evaluates complete strings or regex matches, backtracks to the first token, and reduces its probability. Soft banning can still permit a requested term when no coherent alternative survives min-p filtering.
- The paper reports 90 per cent normal-condition suppression with full requested use at ban-strength 0.4 in its adversarial phrase-use test. It also reports a 69 to 96 per cent throughput reduction for 1,000 to 8,000-item banlists.
- The paper reports FTPO suppression and capability results across three models, but creative-writing quality is judged by Sonnet 4 and GPT-5 rubrics rather than replicated human ratings. The main Reddit evaluation uses 1,000 held-out prompts from the same source dataset, while the out-of-distribution EQ-Bench comparison uses 96 prompts.
- The paper identifies potential harms to legitimate dialects and minority styles, and possible detector evasion. It uses a whitelist, exposes ban strength, recommends human review, and asks future work to replicate quality results with human raters.
- The paper discloses language-model assistance with early drafting. This is provenance information, not a prose-pattern finding or a reason to discount the reported experiments.

## Evidence and claims to extract

- **Direct source reviewed:** every tracked file at repository commit 0ae330e98fbe6f09351f2d1063a51956378a44b2; all four complete JSON lists; arXiv:2510.15061v2, all 37 pages including methods, five tables, 16 figures, appendices A to M, references, reproducibility, ethics, and AI-use disclosure.
- **Method and sample:** 2,000 English creative-writing outputs per profiled model; model-specific word, bigram, and trigram ratios against `wordfreq`, Reddit creative writing, and Project Gutenberg; stopword removal for n-grams; top-120 word and top-40 bigram/trigram profiles; minimum occurrence across three independent prompts; overlap tables across 67 models. Suppression experiments compare token banning, the sampler, FTPO, and DPO on 1,000 held-out Reddit prompts and 96 EQ-Bench prompts, with 2,000, 4,000, and 8,000-item banlists.
- **Direct versus cited evidence:** C01 to C31 below are direct paper, repository-code, repository-documentation, or released-list observations. Related-work claims about RLHF diversity, DPO failure modes, and prior lexical-constraint methods remain indirect evidence from cited sources and are not promoted through this card.
- **Important limits and counterexamples:** creative-writing scope; changing model fingerprints; unknown generating model and incomplete derivation provenance for the repository's dated lists; hand-curated pet peeves mixed with computed entries; common human names, idioms, narrative beats, and genre conventions; judge-model rather than human quality ratings; only three primary suppression model families; Llama-3.3-70B sensitivity and 66 per cent FTPO suppression; severe sampler throughput loss; production banlists can suppress dialect or legitimate requested language; aggregate ratios cannot establish authorship for one document.

## Matched patterns / rules

- Pattern B1 and `no-ai-vocabulary-clustering`: partly covers clustered static vocabulary and phrases, but not model-specific ratios, minimum support, dates, or creative-writing baselines.
- `overall-signal-stacking`: partly covers vocabulary plus structure aggregation and explicitly avoids one-word authorship claims; it does not implement Paech profiles or weights.
- Patterns A1, A4, E1, and G8: cover some significance, promotional, filler, and conclusion phrases found in the repository lists.
- Pattern B3 and `no-negative-parallelisms`: directly recognises the paper's `not X, but Y` and adjacent contrastive-negation family, with broader live matching than the repository's three-line regex file.
- Patterns F1 and F2: threshold repeated shadow, whisper, silence, and quietness vocabulary; they do not cover all paper-reported low-voice or atmosphere trigrams.
- Agent assessments `formulaic_parallelism`, `generic_metaphors`, and `genre_specific` for fiction: relevant contextual homes for repeated skeletons, stock metaphor families, dialogue, pacing, and endings. Registry inspection is not a complete Audit.
- Pattern B5 `vocabulary-diversity`: conceptually relevant to the FTPO lexical-diversity evaluation, but the paper's aggregate metric combines MATTR-500, Root-TTR, HD-D, and Distinct-1/2/3 rather than validating the project's single-document TTR threshold.

## Associated hypotheses

- H1, continuous calibrated register-distance score per pattern.
- H7, five-check gating plus advisory catalogue.
- H12, genre-aware threshold calibration.
- H24, register-specific vocabulary density.
- H25, model-family versus generic-AI residue.
- H27, performative profundity and aphoristic closure.
