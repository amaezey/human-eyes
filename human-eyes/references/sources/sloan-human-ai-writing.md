# Robin Sloan: Writing with the machine

## Metadata

- **URL:** https://www.robinsloan.com/notes/writing-with-the-machine/
- **Author / owner:** Robin Sloan
- **Published:** May 2016
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** practitioner essay and first-party software demonstration
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** live first-party HTML retrieved 2026-07-17, with HTTP `Last-Modified: Mon, 13 Jul 2026 15:54:04 GMT`; previous Jina-derived snapshot retrieved 2026-05-05; no page-specific revision ID
- **Full-text status:** complete
- **Snapshot:** `snapshots/sloan-human-ai-writing.md`
- **Extraction method:** direct first-party HTML downloaded with `curl`, complete `<main>` converted to Markdown and checked through a rendered-reader view; three first-party images downloaded and inspected; cited GitHub implementation READMEs and May 2016 commit histories checked for implementation identity and context, but not used as claim evidence
- **Snapshot SHA-256:** `c822ab3c187af1a43deb4cfad11301a0bba94fdd6a4a5599a0bbe6404f3cc38b`
- **Model / corpus scope:** an unspecified recurrent neural network used through `torch-rnn-server` and the Atom `rnn-writer` plugin in May 2016; trained on Sloan's lightly processed approximately 150 MB, 149,326,361-character corpus derived from *Galaxy* and *IF Magazine* scans in the Internet Archive Pulp Magazine Archive; English science-fiction text containing OCR errors and advertisements, normalized into one text file with no line breaks; no model architecture/configuration, sampling settings, prompt log, repeated trials, comparison corpus, or human baseline reported
- **Access limitations:** none for the essay, its three images, or the cited implementation READMEs. The page has no stable revision history; the HTTP `Last-Modified` value is a server-supplied page timestamp, not a content revision ID. The linked code repositories and corpus are contextual external works, not separately ingested evidence records.

## Summary

Robin Sloan's May 2016 first-person essay describes a two-part, on-demand writing tool: an Atom plugin requests inline continuations from a character-level RNN server trained on old science fiction. The direct evidence is a practitioner build report, two selected animated demonstrations, and Sloan's reflection on using the tool. Its useful contribution to human-eyes is bounded process framing: deliberate human control, augmentation rather than outsourcing, and creative difference rather than surface polish. It is not a study of AI-writing tells, modern transformer models, writing quality, authorship, prevalence, or detection, and its strongest result is negative: the shared tools had not yet produced effects worth their effort.

## Main insights

- Sloan describes a user-initiated call-and-response workflow: the writer presses `tab` to request a suggestion and can work with the RNN's output inside the editor. Exact accept/reject key mappings appear only in the separately accessed current `rnn-writer` README and are not claim evidence here.
- The two GIFs are selected demonstrations rather than a sample. They show locally coherent and strange science-fiction continuations, but provide no output log, rejected-output inventory, rate, comparison, or evaluation criterion.
- Sloan reports an initially deflating first hour and a later, qualified improvement in his view of the tool. He immediately generalises the disappointment as “an unavoidable emotional waystation in any project, and possibly a crucial one”; this is author interpretation from one experience, not a measured usability, quality, or project-development result.
- He rejects the goal of an editor that “writes for you” and instead names augmentation, partnership, and call and response. His goal is harder and different writing, including stranger effects, rather than easier or generically better text.
- He states that the tools do not achieve that goal because their effects do not yet compensate for the effort required. His forward-looking claim that they could get there is explicitly speculative.
- In this experiment, Sloan says corpus collection and processing mattered more than RNN design and training. The corpus was large, genre-specific, lightly normalized into one text file with no line breaks, and noisy with OCR errors and advertisements; he also says the RNN “seems to thrive on that,” a subjective observation with no metric or ablation.
- Sloan's praise of a clear-explanation culture is partly inherited: the causal importance claim belongs to an unnamed friend, and Sloan calls it reasonable based on his experience. The linked Karpathy essay, Udacity course, and Goodwin essay are examples he found useful, not evidence reviewed here for a human-eyes rule.

## Evidence and claims to extract

