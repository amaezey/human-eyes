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

## Skill-use audit

- **Good use:** record a small, dated example of detector false positives; reinforce caution against relying solely on a detector; use the reporting omissions as evaluation-design prompts for provenance, length opportunity, mixed-assistance labels, subgroup counts, uncertainty, and non-authorship wording.
- **Misuse / overclaim:** saying the paper proves a correlation between length and false positives, that medium-length human text is reliably safe, that GPTZero is generally 100% sensitive, or that any GPTZero score transfers to human-eyes.
- **Unsupported use:** no lexical, syntactic, structural, formatting, tone, rhythm, or workflow-residue rule; no threshold or severity; no claim about languages, domains, current GPTZero versions, mixed-authorship performance, population accuracy, causal length effects, fairness, or individual authorship.
- **Underused evidence:** the live testing guide already controls length opportunity and rejects authorship classification, while its separate evaluation lanes could explicitly record mixed-assistance depth and length bins if Mae approves a protocol. This paper supplies only a future-work prompt for those lanes, not outcome evidence.
- **Patterns left on the table:** none. The source contains no prose-pattern examples or measured textual features.

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

## Questions / follow-up

- No source-access question remains; arXiv lists only v1 and the complete official PDF is preserved.
- If the detector results are ever used beyond this record, obtain the 78 essays, item-level GPTZero scores and labels, per-bin counts, prompts, model allocation, detector version/date/threshold, and sampling/authorship documentation from the authors.
- Directly ingest any cited detector study before using its reported result for a project recommendation; C12 remains indirect.
- Mae must disposition every pending row C01-C14. C03 and C10 are the only rows that propose an optional evaluation-protocol choice: a separately labelled length-stratified and mixed-assistance lane. No checker or guidance change is recommended from the reported GPTZero outcomes.

## Update provenance

The reviewed source revision is unchanged. The prior snapshot did not record its own SHA-256 in the card or manifest; this update computed the digest from the exact prior bytes, archived that file, and separately verified that the prior snapshot's recorded PDF SHA-256 matches the newly downloaded official v1 PDF. The complete extracted source body is byte-for-byte unchanged between the archived and current snapshots. The current snapshot replaces only the old five-line provenance wrapper, adds the current `SNAPSHOT_TEMPLATE.md` fields and beginning/middle/end verification, and adds the preserved PDF attachment; no source text was removed or corrected.

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | arXiv:2506.23517v1 | `snapshots/archive/dik-gptzero-accuracy/2026-07-14-arxiv-2506.23517v1.md` | 2026-07-14 | `16b9595a4e40fccee5d28d2c82ae4de1fc7df3e3a0a54838fa85610c8027ac7d` |
| current | arXiv:2506.23517v1; DOI 10.48550/arXiv.2506.23517 | `snapshots/dik-gptzero-accuracy.md` | 2026-07-15 | `1c2de802de9e3847bd63d24cb4a964aa99cb0f6021bd6948f6d70a636507099a` |

## Decision history

- The prior v1 card had four unkeyed recommendations and no recorded user-decision or implementation statuses: make no prose-check change; consider mixed human/AI and AI-edited-human samples; optionally inspect results by length; and retain the detector findings without turning them into a human-eyes restriction. No product diff or verification was recorded. This update replaces those untracked rows with C01-C14. The no-rule and record-only positions remain substantively unchanged; the mixed/length proposal is now bounded by the paper's lack of mixed-text data, lack of length-stratified error counts, and current project coverage. All decisions are therefore `pending` and all implementation states are `not started`.

## Project coverage

