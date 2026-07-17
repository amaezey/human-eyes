# Gmelius: Can Customers Tell an Email May Have Been Written Using Generative AI?

## Metadata

- **URL:** https://gmelius.com/blog/can-customers-tell-an-email-is-written-using-generative-ai
- **Author / owner:** Anwesha Roy / Gmelius
- **Published:** 2025-07-22
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** vendor email-writing guide and product marketing page
- **Evidence tier:** Vendor, first-party, and practitioner guides
- **Review mode:** update
- **Stable identifier:** Webflow page ID `6737568a4ac417efeb387e46`
- **Version / revision:** page metadata `dateModified` 2025-07-22; prior and current article-body bytes are identical
- **Full-text status:** complete
- **Snapshot:** `snapshots/gmelius-email-ai-isms.md`
- **Extraction method:** direct canonical HTML plus Jina Reader Markdown, verified against canonical HTML with Beautiful Soup
- **Snapshot SHA-256:** `b2e311e46b36141dbc5935fedd26b631d1b6fbf414c3c4229f6dfc4bd086891a`
- **Model / corpus scope:** unspecified versions of generative AI, ChatGPT, Gemini, and Gmelius; English email and customer-communication guidance; no collected corpus, sample, comparison group, prompt set, output lengths, model versions, or validation method reported
- **Access limitations:** none for the complete substantive article body; decorative hero and avatar images, navigation, signup chrome, recommendation cards, footer, and unrelated promotional video assets were omitted because they add no evidence needed to interpret the article

## Summary

This first-party Gmelius guide supplies a 20-item practitioner watchlist for English email, editing advice, two cited numerical claims, and product claims about Gmelius. It reports no collection method, model versions, sample, comparison group, frequency, error rate, or human baseline for the 20 signs. Its useful contribution is bounded email-review vocabulary, especially placeholders, missing personalization, generic subject lines, weak domain grounding, formatting excess, and formulaic greetings. It cannot establish prevalence, causality, model-general behavior, customer detection accuracy, or authorship. The 2026-07-15 source body is byte-identical to the prior 2026-05-05 Jina capture; this update deepens provenance, claim coverage, project comparison, decision states, and independent review rather than recording a substantive page revision.

## Main insights

- The directly reviewable contribution is a vendor-practitioner list, not a measured detection study.
- Empty placeholders, generic subject lines, fake or missing personalization, weak domain grounding, and unsupported jargon fit the project's existing marketing-email review better than a general prose detector.
- The article explicitly supplies important exceptions: a short reply can suit the situation; complex vocabulary is not unique to AI; title case and bold can be appropriate; technical or formal language can be required; and personalization depends on supplied context.
- Several claimed cues are absences, such as no semicolons, no humor, few pronouns, and little white space. The source gives no baseline, threshold, or comparison needed to operationalize them safely.
- The live deterministic layer exactly detects the placeholder example and the page's heavy bolding, but it does not detect the page's formulaic email greetings as #19 or #50, and its corporate-speak check does not cover the source's `optimization` and `efficiency` examples.
- The page repeats product and outcome claims, including lower cost and effort, high returns, exponentially stronger messages, weekly reinforcement, variation across outputs, context-aware automation, prevention of hallucination, trust and effectiveness effects, and one hour saved per day, without methods or direct evidence on this page.

## Evidence and claims to extract

- **Direct source reviewed:** complete canonical Gmelius article carrying page metadata `dateModified` 2025-07-22 and Webflow page ID `6737568a4ac417efeb387e46`, retrieved 2026-07-15 through canonical HTML and Jina Reader Markdown.
- **Method and sample:** the author provides 20 numbered observations, examples, editing suggestions, 10 FAQs, and Gmelius marketing claims. No source-generation method, sampled emails, model/version, prompt protocol, annotation procedure, comparison group, language beyond English, platform beyond email/customer communication, output-length range, uncertainty, or error analysis is reported.
- **Direct versus cited evidence:** C01 and C04-C34 describe the page's own taxonomy, examples, qualifications, advice, marketing assertions, and review inferences. C02 inherits Gartner's 64% customer-service preference result and the article's linked summary of wrong-answer and personalization concerns. C03 inherits a 9.44% versus 8.46% click-through result from an external 2024 experiment. C31 uses the FAQ's unspecified `Research shows` wording and remains indirect and unresolved. Neither linked work was directly ingested in this update.
- **Important limits and counterexamples:** the page does not test whether recipients can identify AI-written email and does not validate any sign. It concedes that short replies may fit, complex words are also human, formatting can be appropriate, prompting and training alter outputs, and targeted AI emails can work. A named byline does not reveal how the article was produced, so the page is not a verified human-authored control. The page itself contains many bold spans and repeated vocabulary but that consistency check is not authorship evidence.

