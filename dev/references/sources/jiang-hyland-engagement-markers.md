# Jiang and Hyland: Engagement markers in ChatGPT-generated argumentative essays

## Metadata

- **URL:** https://journals.sagepub.com/doi/10.1177/07410883251328311
- **Author / owner:** Feng (Kevin) Jiang and Ken Hyland
- **Published:** 2025-04-30 online; 2025-07 in Written Communication 42(3), pp. 463-492
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** peer-reviewed corpus study; complete author accepted manuscript reviewed
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** DOI 10.1177/07410883251328311; UEA eprint 97952; accepted-manuscript DOCX SHA-256 74c25cbd1df63d6f4ecc6cfc29cf134b7692036b0684fe5f77f6b1e3e945d3b1
- **Version / revision:** current UEA author accepted manuscript, DOCX core revision 426, modified 2024-12-05T20:00:00Z; prior library snapshot retrieved 2026-05-05 and archived unchanged at SHA-256 ce48e0ac5932c1ba4350be5d45a46e58ed763b02cb526cf2046494de52dd0d87
- **Full-text status:** complete
- **Snapshot:** `snapshots/jiang-hyland-engagement-markers.md`
- **Extraction method:** UEA accepted-manuscript DOCX text extraction with textutil, python-docx, and OOXML footnote inspection
- **Snapshot SHA-256:** `c2eef38f5867353fe9e3918af17c3a2af3a58ae37725722389374a71f9174afc`
- **Model / corpus scope:** 145 English argumentative essays generated with the authors' label "ChatGPT 4.0" and 145 English argumentative essays by second-year British university students from LOCNESS; 72,819 versus 78,060 tokens; eight named topic families; prompts specified role, persuasive style, topic, and about 500 words, but the generation date, model build, sampling settings, full prompt set, and outputs are not reported
- **Access limitations:** complete 37-page accepted manuscript, six tables, two footnotes, references, and appendix were accessible. Publisher HTML exposed only abstract, references, biographies, and metadata without subscription access, and the direct publisher PDF returned HTTP 403, so Version of Record copy-editing differences were not compared. The underlying essay corpora, full prompt set, model build/date/settings, analysis data, and code were not supplied with the manuscript.

## Summary

This peer-reviewed corpus study compares 145 argumentative essays generated under the authors' "ChatGPT 4.0" label with 145 second-year British university student essays from LOCNESS. It searches about 100 candidate expressions across five reader-engagement categories, manually verifies their function, and reports substantially fewer total markers in the ChatGPT corpus, with especially large differences for questions and personal asides. The direct evidence is aggregate, English, model-, prompt-, period-, topic-, and genre-bound. It supports a contextual academic-argument review prompt, not an authorship classifier, universal absence rule, causal account of model cognition, or claim that more markers necessarily improve an essay.

## Main insights

- The direct headline comparison is 393 engagement cases, or 5.40 per 1,000 words, in the ChatGPT corpus versus 1,326, or 16.99 per 1,000 words, in the student corpus (LL 471.98, %DIFF 68.23, p below .001).
- Five functional categories were reviewed: reader mentions, questions, appeals to shared knowledge, directives, and personal asides. Manual concordance checking matters because forms such as obligation modals, `obvious`, parentheses, and imperatives do not always address a reader.
- ChatGPT produced six questions and no personal asides, compared with 134 questions and 91 asides in the student corpus. The source treats these as its clearest engagement-depletion results.
- Directives formed similar shares of each corpus's engagement inventory, but their normalized rates were lower in ChatGPT. The overview table also reports similar reader-mention shares, but that comparison is numerically unsafe because its student subtotal conflicts with the subtype table. ChatGPT relied almost entirely on inclusive `we/our/us` among reader mentions and on obligation modals among directives.
- Appeals to shared knowledge were a larger share of ChatGPT's smaller engagement inventory, not more frequent overall: 1.28 versus 1.59 per 1,000 words. Almost all ChatGPT knowledge appeals concerned tradition or typicality; none were classified as logical-reasoning appeals.
- ChatGPT's category-level standard deviations and dispersion values were generally narrower. The paper interprets this as less variation, but does not turn it into a document-level threshold; its unexplained personal-aside DP of 0.30 despite raw, normalized, and SD values of zero makes that dispersion row unsafe for reuse.
- The authors explicitly say that more interactional devices do not necessarily mean a better text, that students are not expert writers and may overuse engagement, and that both corpora use more engagement than research-article corpora reported by cited work.
- Prompt wording is a stated confound. The authors used iterative prompt refinement and acknowledge, without testing, that `argumentative` and `persuasive` may have changed the generated feature mix.
- The accepted manuscript contains a material internal table conflict: the overview table reports 499 student reader mentions (6.39 per 1,000 words), while the subtype table reports 721 inclusive forms plus 78 second-person forms, totaling 799 (10.24 per 1,000). It also gives ChatGPT personal asides a DP of 0.30 despite zero raw, normalized, and SD values, duplicates the Koubaa reference block after the corpus table, says ChatGPT contained the engagement categories despite zero asides, and labels two early tables as Table 1. These values and integrity anomalies are unsafe to reuse without clarification or a Version of Record comparison.
- Claims that statistical generation causes audience blindness, reduced higher-order thinking, or a preference for coherence over asides are author interpretation or cited context, not causal tests in this study.

