# Jonathan Bailey: Em Dashes, Hyphens and Spotting AI Writing

## Metadata

- **URL:** https://www.plagiarismtoday.com/2025/06/26/em-dashes-hyphens-and-spotting-ai-writing/
- **Author / owner:** Jonathan Bailey
- **Published:** 2025-06-26
- **Retrieved:** 2026-05-05
- **Extracted:** 2026-05-05
- **Contract updated:** 2026-07-15; the preserved extraction was brought into the source-ingest contract without a fresh article scrape
- **Source type:** practitioner journalism and plagiarism commentary
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** article as published 2025-06-26 and captured 2026-05-05; previous record was the same preserved article body before source-ingest contract framing
- **Full-text status:** complete
- **Snapshot:** `snapshots/bailey-em-dash-hyphens.md`
- **Extraction method:** preserved Jina Reader URL-to-Markdown extraction; no fresh scrape
- **Snapshot SHA-256:** `60125940ad10b7fc73e9dc51f1fb1fe1aa13dd6cebe7016ee34aabafcf17b5e8`
- **Model / corpus scope:** one output from each of six free or basic services, named ChatGPT, Microsoft Copilot, DeepSeek, Claude, Gemini, and Meta.ai, generated before the article's 2025-06-26 publication from one English journalism prompt about the H3H3 lawsuit; reported lengths range from 261 to 948 words; exact model versions, dates, settings, sessions, temperatures, repetitions, and human comparison texts are not supplied
- **Access limitations:** none for the preserved article body; the linked Google Doc containing the six raw generated articles was not preserved or reviewed, the generic hero image was not saved, and the article supplies no model build identifiers, repeated trials, human comparison corpus, annotation protocol, statistical test, or reproducible record of the factual-error verification

## Summary

Bailey reports a one-prompt, six-service spot check of em-dash use, then uses the sharply different output counts to reject em dashes as a standalone authorship shortcut. The article's strongest contribution is its own limitation case: three services reportedly used eight or nine em dashes, one used two, and two used none; humans also use the punctuation deliberately; the glyph is easy to replace; and the model-specific pattern can drift. Bailey found concrete factual mistakes more useful than punctuation, but the linked raw outputs were not preserved, so the counts and error examples remain author-reported practitioner observations rather than independently reproducible evidence. The article supports a deeper-review cue and product restraint, not a threshold, hard failure, generic model claim, or authorship verdict.

## Main insights

- The six reported outputs vary from zero to nine em dashes despite one shared prompt, directly challenging a generic claim that every AI-generated text contains them.
- Bailey explicitly says the sample is far too small for statistical significance, reports no human comparison, and names only free or basic product surfaces rather than model versions.
- Bailey says Claude's two em-dash glyphs occurred in one highlighted section, but that clustering detail remains author-reported and cannot be checked without the linked raw output.
- Human writers use em and en dashes, sometimes as a long-standing personal style; Bailey therefore rejects the absence or presence of one glyph as proof.
- Replacing em dashes with hyphens is trivial, while services and users can adapt, so a public surface cue can decay quickly.
- The phrase "ChatGPT hyphen" conflates a hyphen with the em dash under discussion. Bailey's rhetorical questions about hyphens and parentheses do not establish either as an AI pattern.
- Bailey's three factual-error examples point toward source and claim verification, but they are not independently reproducible from the preserved record because the linked model outputs were not captured.
- Bailey parenthetically relays a linked allegation that DeepSeek is "based on ChatGPT." This article does not establish that lineage or show that it explains DeepSeek's dash count, so the allegation remains indirect, unresolved, and non-promoted.
- The article's statement that eight or nine em dashes are beyond what almost any human would use is an unsupported interpretation that sits uneasily with its own account of heavy human use and lacks a human baseline.

## Evidence and claims to extract

