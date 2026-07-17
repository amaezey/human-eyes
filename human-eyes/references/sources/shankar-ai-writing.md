# Shreya Shankar: Writing in the Age of LLMs

## Metadata

- **URL:** https://www.sh-reya.com/blog/ai-writing/
- **Author / owner:** Shreya Shankar
- **Published:** 2025-06-16
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** Practitioner craft essay
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** Canonical page with HTTP ETag `"32e39a37ce87f6c27fbac72f4c69b43c"` and Last-Modified `Thu, 02 Jul 2026 09:13:29 GMT`; previous snapshot retrieved 2026-05-05 had no recorded page revision identifier
- **Full-text status:** complete
- **Snapshot:** `snapshots/shankar-ai-writing.md`
- **Extraction method:** Direct canonical HTML verification with curl and Beautiful Soup 4.14.3; prior Markdown body retained after complete normalized-text and structure comparison
- **Snapshot SHA-256:** `7a03b57dd60c920e58e008b018889c2d28988645483cec5b0b028ed580129321`
- **Model / corpus scope:** Unquantified first-person observations from several technical papers and blog posts reviewed over the preceding couple of years; unspecified LLM tools and settings, one Gemini 2.5 Pro draft example, one unversioned GPT-4 hypothetical/example, English technical and blog prose, no measured corpus or human comparison
- **Access limitations:** None for the article body. The page supplies no study protocol, counts, prompt for most examples, model versions except Gemini 2.5 Pro, comparison corpus, links, citations, or stable first-party revision ID. Non-substantive page chrome and the duplicate table of contents were omitted.

## Summary

Shankar gives a first-person craft account of recurring problems she sees while writing and reviewing technical papers and blog posts, then supplies deliberate-use counterexamples and her own LLM-assisted writing loop. The complete static article contains 4 major sections, 17 subsections, 43 paragraphs, one block quotation, and one two-item list. It is strong practitioner evidence for editorial questions about substance, sentence subjects, reference clarity, rhythm, listification, audience knowledge, and scoped revision, but it is not a corpus study, model comparison, prevalence estimate, mechanism study, detector validation, or basis for document-level authorship inference.

## Main insights

- The direct negative craft observations are empty paragraph summaries, inappropriate listification, flat sentence rhythm, topic-misaligned grammatical subjects, low information density, vague claims and attributions, unclear demonstratives, unexplained fluency, and invented or dubious technical terminology.
- The article's central qualification is that a device associated with generated prose is not bad merely because models use it. Repetition, signposts, parallel structure, predictable headings, declarative openings, and em dashes can all help when they carry information or serve a deliberate rhetorical purpose.
- The source material complicates blanket rules: its flat-rhythm bad and good examples are both below the live sentence-variance check's eligibility boundary; the reviewer's isolated use of its two-item example list trips the list-ratio rule; one `This creates` example is recognized but below the deterministic demonstrative threshold; and the reviewer's content-bearing `In summary` control plus Shankar's intentional em dash are still failed by the live checks.
- Shankar's workflow keeps human judgment in the loop: outline the story, draft rough prose, delegate only the current bottleneck, ask for a scoped rhetorical transformation, select and edit completions, and retain responsibility for framing, depth, and contribution.
- No claim in the essay establishes frequency, causality, an RLHF mechanism, a severity level, a universal threshold, a model-family fingerprint, or authorship.

## Evidence and claims to extract

- **Direct source reviewed:** Complete canonical article HTML served 2026-07-17 with ETag `"32e39a37ce87f6c27fbac72f4c69b43c"` and Last-Modified `Thu, 02 Jul 2026 09:13:29 GMT`; preserved as `snapshots/shankar-ai-writing.md`.
- **Method and sample:** Practitioner reflection based on several unspecified technical papers and blog posts written or reviewed over roughly the prior two years. The article provides selected examples and one self-reported workflow, not a defined sample, comparison group, annotation procedure, frequency table, or outcome evaluation. Models and prompts are mostly unspecified; the low-density introduction names Gemini 2.5 Pro, and an illustrative technical passage names GPT-4 without a version.
- **Direct versus cited evidence:** C01-C23 distinguish direct author observations, examples, qualifications, interpretations, and self-reported process from reviewer analysis in the coverage columns. The page cites no external works. C10's statement that a sample term is not one Shankar has heard, C22's characterization of SWBST as often taught in early education, and C23's capability judgments remain author interpretation rather than independently verified findings. The isolated-list and content-bearing-summary controls in C03 and C13 are reviewer applications of the source's criteria, not author-labelled controls.
- **Important limits and counterexamples:** Human writers can produce the named problems, Shankar says she makes the demonstrative mistake herself, and she directly defends six often-flagged devices. There are no rates, model controls, prompt controls, longitudinal measurements, non-English evidence, genre transfer tests, reader outcomes, null tests, or authorship labels.

