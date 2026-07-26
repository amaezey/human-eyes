# @hosseeb: How to avoid AI voice

## Metadata

- **URL:** https://x.com/hosseeb/status/1969157336100192663
- **Author / owner:** Haseeb Qureshi (@hosseeb)
- **Publisher:** X
- **Published:** 2025-09-19
- **Retrieved:** 2026-07-14
- **Extracted:** 2026-07-14
- **Source type:** X post containing practitioner observations and writing-process advice
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** X post ID 1969157336100192663
- **Version / revision:** single post published 2025-09-19; source bytes unchanged from the pre-contract 2026-07-14 extraction; card upgraded to the current contract on 2026-07-15
- **Full-text status:** complete
- **Snapshot:** `snapshots/qureshi-avoiding-ai-voice.md`
- **Extraction method:** fxtwitter mirror API JSON transcription of the complete single-post body from https://api.fxtwitter.com/hosseeb/status/1969157336100192663; publication time cross-checked by decoding the X post ID snowflake
- **Snapshot SHA-256:** `f6b48ad3c639baaab3e524864b5ba293851e04ee2822d8b00c05b99b5cc07a70`
- **Model / corpus scope:** one English X post of about 340 words, published in September 2025; it discusses unspecified AI writing tools, names Claude Projects and Pangram, does not identify a target writing genre, and supplies no model version, corpus, comparison sample, frequency estimate, or threshold
- **Access limitations:** x.com blocked anonymous retrieval, so the complete post body was obtained through the fxtwitter mirror API. The post is a single long post rather than a thread. Author replies, if any, were not retrieved and are outside the reviewed single-post scope. The source supplies no link for its claimed University of Chicago study.

## Summary

This September 2025 X post gives practitioner advice for avoiding a recognisable AI voice. Qureshi says AI voice sounds hollow and cheap to most readers, says one-shot drafting guarantees that voice, recommends local editing and writer-controlled revision, names four surface tells, and proposes Pangram as a pre-publication perception proxy. The post contributes dated practitioner corroboration and a clear no-authorship qualification, but it contains no measured comparison, threshold, model version, or direct detector evidence. Its Pangram accuracy claim is inherited from an unidentified study, while its low-entropy and human-signature claims are direct but uncited assertions.

## Main insights

- Qureshi frames AI voice as a reader-perception and craft problem rather than proof of authorship.
- He says one-shot generation guarantees AI voice and recommends supplying the writer's own material and style context when whole-draft generation is used.
- He recommends using AI for local editing, beginning whole-piece work with critique, discussing alternatives, and accepting only edits the writer endorses.
- He names the U+2014 em dash, `delve`, `intricate`, and `not just X, but Y` as common AI-associated forms.
- The post explicitly says those forms do not guarantee AI authorship. Its concern is that readers may assume AI use when they see them.
- The Pangram accuracy, detector-comparison, low-entropy, and human-signature claims are not supported by a linked study in the post.

## Evidence and claims to extract

- **Direct source reviewed:** the complete body of X post ID 1969157336100192663, published 2025-09-19 and preserved verbatim in the snapshot.
- **Method and sample:** one English practitioner post of about 340 words. It provides recommendations and examples from the author's experience, not a corpus, experiment, comparison group, model evaluation, reader study, or writing-quality study.
- **Direct versus cited evidence:** C01, C02, and C04 to C11 are direct statements or recommendations made by Qureshi, supported only by practitioner observation. Within C03, the detector comparison and 99%+ precision-and-recall figure are attributed to an unnamed University of Chicago study whose underlying evidence was not supplied. The low-entropy mechanism and categorical human-signature claims are Qureshi's direct but uncited assertions.
- **Important limits and counterexamples:** the tell list is expressly non-exhaustive; none of the four forms receives a frequency estimate from this source; the post says their presence does not prove AI authorship, leaving legitimate human usage as an explicit possibility and a counterexample to authorship inference. The source does not support its claims about most readers or universal AI use, test whether one-shot drafting guarantees a recognisable register, test whether local editing preserves voice, establish that readers and Pangram agree, or measure its prediction that readers will improve at identifying AI voice. It does not identify a target writing genre or establish whether the advice generalises beyond the unspecified writing context of one English X post in September 2025.

