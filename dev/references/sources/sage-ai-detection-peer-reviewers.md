# SAGE: AI detection for peer reviewers

## Metadata

- **URL:** https://www.sagepub.com/explore-our-content/blogs/posts/sage-perspectives/2025/06/11/ai-detection-for-peer-reviewers-look-out-for-red-flags
- **Author / owner:** Alex Moersen / Sage Publishing
- **Published:** 2025-06-11
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** Publisher practitioner guide for academic peer reviewers and editors
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** Sitefinity BlogPost content ID `d9c92359-634e-4c31-85fa-d45f126db9d3`
- **Version / revision:** reviewed Sitefinity `ModifiedOn` `2026-03-23T14:13:02.133Z`; prior unversioned Jina capture retrieved 2026-05-05
- **Full-text status:** complete
- **Snapshot:** `snapshots/sage-ai-detection-peer-reviewers.md`
- **Extraction method:** Direct canonical HTML downloaded with `curl`, parsed from the article block with Python 3 and Beautiful Soup 4, and cross-checked against Jina Reader Markdown; page metadata and author identity checked in the canonical HTML and Sage author page
- **Snapshot SHA-256:** `9f3bcbf4e9ec4aebf5d8065b3792c4331f8343e708dfba0558b685bd8f7c3f76`
- **Model / corpus scope:** No model, version, prompt, corpus, sample, comparison group, rate, threshold, or language-transfer analysis is supplied. The English guide addresses research manuscripts submitted for academic peer review and names prose, references, content/logic, figures/data, formatting/meta residue, and editorial follow-up.
- **Access limitations:** None for the substantive article. Page chrome and decorative images were excluded. The linked Sage policies and author biography were accessed only for provenance/context and are not treated as direct evidence for the guide's red-flag claims. The prior card recorded no snapshot digest or stable revision, so no recorded SHA-256 existed to verify; the exact prior bytes were hashed as `e6cada34588a3aa30f37f7d7077e02a30670a9d48956c91c2f69538c00379cf1` before archival.

## Summary

Alex Moersen's Sage Perspectives guide gives peer reviewers and editors a five-family checklist for possible irresponsible or undisclosed AI use in research manuscripts, followed by four editorial actions and an explicit warning that no single flag is definitive. It also asserts, without evidence, that generative-AI use is becoming more prevalent in academic publishing and can be a powerful research/writing tool when properly disclosed. It is a publisher/practitioner checklist, not a study: it supplies one constructed repetition example and several phrase examples but no sample, model, human control, method, frequency, error rate, detector evaluation, or cited evidence for the red-flag generalisations. Its strongest project contribution is bounded academic-review context for citation, DOI, figure/data, source, and method verification; its prose, utility, prevalence, and authorship claims remain low-tier observations that cannot establish thresholds, causality, rates, or who wrote a document.

## Main insights

- The guide separates writing-style, citation, content/logic, visual/data, and formatting/meta flags; these categories should not be collapsed into one prose detector.
- Its concrete examples include repeated explanation, three vague research phrases, phantom references, bibliographic mismatches, contradictions, technical-term misuse, uniform paragraph structure, suspiciously smooth data, inaccurate or vague captions, repetitive headers, `Insert Table 1 here`, keyword repetition, and weak voice or critical analysis.
- The page explicitly says poor grammar does not necessarily indicate AI use and that no single red flag is definitive.
- The opening asserts increasing generative-AI use in academic publishing and positive research/writing utility under proper disclosure, but supplies no prevalence measure or utility evaluation.
- Its recommended response is verification and clarification: check citations, request raw data or method details, recommend careful revision, and request a detailed process cover letter.
- All behavioural generalisations are unsupported publisher guidance. The article does not measure whether any named feature is more common in AI than in human academic writing, how often it produces false positives or false negatives, or whether its proposed editorial actions are effective.

## Evidence and claims to extract