- **Direct source reviewed:** complete first-party live HTML of “Writing with the machine,” retrieved 2026-07-17; all 33 article `p` elements, three `h2` sections, two lists with five items, and three images were preserved or represented in the snapshot. The current first-party body is text-equivalent to the archived 2026-05-05 Jina capture after packaging and HTML layout normalization.
- **Method and sample:** first-person practitioner account of one 2016 tool build and the author's use of it; two selected animated demonstrations; unspecified RNN configuration; English science-fiction corpus of approximately 150 MB and 149,326,361 characters; no controlled prompt set, repetitions, blind assessment, human comparison, quantitative outcome, or present-day model.
- **Direct versus cited evidence:** C01-C06 are Sloan's direct implementation descriptions, selected examples, observations and interpretation, goals, negative result, and corpus report. C07 combines Sloan's direct assessment with an unnamed friend's causal claim and three linked resources; the causal part is indirect and unresolved. The separately accessed current GitHub READMEs corroborate the two-part tool identity and expose additional interaction details, and their APIs expose contemporaneous May 2016 commits. Those live repository pages were not version-pinned or preserved, so none of their added details is used as claim evidence.
- **Important limits and counterexamples:** the initial disappointment, the explicit failure to reach the stated goal, the effort-cost qualification, and the noisy corpus all constrain positive process claims. The GIFs are cherry-picked demonstrations. No claim supports a surface tell, severity, threshold, model-general tendency, quality score, authorship inference, or requirement that assisted writing be harder or stranger.

## Skill-use audit

- **Good use:** bounded practitioner rationale for retaining writer choice and deliberate form when reviewing human-AI collaborative work; historical context for on-demand, inspectable assistance; a reminder that corpus and interface choices shape a creative tool.
- **Misuse / overclaim:** treating “harder,” “different,” or “weirder” as an objective writing-quality rule; treating selected GIF continuations as representative RNN behaviour; treating an anecdotal 2016 tool as evidence about current LLMs.
- **Unsupported use:** any deterministic pattern, severity, density threshold, detector feature, authorship verdict, causal claim about training data, general productivity claim, or conclusion that collaboration necessarily preserves agency or improves writing.
- **Underused evidence:** the live project preserves deliberate form and source choices, but it does not explicitly distinguish intentional human-AI call-and-response from an editor that substitutes for the writer. That gap is process framing, not a prose-pattern gap.
- **Patterns left on the table:** none for promotion. The GIF continuations and Sloan's “dead-eyed robo-text” phrase are examples inside a selected practitioner essay, not validated pattern evidence.

## Matched patterns / rules

- `human-eyes/references/voice.md`, “Preserve the source” and “Preserve deliberate form”: partly covers C04 by retaining distinctive choices, unusual phrases, form, and images.
- `human-eyes/references/process.md`, “Plan the edit” and “Preserve meaning”: partly covers C04 by protecting stance, genre, point of view, and deliberate devices.
- `human-eyes/scripts/judgement.json`, `genre_specific.fiction`: adjacent only; it asks about surprise, revision depth, voice differentiation, and fidelity that misses a source author's oddities, but it does not evaluate collaborative process and Sloan does not validate that assessment.
- `human-eyes/references/sources/pattern-opportunities.md`, “Audience, intent, and choice as positive voice criteria” and “Pure framing essays as pattern evidence”: directly records the process-guidance and non-promotion boundaries, but its Sloan mapping needs the claim IDs added by this refresh.
- No entry in `human-eyes/scripts/patterns.json` or generated `human-eyes/references/patterns.md` implements Sloan's process framing, and this source does not justify adding one.

## Associated hypotheses

- None directly supported. The previous card's H3 and H8 mappings were too broad: Sloan offers optional creative-process framing, not evidence that detector positioning should be dropped (H3) or that audit and rewrite invocation surfaces need separate voices (H8).

## Questions / follow-up