## Evidence and claims to extract

- **Direct source reviewed:** complete University of East Anglia author accepted manuscript for DOI 10.1177/07410883251328311, DOCX SHA-256 `74c25cbd1df63d6f4ecc6cfc29cf134b7692036b0684fe5f77f6b1e3e945d3b1`, core revision 426; publisher and Crossref metadata were checked separately.
- **Method and sample:** 145 LOCNESS essays by second-year British university students and 145 ChatGPT essays on matched topic families; 78,060 and 72,819 tokens respectively. The authors used TagAnt, AntConc, about 100 candidate engagement items, manual functional filtering, normalization per 1,000 words, log-likelihood tests with a 3.8 cutoff at p=.05, and %DIFF. Both authors independently coded a random 10% of engagement expressions, reporting 97% agreement before resolving disagreements.
- **Direct versus cited evidence:** C01-C12 and C17 describe the study's own method, counts, examples, cautions, and internal inconsistencies. C13 distinguishes the authors' causal interpretation from the measured comparison. C14 records the authors' pedagogical proposals. C15 is a project inference about what the study does not validate. C16 inventories relevant claims inherited from cited literature rather than measured here.
- **Important limits and counterexamples:** no generation date, exact model build, sampling settings, complete prompt set, outputs, released corpus, analysis code, preregistration, blinded coding statement, confidence intervals, multiple-comparison discussion, or document-level classifier evaluation is reported. Topics are heterogeneous but topic-stratified results are absent. The LOCNESS essays lack references despite their formal style, so they do not support H10's citation-checking branch. The prompt was iteratively refined. Students are not expert writers and may overuse markers. More markers do not necessarily improve quality. The study deliberately focuses on an interactional feature that the authors concede the program might be expected to handle poorly. The student reader-mention tables conflict, the personal-aside DP conflicts with the zero count/rate/SD, the Koubaa block is duplicated, and the conclusion's statement that ChatGPT contained the engagement categories conflicts with the reported zero personal asides.

## Matched patterns / rules

- H10 `genre_specific`, academic sub-record in `human-eyes/scripts/judgement.json`: direct conceptual coverage for an argumentative essay with depleted questions, reader engagement, or stance markers; the generated catalogue also names reader address and personal asides.
- H7 `neutrality_collapse`: not a match. Engagement markers concern overt reader alignment, while H7 concerns stance erasure and balanced framing. The prior mapping is retired.
- `human-eyes/SKILL.md` product boundary and `human-eyes/references/process.md`: reports constructions and editing issues without classifying authorship or inventing personal detail.
- `dev/evals/tests/test_judgement_json.py`: confirms H10 is a registered composite, context-warning agent assessment with academic and student-essay branches; it does not validate source-specific recall, specificity, or thresholds.

## Associated hypotheses

- H12, genre-aware threshold calibration: directly relevant because the paper's comparison is specific to argumentative academic/student essays and warns that genre changes engagement rates.
- H25, model-family versus generic-AI residue: relevant because the paper uses an underspecified "ChatGPT 4.0" label and omits generation date/build/settings, preventing transfer to current or generic model claims.
- Proposed source-bound evaluation question: do the five engagement categories and their functional subtypes separate matched current-model and human argumentative essays after controlling topic, prompt, length, proficiency, and deliberate rhetorical choices?