- **Direct source reviewed:** Complete canonical Sage Publishing article at Sitefinity content ID `d9c92359-634e-4c31-85fa-d45f126db9d3`, publisher `ModifiedOn` `2026-03-23T14:13:02.133Z`, retrieved 2026-07-17. The preserved body has seven non-empty section headings, 25 non-empty paragraphs, and four action-list items.
- **Method and sample:** Practitioner/editorial guidance for English-language academic research manuscripts. The page supplies no empirical method, sample, comparison group, model/version, prompt, corpus date, text-length range, participant group, adjudication method, or quantitative result.
- **Direct versus cited evidence:** C01-C22 inventory statements, examples, caveats, and recommendations made directly by the guide. C01, C19, and C22 link to Sage policy pages, but those pages are contextual links rather than evidence for the red-flag or positive-utility claims and were not recursively ingested. No research study or external evidence is cited for C02-C18, C20, or C21.
- **Important limits and counterexamples:** C05 is the guide's explicit poor-writing look-alike; C20 rejects single-flag certainty. Human writers can repeat, use vague language, make citation/data errors, structure paragraphs uniformly, leave placeholders, or lack critical analysis. No source result distinguishes these human causes from AI assistance, responsible disclosed use from undisclosed use, or generated text from ordinary editorial defects.

## Skill-use audit

- **Good use:** Use the guide as bounded practitioner context for H10 academic source/citation/figure/data review, as a prompt to verify claims rather than infer authorship, and as low-tier support for human-review and no-single-flag wording.
- **Misuse / overclaim:** Do not present the checklist as an AI detector, convert any item into a threshold or hard severity, infer that a manuscript was generated by AI, or claim that expert peer review is empirically the most effective detection method.
- **Unsupported use:** The page cannot support model attribution, prevalence, causal mechanism, detector accuracy, automated classification, universal style rules, non-academic transfer, or a claim that polished prose, poor grammar, keywords, smooth data, or any other named feature proves AI use.
- **Underused evidence:** Live H10 covers citation/DOI/journal and figure/data checks, but it does not explicitly ask for raw data, error reporting, methodological clarification, internal contradiction review, caption adequacy, or research-process documentation.
- **Patterns left on the table:** The exact `Studies have shown…` phrase and `Insert Table 1 here` example are missed by the focused surface checks; technical-term correctness, arbitrary manuscript-keyword integration, and evidence-quality review of overly smooth data are not direct deterministic checks. These gaps remain evaluation candidates, not approved changes.

## Matched patterns / rules

- A5 `no-vague-attributions`: adjacent to C03; the exact source phrase `Studies have shown…` was clear in the focused run, while `Studies have shown that` was flagged in a variant fixture.
- E1 `no-filler-phrases`: recognises C02's unquoted `It is important to note` construction, but the source presents it inside an inline quotation and the exact quoted-context run correctly left it clear.
- G6 `no-section-scaffolding` and `structural_monotony`: partly cover C10 and C13; G6 requires a repeated label and does not cover generic headers or every rigid paragraph pattern.
- H8 `no-placeholder-residue`: partly covers C14's concept but missed the exact `Insert Table 1 here` source example.
- H10 `genre_specific` academic branch: fully covers citation/DOI/journal verification and partly covers figure/data consistency, polished surface masking weak evidence, and depleted stance/engagement.
- `semantic_redundancy`, `underspecified_language`, `tonal_uniformity`, `faux_specificity`, `neutrality_collapse`, `even_jargon_distribution`, paragraph-length uniformity, and sentence-length variance are adjacent but do not reproduce the guide's unsupported authorship claims.
- Project product boundary in `references/process.md`, source-review guidance, and the catalogue preamble: findings describe constructions and review problems, not who or what wrote the text.

## Associated hypotheses

