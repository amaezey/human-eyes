# Anthropic: Claude system-prompt release notes

## Metadata

- **URL:** https://platform.claude.com/docs/en/release-notes/system-prompts
- **Author / owner:** Anthropic
- **Published:** living release-notes page; reviewed entries are dated 2024-07-12 through 2026-06-09
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** first-party model documentation
- **Evidence tier:** First-party model docs
- **Review mode:** update
- **Stable identifier:** none found; living page capture retrieved 2026-07-15
- **Version / revision:** complete first-party Markdown capture through Claude Fable 5 dated 2026-06-09; supersedes the partial 2026-05-05 capture
- **Full-text status:** complete
- **Snapshot:** `snapshots/anthropic-sonnet-prompts.md`
- **Extraction method:** direct first-party `.md` documentation endpoint; checked against raw rendered HTML, a fully expanded 64-page browser PDF, and PDF text extraction
- **Snapshot SHA-256:** `b7a5544d3d32e3e8599885cdf13f9f9b65a5a698ba577734d33c8a4dd5fe2be3`
- **Model / corpus scope:** 16 Claude model headings and 28 dated prompt entries spanning Fable 5, Opus 4.8 through Opus 3, Sonnet 4.6 through Sonnet 3.5, and Haiku 4.5 through Haiku 3; Claude web, iOS, and Android system prompts only, not the Claude API; English prompt text with some entries instructing multilingual response behaviour; no model-output corpus, human comparison, compliance measure, prevalence estimate, or prose-length sample
- **Access limitations:** none for the accessible first-party page. The browser PDF retains page chrome and is supporting rendered verification; the direct Markdown snapshot is the authoritative complete text.

## Summary

Anthropic's complete living release-notes page preserves 28 dated web/mobile system prompts across 16 model headings. It directly documents prompt instructions about concision, lists, headings, bolding, Markdown, tone, response openings, follow-up questions, apologies, knowledge-cutoff disclosures, system-prompt leakage, repetition, metaphors, poetry, emoji, and user style controls. This is instruction-level evidence, not measured model behaviour: it cannot establish compliance, frequency, causality, a human comparison, or authorship. The full source changes the earlier partial record substantially because some instructions provide plausible provenance for candidate residue while others explicitly tell named versions not to produce patterns commonly attributed to AI.

## Main insights

- Prompt instructions change materially by model and date; a cue cannot be attributed generically to Claude from this page.
- Many 4.5-and-later entries instruct minimal formatting and restrict lists, headers, and bolding, which is direct counterevidence to a model-general claim that Claude is prompted to over-format.
- Sonnet 3.5 prompts instruct concise answers and offers to elaborate, but also explicitly forbid filler affirmations such as `Certainly!`, `Of course!`, `Absolutely!`, `Great!`, and `Sure!`.
- Entries constrain openings and turn-taking in both directions: newer prompts limit questions, praise, continued-engagement solicitation, directness preambles, and excessive apology, while Sonnet 3.7, Haiku 3.5, and Sonnet 3.5 entries dated 2024-09-09 (both text-only and text-and-images variants) and 2024-07-12 require a post-code explanation question; Sonnet 3.5 also asks for offers to elaborate or piecemeal continuation with feedback.
- Seven Opus/Sonnet 4.x entries prohibit opening by praising a question, idea, or observation as good, great, fascinating, profound, or excellent; three newer 4.x prompts also prohibit `genuinely`, `honestly`, and either `actually` or `straightforward`. These are direct negative instructions relevant to #19/#21 and #7/#56, not evidence of compliance.
- Older Sonnet 3.5 prompts tell the model to vary repeated wording; this is a direct alternative prompt-level mechanism relevant to synonym cycling, but the page supplies no output evidence that the instruction causes that pattern. Synonym cycling was removed from the catalogue on 2026-07-25 through DR-156, so the mechanism question has no product surface left to attach to.
- Knowledge-cutoff and current-date disclosures are conditionally prompted, which supplies model/version-specific provenance context for #20 without showing that such disclaimers are frequent or inappropriate in every genre.
- User requests, preferences, and style settings can override default tone and formatting, so the same model snapshot does not imply one fixed surface style.

## Evidence and claims to extract