## Skill-use audit

- **Good use:** bounded practitioner support for #39 placeholder residue and the #41 marketing-email prompts for personalization, generic subject lines, domain grounding, jargon, hype, and decorative action lists; adjacent examples for #13, #15, #16/#31a, #31, #35, #43, #50, #52, and #53 when their actual implementation limits remain explicit.
- **Misuse / overclaim:** treating the list as a universal AI taxonomy, a customer-detection result, a document-level classifier, or evidence that an isolated feature establishes AI origin.
- **Unsupported use:** thresholds or severity for short length, commas, semicolon absence, humor, pronoun use, formality, whitespace, greetings, emojis, or any product performance, prevalence, mechanism, causal, cost, trust, hallucination, or time-saving claim.
- **Underused evidence:** the source's own exceptions; the distinction between placeholders as workflow residue and stylistic cues; the exact greeting variants not recognized by #19 or #50; and the need to separate domain-grounding checks from vague corporate vocabulary.
- **Patterns left on the table:** controlled email-specific evaluation of `I hope you are well`, `I hope this email finds you well`, generic birthday subjects, missing recipient history, dense unbroken email paragraphs, and the source's `optimization` and `efficiency` without supporting data. These remain candidates, not promoted rules.

## Matched patterns / rules

- #13 / `no-boldface-overuse`
- #15 / title case in headings, manual only
- #16 and #31a / `no-unicode-flair`
- #25 / `no-staccato-sequences`, only adjacent to short-email advice
- #31 / `no-excessive-lists`
- #35 / agent assessment `tonal_uniformity`
- #39 / `no-placeholder-residue`
- #41 / agent assessment `genre_specific`, marketing-email branch
- #43 / `no-corporate-ai-speak`, only partial lexical overlap
- #50 / `no-formulaic-openers`, not the article's greeting examples
- #52 / `sentence-length-variance`, not a long-sentence or comma check
- #53 / `vocabulary-diversity`
- Agent assessments `semantic_redundancy` and `even_jargon_distribution`
- Closed-source and source-grounding constraints in `human-eyes/references/process.md`

## Associated hypotheses

- H9, field-guide voice with similar-species disambiguation per pattern
- H12, genre-aware threshold calibration
- H13, sentence-length mean as a register-aware research candidate, adjacent only
- H24, register-specific vocabulary density
- H25, model-family versus generic-AI residue

## Questions / follow-up

- Directly ingest the linked Gartner release or click-through experiment only if their bounded findings will support a project or guidance decision.
- Evaluate uncovered email greetings, subject lines, personalization failures, and dense paragraphing only with rights-cleared, matched human and generated email samples.
- Retain the root README's existing `email-domain example` wording for #19 and #50; it is already adjacent-context wording rather than a claim of exact regex coverage.
- No source-access blocker remains.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none recorded; archived by verified hash | `snapshots/archive/gmelius-email-ai-isms/2026-05-05-00dd9560.md` | 2026-05-05 | `00dd956099b857e2b41a3673d9d9914ae49f48cd86f4c323ad99f2c0269e1bdf` |
| current | Webflow page ID `6737568a4ac417efeb387e46` | `snapshots/gmelius-email-ai-isms.md` | 2026-07-15 | `b2e311e46b36141dbc5935fedd26b631d1b6fbf414c3c4229f6dfc4bd086891a` |

