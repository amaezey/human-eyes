# AI Detectors: How to Tell If Text Is Written by AI: 9 Signs to Look For

## Metadata

- **URL:** https://www.aidetectors.io/blog/how-to-tell-if-text-is-ai-written
- **Author / owner:** AI Detectors
- **Published:** 2026 page context; exact date not stated in the preserved page
- **Retrieved:** 2026-05-05
- **Extracted:** 2026-05-05
- **Contract updated:** 2026-07-15; the preserved extraction was brought into the source-ingest contract without a fresh article scrape
- **Source type:** vendor-authored practitioner guide
- **Evidence tier:** Vendor / detector pages
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** living webpage as retrieved 2026-05-05; previous record was the same preserved article body before source-ingest contract framing
- **Full-text status:** complete
- **Snapshot:** `snapshots/aidetectors-ai-writing-signs.md`
- **Extraction method:** preserved Jina Reader URL-to-Markdown extraction; no fresh scrape
- **Snapshot SHA-256:** `de47b2e3453befb7e82690b2cfbea85ba9ddb1a2177b4065cf1cef57d7fd7e22`
- **Model / corpus scope:** undated vendor observations framed as applying to ChatGPT, Claude, Gemini, and other LLMs in student essays, marketing copy, social posts, and unspecified articles; no model versions, prompts, sample, comparison corpus, language, platform, text-length distribution, annotation method, or measurement dates are supplied; the page mentions GPT-5 and Claude 3.5 without documenting tests
- **Access limitations:** none for the preserved article body; the page supplies no footnotes, datasets, test outputs, methodology, or sources for its reliability, frequency, threshold, detector-performance, model-family, or model-progress claims

## Summary

This AI-detector vendor article presents nine manual signs of AI-shaped prose, illustrated with short constructed examples, then recommends combining several signs with detector tools, author conversation, and document metadata. Its useful contribution is a compact practitioner vocabulary for sentence rhythm, hedging, specificity, stance, transition density, voice, paragraph shape, and source grounding, plus explicit cautions against treating one em dash or one signal as proof. It reports no study, measured sample, human comparison corpus, or validation method, so its numerical thresholds, comparative rates, reliability labels, model-family claims, and promised detection performance are unverified vendor assertions rather than empirical evidence.

## Main insights

- The nine named signs are uniform sentence length, excessive hedging, em-dash overuse, generic examples, overly balanced perspectives, transition-word overload, technically perfect but personality-free prose, repetitive paragraph structure, and missing or nonspecific citations.
- The strongest reusable material is qualitative and contextual: inspect clusters, preserve legitimate human punctuation and qualification, examine specificity and stance, verify named sources, and consider writing process rather than treating one surface cue as authorship proof.
- The article repeatedly overstates its evidence. It calls sentence uniformity the most reliable manual signal, gives a 15-20-word band, claims transition words occur two to three times as often, proposes a 30% em-dash threshold and three- or five-sign suspicion thresholds, calls detector output data-backed confirmation, says the signs catch most cases, and attributes stable traits to model families without showing data.
- Several human comparisons are categorical rather than measured: humans supposedly vary sentence length, draw on lived experience, take sides, accept imperfections, and structure paragraphs organically. These are useful review questions, not universal human-writing rules.
- The page itself supplies important counterweight: em dashes are valid punctuation, one signal is insufficient, edited or newer-model output can be harder to spot, and non-native or formal academic human writing may exhibit the same cues.

## Evidence and claims to extract

- **Direct source reviewed:** Complete preserved article titled "How to Tell If Text Is Written by AI: 9 Signs to Look For," including all nine sections, constructed examples, caveat, confirmation workflow, FAQs, final thoughts, and promotional footer, retrieved 2026-05-05.
- **Method and sample:** Practitioner checklist and vendor marketing copy based on unspecified observation. No sample size, models or versions tested, dates of generated text, prompts, genres by claim, languages, human comparison group, annotators, detector runs, statistical analysis, or article-length controls are disclosed.
- **Direct versus cited evidence:** C01-C13 are direct statements or examples from this page, but none are supported by a disclosed measurement. The article mentions unspecified "studies" and "research" only as examples of vague attribution; it does not cite upstream research for its own claims.
- **Important limits and counterexamples:** Constructed examples show what the author means but cannot establish prevalence, reliability, causality, a threshold, or an authorship verdict. The page acknowledges legitimate human em-dash use, non-native and formal-academic look-alikes, editing and model drift, imperfect detectors, and the need for multiple signals. Its commercial interest in detection and citation-verification tools further limits its value as independent validation.

