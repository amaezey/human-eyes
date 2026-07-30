# Emi and Spero: Technical Report on the Pangram AI-Generated Text Classifier

## Metadata

- **URL:** https://arxiv.org/abs/2402.14873
- **Author / owner:** Bradley Emi and Max Spero; Pangram Labs
- **Published:** 2024-02-21 (v1); reviewed revision submitted 2024-07-29 and dated 2024-07-30
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** vendor-authored technical preprint and self-evaluation
- **Evidence tier:** Vendor / detector pages
- **Review mode:** update
- **Stable identifier:** arXiv:2402.14873v3; DOI 10.48550/arXiv.2402.14873
- **Version / revision:** current review: arXiv v3 submitted 2024-07-29; prior record: arXiv v3 abstract page retrieved 2026-05-05
- **Full-text status:** complete
- **Snapshot:** `snapshots/pangram-classifier.md`
- **Extraction method:** official arXiv v3 PDF and source bundle downloaded with `curl`; all 15 PDF pages extracted with Poppler `pdftotext -layout`, rendered with `pdftoppm`, and visually checked; experimental arXiv HTML used for structure comparison; paper-linked benchmark CSV downloaded from Amazon S3 and inspected with Python's CSV parser
- **Snapshot SHA-256:** `1a1c3446f21f59df815eff28df53709e55eb7c23c923baec617fa69b576b40ce`
- **Model / corpus scope:** original 1,976-document English benchmark reports GPT-3.5 Turbo 0301/1106, GPT-4 0613, GPT-4 Turbo 1106, Gemini Pro, Mistral 7B Instruct, Mixtral 8x7B Instruct, and Llama 2 70B Chat across blog posts, books, creative writing, email, news, Q&A, reviews, scientific writing, student writing, and Wikipedia; July 2024 additions report GPT-4o, Claude 3, Llama 3, seven unseen open-source models, and seven non-English languages; training uses approximately 28 million pre-2022 human documents and synthetic mirrors
- **Access limitations:** no access barrier to the complete paper, arXiv source bundle, or linked 1,976-row benchmark CSV. The report does not release the training corpus, trained classifier, detector predictions or scores, analysis code, confidence intervals, product build identifiers, calibration details, or enough subgroup metadata to reproduce its reported performance.

## Summary

This 15-page Pangram Labs arXiv preprint describes a modified transformer classifier trained with synthetic mirrors and hard-negative mining, then reports vendor-run comparisons with GPTZero, Originality.ai, and DetectGPT. The update replaces an abstract-only record with the complete v3 paper, all seven figures, six tables, the algorithm, the 1,976-row public benchmark CSV, and the arXiv source bundle. The paper contributes dated evaluation-design ideas and a strong warning against sole-arbiter use, but not independently replicated detector accuracy or interpretable prose-pattern evidence. Its own released CSV conflicts with the paper's eight-model, evenly-across-domains account, and the displayed metrics contain additional internal inconsistencies. Human-eyes already rejects authorship classification; this source does not justify a checker, severity, threshold, current-performance claim, or origin verdict.

## Main insights

- Pangram reports 99.85% overall accuracy, 0.19% false positives, and 0.11% false negatives on its 1,976-document benchmark, but these are vendor self-evaluation point estimates without uncertainty, run artefacts, detector-build provenance, or independent replication.
- The public CSV has exactly 1,976 rows and all ten domains, but it contains 1,048 human and 928 AI labels, nine generator tags rather than the table's eight, non-uniform model-by-domain counts, and no detector outputs. It therefore does not reproduce the paper's performance claims.
- The source's strongest reusable method idea is to match AI examples to human topic, length, tone, and domain, remove easy packaging artefacts, and evaluate model/domain transfer separately. This is a test-design candidate, not prose-pattern evidence.
- Reported low false-positive rates on three English-learner datasets are narrower than the conclusion that the classifier is not biased against non-native English writers; subgroup fairness, proficiency, language background, and false-negative parity are not evaluated.
- The paper directly discourages using any detector as the sole arbiter of academic integrity and says detector output cannot establish factuality. That aligns with human-eyes' existing no-authorship and source-verification boundary.
- The only visible cues named are the unquantified examples `delve`, `it is important to note`, and `as an AI language model`. They are author observations, not measured feature effects or validated origin rules.

