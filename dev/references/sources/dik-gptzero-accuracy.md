# Dik, Erdem, and Dik: GPTZero accuracy by essay length

## Metadata

- **URL:** https://arxiv.org/abs/2506.23517
- **Author / owner:** Selin Dik, Osman Erdem, and Mehmet Dik
- **Published:** 2025-06-30
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** academic preprint / small detector evaluation
- **Evidence tier:** Peer-reviewed / academic empirical, with preprint status and severe reporting limits
- **Review mode:** update
- **Stable identifier:** arXiv:2506.23517v1; DOI 10.48550/arXiv.2506.23517
- **Version / revision:** current review: arXiv v1 submitted 2025-06-30; prior record: the same arXiv v1 retrieved 2026-07-14
- **Full-text status:** complete
- **Snapshot:** `snapshots/dik-gptzero-accuracy.md`
- **Extraction method:** official version-specific arXiv PDF downloaded with `curl`; complete six-page embedded text layer extracted with Poppler `pdftotext -layout`; `pdfinfo` and `pdfimages -list` used for structure; pages 1, 4, 5, and 6 rendered and visually checked; authoritative PDF preserved under `snapshots/attachments/`
- **Snapshot SHA-256:** `1c2de802de9e3847bd63d24cb4a964aa99cb0f6021bd6948f6d70a636507099a`
- **Model / corpus scope:** 78 essays submitted to the GPTZero web product: 50 described as student-written without AI and 28 generated from unspecified random prompts with ChatGPT 3.5 or 4o; essay language, topics, sources, authorship controls, model allocation, generation settings, detector version, submission date, decision threshold, and per-length subgroup sizes are not reported; nominal length scope is 40-800 words, but bin endpoints conflict within the paper
- **Access limitations:** no access barrier; the complete official PDF is preserved. The paper does not release raw essay text, prompts, item-level scores, subgroup counts, GPTZero output records, code, or data, so its calculations and length claims cannot be independently reproduced from the paper.

## Summary

This six-page arXiv preprint tests GPTZero on 28 ChatGPT 3.5/4o essays and 50 human student essays, reports group-mean AI scores by three length bins, and gives one aggregate confusion matrix. It directly reports eight human false positives and no AI false negatives in this sample, but it does not publish raw data, length-stratified confusion counts, statistical tests, detector/version provenance, or enough sample construction detail to establish a correlation between essay length and false positives. The update preserves the unchanged v1 paper and exposes numerical and category inconsistencies omitted from the prior card. The paper is detector-evaluation and caution evidence only; it supplies no prose-pattern evidence and no valid transfer from GPTZero performance to human-eyes checks.

## Main insights

- The reported aggregate confusion matrix is 42 human essays classified human, eight human essays classified AI, zero AI essays classified human, and 28 AI essays classified AI. The paper reports a 16% human false-positive rate and 10.3% overall error rate for this sample.
- Table 1 reports mean GPTZero AI scores of 35.56, 10.29, and 14.75 for short, medium, and long human groups and 99.17, 97.00, and 98.83 for the corresponding AI groups.
- The displayed evidence does not establish the paper's stated length-correlation question. It provides neither per-bin sample sizes and false-positive counts nor raw observations, uncertainty, or a statistical correlation test.
- The prose conflicts with Table 1: it gives the short-human mean as 29.86 rather than 35.56 and says no AI-category mean fell below 98% even though the table reports 97.00 for medium AI essays. The abstract's 91-100% per-essay score range and the conclusion's “around 90-99% accuracy rate” also mix product scores with classification accuracy and do not align cleanly with the table or the 28/28 confusion-matrix result.
- Length definitions conflict across the abstract, methods, tables, and conclusion: short is variously 40-100, 0-100, or below 100 words; medium and long share ambiguous 100 and 350 endpoints; long is variously above 350 or 350-800.
- The authors themselves stop short of a solid correlation, say medium-length outcomes cannot be predicted reliably every time, and ask for larger, mixed human/AI samples and study of other factors.
- The paper's detector result is not evidence for a human-eyes prose rule, severity, threshold, or authorship conclusion.

## Evidence and claims to extract

- **Direct source reviewed:** complete official arXiv:2506.23517v1 PDF, six pages, three tables, two charts, and seven references; the PDF's SHA-256 is `4c5dacf577a28005a6b2acd9b429c855c8d6b8110d85131fa28bbbba49c36e5a`.
- **Method and sample:** 50 essays described as written by students without AI and 28 essays generated from random prompts with ChatGPT 3.5 or 4o; each was pasted into GPTZero and a percentage chance was recorded. The paper does not identify essay sources, topics, dates, author demographics, language explicitly, prompt text, model allocation, generation parameters, GPTZero version, threshold, or subgroup sizes.
- **Direct versus cited evidence:** C01-C11 and C13-C14 concern the paper's own method, reported results, omissions, contradictions, or the review's evidence boundary. C12 is a bundled inventory of seven literature-review claims that are indirect here and were not independently re-reviewed for project use. C11's company-identity correction was checked only against first-party GPTZero and OpenAI pages; those pages are verification context, not separately ingested evidence.
- **Important limits and counterexamples:** the source calls AI essays a control and human essays an experimental group without explaining randomisation; reports group means as “observed counts”; conflates GPTZero percentage scores with classification accuracy in places; supplies no raw data or inference; and contains the numerical, bin-definition, and company-provenance conflicts recorded below. Its only human comparison is the 50-paper aggregate, and it gives no length-stratified confusion matrix.

## Matched patterns / rules

- No direct pattern or agent-assessment match.
- `dev/TESTING.md` additional-corpus controls for provenance, comparable body-prose length, length-normalised reporting, false-positive/confound reporting, and the statement that human-eyes does not classify authorship.
- `human-eyes/references/process.md` Product boundary: human-eyes reports writing patterns and does not infer who or what wrote the text.
- `human-eyes/scripts/grade.py`: `sentence-length-variance` skips only when the input has both fewer than six sentences and fewer than 100 whitespace-delimited words; among non-skipped inputs, fewer than three sentences hard-fails as too few to measure, while inputs with at least three sentences reach sentence-word-count standard deviation and require greater than 4. The generated catalogue says the check is skipped on prose under 100 words and six sentences, which does not fully describe either implementation gate. `paragraph-length-uniformity` considers paragraphs with at least 25 regex words, skips below seven qualifying paragraphs, and flags coefficient of variation below 0.18. `vocabulary-diversity` strips non-ASCII letters, skips below 150 words, and flags type-token ratio at or below 0.40. This paper does not validate any direction or threshold.
- `dev/references/sources/pattern-opportunities.md`: pending graduated-provenance and human-edit/co-writing evaluation lanes from stronger direct sources; this paper adds no mixed-text result.

## Associated hypotheses

- H1, continuous calibrated register-distance score per pattern: adjacent uncertainty and non-binary-output framing only; this paper does not evaluate human-eyes or register-specific distributions.
- H12, genre-aware threshold calibration: adjacent support for controlling text length and reporting scope; the paper does not supply genre-aware human-eyes thresholds.
- H17, calibration golden set, and H19, bootstrap confidence intervals: the paper's missing item-level data and uncertainty illustrate why reproducible labelled samples and interval reporting matter, but provide no direct test of either hypothesis.
- No new hypothesis proposed. Mixed-assistance and length-stratified evaluation are already represented in live testing guidance and pending pattern-opportunity lanes closely enough to avoid duplicate hypothesis wording.