- **Direct source reviewed:** Complete first-party Markdown response from `https://platform.claude.com/docs/en/release-notes/system-prompts.md`, retrieved 2026-07-15, with 16 model sections and 28 dated Accordion entries. The source was checked against the rendered canonical page, raw HTML, a 64-page expanded PDF, and extracted PDF text at the beginning, middle, and end.
- **Method and sample:** First-party living documentation, not a study. The sample is the complete accessible prompt archive for named Claude web/mobile releases from 2024-07-12 to 2026-06-09. It contains prompt instructions but no outputs, users, documents, comparison group, ratings, error bars, compliance tests, or human-authored prose.
- **Direct versus cited evidence:** C01-C24 are direct statements, prompt instructions, or direct comparisons among the preserved dated entries. No cited source is used to establish a project conclusion. References inside the prompts to product documentation, support pages, or external facts are not separately reviewed here.
- **Important limits and counterexamples:** A system instruction is not a behavioural result. The page cannot show whether a model follows an instruction, how often a surface feature appears, whether an instruction caused it, or whether humans use the same feature differently. User requests and style settings are explicit modifiers. Bold markup for multi-entry models marks documentation changes, while bold inside single-entry prompts may be literal prompt emphasis; neither is model-output evidence.

## Skill-use audit

- **Good use:** Use the page to scope prompt-level provenance by model, date, and product surface; identify direct instructions that align with or contradict a proposed causal story; and design later matched-output evaluations.
- **Misuse / overclaim:** Do not cite the prompt as proof that a model complied, that a pattern is prevalent, that a prompt caused a surface feature, or that a document was AI-authored.
- **Unsupported use:** The source cannot set severities, thresholds, model-family fingerprints, human-versus-model rates, or universal style rules. It cannot support Claude API claims because the page expressly excludes API prompts.
- **Underused evidence:** H25 and source mappings do not yet record the complete prompt archive's positive and negative instruction-level evidence: old follow-up offers and cutoff disclosures alongside explicit anti-affirmation, anti-overformatting, anti-list, anti-caveat, and anti-apology instructions.
- **Patterns left on the table:** Version-scoped prompt context for #13, #16, #19-#21, #31, #38, #41, and #56; none should be promoted as behavioural validation without direct outputs. The same context for #11 lapsed when that entry was removed through DR-156.

## Matched patterns / rules

