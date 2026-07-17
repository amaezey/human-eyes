# Laura Preston: HUMAN_FALLBACK

## Metadata

- **URL:** https://www.nplusonemag.com/issue-44/essays/human_fallback/
- **Author / owner:** Laura Preston
- **Published:** Winter 2023 issue; HTML metadata records 2022-11-21T16:43:13-05:00 and modification 2022-12-12T10:18:15-05:00
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** First-person practitioner observation / literary-cultural essay
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** n+1 WordPress post 33730
- **Version / revision:** publisher HTML with article:modified_time 2022-12-12T10:18:15-05:00; prior unversioned direct-HTML extraction retrieved 2026-05-05 archived by exact digest
- **Full-text status:** complete
- **Snapshot:** `snapshots/preston-human-fallback.md`
- **Extraction method:** canonical HTML and WordPress shortlink fetched with `curl -L`; publisher header, caption, and all direct article-body paragraphs and block quotations inspected with Beautiful Soup 4; all 94 text-bearing blocks compared in order with the archived extraction
- **Snapshot SHA-256:** `c1d6433717dd82834cd0706fb1ee84e94184813ed9cbab322192e5afedc66e82`
- **Model / corpus scope:** English-language first-person account of about sixty human operators supervising Brenda, a US real-estate conversational AI, during Preston's nine months of work beginning in spring 2019 and ending 2020-01-31; keyword classification, database/boilerplate retrieval, queued text replies, and human takeover are described, but the company, model architecture/version, training data, message count, logs, accuracy, comparison group, and independent evaluation are not supplied
- **Access limitations:** none for the complete publisher article text. Navigation, share controls, subscription/donation material, advertising, and related-page chrome were excluded. Six decorative horizontal rules and three `Tweet` controls were omitted; inline styling and non-breaking spaces were normalised. The non-evidentiary hero image was not preserved, but its full caption is in the snapshot.

## Summary

Preston's essay is a first-person account of supervising a pre-ChatGPT real-estate conversational system. It documents a layered workflow in which keyword classification and boilerplate generation were followed by timed human review, lightweight tag correction, or full `HUMAN_FALLBACK` takeover. Its strongest contribution to human-eyes is process evidence: automated recognition, bounded human judgement, uncertainty, missing knowledge, script-breaking replies, deceptive persona continuity, unequal access, and reviewer burden must be kept separate. The essay is not a measured writing study, supplies no reusable prose tell or threshold, and cannot validate the legacy mappings to #30, #36, or #37.

## Main insights

- Brenda classified messages by keywords, selected database-backed boilerplate, and queued replies behind a three-minute timer for an operator to review.
- Operators usually corrected a classification, selected an existing response, or softened a composite response; full takeover was reserved for messages Brenda tagged `HUMAN_FALLBACK`.
- Idioms, out-of-domain questions, multi-question composites, non-binary replies, ambiguous disclosures, emotional stakes, and requests for unavailable specifics exposed different failure modes and demanded different interventions.
- Human fallback did not create knowledge or authority. Operators could not determine eligibility, inspect properties, answer many accessibility questions, or safely resolve tenant emergencies.
- A prospect threatened to shoot everyone in a leasing office; the office closed, operators sought guidance, and the essay reports an engineer dismissing the concern. This is a bounded workplace anecdote, not a general safety-system result.
- Brenda and the operators were forbidden to say `I don't know`, disclose the bot, or directly answer suspected-bot questions; confident deflection and persona continuity could hide those limits.
- The source includes positive operational counterevidence: rapid database lookup, round-the-clock availability, reduced office phone load, and scheduled tours. These are author-described benefits, not measured outcomes.
- A developer claim that uniform responses meant no bias is challenged within the essay by exclusion of people without reliable devices or English literacy and by inaccessible property/contact information.
- Timers, message volume, surveillance, shift scarcity, public shaming, emotional disclosures, and low-cost labour shaped review quality and depleted operators.
- Preston describes bidirectional adaptation: Brenda reportedly learned operator language, while operators absorbed Brenda's lexicon and sometimes allowed awkward replies to discourage intimate disclosures.
- The article's examples are quoted conversations and literary narration from one operator's experience. They are not a corpus of AI versus human prose and do not establish authorship signals.

