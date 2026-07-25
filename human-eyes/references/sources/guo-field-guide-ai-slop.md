# Charlie Guo: The Field Guide to AI Slop

## Metadata

- **URL:** https://www.ignorance.ai/p/the-field-guide-to-ai-slop
- **Author / owner:** Charlie Guo
- **Published:** 2025-10-22T14:02:46.371Z
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** Practitioner essay and field guide
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** Substack post 176806840
- **Version / revision:** publisher `updated_at` 2025-10-22T14:05:50.030Z; prior reviewed capture extracted 2026-05-05 with no stable identifier recorded
- **Full-text status:** complete
- **Snapshot:** `snapshots/guo-field-guide-ai-slop.md`
- **Extraction method:** Canonical HTML and public Substack post JSON API fetched with `curl`; first-party `body_html` converted to Markdown with Python 3 and BeautifulSoup 4; all six original images downloaded and visually checked; three content-bearing images transcribed; current Jina Reader extraction used as a text cross-check
- **Snapshot SHA-256:** `258d51d673320ec94c6768983d3714a56c6c5e7a3f8a4015e3adceace2717497`
- **Model / corpus scope:** Dated English-language practitioner observations about ChatGPT, Claude, Gemini, GPT-4o, and GPT-5 across social posts, blogs, long-form articles, workplace messages, professional lists, and creative writing; four source-supplied ChatGPT metaphor examples and one source-labelled AI ukulele example have no prompt, model version, generation date, or comparison sample; the cited Reddit chart covers selected top-post self-text from six technology/startup subreddits rather than a matched human/AI corpus
- **Access limitations:** None for the direct source. The article supplies no raw generation records, detector outputs, authorship labels, systematic human comparison, or data behind most practitioner observations. Its linked Graphite, Originality, Slack, AP-NORC, MIT, Gary Provost, Churchill, and New Yorker materials remain indirect evidence here. The linked em-dash repository was inspected only to verify its implementation and limits; it is not recursively ingested by this record.

## Summary

Guo's dated practitioner field guide names red herrings, stylistic tics, structural patterns, content problems, human look-alikes, detector harms, and an authenticity feedback loop. Its direct evidence is an unlabelled illustrative ukulele passage, four unscoped ChatGPT metaphor examples, the author's repeated observations and personal AI-assisted writing practice, plus two reproduced charts and several cited reports. The complete refresh restores 13 headings and the fifth footnote omitted by the prior Jina snapshot, preserves all six images and first-party source files, and checks the linked em-dash implementation. The source is useful for craft prompts, exact examples, coverage challenges, and false-positive disambiguation; it does not validate prevalence, causality, thresholds, model attribution, detector performance, or document authorship.

## Main insights

- Guo explicitly separates three “yellow flags” from stronger intuitions: academic vocabulary, polished spelling/grammar, and contraction avoidance all have ordinary professional, editing-tool, or second-language explanations.
- The named style and formatting families are em dashes, repeated parallelism, triads, abrupt profundity, mid-paragraph question-answer templates, generic transitions, mechanical bolding, decorative Unicode, excessive lists, and emoji-led professional lists.
- The named rhythm and content families are similar sentence lengths, repeated paragraph cadence, stable tense or point of view, generic metaphors, incoherent throughlines, semantic padding, and polished prose with little underneath.
- Guo repeatedly qualifies the catalogue: one occurrence can be legitimate, human writers use all of these devices, intention and repetition matter, model and prompt effects drift, and even a text with all the tells can be human-written.
- The source's reproduced Reddit chart is weaker than its prose implies. The linked repository warns of top-post time bias; the implementation drops empty/removed self-text, groups by month, plots two-month rolling means, excludes January 2025, and displays May-December 2024 rather than a full plotted year. It measures U+2014 occurrence, not AI use or authorship.
- The categorical detector claims and broad training/RLHF explanations are cited, speculative, or interpretive rather than demonstrated in the article. The model-specific emoji comparison is explicitly anecdotal and system-prompt-confounded.
- The strongest non-pattern contribution is the authenticity warning: fear of accusation can cause human writers to suppress legitimate style. Guo's preferred response is specificity, particular knowledge, tangible experience, voice, and point of view, not detector-directed camouflage.