This is the authoritative review table. `fully covered`, `partly covered`, and `not covered` describe the live project's treatment of the source claim, not whether the source result is correct.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: The study asks whether GPTZero false positives correlate with essay length and hypothesises that incorrect flags decrease as length increases. | Direct statement of purpose and hypothesis; not a result. Scope is the paper's 78 essays and unspecified GPTZero instance. | H12 and `dev/TESTING.md` length-opportunity controls; partly covered as an evaluation concern, not as a detector claim. | No item-level analysis, correlation coefficient, hypothesis test, or human-eyes evidence. | Record the hypothesis as unconfirmed; take no product action. Verification: source-record validation only. | pending | not started |
| C02: The sample comprises 50 student essays described as written without AI and 28 essays generated from random prompts with ChatGPT 3.5 or 4o. | Direct method statement. The sample sources, topics, author controls, prompt text, model allocation, settings, dates, and selection process are not reported. | `dev/TESTING.md` requires source/generation provenance, prompt constraints, comparable lengths, and confound reporting; partly covered. | The paper's sample cannot be reconstructed or audited, and “random” is not operationalised. | Record the sample and provenance limits; do not import its labels or rates into project evaluation. Verification: none beyond the source record. | pending | not started |
| C03: Essays are divided into short, medium, and long groups. | Direct method, but bin definitions conflict: 40-100 versus 0-100 versus under 100; 100 and 350 endpoints overlap or are ambiguous; long is above 350 versus 350-800. No per-bin counts are reported. | `dev/TESTING.md` requires comparable body lengths or length-normalised results. Live `grade.py` partly covers length opportunity: sentence variance skips only when both `<6` sentences and `<100` whitespace words, then hard-fails non-skipped inputs with `<3` sentences, and otherwise requires SD `>4`; paragraph uniformity needs seven paragraphs of at least 25 regex words; vocabulary diversity needs 150 ASCII-letter words. The sentence catalogue omits the second gate and describes a simpler short-text skip than the code. | No standard evaluation bins, mixed-assistance stratification, or documented boundary rule connects the paper to human-eyes; the live measures are feature-specific gates, not evidence for GPTZero's length claim. | Test-adapt only if Mae approves: specify non-overlapping bins, per-bin counts, matched genres, and raw plus length-normalised complete-Audit results in a separate evaluation lane. | pending | not started |
| C04: Table 1 reports mean AI scores by length: human 35.56/10.29/14.75 and ChatGPT 99.17/97.00/98.83 for short/medium/long. | Direct displayed group means. The paper calls them “observed counts” although they are percentages; it gives no subgroup sizes, distributions, uncertainty, or raw values. | No human-eyes mechanism consumes GPTZero scores; not covered by design. | These opaque product scores cannot calibrate human-eyes checks or severity. | Record only; do not map the means to a pattern, threshold, or authorship statement. | pending | not started |
| C05: The abstract says AI-essay scores range from 91-100%; the Results prose says the short-human mean is 29.86 and no AI-category mean is below 98%; the conclusion calls an “around 90-99%” score an “accuracy rate.” | Direct source statements. Table 1 instead gives 35.56 for short human and 97.00 for medium AI, while Table 3 reports 28/28 AI classifications. The paper conflates per-essay or group-mean GPTZero scores with classification accuracy. | No project coverage; this is source-quality and evidence-category evidence. | The paper provides no correction, raw data, score-to-label threshold, or version after v1 to reconcile the 91-100, 90-99, 97.00, and 28/28 statements. | Preserve every stated range and contradiction as unresolved; do not select a preferred value or treat product scores as accuracy without author data. | pending | not started |
| C06: The aggregate confusion matrix is 42 true human, eight human misclassified as AI, zero AI misclassified as human, and 28 AI classified as AI; the paper reports a 16% human false-positive rate and 10.3% overall error rate. | Direct Table 3 and accompanying prose for this sample. No uncertainty, repeat runs, threshold, or detector version is supplied. | `dev/TESTING.md` requires false-positive and confound reporting but does not benchmark GPTZero; partly covered as reporting guidance only. | The aggregate matrix cannot reveal which length bins produced errors or generalise to other models, domains, languages, populations, detector versions, or mixed text. | Record as a dated sample result only; take no product action. | pending | not started |
| C07: The authors say short and long human essays are more inaccurate or false-positive-prone than medium essays, while AI essays are detected well regardless of length. | Direct author interpretation. Table 1 supports only the ordering of mean human scores; the paper gives no per-bin classification counts, raw scores, statistical test, or stable threshold. | H1/H12 and `dev/TESTING.md` support calibrated, register-aware, length-aware project evaluation; partly covered. | The false-positive-by-length claim is not demonstrated by the displayed evidence, and no transfer to human-eyes is valid. | Record the claim as under-supported; do not adopt its direction as a human-eyes expectation. | pending | not started |
| C08: The conclusion says medium-length results still fluctuate, no solid correlation has been established, and other factors may matter. | Direct limitation and null/unresolved result. The authors name page count and font size as examples but test neither. | H12, H17, H19, and `dev/TESTING.md` confound and provenance requirements; partly covered. | The paper does not identify or measure the other factors. | Preserve the null and uncertainty; take no product action from speculative factors. | pending | not started |
| C09: The authors advise educators to exercise caution rather than rely solely on AI detectors. | Direct author recommendation, bounded to detector use in education. | `human-eyes/references/process.md` Product boundary and the `dev/TESTING.md` non-authorship statement fully cover the applicable project principle. | No project gap. The paper does not evaluate human-eyes reports or interventions. | Take no further action; retain as detector-caution context. | pending | not started |
| C10: Future work should use more human and AI texts, include mixed human/AI text, investigate false-positive causes, and examine factors beyond word count. | Direct future-work proposal, not a measured result. Mixed text and extra factors were not tested. | The committed corpus includes AI rewrites of human originals; `pattern-opportunities.md` already holds pending graduated-provenance, human-edit, and co-writing lanes from direct sources; partly covered. | No agreed mixed-assistance taxonomy, construction protocol, per-span ground truth, or length-stratified complete-Audit design. | Test-adapt only if Mae approves a separate protocol; cite this paper as motivation, never as performance evidence. | pending | not started |
| C11: The Introduction says GPTZero was “made by the makers of ChatGPT.” | Direct source statement. First-party identity checks on 2026-07-15 identify GPTZero's co-founders as Edward Tian and Alex Cui and the official ChatGPT app publisher as OpenAI, so the paper's company-provenance statement is false. | No product coverage; this is a source factual-error boundary. | The error weakens confidence in the paper's product context but does not by itself invalidate the displayed experiment. | Record the correction; do not reproduce the claim in project guidance. Verification context: `https://gptzero.me/team` and `https://help.openai.com/en/articles/8167604`. | pending | not started |
| C12: The literature review reports that Walters tested 42 ChatGPT and 42 first-year-student essays across 16 detectors and found GPTZero identified 81% while “wrongfully identifying” 4%; Liu et al. tested 50 rehabilitation articles and 50 ChatGPT articles and reported 70% GPTZero AI identification; Elkhatat et al. tested 15 ChatGPT-3.5 paragraphs, 15 ChatGPT-4 paragraphs, and five human controls and found detectors more successful on 3.5; Popkov and Barrett compared more than 100 older behavioural-health/psychiatry articles with 100 Claude/ChatGPT essays and found commercial detectors less accurate than assumed; Akram compared six detectors without a result stated here; Perkins et al. submitted 20 ChatGPT texts to Turnitin and the review reports 95% “containing AI” versus 45% “generated using AI”; Foltýnek et al. compared six detectors for machine-obfuscated plagiarism and the review says OPT rewording of a few paragraphs can push similarity below Turnitin's threshold. | All seven are indirect claims as worded by Dik et al. This update preserved their references but did not independently ingest or validate their numbers, dates, task definitions, or interpretations. | Some detector-caution concepts overlap existing source cards and project guidance, but these inherited claims are not mapped from this conduit; not covered for decision use. | Directness and accuracy remain unresolved; the review conflates AI detection, plagiarism detection, similarity thresholds, product scores, and classification. | Record only. Ingest the relevant primary paper separately before any claim affects a recommendation. | pending | not started |
| C13: The paper reports no raw essays, item scores, prompts, subgroup sizes, inference, detector/version/date/threshold, repeated runs, code, or data. | Directly verified absence from the complete v1 paper; reviewer inventory, not an author claim. These omissions block reproduction and population inference. | `dev/TESTING.md` provenance, immutable-version, complete-Audit, false-positive, and confound requirements fully cover the applicable reporting standard. | The source record can name the gap but cannot repair the study. | Record the limitations; take no product action and do not use the point estimates as release evidence. | pending | not started |
| C14: The paper evaluates a commercial detector's document scores and labels; it identifies no words, constructions, formatting habits, rhythms, tones, or workflow residue. | Evidence-category boundary established by a complete source scan. This is reviewer interpretation of what the source does not contain. | Live patterns and agent assessments have no direct match; fully covered by leaving them unmapped. | No missing prose check. Detector accuracy is a different task from auditing unwanted writing patterns. | Do not adopt any prose rule, severity, threshold, or authorship inference from this source. | pending | not started |