## Evidence and claims to extract

- **Direct source reviewed:** the complete publisher article at n+1 WordPress post 33730, canonical and shortlink routes, versioned by the page's 2022-12-12 modification timestamp. The rendered body has 78 paragraphs, 16 block quotations, and six decorative horizontal rules; all 94 text-bearing blocks were checked at the beginning, midpoint, and end and matched sequentially with the archived article body.
- **Method and sample:** qualitative first-person retrospective of nine months in 2019-2020, about sixty operators, one named conversational product, US rental-listing interactions, English article text, and selected prospect/operator exchanges. Preston reports $25 hourly pay, fifteen-to-thirty weekly hours allocated through a shift lottery, five-hour shifts with one ten-minute break, ten-hour double shifts with two ten-minute breaks, and a forty-five-minute fair-housing presentation during onboarding; these are working conditions in the account, not an independent employment record, time study, or training evaluation. No systematic sample, raw logs, denominator, model/version, accuracy measure, control group, interview method, independent corroboration, or current-system replication is reported.
- **Direct versus cited evidence:** C01-C05 and C07-C10 mainly report Preston's work observations and selected exchanges. C06 is Preston's critique of a developer claim. C11 combines author-observed capabilities with company/client framing. C12-C13 are source-record scope conclusions from the complete article. C14 distinguishes recruiter, developer, supervisor, and company claims from independently verified findings. C15 is a reviewer boundary drawn from the source's unresolved identity episode and the project's no-authorship rule. The article cites no research or external evidentiary source.
- **Important limits and counterexamples:** one operator and one company context; selected anecdotes; no message counts, rates, logs, model details, or human comparison; remembered dialogue may be curated; the source predates current generative chat systems; successful routing and scheduling coexist with failures; human review sometimes improved context and tone but could not supply missing facts, authority, or a reliable response to the reported threat; the exact pay, shift, break, and training parameters are author-reported rather than independently evaluated; consistent replies did not guarantee equitable treatment; full fallback was not invoked for every error; and the article does not prove any participant's digital identity or any document's authorship.

## Skill-use audit

- **Good use:** support a process distinction between deterministic candidates, complete contextual review, and explicit escalation; reinforce closed-source rewriting, uncertainty disclosure, source-grounded specifics, and human review for context the surface layer cannot resolve.
- **Misuse / overclaim:** treating `HUMAN_FALLBACK` as a validated confidence threshold, generalising Brenda's 2019 behaviour to current LLMs, converting prospect dialogue into a prose tell, or claiming that human review reliably fixes automated output.
- **Unsupported use:** #30 generic metaphors, #36 faux specificity, #37 neutrality collapse, a detector rule, a severity level, an authorship verdict, a model mechanism, a measured bias rate, or a claim that all consistent automation is exclusionary.
- **Underused evidence:** the live Audit requires human-supplied agent assessments but has no explicit source-backed escalation taxonomy separating wrong classification, missing knowledge, script break, emotional stakes, and reviewer overload.
- **Patterns left on the table:** none for deterministic prose recognition. Process candidates remain explicit `cannot determine` handling, task/authority boundaries, accessibility context, and a human-review workload guardrail; all require Mae's decision and broader evidence before product adoption.

## Matched patterns / rules

- `human-eyes/scripts/grade.py` separates deterministic checks from a complete bound Audit and refuses full status until every `judgement.json` record has a valid, source-bound answer. This is **partly covered** architecture for C01-C03 and C10, but it does not implement source-derived fallback triggers or operator-capacity controls.
- `human-eyes/scripts/judgement.json` includes contextual agent assessments for `referential_clarity`, `underspecified_language`, `context_leakage`, `performed_candour`, and `genre_specific`. These are adjacent to ambiguity, missing criteria, absent context, authenticity language, and genre handling; they do not validate a Brenda-specific rule or establish provenance.
- `human-eyes/references/process.md` requires a complete Audit before rewriting, treats source and brief as closed factual records, protects qualifications and deliberate choices, reports remaining findings, and forbids authorship statements. This substantially covers C04, C12-C15 as project boundaries, but not disclosure policy, accessibility, or reviewer labour.
- `human-eyes/references/sources/pattern-opportunities.md` explicitly removes Preston's inherited #30/#36/#37 mappings and retains human-fallback, script-break, and missing-specifics process guidance. The non-promotion is correct and remains pending rather than implemented product evidence.
- No focused surface-only check was run: the complete source scan identified no claim that proposes an exact deterministic construction, and the relevant live mechanisms were inspected directly in `grade.py`, `judgement.json`, `process.md`, `patterns.json`, and the generated `patterns.md` catalogue.

