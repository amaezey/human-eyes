# Waltzer, Cox, and Heyman: Can teachers detect AI-generated student essays?

## Metadata

- **URL:** https://doi.org/10.1155/2023/1923981
- **Author / owner:** Tal Waltzer, Riley L. Cox, and Gail D. Heyman
- **Published:** 2023-06-26
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** Peer-reviewed controlled human-judgement study with public stimuli, survey materials, data, and analysis code
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** DOI 10.1155/2023/1923981; Article ID 1923981; NSF PAR record 10493551; OSF node 8qv6z
- **Version / revision:** Current: nine-page publisher-typeset article for DOI 10.1155/2023/1923981, deposited in NSF PAR as `Accepted Manuscript`, plus OSF node state last modified 2023-04-29; previous: same DOI in a 2026-05-05 contract-incomplete extraction
- **Full-text status:** complete
- **Snapshot:** `snapshots/waltzer-teachers-detect-ai-essays.md`
- **Extraction method:** Complete NSF PAR PDF downloaded and inspected with `pdfinfo`; all nine pages converted from the embedded text layer with Poppler `pdftotext -layout`; pages 1, 5, and 9 rendered and visually checked; Figures 1 and 2 restored from the rendered PDF and matching OSF workbooks; Crossref metadata and all 17 files in the public OSF supplement inspected
- **Snapshot SHA-256:** `a2e8c41447a78fc9b074b77e8313bbc1e3246d706a7863bd15041b80f63ecee2`
- **Model / corpus scope:** Public ChatGPT responses generated 2023-02-02; exact model/build not disclosed; 50 generated English essays and 50 edited high-school-student essays across two 4-6-sentence prompts; judgement sample 69 high-school teachers and 140 high-school students, with student data from ten classes at one school and teacher school count not reported, six forced-choice pairs per participant, collected 2023-02-27 through 2023-03-06
- **Access limitations:** Direct Wiley `pdfdirect` and Crossref-listed Hindawi PDF/XML routes returned HTTP 403; the complete article was recovered from NSF PAR. The linked AsPredicted PDF returned HTTP 406, but the public OSF package contains the dated one-page analysis plan. The OSF node declares no licence, so its files were inspected but not copied into the repository.

## Summary

This peer-reviewed study tested whether 69 high-school teachers and 140 high-school students could distinguish short student essays from public-ChatGPT responses in six paired forced choices. Teachers averaged 70% and students 62%, both above 50% chance, but 84% of teachers and 87% of students missed at least one pair. Confidence, English expertise, and prior ChatGPT experience did not significantly predict accuracy in this task. Slightly higher-rated student essays were harder to distinguish, and participant comments named possible cues such as `overall` and transition words without validating those cues. The evidence supports bounded caution about short student-writing judgements, human look-alikes, cue policing, and model/task drift. It does not provide a document-level authorship rule, a current-model result, a reliable cue taxonomy, or a threshold for human-eyes.

## Main insights