## Skill-use audit

- **Good use:** Treat the article as weak practitioner terminology and examples for existing review prompts: sentence-rhythm variation, hedge stacking, faux specificity, false balance, structural monotony, source verification, false-positive caution, and model/date metadata.
- **Misuse / overclaim:** Do not cite it as proof that a document is AI-authored, that its nine signs are reliable or broadly prevalent, that three or five signs confirm AI involvement, or that commercial detector agreement is data-backed confirmation.
- **Unsupported use:** Do not adopt its 15-20-word sentence band, 30% em-dash threshold, two-to-three-times transition claim, model-family profiles, GPT-5/Claude 3.5 progress claim, causal training explanations, "inherent" low-burstiness claim, or promise that the signs catch most cases.
- **Underused evidence:** The current project catches two of the article's hedge-list phrases as #22 filler and catches paragraph-initial `It is worth noting` under #50, but it only partly operationalises the article's broader transition-density and source-specificity examples and does not systematically represent its process-history or document-metadata suggestions. Those gaps require stronger evidence and policy work before promotion.
- **Patterns left on the table:** The live checks do not measure density across the article's full transition list, even though `It is worth noting` has filler and paragraph-opener coverage; `Studies show that` is not recognised by the live vague-attribution regex even though `Research has found that` is; detector cross-checking, author conversation, and metadata inspection sit outside the current prose-pattern product boundary.

## Matched patterns / rules

- #52 `sentence-length-variance`; H13 sentence-length mean; H22 long-tail compression and grammatical standardisation
- #22 `no-filler-phrases`, #23 `no-excessive-hedging`, and H12 genre-aware threshold calibration
- #49 `no-em-dashes`; deliberate-punctuation and human-look-alike guidance
- #36 `faux_specificity`
- #37 `neutrality_collapse` and #23a `no-false-concession-hedges`
- #22 `no-filler-phrases` and #50 `no-formulaic-openers` as partial coverage of `It is worth noting`; #47 `no-soft-scaffolding` as an uncovered neighbour for the broader transition-overload claim
- #35 `tonal_uniformity` and the rewrite process's voice-preservation requirements
- #54 `structural_monotony`, #34 `no-tidy-paragraph-endings`, and `paragraph-length-uniformity`
- #5 `no-vague-attributions` and #41 `genre_specific` citation/source verification
- `overall-signal-stacking`, product non-authorship boundary, H3 detection-framing review, H7 advisory catalogue, H9 similar-species disambiguation, H12 genre calibration, and H25 model-family versus generic-AI residue

## Associated hypotheses

- H3: Drop detection framing entirely
- H7: Five-check gating grader plus advisory catalogue
- H9: Field-guide voice with similar-species disambiguation per pattern
- H12: Genre-aware threshold calibration
- H13: Sentence-length mean as a grader check
- H22: Long-tail compression and grammatical standardisation
- H25: Model-family versus generic-AI residue

## Questions / follow-up

- Independent source-record review and focused re-review are complete; the recommendations remain pending user decisions.
- Stronger direct evidence would be required before adopting any numerical threshold, frequency multiplier, detector-confirmation workflow, or model-family attribution from this vendor page.
- If source-grounding coverage is changed later, test both `Studies show that` and `Research has found that` against legitimate quotations, literature-review prose, and named-source controls.
- If transition density is evaluated later, compare paragraph-initial transitions across matched genres rather than importing the article's unsupported two-to-three-times claim.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none found; preserved 2026-05-05 Jina Reader extraction | `snapshots/archive/aidetectors-ai-writing-signs/2026-05-05-92ded73f.md` | 2026-05-05 | `92ded73f1084b25277acea9b57cf5e491c62b8fde82474667bd8f0c678c03110` |
| current | none found | `snapshots/aidetectors-ai-writing-signs.md` | 2026-05-05 | `de47b2e3453befb7e82690b2cfbea85ba9ddb1a2177b4065cf1cef57d7fd7e22` |