- If Mae wants explicit human-AI collaboration language in `voice.md` or `process.md`, decide separately whether Sloan's bounded 2016 framing is useful enough to add; test that wording against accessibility, assistive-use, ordinary editing, and writer-efficiency cases so “harder” or “stranger” does not become a requirement.
- Any use of the unnamed friend's causal explanation, the linked learning resources, repository behaviour beyond the checked READMEs, or corpus effects requires direct review of that separate source or implementation.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none found | `snapshots/archive/sloan-human-ai-writing/2026-05-05-49d088c5.md` | 2026-05-05 | `49d088c5bfb889f4354c97b096a2adc1f58a196ead0ba1b48ae1489b9de58c92` |
| current | none found | `snapshots/sloan-human-ai-writing.md` | 2026-07-17 | `c822ab3c187af1a43deb4cfad11301a0bba94fdd6a4a5599a0bbe6404f3cc38b` |

The prior snapshot had no recorded digest in either the prior card or its four-column manifest row. Before replacement, its on-disk SHA-256 was computed as `49d088c5bfb889f4354c97b096a2adc1f58a196ead0ba1b48ae1489b9de58c92`; the archive copy is byte-identical. The current article prose is unchanged in substance. The refreshed snapshot adds full provenance, attachment preservation, image verification, structure counts, and explicit extraction boundaries.

## Decision history

- None: the previous card contained no claim-keyed user decisions or implementation statuses. This update retires its unsupported H3/H8 associations and replaces unkeyed recommendations with seven pending, non-product-change decisions. No checker, registry, test, hypothesis, or guidance implementation was changed.

## Project coverage

This is the authoritative review table. The source is historical practitioner evidence; “not covered” below does not imply that a new check should exist.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Sloan built a two-part 2016 tool in which an Atom plugin requests RNN continuations when the writer presses `tab`, bringing the output into an editor where the writer can work with it. | Direct first-person implementation description and GIF demonstration. The separately accessed current GitHub READMEs corroborate identity but are unpinned context and supply no evidence used in this claim. No usability sample, versioned package release, or outcome comparison. | `voice.md` and `process.md` preserve writer choices but do not describe collaborative tool topology; `patterns.json` and `judgement.json` have no process check. **Partly covered.** | The project lacks explicit wording that inspectable, user-initiated assistance differs from prose substitution, but a style checker need not encode tool architecture. | Record as bounded historical process context. If explicit collaboration wording is later proposed for `voice.md` or `process.md`, require separate user approval and task/accessibility controls; add no checker. | pending | not started |
| C02: The two selected GIFs show locally coherent and strange science-fiction continuations, including a servo-robot passage, during interactive writing. | Direct selected visual examples, fully preserved; no prompt/output log, selection method, rejected-output inventory, repetitions, rate, current model, or human control. They demonstrate possibility only. | No exact checker mapping. The `genre_specific.fiction` assessment is adjacent but tests finished-prose qualities, not selected continuation behaviour. **Not covered.** | Promoting the phrases would confuse a cherry-picked 2016 demonstration with reusable pattern evidence. | Preserve as source examples and take no product action; do not add the phrases to patterns, fixtures, or authorship guidance without a separately designed, licensed evaluation. | pending | not started |
| C03: Sloan's first hour was deflating, while longer use partially restored his interest; he calls the disappointment “an unavoidable emotional waystation in any project, and possibly a crucial one.” | Direct subjective before/after observation plus author interpretation from one builder-user; no instrument, duration beyond “more time,” comparison, or generalisable outcome. The “any project” sentence is unsupported generalisation, not a measured result. | No project implementation; `pattern-opportunities.md` treats Sloan as rationale/process rather than outcome evidence. **Not covered.** | Nothing in the source supports the project-wide generalisation or usability, learning, quality, or productivity claims; no implementation is warranted. | Record only; take no further action and do not use the anecdote or generalisation as a product-effect claim. | pending | not started |
| C04: The animating ideas are augmentation, partnership, and call and response; the desired outcome is harder and different writing, with stranger effects, not an editor that writes for the user or generically easier/better text. | Direct practitioner purpose and normative framing. It describes Sloan's aim for this tool, not a measured quality construct, universal collaboration standard, or outcome. | `voice.md` “Preserve deliberate form,” `process.md` “Plan the edit,” and the `pattern-opportunities.md` positive-voice row preserve choice and unusual form. The fiction branch in `judgement.json` asks about missed oddities but is not validated by Sloan. **Partly covered.** | Live guidance does not explicitly name on-demand human-AI collaboration; conversely, literal adoption of “harder” or “stranger” could penalise accessibility, efficiency, or ordinary editing. | Retain as optional process rationale only. Any explicit guidance addition should say writer-chosen effects may be preserved, not require difficulty or strangeness; test interpretation before implementation. | pending | not started |
| C05: Sloan says the shared tools do not achieve his goal because their effects do not yet compensate for the effort required, while speculating that they could improve. | Direct negative practitioner result plus explicitly speculative forecast; no outcome measure, time-on-task record, comparison tool, or later follow-up. | `pattern-opportunities.md` classifies Sloan as framing and not direct pattern support, but no project mechanism covers the tool-effect claim. **Not covered.** | Positive-only summaries erase the source's null/negative result and modality; no product-effect implementation is warranted. | Keep the failure and speculative modality in process citations; take no product action. | pending | not started |
| C06: For Sloan's experiment, corpus collection and processing mattered more than RNN design/training; the approximately 150 MB corpus contained 149,326,361 characters of lightly normalized *Galaxy* and *IF Magazine* scans with OCR errors and advertisements, combined into one file with no line breaks, and the RNN “seems to thrive on that.” | Direct builder report with exact corpus provenance, transformation, and size statements plus a subjective response observation; no metric, ablation, model comparison, complete preprocessing record in this source, or causal test. The claim is limited to his experience. | `dev/TESTING.md` requires source/generation provenance, corpus-overlap disclosure, and matched packaging for evaluations, but does not encode Sloan's causal ranking or “thrives” observation. **Partly covered** at the provenance-policy level. | The essay cannot establish general training-data causality, performance, or transfer from character RNNs to current LLMs. | Retain as historical provenance context only; do not add a pattern or causal mechanism. If the corpus is used in an evaluation, ingest and license-check it separately and pin its bytes. | pending | not started |
| C07: Sloan reports a strong culture of clear explanation and considers plausible an unnamed friend's view that it was as important to deep learning's rise as fast GPUs and large datasets; he names three useful learning resources. | Sloan's experience is direct practitioner observation; the causal comparison is an indirect, unnamed-friend claim. The three links are recommendations, not evidence reviewed here. | No relevant checker or process rule. The source-record contract governs attribution but does not cover the substance of this claim. **Not covered.** | Using the causal or quality claims would cross the source boundary without reviewing the cited works and would not address AI-writing patterns; no product implementation is warranted. | Record the attribution boundary and take no product action; separately ingest an upstream source only if a future decision depends on it. | pending | not started |

