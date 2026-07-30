# Ju, Blix, and Williams: Domain Regeneration

## Metadata

- **URL:** https://aclanthology.org/2025.findings-acl.120/
- **Author / owner:** Da Ju, Hagen Blix, and Adina Williams
- **Published:** 2025-07
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** peer-reviewed conference paper
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** ACL Anthology ID 2025.findings-acl.120; DOI 10.18653/v1/2025.findings-acl.120; arXiv:2505.07784v2
- **Version / revision:** current authoritative 22-page ACL 2025 proceedings PDF; prior 2026-05-05 ACL landing-page/Jina capture
- **Full-text status:** complete
- **Snapshot:** `snapshots/ju-blix-williams-domain-regeneration.md`
- **Extraction method:** official ACL PDF downloaded with `curl`; all 22 pages converted from the embedded text layer with Poppler `pdftotext -layout`; PDF metadata and image inventory inspected with `pdfinfo` and `pdfimages -list`; pages 1, 5-8, 11, and 22 rendered with `pdftoppm` and visually compared; ACL HTML, arXiv API metadata, and the arXiv v2 PDF cross-checked
- **Snapshot SHA-256:** `33b381404724efb7515ef94c6409fd7eff0c85a101828fac011d261b9410566f`
- **Model / corpus scope:** English Wikipedia, CCNews, and ELI5; about 6.4M, 0.6M, and 0.6M human articles respectively in the parse-depth descriptive table; main Llama-2-70B-Instruct regenerations plus Llama-3.3-70B-Instruct, Llama-3.1-8B-Instruct, Mistral-Small-24B-Instruct-2501, and Ministral-8B-Instruct-2410 comparisons; first 256 Wikipedia words, first 180 CCNews words, or ELI5 title supplied to vLLM at default temperature 1.0
- **Access limitations:** none for the paper. The authoritative ACL PDF and arXiv v2 PDF are preserved. The ACL landing-page abstract and arXiv API summary still describe two domains, while both full PDFs describe and evaluate three domains including ELI5. Plot pixels remain in the preserved PDFs; captions, embedded labels, tables, prompts, examples, appendices, and all page text are in the snapshot.

## Summary

This peer-reviewed ACL paper introduces domain regeneration: models continue the beginning of a human-domain document, allowing large human and regenerated corpora to be compared while partly controlling topic and content. Across English Wikipedia, CCNews, and ELI5, the authors measure sentence length, article readability, unique dependency tags, constituency-tree depth, Yngve score, and unique constituency labels. The most stable direct result is distributional rather than lexical: regenerated text is usually less variable and has a reduced right tail, while mean direction depends on domain, metric, and sometimes model. The paper also gives qualitative Llama-2 examples of American spelling normalization, Wikipedia value judgments, factual errors, invented quotations and acronyms in news, and essay-like or promotional endings. These observations are model-, prompt-, language-, domain-, and date-bound; they do not validate a single-document authorship rule.

## Main insights

- Regenerated distributions usually narrow and lose part of the human right tail, but neither effect is universal: ELI5 parse depth is the explicit no-narrowing result, and dependency-tag distributions have no human long tail to reduce.
- Means do not move in one generic AI direction. Llama outputs tend to increase complexity means for Wikipedia and CCNews but match or reduce them for ELI5; some model-specific exceptions occur.
- The authors interpret the mean pattern as domain-complexity overshoot, not collapse to a neutral middle. This is an interpretation of measured distributions, not a directly tested training mechanism.
- Sentence length, readability, dependency-tag count, parse depth, Yngve score, and constituency-label count are separate metrics. The paper does not reduce its result to sentence-length standard deviation.
- The full paper adds ELI5, multiple Llama and Mistral variants, cleaning ablations, prompts, exact descriptive tables, nulls, limitations, and qualitative examples omitted by the prior abstract-only record.
- Qualitative examples show Americanization of British spelling, Wikipedia neutrality failures, factual mistakes, invented quotations and acronyms, explicit `In conclusion` wrap-ups, praise, sales copy, and reader address. These are manual observations, not prevalence estimates.
- The default decoding temperature was 1.0. Effects of other temperatures, including effects on the long tail, were not tested.
- Tooling and parsing can fail on extreme or malformed text. Uniform application may limit bias, but the paper does not quantify residual measurement error.
- The paper suggests possible synthetic-text detection use, but it does not train or evaluate a detector, choose thresholds, report document-level classification accuracy, or establish authorship.
- The current ACL and arXiv metadata abstracts are stale relative to their own PDFs: metadata says two domains; the PDFs say and evaluate three.
- Appendix I adds an anecdotal comparison: human CCNews examples appeared less similar to Llama continuations than the two Llama generations appeared to each other. This is illustrative, not a measured similarity result.

