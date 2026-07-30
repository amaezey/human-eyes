# Murray and Tersigni: Can instructors detect AI-generated papers?

## Metadata

- **URL:** https://jalt.open-publishing.org/index.php/jalt/article/view/1895
- **Author / owner:** Nathan Murray and Elisa Tersigni
- **Published:** 2024-07-21; publisher PDF says available online 2024-07-22
- **Retrieved:** 2026-07-16
- **Extracted:** 2026-07-16
- **Source type:** peer-reviewed empirical study
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** DOI 10.37074/jalt.2024.7.2.12
- **Version / revision:** publisher PDF, Journal of Applied Learning & Teaching 7(2), pages 155-167; prior reviewed capture was the same DOI and substantive article text, retrieved 2026-05-05
- **Full-text status:** complete
- **Snapshot:** `snapshots/murray-tersigni-ai-generated-papers.md`
- **Extraction method:** publisher PDF download plus Poppler `pdftotext` and embedded-image transcription
- **Snapshot SHA-256:** `4c61e54756cea774b91d7f77bba292ec2058216797e1178128ead9196f9f2f52`
- **Model / corpus scope:** two English student essays submitted to an August 2022 first-year composition course before public ChatGPT release; two English essays generated with ChatGPT3.5 editions dated 2023-01-30 and 2023-02-13 on 2023-02-06 and 2023-03-03; one generated with the assignment prompt alone and one with three refinement prompts; twenty experienced postsecondary writing instructors interviewed in Canada, the United States, and New Zealand in March-April 2023
- **Access limitations:** none for the 13-page article, figures, table, appendix prompt, rubric, and references; the four essay texts, participant-level ratings, interview transcripts, questionnaire, analysis code, and underlying data are not published or linked in the article

## Summary

This small mixed-method study asked twenty experienced postsecondary writing instructors to grade four anonymized first-year composition essays and classify two pre-ChatGPT student essays and two dated ChatGPT3.5 essays. It directly reports grading, classification, self-reported knowledge and confidence, interview rationales, teaching practices, and perceptions. The generated essays averaged slightly higher grades and had stronger spelling and grammar but weaker evidence, yet only 35% of instructors classified all four correctly. The useful human-eyes evidence is therefore bounded: the study supports academic and student-writing review of evidence, references, reasoning, cross-rubric unevenness, and known-writer baselines, while its own false positives show that cue labels such as formulaic, bland, clean, and robotic are not authorship proof. The sample is preliminary, dated, geographically concentrated, and does not publish the essays or participant-level data.

## Main insights

- Two ChatGPT3.5 essays averaged 72.5% and two student essays 70.44%; the guided ChatGPT essay received the highest mean grade, 75.5%, while the unguided ChatGPT essay and one student essay were the lower-scoring pair.
- The generated essays were rated highly for spelling and grammar and poorly for evidence. Both generated essays used entirely fabricated references, although the paper says their deliberately general claims were not false.
- The abstract says generated essays scored lower in argumentation, but Figure 2 shows the two generated essays with ten excellent and three needs-improvement argumentation ratings, versus four excellent and five needs-improvement ratings for the two student essays. The methods and results also call the four levels excellent, good, fair, and needs improvement, while the appendix rubric labels the last two below average and ineffective.
- Only seven of twenty instructors classified all four essays correctly. Per-essay AI classifications included both false positives and false negatives.
- Mean classification confidence was 3.2 of 5, with median 3 and standard deviation 1.01. Self-reported knowledge and confidence did not meaningfully predict classification accuracy, and the most confident participant classified only one essay correctly.
- Instructors named fake or poor references, formulaic writing, bland or robotic prose, spelling and grammar, repetition, superficial analysis, gut instinct, and lack of evidence. They also applied stereotyped AI descriptions when they had actually selected student work.
- The authors propose unevenness across rubric categories as a possible flag. That is an interpretation of four essays, not a validated threshold or standalone rule.
- Familiarity with a student's prior writing was described as potentially useful, but the experiment did not test instructors on their own students. A baseline shift can prompt review; it cannot establish authorship.
- The article's detector limits, software false-positive claims, EAL detector-bias claim, ChatGPT-4 consistency and hedging claims, and no-foolproof-software conclusion rely on cited work rather than tests conducted in this study.
- The direct teaching interviews show mixed practice, policy, and opinion, including disagreement about which stages of writing should remain independent. The paper's policy and pedagogical recommendations are author interpretation, not outcome-tested interventions.
- The study is preliminary: twenty instructors, four essays, two ChatGPT3.5 generations from early 2023, no student participants, no released essay texts or row-level data, and no test of current models, editing, detector software, or real-course authorship decisions. The authors make an untested ChatGPT 4o source-behaviour assertion and anomalously say the study was designed before the release of "ChatGPT-3," a model/version wording ambiguity that the paper does not resolve.