## Skill-use audit

- **Good use:** dated practitioner corroboration for four known surface forms; support for the project's craft and reader-perception framing; a direct no-authorship qualification; and possible non-binding workflow guidance about writer control, critique before revision, and selective acceptance.
- **Misuse / overclaim:** using the post to set severity, a count threshold, a detector score, or an authorship verdict; treating its four examples as a complete blacklist; or presenting the Pangram and entropy claims as verified.
- **Unsupported use:** claims about any named model version, non-English writing, detector fairness, classifier performance, reader accuracy, causal workflow effects, or the frequency of the four forms in human and AI text.
- **Underused evidence:** the live project already values voice preservation and deliberate choice, but it does not state Qureshi's specific one-shot, local-editor, critique-first, or selective-acceptance workflow.
- **Patterns left on the table:** no new prose pattern. The only possible additions are source mappings, contextual reader-perception wording, and process guidance, all pending Mae's decision and any required evaluation.

## Matched patterns / rules

- `STRATEGY.md` partly covers the craft framing and fully covers the boundary against authorship classification; it does not make the post's universal-use or majority-reader claims.
- `human-eyes/references/process.md` partly covers writer control, voice preservation, planned editing, and validation, but not Qureshi's one-shot, local-editor, critique-first, or top-edits sequence.
- `no-em-dashes` / pattern C7 in `human-eyes/scripts/grade.py`, `human-eyes/scripts/patterns.json`, and `human-eyes/references/patterns.md` detects every U+2014 occurrence. Its current implementation fails a single occurrence at Balanced and All depth.
- `no-ai-vocabulary-clustering` / pattern B1 recognises `delve` and `intricate`, but the deterministic check passes one or two listed words in a paragraph and fails at three or more.
- `no-negative-parallelisms` / pattern B3 directly detects `not just X, but Y`, reports occurrence count, and states that a match is not proof of authorship.
- `pangram-classifier.md` (with `spero-emi-pangram-classifier.md` retired 2026-07-17 as its duplicate) and the detector-caution rows in `pattern-opportunities.md` cover Pangram as evaluation context rather than prose-pattern evidence. They do not verify the post's 99%+ claim.
- No live agent-assessment record in `human-eyes/scripts/judgement.json` covers one-shot drafting, editor-versus-ghostwriter workflow, selective acceptance, or agreement between detector output and reader perception.

## Associated hypotheses

- H3, drop detection framing entirely.
- H7, five-check gating grader plus advisory catalogue.
- H9, field-guide disambiguation for legitimate human look-alikes.
- H11, manufactured insight as a deliberate human rhetorical move that still requires matched-register calibration.
- H24, register-specific vocabulary density rather than flat one-word blacklists.
- H25, model-family, model-version, prompt-style, and public-tell drift.

## Questions / follow-up

- Can the unnamed University of Chicago detector study be identified and reviewed directly, and does it support the reported 99%+ precision and recall claim?
- Should this source be mapped to patterns B1, B3, and C7 as practitioner corroboration without changing their rules or severity?
- Should any of the workflow advice be added as optional process guidance, and what real rewrite samples would be required before doing so?
- Should the reader-perception qualification appear in report guidance, or is the existing non-authorship boundary sufficient?
- Should the recommendation to use Pangram as a reader proxy be explicitly recorded as a non-promotion because it conflicts with the project's detector-caution evidence?

## Update provenance

The source and current snapshot are unchanged. This update upgrades a pre-contract card to the current source-ingest structure. An archival copy preserves the exact snapshot bytes that supported the pre-contract card, so the previous and current record remain independently addressable even though their digests match.

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | X post ID 1969157336100192663 | `snapshots/archive/qureshi-avoiding-ai-voice/2026-07-14-1969157336100192663.md` | 2026-07-14 | `f6b48ad3c639baaab3e524864b5ba293851e04ee2822d8b00c05b99b5cc07a70` |
| current | X post ID 1969157336100192663 | `snapshots/qureshi-avoiding-ai-voice.md` | 2026-07-14 | `f6b48ad3c639baaab3e524864b5ba293851e04ee2822d8b00c05b99b5cc07a70` |

