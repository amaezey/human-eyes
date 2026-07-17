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

## Skill-use audit

- **Good use:** Support no-authorship-verdict language; require task, reader, model/date, genre, and human-look-alike boundaries; motivate matched student-writing evaluation and known-writer/draft-history context rather than cue policing.
- **Misuse / overclaim:** Do not convert 70% or 62% into a detector accuracy, a probability that a particular essay is AI-written, or proof that teachers are reliable or unreliable in other settings.
- **Unsupported use:** A current-model claim; a universal transition-word rule; a threshold for `overall`, `firstly`, or `additionally`; a causal claim that polish causes false positives; a policy-effectiveness result; or evidence for rubric echoing.
- **Underused evidence:** The public matched pool of 50 ChatGPT and 50 student essays can support a dated, task-bounded evaluation with prompt, topic, grammar-correction, and human-look-alike controls.
- **Patterns left on the table:** Topic sensitivity; the distinction between cue recognition and cue validity; grammar-normalisation as a surface confound; and the risk that anti-AI style policing changes student prose rather than measuring learning.

## Matched patterns / rules

- #7 `no-ai-vocabulary-clustering`: adjacent coverage for `additionally`, but the source does not validate the live three-per-paragraph threshold.
- #24 `no-generic-conclusions`: exact live coverage for `overall` only when the phrase matches the implementation's narrow conclusion forms.
- #41 `genre_specific` student-essay assessment: partly covers known-student baseline, surface polish masking weak reasoning, evidence, and draft-history context.
- `human-eyes/references/process.md` product boundary and `README.md` pattern-detector framing: cover the no-authorship-verdict implication.
- `overall-signal-stacking`: relevant only as aggregate project behaviour; the source does not validate its components or threshold.

## Associated hypotheses

- H3: Drop detection framing entirely.
- H9: Field-guide voice with similar-species disambiguation per pattern.
- H12: Genre-aware threshold calibration.
- H25: Model-family versus generic-AI residue.

## Questions / follow-up

- Should the OSF 50-versus-50 essay pool become a dated student-writing evaluation set with prompt/topic strata and grammar-correction provenance?
- Should student-writing guidance name polished human work, cue validity, and anti-AI camouflage as explicit look-alike and process risks?
- The OSF node has no declared licence. Confirm reuse rights before committing its stimuli or raw data to a product evaluation corpus.
- Direct review of cited studies is required before using C18's inherited results for project decisions.

## Update provenance

The prior card and snapshot named the correct DOI and preserved nearly all PDF text, but the card lacked the current metadata, claim table, decisions, update history, hash, and review gate. The prior snapshot omitted the four essay texts embedded in Figures 1 and 2. No source revision was found; this update restores that omitted material and brings the record to the current contract.

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | DOI 10.1155/2023/1923981; local snapshot hash 08c46c61 | `snapshots/archive/waltzer-teachers-detect-ai-essays/2026-05-05-08c46c61.md` | 2026-05-05 | `08c46c61400008bd5e288d58137bdc6cbae69d12c5e22ea203706ffc153ab6d9` |
| current | DOI 10.1155/2023/1923981; Article ID 1923981; NSF PAR record 10493551; OSF node 8qv6z | `snapshots/waltzer-teachers-detect-ai-essays.md` | 2026-07-17 | `a2e8c41447a78fc9b074b77e8313bbc1e3246d706a7863bd15041b80f63ecee2` |

## Decision history

- None: the 2026-05-05 card contained no claim-keyed user decisions or implementation statuses. All claims in this contract refresh begin as `pending` and `not started`; no checker, registry, guidance, test, hypothesis, or product change was made.

## Project coverage