## Evidence and claims to extract

- **Direct source reviewed:** complete first-party publisher PDF for DOI 10.37074/jalt.2024.7.2.12, 13 pages, five figures, Table 1, full references, appendix essay prompt, and appendix rubric; after whitespace normalization, the current PDF extraction and archived 2026-05-05 article body were byte-identical at 69,746 characters with SHA-256 `3784c28d052793bde6988f4ed35499be5251c02433279ef532feaae77e114943`, while the refreshed snapshot adds current provenance, reading-order extraction, and complete embedded-image transcription.
- **Method and sample:** twenty current college or university composition instructors, seventeen in Canada, two in the United States, and one in New Zealand; 70% had taught more than five years, 65% at least eleven years, and 60% four or more courses in the preceding year. Interviews ran in March-April 2023. Participants graded four equally formatted English essays against argumentation, evidence, organization, and spelling and grammar, then classified authorship and completed a semi-structured interview. Two essays were August 2022 first-year student submissions and two were dated ChatGPT3.5 outputs.
- **Direct versus cited evidence:** C01-C20 and C24-C28 are direct design, results, author interpretation, or limitations from this article. C21 separates detector, EAL, sentence-consistency, grammatical-variation, and hedging claims inherited from cited studies. C22-C23 are the authors' recommendations, not tested intervention outcomes. C25 is a prediction. No cited source was promoted as direct human-eyes evidence in this refresh.
- **Important limits and counterexamples:** two human and two generated essays cannot establish a reusable prose taxonomy or threshold; essay bodies and row-level data are unavailable; instructors did not grade their own students; the model builds and prompts are dated; the source's "ChatGPT-3" limitations wording is ambiguous; one high-scoring and one lower-scoring essay occurred in each authorship group; the abstract's lower-argumentation statement conflicts with Figure 2; rating-level labels differ between the methods/results and appendix rubric; instructor stereotypes were sometimes applied to student work; confidence and knowledge regressions were null; no student participants were interviewed; and the study did not test detectors, editing, current models, or intervention effectiveness.

## Matched patterns / rules

- H10 `genre_specific` academic branch: fake, broken, or irrelevant citations; wrong citation details; unsupported claims; polished academic surface masking weak evidence or generic argument.
- H10 `genre_specific` student-essay branch: weak reasoning, unsupported claims, abrupt change from a known student baseline, and surface polish masking weak reasoning.
- H9 `no-rubric-echoing`: inspected implementation in `grade.py`; it matches seven boilerplate phrase families only after three candidates. The source does not test those phrases. A source-cue sample containing formulaic, repetitive, fake references, clean grammar, superficial analysis, bland, robotic, and lack of evidence returned zero rubric-echo candidates in a surface-only audit.
- Product boundary in `human-eyes/references/process.md` and the root README: the Audit describes patterns and editing problems and does not infer authorship.
- H3 `Drop detection framing entirely`: the classification errors and cited detector cautions support the hypothesis's epistemic concern but do not decide the product-positioning question.
- H12 `Genre-aware threshold calibration`: the narrow first-year composition register and dated model scope support register-specific evaluation, not a threshold.
- H21 `Low information density and wrong sentence subject`: weak evidence and superficial analysis are adjacent, but this source neither measures sentence-level information density nor identifies sentence subjects.
- H22 `Long-tail compression and grammatical standardisation`: the paper's speculative homogenization discussion is adjacent only; it supplies no structural distribution measurement.
- `pattern-opportunities.md` candidate `Student-writing argument/evidence quality`: the source directly supports the evidence-quality and false-positive boundary, with the qualifications in this card.

## Associated hypotheses

- H3: Drop detection framing entirely.
- H12: Genre-aware threshold calibration.
- H21: Low information density and wrong sentence subject, adjacent only.
- H22: Long-tail compression and grammatical standardisation, adjacent and speculative only.