- **Direct source reviewed:** Complete preserved article titled "Em Dashes, Hyphens and Spotting AI Writing," including the punctuation background, six-system test and counts, limitation discussion, bottom line, three factual-error examples, inline links, and reuse footer, retrieved 2026-05-05.
- **Method and sample:** One unconstrained prompt, "Write an article about the H3H3 lawsuit against reaction streamers," was submitted to six free or basic AI services. Bailey reports one output per service, word counts, em-dash counts, and en-dash counts for two outputs. No repetition, randomisation, model version, generation date, decoding settings, blinded coding, human control, or inferential analysis is reported.
- **Direct versus cited evidence:** C05-C07 and C12 are direct author-reported observations from Bailey's own test, although the raw outputs needed to reproduce them are not preserved. C01, C08-C11, C13, and C15 are Bailey's interpretations or conclusions. C02-C04 and C09 draw partly on linked public comments, dictionaries, style guides, and earlier Plagiarism Today articles rather than evidence generated in this article. C17 is Bailey's indirect relay of a linked Gizmodo allegation about DeepSeek and ChatGPT; the linked source was not reviewed in this work unit. C14 identifies an internal overreach in Bailey's interpretation. C16 is this review's provenance assessment, not a source claim.
- **Important limits and counterexamples:** One output per service cannot establish prevalence or a threshold. Product names are not model versions. Bailey reports that Claude's two em dashes occurred in one highlighted section, but the missing raw output prevents verification of that clustering qualification. Gemini and Meta.ai are direct counterexamples to any universal em-dash claim in this sample, while deliberate and habitual human use is an explicit false-positive case. Easy substitution creates evasion and drift. The raw model text and factual checks were not preserved, so the reported counts and errors are attributable to Bailey but cannot be independently recomputed here. The linked DeepSeek-lineage allegation is also unresolved and cannot explain the observed counts.

## Skill-use audit

- **Good use:** Use the article as dated practitioner evidence that em-dash behaviour differs by service, that humans are strong look-alikes, that the cue is easy to evade, and that factual verification can justify deeper review more concretely than punctuation alone.
- **Misuse / overclaim:** Do not cite it to prove authorship, describe em dashes as a universal AI feature, set a density or any-occurrence threshold, infer a model family, or claim that factual errors themselves prove AI use.
- **Unsupported use:** Do not promote the article's "most humans use hyphens" assertion, its "beyond what any human would likely do" interpretation, the "ChatGPT hyphen" nickname, generic hyphen or parenthesis suspicion, a prediction that the cue will fail within a specified number of months, or the linked allegation about DeepSeek as an established model-lineage fact or explanation for its punctuation.
- **Underused evidence:** Root documentation already gives Bailey a small-test, explicit-limits mapping, but live #49 still treats any unsuppressed U+2014 occurrence as a strong warning. The article's model variation, human-style counterexample, easy substitution, and no-certainty conclusion argue for matched calibration rather than stronger rule language.
- **Patterns left on the table:** No new surface pattern is justified. The useful open work is a dated model/version evidence convention, deliberate-use and genre controls for #49, explicit separation of em dashes from en dashes and hyphens, and factual/source verification that remains a manual non-authorship review.

## Matched patterns / rules

- #49 `no-em-dashes`; root pattern table row 49; catalogue em-dash tolerance note; focused `grade.ALL_CHECKS["no-em-dashes"]` results
- #18 `no-compound-modifier-density` only as a distinct hyphenated-modifier check, not coverage of Bailey's rhetorical question about generic hyphen substitution
- #41 `genre_specific` journalism and academic source-verification branches
- Product boundary in root `README.md` and `human-eyes/references/process.md`: pattern review does not infer authorship
- H7 advisory catalogue, H9 similar-species disambiguation, H12 genre-aware threshold calibration, and H25 model-family versus generic-AI residue
- `pattern-opportunities.md` mappings for source-grounding, deliberate punctuation, and source date/model metadata

## Associated hypotheses

- H7: Five-check gating grader plus advisory catalogue
- H9: Field-guide voice with similar-species disambiguation per pattern
- H12: Genre-aware threshold calibration
- H25: Model-family versus generic-AI residue

## Questions / follow-up

- The fresh final independent source-record reviewer passed the remediated record with no unresolved findings.
- If the linked Google Doc becomes available later, preserve it separately and recompute the six word, em-dash, and en-dash counts before treating them as reproducible examples or fixtures.
- If DeepSeek lineage ever becomes relevant to a project decision, ingest the linked account separately and seek direct primary evidence; Bailey's parenthetical allegation is not decision-ready evidence.
- If #49 is reconsidered, use matched human and generated prose across model versions and genres, retain deliberate punctuation controls, and report candidate recognition separately from threshold firing.
- Recommendation decisions remain pending; no product files or checks were changed in this update.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none found; preserved 2026-05-05 Jina Reader extraction | `snapshots/archive/bailey-em-dash-hyphens/2026-05-05-a9ec56d41ccd.md` | 2026-05-05 | `a9ec56d41ccde9200984a22b6a47e8b7d8a48ffab5318c50afa4ace8c855d68e` |
| current | none found | `snapshots/bailey-em-dash-hyphens.md` | 2026-05-05 | `60125940ad10b7fc73e9dc51f1fb1fe1aa13dd6cebe7016ee34aabafcf17b5e8` |