## Skill-use audit

- **Good use:** Use the source as bounded craft support for manual or agent review of paragraph substance, referential clarity, sentence-topic alignment, audience knowledge, unnecessary listification, rhythm, and scoped revision. Use its positive examples as legitimate-use controls.
- **Misuse / overclaim:** Do not turn the essay into bans on bullets, summaries, repetition, signposts, parallel structure, predictable headings, declarative openings, or em dashes. Do not infer a universal rule from one selected example or an aggregate/document-level verdict from a practitioner observation.
- **Unsupported use:** The article cannot validate prevalence, severity, thresholds, causal explanations, model attribution, detector performance, human-versus-AI separation, current-model behavior, or authorship.
- **Underused evidence:** The live project tracks low information density and wrong sentence subjects only in open H21. It has no general audience-knowledge assessment, no direct subject-topic alignment check, no authoring guidance for delegating only the current bottleneck, and no SWBST evaluation.
- **Patterns left on the table:** The exact flat-rhythm pair exposes an eligibility boundary in #52; the exact `This creates` example exposes candidate-versus-threshold behavior in #35a; the useful `In summary` paragraph and explicit em-dash defense challenge fail-on-occurrence behavior; and the writing loop supplies process evidence rather than a new prose tell.

## Matched patterns / rules

- #5 `no-vague-attributions`
- #31 `no-excessive-lists`
- #34 `no-tidy-paragraph-endings` plus agent assessment `semantic_redundancy`
- #35a `no-orphaned-demonstratives`, #35b `no-this-chains`, and agent assessment `referential_clarity`
- #38 `no-section-scaffolding`
- #41 agent assessment `genre_specific`
- #44 `no-signposted-conclusions`
- #49 `no-em-dashes`
- #51 `no-anaphora`
- #52 `sentence-length-variance`
- Agent assessments `underspecified_language`, `formulaic_parallelism`, and `semantic_redundancy`
- `human-eyes/references/process.md` meaning preservation, structural repair, and product boundary

## Associated hypotheses

- H8 audience-aware voice via invocation surface
- H9 field-guide voice with similar-species disambiguation
- H12 genre-aware threshold calibration
- H21 low information density and wrong sentence subject
- H22 long-tail compression and grammatical standardisation
- H27 performative profundity and aphoristic closure, as adjacent ending research only

## Questions / follow-up

- Should H21 be evaluated as one or more agent assessments, rewrite-only questions, or both, with matched human and AI controls?
- Should #52's documented eligibility wording be reconciled with the implementation before Shankar's short three-sentence pair is used as a test?
- Should useful signposts and deliberate em dashes receive context-sensitive treatment rather than fail-on-occurrence behavior?
- Should Shankar's bottleneck delegation, subject-verb placement, and SWBST workflow be evaluated for optional writing-process guidance?

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none found; prior page revision not recorded | `snapshots/archive/shankar-ai-writing/2026-05-05-02b364d3.md` | 2026-05-05 | `02b364d3265d04094ba842a2feeffcda913292bd8839fb130c87fe0e0e6b9133` |
| current | none found | `snapshots/shankar-ai-writing.md` | 2026-07-17 | `7a03b57dd60c920e58e008b018889c2d28988645483cec5b0b028ed580129321` |

The previous card and manifest recorded no SHA-256, so there was no declared digest to compare. Before replacement, the prior snapshot's on-disk SHA-256 was computed as `02b364d3265d04094ba842a2feeffcda913292bd8839fb130c87fe0e0e6b9133`; the archived bytes are identical by `cmp` and hash. The current canonical article's 2,142 normalized word tokens match the prior body in order, so this refresh changes provenance, contract coverage, and analysis rather than substantive article prose.

## Decision history