## Evidence and claims to extract

- **Direct source reviewed:** complete arXiv:2402.14873v3 PDF, 15 pages; sections 1-7; Figures 1-7; Tables 1-6; Algorithm 1; footnotes and references; the 13-file arXiv source bundle; and the paper-linked 4,537,550-byte benchmark CSV with 1,976 rows.
- **Method and sample:** vendor-authored classifier self-evaluation; original benchmark contains 1,976 human and AI documents from ten English text domains and dated 2023-2024 generators; separate reported evaluations cover three English-learner corpora, held-out Enron email, seven unseen open-source generators, a 25,000-document July 2024 generator update, and seven non-English languages. Training begins from approximately 28 million human documents dated 2021 or earlier, holds out approximately four million, creates topic/length/style-matched synthetic mirrors, and iteratively mines false positives.
- **Direct versus cited evidence:** C01-C19 and C21-C23 concern the paper, preserved figures/tables/source bundle, or released benchmark. C20 bundles detector, probability-feature, bias, watermark, and paraphrase claims inherited from cited work; those claims are indirect here and are not treated as new evidence. C19's visible-cue examples are direct author observations but have no supplied counts, comparison, ablation, or causal analysis.
- **Important limits and counterexamples:** no independent review or replication; incomplete architecture, training, calibration, competitor-version, and run provenance; no confidence intervals or significance tests despite a figure caption saying `significantly`; public data lacks predictions and conflicts with Table 1; several prose numbers conflict with displayed figures; subgroup results omit sample construction and uncertainty; July updates are absent from the February 2024 CSV; source-cleaning removes easy artefacts; all claims are dated to v3 and the named conditions.

## Matched patterns / rules

- `human-eyes/SKILL.md` and `human-eyes/references/process.md`: human-eyes identifies constructions and never classifies authorship; source claims and qualifications must be preserved.
- `dev/TESTING.md`: matched human/AI provenance, comparable length or length-normalised reporting, genre/register controls, complete-Audit requirement, false-positive/confound reporting, immutable revision records, and the explicit statement that human-eyes does not classify authorship.
- `human-eyes/scripts/grade.py` and `human-eyes/scripts/patterns.json`: `no-ai-vocabulary-clustering` includes `delve` but needs three recognized words in one paragraph to flag; `no-filler-phrases` flags `it is important to note` at one occurrence; `no-collaborative-artifacts` does not recognize `as an AI language model` in the focused control. Surface-only output remains incomplete.
- `dev/references/sources/pattern-opportunities.md`: the current Pangram/Spero-Emi row proposes domain coverage and synthetic mirrors for evaluation and fixture design, not pattern evidence; the refreshed source narrows that proposal with accounting, version, prediction, and uncertainty requirements.
- No live classifier, origin score, Pangram integration, or detector threshold exists in human-eyes.

## Associated hypotheses

- H1, continuous calibrated register-distance score: adjacent support for threshold-aware comparison and uncertainty requirements, but Pangram does not evaluate human-eyes or publish uncertainty.
- H3, drop detection framing entirely: the paper's ethics section supports non-sole-arbiter caution, while its classifier objective is outside human-eyes' product boundary.
- H9, similar-species disambiguation, and H12, genre-aware threshold calibration: domain, language, and human-look-alike controls are relevant, but the vendor report supplies no human-eyes thresholds.
- H19, bootstrap confidence intervals: the absence of intervals and run-level variation illustrates an evaluation requirement, not evidence for a numeric setting.
- H25, model-family versus generic-AI residue: the dated generator differences and later model update support recording model/build/date, not a model-family verdict.
- No new hypothesis proposed; the live hypotheses and pending detector-robustness lanes already cover the defensible research questions.