## Associated hypotheses

- None supported directly. The legacy H8 audience-aware-voice and H9 similar-species-disambiguation mappings are retired: Brenda's persona emulation and Preston's account of script breaks do not test human-eyes invocation voice or pattern look-alike explanations. H12 genre-aware thresholds and H16 human review of judge disagreement are conceptually adjacent but receive no comparative or evaluation evidence from this essay.

## Questions / follow-up

- Should human-eyes name separate escalation reasons for missing factual authority, ambiguous reference, script-breaking intent, emotional stakes, and inaccessible context, or is the current complete-Audit requirement sufficient?
- Should the report surface an explicit `cannot determine from the supplied source` outcome when closed-source review cannot answer a user-relevant question?
- If accessibility or reviewer workload becomes product guidance, what broader direct evidence and user testing should supplement this single practitioner account?
- Would any future agent-output review need an authoritative escalation outcome distinct from ordinary human prose review, or is that safety/service-design question outside human-eyes's scope?
- No missing source material blocks this record. Product changes remain pending decisions for Mae.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none found in legacy record; exact legacy bytes identified by SHA-256 | `snapshots/archive/preston-human-fallback/2026-05-05-75b6bded.md` | 2026-05-05 | `75b6bdedd678e95ee5823f67d290ff50ee270108560c66c697406252998c6e70` |
| current | n+1 WordPress post 33730 | `snapshots/preston-human-fallback.md` | 2026-07-17 | `c1d6433717dd82834cd0706fb1ee84e94184813ed9cbab322192e5afedc66e82` |

The prior card did not record a snapshot digest, so no historical digest existed to verify. Before replacement, the exact on-disk bytes were hashed as `75b6bdedd678e95ee5823f67d290ff50ee270108560c66c697406252998c6e70`, archived unchanged, and verified byte-for-byte with `cmp`. The current canonical and shortlink routes exposed the same 94 text-bearing body blocks as the archive. No substantive article-body addition, removal, or reordering was found; the refresh corrects legacy inline-span extraction artifacts such as split drop caps and spaces before punctuation. It also adds complete provenance, the publisher header/deck/caption, extraction verification, claim IDs, live-project coverage, and decision states.

## Decision history

- The legacy card had no authoritative Project coverage table, claim-keyed user decisions, implementation statuses, snapshot digest, update history, or independent-review record. No earlier recommendation can be treated as approved or implemented.
- The inherited #30 generic-metaphor, #36 faux-specificity, and #37 neutrality-collapse mappings were already removed in `pattern-opportunities.md`; C13 confirms that retirement from the complete article.
- The legacy H8 and H9 associations are retired as conceptual adjacency rather than source support.
- All current recommendations are `pending` / `not started`. No checker, registry, test, hypothesis, guidance, shared index, or product file changed.

## Project coverage