- 2026-07-17: Mae tagged weak sentence subjects (C05) and subject-verb distance (C21) as POS-dependency candidates, to be implemented with the tagger from her other project (register POS-01/POS-02). SWBST (C22) remains pending: single-source assertion, no output evidence.
- 2026-07-17: Mae approved two agent-judgement changes: audience-knowledge mismatch added as a registry record, and empty-summary endings folded into semantic_redundancy. Weak sentence subjects, the subject-verb interruption regex, and SWBST remain pending her explicit call.
- 2026-07-17: Mae approved removing the #47 soft-scaffolding citation from the root README; the essay does not support that exact mapping. Pattern #47 unchanged.
- The 2026-05-05 card contained an unkeyed second-pass summary, no authoritative claim table, no recorded user decisions, and no implementation statuses. This update reopens all evidence as C01-C23 with `pending` decisions and `not started` implementation statuses. No prior approved or implemented decision is retired.
- C04 approved 2026-07-17: reconcile #52's documented eligibility with the implementation. Implemented in commit 13e235f; #52 now skips prose under 100 words or under 6 sentences per the documented eligibility.
- C17 decided 2026-07-17: #49 remains fail-on-any (deliberate stance); the proposed density/threshold reconsideration is declined and no product change follows.

## Project coverage

This is the authoritative review table. Focused results below are deterministic surface checks only, not complete Audits.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: While writing and reviewing technical papers and blog posts, Shankar reports encountering LLM-generated writing that feels off; she also values LLMs for early drafts, summaries, and rephrasing, and frames much current reading as machine-generated. | Direct first-person practitioner framing; unspecified tools, prompts, counts, and outcomes; the statement that much reading is now machine-generated is unquantified author framing, not a prevalence result. | Partly covered by the source-tier rules and product boundary, which allow craft guidance while prohibiting authorship inference. | The current general evidence note calls this one of the strongest craft references and says the claims directly support several checks without restating the bounded anecdotal method, broad machine-generated-reading frame, or workflow substance. | Record the bounded method, unquantified framing, workflow scope, and no-authorship limit in source mappings; no checker change. Verify by source-card review. | pending | not started |
| C02: Empty paragraph-final summary sentences can sound conclusive while adding nothing, and Shankar has no reliable recipe for a substantive parting thought. | Direct practitioner observation plus two selected examples; the failed-recipe statement is a null process result, not a model evaluation. | Partly covered by #34, agent assessment `semantic_redundancy`, and process guidance to remove paragraph recaps. Focused #34 execution on the two examples returned `Tidy paragraph endings: 0`. | The exact examples are outside #34's lexical and structural candidate shapes, and no outcome evidence justifies a new threshold. | Add the examples only to H21 or a future semantic-redundancy evaluation with human controls before any rule change. | approved | implemented |
| C03: Bullets and outlines are overused when connected ideas need context; lists remain useful for parallel, independent items. | Direct practitioner observation with an explicit legitimate-use condition; no count or rate. The two-item list used in focused execution belongs to C02 and is a reviewer-selected short-list control, not an author-labelled legitimate-list example. | Partly covered by #31 and process guidance to preserve lists that compare real content. Focused execution on that isolated two-item control returned a finding from a 50% line ratio. | #31's ratio can fail a short two-item list in isolation and cannot judge whether items are independent or context-dependent. | Evaluate #31's line-ratio behavior on short legitimate lists and prose-conversion cases before adapting thresholds or guidance. | pending | not started |
| C04: Flat sentence lengths reduce rhythm, emphasis, attention guidance, and pace; varied lengths can improve the same technical explanation. | Direct craft claim with one author-labelled bad/good pair; no reader test, authorship labels, or quantitative rhythm metric. | Partly covered by #52 and process guidance. Focused #52 execution skipped both examples: bad was 79 words and 3 sentences; good was 54 words and 3 sentences. Both examples separately triggered #10 triad candidates, which is unrelated to the claimed rhythm contrast. | The exact evidence pair does not exercise #52, and the catalogue says 100-plus words while the implementation skips only when both sentence count is below 6 and words are below 100. | Reconcile #52's documented eligibility with code, then evaluate the pair only as a short-form control; do not infer a threshold from it. | approved | implemented |
| C05: A sentence can obscure its topic by choosing the wrong grammatical subject; the source contrasts `Readers are better guided...` with `Choosing the right subject...`. | Direct grammatical explanation and selected rewrite pair; no measured sample or reader outcome. | Not covered. H21 tracks the issue, while #35a and `referential_clarity` handle vague referents rather than general subject-topic alignment. | No live assessment asks whether the grammatical subject is the sentence's actual topic. | Test H21 on matched examples and decide whether subject-topic alignment belongs in agent assessment or rewrite-only guidance. | pending | not started |
| C06: A Gemini 2.5 Pro introduction is fluent but low-density because it supplies no concrete insight, framing, or momentum. | Directly identified model and selected generated excerpt; prompt is paraphrased but settings, date, retries, and comparison are absent. | Partly covered by H21 and the `underspecified_language` assessment, but neither currently measures contribution relative to length or framing momentum. | No live finding names low information density as a general construct, and one selected model output cannot validate a threshold. | Keep the excerpt as an H21 evaluation candidate with human low-density and concise technical controls. | pending | not started |
| C07: Vague prose refers to undefined ideas and makes unsupported claims, illustrated by unnamed experts and an unspecified productivity impact. | Direct practitioner observation and selected example; no frequency or model identity. | Fully covered across #5 `no-vague-attributions` and the general `underspecified_language` assessment. Focused #5 execution matched `experts say`. | Deterministic #5 covers only the unnamed-authority portion; the complete Audit is needed for missing criteria and stakes. #41's default branch adds no coverage here. | Retain the #5 and `underspecified_language` mappings and add no new rule; use complete-Audit evidence when evaluating the broader example. | pending | not started |
| C08: Demonstratives such as this, that, these, and those become unclear without a same-sentence or immediately prior noun; Shankar says humans make this mistake too. | Direct observation, explicit human look-alike, and one `This creates friction in production` example. | Fully covered by `referential_clarity` in a complete Audit and partly by #35a/#35b. Focused #35a recognized `this creates` as one candidate but stayed below its three-candidate threshold. | The deterministic finding threshold does not make the candidate invisible, but a surface-only report does not decide antecedent clarity; human occurrence defeats authorship use. | Retain the complete-Audit mapping and human look-alike note; do not lower a threshold from one example. | pending | not started |
| C09: Fluent technical prose can fail when it assumes audience knowledge and explains neither a term nor the hard part; a human must fill the gap. | Direct practitioner observation and selected attention-mechanism example; no audience study or comprehension measurement. | Partly covered by H21 and process meaning preservation. | #41's default branch has no watchlist, its academic/student branches do not assess reader prior knowledge, and no current check asks what the intended reader already knows. | Evaluate an audience-knowledge question with technical, expert-audience, and definition controls before adding guidance. | approved | implemented |
| C10: LLMs may produce dubious technical terminology; Shankar gives `retrieval grounding` and says it is not a term she has heard. | Direct anecdotal observation and an explicitly hedged personal-knowledge boundary; the source does not prove the term nonexistent or name the generating model/version. | Partly covered by #41 source and factual verification in named genres and by the closed-factual-record process. | General technical prose in the default branch has no terminology-verification assessment, and the example cannot support a lexical ban. | Record as a terminology-verification candidate only; require domain sources before treating any term as invented. | pending | not started |
| C11: A structure is not bad merely because it appears in model output; the goal is clarity, intention, and control rather than sounding unlike a model. | Direct source qualification and central counterexample boundary. | Fully covered by the product boundary, evidence note, context-sensitive process, and tolerance notes. | Some individual checks still fail on occurrence or surface thresholds despite the general policy. | Preserve this as the governing interpretation for C12-C17 and as a no-authorship limit. | pending | not started |
| C12: Intentional repetition and some predictability can clarify or reinforce complex material when the repetition is purposeful. | Direct craft judgment and one vector-database paraphrase example; no reader study. | Fully covered by process guidance to preserve deliberate devices, #51's deliberate-anaphora tolerance, and `semantic_redundancy` for repetition that adds nothing. | The source's example is paraphrastic repetition, not necessarily the same construction as #51. | Record as a deliberate-use control; take no further product action without evaluation. | pending | not started |
| C13: Signposts such as `essentially`, `in short`, and `the point is` can help readers reorient if useful content follows. | Direct craft judgment and one concrete author-labelled `Essentially` example; no reader test. Treating the separate `In summary` paragraph as content-bearing is the reviewer's application of Shankar's criterion. | Challenges current behavior. The concrete `Essentially` example passes #44 and #47, while the reviewer-selected content-bearing paragraph beginning `In summary` fails #44 on one occurrence. | #44 treats listed conclusion signposts as failures without testing whether the following content is useful; its genre gates do not cover ordinary technical explanation. | Evaluate #44 with reviewer-labelled content-bearing and empty summary-signpost pairs before deciding whether to add a content or context control. | pending | not started |
| C14: Parallel structure can organize related ideas when each clause contributes new information. | Direct craft judgment and one three-clause example; no reader study. | Fully covered by process guidance to preserve parallel forms that compare real content and by #10/`formulaic_parallelism` only when symmetry substitutes for information. The exact source example did not trigger #10 in focused execution. | No material gap for this bounded legitimate-use claim. | Keep as a control for #10 and take no further action. | pending | not started |
| C15: Predictable headings such as `Why X fails`, `What to do instead`, and `How to know if it worked` can be clear when their sections deliver. | Direct craft judgment with a three-heading schema; no outcome study. | Fully covered. #38 targets an identical short label repeated three times, not distinct echoing headings, and the three source headings passed focused #38/#44 execution when paired with distinct body text. | #38's implementation can also count repeated short body lines, but that is outside this source claim. | Keep the heading schema as a legitimate control; take no further source-driven action. | pending | not started |
| C16: A declarative opening can ground readers when the body supplies evidence. | Direct craft judgment and one evaluation-topic example; no reader study. | Fully covered by the absence of a declarative-opening ban and by source/evidence review for whether support follows. | No implementation is needed merely to preserve an allowed construction. | Record as a legitimate control and take no further action. | pending | not started |
| C17: Em dashes can add clarification, shifts, rhythm, emphasis, and conversational flow when used well. | Direct human-practitioner preference and legitimate-use claim; no frequency comparison or model evidence. | Challenges #49. Focused execution fails the source's single intentional em dash; the live check counts any U+2014 and All requires removal despite the catalogue tolerance note. | The implementation cannot distinguish deliberate human use, density, function, genre, or quoted/source-preserved text at the raw check level. | Add Shankar to the pending matched evaluation of deliberate em-dash preservation; do not change #49 without human and generated controls. | rejected | not applicable |
| C18: Shankar's writing loop is outline, draft, read, critique, and revise at varying granularities; she identifies the current bottleneck and delegates only enough to regain momentum. | Direct self-reported process; no comparative productivity or quality evaluation. | Partly covered by the project's plan-edit-audit loop and meaning-preservation requirements. | The live process begins after an Audit and does not describe bottleneck-limited delegation during composition. | Record as optional process evidence and compare it with the Write lifecycle before proposing guidance. | pending | not started |
| C19: Shankar narrates the intended story to an LLM for a detailed outline and does not draft until the structure feels solid. | Direct self-reported workflow; no prompt, model, output, or outcome preserved. | Not covered by current write or rewrite guidance. | No evidence shows this method generalizes or improves results. | Consider only as optional authoring guidance after a closed-brief and outcome-preservation evaluation. | pending | not started |
| C20: She drafts each paragraph herself, uses the model when phrasing stalls, then chooses and edits a completion. | Direct self-report plus one rough-fragment/`finish it` example; model and alternative completions are not preserved. | Not covered as an authoring workflow; current process covers fidelity after a draft exists. | The example supplies no comparison against unaided drafting or broader model behavior. | Record as bounded human-in-the-loop practice; do not turn it into required workflow. | pending | not started |
| C21: Scoped rewrite prompts are preferable to `make it better`; one strategy places the subject and verb close together near the sentence opening. | Direct self-reported strategy; no controlled evaluation. | Partly covered by process instructions to plan a specific edit and validate changed context; general subject-verb placement is not named, while H21 covers adjacent subject choice. | The rule could be harmful when genre, emphasis, or syntax calls for a different order. | Evaluate subject-verb placement as optional rewrite guidance with preservation and genre controls. | pending | not started |
| C22: SWBST can compactly express actor, goal, obstacle, response, and outcome in technical decision narratives. | Direct craft interpretation and one GPT-4/retrieval/reranking example; the education-history statement is uncited and no reader outcome is measured. | Not covered by a named check, assessment, hypothesis, or process formula. | A fixed five-beat template could itself create formulaic structure or distort source chronology. | Test SWBST on technical decision passages against formulaic-parallelism, factual-preservation, and non-narrative controls before any guidance. | pending | not started |
| C23: Text generation is cheap, including high quality in narrow scopes, but framing, depth, and judgment remain hard; contribution should be commensurate with length. | Direct author interpretation and closing craft standard; no cost, quality, or capability measurement. | Partly covered by H21, closed-source factual discipline, and process requirements against padding or invented material. | The project does not assess contribution relative to length, and the model-capability claim is time-sensitive and unmeasured. | Retain the craft standard as H21 context while recording the capability statement as dated interpretation, not a current-model fact. | pending | not started |