## Evidence and claims to extract

- **Direct source reviewed:** Complete first-party Substack post 176806840, publisher `updated_at` 2025-10-22T14:05:50.030Z, including 50 root article paragraphs, a five-paragraph block quotation, two lists with eight items, 13 headings, six figures, four captions, 28 links, and five footnotes. The canonical HTML, JSON API record, six original images, current Jina output, and the linked em-dash repository implementation at commit `e40a2fbcfdfb82c9f7fcc21d373405972bcecb6f` were checked.
- **Method and sample:** Practitioner observation with an unreported observation count and no controlled comparison; one source-labelled AI ukulele passage of unspecified provenance; four ChatGPT metaphor outputs with no prompt or model version; one reproduced Graphite/Axios chart; one linked Reddit analysis whose six displayed subreddits contain 489-965 retained top-post self-text records across nine stored months, with only May-December 2024 plotted after January 2025 exclusion. Platform scope is English-language web, workplace, social, professional, and creative-writing contexts.
- **Direct versus cited evidence:** C01, C03-C07, C09-C24, and C27-C30 are direct examples, observations, interpretation, or personal disclosure in Guo's post. C02, C08, C25, and parts of C26 inherit claims from charts, reports, or links; the em-dash code and CSV were inspected, while the other cited materials remain indirect and unresolved for promotion. No claim is a controlled measurement performed by Guo.
- **Important limits and counterexamples:** No ground-truth authorship validation, prevalence estimate, threshold, matched human sample, uncertainty, prompt record, generation record, model-version control, genre control, or longitudinal replication is supplied. Guo provides strong human look-alikes and ends with an explicit non-authorship warning. The article's own em-dash chart description compresses an eight-month displayed range into “over a year,” and the source calls polished emptiness an AI “signature” before acknowledging human weak writing and rejecting conclusive inference.

## Skill-use audit

- **Good use:** Use the source as practitioner language for manual review, exact pattern examples, source-specific model anecdotes, clustering/intention cautions, and false-positive disambiguators. It directly motivates checking whether a pattern is repeated, appropriate to genre, quoted, deliberate, or a normal human/professional convention.
- **Misuse / overclaim:** Do not cite the post as empirical proof that a feature is AI-overrepresented, as support for the live #49 any-occurrence severity, as evidence that RLHF caused list use, as proof that a detector fails, or as evidence that a person or model wrote a document.
- **Unsupported use:** It cannot support numeric thresholds, generic model-family attribution, current-model behavior, prevalence of AI-authored web text, causal training-data claims, causal authenticity effects, or the assertion that any prompt bypasses any detector.
- **Underused evidence:** The live project underuses the article's red-herring controls, its distinction between frequency and occurrence, its stylized-Unicode variants, its model/prompt caveat, its direct human-authenticity harm, and its explicit all-tells-can-be-human conclusion.
- **Patterns left on the table:** Exact stylized-bold and stylized-italic Unicode plus multiplication-sign variants are missed by `no-unicode-flair`; “As technology continues to evolve” and “In today’s fast-paced world” are catalogued under #22 but the focused surface run matched only “At the end of the day”; #42 documents the straight-apostrophe candidate “But here's the thing” but misses Guo's curly-apostrophe form; stable tense/POV is only loosely represented; low information density remains H21; and the current Guo triage row omits #9, #13, #30, #31, #31a, #32, #49, #52, H21, and the red-herring/non-authorship boundaries.

## Matched patterns / rules

- #7 `no-ai-vocabulary-clustering`, with register and single-word cautions
- #9 `no-negative-parallelisms`
- #10 `no-forced-triads`
- #13 `no-boldface-overuse`
- #22 `no-filler-phrases`, partial lexical coverage only
- #29 `no-rhetorical-questions`
- #30 `generic_metaphors` agent assessment
- #31 `no-excessive-lists`
- #31a `no-unicode-flair`
- #32 `no-dramatic-transitions`
- #35 `tonal_uniformity` and `structural_monotony` agent assessments, adjacent rather than exact
- #41 `genre_specific` fiction and marketing/email branches, adjacent rather than exact
- #42 `no-manufactured-insight`, exact documented candidate with a straight-versus-curly apostrophe implementation gap
- #49 `no-em-dashes`, challenged by the source's occurrence-versus-density and human-use cautions
- #52 `sentence-length-variance` and `paragraph-length-uniformity`
- `formulaic_parallelism`, `semantic_redundancy`, `underspecified_language`, and `faux_specificity` agent assessments
- `overall-signal-stacking` and the project-wide no-authorship boundary