This is the authoritative review table. The focused project check used all 50 preserved ChatGPT stimuli and all 50 preserved student stimuli as separate documents with `python3 human-eyes/scripts/grade.py audit <file> --surface-only --format json`. This proves deterministic surface behaviour only, not a complete Audit or authorship result.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: The study used 69 teachers, 140 students, and six forced-choice pairs per participant, each pairing one ChatGPT and one student essay. | Direct peer-reviewed method and public materials; student data from ten classes at one school, teacher school count not reported, two prompts, 4-6 sentences, English, February-March 2023. The public load script documents exclusions; the supplement reports age, gender, race, and native-English distributions. | `README.md` and `human-eyes/references/process.md`; fully covered as a need to describe what was measured and avoid authorship classification. | No product gap. The task cannot be treated as independent-document detection. | Record the study design as bounded human-judgement context; make no checker change. Verify future citations preserve the paired-task and sample boundaries. | pending | not started |
| C02: Teachers averaged 70% and students 62%; both exceeded 50% chance, and teachers were more accurate, t(160) = 2.50, p = .013. | Direct aggregate result; teacher 95% CI 65%-74%, student 95% CI 58%-65%. It is not a detector metric or per-document probability. | H3 and the product boundary; fully covered for no-authorship framing, while this population/task result is new source evidence. | The project has no direct mapping of these exact task-stratified rates. | Record the rates only with population, paired-task, date, and confidence-interval context; do not turn them into thresholds or verdicts. | pending | not started |
| C03: Eighty-four percent of teachers and 87% of students missed at least one of six trials. | Direct result showing error prevalence despite above-chance aggregate accuracy. Paired choice makes one selection simultaneously a hit and a rejection, so conventional false-positive/false-negative rates are unavailable. | H3, H9, process product boundary, and #41; fully covered in principle. | Current source mapping did not state this counterweight or task-metric limitation. | Add this only to evidence guidance for uncertainty and human-look-alike context; no deterministic rule. | pending | not started |
| C04: Pre-task confidence and post-task estimated score did not significantly predict overall accuracy; dichotomised trial confidence did not significantly predict trial accuracy. | Direct nulls: F(1) = 0.09, p = .760; F(1) = 0.95, p = .330; trial LRT D(1) = 0.48, p = .490. The released trial model converts confidence to `> 50` versus `<= 50` and omits 13 participants with missing confidence, so it does not test a continuous trial-confidence slope. | H3 and process no-confidence-output rule; fully covered as product restraint, not as replication of the study. | No study-specific confidence-null mapping. | Record the bounded null and keep human-eyes from emitting authorship confidence. Do not claim confidence can never be calibrated. | pending | not started |
| C05: Subject expertise did not predict accuracy, and English teachers were not significantly better than other teachers. | Direct nulls: teacher expertise F(1) = 0.03, p = .853; student expertise F(1) = 2.76, p = .099; English versus other teachers t(43) = 0.53, p = .599. | #41 uses genre-specific manual review but does not equate expertise with reliable authorship judgement; fully covered in principle. | The live guidance does not distinguish subject-matter review from source-provenance classification. | Record only; preserve the distinction between reviewing writing quality and inferring provenance. | pending | not started |
| C06: Prior ChatGPT use and self-rated ChatGPT experience did not significantly predict accuracy in either group. | Direct bounded nulls. The paper explicitly says this must not be read as proof that specialised training cannot help. | H3 and H25; fully covered for model/task caution. | No exact source mapping for the null or its anti-overinterpretation qualification. | Record the null with its qualification; do not generalise it to other training, models, or tasks. | pending | not started |
| C07: Trials answered incorrectly contained slightly higher-rated student essays, mean 86.72 versus 85.47 for correct trials, LRT D(1) = 12.03, p < .001. | Direct trial-level association under a mixed model with participant random intercept, topic, school role, binary confidence (above 50 versus 50 or lower), and scaled quality. The 1.25-point difference is not a general writing-quality comparison. Topic and school role appear in the released model but not in the article's analysis-method description or dated plan. | #41 student branch names surface polish masking weak reasoning and known-student baseline; partly covered. | The live branch does not name polished human work as a false-positive/look-alike control, and no matched evaluation exists. | Test-adapt: evaluate #41 and relevant surface checks on the public 50-versus-50 pool, stratified by teacher grade and prompt, before deciding whether to change guidance. Confirm reuse rights first. | pending | not started |
| C08: The authors interpret better-written student essays as harder to distinguish; vague and idiosyncratic human phrasing may also have served as student cues. The supplement separately records two graders' binary `student-specific language` judgements for every selected student essay. | Direct result plus author interpretation and two human examples. The grader instructions define the code as obvious adolescent language such as slang; 4/50 essays were marked by at least one grader and 2/50 by both. The article and released R analysis do not evaluate this code, report reliability, isolate cue effects, or derive an authorship rule. | H9 and #41 known-baseline/complexity-shift guidance; partly covered. | The project lacks explicit look-alike wording for polished human student prose and should not treat vague, idiosyncratic, or grader-coded student language as proof of human authorship. | Test-adapt: add these as bidirectional evaluation controls, not rules, if the matched-pool evaluation is approved. | pending | not started |
| C09: Several teachers mentioned `overall`; one perfect-scoring teacher mentioned transitions such as `firstly` and `additionally`; the paper cautions that heuristics are not necessarily helpful. | Direct open-comment anecdotes, not a coded cue study. No cue prevalence, conditional accuracy, human baseline, or causal result is reported. | `grade.py` directly implements clustered #7 vocabulary, filler phrases, and a narrow `Overall, this/the/these/it` conclusion regex. In surface-only runs, #7 flagged 6/50 ChatGPT and 0/50 student essays; generic conclusions flagged 23/50 ChatGPT and 2/50 student essays; filler phrases flagged 15/50 and 3/50. Partly covered. | `firstly` is not itself a live #7 item; `overall` has human counterexamples; the source does not validate any live threshold. | Test-adapt: retain the focused run as dated coverage evidence, do not promote teacher comments into a universal cue or severity, and require matched-human controls for any future change. | pending | not started |
| C10: Student texts were handwritten under proctoring, filtered, transcribed, and mechanically corrected; ChatGPT generated 25 responses per prompt by regeneration on 2023-02-02. | Direct method and supplement. Corrections removed obvious spelling, punctuation, grammar, capitalisation, and agreement cues; selection retained 25 of 40 literature and 25 of 42 proverb essays after exclusions. | H12 and `dev/TESTING.md` packaging/provenance controls; partly covered. | Existing source mapping omitted grammar normalisation, selection, and regeneration as confounds. | Record these controls in every reuse of the pool; do not compare the stimuli as untouched natural student prose. | pending | not started |
| C11: The exact ChatGPT model/build is not disclosed. | Direct provenance limit. The survey says GPT-3 family and shows `ChatGPT Feb 13 Version`, but stimuli predate that screenshot and were generated on February 2. | H25 and source metadata conventions; fully covered in principle. | Any current-model or precise GPT-3.5 attribution would exceed the record. | Record model as public ChatGPT, 2023-02-02, exact build unknown; reject current-model extrapolation. | pending | not started |
| C12: The released OSF analysis reports 69% accuracy on literature pairs and 60% on proverb pairs, LRT D(1) = 6.51, p = .011. | Direct supplemental exploratory result omitted from the article narrative and absent from the dated 2023-02-24 analysis plan. The released trial model adds topic and school role beyond the plan's quality-and-confidence specification; no confidence intervals or interaction analysis are supplied for the topic split. | H12 genre-aware calibration and `dev/TESTING.md` register stratification; partly covered. | Current project has no student-topic-specific evaluation and should not infer a stable genre effect from two prompts or promote an unplanned analysis as confirmatory. | Test-adapt: if the pool evaluation is approved, report prompt strata as exploratory task description; take no threshold action from this two-topic result alone. | pending | not started |
| C13: Students and teachers rated direct submission negatively; teachers rated modification, enhancement, and formatting more negatively; both groups rated practice-problem use positively, with no group difference for practice. | Direct attitude results on -10 to +10 scales. These are views, not observed conduct or writing-cue validity. | No prose checker should cover attitude preferences; fully covered by the product boundary. | None for pattern detection. | Record as educational-context evidence only; make no checker, severity, or authorship change. | pending | not started |
| C14: Teachers were more concerned and less optimistic than students; groups did not differ significantly in estimated cheating prevalence. | Direct attitude results: concern t(181) = 5.18, p < .001; optimism t(166) = 4.02, p < .001; expected cheating t(147) = 1.15, p = .251. | Not covered and not needed for prose-pattern behaviour. | Attitudes do not establish prevalence or consequences. | Record only; do not use perceptions as prevalence evidence. | pending | not started |
| C15: The authors warn that superficial cue policing may produce an arms race, software will not be a panacea because of false positives and negatives, and total bans are unlikely to work. | Author interpretation and policy recommendation, not an evaluated intervention. The false-positive/negative statement cites sources 46-47 indirectly. | `README.md`, `human-eyes/references/process.md`, H3, and H9; fully covered for no-authorship verdict and meaning-preserving review. | The current source indexes do not attribute this policy boundary to Waltzer. | Record the interpretation as cautionary framing only; do not claim the study tested bans, software, or camouflage effects. | pending | not started |
| C16: Generalisability is limited by one subject, narrow short essays, student recruitment from one school, an unreported teacher sampling frame, grammar-corrected student prose, an undisclosed model build, and untested prompt variants. | Direct limitations plus method-bound reviewer synthesis. The authors explicitly name narrow essays, one subject, grammar correction, and prompt variation; student-school, teacher-sampling, and model boundaries follow directly from the reported method. | H12, H25, source metadata conventions, and `dev/TESTING.md`; fully covered in principle. | Prior card omitted most boundaries. | Require all seven boundaries whenever this source supports a project claim or evaluation. | pending | not started |
| C17: The source does not validate a textual cue taxonomy, a cue threshold, a document-level authorship classifier, or current-model performance. | Direct absence/boundary established by full article and supplement review. Open strategies exist in raw data. A systematic but narrow two-grader code for student-specific language exists in the workbook, yet the paper and analysis never test its reliability, association with participant choices, or cue validity. | Product boundary fully covers no-authorship claims. Focused surface-only runs found at least one non-curly-quote required flag in 50/50 ChatGPT and 30/50 student stimuli; all 50 ChatGPT and 42/50 student essays had any required flag when curly-quote house style was included. This challenges any use of raw flag presence as provenance. | No complete bound-work-bundle Audit was run, and surface counts are not classification results. | Record the live run and grader code as coverage/false-positive context only; do not publish either as detector performance or use them to set thresholds. | pending | not started |
| C18: The literature review reports earlier GPT-2 narrative and poetry judgements, ChatGPT academic performance, plagiarism scores, and detection-tool context. | Indirect cited evidence. The underlying studies were not ingested or re-reviewed in this update, so their methods and numbers remain unresolved here. | Some cited topics have separate project cards, but this card cannot upgrade the article's summaries into direct evidence. Not covered as a single claim. | Direct-source review is required before any project conclusion. | Take no further action from the inherited summaries; route any desired claim to a separate source ingest. | pending | not started |
| C19: The article links public data, reports NSF grant 2104610, declares no conflict of interest, and credits named stimulus, recruitment, grading, and manuscript contributors. | Direct provenance details from Data Availability, Conflicts, and Acknowledgments; OSF node 8qv6z contains four folders and 17 files and was last modified 2023-04-29. | Source-record provenance fields; partly covered by the refreshed snapshot and card. | The OSF node has no declared licence, and the AsPredicted PDF route was inaccessible. | Preserve the article PDF and access-route metadata; do not copy the OSF package into a reusable corpus until rights are confirmed. | pending | not started |