## Recommendations

- C01: Record the length hypothesis as unconfirmed; no product change.
- C02: Retain the sample and provenance limitations; do not import labels or rates.
- C03: If Mae wants a length lane, test-adapt it with non-overlapping bins, per-bin counts, matched genres, and raw plus length-normalised complete-Audit results.
- C04: Record the displayed group means only; do not map them to human-eyes.
- C05: Preserve both numerical contradictions as unresolved; do not silently choose a value.
- C06: Retain the aggregate confusion matrix as a dated sample result only.
- C07: Mark the length interpretation under-supported and do not adopt its direction.
- C08: Preserve the null/uncertainty and speculative-factor boundary; no product change.
- C09: Take no further action because live process and testing guidance already prohibit authorship conclusions.
- C10: If Mae approves, test-adapt a separate mixed-assistance protocol with transformation-depth provenance and per-span ground truth; cite this source only as future-work motivation.
- C11: Record the GPTZero/ChatGPT company-provenance correction; do not repeat the false statement.
- C12: Treat all seven literature-review claims as indirect until their primary sources receive separate ingestion.
- C13: Record reproducibility limits; do not use these point estimates as release evidence.
- C14: Do not add or alter a pattern, check, agent assessment, severity, threshold, or guidance from this paper.

## Evaluation of approved changes