## Associated hypotheses

- H3 drop detection framing entirely
- H4 single-source registry and traceable source attribution
- H9 field-guide voice with similar-species disambiguation per pattern
- H10 user-reported false-positive intake
- H11 manufactured insight is register-coded in long-form essay
- H12 genre-aware threshold calibration
- H21 low information density and wrong sentence subject
- H22 long-tail compression and grammatical standardisation
- H24 register-specific vocabulary density
- H25 model-family versus generic-AI residue

## Questions / follow-up

- Should Guo's human-look-alike and all-tells-can-be-human cautions be named in the #49 and field-guide disambiguation evidence, pending matched evaluation rather than a severity change?
- Should the exact #22 implementation gaps for Guo's two catalogued opener phrases receive focused fixtures before any regex expansion?
- Should the current Guo row in `pattern-opportunities.md` be replaced with a claim-keyed resolution that corrects the #42 overstatement and records the additional exact mappings and non-promotions?

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none recorded; Jina capture extracted 2026-05-05 | `snapshots/archive/guo-field-guide-ai-slop/2026-05-05-c53a62d4.md` | 2026-05-05 | `c53a62d4a58214bf7b119eb60364a32645ecb4f088bee17999f445f2ec0957f9` |
| current | Substack post 176806840 | `snapshots/guo-field-guide-ai-slop.md` | 2026-07-15 | `258d51d673320ec94c6768983d3714a56c6c5e7a3f8a4015e3adceace2717497` |

The prior card recorded no snapshot digest or stable identifier. Its snapshot bytes were therefore hashed before replacement, matched a fresh current Jina retrieval byte-for-byte, and were archived exactly. The direct first-party API shows the same publication and update timestamps as the current page. No substantive article-body change was identified; this update repairs the record by restoring all 13 headings and footnote 5, removing share chrome, adding complete provenance, preserving and transcribing figures, and formalising the full claim and coverage inventory.

## Decision history

- The 2026-05-05 card had no claim IDs, user-decision states, implementation states, snapshot digest, or recorded stable identifier. Its unkeyed #29, #30, #31, #42, #51, #52, low-information, and emoji mappings and its low-information follow-up question had no recorded approval and are superseded by C01-C30 below.
- The former #51 mechanical repeated-start mapping is retired because the source discusses repeated structure, sentence length, paragraph rhythm, tense, and point of view, not repeated sentence starts. The former categorical #42 confirmation is corrected: `no-dramatic-transitions` directly covers two examples, while #42's documentation and live candidate set include the straight-apostrophe “But here's the thing” but fail to match Guo's curly-apostrophe form because candidate matching does not normalise apostrophe typography.
- No product implementation is attributed to the prior card. All current recommendations are reset to `pending` for Mae's decision; C07 and C24 are marked `review required`, and all others are `not started`.
- C11 approved 2026-07-17: #42 `no-manufactured-insight` now matches the curly-apostrophe "here's the thing" form (commit 61360d6), closing the typographic-normalisation challenge.
- C13 approved 2026-07-17: the two catalogued implementation misses, "As technology continues to evolve" and "In today's fast-paced world", now fire on #22 `no-filler-phrases` (commit 9c7f3b8). All other rows remain pending.
- C15 approved 2026-07-19 via DR-19C: #31a now counts each contiguous stylized Unicode letter run as one candidate and counts `×` as a decorative-symbol candidate. Ordinary Markdown bold and italics remain outside the check.

## Project coverage