## Decision history

- None. The pre-contract card contained analysis but no claim-level user decisions or implementation statuses. This update preserves that analysis, assigns claim IDs, and opens every recommendation as `pending` with implementation `not started`.

## Project coverage

This is the authoritative review table. Each coverage verdict reflects the live implementation and documentation inspected on 2026-07-15.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Qureshi says AI voice sounds hollow and cheap to most readers, while everyone uses AI for writing and the difference is whether it is done well. | Direct practitioner framing from one English X post. The majority-reader and universal-use wording is unsupported by a reader study, comparison corpus, rate, model version, or human control. The post distinguishes writing quality from provenance. | Partly covered: `STRATEGY.md` defines the target as cumulative patterns that make AI-assisted prose feel synthetic while rejecting authorship classification. It does not claim that everyone uses AI for writing or that AI voice sounds hollow and cheap to most readers. | The source adds a dated practitioner formulation, but its prevalence and majority-reader assertions have no live implementation or evaluation evidence. | Record as corroborating project framing only. Do not change a rule, severity, threshold, or product claim from this source. | pending | not started |
| C02: Qureshi says one-shot generation guarantees AI voice and recommends starting from the writer's bullet points, a custom prompt, and past writing as context, with Claude Projects named as suitable for this use. | Direct practitioner recommendation; the guarantee and implied causal benefit are unsupported by an experiment, comparison, model version, or measured outcome. Style imitation may also flatten or misrepresent voice. | Not covered: no deterministic check or agent assessment can infer drafting workflow from final prose. `human-eyes/references/process.md` protects supplied facts, stance, and voice but does not prescribe this prompting method. | The project has no evidence that the proposed workflow reliably prevents catalogue findings or preserves voice across genres and models. | If Mae wishes to consider workflow guidance, evaluate one-shot and writer-seeded drafting on real matched briefs with complete Audits and voice-preservation review before adding non-binding guidance. | pending | not started |
| C03: Pangram has 99%+ precision and recall, lazy AI writing is reliably detectable, low-entropy token choice supplies the signature, and human writing cannot imitate it closely enough to register as AI. | Mixed directness and unresolved. The detector comparison and 99%+ figure are inherited from an unidentified University of Chicago study. The low-entropy mechanism and human-signature claims are Qureshi's direct but uncited assertions. The post names no dataset, model, domain, threshold, detector version, class balance, or error definition. The project's Liang detector-bias record provides counterevidence to any absolute human-signature claim. | Challenges current behaviour: `pangram-classifier.md` and `spero-emi-pangram-classifier.md` record benchmark and domain claims without supporting the 99%+ figure; `liang-detector-bias.md`, `STRATEGY.md`, and `pattern-opportunities.md` collectively reject using classifier scores as prose-rule severity or individual authorship proof. | The named study is unidentified, the exact figure is unverified, and the categorical human-versus-AI mechanism exceeds the reviewed evidence. | Keep this claim unresolved and out of product guidance. Identify and ingest the direct study separately before any further recommendation. | pending | not started |
| C04: Writers should run drafts through Pangram before publication, treat a detector flag as a proxy for how readers will respond, and expect readers to become better at identifying AI voice. | Direct practitioner recommendation and trend prediction, but the equivalence between one detector and reader perception is untested in the post. It supplies no false-positive controls, longitudinal evidence, or genre, language, length, and model limits. | Challenges current behaviour: human-eyes requires a complete source-bound Audit for its own actions and states that writing-pattern findings do not classify authorship. Existing detector evidence is retained for calibration and caution, not as a reader-perception oracle. | No live evidence establishes agreement between Pangram and readers or supports the predicted improvement in reader identification. Promoting this advice could reintroduce the detector framing the project deliberately avoids. | Record as a non-promotion unless Mae requests a separate reader-perception evaluation. Do not recommend Pangram as a publication gate from this source. | pending | not started |
| C05: AI should be used as a local editor rather than a ghostwriter, with tightening and flow work limited to sentences or paragraphs. | Direct practitioner process advice; no comparison, quality measure, genre control, or test of whether local edits preserve meaning and voice. | Partly covered: `human-eyes/references/process.md` plans edits, protects meaning and voice, validates changed context, and requires a fresh complete Audit. It does not state an editor-versus-ghostwriter rule or limit assistance to local spans. | The source offers useful craft language but no evidence for a universal span limit or a claim that local AI edits are safer. | If Mae approves process work, consider non-binding local-edit guidance paired with the existing protected-literal, changed-context, and complete-Audit safeguards. Verify it on real rewrite cases before promotion. | pending | not started |
| C06: Whole-piece editing should begin with critique and discussion, then present a ranked set of explained before-and-after edits that the writer selectively accepts. | Direct practitioner workflow advice; the number ten is prescriptive rather than evidence-based. Selective acceptance preserves writer agency in principle, but the post does not test outcomes. | Partly covered: `human-eyes/references/process.md` requires planning, material edit explanations, exact changed-context validation, preservation checks, and user-visible unresolved findings. It does not require critique-first discussion, ranking, or a fixed top-ten list. | The useful elements are critique before rewriting, reasons for each edit, and writer choice. A fixed count may distort the amount of work and is not supported as a threshold. | If Mae approves, evaluate critique-first and selective-acceptance workflow as optional guidance. Do not import the fixed top-ten quantity as a project rule. | pending | not started |
| C07: Qureshi lists the U+2014 em dash as a common AI-associated form writers should avoid and says it has become socially costly because readers may assume AI use. | Direct practitioner observation from September 2025; no frequency comparison or reader study. The post explicitly says the form does not guarantee AI authorship and acknowledges legitimate human use by implication. | Partly covered: `check_em_dashes` and pattern C7 detect every U+2014 occurrence. A focused run on one occurrence returned `passed: false` with `Found 1 em dash(es)`. The registry calls density the giveaway and recognises deliberate human use, but the implementation fails any occurrence at Balanced and All depth. | The source supports public salience and a no-authorship caveat, not the current severity or zero-tolerance implementation. It adds no direct frequency or false-positive evidence. | Add only a practitioner source mapping and dated reader-perception note if Mae approves. Do not use this post to change severity, threshold, or preservation behaviour. | pending | not started |
| C08: `delve` is a common AI-associated word writers should avoid. | Direct practitioner observation with no count, corpus, context, model, genre, or human comparison. Stronger aggregate academic evidence is recorded in `juzek-ward-delve.md` and `kousha-thelwall-academic-papers.md`. | Partly covered: `delve` is in `AI_VOCABULARY`, pattern B1, and the live registry. A focused run on `We delve into the evidence.` returned `passed: true` with one AI word; the paragraph check fails only at three listed items. | The word is recognised but not surfaced as a standalone failure. This source does not justify changing the clustering threshold or treating one occurrence as proof. | Map as practitioner corroboration only if Mae approves. Retain cluster-based handling and stronger aggregate academic evidence as the basis for any future rule decision. | pending | not started |
| C09: `intricate` is a common AI-associated word writers should avoid. | Direct practitioner observation with no count, corpus, context, model, genre, or human comparison. Stronger aggregate academic evidence is recorded in `juzek-ward-delve.md`, `juzek-ward-word-overuse-alignment.md`, and `kousha-thelwall-academic-papers.md`; legitimate descriptive usage remains a human look-alike. | Partly covered: `intricate` is in `AI_VOCABULARY`, pattern B1, and the live registry. A focused run on `The mechanism is intricate.` returned `passed: true` with one AI word; `delve` plus `intricate` also passed at two, while a paragraph containing three listed items failed. | The word is recognised only as cluster evidence. This source does not justify standalone severity, a lower threshold, or a blanket rewrite rule. | Map as practitioner corroboration only if Mae approves. Keep it within contextual cluster handling unless stronger matched evidence supports a change. | pending | not started |
| C10: `not just X, but Y` is a common AI-associated construction writers should avoid. | Direct practitioner observation with no rate or comparison group. The post explicitly says one use does not prove AI authorship. Deliberate human rhetoric is a known look-alike. | Partly covered: `check_negative_parallelisms`, pattern B3, and `dev/evals/tests/test_grade.py` include the exact form and broader variants. A focused run on `It is not just X, but Y.` returned one candidate and `passed: false`. Registry guidance reports occurrences and rejects authorship conclusions, but it does not impose the source's blanket avoidance advice. | The implementation already detects the example and supplies the qualification. This source adds dated practitioner corroboration but no new variation or threshold evidence, and it does not justify requiring revision of every occurrence. | Add only a source mapping if Mae approves. Make no rule, severity, threshold, or test change from this claim. | pending | not started |
| C11: Surface tells do not guarantee AI authorship, but readers may still accuse writers who use them; public perception is therefore separate from provenance. | Direct practitioner interpretation and explicit qualification. It documents the author's perception of comment-section behaviour, not measured reader accuracy or writing quality. | Partly covered: `STRATEGY.md`, `human-eyes/references/process.md`, pattern B3, and testing guidance establish the non-authorship boundary. Pattern B1 says one word is not proof but still calls a three-word density a fingerprint. The project targets synthetic-feeling prose but does not explicitly describe accusation as the consequence. | The social-cost rationale could clarify why a human-authored occurrence is still surfaced, but it could also encourage camouflage or overstate reader consensus without direct reader evidence. Mae must separately decide whether pattern B1's fingerprint wording needs alignment with the project-wide non-authorship boundary. | If Mae approves, use this only as dated contextual rationale with the explicit no-authorship qualification. Do not use perceived accusation to increase severity or require revision. Separately review pattern B1's fingerprint wording against the project-wide boundary only if Mae asks for that alignment work. | pending | not started |