The prior card and manifest recorded no snapshot digest. Before archiving, the previous snapshot's 15,056 bytes were hashed as `00dd956099b857e2b41a3673d9d9914ae49f48cd86f4c323ad99f2c0269e1bdf`; the archive copy has the same recomputed hash. A fresh 2026-07-15 Jina retrieval had the same 15,056 bytes and digest. The current snapshot adds contract-compliant provenance and extraction verification around that unchanged complete body. Canonical HTML independently confirmed the author, publication and modification date, 20 numbered signs, all following article sections, and all 10 FAQs.

## Decision history

- The previous unstructured mappings to #13, #15, #16/#31a, #19, #31, #39, #41, #43, #50, and H12 recorded no user decision or implementation status. They are superseded by C01-C34 below.
- The prior #19 and #50 mappings are narrowed analytically: neither `no-collaborative-artifacts` nor `no-formulaic-openers` detects the article's `I hope you are well` or `I hope this email finds you well` examples. The root README already calls Gmelius an `email-domain example`, so no root-index wording change is required.
- No previous recommendation was approved or implemented. The source body is unchanged, and all current recommendations remain `pending` and `not started`.

## Project coverage

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: The page presents 20 signs that an email may have been written by generative AI. | Direct vendor-practitioner taxonomy; no collection method, sample, model/version, comparison, frequency, validation, or error rate. | #41 `genre_specific` supplies an email watchlist; partly covered. | The live watchlist covers only a subset and cannot validate the taxonomy or infer origin. | Record the 20-item list as bounded email-review guidance only; verify through source-card validation and independent review. | pending | not started |
| C02: Gmelius cites Gartner's result that 64% of customers would prefer companies not use AI for customer service and says customers fear wrong answers and reduced personalization. | Indirect cited preference and concern summary about customer service, not detection of AI-written email; linked source not directly reviewed here. | No directly ingested Gartner card or project check; not covered. | Population, questionnaire, sampling, exact support for the two concerns, and relationship to email prose cues remain outside this review. | Keep indirect and non-promoted; ingest Gartner separately before any product use. | pending | not started |
| C03: Gmelius cites a 2024 experiment reporting 9.44% click-through for AI email versus 8.46% for from-scratch email. | Indirect cited performance result; no design, sample, uncertainty, content, model, or statistical comparison reviewed here. | No directly ingested experiment card or project check; not covered. | A one-point observed difference does not establish superiority or explain prose features. | Keep indirect and non-promoted; require direct review before any performance conclusion. | pending | not started |
| C04: The page says tools such as ChatGPT and Gemini predict word sequences from large text databases. | Direct high-level mechanism description; not evidence for any listed surface sign. | `human-eyes/SKILL.md`, `Keep the product boundary`, requires construction-level findings and forbids provenance inference; fully covered as a scope limit. | Model architecture, training data, and versions are unspecified. | Record as framing only; do not use it to justify a pattern or causal claim. | pending | not started |
| C05: The conclusion says customers can mostly tell and models carry signatures or telltale signs. | Direct author conclusion; the page runs no customer-identification study and validates no signature. | `human-eyes/SKILL.md`, `Keep the product boundary`, says the skill never classifies authorship or assigns provenance; fully covered as a rejected inference. | No accuracy, baseline, prevalence, false-positive, or document-level evidence. | Do not promote the `mostly yes`, signature, or authorship inference. | pending | not started |
| C06: Very short one-line replies can look generic, but the page says the example may be suitable in some scenarios. | Direct practitioner observation plus explicit counterexample; no length threshold or comparison. | #25 staccato and #52 sentence variance are adjacent; partly covered. The source-page surface run cleared #25 and reported sentence-length SD 10.9. | Neither check evaluates one-line email appropriateness, and short replies are normal in many email tasks. | Keep as task-conditional email review only; add no length rule from this source. | pending | not started |
| C07: Missing previous-conversation or recipient details makes email less personalized. | Direct practitioner advice; no measured outcome or AI-human comparison. | #41 marketing-email watchlist names generic subject lines or fake personalization; fully covered as manual review. | Live guidance cannot know recipient history without task context. | Retain in #41 only when the source materials include recipient context; never invent personalization. | pending | not started |
| C08: Unedited placeholders such as `Hi! I'm excited to learn more about {company name}` are workflow residue. | Direct example; strongest concrete item because the residue is observable without an authorship inference. | #39 `no-placeholder-residue` exactly detects `{company name}`; fully covered. The source-page surface run found both occurrences. | `check_placeholder_residue` in `human-eyes/scripts/grade.py` is not quote-aware, so quoted examples still trigger the surface layer. | Keep #39. If Mae approves quote-context work, add quoted and live placeholder fixtures to `dev/evals/tests/test_grade.py`, then run `python3 dev/evals/tests/test_grade.py`. | pending | not started |
| C09: AI assistants may add excessive bulleted or numbered lists where prose would fit. | Direct practitioner observation; no count, rate, or genre baseline. | #31 `no-excessive-lists` checks at least 8 items across 2 blocks or a 30% line ratio and preserves legitimate discrete lists; partly covered. The source page itself cleared with 0 list-item lines. | Source gives no operational threshold and its numbered taxonomy is a legitimate list structure rendered as headings. | Keep contextual listification review; add no new threshold. | pending | not started |
| C10: AI email may produce 30-to-50-word sentences joined by commas. | Direct claim and one constructed example; no sample, rate, human comparison, or evidence that comma joining caused the result. | #52 measures sentence-length variance, not long-sentence mean, maximum, clause count, or commas; not covered. The page's overall SD was 10.9 and cleared #52. | No long-sentence or comma-splice implementation, register baseline, or length evidence. | Do not add a comma or length rule; evaluate with matched email controls first. | pending | not started |
| C11: AI agents tend not to use colons and semicolons in ordinary sentences. | Direct categorical absence claim; no counts, models, prompts, periods, genres, or human comparison. | No exact check; not covered. | Absence requires sufficient text length and a baseline, and the claim conflicts with model and prompt variability. | Take no product action; require comparative corpus evidence. | pending | not started |
| C12: Generative AI lacks humor unless prompted, while humans should add humor. | Direct craft assertion with a prompt qualification; no humor definition, quality measure, or comparison. | #35 `tonal_uniformity` can review register drift; partly covered. | The project has no humor requirement, and humor can be inappropriate or supplied by the source. | Keep humor task-conditional and source-grounded; never require or invent it. | pending | not started |
| C13: Title case is frequent in AI-generated headings and should be checked for appropriateness. | Direct practitioner observation; no rate or comparison. | #15 title-case heading guidance is manual and house-style conditional; fully covered as style review. | No programmatic title-case check and no reason to treat appropriate title case as origin evidence. | Retain manual house-style review only. | pending | not started |
| C14: AI may overuse bold on arbitrary phrases. | Direct practitioner observation; no rate or comparison. | #13 `no-boldface-overuse` flags 4 or more non-list, non-heading bold spans; fully covered for the named surface. The source page itself produced 18 spans and a flagged result. | The source gives no threshold, and some emphasis is legitimate. | Keep #13 with its contextual threshold and definition-header exception; add no severity change. | pending | not started |
| C15: AI may repeat words and phrases to lengthen or sound polite, reducing engagement. | Direct mechanism and outcome assertions without comparison or measurement. | #53 `vocabulary-diversity`, agent assessment `semantic_redundancy`, #51 `no-anaphora`, and #35b `no-this-chains` cover parts; partly covered. The page's type-token ratio was 0.351 and flagged #53. | Existing checks do not establish motive, politeness, engagement effect, or AI origin. | Use repetition only as a coarse writing-quality signal; do not adopt the mechanism or outcome claim. | pending | not started |
| C16: Business-training data leads models to unsupported jargon such as `optimization` and `efficiency`. | Direct causal and lexical claim; training corpus, rate, and comparison are unspecified. | #41 names unsupported jargon; `even_jargon_distribution` and #43 `no-corporate-ai-speak` are adjacent; partly covered. The page cleared #43 and vocabulary clustering, showing the exact examples are not live regex terms. | No evidence for the training-data cause, and the exact two words can be necessary domain language. | Keep as contextual #41 review only; test support and distribution, not isolated words. | pending | not started |
| C17: Human email uses first- and second-person pronouns more often; AI uses little, while second person can become salesy. | Direct directional claim plus qualification; no counts, text length, genre split, or comparison. | No exact pronoun-density check; not covered. | The two claims pull in different directions and depend on task, audience, and email role. | Take no product action; require matched email evidence and task controls. | pending | not started |
| C18: Generative AI's positive default can become overexcited hyperbole. | Direct tone claim; no model/version, prompt, rate, or human comparison. | #4 promotional language and #41 exaggerated-transformation review cover parts; partly covered. | Positivity, excitement, and hyperbole are distinct, and the source supplies no threshold or outcome evidence. | Keep as manual register-fit review; do not infer model origin. | pending | not started |
| C19: AI subject-line generators can return generic lines such as `Birthday Greetings` rather than a tailored alternative. | Direct constructed example and practitioner advice; no sampled outputs or outcome comparison. | #41 marketing-email watchlist exactly names generic subject lines; fully covered manually. | No deterministic subject-line context or test corpus exists. | Retain #41 and evaluate subject lines only when the task identifies the subject field and recipient context. | pending | not started |
| C20: Generic email can reflect missing industry, demographic, or department context, with prompting or training offered as the qualification. | Direct practitioner observation and explicit context qualification; no measured model comparison. | #41 `genre_specific` names weak domain understanding; `human-eyes/SKILL.md`, `Produce new writing`, and `human-eyes/references/process.md`, `Preserve meaning`, require brief-traceable facts and forbid invented details; fully covered in principle. | The live agent needs the task's domain sources and must not manufacture details. | Keep source-grounded domain review; never treat missing undisclosed context as authorship evidence. | pending | not started |
| C21: Difficult words such as `meticulous` and `pivotal` may appear where simpler words work, but the page says this is not unique to AI and matters especially when repeated. | Direct examples plus explicit human look-alike and frequency qualification; no measured rate. | #7 vocabulary clustering contains both words and uses density rather than one-word proof; partly covered. | Register and meaning can require either word; the page supplies no threshold. | Preserve the human-use and repetition qualifications; add no isolated-word rule. | pending | not started |
| C22: AI email can be overly formal or cold unless trained or instructed. | Direct register claim with prompt/training qualification and an unsupported business-data causal explanation. | #35 `tonal_uniformity` and #41 genre review are adjacent; partly covered. | The live #35 item evaluates uniformity, not formality itself, and formal email can be correct. | Treat as audience and brief fit only; reject the causal and model-general claims. | pending | not started |
| C23: Dense long paragraphs without white space can look synthetic in email. | Direct layout observation; no paragraph counts, lengths, viewport, device, comparison, or outcome. | `paragraph-length-uniformity` measures similarity across at least 7 substantial paragraphs, not density or white space; not covered. The page cleared at CV 0.27 across 47 paragraphs. | No email-density metric or rendering context exists. | Keep as manual readability guidance; require device- and genre-aware evidence before implementation. | pending | not started |
| C24: Formulaic greetings include `I hope you are well` and `I hope this email finds you well`. | Direct exact examples; no frequency or comparison. | #41 covers over-warm openings; partly covered. The source-page run cleared #19 `no-collaborative-artifacts` and #50 `no-formulaic-openers`; neither regex contains these greetings. | Exact deterministic coverage is absent, but the root README already labels Gmelius only as an email-domain example. | Keep the current adjacent #41/#19/#50 source mappings unchanged; evaluate greetings with human email controls before any regex. | pending | not started |
| C25: AI may overuse or misplace rocket, fire, and alert emojis in email. | Direct practitioner examples; no rate, rendering, audience, or comparison. | #16/#31a `no-unicode-flair` covers emoji glyphs and shortcodes with a 2-candidate threshold; fully covered for the surface, context still required. | The source gives no threshold and emoji use can be deliberate or audience-appropriate. | Keep the existing contextual check and UI, quoted-source, checklist, and genre exceptions. | pending | not started |
| C26: Supplying desired structure, customer history, phrasing, formality, preferred structure, and other context can reduce generic paragraphing and help an email reflect the user's tone. | Direct workflow and tone-training advice; no before-and-after outputs or evaluation. | #41 `genre_specific` and `human-eyes/references/process.md`, `Preserve meaning`, require genre fit and source-grounded detail; fully covered in principle. | No measured improvement and no permission to invent missing customer context, preferences, or voice examples. | Retain only as closed-source prompting guidance; verify all added specifics against supplied material. | pending | not started |
| C27: Reusing a prompt causes monotonous outputs, while small prompt changes help the model keep learning. | Direct causal and mechanism claim; no experiment, model behavior evidence, or distinction between in-context variation and model training. | No exact project evidence; not covered. | Repeated inference does not by itself train most deployed models, so `keep learning` is unsupported here. | Do not promote the mechanism; treat prompt variation as unvalidated workflow advice only. | pending | not started |
| C28: Gmelius learns a user's voice from thousands of sent emails and weekly reinforcement, trains from websites, help centers, and wikis, continuously adapts, and encourages variation in phrasing, tone, and formatting. | Direct first-party product claims; no technical documentation, evaluation, privacy detail, sample, or version on this page. | No exact project implementation or source; not covered. | This source cannot verify training behavior, adaptation quality, output variation, or voice fidelity. | Record as product marketing only; take no human-eyes product action. | pending | not started |
| C29: Gmelius distinguishes reply-worthy messages, leaves notes when context is insufficient, avoids hallucination, and guarantees no generic or out-of-context email; the FAQ adds that generic tools can hallucinate, damage trust, and reduce effectiveness. | Direct first-party workflow, risk, and outcome claims; no error analysis or evaluation. | #41 `genre_specific` names domain context and `human-eyes/references/process.md`, `Preserve meaning`, requires brief-traceable claims; partly covered as a principle only, not product evidence. | `Avoids` and `guarantees` are categorical, and the trust and effectiveness harms are unsupported by results on this page. | Preserve only the abstention and source-grounding principles; do not promote the product-performance, trust, or effectiveness claims. | pending | not started |
| C30: The page says AI email costs and takes a fraction of traditional effort, can return highly, can save hours, can become exponentially more powerful without losing efficiency, and Gmelius saves one hour every day. | Direct marketing efficiency and outcome claims; no study, sample, task mix, baseline, statistic, or citation for these assertions. | No project evidence; not covered. | The cost, return, power, efficiency-preservation, hours-saved, and one-hour claims are unsupported on the page. | Take no product or guidance action on any efficiency or outcome claim. | pending | not started |
| C31: The FAQ says research shows customers notice tone, personalization, structure, and other cues that reveal generated content. | Direct wording but unspecified research; the only linked Gartner item concerns service preference rather than cue-based email identification. | `human-eyes/SKILL.md`, `Keep the product boundary`, forbids proof-of-authorship and provenance claims; fully covered as a caution against promotion. | No cited cue-identification study, stimuli, participant rationale, accuracy, or false-positive evidence. | Do not promote this as research-backed detection evidence. | pending | not started |
| C32: The FAQ recommends full automation only when context-aware and says generated email can be effective when targeted and personalized. | Direct prescriptive qualification plus product self-endorsement; no independent outcome evaluation. | #41 and process source-grounding rules support the context requirement; partly covered. | `Only if` is categorical, and the page does not establish safe automation conditions or effectiveness. | Retain context and human-proofreading cautions only; take no automation-policy action. | pending | not started |
| C33: Within the selected checks used for C06, C08-C10, C14-C16, and C23-C25 coverage mapping, a focused surface-only run flagged the placeholder examples, 18 bold spans, and low vocabulary diversity, while clearing collaborative artifacts, excessive lists, Unicode flair, formulaic openers, corporate AI-speak, staccato, sentence variance, and paragraph uniformity. | Reproducible reviewer measurement of selected mapped checks, not a complete result inventory or source-authorship finding. | The live deterministic layer provides exact selected-check coverage evidence; fully covered for those mappings. | The same run has additional findings outside this source-card mapping, quoted placeholders are not context-suppressed, and surface output is not a complete Audit. The page's production method is unknown. | Record these selected results only as implementation mapping and false-positive/context evidence; preserve the complete JSON in `tmp/gmelius-email-ai-isms/surface.json` and do not use it as authorship evidence. | pending | not started |
| C34: The page is product marketing with a named byline, but it does not disclose the article's production process. | Direct provenance observation; authorship workflow is unspecified. | `sources/README.md`, `Vendor, first-party, and practitioner guides`, supplies the evidence tier, while `human-eyes/SKILL.md`, `Keep the product boundary`, forbids authorship inference; fully covered. | A byline cannot make the page a verified human control or validate the signs. | Preserve the vendor tier and unknown-production limitation in every reuse. | pending | not started |