## Recommendations

- C01: Record the bounded practitioner method, unquantified machine-generated-reading framing, workflow scope, and no-authorship limit in source mappings; no checker change.
- C02: Evaluate the exact empty-summary examples with human controls under H21 and `semantic_redundancy` before adapting #34.
- C03: Test #31's line-ratio behavior on short legitimate lists and context-dependent prose before any threshold or guidance change.
- C04: Reconcile #52's documented and implemented eligibility, then use the pair only as a short-form control.
- C05: Evaluate subject-topic alignment under H21 as an agent-assessment or rewrite-only question.
- C06: Preserve the Gemini 2.5 Pro excerpt as a bounded H21 candidate with matched controls.
- C07: Retain #5 and complete-Audit mappings; add no new rule.
- C08: Retain `referential_clarity` and #35 candidate mappings with the explicit human look-alike; do not infer a lower threshold.
- C09: Evaluate an audience-knowledge assessment with technical and expert-audience controls.
- C10: Record terminology verification only; require domain evidence before calling a term invented.
- C11: Use the clarity, intention, and control qualification as the governing boundary for C12-C17.
- C12: Keep purposeful repetition as a deliberate-use control and take no further source-driven action.
- C13: Evaluate #44 with useful and empty summary-signpost pairs before changing behavior.
- C14: Keep the source example as a legitimate parallelism control and take no further action.
- C15: Keep the heading schema as a legitimate #38/#44 control and take no further action.
- C16: Record declarative openings as legitimate when supported; take no further action.
- C17: Add Shankar to the pending matched evaluation of deliberate em-dash preservation.
- C18: Compare bottleneck-limited delegation with the current Write lifecycle before proposing optional process guidance.
- C19: Consider narrated-outline guidance only after closed-brief and outcome-preservation evaluation.
- C20: Record the bounded human-in-the-loop workflow without making it mandatory.
- C21: Evaluate scoped subject-verb placement with fidelity and genre controls.
- C22: Test SWBST against formulaic structure, chronology, and factual-preservation controls.
- C23: Retain contribution-relative-to-length as H21 context and the capability statement as dated interpretation.