- H9 `Field-guide voice with similar-species disambiguation per pattern`: C05 and C20 reinforce the need to show ordinary-writing look-alikes and reject single-cue attribution.
- H12 `Genre-aware threshold calibration`: the guide is explicitly academic-manuscript scoped; any evaluation of its cues needs matched academic controls.
- H21 `Low information density and wrong sentence subject`: C04 supplies practitioner language for polished emptiness, but no empirical validation.
- H24 `Register-specific vocabulary density`: C15 concerns manuscript-keyword repetition in academic prose, not the live B1 AI-vocabulary list; it remains only a weak register-scoped candidate.

## Questions / follow-up

- Should future academic-review evaluation test internal contradictions, caption-to-figure fit, error-reporting adequacy, raw-data/method clarification, and process-documentation requests as evidence-quality checks rather than AI tells?
- Should the exact `Studies have shown…` and `Insert Table 1 here` variants enter candidate/control evaluation for A5 and H8, with quotation, instruction, manuscript-template, and legitimate publishing-workflow controls?
- No product change is authorised by this source refresh; every recommendation below remains pending Mae's decision.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none recorded; unversioned Jina capture | `snapshots/archive/sage-ai-detection-peer-reviewers/2026-05-05-e6cada34588a.md` | 2026-05-05 | `e6cada34588a3aa30f37f7d7077e02a30670a9d48956c91c2f69538c00379cf1` |
| current | Sitefinity BlogPost content ID `d9c92359-634e-4c31-85fa-d45f126db9d3` | `snapshots/sage-ai-detection-peer-reviewers.md` | 2026-07-17 | `9f3bcbf4e9ec4aebf5d8065b3792c4331f8343e708dfba0558b685bd8f7c3f76` |

The prior and current substantive article bodies are unchanged at 768 words after normalising Markdown/HTML markup and punctuation-adjacent whitespace. The refresh corrects the byline from the old card's unsupported `Anna Moersen` to the canonical page's `Alex Moersen`, records the Sitefinity content ID and modification timestamp, removes page chrome from the live snapshot, archives the exact prior bytes, and replaces broad project mappings with claim-keyed evidence boundaries.

## Decision history

- C05, C09, C11 approved 2026-07-26 via DR-131: Mae queued this work for later rather than ruling on its shape now. No checker, registry, or test change has been made and implementation has not started.
- The previous card had no claim IDs, user-decision cells, implementation statuses, or evaluation record. Its broad mappings to H8 machine-cleanliness, G6 repetitive headers, technical-term misuse, and generic provenance/context checks were not approved product decisions. Current C01-C22 are newly reconciled against the preserved source and live project, so every recommendation is `pending` and every implementation status is `not started`.
- The former H8 mapping is retired: live H8 is placeholder residue, not flawless grammar or machine cleanliness. C14 now records the exact placeholder adjacency and focused miss.
- No implementation is removed or reversed by this refresh because the prior record documented none.
- C10 approved 2026-07-17 via DR-115 component 4: H16 `no-paragraph-anaphora` (context_warning) now flags three or more consecutive prose paragraphs opening with the same word, ignoring trivial openers; headings and list blocks are skipped and do not break a run. C13 rejected via component 5: generic or varied-but-repetitive headers stay undetected and G6 remains identical-label repetition only.
- C03 approved 2026-07-19 via DR-15 option A: `Studies have shown` joined A5, while `This is an important area of research` and `More research is needed` joined E1.
- C14 approved 2026-07-19 via DR-20A: H8 now recognises `Insert Table 1 here` and equivalent numbered publishing instructions as hard-fail residue.

## Project coverage

