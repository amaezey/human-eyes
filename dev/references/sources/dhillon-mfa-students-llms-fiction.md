# Dhillon et al.: Readers Prefer Outputs of AI Trained on Copyrighted Books over Expert Human Writers

## Metadata

- **URL:** https://arxiv.org/abs/2510.13939
- **Author / owner:** Tuhin Chakrabarty, Jane C. Ginsburg, and Paramveer Dhillon
- **Published:** 2025-10-15 submitted; revised 2026-03-17
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** academic preprint; preregistered behavioral study with exploratory stylometry and mediation analyses
- **Evidence tier:** Peer-reviewed / academic empirical (preprint)
- **Review mode:** update
- **Stable identifier:** arXiv:2510.13939v4; DOI 10.48550/arXiv.2510.13939
- **Version / revision:** arXiv v4, 2026-03-17; prior local snapshot was also a complete normalized v4 extraction retrieved 2026-05-05 but lacked contract metadata and a recorded digest
- **Full-text status:** complete
- **Snapshot:** `snapshots/dhillon-mfa-students-llms-fiction.md`
- **Extraction method:** authoritative 50-page arXiv v4 PDF downloaded and preserved
- **Snapshot SHA-256:** `a9acebcb757b69ce3197a42cd924be9f058c977f43c45c3e8872920163dfc5b3`
- **Model / corpus scope:** up-to-450-word English literary-fiction or creative-nonfiction emulations of 50 named authors; in-context GPT-4o, Claude 3.5 Sonnet, and Gemini 1.5 Pro outputs; author-specific fine-tuned GPT-4o for 30 living authors; 150 human/in-context-AI pairs, 90 human/fine-tuned-AI pairs, 330 unique excerpts, 28 U.S.-resident MFA-trained readers, 516 college-educated native-born U.S./U.K. English-speaking Prolific readers, and 10,920 blind pairwise judgments
- **Access limitations:** none for the paper. The linked GitHub data/code repository and OSF preregistration were not recursively preserved or independently reproduced in this one-source paper review; repository-reproduction claims remain source-reported. Figure pixels are preserved in the PDF attachment, while the Markdown snapshot preserves their captions and surrounding interpretation.

## Summary

This preregistered study compares short expert-written and model-generated emulations from a pool the main paper repeatedly calls 50 award-winning authors. Supplementary S1.1 qualifies that label: it documents 34 of the 50 as having at least one named major national or international prize and describes the rest through canon, prominence, or critical-emergence groupings. MFA-trained readers strongly preferred human excerpts under identical in-context prompting, while college-educated general readers preferred the prompted AI on quality and showed no aggregate fidelity preference. Author-specific GPT-4o fine-tuning, coupled with filtering, resampling, and grammar/consistency post-processing, reversed both reader groups' preferences. The paper also reports that two commercial detectors largely missed the fine-tuned outputs, and its exploratory analysis links Pangram scores most strongly to a human-adjudicated cliche-density measure. For human-eyes, the strongest contribution is not an authorship rule: it is evidence that audience expertise, model condition, author, post-processing, and genre materially alter both perceived quality and detectability. The paper's selected expert rationales provide limited fiction-craft examples, but they are not a systematic taxonomy or a validation of the live generic-metaphor rule. The same Pangram product also served as an exclusion screen for reader rationales, with no participant-flow count reported for that exclusion.

## Main insights

- Reader expertise changed both preference and agreement: MFA-trained readers rejected in-context emulations, while general readers were more favorable to them and agreed much less with one another.
- Writing-quality and style-fidelity judgments were correlated in both conditions, but the correlation fell more for MFA readers, from 0.64 under prompting to 0.39 after fine-tuning, than for general readers, from 0.52 to 0.45. Those are direct Figure 14 results; the paper's explanations about expert stylistic sensitivity and general-reader attention to surface fluency are author interpretation.
- Fine-tuning did not simply mean training once on raw books. The pipeline segmented books, used GPT-4o-generated content descriptions, resampled overlap or content failures, manually checked verbatim overlap, and post-processed grammar, tense, spelling, punctuation, awkwardness, and logical inconsistencies.
- The detector result is tightly bounded to 330 short excerpts, Pangram and GPTZero, a chosen 0.9 threshold, and the tested 2025-era model/pipeline conditions. It does not establish that detectors generally fail or that any surface pattern proves authorship.
- Cliche density was the strongest reported correlate of Pangram score, but the measure began with a Claude 4.1 Opus candidate list and retained only the intersection of two authors' judgments. It is exploratory, tool-dependent, and not equivalent to human-eyes G2 generic/ungrounded metaphors.
- Selected MFA rationales name repetition and over-explanation; convoluted, clipped, or affectless prose; cliches, purple prose, too much telling or exposition, predictable conclusions, lack of subtext, and mixed metaphors. The selected positive comparisons praise idiosyncratic voice, humor, code-switching, slang, and profanity rather than safe/polite voice. These are illustrative qualitative examples and author interpretation, not frequency-coded findings across the sample.
- Author-level outcomes varied sharply. Tony Tulathimutte was a direct counterexample to the broad style-superiority claim, and two authors remained below parity on quality. Relative to each author's prompted baseline, one of 30 style premiums and six of 30 quality premiums were nonpositive; median premiums were +34.2 and +13.4 percentage points, respectively.
- The study covers short, blinded pairwise excerpt judgments, not complete novels, disclosed-AI choices, sales, publication readiness, longitudinal reader behavior, or the full human labor needed to create a marketable book.