## Evaluation of approved changes

- C04: passed - #52 eligibility reconciled with documentation in commit 13e235f (skip under 100 words or under 6 sentences; `human-eyes/scripts/grade.py` plus regression tests in `dev/evals/tests/test_grade.py`); `python3 -m unittest dev.evals.tests.test_grade` passes on 2026-07-17.
- C17: not applicable - rejected 2026-07-17; #49 remains fail-on-any as a deliberate stance and no product change was made.
- C02: passed - `semantic_redundancy` registry prompt extended to closing paragraphs that restate without adding (`human-eyes/scripts/judgement.json`); `python3 -m unittest dev.evals.tests.test_judgement_json` passes on 2026-07-17.
- C09: passed - new `audience_knowledge_mismatch` agent-judgement record added to `human-eyes/scripts/judgement.json`; `python3 -m unittest dev.evals.tests.test_judgement_json` passes on 2026-07-17.
- All other rows (C01, C03, C05-C08, C10-C16, C18-C23): not applicable - recommendations remain pending; no product, checker, registry, test, hypothesis, or guidance change was authorized or made.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: /root/shankar_reviewer; initial five-lens review plus two focused re-checks
- **Findings resolved:** Six material findings resolved: extraction provenance now records reuse of the prior Markdown body after current-HTML comparison; C01 restores the source's LLM-generated wording and unquantified machine-generated-reading frame; C03/C13 label reviewer-selected controls; C01 is partly covered; C07/C09 remove unsupported #41/H8 coverage; and the standalone C01 recommendation matches its authoritative table row. Final reviewer verdict: `VERDICT: focused re-check passed with no unresolved findings`.
- **Unresolved findings:** none