- The task measured six paired forced choices, not independent-document classification. It cannot supply conventional false-positive, false-negative, sensitivity, specificity, or document-authorship rates.
- Teachers averaged 70% and students 62%; both groups were above chance, teachers performed better, and most participants still made at least one error.
- Pre-task confidence and post-task estimated score did not predict overall accuracy. In the trial model, confidence was dichotomised as greater than 50 versus 50 or lower and was not significant; 13 participants with missing confidence were omitted. These nulls are bounded to this short task and do not prove training could never help.
- Subject familiarity, prior English teaching, and prior ChatGPT experience also did not significantly predict accuracy.
- Correct trials contained student essays with a mean teacher grade of 85.47, versus 86.72 on incorrect trials. The 1.25-point association does not establish that ChatGPT writes better in general.
- The authors suggest that polished student prose can be a human look-alike. Vague or idiosyncratic language may also have cued student authorship, but those examples are interpretive, not validated features. Two graders separately coded all 50 selected student essays for `student-specific language`; 4 were marked by at least one grader and 2 by both, but the article and released analysis do not evaluate this measure or report reliability.
- Several teachers mentioned `overall`; one perfect-scoring teacher mentioned transitions such as `firstly` and `additionally`. The paper explicitly warns that participant heuristics are not necessarily helpful and supplies no systematic coding or cue-level accuracy for participant-reported heuristics.
- The released OSF analysis reports an exploratory topic difference omitted from the article narrative and the dated analysis plan: 69% accuracy for literature pairs and 60% for proverb pairs, likelihood-ratio p = .011. Its trial model also adds topic and school role to the planned quality-and-confidence predictors, so the result should be treated as unplanned task-bound exploration, not confirmation of a genre effect.
- Student stimuli were handwritten under proctoring and then mechanically corrected for spelling, punctuation, grammar, capitalisation, and agreement. That control removed obvious errors and changed the natural student-writing surface.
- The authors warn that superficial cue policing could create an arms race and that false positives and false negatives prevent software from being a panacea. Those are policy interpretations, not evaluated interventions.
- Students and teachers both rated direct submission negatively; teachers rated nearly every assessed use more negatively, while both groups viewed practice-problem generation positively. These attitude results do not validate a writing cue.
- The exact ChatGPT build is not disclosed. A survey screenshot shows `ChatGPT Feb 13 Version`, but stimuli were generated on February 2, so the screenshot cannot identify the stimulus build.

## Evidence and claims to extract

- **Direct source reviewed:** Complete nine-page article for DOI 10.1155/2023/1923981 from NSF PAR, including three figures, Table 1, acknowledgements, data statement, and all 48 references; the 17-file OSF supplement was checked recursively, including 50 ChatGPT stimuli, 50 graded student stimuli, the survey, selection protocol, raw export, scores, and R scripts.
- **Method and sample:** English-language study with 69 teachers and 140 students; six random paired comparisons per participant from pools of 25 ChatGPT and 25 student essays for each of two short prompts. Student source essays came from 97 students in four English classes, were handwritten under proctoring, filtered, transcribed, mechanically corrected, graded by two teachers, and sampled to 25 per prompt. Student participant data were collected from ten classes at the same school; the article does not report how many schools supplied the teacher sample. ChatGPT texts were generated on 2023-02-02 by regeneration until 25 responses existed for each prompt. The released load script excludes incomplete, non-anonymous, pilot, non-high-school-teacher, and duplicate-student records; the final student sample averaged 16.86 years, included 61 girls of 140, was 57% white, and was 96% native-English-speaking, while the teacher sample included 37 women of 69, was 71% white, and was 97% native-English-speaking.
- **Direct versus cited evidence:** C01-C14, C16-C17, and C19 use the article or public supplement directly. C15 is the authors' interpretation and policy framing. C18 groups literature-review claims that remain indirect here and are not promoted without direct review of the cited works.
- **Important limits and counterexamples:** Two prompts, 4-6 sentences, one subject, student data from one school, teacher sampling frame not reported, largely higher-achieving student source pool, grammar-corrected student stimuli, six forced choices, dated undisclosed ChatGPT build, no evaluated cue taxonomy, and no independent-document classification. The supplement contains a narrow two-grader student-language code, but it was not analysed and is not an authorship rule. High-quality student essays, human use of `overall`, transitions, triads, and negative parallelism are direct counterweights to cue-based accusations.

## Matched patterns / rules

- B1 `no-ai-vocabulary-clustering`: adjacent coverage for `additionally`, but the source does not validate the live three-per-paragraph threshold.
- E4 `no-generic-conclusions`: exact live coverage for `overall` only when the phrase matches the implementation's narrow conclusion forms.
- H10 `genre_specific` student-essay assessment: partly covers known-student baseline, surface polish masking weak reasoning, evidence, and draft-history context.
- `human-eyes/references/process.md` product boundary and `README.md` pattern-detector framing: cover the no-authorship-verdict implication.
- `overall-signal-stacking`: relevant only as aggregate project behaviour; the source does not validate its components or threshold.

## Associated hypotheses

- H3: Drop detection framing entirely.
- H9: Field-guide voice with similar-species disambiguation per pattern.
- H12: Genre-aware threshold calibration.
- H25: Model-family versus generic-AI residue.