The article body is unchanged. The current snapshot adds the required provenance, scope, extraction-verification, omission, and attachment fields around the preserved text. The prior card's compact second-pass notes were expanded into a complete claim inventory and live-project comparison.

## Decision history

- The previous card predated claim IDs and decision/implementation fields. It recorded no user-approved recommendation and no source-specific implementation.
- No prior claim was removed. Earlier mappings to #7 AI vocabulary and #55 even-jargon distribution were not carried forward as source claims because the preserved article does not present an AI-vocabulary list or a technical-jargon-distribution claim. Root-index mappings to #3 superficial -ing analysis, #33 countdown negation, and #43 corporate AI-speak were also removed because the preserved article does not support those constructions. The old reference to #35 as a possible mapping is now scoped to C07's personality/register claim.
- The first independent review found material coverage errors in C02, C04, and C06. This remediation records the exact C02 wording and #22 findings, changes C04 from fully to partly covered because `faux_specificity` cannot detect a complete absence of attempted specificity, and changes C06 from not covered to partly covered because `It is worth noting` triggers both filler and paragraph-initial formulaic-opener checks. All affected recommendations remain pending; the subsequent focused independent re-review passed.
- C01-C13 are newly assigned stable IDs for the unchanged preserved article and therefore begin at `pending` / `not started`.
- C02 approved 2026-07-17 (DR-118 component 3): `can potentially` joined the #23 hedging density list; `it is important to note` was already in #22 and `may vary depending on` was already covered by the DR-150 `may vary` entry.

## Project coverage