The article body is unchanged except for removal of one trailing space. The current snapshot adds the required provenance, scope, extraction-verification, omission, and attachment fields around the preserved text. The prior compact card was expanded into a complete claim inventory and live-project comparison.

## Decision history

- The previous card predated stable claim IDs and decision or implementation fields. It recorded no user-approved recommendation and no source-specific implementation.
- The old card mapped the source to #49 and factual-error review. Those useful mappings remain, but the current review narrows #49 to dated small-sample context and makes clear that #41 source verification does not establish authorship.
- C01-C17 are newly assigned stable IDs for the unchanged preserved article and therefore begin at `pending` / `not started`.
- C07, C09, and C14 decided 2026-07-17: #49 remains fail-on-any (deliberate stance). The proposed density/threshold reconsideration is closed with no product change; this does not promote Bailey's human-ceiling claim or small-sample counts as severity evidence.

## Project coverage

This is the authoritative review table. Focused deterministic results are live surface-function checks, not a complete human-eyes Audit. The six raw generated outputs were unavailable, so the reported model counts were not rerun.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Detection efforts have varied results, scanning everything is impractical, and distinguishing AI polishing from AI writing is difficult. | Bailey's interpretive framing supported only by links to three earlier Plagiarism Today articles; no detector experiment or mixed-authorship analysis is supplied here. | **fully covered:** root `README.md` distinguishes pattern auditing from commercial authorship detection, and `references/process.md` limits reports to prose findings rather than authorship. | This article cannot quantify detector performance or define a polishing boundary. | Record as practitioner rationale for the existing non-authorship boundary; take no product action. | pending | not started |
| C02: A public shortcut claims AI commonly uses em dashes while humans are less likely to, sometimes calling the glyph a "ChatGPT hyphen." | Reported commenter and linked social-media claim; no sample, counts, human baseline, or terminology validation. The nickname confuses an em dash with a hyphen. | **partly covered:** #49 names em dashes as a review signal, while root row 49 already says legitimate human punctuation cannot prove authorship. | The public prevalence claim and nickname are not evidence for severity or a threshold. | Keep only as provenance for a public tell; explicitly do not promote the nickname or prevalence claim. | pending | not started |
| C03: Em dashes, en dashes, and hyphens are distinct; em dashes can mark a change in direction or parenthetical interruption; major human style guides license dash use, generally sparingly. | Definitions and usage are inherited from linked Merriam-Webster, AP, Chicago, APA, and MLA pages; Bailey supplies no original usage study. | **partly covered:** #49 targets only U+2014 and documents legitimate deliberate use; #18 separately targets clustered stock hyphenated modifiers. The project has no generic en-dash or hyphen punctuation check. | The current catalogue does not need a general punctuation lesson, and this cited material does not validate authorship inference. | Record the distinctions and human-use counterexample; take no new check or severity action. | pending | not started |
| C04: Because keyboards lack a dedicated em-dash key, most humans use hyphens rather than em or en dashes. | Direct author assertion and causal inference; no keyboard study, input-method survey, platform scope, or human corpus. Autocorrect and typography workflows are only mentioned, not measured. | **not covered:** the project does not treat input convenience as authorship evidence, appropriately. #18 is about compound modifiers, not dash substitution. | The asserted human frequency and causal explanation are unsupported and platform-dependent. | Do not promote this assertion into pattern evidence, examples, or explanation text. | pending | not started |
| C05: Bailey tested one output from each of six free or basic services using the same broad English journalism prompt to encourage unconstrained writing. | Directly reported method; one output per product, no versions, dates, settings, repetitions, randomisation, blind coding, or human control. The raw-output link was not preserved. | **partly covered:** source metadata conventions and H25 require model, version, date, genre, and sample scope; this card now records the available product, prompt, tier, genre, language, and one-output design. | Missing build identifiers and raw outputs prevent reproduction or model-family attribution. | Retain as dated practitioner context only; require raw outputs and exact model metadata before using the test as a fixture. | pending | not started |
| C06: Reported results were ChatGPT 573 words and 8 em dashes; Copilot 466 and 8; DeepSeek 555 and 9 plus 4 en dashes; Claude 948 and 2 plus 1 en dash, with its two em dashes occurring in one highlighted section; Gemini 499 and 0; Meta.ai 261 and 0. | Direct author-reported observations from one output per service, including Bailey's qualification about the two Claude glyphs being confined to one highlighted section. No raw outputs are preserved here, so neither counts nor within-output clustering can be recomputed; no denominator-normalised comparison or uncertainty is provided. | **partly covered:** live #49 recognises any U+2014 candidate, while a focused check confirmed one synthetic em dash fails and en dash or hyphen variants pass. If the raw outputs match the report, #49 would recognise the named em-dash glyphs but would not verify Bailey's counts, the Claude clustering qualification, or his interpretation. | The live check is occurrence-based and product-agnostic; the source results and the one-section Claude qualification are unverified, unequal-length, one-shot product observations. | Record the six counts and Bailey's Claude clustering qualification with their limits; do not import them as thresholds, prevalence claims, clustering evidence, or committed fixtures until the linked outputs are preserved and checked. | pending | not started |
| C07: The sample is far too small for statistical significance, and the zero-count Gemini and Meta.ai outputs show that not all AI-generated works contain em dashes. | Direct author qualification and direct within-test counterexamples; one output per product cannot estimate absence rates. | **challenges current behaviour:** root row 49 describes frequent default em dashes only as a cue and H25 tracks model-specific residue, but live #49 still fails any unsuppressed U+2014 as a `strong_warning`. | Generic strong-signal language can absorb a service-specific, date-specific result while missing zero-dash AI output entirely. | Add Bailey only to the existing #49 calibration question; evaluate model, version, date, genre, frequency, and zero-dash counterexamples before retaining or changing severity. | rejected | not applicable |
| C08: Em-dash detection is easy to game because services may omit the glyph and a user can replace it with hyphens automatically; public tells and goalposts will move. | Direct author argument based on simple substitution and the observed cross-service variation; no evasion experiment or longitudinal evidence. | **partly covered:** H25 and root source notes recognise model/version drift; the product does not claim adversarial robustness. Live #49 ignores en dashes and hyphens, as the focused check confirmed. | No active output explains cue decay or separates unedited from substituted text; the article cannot quantify when or how quickly the cue changes. | Record evasion and drift as interpretation limits; do not expand detection to replacement punctuation without direct matched evidence. | pending | not started |
| C09: Humans use em and en dashes, sometimes heavily as a long-standing personal style, so dash-laden prose is not guaranteed to be AI-written. | Direct human-look-alike claim supported by Bailey's own style analogy and linked style guides, not by a measured human corpus. | **challenges current behaviour:** #49's catalogue tolerance note and root row acknowledge legitimate use. The live check suppresses candidates in high-confidence formal-report and screenplay-style contexts, but the focused checks show one ordinary U+2014 fails while a formal-report example with two is suppressed. | The any-occurrence rule and `strong_warning` framing can still flag deliberate human prose outside the narrow inferred contexts. | Preserve the human look-alike and evaluate any-occurrence versus density behaviour on matched human prose before changing #49; do not treat stylistic use as provenance. | rejected | not applicable |
| C10: Many em dashes can be a clue that deeper analysis is needed, but they are not a gold standard and cannot be much more than a clue. | Bailey's cautious interpretation of his six-output spot check; no validated threshold, human comparison, or outcome measure. | **partly covered:** root row 49 already calls frequent default use a review cue and rejects authorship proof. Live #49 nevertheless labels any unsuppressed occurrence a strong warning and Balanced or All actions require change. | User-facing severity and action behaviour are stronger than the source's qualified conclusion, while this source cannot supply a replacement threshold. | Keep the source as caution and deeper-review context; require matched evaluation and deliberate-use controls before any product change. | pending | not started |
| C11: No single clue, detector, formatting habit, or obvious mistake guarantees authorship; clues can only inform a probability, and there is no reliable way to be sure without human acknowledgement. | Direct author conclusion and interpretation; no formal probabilistic model or reliability study. | **fully covered:** root and process product boundaries state that human-eyes audits patterns and does not classify authorship; complete Audit combines deterministic and agent-assessed review without claiming origin. | The article does not validate a probability score or detector ensemble. | Take no product action; retain as support for non-authorship wording and refusal to produce certainty claims. | pending | not started |
| C12: Bailey found factual mistakes more telling than punctuation: ChatGPT allegedly conflated two lawsuits, Copilot misstated Klein's admission, and DeepSeek falsely said a newly filed suit had settled. | Direct author inspection of three generated outputs, with links to surrounding source material but no preserved raw outputs or documented fact-check trail in this record. | **partly covered:** #41 journalism review asks for unsupported claims, wrong dates, unverifiable statements, and source traceability; `pattern-opportunities.md` already maps Bailey to source-grounding and claim verification. | human-eyes does not perform comprehensive external fact checking, and factual error is not authorship proof. The exact examples cannot be independently matched to the outputs here. | Keep the #41 manual source-verification mapping; do not turn factual mistakes into an AI-writing check or claim the three examples are reproduced. | pending | not started |
| C13: Finding the factual errors required deep reading; for casual readers, an em dash may only prompt deeper analysis. | Direct author process observation based on this test; no timing, reviewer, or accuracy comparison. | **fully covered:** #41 provides genre-specific manual review, while the root pattern table frames #49 as a cue rather than a verdict. | A surface-only finding cannot establish the deeper factual result, and a complete human-eyes Audit is still not a fact checker. | Take no new product action; retain the sequence as process context: surface cue, then source-aware review, without authorship inference. | pending | not started |
| C14: ChatGPT, DeepSeek, and Copilot used em dashes "well beyond what any human would likely do." | Direct author interpretation of the three one-shot counts; no human comparison corpus, genre baseline, distribution, or threshold. It conflicts with the article's own recognition of heavy habitual human use. | **challenges current behaviour:** root row 49 avoids this universal comparison, but the source's name in the evidence list could be misread as support for strong severity if the limitation is omitted. | The claim cannot establish a human ceiling or specificity and should not be used to justify fail-on-any behaviour. | Explicitly do not promote the human-ceiling claim; keep Bailey's root mapping qualified as a small test with explicit limits. | rejected | not applicable |
| C15: Replacing em dashes raises rhetorical questions about whether many hyphens or parentheses would then become AI signs. | Speculative questions, not findings; no examples, counts, model outputs, human controls, or test. | **not covered:** correctly, #49 checks U+2014 only and #18 covers a specific cluster of stock compound modifiers rather than generic hyphens; parentheses are not treated as a generic AI signal. | Expanding to en dashes, hyphens, or parentheses would chase an unvalidated evasion path and increase human false positives. | Do not promote generic hyphen, en-dash, or parenthesis checks from this source. | pending | not started |
| C16: The preserved article is complete, but its linked Google Doc raw outputs, exact model builds, and reproducible fact-check record are unavailable, so direct observations cannot be independently recomputed. | Reviewer provenance assessment based on the preserved snapshot and archive; not a claim Bailey makes. | **fully covered:** the source-ingest contract requires explicit access limitations, directness, archived prior bytes, stable hashes, and follow-up items; this card and snapshot now supply them. | A future source refresh would be needed to convert the six outputs from author-reported observations into reviewable raw evidence. | Keep the evidence bounded and request the linked outputs only if later threshold or fixture work depends on them; no product action. | pending | not started |
| C17: Bailey parenthetically says DeepSeek is "allegedly based on ChatGPT," linking a Gizmodo article. | Cited, indirect, and unresolved allegation. Bailey supplies no model-lineage or training evidence, the linked Gizmodo source was not reviewed or preserved in this work unit, and "based on ChatGPT" is ambiguous. | **not covered:** appropriately, the project records only the tested product name and H25 requires model-family claims to remain distinct from generic-AI evidence; it does not encode the alleged lineage. | This source does not establish DeepSeek's lineage and cannot use that allegation to explain the similar one-shot dash counts or infer a shared model family. | Record the allegation only as indirect unresolved context; explicitly do not promote it into model metadata, H25 evidence, a punctuation explanation, or product guidance. Ingest the linked account separately and seek primary evidence before any lineage-dependent use. | pending | not started |