This is the authoritative review table. Coverage statements name the live implementations inspected; no surface-only result is presented as a complete Audit.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Brenda scanned messages for keywords, assigned a classification tag, selected database boilerplate, and queued a reply behind a three-minute human-review timer; she also offered rapid lookup and round-the-clock availability. | Direct first-person operational description plus author-observed capability; no logs, error rate, latency data, or measured comparison with leasing agents. | `grade.py` builds a bound work bundle containing programmatic checks and empty agent answers before full review; **partly covered** as layered architecture, not as evidence that this exact workflow is effective. | The project has no queue timer, workload model, or source-backed claim that automated first pass plus human review improves outcomes. | **Test-adapt:** retain as process rationale only; if escalation architecture is changed, evaluate recognition, review completeness, reviewer load, and failure handling separately. | pending | not started |
| C02: Operators normally corrected wrong classifications, selected an existing answer, or softened overstuffed composite replies; full takeover occurred when Brenda recognised non-understanding and emitted `HUMAN_FALLBACK`. | Direct practitioner description distinguishing light correction from full takeover; no frequency, decision criteria, false-negative count, or outcome measure. | `grade.py` and `judgement.json` separate deterministic candidates from agent assessment and require every agent record for a complete Audit; **partly covered**. | No explicit escalation reason or confidence boundary distinguishes a wrong candidate, missing knowledge, ambiguous intent, or failed assessment. | **Test-adapt:** evaluate a named escalation taxonomy before changing process guidance; do not copy Brenda's tag or imply a validated threshold. | pending | not started |
| C03: Idioms, out-of-domain questions, multi-question composites, non-binary answers, ambiguous disclosures, and emotionally charged messages could break Brenda's script or require contextual takeover. | Selected first-person examples across one rental chatbot; examples demonstrate possibility and heterogeneity, not prevalence or an exhaustive taxonomy. | `judgement.json` contextual assessments and open H9 look-alike work are adjacent; **partly covered** for contextual reading, not for script-break detection. | The project has no agent assessment specifically for user intent, emotional stakes, or out-of-domain authority, and a regex would be inappropriate. | **Test-adapt:** if broader evidence supports it, add non-deterministic review prompts and legitimate-context controls; do not add lexical triggers from prospect dialogue. | pending | not started |
| C04: Human fallback could not answer questions outside the operators' data or authority, including eligibility, property specifics, accessibility, tenant emergencies, and safety escalation. After a prospect threatened to shoot everyone in a leasing office, the office closed, operators sought guidance, and an engineer reportedly dismissed the concern; operators were also told not to say `I don't know` and instead redirected users. | Direct workplace account and quoted examples; no independent property, company, police, or user record and no general safety-system evaluation. This is a bounded null on fallback sufficiency, not proof that human review always fails. | `process.md` treats source and brief as closed factual records, prohibits invented facts, protects uncertainty, and reports remaining findings; **partly covered** as a writing boundary. | The report has no standard `cannot determine` outcome, and the prose-review workflow has no authoritative escalation path for a reviewer who lacks facts, authority, or safety responsibility. Service-agent safety design is outside the current product scope. | **Test-adapt the boundary only:** keep the existing closed-source rule and consider explicit `cannot determine` wording; require separate safety and human-factors evidence before any authoritative-escalation guidance or product expansion. | pending | not started |
| C05: Operators emulated Brenda's persona, customers were not meant to notice the handoff, suspected-bot questions could not be answered `Yes`, and the prescribed response was `I'm real!`. | Direct first-person account of company instructions and practice; no policy document, customer study, or independent verification. | `performed_candour` preserves literal uses and quotations while flagging empty authenticity boosters, and `process.md` forbids authorship claims; **partly covered**. | A prose-style check cannot decide whether a speaker is a bot or whether disclosure is adequate; the source raises a policy issue outside the current rewrite scope. | **Do not adopt** `I'm real!` as an authorship tell or generic banned phrase; record the disclosure boundary and require separate policy evidence for any product change. | pending | not started |
| C06: Developers framed Brenda's identical treatment as freedom from bias, but Preston says the system repelled people without smartphones, reliable internet, English literacy, or pre-visit accessibility information and blocked some tenants from management. | Direct report of a developer claim followed by Preston's qualitative counterexamples; no subgroup counts, causal design, or measured disparity. | H9/H12 propose contextual and register controls, while `process.md` forbids authorship inference; **not covered** for access or service-design equity. | The essay challenges consistency-as-fairness but cannot quantify bias or validate a universal mechanism. | **Test-adapt only with broader evidence:** keep accessibility and language as context questions, not prose signals or measured bias claims. | pending | not started |
| C07: Brenda repeatedly steered conversations toward booking a property tour and could deflect questions that did not advance that goal; Preston explicitly writes that the point was to add prospects to the database, book tours, and turn prospects into residents. | Direct author interpretation supported by observed routing examples; no conversion data, internal objective specification, or independent confirmation. | Closed-source rewriting and stance preservation constrain invented goals, but no live check assesses goal misalignment; **not covered**. | Human-eyes reviews prose, not service-agent objective design, and cannot infer an unseen system goal from a standalone document that lacks Preston's direct account. | **Do not adopt** as a checker; retain as process context if future agent-output review explicitly covers task versus user-goal conflict. | pending | not started |
| C08: Message volume, three-minute timers, supervisor monitoring, public Slack shaming, limited breaks, and shift pressure pushed operators toward reflexive triage. Preston reports $25 hourly pay, fifteen-to-thirty weekly hours assigned through a shift lottery, five-hour shifts with one ten-minute break, ten-hour double shifts with two ten-minute breaks, and a forty-five-minute fair-housing presentation during onboarding. | First-person workplace account with exact author-reported operating parameters; no time study, comparison group, independent employment record, training assessment, or causal estimate of review quality. | No reviewer-capacity, labour-condition, or training-adequacy mechanism; **not covered**. | A human-review requirement can still fail when reviewers lack time, authority, preparation, or safe escalation, but one essay cannot set capacity or training thresholds. | **Record only:** if reviewer workload or preparation becomes guidance, obtain broader human-factors evidence and test the workflow; take no product action now. | pending | not started |
| C09: Preston describes emotional depletion and bidirectional adaptation: operators absorbed Brenda's lexicon and one operator allowed odd replies through because they discouraged intimate disclosures. | Direct introspection and selected behaviour from one operator; Brenda's machine-learning uptake is recruiter/company-reported, not independently verified. | No operator-adaptation or emotional-load mechanism; **not covered**. | The source cannot establish a general cognitive effect, learning mechanism, or current-model behaviour. | **Do not adopt** a causal or model-mechanism claim; preserve the bounded workload and adaptation observation as practitioner context. | pending | not started |
| C10: Human intervention sometimes added empathy, alternatives, line breaks, or a more suitable classification, yet Preston says much work was mouse-click correction and later let factually accurate but graceless replies pass. | Direct paired examples and practitioner interpretation, with negative and counterexample evidence; no blinded quality assessment or user outcome. | A complete Audit plus source-preserving rewrite is **partly covered** as a higher-context review path. | The source does not prove that human editing is reliably better, that tone always matters, or that every automated response requires takeover. | **Test-adapt:** use paired, source-bound evaluation before changing human-review guidance; preserve the null and counterexample rather than claiming guaranteed improvement. | pending | not started |
| C11: Brenda reduced office phone load, scheduled tours, worked continuously, and cross-referenced property data quickly; the company paired these benefits with inexpensive humanities-trained operators. | Author-observed and company-framed benefits with no cost accounting, baseline, or independent outcome measure; an important counterweight to the failure narrative. | No product mechanism and outside prose-pattern scope; **not covered**, appropriately. | Omitting the positive capabilities would distort the source, while generalising them would overclaim. | **Record only** with the measurement limits; take no checker, threshold, or architecture action. | pending | not started |
| C12: The evidence is one English-language literary account of one 2019-2020 real-estate system and about sixty operators, with no disclosed model version, logs, sample counts, control group, or current replication. | Direct scope facts plus explicit absences from the complete article. | Current source metadata, update provenance, and no-authorship boundary **fully cover** this evidence limitation. | The legacy card blurred process relevance with support for current prose patterns. | **Adopt the boundary, not a feature:** keep every use dated, domain-specific, qualitative, and non-authorial. | pending | not started |
| C13: The article contains Preston's own vivid metaphors, stance, and lived specifics but does not compare human and AI prose, measure any construction, or report a rewrite experiment; it therefore does not support #30, #36, or #37. | Source-record inference from all 94 text blocks and the absence of a comparison method; the article's literary language is human-authored content, not a controlled human baseline. | `pattern-opportunities.md` already removes all three inherited mappings; **fully covered** as explicit non-promotion. | The legacy card still named H8/H9 without evidence and lacked claim-keyed rationale. | **Do not adopt** any prose-pattern mapping; retain the exact non-promotion and retire the H8/H9 source-support labels. | pending | not started |
| C14: Recruiter, developer, supervisor, and company statements within the essay include claims about fluency, machine learning, fairness, efficiency, and recommended tactics; none is independently sourced in the article. | Directly preserved reported speech and Preston's recollection, but indirect as technical or performance evidence. The article has no citations or reference list. | The source-ingest directness rules and this card's evidence separation **fully cover** attribution; no product check consumes the claims. | Repeating reported claims as measured findings would erase provenance and uncertainty. | **Adopt the attribution boundary only:** label these as reported company/workplace claims and require separate direct evidence before technical use. | pending | not started |
| C15: Preston cannot resolve whether Raymond Egg was a real person or a collage of real and copied material after reverse-image checks found paintings by other artists. | Direct anecdote and explicit unresolved interpretation; no preserved images, search record, or identity evidence. | `process.md` forbids authorship statements and protects uncertainty; **fully covered** as a reporting boundary. | The episode concerns uncertain identity and copied imagery, not AI-text provenance or a prose construction. | **Do not adopt** as an AI-text signal; retain only as a concrete example of unresolved digital identity and attribution. | pending | not started |

## Recommendations

- C01: Test-adapt the layered-workflow rationale only through separate evaluation of recognition, review completeness, load, and failure handling.
- C02: Evaluate a named escalation taxonomy before changing process guidance; do not copy Brenda's tag or imply a threshold.
- C03: Consider context-sensitive, non-deterministic review prompts only with broader evidence and controls; add no lexical trigger.
- C04: Keep the closed-source rule, consider explicit `cannot determine` wording, and require separate safety/human-factors evidence before any authoritative-escalation guidance.
- C05: Do not adopt `I'm real!` as an authorship tell or generic banned phrase.
- C06: Consider accessibility and language context only with broader evidence; add no prose signal or bias magnitude.
- C07: Do not add a checker; retain goal-misalignment as out-of-scope process context.
- C08: Record the exact author-reported pay, hours, breaks, shift allocation, and onboarding conditions with their limits; require broader human-factors evidence before guidance.
- C09: Record the bounded adaptation account; do not infer causal cognitive or model effects.
- C10: Require paired, source-bound evaluation before claiming human intervention improves output.
- C11: Preserve the positive operational counterevidence and take no product action.
- C12: Keep the date/domain/method boundary and no-authorship rule.
- C13: Maintain the #30/#36/#37 non-promotion and retire H8/H9 source-support labels.
- C14: Preserve reported-speech attribution; require separate direct evidence for technical claims.
- C15: Retain identity uncertainty; do not promote it as AI-text evidence.