This is the authoritative review table. The focused checker results below are deterministic surface-only outputs and are not complete human-eyes Audits. The ukulele passage was tested exactly as printed. Other focused fixtures were constructed from source-derived phrases for diagnostic purposes; they are not exact source samples, and no sentence-rhythm conclusion is drawn from their synthetic assembly or punctuation.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Guo reports encountering disconnected-but-polished comments, clickbait/meandering blogs, plausible long-form “slop,” and unusually fast verbose coworker messages. | Direct practitioner observation; no count, sampling frame, labels, model versions, or human comparison. | H3 and the project evidence boundary provide framing; not covered as an executable claim. | No reproducible observation set or provenance test. | Record only as dated context; do not promote to a pattern or authorship rule. | pending | not started |
| C02: Cited Graphite/Axios, Originality, Slack, and AP-NORC materials are used to suggest high AI-article and workplace-use prevalence. | Indirect cited claims; the preserved Axios image says 65,000 English articles and ends May 2025 at 52% AI-generated, while the other linked studies were not directly reviewed here. | No live prose check depends on these values; H3 separates prevalence from pattern evidence. | Methods, labels, model/date definitions, and direct primary review are absent from this record. | Do not promote; ingest each upstream source separately before any project use. | pending | not started |
| C03: The source-labelled AI ukulele passage bundles bold header/list labels, four emoji-led steps, five em dashes, generic advice, triads, a not-X-but-Y conclusion, and a universal closing metaphor. | Direct illustrative example, but model, prompt, date, generation record, and selection method are unspecified. | Partly covered. Exact surface-only run: `no-em-dashes` 5 and threshold met; `no-unicode-flair` 4 and met; `no-boldface-overuse` 5 and met; `no-negative-parallelisms` 1 and met; `no-forced-triads` 1 and met; one tidy-ending candidate below its 3-candidate threshold. | `no-excessive-lists` does not recognise emoji-led paragraphs without Markdown list markers; no complete agent assessment was run, and surface output is not an Audit. | Preserve as a bounded practitioner example and possible future fixture only after adding legitimate professional-list, quotation, and human social-post controls. | pending | not started |
| C04: Academic words such as “delve,” “unpack,” “ascertain,” and “multifaceted” are yellow flags, not conclusions, because professionals also use them. | Direct practitioner qualification with one consulting-email look-alike; no frequencies. | Fully covered in principle by #7 clustering, its single-word warning, H24 register calibration, and `overall-signal-stacking`. | Guo is not named in the live evidence note, but behavior already requires clustering and structural combination. | Record as a disambiguator; take no product action without source-attribution work under H4/H24. | pending | not started |
| C05: Error-free spelling and grammar can result from Grammarly or spell-check rather than full AI generation. | Direct red-herring argument; no measured error rates or tool study. | Not covered as a positive check, which is appropriate; the project has no typo-absence rule. | Existing secondary notes could still imply “machine cleanliness” if not source-checked. | Explicitly do not promote typo absence; record as a human/tool look-alike. | pending | not started |
| C06: Avoided contractions can result from superficial editing or English-language-learning history rather than AI generation. | Direct red-herring argument; no language-background sample. | Not covered as a positive check, which is appropriate; no contraction-absence rule exists. | Human and second-language look-alikes make a generic rule unsafe. | Explicitly do not promote contraction absence; use only as false-positive context. | pending | not started |
| C07: Em dashes are a practitioner tell, but human columnists use them and a single occurrence is not conclusive; Guo later says intention, sparing use, and repetition are the meaningful distinction. | Direct observation and qualification; claims about rarity in human day-to-day writing are unmeasured. | Challenges current behavior. #49 documents a density/intention caveat but `check_em_dashes` fails on any U+2014 and labels it a strong warning; the ukulele sample's five occurrences are recognised. | Catalogue prose says one or two can be fine while the implementation has an any-occurrence threshold. | Add this source to pending #49 occurrence-versus-density evaluation and disambiguation; do not change severity from practitioner evidence alone. | pending | review required |
| C08: The linked “Em Dash Conspiracy” is described as top-1000 Reddit data showing em-dash use roughly tripling over a year, with correlation not causation. | Indirect implementation checked at commit `e40a2fb`. README warns of recent-post underrepresentation. Code filters empty/removed self-text, groups monthly, uses two-month rolling means, excludes January 2025, and plots May-December 2024. Raw retained totals across the six displayed subreddits are 489-965, with varying monthly denominators. | Not used by the live checker as a threshold; #49 has no source-bound Reddit calibration. | The article overstates the displayed range as a year; the analysis measures post occurrence only, has top-score/time/composition confounds, no uncertainty, and no AI labels. | Record the correction and do not promote the chart as authorship, causality, or threshold evidence. | pending | not started |
| C09: Parallelism is legitimate rhetoric, but repeated reflexive use can substitute form for information; single occurrences are forgivable in context. | Direct practitioner observation with human-use and frequency qualifications; no rate. | Partly covered by `formulaic_parallelism`, #9 `no-negative-parallelisms`, #10, and the project rewrite process, all of which retain context or density controls. | No measure of non-informative function; `formulaic_parallelism` remains agent-assessed. | Record as rationale for the existing contextual review; no new check. | pending | not started |
| C10: “Fast, efficient, and reliable” and “Think bigger. Act bolder. Move faster.” illustrate snappy three-beat cadence. | Direct examples; no provenance or frequency. | Fully covered at the candidate level by #10 and at 4+ candidates in 300+ words by #10a. A constructed source-derived diagnostic recognised one grammatical triad; its synthetic assembly cannot establish staccato or sentence-length behavior. | Candidate occurrence is not misuse and no source threshold exists. | Add Guo as practitioner example provenance for #10 only; retain human-rhetoric controls. | pending | not started |
| C11: “Something shifted,” “Everything changed,” and “But here’s the thing” illustrate unearned profundity or abrupt narrative turning. | Direct examples; no provenance or rate. | Partly covered. A constructed source-derived diagnostic made #32 `no-dramatic-transitions` meet threshold on the first two. The live #42 documentation and candidate set include straight-apostrophe “But here's the thing,” but Guo's curly-apostrophe form did not match. | Candidate matching lacks apostrophe normalisation, so the documented exact #42 phrase has typographically inconsistent behavior. The current Guo triage row also overstates categorical confirmation. | Replace the triage mapping with #32 direct coverage and a #42 typographic-normalisation challenge; test matched straight- and curly-apostrophe fixtures before any implementation decision. | approved | implemented |
| C12: “But now?” and “The solution?” followed by immediate answers illustrate mid-sentence question templates. | Direct examples with the source's single-instance/context caution. | Fully covered by #29. Exact surface-only run recognised both candidates and met the two-candidate threshold. | No material gap; teaching, interview, comic, and deliberate-argument controls remain necessary. | Retain #29 mapping and add the source's frequency/context qualification. | pending | not started |
| C13: “As technology continues to evolve,” “In today’s fast-paced world,” and “At the end of the day” illustrate vapid transitions; footnote 3 says Guo uses this pattern himself. | Direct examples plus an explicit human look-alike; no rate. | Partly covered and challenges documentation. #22 catalogue prose names all three, but the exact surface-only run matched only “At the end of the day”; #50 did not supply the missing exact coverage. | Two catalogued examples are implementation misses; human use argues for contextual handling. | Add focused fixtures for the two misses and matched human controls before deciding whether to change #22. | approved | implemented |
| C14: Mechanical bolding that does not mark key points is a possible formatting tell. | Direct practitioner observation; no corpus or threshold. | Partly covered by #13, which counts four or more Markdown bold spans. The exact ukulele passage produced five; a separate constructed source-derived diagnostic with four injected bold spans also met the accumulation threshold. | The check cannot judge whether emphasis is semantically mechanical, the source offers no threshold, and the constructed fixture is not evidence that Guo bolded those phrases. | Record as practitioner rationale for contextual review around #13; retain the live accumulation threshold and definition-header controls without treating the count as a semantic judgment. | pending | not started |
| C15: Stylized Unicode bold/italic letters, arrows, and multiplication signs can look machine-formatted, with an explicit non-English/social-platform human-use caveat. | Direct practitioner observation and human look-alike; no frequencies. | Covered by #31a: each contiguous stylized-letter run is one candidate, while arrows, `×`, and the existing decorative symbols count individually. | None for the approved surface family. | Add the missed stylized-letter runs and `×` to programmatic #31a without treating ordinary Markdown emphasis as Unicode flair. | approved | implemented |
| C16: ChatGPT often turns prose into lists; Guo speculates that RLHF ratings reward structured answers. | Behavior is direct observation; the RLHF explanation is explicitly speculation and uncited. | Partly covered by #31, which needs 30% list-line ratio or 8 items across 2 blocks and has recipe/technical context gates. | The source provides no mechanism evidence or threshold; emoji-led non-list paragraphs are outside #31. | Retain #31 as context-sensitive listification coverage; do not promote the RLHF causal explanation from this source. | pending | not started |
| C17: Emoji-led bullets are especially suspicious in professional contexts; Guo anecdotally sees more in GPT-4o than predecessors or GPT-5 and less in Claude, possibly because of system prompts. | Direct dated anecdote with explicit system-prompt confounding; no sample or prompt set. | Formatting is fully covered by #31a at two symbols and the marketing/email genre branch. Model comparison is not covered; H25 tracks version-specific residue. | No model-version, prompt, date, or frequency controls. | Keep model comparison as H25 context only; do not generalise to model attribution. | pending | not started |
| C18: Repetitive structure, similar sentence lengths, repeated paragraph rhythm, and unvarying cadence can make prose feel mechanical. | Direct subjective observation; the Gary Provost image is cited human craft guidance, not AI measurement. | Partly covered by #52 sentence-length SD under 4 for eligible prose, paragraph CV at 7+ substantial paragraphs, `structural_monotony`, and `tonal_uniformity`. | The project metrics cover only coarse length/arc/register proxies and the source supplies no threshold or human baseline. | Record as practitioner rationale; retain H12/H22 matched-register evaluation before changing metrics. | pending | not started |
| C19: Creative writing varies structure, tense, and point of view, whereas LLM prose may stay in one lane with unnatural consistency. | Direct practitioner generalisation; no corpus, model version, or counterexample set. | Partly covered in #41 fiction description (“locked POV with no pressure”) and tonal/structural assessments; the executable fiction watchlist does not name tense or POV as a distinct item. | Stable POV can be correct craft; cross-genre and deliberate-style controls are absent. | Track as a fiction/manual evaluation candidate under H12/H22, not a generic violation. | pending | not started |
| C20: Four ChatGPT metaphors are plausible but generic; Guo contrasts them with human metaphors grounded in personal experience or shared culture. | Direct source-supplied outputs without prompt/model version; human comparison is interpretive. | Fully covered as an agent-assessment concept by #30 `generic_metaphors` and #36 `faux_specificity`; two exact Guo examples already appear in live #30 catalogue prose. Surface-only output cannot evaluate genericity. | Live catalogue lacks explicit Guo attribution and the claim is not an empirical human/AI distribution. | Correct source attribution in triage/source mapping; retain agent assessment and concrete-property controls, not a regex. | pending | not started |
| C21: Filler appears as an incoherent throughline or four sentences doing one sentence's work. | Direct practitioner observation; no measured examples beyond the description. | Partly covered by H21, `semantic_redundancy`, `underspecified_language`, `vacuous_connection`, #22 stock filler, and student-writing weak-reasoning review. | No general information-density measure exists; #22 is lexical rather than semantic. | Keep as H21 evidence and collect matched examples before deciding on agent-assessment or rewrite-only treatment. | pending | not started |
| C22: Guo calls polished, grammatical prose with little meaning an AI “signature,” while acknowledging that humans can also communicate badly. | Direct interpretation with an internal human counterexample; not validated. | Partly covered by H21 and #41 student surface-polish review; challenges the project no-authorship boundary if quoted categorically. | “Signature” can be misread as authorship proof and the source supplies no specificity estimate. | Paraphrase only as a craft-quality prompt; never promote the “signature” wording as provenance evidence. | pending | not started |
| C23: Guo says these patterns have “worked” countless times for spotting likely AI slop. | Direct personal claim; no preserved cases, ground truth, false-positive count, or method. | Not covered as validation; the project requires corpus and complete-Audit evidence for performance claims. | Entire validation chain is absent. | Record as practitioner experience only; take no product or evidence-tier action. | pending | not started |
| C24: Humans use the same devices; Guo argues good writers use them sparingly and intentionally while AI uses them indiscriminately, and attributes overlap to training on prominent long-form outlets. | Direct craft interpretation and training-data assertion; frequency/intention distinction is useful, but training composition and causal mechanism are unsupported here. | Partly covered by #10, thresholds, tolerance notes, genre gates, and `overall-signal-stacking`; the project already says clusters are not authorship proof. | Several live checks, especially #49, still act on occurrence; intention is not directly measurable by surface checks. | Use as a disambiguation and clustering rationale; do not promote the training-data explanation. | pending | review required |
| C25: The article categorically says AI detectors do not work and cause harmful false positives, citing MIT Sloan teaching guidance. | Indirect cited claim plus reported harm; the linked source is not directly ingested here and “do not work” is broader than a source-specific performance result. | Project H3, detector-bias sources, evidence-tier guidance, and no-authorship reporting already reflect uncertainty and harm. | No direct detector/model/domain/threshold evidence in Guo's article. | Retain as indirect motivation only; use directly reviewed detector sources for project claims. | pending | not started |
| C26: Guo predicts tells will weaken as models improve, public tell lists may train evasion, and five minutes of prompting can bypass any third-party detector. | Direct prediction and footnote assertion; no experiment, detector list, model versions, or bypass outcomes. | H24/H25 and adversarial detector-evaluation lanes cover drift conceptually; no live check treats the claim as measured. | “Any” detector and five-minute bypass are unsupported universal claims. | Record drift as a dated hypothesis; do not promote the universal bypass or training-feedback claims. | pending | not started |
| C27: Guo discloses using AI to ideate, restructure, draft, and edit, varying between developmental editor and proofreader, while worrying about stylistic fingerprints. | Direct personal workflow disclosure; no post-level intervention log or before/after text. | Not a prose-pattern check; adjacent to graduated provenance and closed-source preservation work. | Cannot attribute any article phrase to AI or quantify transformation depth. | Record as source provenance context only; do not infer authorship or contamination. | pending | not started |
| C28: Fear of AI accusation can make human writers avoid their own patterns, creating an authenticity feedback loop. | Direct practitioner reflection and personal harm account; no population study or causal design. | H3, H9, H10, and the no-camouflage/process guidance partly cover the risk. | No direct project output currently presents this source-specific feedback-loop evidence. | Add as framing/disambiguation evidence pending user decision; no detector behavior change. | pending | not started |
| C29: Guo recommends specificity rooted in particular knowledge and tangible experience, plus a consistent voice and point of view, rather than style camouflage. | Direct practitioner advice; the claim that AI struggles to replicate it is unmeasured. | Fully covered as editing guidance by #30, #36, `generic_metaphors`, `faux_specificity`, and the process requirement to preserve source facts and voice. | Advice can invite invented details if used outside the closed factual record. | Retain as source-grounded editing guidance only; require facts to come from the writer/source. | pending | not started |
| C30: The closing instruction says to use the guide carefully because a human may have written a text even when it has all the tells. | Direct explicit non-authorship boundary and counterexample. | Fully covered by the project evidence note, `overall-signal-stacking` guidance, process product boundary, and complete-Audit/report rules. | Guo is not presently named in the live disambiguation evidence. | Add Guo as source support for the existing no-authorship boundary; take no behavior change. | pending | not started |