## Recommendations

- C01: Record as practitioner support for the existing non-authorship boundary; take no product action.
- C02: Preserve only as public-tell provenance; do not promote the nickname or prevalence claim.
- C03: Record the punctuation distinctions and human-use counterexample without adding a check or changing severity.
- C04: Do not promote the keyboard-convenience or "most humans" assertion.
- C05: Retain the one-prompt method as dated context; require raw outputs and model identifiers before fixture use.
- C06: Record the six author-reported counts and Bailey's one-highlighted-section qualification for Claude with limits; do not adopt them as thresholds, prevalence estimates, clustering evidence, or fixtures yet.
- C07: Add Bailey only to the existing #49 calibration question and require stratified matched evidence before any severity decision.
- C08: Record evasion and drift as interpretation limits; do not chase replacement punctuation without direct evidence.
- C09: Preserve the human look-alike and evaluate any-occurrence versus density behaviour with deliberate-use controls before changing #49.
- C10: Keep the deeper-review cue and source caution; do not derive a threshold from this article.
- C11: Take no product action; retain the no-certainty conclusion as support for the product boundary.
- C12: Keep the #41 source-verification mapping while explicitly separating factual review from authorship inference.
- C13: Take no product action; retain the surface-cue to deeper-review sequence as process context.
- C14: Explicitly do not promote the unsupported human-ceiling interpretation.
- C15: Do not promote generic hyphen, en-dash, or parenthesis checks.
- C16: Keep the provenance limitation and retrieve raw outputs only if later decision work requires them.
- C17: Keep the linked DeepSeek-lineage allegation cited, indirect, unresolved, and explicitly non-promoted; do not use it to explain the dash result or establish model metadata without separate direct review and primary evidence.