## Recommendations

- C01: Record the post as corroborating project framing only; make no product change.
- C02: Before considering non-binding one-shot or writer-seeded workflow guidance, evaluate it on real matched briefs with complete Audits and voice-preservation review.
- C03: Keep the Pangram, entropy, and human-signature claims unresolved and out of product guidance until the direct study is identified and separately ingested.
- C04: Record the Pangram reader-proxy advice as a non-promotion unless Mae requests a separate reader-perception evaluation.
- C05: If approved, evaluate optional local-editor guidance together with the project's existing meaning, context, and complete-Audit safeguards.
- C06: If approved, evaluate critique-first and selective-acceptance guidance, but do not import a fixed top-ten rule.
- C07: If approved, add only a dated practitioner mapping and reader-perception note to pattern C7; do not change severity, threshold, or preservation behaviour.
- C08: If approved, map `delve` as practitioner corroboration for pattern B1 while retaining cluster handling and stronger aggregate academic evidence.
- C09: If approved, map `intricate` as practitioner corroboration for pattern B1 while retaining cluster handling and requiring stronger matched evidence for any change.
- C10: If approved, add only a source mapping to pattern B3; the live rule, qualification, and exact example coverage require no change.
- C11: If approved, use the accusation concern only as dated contextual rationale with an explicit no-authorship qualification; do not raise severity from perception alone. Separately review pattern B1's fingerprint wording against the project-wide boundary only if Mae asks for that alignment work.

## Evaluation of approved changes

- C01: not applicable - recommendation pending; no product change implemented.
- C02: not applicable - recommendation pending; no product change implemented.
- C03: not applicable - recommendation pending; no product change implemented.
- C04: not applicable - recommendation pending; no product change implemented.
- C05: not applicable - recommendation pending; no product change implemented.
- C06: not applicable - recommendation pending; no product change implemented.
- C07: not applicable - recommendation pending; no product change implemented.
- C08: not applicable - recommendation pending; no product change implemented.
- C09: not applicable - recommendation pending; no product change implemented.
- C10: not applicable - recommendation pending; no product change implemented.
- C11: not applicable - recommendation pending; no product change implemented.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: Codex CLI fresh process, did not perform the extraction
- **Findings resolved:** corrected softened and omitted source claims, mixed direct-versus-cited attribution, post length and access provenance, target-genre scope, hypothesis coverage, overstated project-coverage verdicts, and recommendation alignment; recorded the live pattern B1 non-authorship wording gap for Mae's decision
- **Unresolved findings:** none