## Recommendations

- C01: Record the complete taxonomy as bounded email-review guidance only.
- C02: Keep the Gartner preference and concern summary indirect and non-promoted until separately ingested.
- C03: Keep the click-through result indirect and non-promoted until separately ingested.
- C04: Use the model-mechanism sentence as framing only.
- C05: Reject the `mostly yes`, signature, and authorship inference.
- C06: Keep short replies task-conditional and add no length rule.
- C07: Retain personalization review only when recipient context is supplied.
- C08: Keep #39; if quote-context work is approved, add quoted/live fixtures to `test_grade.py` and run that test file.
- C09: Keep contextual listification review and its existing thresholds.
- C10: Add no comma or long-sentence rule without matched evidence.
- C11: Take no action on semicolon or colon absence.
- C12: Keep humor task-conditional and source-grounded.
- C13: Retain manual, house-style-specific title-case review only.
- C14: Keep #13 with its current threshold and legitimate-emphasis exception.
- C15: Use repetition only as a coarse quality signal, not motive or origin evidence.
- C16: Keep jargon review contextual; do not blacklist `optimization` or `efficiency`.
- C17: Add no pronoun-density rule without matched email evidence.
- C18: Keep excitement and hyperbole as manual register-fit review.
- C19: Retain the #41 subject-line prompt with field and recipient context.
- C20: Keep domain review source-grounded and non-provenance-based.
- C21: Preserve human-use, context, and repetition qualifications for vocabulary.
- C22: Treat formality as audience fit, not an AI cue by itself.
- C23: Keep dense paragraphing as manual readability guidance only.
- C24: Keep current adjacent source mappings unchanged and evaluate greetings before any regex.
- C25: Keep the contextual emoji check and its exceptions.
- C26: Retain only closed-source structure, context, and tone-example prompting guidance.
- C27: Do not promote the unsupported prompt-reuse learning mechanism.
- C28: Record product training, adaptation, and variation claims as marketing only.
- C29: Preserve abstention and source-grounding principles but not product guarantees or trust/effectiveness claims.
- C30: Take no action on unsupported cost, return, power, efficiency, or time-saving claims.
- C31: Do not describe email-cue identification as research-backed from this page.
- C32: Retain context and proofreading cautions only; add no automation policy.
- C33: Preserve the focused run as mapping evidence, never authorship evidence.
- C34: Keep the vendor tier and unknown-production limitation attached to reuse.

## Evaluation of approved changes

- C01-C34: not applicable - all recommendations remain pending; no checker, registry, test, hypothesis, guidance, or product implementation was authorized.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/gmelius_reviewer_4`
- **Reviewer isolation:** fresh source-dedicated agent; one source only; not reused
- **Findings resolved:** reviewer `/root/gmelius_reviewer_1` returned five findings, corrected for completeness, exact project artifacts, decision specificity, stable-identifier consistency, and heading counts; reviewer `/root/gmelius_reviewer_2` returned one provenance finding, corrected by distinguishing the newly computed pre-archive digest from a previously recorded digest; reviewer `/root/gmelius_reviewer_3` returned one focused-run completeness finding, corrected by explicitly limiting C33 to the selected mapped checks and preserving the complete JSON result; reviewer `/root/gmelius_reviewer_4` found no residual issues
- **Unresolved findings:** none