## Evidence and claims to extract

- **Direct source reviewed:** complete 50-page arXiv:2510.13939v4 paper, including main text, references, methods, figures and captions, supplementary sections S1-S10, Tables 1-19, Figures 1-25, preregistration deviations, and code/data statement.
- **Method and sample:** five English-literature PhD students helped select 50 authors and construct prompts with 20 author excerpts, a style description, and content specifications. For each author, three MFA writers each produced a separate human emulation; the writers were paid $75 per excerpt, had no submission time limit, and later supplied judgments from the same participant pool without ever evaluating their own work. The in-context condition paired 150 human excerpts with 50 outputs each from GPT-4o, Claude 3.5 Sonnet, and Gemini 1.5 Pro; Llama 3.1 was tried but excluded after poor long-context instruction following. The fine-tuned condition used 30 author-specific GPT-4o models and 90 human-AI pairs. For four translated authors, the source says the same translator's work was used across books. Each randomized pair received three MFA judgments and 19 or 21 general-reader judgments per outcome, yielding 10,920 blind forced-choice judgments across style fidelity and writing quality. Analyses used fixed-effect logistic GLMs with CR2 reader-clustered standard errors; Holm correction covered the primary reader-group contrasts.
- **Direct versus cited evidence:** C01-C24, C27-C28, and C30-C31 summarize direct study design, outputs, reader judgments, detector runs, derived stylometry, pipeline procedures, limits, deviations, quality controls, and quality-style correlations. C25 preserves a source-reported cost comparison whose $25,000 human benchmark is not derived in the paper. C26 is the authors' legal/economic interpretation. C29 records the now-completed evidence-index correction separating inherited background from direct data. The introductory claims that prompting produces cliches, purple prose, unnecessary exposition, reduced diversity, formulaic writing, or lost voice are citations to prior work; only the selected rationales and exploratory cliche measure provide direct evidence here.
- **Important limits and counterexamples:** short English excerpts; U.S.-resident MFA sample; native-born U.S./U.K. general-reader eligibility; blind forced choice rather than absolute scores or disclosed provenance; MFA writers also served as readers but never judged their own work; sparse author-level data pooled 87.5% toward general readers; minimal general-reader agreement; a selected and transformed generation pipeline; only two commercial detectors; no independent data/code reproduction in this review; no finished novels, market purchases, editing-cost estimate, or unblinded disclosure test. The headline participant total is 544, while Table 15 reports 542 quality-model reader clusters and 535 style-model reader clusters without a participant-flow reconciliation.

## Matched patterns / rules

- H10 `genre_specific`, fiction branch: partly overlaps role-explaining exposition, scene pressure, and style imitation that misses an author's oddities; it does not explicitly cover reader expertise, subtext, general exposition or telling, cliche density, purple prose, mixed metaphors, or model/pipeline boundaries.
- G2 `generic_metaphors`: only partial conceptual overlap with selected mixed/overwrought-metaphor rationales; its ungrounded-metaphor criterion is not measured by the paper.
- G9 `sentence-length-variance`: named as an exploratory mediation feature, but the paper reports no standalone coefficient or direct human-eyes threshold validation.
- H25 model-family versus generic-AI residue: supported by differences among the three in-context models and the sharp prompted/fine-tuned GPT-4o contrast.
- `references/process.md` product boundary: reinforced because detector/craft signals do not establish authorship and because quality preference is distinct from source provenance.

## Associated hypotheses

- H20 severity calibration of agent-judgement items, especially G2 and H10 in fiction.
- H22 long-tail compression and grammatical standardisation, but only as a future comparison: sentence-length variance entered exploratory mediation without a reported independent result.
- H25 model-family versus generic-AI residue.
- Proposed: fiction craft findings should be evaluated by reader expertise, author, model condition, and post-processing state rather than pooled into a timeless AI-tell list.