This is the authoritative review table. Focused deterministic evidence comes from `python3 human-eyes/scripts/grade.py audit tmp/sage-ai-detection-peer-reviewers/coverage-fixture.md --surface-only --format json`, the exact-phrase fixture, and the exact quoted-example fixture. Surface-only output establishes deterministic coverage only, not a complete Audit or authorship result.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: The guide distinguishes properly disclosed author use of AI from irresponsible or untransparent use and frames its checklist around suspected generated or heavily assisted research manuscripts. | Direct publisher framing linked to Sage policy; the policy is contextual and not direct evidence for the checklist. No sample, prevalence, disclosure taxonomy, or outcome is supplied. | **partly covered:** H10 detects academic genre, and project reports reject authorship claims, but no graduated assistance/disclosure model is implemented. | The guide does not define responsible use, heavily assisted, or transparent disclosure, and cannot supply a policy rule by itself. | Record the scope boundary only; do not add a disclosure or misconduct rule without a separate policy decision and direct policy review. | pending | not started |
| C02: Repetition, restatement, summary of what was just said, and over-explanation are offered as flags; the constructed example repeats `important` and begins `It is important to note`. | Direct practitioner assertion and one constructed quoted example; no generated provenance, human comparison, frequency, or threshold. | **partly covered:** E1 flagged the unquoted `it is important to note` construction, while an exact source-context run preserved the inline quotation and reported `no-filler-phrases: clear`; `semantic_redundancy` and `structural_monotony` cover repeated information or arcs only through agent assessment. | The source does not validate E1 severity or prove that semantic repetition indicates AI; broader repetition remains contextual and quoted examples must remain suppressed. | Keep the example as low-tier context for E1 and semantic-redundancy review; make no threshold or severity change without matched academic and quotation controls. | pending | not started |
| C03: Generic or vague research language includes `This is an important area of research`, `More research is needed`, and uncited `Studies have shown…`. | Direct phrase examples and practitioner interpretation; no citation analysis, corpus, human baseline, or rate. | Fully covered for the exact forms: `Studies have shown` fails A5; the two generic research formulas fail E1. | No remaining exact-form gap. | Keep the attribution form in A5 and the two research formulas in E1. | approved | implemented |
| C04: Smooth, grammatically flawless prose may still be superficial, empty, lifeless, or meaningless. | Direct practitioner interpretation without examples beyond labels, method, human comparison, or measurable definition. | **fully covered at construct level:** H10 academic review names polished surface masking weak evidence or generic argument; H21 tracks low information density. No deterministic check claims to measure meaning. | The source cannot validate a mechanical emptiness score, threshold, or authorship inference. | Retain as practitioner context for H10/H21 only; require direct evidence and a falsifiable rubric before any new assessment. | pending | not started |
| C05: Poor grammar or writing does not necessarily indicate AI use. | Direct explicit counterexample/qualification; no empirical false-positive estimate. | **partly covered:** the project boundary forbids authorship claims and open H9 proposes look-alike disambiguation, but live H10 does not name poor grammar as a human look-alike. | The old card omitted this boundary while implying strong checklist support, and the live product lacks this concrete disambiguator. | Record the non-authorship and poor-grammar look-alike caution for future H9 evaluation; take no checker action from this source alone. | approved | not started |
| C06: Non-existent or phantom references that look plausible should be checked in bibliographic databases. | Direct practitioner claim and verification advice; no tested references, model/version, incidence, or database-recall evidence. | **fully covered:** H10 academic branch checks fake/broken/irrelevant citations and whether cited works support claims. | Existence checking is manual; the source supplies no automation method or accuracy evidence. | Keep as low-tier support for H10 citation verification; do not treat a phantom reference as authorship proof. | pending | not started |
| C07: Wrong DOIs, journal titles, volumes, issues, or page numbers are citation red flags that should be double-checked. | Direct practitioner checklist; no cases, counts, comparison, or effectiveness test. | **fully covered:** H10 academic branch names DOI, journal, date, reference-order, and citation verification; volume/issue/page checks fit that manual task. | No automated bibliographic resolver or source-support check is implemented, and the source does not justify one. | Retain in H10/source-grounding documentation; any automation needs separate bibliographic tests and human-error controls. | pending | not started |
| C08: Contradictions between paragraphs may indicate generated content. | Direct practitioner assertion; no contradiction examples, adjudication method, comparison, frequency, or specificity. | **not covered:** H10 covers weak evidence and figure/data consistency but does not directly require internal contradiction review; no deterministic checker establishes semantic contradiction. `pattern-opportunities.md` already records a pending `Factual and internal-consistency assessment` candidate with held-out contradiction controls, not implemented coverage. | Human drafts and complex arguments also contain or appear to contain contradictions; the source gives no disambiguation rule. | Add this source only as low-tier context to the existing pending factual/internal-consistency candidate; do not create a tell or authorship rule from this page. | pending | not started |
| C09: Incorrect or awkward technical-term use may warrant closer review. | Direct practitioner assertion; no examples, field, terminology set, human control, or validation. | **not covered:** `even_jargon_distribution` assesses unnecessary uniform density, not correctness; H10 does not currently name technical-term validation. | Term correctness is discipline-specific and cannot be inferred from surface jargon counts. | Record as an expert-review prompt only; require domain-expert evidence and matched controls before product guidance. | approved | not started |
| C10: Identical paragraph starts or rigid paragraph patterns are offered as signs of overly uniform structure. | Direct practitioner examples-in-description; no measured texts, threshold, genre control, or human baseline. | **partly covered:** `structural_monotony`, G6 repeated section scaffolding, paragraph-length uniformity, and G9 sentence-length variance inspect adjacent but different structures. The focused fixture flagged G6 only after the same heading appeared three times. | None of the live checks measures identical paragraph openings as described, and fixed academic sections can be legitimate. | Keep as H12/structural evaluation context; do not broaden G6 or statistical thresholds without matched academic controls. | approved | implemented |
| C11: The guide labels `Fabricated or Generic-looking Data` a category of possible red flags and illustrates it with perfectly smooth trends, missing real-world noise, low variability, or absent error reporting. | Direct unsupported publisher label plus narrower examples; no dataset, fabrication finding, example figure, statistical definition, field, model, false-positive control, or citation. The label does not establish that data are fabricated. | **partly covered:** H10 asks reviewers to check figure/data consistency, but it does not define fabricated/generic-looking data, suspicious smoothness, variability, or error-reporting adequacy. | Clean experimental/theoretical data can be legitimate; appearance cannot establish fabrication or AI use without method, provenance, and domain context. | Record as a pending evidence-quality/manual-review candidate; do not add a fabrication claim, visual rule, or statistical detector from this source. | approved | not started |
| C12: A caption that describes its figure inaccurately or vaguely may be a flag. | Direct practitioner assertion; no caption/figure examples, comparison, rate, or annotation protocol. | **partly covered:** H10 figure/data consistency can catch inaccurate captions, while `underspecified_language` is adjacent to vagueness but not figure-bound. | Caption adequacy requires access to the figure and disciplinary context; no pairwise check is specified. | Retain as H10 figure-consistency context and evaluate only in complete figure-caption tasks; no surface rule. | pending | not started |
| C13: Repetitive or generic section headers may indicate AI involvement. | Direct practitioner assertion; no examples, counts, human comparison, or threshold. | **partly covered:** G6 flagged an identical `How to make this work` label repeated three times; it does not cover merely generic or varied-but-repetitive headers. | Academic genre often requires repeated standard sections, and the source supplies no exception or rate. | Keep as bounded context for G6/H12; preserve required manuscript structure and require repetition plus genre controls before any change. | rejected | not applicable |
| C14: Unreplaced placeholder text such as `Insert Table 1 here` is formatting/meta residue. | Direct exact publishing-workflow example. | H8 now recognises numbered `Insert Table/Figure/Chart/Diagram/Appendix ... here` instructions and hard-fails on one match. | No remaining checker gap. | Keep the publishing-instruction family in H8. | approved | implemented |
| C15: Keywords repeated without integration into the narrative may be a flag. | Direct practitioner assertion; no keyword definition, examples, counts, model, corpus, comparison, or threshold. | **not covered:** B1/H24 concern AI-associated vocabulary density, not author-supplied manuscript keywords or narrative integration. | Mapping this to B1 would conflate arbitrary topic-keyword repetition with dated AI-vocabulary evidence. | Explicitly do not map C15 to B1; record only as weak academic-editing context pending direct evidence. | pending | not started |
| C16: AI-generated text is said to lack unique authorial voice and critical analysis. | Direct practitioner generalisation; no texts, voice/analysis rubric, human comparison, model/version, or exceptions. | **partly covered:** H10 names depleted engagement/stance and polished surface masking weak argument; `tonal_uniformity`, `neutrality_collapse`, `faux_specificity`, and H21 inspect adjacent constructs. | A stable formal voice or restrained style can be legitimate; the page cannot prove AI use or define a universal human voice. | Keep as a bounded academic critical-analysis prompt with H9/H12 controls; do not create a voice/authorship rule. | pending | not started |
| C17: Editors should verify every citation when they suspect generated or heavily assisted text. | Direct recommended action; no evidence that universal verification is efficient or improves AI detection. | **fully covered:** H10 academic citation and source-support review names this action. | The source's suspicion framing should not make a prose cue a prerequisite for ordinary citation review. | Retain as source-grounding process context and apply based on evidence risk, not an AI verdict. | pending | not started |
| C18: Editors can request raw data or methodological clarification to check whether research is sound. | Direct recommended action; no study of effectiveness, burden, policy, or access constraints. | **partly covered:** H10 checks figure/data consistency and claim support but does not explicitly name raw-data or clarification requests. | Availability, confidentiality, discipline norms, and editorial authority are not addressed. | Record as a pending academic evidence-quality process option; require policy and discipline review before product guidance. | pending | not started |
| C19: Editors can recommend careful revision, ask authors for clarification, and request a detailed cover letter describing the research process; the page also directs readers to Sage policies. | Direct editorial recommendations plus linked policy context; no evaluation of outcomes. The linked policies were not ingested as evidence in this run. | **not covered:** rewrite preservation guidance is author-facing and does not implement editor-author clarification or cover-letter workflow. | The guide does not define when requests are proportionate, what evidence a cover letter supplies, or how policy governs the response. | Record only; do not add an editorial escalation workflow without direct policy review and a user decision. | pending | not started |
| C20: No single red flag definitively indicates AI use; the author says expert human peer review remains the most effective monitoring method. | Direct caveat plus unsupported comparative effectiveness claim; no evaluated alternative, outcome, rate, or study. | **fully covered for the caveat:** catalogue and process language reject single-cue and authorship verdicts and require contextual human review. The comparative `most effective` claim is not project evidence. | Treating the second clause as measured effectiveness would overstate the page. | Retain the no-single-flag/human-review boundary; explicitly do not promote the `most effective` superiority claim without direct comparative evidence. | pending | not started |
| C21: Generative-AI use is said to be becoming more prevalent in academic publishing. | Direct opening assertion with no citation, corpus, baseline, dates, measure, or rate; this is not a finding from the page. | **not covered as evidence:** source metadata and H25 track date/model drift, but the project has no prevalence measure for academic publishing. | Treating this as measured adoption would invent evidence; `becoming more prevalent` has no stated comparison period or denominator. | Record only as unsupported 2025 publisher framing; do not use it for prevalence, trend, threshold, or urgency claims. | pending | not started |
| C22: AI can be a powerful tool during research and writing when its use is properly disclosed. | Direct positive utility assertion linked to Sage author guidelines; no task, model, outcome, comparison, or utility evaluation. The linked policy was not ingested as evidence. | **not covered:** the project has no general AI-research/writing utility assessment or disclosure framework, and this source cannot supply one. | Utility and proper disclosure are task- and policy-dependent; the page does not define either construct or compare outcomes. | Record only as publisher framing; require separate direct policy and task-specific evidence before any utility or disclosure guidance. | pending | not started |