## Evaluation of approved changes

- C01: not applicable - pending user decision; no product change implemented.
- C02: not applicable - pending user decision; no product change implemented.
- C03: not applicable - pending user decision; no product change implemented.
- C04: not applicable - pending user decision; no product change implemented.
- C05: not applicable - pending user decision; no product change implemented.
- C06: not applicable - pending user decision; no product change implemented.
- C07: not applicable - pending user decision; no product change implemented.
- C08: not applicable - pending user decision; no product change implemented.
- C09: not applicable - pending user decision; no product change implemented.
- C10: not applicable - pending user decision; no product change implemented.
- C11: not applicable - pending user decision; no product change implemented.
- C12: not applicable - pending user decision; no product change implemented.
- C13: not applicable - pending user decision; no product change implemented.
- C14: not applicable - pending user decision; no product change implemented.
- C15: not applicable - pending user decision; no product change implemented.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `preston_fallback_review_once`; focused recheck by the same reviewer after remediation of three findings
- **Reviewer isolation:** fresh source-dedicated agent; one source only; not reused
- **Findings resolved:** (1) added the bounded shooting-threat escalation failure and separated it from any general safety-system claim; (2) added the exact author-reported pay, weekly-hour, shift-lottery, break, and fair-housing-onboarding conditions with explicit evidence limits; (3) corrected the tour-conversion objective from reviewer inference to Preston's direct author interpretation. The same reviewer rechecked the affected passages and found no new discrepancy.
- **Unresolved findings:** none