This is the authoritative review table. Deterministic results below are focused live-function checks against exact or closely combined article examples; they are surface evidence only, not a complete human-eyes Audit.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Similar sentence lengths create mechanical rhythm; the page calls this the most reliable manual signal and suggests a 15-20-word band. | Direct vendor assertion with one four-sentence constructed AI-like example and one contrasting human-like example; no corpus, reliability test, genre control, or source for the word band. | **partly covered:** #52 `sentence-length-variance`, H13, and H22 cover coarse rhythm/structure questions. The live #52 check skipped the exact 39-word, four-sentence AI-like example as short text. | The example is below the check's opportunity threshold; the article does not validate the project's SD threshold or its own band, and neither establishes authorship. | Keep AI Detectors as weak practitioner context for #52 only; do not adopt the reliability label or 15-20-word band. Evaluate sentence-length measures under H12/H13/H22 on matched genres before any rule change. | pending | not started |
| C02: Repeated qualifiers such as "It is important to note that...", "This can potentially...", and "This may vary depending on..." soften nearly every claim; the page attributes this to model caution training. | Direct vendor observation and phrase list; no counts, comparison corpus, training evidence, or model/version scope. One or two hedges are expressly described as normal. | **partly covered:** #22 `no-filler-phrases`, #23 `no-excessive-hedging`, and the rewrite process preserve warranted qualification. A focused combined passage using all six exact source phrases produced zero `no-excessive-hedging` findings, but `no-filler-phrases` produced two findings corresponding to `it is important to note` and `it is worth mentioning`; because the source contracts the latter as `It's worth mentioning`, the grader's verbatim spans are `it is important to note` and `worth mentioning`. | #22 catches two stock frames, but #23 does not recognise any of the exact examples or represent the page's repeated-qualification density claim. The causal training explanation and universal human willingness to take a stance are unsupported. | Keep the two exact #22 matches as weak practitioner support for existing filler coverage and retain the remaining phrase list only as discovery evidence. Do not expand #23 or change thresholds from this page alone; if pursued, test exact candidates and legitimate uncertainty across academic, policy, and informal controls under H12. | approved | implemented |
| C03: ChatGPT especially overuses em dashes; more than 30% of sentences merits a flag, but em dashes are valid human punctuation and never sufficient alone. | Direct vendor assertion with no counts, corpus, model version, denominator definition, or source; the human-use caveat directly qualifies the threshold claim. | **challenges current behaviour:** #49 and project guidance acknowledge density, deliberate style, genre, and false positives, but live `no-em-dashes` failed the article's own human example for one em dash because it fails on any occurrence. | The implementation is occurrence-based despite density-oriented explanation. The vendor's 30% threshold cannot resolve that discrepancy. | Do not adopt 30%. Add this page only as weak caution/example context to the existing #49 calibration question; evaluate occurrence versus density with stronger matched evidence and deliberate-use controls before changing behaviour. | pending | not started |
| C04: AI examples are plausible but generic; human examples use names, numbers, personal observations, and lived specifics. | Direct constructed pair contrasting a generic marketing scenario with an Acme/Claude/time-and-engagement example; no authentic AI or human sample and no test that the details are lived rather than invented. | **partly covered:** #36 `faux_specificity` asks whether attempted specifics such as names, dates, places, sensory details, or apparently concrete examples are grounded or merely genre-convention filler. It does not flag a complete absence of attempted specificity, and it requires complete agent assessment rather than a regex. | The source's generic AI-like example contains no performed specificity for `faux_specificity` to list. The article also incorrectly treats surface specificity as a reliable human distinction; generated text can invent names and numbers. | Retain the pair as weak evidence for a manual missing-specificity question, subject to source grounding and genre controls; do not broaden #36 or require added names or numbers from this vendor example alone. | pending | not started |
| C05: AI habitually presents both sides with diplomatic neutrality instead of committing to a position. | Direct vendor generalisation without examples, corpus, topic controls, safety/prompt context, or distinction between appropriate balance and evasive balance. | **fully covered:** #37 `neutrality_collapse` evaluates lost stance, and #23a `no-false-concession-hedges` recognises narrow stock both-sides formulas. A focused check of the article's descriptive sentence produced no deterministic #23a candidate, as expected; #37 requires whole-text agent judgement. | The page's claim that human writers take sides is overbroad; informative, legal, academic, and contested-topic prose may require balance. | Take no product action. Keep as weak practitioner support for the existing whole-text stance review, subject to H9/H12 look-alike and genre controls. | pending | not started |
| C06: Paragraphs that repeatedly begin with formal transitions such as "Furthermore," "Moreover," and "Additionally" show transition-word overload; the page claims AI uses them at two to three times the human rate. | Direct phrase list and unsupported comparative multiplier; no corpus, unit of analysis, baseline, genre, or model/date details. | **partly covered:** #22 `no-filler-phrases` and #50 `no-formulaic-openers` both recognise paragraph-initial `It is worth noting`; #47 `no-soft-scaffolding` remains only an adjacent check. In a focused paragraph-separated passage containing every listed transition, #22 found `it is worth noting`, #50 found that same paragraph opener, and #47 found zero candidates. | The other listed transitions and their claimed paragraph-opening density are not covered, and no paragraph-initial denominator exists. The two-to-three-times multiplier is unsubstantiated; the two live findings are overlapping coverage of one source phrase, not evidence of density. | Preserve the existing #22/#50 coverage for `It is worth noting` and defer only the remaining phrase-list and transition-density gap. Before any implementation, measure paragraph-initial transitions in matched genres and test legitimate argumentative, legal, and instructional controls; do not import the two-to-three-times claim. | pending | not started |
| C07: Technically perfect grammar combined with a sterile, unvarying voice may lack personality; human writing may use fragments, colloquialisms, humour, and register shifts. | Direct practitioner interpretation with no measured texts; it conflates grammatical correctness, informality, personality, and human authorship. | **partly covered:** #35 `tonal_uniformity` reviews register lock, and rewrite/write guidance preserves stance, point of view, humour, doubt, and deliberate form. The project does not treat correct grammar or typo absence as a violation. | No safe check can infer personality from errorlessness alone, and deliberate formal consistency is a human look-alike. | Explicitly do not promote perfect grammar, typo absence, slang, or fragments as authorship rules. Retain only the higher-level voice/register question under existing H9/H12 controls. | pending | not started |
| C08: Repeating a topic sentence, elaboration, example, and echoing conclusion in every paragraph creates mechanical structure. | Direct practitioner description of a four-step formula; no analysed documents or frequency comparison. The page also notes legitimate paragraph-length variation. | **fully covered:** #54 `structural_monotony` asks whether sections repeat a rhetorical arc; #34 checks repeated tidy paragraph endings; `paragraph-length-uniformity` measures block-size sameness only. Complete agent assessment is required for the claimed formula. | Surface-only paragraph-length CV cannot establish rhetorical-arc repetition, and the article supplies no threshold or controls. | Take no product action. Retain as a weak explanatory example for #54, clearly separate from the paragraph-length metric and from authorship inference. | pending | not started |
| C09: Missing named sources, vague "Studies show" or "Research has found" attributions, and fabricated citations warrant verification. | Direct vendor observation; the hallucination statement is unsupported here, but the exact vague-attribution examples and verification advice are clear. No incidence, model, genre, or citation dataset is supplied. | **partly covered:** #5 `no-vague-attributions` and #41 academic/journalism branches verify citations and source support. A focused check failed on `Research has found that` but did not recognise `Studies show that`. | The exact `Studies show that` variant is a lexical gap; complete citation existence/support checks remain manual and genre-specific. | Keep the source in #41's source-grounding mapping. Consider `Studies show that` for #5 only after focused candidate/control tests and quotation handling; do not treat citation failure as authorship proof. | pending | not started |
| C10: Manual review is a starting point rather than a conclusion; one signal is insufficient, while the page proposes suspicion at three signs and stronger concern at five. | Direct vendor advice containing a sound qualitative caution and unsupported fixed three-/five-sign thresholds; no calibration, weighting, dependence analysis, base rate, or outcome definition. | **partly covered:** `overall-signal-stacking` combines a defined subset of deterministic findings at threshold four, while README/process guidance says density, genre, intent, and co-occurrence matter and forbids authorship verdicts. It does not count these nine signs or validate the vendor thresholds. | The vendor's signs overlap and are not independent. The project aggregate omits agent judgements and is diagnostic, not confirmation. | Preserve the one-signal caution; explicitly do not adopt the three-/five-sign counts. Any aggregate change requires claim-independent calibration, complete-Audit coverage, and matched human/AI evaluation under H3/H7/H12. | pending | not started |
| C11: Confirmation should combine an AI detector, multiple detector tools, author conversation, and document metadata; detector output is described as data-backed assessment. | Direct vendor workflow and product promotion; no detector names/results, validity study, metadata taxonomy, process protocol, or evidence that agreement confirms authorship. | **challenges current behaviour:** human-eyes deliberately audits prose patterns rather than classifying authorship. It supports source/provenance review in #41 but has no commercial-detector ensemble, author-interview workflow, or document-metadata check. | Cross-detector agreement can share biases and is not confirmation. Author conversation and metadata may be useful process evidence but raise separate policy, access, and fairness questions. | Do not promote detector cross-checking or "data-backed confirmation." Record author/process history and metadata as possible non-prose provenance inputs for separate policy design only; keep them outside pattern scoring unless independently validated. | pending | not started |
| C12: ChatGPT favours em dashes, Claude verbose caveats, and Gemini structured lists; newer GPT-5 and Claude 3.5 are more natural, but low burstiness and hedging supposedly persist inherently. | Direct, dated vendor assertions with no prompts, outputs, model build identifiers, dates, sample, comparison, or citations. The causal and persistence claims are unsupported and highly drift-prone. | **not covered:** H25 records model-family/version residue as a research dimension; active rules are not model-attribution checks. Source metadata conventions require model/date scope that this page lacks. | The page mixes model-family attribution, product-version progress, generic-AI cues, and causal explanation without evidence. | Record only as unverified 2026 vendor observations under H25; do not map them to generic checks, model attribution, or causal explanations. Require direct dated model outputs and matched controls before reconsideration. | pending | not started |
| C13: Edited or newer-model text may be harder to spot, and non-native English or formal academic human writers may naturally display the listed cues. | Direct caveat without measured false-positive or editing study, but it contradicts the page's broader reliability and "catch most" language and identifies concrete human look-alikes. | **fully covered:** the product boundary rejects authorship classification; H9/H12 require look-alikes and genre calibration; academic hedging and some punctuation are context-gated; testing guidance requires matched genres and false-positive review. | Current context gates do not encode nationality or native-language status, appropriately; the page cannot quantify the risk or justify demographic inference. | Retain the caveat as a reason to soften or withhold claims, never as a demographic writing profile. Require stronger direct fairness and editing evidence for evaluation design; take no source-specific product action. | pending | not started |