## Recommendations

- C01: Record the disclosed-versus-irresponsible-use scope boundary only; require separate direct policy review before any disclosure or misconduct rule.
- C02: Keep the exact repetition example as low-tier context for E1 and semantic redundancy; make no severity or threshold change without matched academic and quotation controls.
- C03: Keep `Studies have shown` in A5 and the two exact research formulas in E1.
- C04: Retain as practitioner context for H10/H21; do not create a mechanical emptiness rule from this source.
- C05: Record the poor-grammar look-alike and non-authorship caution for future H9 evaluation; take no checker action from this source alone.
- C06: Keep as low-tier support for H10 citation verification; do not treat phantom references as authorship proof.
- C07: Retain in H10/source-grounding documentation; require separate tests for any bibliographic automation.
- C08: Add only as low-tier context to the existing pending factual/internal-consistency evaluation candidate; do not implement a tell.
- C09: Record as an expert-review prompt; require domain-expert evidence before product guidance.
- C10: Keep as H12/structural evaluation context; do not broaden G6 or statistical thresholds yet.
- C11: Record as a pending evidence-quality review candidate; do not promote the fabrication label or implement a smooth-data detector.
- C12: Retain as H10 figure-consistency context and test only in figure-caption tasks.
- C13: Keep as bounded G6/H12 context with required-structure controls.
- C14: Keep numbered publishing instructions in H8.
- C15: Explicitly do not map manuscript-keyword repetition to B1; record only as weak academic-editing context.
- C16: Keep as bounded academic critical-analysis context with H9/H12 controls; do not create a voice/authorship rule.
- C17: Retain citation verification as evidence-risk review rather than AI-suspicion proof.
- C18: Record raw-data/method clarification as a pending policy- and discipline-dependent process option.
- C19: Record only; require direct policy review and a user decision before any editorial escalation workflow.
- C20: Retain the no-single-flag/human-review boundary and explicitly exclude the unsupported comparative-effectiveness claim.
- C21: Record increasing-prevalence language only as unsupported 2025 publisher framing; do not use it as trend evidence.
- C22: Record positive utility only as publisher framing; require separate policy and task-specific evidence before guidance.