## Recommendations

- C01: Record the paired six-trial design as bounded human-judgement context; make no checker change.
- C02: Keep the 70% and 62% rates population-, task-, date-, and interval-bound; do not derive a threshold or verdict.
- C03: Add the one-error prevalence only to uncertainty and human-look-alike evidence guidance.
- C04: Record the three confidence nulls with the trial dichotomisation, missingness, and anti-overinterpretation boundary; keep authorship confidence out of output.
- C05: Record that subject expertise and provenance classification are different tasks; make no product change.
- C06: Record the experience null and its explicit training qualification; do not generalise.
- C07: Test-adapt the public matched pool by teacher grade and prompt before considering #41 guidance, contingent on reuse rights.
- C08: Use polished, vague, idiosyncratic, and grader-coded student-language examples as bidirectional evaluation controls, not rules, if C07 is approved.
- C09: Retain the focused live results as dated coverage evidence; do not promote anecdotal cue comments or change severity without matched evaluation.
- C10: Preserve selection, proctoring, correction, and regeneration provenance in every pool reuse.
- C11: Tag the stimuli as public ChatGPT generated 2023-02-02, exact build unknown; reject current-model extrapolation.
- C12: If an evaluation is approved, report the two prompt strata as exploratory task description; do not infer a stable genre threshold.
- C13: Record the use-attitude results as context only; make no prose-pattern change.
- C14: Record concern, optimism, and expected-cheating results as perceptions, not prevalence.
- C15: Record the cue-policing/software/ban discussion as author interpretation, not intervention evidence.
- C16: Require all source-scope boundaries whenever the source is cited.
- C17: Keep the surface-only run and unanalysed grader code out of detector-performance claims; no threshold or authorship action.
- C18: Do not promote indirect literature summaries; ingest any underlying source separately before use.
- C19: Preserve provenance and confirm OSF reuse rights before committing the supplement to a product evaluation corpus.