## Recommendations

- C01: Keep as weak #52 context; reject the reliability label and 15-20-word band pending matched H12/H13/H22 evaluation.
- C02: Record `It is important to note` and `It is worth mentioning` as weak #22 support; retain the other exact phrases as discovery evidence and require genre-matched candidate/control evaluation before any #23 or threshold change.
- C03: Reject the 30% threshold; include the article only as weak caution context in the existing occurrence-versus-density evaluation for #49.
- C04: Record the constructed pair as weak evidence for a manual missing-specificity question, while preserving source-grounding and genre controls; do not broaden #36 from this page alone.
- C05: Take no product action; retain as weak support for existing stance review with look-alike controls.
- C06: Preserve the existing #22/#50 mapping for `It is worth noting`; defer the remaining transition-list and density gap, and do not promote the multiplier without matched evidence.
- C07: Explicitly do not promote grammatical correctness, typo absence, slang, or fragments as authorship indicators; retain only the existing voice/register review.
- C08: Take no product action; retain the paragraph formula only as a qualified #54 illustration.
- C09: Keep the source-grounding mapping and evaluate the `Studies show that` lexical gap with quotation and legitimate-use controls before any #5 change.
- C10: Preserve the one-signal caution but reject fixed three-/five-sign counts; require calibrated complete-Audit evaluation for aggregate changes.
- C11: Do not promote commercial detector agreement as confirmation; handle author process and metadata, if desired, as a separate provenance-policy question.
- C12: Record the model-family/version statements as unverified dated H25 observations only; do not create generic or model-attribution rules.
- C13: Retain the human-look-alike caveat for report restraint and evaluation design; never turn native-language status into a prose pattern.