## Evaluation of approved changes

- C01: not applicable - pending; no product change approved.
- C02: not applicable - pending; no product change approved.
- C03: passed - DR-15A asserts all three exact forms in their assigned A5/E1 checks.
- C04: not applicable - pending; no product change approved.
- C05: not applicable - pending; no product change approved.
- C06: not applicable - pending; no product change approved.
- C07: not applicable - pending; no product change approved.
- C08: not applicable - pending; no product change approved.
- C09: not applicable - pending; no product change approved.
- C10: passed - DR-115 component 4 added H16 `no-paragraph-anaphora` to `grade.py`; `python3 dev/evals/tests/test_grade.py` passes the DR-115 block, including the three-paragraph run, trivial-opener, heading-interruption, and list-block controls, on 2026-07-17.
- C11: not applicable - pending; no product change approved.
- C12: not applicable - pending; no product change approved.
- C13: not applicable - rejected 2026-07-17 via DR-115 component 5; G6 remains identical-label repetition only.
- C14: passed - DR-20A makes `Insert Table 1 here` fail H8 while ordinary finished prose remains clear; all grader tests pass.
- C15: not applicable - pending; no product change approved.
- C16: not applicable - pending; no product change approved.
- C17: not applicable - pending; no product change approved.
- C18: not applicable - pending; no product change approved.
- C19: not applicable - pending; no product change approved.
- C20: not applicable - pending; no product change approved.
- C21: not applicable - pending; no product change approved.
- C22: not applicable - pending; no product change approved.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: sage_source_reviewer
- **Findings resolved:** Five material findings from the initial review were addressed: C21 and C22 now inventory the uncited prevalence and positive-utility assertions; C11 preserves and bounds the `Fabricated or Generic-looking Data` label; C05 is partly covered and names the missing poor-grammar disambiguator; C08 names the existing pending internal-consistency candidate without implying implementation; and C02 now distinguishes unquoted E1 coverage from the exact quoted-example suppression and requires quotation controls. The same reviewer focused-rechecked all five remediations and found no residual inconsistency.
- **Unresolved findings:** none