- C01: not applicable - pending record-only recommendation; no product change requested.
- C02: not applicable - pending record-only recommendation; no product change requested.
- C03: not applicable - pending evaluation-protocol decision; no implementation started.
- C04: not applicable - pending record-only recommendation; no product change requested.
- C05: not applicable - pending source-integrity disposition; no product change requested.
- C06: not applicable - pending record-only recommendation; no product change requested.
- C07: not applicable - pending record-only recommendation; no product change requested.
- C08: not applicable - pending record-only recommendation; no product change requested.
- C09: not applicable - pending take-no-further-action recommendation.
- C10: not applicable - pending evaluation-protocol decision; no implementation started.
- C11: not applicable - pending record-only correction; no product change requested.
- C12: not applicable - pending direct-review requirement; no product change requested.
- C13: not applicable - pending record-only recommendation; no product change requested.
- C14: not applicable - pending do-not-adopt recommendation; no product change requested.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: dik_gptzero_review_3 (fresh final re-review); earlier read-only reviews: dik_gptzero_review_1 and dik_gptzero_review_2
- **Findings resolved:** six total: removed an unsupported language assertion; inventoried all seven indirect literature-review claims and numbers; added the abstract/conclusion score ranges and score-versus-accuracy conflict; reopened `grade.py` and recorded the exact sentence-variance, paragraph-uniformity, and vocabulary-diversity gates plus the sentence-check catalogue/code mismatch; reconciled the pending-decision wording; and added the residual non-skipped fewer-than-three-sentences hard-fail. Reviewer 1 reported five findings, reviewer 2 reported one, and fresh reviewer 3 reported zero.
- **Unresolved findings:** none