## Recommendations

- C01: Record only as dated practitioner context.
- C02: Require separate direct ingestion of upstream prevalence sources before project use.
- C03: Preserve as a bounded possible fixture with legitimate controls; do not treat the surface result as a complete Audit.
- C04: Record as a #7/H24 disambiguator; no behavior change.
- C05: Explicitly do not promote typo absence.
- C06: Explicitly do not promote contraction absence.
- C07: Add to pending #49 occurrence-versus-density evaluation and disambiguation; do not alter severity from this source.
- C08: Record the repository-method correction; do not promote the chart as causal, authorship, or threshold evidence.
- C09: Retain existing contextual formulaic-parallelism review; no new check.
- C10: Add source provenance for #10 examples with human-rhetoric controls.
- C11: Correct triage to #32 direct coverage and a #42 apostrophe-normalisation challenge; test straight and curly forms before deciding on implementation.
- C12: Retain #29 with its contextual controls.
- C13: Add two focused #22 fixtures and matched human controls before deciding on implementation.
- C14: Retain #13's accumulation threshold and controls while keeping semantic mechanicality a contextual judgment.
- C15: Keep stylized Unicode letter runs and `×` in programmatic #31a; ordinary Markdown emphasis remains outside the check.
- C16: Retain context-sensitive #31 coverage; reject the uncited RLHF mechanism as evidence.
- C17: Keep model-specific emoji comparison under H25 only.
- C18: Keep as rationale for existing rhythm/structure reviews and H12/H22 evaluation.
- C19: Track as a fiction/manual evaluation candidate with deliberate stable-POV controls.
- C20: Correct Guo attribution for the exact #30 examples; retain agent assessment.
- C21: Keep as direct H21 practitioner evidence pending matched evaluation.
- C22: Use only as a craft-quality prompt; do not promote “signature” as provenance evidence.
- C23: Record practitioner experience without validation status.
- C24: Use as clustering/disambiguation rationale; reject unsupported training-causality inference.
- C25: Rely on direct detector sources for project claims.
- C26: Record drift as a hypothesis; reject the universal bypass claim as project evidence.
- C27: Record personal AI-use disclosure without phrase-level attribution.
- C28: Add as pending authenticity-harm framing evidence, not detector behavior.
- C29: Retain source-grounded specificity advice within the closed factual record.
- C30: Add Guo as support for the existing no-authorship boundary; no behavior change.