## Evaluation of approved changes

- C01: not applicable - pending source-record recommendation; no product change requested.
- C02: not applicable - pending source-record recommendation; no product change requested.
- C03: not applicable - pending source-record recommendation; no product change requested.
- C04: not applicable - pending source-record recommendation; no product change requested.
- C05: not applicable - pending source-record recommendation; no product change requested.
- C06: not applicable - pending source-record recommendation; focused live checks found one synthetic U+2014 occurrence failed while the equivalent en-dash and hyphen examples passed; the six source outputs were unavailable, so the counts and Bailey's one-section Claude qualification were not rerun.
- C07: not applicable - rejected 2026-07-17; #49 remains fail-on-any as a deliberate stance and no product change was made.
- C08: not applicable - pending source-record recommendation; focused live checks confirmed #49 ignores en dashes and hyphens; no product change requested.
- C09: not applicable - rejected 2026-07-17; #49 remains fail-on-any as a deliberate stance. The earlier focused live checks (one ordinary em dash failed; a formal-report example was context-suppressed) are retained as evidence; no product change was made.
- C10: not applicable - pending source-record recommendation; no product change requested.
- C11: not applicable - pending source-record recommendation; no product change requested.
- C12: not applicable - pending source-record recommendation; no product change requested.
- C13: not applicable - pending source-record recommendation; no product change requested.
- C14: not applicable - rejected 2026-07-17; #49 remains fail-on-any as a deliberate stance without promoting the human-ceiling claim, and no product change was made.
- C15: not applicable - pending source-record recommendation; no product change requested.
- C16: not applicable - pending source-record recommendation; prior and current snapshot hashes verified; no product change requested.
- C17: not applicable - pending source-record recommendation; the linked Gizmodo account was not reviewed in this work unit, and the indirect allegation was not promoted or used as an explanation; no product change requested.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `rereview_bailey_final_batch2_once`; initial review by `review_bailey_batch2_once`, first remediation by `remediate_bailey_batch2_once`, focused re-review by `rereview_bailey_batch2_once`, second remediation by `remediate_bailey_second_batch2_once`, and final focused re-review by `rereview_bailey_final_batch2_once`
- **Reviewer isolation:** fresh source-dedicated agent; one source only; not reused
- **Findings resolved:** three total: the first independent review's two findings are resolved because C06 now preserves Bailey's author-reported, unreproducible qualification that Claude's two em dashes occurred in one highlighted section, while new C17 classifies the linked DeepSeek/ChatGPT allegation as cited, indirect, unresolved, non-promoted, and not an explanation established by this source; the focused re-review's residual root-catalogue finding is resolved by describing Bailey's experiment as a six-service test rather than a six-model test. The fresh final independent re-review passed with no material findings.
- **Unresolved findings:** none