- #13 `no-boldface-overuse`, #31 `no-excessive-lists`, and #38 `no-section-scaffolding`: relevant as instructed-against formatting in many recent prompts, not as observed behaviour.
- #16/#31a `no-unicode-flair`: several dated prompts instruct against unrequested emoji; the instruction does not prove output compliance.
- #19/#21 `no-collaborative-artifacts`: exact anti-affirmation wording appears in Sonnet 3.5, seven Opus/Sonnet 4.x entries prohibit opening praise, and older entries positively instruct offers to elaborate, piecemeal continuation/feedback, or a post-code explanation question. The post-code instruction appears in Sonnet 3.7, Haiku 3.5, and Sonnet 3.5 entries dated 2024-09-09 (both variants) and 2024-07-12.
- #20 `no-knowledge-cutoff-disclaimers`: several prompts conditionally require cutoff or current-information disclosures.
- #7 AI vocabulary and #56 `no-performed-candour`: Sonnet 3.5 and Haiku 3.5 explicitly forbid directness/honesty preambles, including examples beginning `I aim to` and `I need to be`; Opus 4.8, Sonnet 4.6, and Opus 4.6 prohibit `genuinely`, `honestly`, and either `actually` or `straightforward`.
- Synonym cycling (former #11, removed 2026-07-25 via DR-156): Sonnet 3.5 directs lexical variation, but supplies no output or causal test.
- #30 generic metaphors and #41 poetry review: prompts allow explanatory metaphors while Sonnet 3.7 and Haiku 3.5 instruct against hackneyed poetry imagery and predictable rhyme.
- H25 `Model-family versus generic-AI residue`: the primary project home for the prompt archive's model/date/surface boundaries.

## Associated hypotheses

- H25: Model-family versus generic-AI residue — directly supported as a provenance requirement because prompt instructions vary by model, date, product surface, and user style control; not supported as a behavioural or authorship result.

## Questions / follow-up

- Fresh independent source-record review passed after verifying all 24 claims, the 16 model headings, 28 dated entries, complete Markdown and 64-page rendered-PDF provenance, hashes, live-project coverage, decisions, and remediations.
- Any behavioural recommendation needs a separate, reproducible matched-output study that binds model ID, prompt revision/date, product surface, user instructions, language, genre, and length.
- No product implementation is justified by this first-party prompt archive alone.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none found; partial page capture retrieved 2026-05-05 | `snapshots/archive/anthropic-sonnet-prompts/2026-05-05-0ddba21120f1.md` | 2026-05-05 | `0ddba21120f1dcb30ad70a4ab31a6ce0604c7f25c36c6561c2691fdab92f9f8e` |
| current | none found; living page capture retrieved 2026-07-15 | `snapshots/anthropic-sonnet-prompts.md` | 2026-07-15 | `b7a5544d3d32e3e8599885cdf13f9f9b65a5a698ba577734d33c8a4dd5fe2be3` |

The previous contract-wrapped partial snapshot is archived byte-for-byte at the path above. The earlier raw partial capture remains at `snapshots/archive/anthropic-sonnet-prompts/2026-05-05-903911b56951.md` with SHA-256 `903911b569517a33e4e3f6519c10280e942df353698ba0d0bd1727965ba1e26e`. The current snapshot replaces loading placeholders with the complete first-party prompt bodies and preserves the rendered PDF used for verification.

## Decision history

- The partial-source C01-C07 record had `pending` / `not started` recommendations and no approved or implemented product change. Those IDs are superseded because their central premise — that no prompt bodies were available — is no longer true.
- Prior C01-C06 metadata statements are retained and expanded in current C01-C03. Prior C07, the missing-prompt-body limitation, is retired by the complete 2026-07-15 capture.
- The prior #19 non-promotion remains historically correct for the partial bytes but no longer describes the current evidence. The new record distinguishes direct prompt instructions that may provide provenance context from measured model behaviour, which remains unavailable.
- All current C01-C24 recommendations are materially new or changed and begin at `pending` / `not started`.
- C17 approved 2026-07-17 as a documentation-only rewording: #11's causal wording now presents repetition-penalty tuning as a proposed, untested mechanism, leaving the instruction-level alternative unresolved. Implemented in commit 64ac03b. Superseded 2026-07-25 by DR-156: catalogue entry #11 was removed, so no causal wording remains in the product layer and the unresolved mechanism question is moot. All other rows remain pending.
- C15 approved 2026-07-17 via DR-113: commit 340ea99 added an apology-led refusal pattern ("I'm sorry, but I can't") to #19 `no-collaborative-artifacts` as one of five pasted-chat residue families; this card remains instruction-level provenance context, not compliance evidence, and no general apology blacklist was added.
- C16 approved 2026-07-19 via DR-134 option B: `I aim to be direct` and `I need to be clear` joined #56; `straightforward` joined #7's clustering candidates. Existing coverage already handled `I need to be honest`, `honestly`, `genuinely`, and `actually` in their applicable checks.

## Project coverage

This is the authoritative review table. Coverage describes the live project, not whether the prompt instruction was obeyed by a model.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: The documented system prompts apply to Claude's web, iOS, and Android products and expressly do not apply to the Claude API. | Direct first-party scope statement; no API prompt or output comparison is supplied. | **partly covered:** H25 requires model/version/prompt-style boundaries, and this card records the surface boundary; no checker models invocation surface. | Any transfer from web/mobile prompt evidence to API output would exceed the source. | Preserve the web/mobile/API boundary in every future use; take no checker action. | pending | not started |
| C02: The page is a living prompt archive; multi-entry changes are bolded, and starting with the 4.6 generation each model ID is a single fixed snapshot. | Direct first-party versioning statement; bold is documentation-diff markup for multi-entry models, not output formatting. | **fully covered:** H25 and the source-card metadata provide the correct version-drift home. | The live source mapping previously lacked the complete archive and fixed-snapshot note. | Update source mapping only; require exact model and prompt date for future behavioural work. | pending | not started |
| C03: The reviewed archive contains 16 model headings and 28 dated entries from 2024-07-12 through 2026-06-09, with materially different instructions across entries. | Direct complete-page inventory and cross-entry comparison; no output corpus. | **fully covered:** this snapshot, manifest, and card preserve the inventory; H25 covers the interpretation. | No project gap beyond keeping the living page fresh. | Record the reviewed range and refresh only when a later revision is intentionally ingested. | pending | not started |
| C04: The page documents instructions, not compliance, frequency, causality, human comparison, or authorship. | Direct method limitation established by the source type and absence of outputs or evaluation. | **fully covered:** README evidence tiers and H25 separate first-party prompt context from prose-pattern proof. | No remaining coverage gap; future citations could still overstate directness. | Keep every mapping labelled instruction-level and non-authorship; take no product action. | pending | not started |
| C05: User requests, user preferences, and a style feature can change tone, formatting, and feature use. | Direct prompt instructions in multiple 4.5-and-later entries; the page does not test how strongly customization changes output. | **partly covered:** #13 and #31 mention requested or legitimate formatting controls, while H25 covers prompt-style variation. | The project has no explicit user-style-setting metadata field for output studies. | Add the control only to future evaluation provenance; do not change checks from this source alone. | pending | not started |
| C06: Across the archive, simple questions are generally assigned concise answers and complex/open-ended tasks more thorough answers; some versions say to provide the shortest adequate answer or one to three sentences. | Direct recurring instruction with model/date variation; no response lengths are measured. | **not covered:** `sentence-length-variance` measures within-document sentence variation, not requested response length or task complexity. | Conflating response length with sentence rhythm would be a category error. | Record as prompt-scope metadata only; take no pattern action. | pending | not started |
| C07: Many 4.5-and-later prompts say to minimize bold, headers, lists, and bullet points rather than over-format by default. | Direct negative instructions in named prompt entries; not a compliance result. | **partly covered:** #13, #31, and #38 detect over-formatting without claiming that Claude prompts cause it, and H25 supplies the general drift warning. | The source mapping does not yet record this instructed-against context; the evidence does not challenge the checks or demonstrate model behaviour. | Add source-level negative context only after approval; retain checks and make no compliance or prompt-causality claim. | pending | not started |
| C08: Several prompts reserve lists for explicit requests or genuinely multifaceted content, require substantial bullets, prefer prose for reports/documents/explanations, and sometimes forbid bullets in refusals. | Direct, context-qualified formatting instructions across multiple named entries; not universal across all 28 prompts. | **partly covered:** #31 already treats genuinely discrete and instructional lists as legitimate and flags document-level excess, but it does not record model/date prompt context. | No behavioural evidence shows whether these instructions reduce listification. | Preserve #31's context controls and record this as counterevidence to a universal prompt-causality claim; no threshold change. | pending | not started |
| C09: Older Sonnet 3.5 and Haiku 3.5 prompts prescribe Markdown syntax and spacing, while the page introduction names Markdown code snippets as a prompt function. | Direct formatting instructions; code formatting and correct Markdown are not the same as unrequested prose scaffolding. | **not covered:** #13, #14, #31, and #38 inspect excessive output structure, not compliance with Markdown syntax. | Treating correct code Markdown as an AI prose tell would be a category error. | Take no product action; preserve code/prose and requested/unrequested boundaries. | pending | not started |
| C10: Several dated prompts restrict emoji, asterisk emotes, and profanity unless requested or contextually mirrored, but those instructions are absent from some other entries. | Direct model/date-specific instructions and direct cross-entry absence; no output comparison. | **partly covered:** #16/#31a flags unrequested emoji and decorative Unicode, with UI/quoted/checklist controls; emotes and profanity are outside its scope. | The source does not validate emoji prevalence or a universal model fingerprint. | Keep #16/#31a treatment contextual and do not add emote/profanity rules from prompt text alone. | pending | not started |
| C11: Multiple prompts request warm, natural, empathetic, or conversational tone, with context-dependent prose/list choices and user customization. | Direct tone instruction; no model output or human comparison. | **partly covered:** `tonal_uniformity` reviews register lock, not the presence of a warm register, and H25 covers prompt context. | A requested warm tone is not evidence of tonal uniformity or authorship. | Record as a control for future tone evaluations; do not map warmth itself to a violation. | pending | not started |
| C12: Several prompts say not always to ask questions, to ask at most one, and to answer an ambiguous query before seeking clarification; newer prompts also avoid eliciting another turn when the user wants to stop. Conversely, Sonnet 3.7, Haiku 3.5, and Sonnet 3.5 entries dated 2024-09-09 (both text-only and text-and-images variants) and 2024-07-12 require a post-code question asking whether the user wants an explanation. | Direct positive and negative turn-taking instructions with model/date variation; the positive instruction appears in Sonnet 3.7 dated 2025-02-24, Haiku 3.5 dated 2024-10-22, and the named Sonnet 3.5 entries; no output comparison. | **partly covered:** #19 catches some follow-up offers and `context_leakage` catches answer-shaped residue, but neither counts questions or tests whether clarification or a code explanation was necessary. | A question can be required in chat and residue only when pasted into finished prose. | Keep #19's finished-prose boundary and record every named model/date instance of the post-code question as version-specific positive instruction context; do not add a bare question-count rule. | pending | not started |
| C13: Sonnet 3.5 entries instruct concise answers that offer to elaborate if more information may help; the 2024-09-09 text-only and text-and-images variants and the 2024-07-12 entry require a post-code explanation question; July and September 2024 entries also instruct piecemeal continuation with user feedback for tasks too long for one response. | Direct positive continuation instructions in 2024 Sonnet 3.5 entries; the post-code question is exact prompt wording, but the page supplies no observed output or compliance result. | **partly covered:** #19 catches `let me know`, `would you like`, and similar continuation offers, but the prompts supply functions rather than evidence that those exact output strings occur. | The source cannot establish output phrasing, frequency, or current-model persistence; these instructions are legitimate in live chat and become residue only when pasted into finished prose. | Record offers to elaborate, piecemeal feedback, and the dated Sonnet 3.5 post-code questions as version-specific positive provenance context for #19; do not expand the regex without output fixtures. | pending | not started |
| C14: Sonnet 3.5 explicitly forbids unnecessary filler affirmations including `Certainly!`, `Of course!`, `Absolutely!`, `Great!`, and `Sure!`, and forbids a `Certainly` opener. Seven Opus/Sonnet 4.x entries also prohibit opening by calling a question, idea, or observation good, great, fascinating, profound, or excellent. | Direct exact negative prompt wording in Sonnet 3.5 plus Opus 4.1 dated 2025-08-05, Opus 4 dated 2025-05-22, 2025-07-31, and 2025-08-05, and Sonnet 4 on those same three dates; not evidence of compliance. | **fully covered:** this is direct negative instruction context for #19/#21, whose live checks detect residue but do not claim that these prompts cause it. | No checker gap follows from instructed-against phrases; the source cannot establish output frequency or compliance. | Record both anti-affirmation families as negative, version-scoped prompt context; retain #19/#21 unchanged. | pending | not started |
| C15: Early Sonnet 3.5 prompts say refusals should not begin with `I'm sorry` or `I apologize`; newer prompts instead caution against excessive apology, self-critique, submission, or self-abasement after mistakes. | Direct opening and tone instructions across different dates/models; no observed refusal or mistake-response corpus. | **partly covered:** #19 does not match generic apology openings, while the AI for Lifelong Learners opportunity already records apology macros as a pending fixture candidate. | The project cannot infer that all apologies are residue or that current models follow either historical instruction. | Keep apology handling in controlled, context-specific evaluation; do not add an apology blacklist. | approved | implemented |
| C16: Sonnet 3.5 and Haiku 3.5 forbid self-announcing directness/honesty caveats such as `I aim to be direct`, `I need to be clear`, and `I need to be honest`. Newer prompts also prohibit `genuinely`, `honestly`, and either `actually` (Opus 4.8) or `straightforward` (Sonnet 4.6 and Opus 4.6). | Direct exact negative instructions; no output prevalence or compliance result. | Covered for the selected exact surfaces: #56 catches all three directness/honesty frames and `Honestly?`; #7 includes `genuinely`, `actually`, and `straightforward` as clustering candidates. | The evidence remains exact prompt wording rather than measured output frequency; no broader prompt-derived vocabulary rule was added. | Keep the exact #7/#56 forms selected in DR-134. | approved | implemented |
| C17: Sonnet 3.5 tells the model to avoid rote/repeated phrasing and vary its language. | Direct instruction; no output sample and no causal analysis. | No product surface remains. #11 carried the competing repetition-penalty explanation and was removed through DR-156, so neither mechanism appears in the catalogue. | Nothing to reconcile; the product makes no causal claim about lexical variation. | Carry no causal explanation for synonym cycling in the product layer. | approved | implemented |
| C18: Many prompts allow examples, thought experiments, or metaphors, while Sonnet 3.7 and Haiku 3.5 specifically instruct against hackneyed poetry imagery/metaphors and predictable rhyme. | Direct positive and negative craft instructions with genre/model boundaries; no generated poem or rating. | **partly covered:** #30 reviews generic metaphors and #41 has poetry-specific checks, but neither records these prompt instructions as behavioural evidence. | The prompt cannot show that metaphors are generic or that poetry avoids clichés in practice. | Record as a model/date/genre control only; take no checker action. | pending | not started |
| C19: Newer prompts tell the model not to attribute behaviour to hidden system prompts or internal mechanics and generally not to mention prompt information unless pertinent. | Direct process-residue suppression instructions; no leak-rate measurement. | **not covered:** #39 handles placeholders and `context_leakage` handles missing conversational context, not internal-mechanics attribution. | The source is negative instruction-level evidence and cannot validate a new leakage rule. | Take no product action; use only as context when directly reviewing documented process residue. | pending | not started |
| C20: The prompts provide current-date and knowledge-cutoff context and conditionally instruct disclosures when dates, obscure topics, citations, or post-cutoff events make them relevant. | Direct conditional instructions that vary by model/date; no output frequency or correctness measure. | **fully covered:** #20 detects cutoff/training disclaimers left in finished prose and distinguishes them from #19 chat residue. | The project should not imply that every disclosure is wrong inside a live chat; its product boundary is publication-ready prose. | Retain #20 and its finished-prose boundary; cite this source only as version-specific provenance context, not validation of severity. | pending | not started |
| C21: Several entries instruct responses in the user's language or all languages. | Direct prompt instruction; the preserved prompts are English and contain no multilingual outputs or comparisons. | **not covered:** the project does not claim multilingual validation from this source. | Prompt language scope cannot establish cross-language pattern performance. | Record the language instruction as metadata and require language-specific evaluation before transfer. | pending | not started |
| C22: Instruction sets appear, disappear, and change across model/date entries; Fable 5, for example, does not simply reproduce every explicit formatting constraint found in earlier 4.x entries. | Direct cross-version comparison of the complete archive; absence is bounded to the preserved prompt text, not proof of behavioural reversal. | **fully covered:** H25 is expressly about model family, version, prompt style, and drift. | The current source indexes do not yet summarize the concrete inversions and omissions. | Update only the source-level H25 mapping; require exact version/date rather than `Claude` as a generic label. | pending | not started |
| C23: Newer prompts discourage thanking someone merely for reaching out, asking them to keep talking, encouraging continued engagement, or reiterating willingness to continue. Older positive counterexamples include post-code explanation questions in Sonnet 3.7, Haiku 3.5, and Sonnet 3.5 entries dated 2024-09-09 (both variants) and 2024-07-12, plus Sonnet 3.5 offers to elaborate or continue long tasks piecemeal with feedback. | Direct negative and positive turn-continuation instructions across named model/date entries; no compliance result. | **partly covered:** #19 catches some continuation offers but not these functions generally, and the project correctly limits the check to residue in finished prose. | A generic semantic turn-solicitation check would require conversation context, version controls, and legitimate live-chat controls. | Record both instruction directions, including every named post-code-question instance, as version-specific #19 context; do not expand #19 from prompt text alone. | pending | not started |
| C24: Some prompts restrict reflective listening only when it would reinforce or amplify distress, while otherwise requesting warmth and empathy. | Direct context-qualified tone instruction; not a general prohibition and not a prose-quality study. | **not covered:** no human-eyes check targets reflective listening, and `tonal_uniformity` is not equivalent. | Removing reflective language without the emotional-risk context would misrepresent the source. | Take no product action; retain only as a counterexample to flattening prompt tone into one generic rule. | pending | not started |

## Recommendations

- C01: Preserve the web/mobile/API boundary in every future use; take no checker action.
- C02: Update source mapping with the living-page and fixed-snapshot version rule.
- C03: Record the 16-model, 28-entry reviewed range and refresh intentionally when needed.
- C04: Keep all prompt mappings instruction-level and non-authorship.
- C05: Add user style/request controls only to future evaluation provenance.
- C06: Record adaptive response length as metadata; do not map it to sentence rhythm.
- C07: Record anti-overformatting as negative prompt context; retain current checks and make no compliance or prompt-causality claim.
- C08: Preserve #31's context controls and reject universal list-causality claims.
- C09: Keep correct/requested Markdown distinct from unrequested prose scaffolding.
- C10: Keep emoji handling contextual; add no emote or profanity rule from prompt text.
- C11: Treat warmth as an evaluation control, not a violation.
- C12: Preserve #19's finished-prose boundary and record the post-code question in Sonnet 3.7, Haiku 3.5, and Sonnet 3.5 entries dated 2024-09-09 (both variants) and 2024-07-12; add no bare question-count rule.
- C13: Record the old Sonnet 3.5 offer-to-elaborate, piecemeal-feedback, and dated post-code-question instructions as version-specific positive provenance context.
- C14: Record both exact anti-affirmation families as negative prompt evidence; retain #19/#21 unchanged.
- C15: Keep apology handling in controlled, context-specific evaluation.
- C16: Keep the selected exact directness frames in #56 and `straightforward` in #7's clustering candidates.
- C17: Carry no causal explanation for synonym cycling in the product layer.
- C18: Use metaphor/poetry instructions only as model/date/genre controls.
- C19: Take no product action on internal-mechanics suppression without output evidence.
- C20: Retain #20's finished-prose boundary and use this source only as provenance context.
- C21: Require language-specific evaluation before multilingual transfer.
- C22: Require exact model and prompt date in every prompt-related claim.
- C23: Record both anti-turn-solicitation and older positive continuation instructions, including all named Sonnet 3.5/Sonnet 3.7/Haiku 3.5 post-code-question instances, as version-specific #19 context; do not expand #19 from instructions alone.
- C24: Take no product action on reflective listening; preserve the source's narrow emotional-risk condition.

## Evaluation of approved changes

- C01: not applicable — pending scope-only recommendation.
- C02: not applicable — pending source-mapping recommendation.
- C03: not applicable — pending provenance-only recommendation.
- C04: not applicable — pending evidence-boundary recommendation.
- C05: not applicable — pending evaluation-metadata recommendation.
- C06: not applicable — pending record-only recommendation.
- C07: not applicable — pending counterevidence recommendation; no product change requested.
- C08: not applicable — pending record-only recommendation.
- C09: not applicable — pending no-product-change recommendation.
- C10: not applicable — pending no-product-change recommendation.
- C11: not applicable — pending evaluation-control recommendation.
- C12: not applicable — pending no-product-change recommendation.
- C13: not applicable — pending provenance-context recommendation.
- C14: not applicable — pending source-note recommendation; checker unchanged.
- C15: passed - commit 340ea99 (DR-113) added the apology-led refusal pattern to #19 `no-collaborative-artifacts`; `python3 dev/evals/tests/test_grade.py` passes the DR-113 assertions on 2026-07-17; instruction-level provenance only, no compliance claim.
- C16: passed - DR-134B asserts that `I aim to be direct` and `I need to be clear` fail #56 and that `straightforward` participates in #7 clustering; existing coverage retains the other listed forms.
- C17: passed - commit 64ac03b first reworded #11 so the repetition-penalty explanation read as a proposed but untested mechanism; DR-156 then removed catalogue entry #11 from `human-eyes/scripts/patterns.json` and the regenerated `human-eyes/references/patterns.md` on 2026-07-25, so no causal explanation remains. Documentation-only throughout; no checker change and no mechanism promoted.
- C18: not applicable — pending control-only recommendation.
- C19: not applicable — pending no-product-change recommendation.
- C20: not applicable — pending provenance-context recommendation.
- C21: not applicable — pending evaluation-boundary recommendation.
- C22: not applicable — pending H25/source-mapping recommendation.
- C23: not applicable — pending no-product-change recommendation.
- C24: not applicable — pending no-product-change recommendation.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `rereview_anthropic_sonnet35_once`
- **Reviewer isolation:** fresh source-dedicated agent; one source only; not reused
- **Findings resolved:** Corrected seven full-source review findings: the inventory is 16 model headings; poetry wording belongs to Sonnet 3.7 and Haiku 3.5; C14 now includes all seven 4.x anti-praise entries; C16 includes the newer `genuinely` / `honestly` / `actually` / `straightforward` prohibitions as negative #7/#56 context; C12/C13/C23 include the older positive continuation instructions; C07 is negative instruction context rather than a challenge to current behaviour; and the post-code explanation question is now attributed not only to Sonnet 3.7 and Haiku 3.5 but also to both Sonnet 3.5 variants dated 2024-09-09 and the 2024-07-12 Sonnet 3.5 entry. The snapshot hash remains unchanged because this correction uses the already preserved full text.
- **Unresolved findings:** none