## Evaluation of approved changes

- C01: not applicable - recommendation pending; no product change requested.
- C02: not applicable - recommendation pending; no product change requested.
- C03: not applicable - recommendation pending; no product change requested.
- C04: not applicable - recommendation pending; no product change requested.
- C05: not applicable - recommendation pending; no product change requested.
- C06: not applicable - recommendation pending; no product change requested.
- C07: not applicable - recommendation pending; existing behavior requires review.
- C08: not applicable - recommendation pending; no product change requested.
- C09: not applicable - recommendation pending; no product change requested.
- C10: not applicable - recommendation pending; no product change requested.
- C11: passed - commit 61360d6 normalised apostrophe typography in #42; direct invocation of `check_manufactured_insight("But here’s the thing: nothing changed.")` returned `passed=False` with matches `here’s the thing:` and `but here’s` on 2026-07-17.
- C12: not applicable - recommendation pending; no product change requested.
- C13: passed - commit 9c7f3b8 added the two catalogued openers to #22; direct invocation of `check_filler_phrases` flagged "As technology continues to evolve" and "In today’s fast-paced world" on 2026-07-17.
- C14: not applicable - recommendation pending; no product change requested.
- C15: passed - DR-19C makes two stylized-letter runs, or one such run plus `×`, meet #31a's existing two-candidate threshold; one stylized word and ordinary Markdown emphasis pass.
- C16: not applicable - recommendation pending; no product change requested.
- C17: not applicable - recommendation pending; no product change requested.
- C18: not applicable - recommendation pending; no product change requested.
- C19: not applicable - recommendation pending; no product change requested.
- C20: not applicable - recommendation pending; no product change requested.
- C21: not applicable - recommendation pending; no product change requested.
- C22: not applicable - recommendation pending; no product change requested.
- C23: not applicable - recommendation pending; no product change requested.
- C24: not applicable - recommendation pending; existing behavior requires review.
- C25: not applicable - recommendation pending; no product change requested.
- C26: not applicable - recommendation pending; no product change requested.
- C27: not applicable - recommendation pending; no product change requested.
- C28: not applicable - recommendation pending; no product change requested.
- C29: not applicable - recommendation pending; no product change requested.
- C30: not applicable - recommendation pending; no product change requested.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `guo_source_record_reviewer`
- **Reviewer isolation:** fresh source-dedicated agent; one source only; not reused
- **Findings resolved:** four material findings and two completeness notes resolved; one residual wording contradiction resolved during focused re-check
- **Unresolved findings:** none