## Evaluation of approved changes

- C01: not applicable - pending source-record recommendation; no product change requested.
- C02: passed - `can potentially` counts toward #23 density; the DR-118 assertion in test_grade.py holds it.
- C03: not applicable - pending source-record recommendation; no product change requested.
- C04: not applicable - pending source-record recommendation; coverage corrected to partly covered because `faux_specificity` does not detect complete absence of attempted specificity; no product change requested.
- C05: not applicable - pending source-record recommendation; no product change requested.
- C06: not applicable - pending source-record recommendation; focused live checks found one filler and one formulaic-opener finding for `It is worth noting`, while the broader transition-density gap remains; no product change requested.
- C07: not applicable - pending source-record recommendation; no product change requested.
- C08: not applicable - pending source-record recommendation; no product change requested.
- C09: not applicable - pending source-record recommendation; no product change requested.
- C10: not applicable - pending source-record recommendation; no product change requested.
- C11: not applicable - pending source-record recommendation; no product change requested.
- C12: not applicable - pending source-record recommendation; no product change requested.
- C13: not applicable - pending source-record recommendation; no product change requested.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `review_aidetectors_once`; remediation by `remediate_aidetectors_once`; focused independent re-review by `rereview_aidetectors_once` passed
- **Reviewer isolation:** fresh source-dedicated agent; one source only; not reused
- **Findings resolved:** five findings from the first review: corrected C02's exact source wording and #22 results; narrowed C04 to partly covered because missing specificity is outside `faux_specificity`; recorded C06's partial #22/#50 filler-and-opener coverage; removed stale unsupported root-index mappings; distinguished the 2026-05-05 extraction from the 2026-07-15 contract update
- **Unresolved findings:** none