## Recommendations

- C01: Record the user-initiated two-part tool as bounded historical process context; require separate approval and controls before adding collaboration wording, and add no checker.
- C02: Preserve the GIFs as selected source examples only; do not promote their phrases into patterns or fixtures.
- C03: Keep the subjective negative-to-qualified-positive observation and unsupported “any project” generalisation as context only; make no product-effect claim.
- C04: Retain Sloan as optional rationale for writer choice and deliberate form; never turn “harder” or “stranger” into a quality requirement.
- C05: Preserve the explicit failure and speculative modality wherever the source is summarized; make no product change.
- C06: Retain exact corpus provenance, no-line-break transformation, and subjective “seems to thrive” wording without generalising the causal or performance claim; ingest and license-check the corpus separately only if it enters evaluation.
- C07: Keep the clear-explanation causal statement marked indirect; require separate upstream review before use.

## Evaluation of approved changes

- C01: not applicable - recommendation pending; no product change made.
- C02: not applicable - recommendation pending; no product change made.
- C03: not applicable - recommendation pending; no product change made.
- C04: not applicable - recommendation pending; no product change made.
- C05: not applicable - recommendation pending; no product change made.
- C06: not applicable - recommendation pending; no product change made.
- C07: not applicable - recommendation pending; no product change made.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/sloan_source_reviewer`; focused re-check by the same reviewer after material remediation
- **Findings resolved:** four material findings: separated unpinned GitHub README context from direct essay evidence; restored and bounded the “unavoidable emotional waystation” interpretation; restored and bounded the “seems to thrive” and no-line-break corpus details; corrected C03, C05, and C07 from fully covered to not covered
- **Unresolved findings:** none
- **Final reviewer verdict:** “Focused re-review passed: all four original findings are resolved, the affected claims remain source-faithful and internally consistent, and no new findings were introduced.”