## Evaluation of approved changes

- C01: not applicable - pending record-only recommendation; no product change approved.
- C02: not applicable - pending record-only recommendation; no product change approved.
- C03: not applicable - pending evidence-guidance recommendation; no product change approved.
- C04: not applicable - pending record-only recommendation; no product change approved.
- C05: not applicable - pending record-only recommendation; no product change approved.
- C06: not applicable - pending record-only recommendation; no product change approved.
- C07: not applicable - pending evaluation recommendation; no product change approved.
- C08: not applicable - pending evaluation-control recommendation; no product change approved.
- C09: not applicable - pending evaluation recommendation; no product change approved.
- C10: not applicable - pending provenance recommendation; no product change approved.
- C11: not applicable - pending metadata recommendation; no product change approved.
- C12: not applicable - pending evaluation recommendation; no product change approved.
- C13: not applicable - pending record-only recommendation; no product change approved.
- C14: not applicable - pending record-only recommendation; no product change approved.
- C15: not applicable - pending framing recommendation; no product change approved.
- C16: not applicable - pending source-use boundary; no product change approved.
- C17: not applicable - pending record-only recommendation; no product change approved.
- C18: not applicable - pending no-promotion recommendation; no product change approved.
- C19: not applicable - pending provenance recommendation; no product change approved.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: /root/waltzer_source_reviewer
- **Findings resolved:** Five material findings resolved: corrected prior-snapshot and publisher-mark provenance; specified trial-confidence dichotomisation and missingness; bounded the unplanned topic analysis and added trial-model covariates; documented the unanalysed two-grader student-language code and counts; and added a hash- and route-complete 17-file OSF inventory. The same reviewer performed a focused re-check and found 0 further findings.
- **Unresolved findings:** none