## Evidence and claims to extract

- **Direct source reviewed:** authoritative ACL proceedings PDF for 2025.findings-acl.120, 22 pages, printed pages 2367-2388; compared with the 22-page arXiv:2505.07784v2 PDF and current first-party metadata.
- **Method and sample:** observational corpus analysis of English Wikipedia, CCNews, and ELI5. The main system is Llama-2-70B-Instruct, with Llama-3.3-70B-Instruct, Llama-3.1-8B-Instruct, Mistral-Small-24B-Instruct-2501, and Ministral-8B-Instruct-2410 in subsets. Human and regenerated corpora contain roughly 0.6M-6.6M articles per listed condition, with tens to hundreds of millions of successfully parsed sentences. Stanza supplies dependency and constituency parses; vLLM generation uses temperature 1.0. Wikipedia and CCNews prompts include the first 256 and 180 words and target at least 700 and 500 words; ELI5 receives only the title and targets at least 100 words.
- **Direct versus cited evidence:** C01-C26 and C29 are direct methods, results, examples, interpretations, or limits from this paper. C27 records claims inherited from cited work on model collapse, token/topic diversity, and POS-template homogeneity. C28 records the paper's comparison with Russell et al.'s detector tips. Neither cited source was ingested as part of this source boundary.
- **Important limits and counterexamples:** no known training inventory; no random decoding-temperature comparison; no non-English data; no closed-model results; no human-authorship classification evaluation; metric availability depends on successful parsing; article-level and sentence-level denominators differ; cleaning excludes fewer than 10% of CCNews and fewer than 15% of Wikipedia on average; readability is calculated on uncleaned articles over 100 words; Appendix A's raw-versus-filtered plots cover only dependency-tag and constituency-label counts for Wikipedia and CCNews, while depth/Yngve ablations are not plotted; ELI5 depth variance is the study's one clear no-narrowing case; dependency-tag results have no long-tail reduction because the human distribution is near-normal; qualitative examples are anecdotal.

## Matched patterns / rules

- H22 `Long-tail compression and grammatical standardisation`: direct conceptual home for C05-C12, but still open and unimplemented.
- G9 `sentence-length-variance`: partial coverage of C06 and only coarse adjacency to C07-C12; it computes within-document sentence-word-count standard deviation, not corpus mean shift, parse distributions, or right-tail loss.
- H13 `Sentence-length mean as a grader check` and H12 `Genre-aware threshold calibration`: research homes for the mean and domain-specific direction, both open and unimplemented.
- G8 `no-signposted-conclusions`: exact coverage for line-initial `In conclusion` in C17/C19. Focused checks failed on that phrase as expected.
- E4 `no-generic-conclusions`, A4 `no-promotional-language`, A1 `no-significance-inflation`, and H2 `no-tidy-paragraph-endings`: partial or challenged coverage for C16-C20. Focused checks caught `testament` in one CCNews ending and line-initial `In conclusion`, but missed the ARKit sales ending, `His legacy endures`, the article `A` wrap-up except when isolated at line start, and the factual errors.
- H10 `genre_specific`, journalism branch, plus source-grounding and closed-source process guidance: manual coverage for C18-C20's unverifiable quotations, unsupported claims, and factual checks.
- H25 `Model-family versus generic-AI residue`: appropriate caution for the Llama-2 qualitative examples and other model comparisons; not an implemented attribution feature.

## Associated hypotheses

- H12 Genre-aware threshold calibration
- H13 Sentence-length mean as a grader check
- H22 Long-tail compression and grammatical standardisation
- H25 Model-family versus generic-AI residue
