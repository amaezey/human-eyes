# Eve Fairbanks: The Biggest Tell That Something Was Written by AI

## Metadata

- **URL:** https://www.theatlantic.com/technology/2026/05/how-to-tell-ai-writing/687345/
- **Author / owner:** Eve Fairbanks / The Atlantic
- **Published:** 2026-05-29
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** Journalism and editor essay with reported cases, personal writing-process anecdotes, one reproduced model interaction, and secondary reporting of two empirical studies
- **Evidence tier:** Journalism / reported cases
- **Review mode:** update
- **Stable identifier:** The Atlantic article 687345
- **Version / revision:** Current and previous reviews cover the published version modified 2026-05-29T17:08:00Z; current canonical and gift HTML were retrieved 2026-07-15
- **Full-text status:** complete
- **Snapshot:** `snapshots/fairbanks-atlantic-ai-writing.md`
- **Extraction method:** direct canonical and gift-link HTML fetched with `curl`; Python 3 and BeautifulSoup 4 used for DOM counts and text comparison; Markdown body retained from the prior verified extraction after the current rendered article matched it token for token
- **Snapshot SHA-256:** `e2fcd6ea012535eee831ba6f224590ff4ec534dec9123580bad3f6ee8f4a7db4`
- **Model / corpus scope:** The direct model example is labelled ChatGPT Pro, but the model name, version, interaction date, system prompt, complete conversation context, and sampling settings are not supplied. Broader direct observations concern unspecified AI-assisted English-language messages and submissions seen by one Johannesburg-based editor. The cited sycophancy study concerns advice and interpersonal-conflict tasks across 11 models, not finished-prose drafting. The cited vocabulary study concerns spoken English in YouTube academic talks and podcasts, not written prose.
- **Access limitations:** Both current Atlantic routes returned the complete server-rendered article. The snapshot omits page chrome, advertising, audio and sharing controls, author boilerplate, and a non-substantive lead illustration; its checked caption is recorded. No article-body text is omitted. The article's publisher policy supports only presumed human authorship, not independently verified provenance.

## Summary

Fairbanks argues that removable surface tics are less important than prose that has not undergone a writer's stopping, backtracking, premise-testing, and revision. The essay combines one editor's recent observations, personal anecdotes, links to reported cases, one reproduced ChatGPT Pro exchange, and secondary summaries of sycophancy and spoken-language-transfer studies. Its strongest contribution to human-eyes is a craft and evaluation frame for conceptual coherence and local repairability, plus a useful human-look-alike case against punctuation and rhetorical-form shortcuts. It supplies no verified submission corpus, prevalence estimate, authorship method, model metadata, controlled comparison, or threshold, so its broad claims remain journalism and interpretation rather than detector evidence.

## Main insights

- The source distinguishes removable public tells from distributed failures in premise, reasoning, facts, structure, diction, and tone.
- Mechanical cleanliness, even pacing, and a breezy-grandiose register are one editor's observations about submissions she inferred were substantially AI-assisted; the source supplies no counts, verification method, or comparison corpus.
- Writing friction can prompt a writer to revise a premise, abandon a draft, or withhold a message. The essay treats that process as part of thinking, not inefficiency to be cosmetically simulated.
- Fairbanks also says writing may become easy after the writer finds the right idea. Ease and fluency alone are therefore not adverse evidence; her distinction is between premature frictionlessness and ease after premise resolution.
- One ChatGPT Pro exchange shows a fluent metaphor being rationalised through successive prompts and then conceded when challenged. It is a qualitative example, not model-wide prevalence evidence.
- The article reports that sycophantic systems affirm users more than humans and that model-associated vocabulary may transfer into later spoken English. These are indirect claims whose direct papers have different task and register boundaries.
- The source itself contains 14 em dashes, two detected negative-parallelism candidates, three detected triads, 83 curly quotation marks, and ordinary uses of `renowned` and `crucial`. That makes it useful for contextual calibration, not verified authorship classification.
- The essay's claims that all substantially generated writing is incoherent, that AI cannot make human-like judgments, and that infiltration cannot be stopped are arguments or forecasts, not results established by its evidence.
- Valuing genuine confusion, doubt, and revision must not become guidance to invent errors, uncertainty, autobiography, or irregularity.

## Evidence and claims to extract

- **Direct source reviewed:** Current canonical and gift-link HTML for The Atlantic article 687345, published 2026-05-29 and still carrying publisher modification time `2026-05-29T17:08:00Z`; the complete body was compared with the preserved snapshot.
- **Method and sample:** Twenty-seven rendered paragraph elements including the deck, two editorial cross-links, and four poem-line elements; 10 body links; one block quote; one editor's submission observations; two AI-mediated message anecdotes; two autobiographical writing examples; one reproduced ChatGPT Pro exchange; and secondary reports of Cheng et al. and Yakura et al. No submission count, selection rule, verified provenance, model configuration, controlled comparison, uncertainty estimate, or direct written-language corpus is supplied.
- **Direct versus cited evidence:** C01-C13, C15-C16, and C18-C21 are Fairbanks's observations, examples, arguments, or forecasts. C14 reports Cheng et al., *Science* 391, eaec8352 (2026), DOI `10.1126/science.aec8352`; its structured abstract was checked for scope, but this card does not ingest the paper. C17 reports Yakura et al., arXiv `2409.01754v3`; its abstract was checked for spoken-English scope, but this card does not promote it as direct project evidence. Linked journalism, the X post, surveys, tutorials, and submission provenance were not independently substantiated here.
- **Important limits and counterexamples:** The article generalises from anecdotes and editorial judgments; its public-tell list supplies no rates or thresholds; its own edited prose triggers the named surface checks; the ChatGPT exchange lacks model/version and full context; the sycophancy evidence is conversational and interpersonal; the vocabulary evidence is spoken English; no null result or systematic counterexample set is reported; and the publisher's disclosure policy is not independent authorship proof.

### Deterministic coverage check

The checked input is the snapshot content between `## Full text` and `## Extraction verification`, excluding the two editorial `Read:` lines, with Markdown links reduced to visible text, `<br>` markers removed, and block-quote markers removed while preserving paragraph and poem-line boundaries. The UTF-8 body at `tmp/fairbanks-atlantic-body-from-snapshot-2026-07-15.txt` has SHA-256 `c48d86595a35556c7368a23f477bf05084eed7bc170fbcbab2dcfb6933dd9c8f`, 1,775 whitespace-delimited words, and 52 lines. Running:

```bash
python3 human-eyes/scripts/grade.py audit tmp/fairbanks-atlantic-body-from-snapshot-2026-07-15.txt --surface-only --format json
```

returns `coverage_mode: surface_only`, `audit_status: incomplete`, and seven flagged programmatic checks: `no-em-dashes` with 14 candidates; `no-negative-parallelisms` with two candidates; `no-forced-triads` with three candidates; `no-curly-quotes` with 83 glyphs across 45 candidate sentences; `no-promotional-language` for `renowned`; `no-significance-inflation` for `crucial`; and `overall-signal-stacking` at 5/4 from four negative-parallelism points plus one vocabulary point. One em dash occurs in the poem and one in the quoted vocabulary-study language; the remaining 12 occur in Fairbanks's prose. One triad is inside the cited word list and one is in the poem. This is deterministic surface coverage only, not a complete Audit or an authorship result.

The quoted tutorial form `It’s not X; it’s Y` is intentionally masked as quoted material by the audit pipeline, so it is not one of the two document-level candidates. A focused direct call to `check_negative_parallelisms` on that exact curly-apostrophe semicolon construction returns `passed: false`, `candidate_count: 1`, and match `It’s not X; it’s`. The live rule therefore recognises the named form outside quotation; the two body-audit candidates are separate, unquoted human-look-alike constructions.

## Skill-use audit

- **Good use:** Craft framing for premise-testing, conceptual coherence, local repairability, and genuine revision; a bounded qualitative metaphor-rationalisation case; public-tell/evasion context; and a human-look-alike case for register, quotation, density, and purpose controls.
- **Misuse / overclaim:** Do not cite the essay as empirical proof that substantially generated writing is always incoherent, uneditable, tonally uniform, or authored by a particular model. Do not treat Fairbanks's inferred submission provenance or The Atlantic's policy as verified authorship.
- **Unsupported use:** The source cannot establish punctuation, colon, paragraph-length, tone, metaphor, sycophancy, vocabulary, or signal-stacking thresholds. It cannot validate a detector, an authorship verdict, a causal model mechanism, current prevalence, or transfer from speech to writing.
- **Underused evidence:** The project does not directly assess whether a draft's premise, evidence, reasoning, structure, diction, and facts compose into a defensible whole, nor whether repair is local or requires rebuilding.
- **Patterns left on the table:** Premise revision or abandonment; local repairability; distributed cross-level failure; post-hoc justification across turns; blurred meanings of `writing tool`; and the risk that public cue removal optimises camouflage without improving thought.

## Matched patterns / rules

- **#9 / `no-negative-parallelisms`:** Named as a public tell and challenged by two detected deliberate-use candidates in the article.
- **#21 / `no-collaborative-artifacts`:** Covers fixed praise and agreement residue, but not premise-level sycophancy or user self-correction.
- **#30 / `generic_metaphors` and `underspecified_language`:** Relevant to the raccoon exchange as a qualitative semantic case, not a prevalence finding.
- **#34, #52, `paragraph-length-uniformity`, and `sentence-length-variance`:** Related to the editor's cleanliness, uniformity, and pacing observation but do not verify provenance or reproduce her submission judgment.
- **#35 / `tonal_uniformity`:** Related to the reported breezy-grandiose consistency, although hybrid register and register lock are not identical.
- **#41 / `genre_specific`:** Journalism review covers sourcing and factual support, but not conceptual coherence or local repairability.
- **#49 / `no-em-dashes`:** Named as a public tell and challenged by 14 occurrences in the presumed-human edited article.
- **`overall-signal-stacking`:** Flags the article at 5/4, reinforcing that the output describes accumulated writing signals rather than authorship.

## Associated hypotheses

- **H3:** The essay supports dropping authorship-detection framing for these craft judgments.
- **H9 and H12:** The article is a journalism-register look-alike case for em-dash and negative-parallelism interpretation, not ground-truth classifier evidence.
- **H21:** Low information density and weak reasoning overlap with Fairbanks's distributed-failure argument but do not capture premise validity or repair cost.
- **H24 and H25:** The reported vocabulary transfer supports time-, register-, and model-aware treatment and cautions against static blacklists.
- **Proposed hypothesis:** Conceptual coherence across premise, evidence, reasoning, structure, diction, and facts, assessed as text quality without provenance inference.
- **Proposed hypothesis:** Local repairability, assessed separately from coherence: whether bounded edits can fix the draft or whether the argument needs reconstruction.

## Questions / follow-up

- Whether to add the article to a journalism calibration corpus labelled `presumed human under publisher policy`, with licence and provenance review before committing text.
- Whether conceptual coherence and local repairability should become separate hypotheses, extend H21, or remain source-record concepts.
- Whether premise-level sycophancy belongs outside phrase-level #21 and requires writing-assistance evidence before product work.
- Whether #49 and `overall-signal-stacking` need journalism, quotation, poem, and publisher-typography controls.
- Whether to ingest Cheng et al. and Yakura et al. separately before using their findings for project changes.

## Update provenance

The source body and publisher modification timestamp are unchanged. This update archives the exact prior bytes, replaces the snapshot wrapper with current-template provenance and verification fields, expands the claim inventory, and re-runs live coverage. A changed retrieval date is not treated as a source revision.

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | The Atlantic article 687345 | `snapshots/archive/fairbanks-atlantic-ai-writing/2026-07-14-d172c568.md` | 2026-07-14 | `d172c568cb9a99c0bbe319623d3ac10e7569a355be646353015296e28a7925f0` |
| current | The Atlantic article 687345 | `snapshots/fairbanks-atlantic-ai-writing.md` | 2026-07-15 | `e2fcd6ea012535eee831ba6f224590ff4ec534dec9123580bad3f6ee8f4a7db4` |

## Decision history

- C12 rejected 2026-07-26 via DR-129: dev-file registrations; the queued Reinhart evaluation was delivered by DR-159 as #65, #66, and #67. No checker, registry, or test change was made.
- The previous reviewed record had C01-C11 at `pending` / `not started`; no recommendation was approved or implemented. Their evidence was materially unchanged and is remapped as follows: old C01 to current C04, old C02 to C05, old C03 to C08, old C04 to C09, old C05 to C10, old C06 to C12, old C07 to C14, old C08 to C16, old C09 to C15, old C10 to C17, and old C11 to C21.
- Current C01-C03, C06-C07, C11, C13, C18-C20 make previously implicit source material explicit. All current rows remain `pending` / `not started`; the refresh carries forward no approval.
- C05 approved 2026-07-17 (DR-117 component 2): commit fcdd906 adds the simultaneously breezy and grandiose tone as a named related cue in the `tonal_uniformity` prompt.
- C16 closed 2026-07-18 via DR-123 with no product change: the single collapsing-metaphor interaction remains a qualitative source example; no cross-turn assessment or general rule was added.

## Project coverage

This is the authoritative review table. Coverage and decision status are stated per row.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Two different people sent Fairbanks unusually polished messages in what she judged to be the same AI voice | Two personal anecdotes; AI use and shared voice inferred, not verified; no model, baseline, or comparison set | #35, H25, and journalism provenance review; partly covered | No evidence separates common tool use, editing, accommodation, or Fairbanks's perception | Record as provenance/craft context only; require source-verified, baseline-aware data before any voice-convergence claim | pending | not started |
| C02: People report distrust of generated writing while using it more in everyday communication, creating cognitive load for readers | Unspecified surveys, trend assertion, and a linked Koebler quotation; secondary and unquantified here | H3 and product-boundary guidance; partly covered | No named survey, rate, time series, or user study is reviewed in this card | Record the trust-and-uncertainty context; do not derive a prose check or prevalence claim | pending | not started |
| C03: AI-assisted writing is entering elite publishing spaces and editors face inferred-provenance submissions | Linked journalism plus one editor's observation; no direct review of the linked cases or verified submission sample | #41 journalism watchlist and source provenance guidance; partly covered | No submission count, verification method, current prevalence, or false-positive analysis | Keep as dated reported context; ingest linked incidents separately before using them as direct evidence | pending | not started |
| C04: Some submissions appeared perfectly clean, uniform in length, and evenly paced | Direct editor observation; recent unspecified submissions; no count, threshold, provenance verification, or matched human set | #34, #52, `paragraph-length-uniformity`, and `sentence-length-variance`; partly covered; the current body audit clears both metrics with paragraph-length CV 0.45 across 19 substantial paragraphs and sentence-length SD 12.6 | Metrics measure form, not cleanliness or provenance, and the source validates no threshold | Take no product action; require matched, register-controlled evaluation before any threshold or severity change | pending | not started |
| C05: A simultaneously breezy and grandiose tone can recur in inferred AI-assisted submissions | Direct qualitative observation; no operational definition, examples, corpus, rate, or model scope | #35 `tonal_uniformity` plus inflation families; partly covered | Hybrid register is not the same construct as register lock | Retain as a semantic research example only; test definition and inter-rater agreement before promotion | approved | implemented |
| C06: `Writing tool` spans minor assistance through full drafting, while competition and volume pressure encourage adoption within perceived professional boundaries | Author reports and interpretation, plus The Atlantic's stated disclosure policy; no adoption study or boundary taxonomy | Process, provenance, and disclosure guidance; partly covered | No graduated assistance metadata or tested policy model | Record the scope ambiguity; consider a separate provenance-policy decision without treating disclosure as a writing tell | pending | not started |
| C07: Smooth grammatical output can mislead skimming readers, and public tutorials remove familiar cues without fixing deeper problems | Author assertion and report that tutorials exist; no reader experiment or tutorial sample | Product boundary, #9, and #49; partly covered | No skim-versus-close-read comparison, evasion rate, or post-edit quality measure | Use as motivation for meaning-focused evaluation; require direct adversarial evidence before changing checks | pending | not started |
| C08: Em dashes are publicly recognised as an AI tell | Public-salience report without frequency evidence; current article contains 14 em dashes | #49 `no-em-dashes`; fully covered and challenges current behaviour | Any-occurrence warning creates false-positive pressure in edited journalism, quotation, and poetry | If approved, evaluate #49 on licensed journalism look-alikes by genre, quotation, density, and purpose before changing severity | pending | not started |
| C09: Colons are publicly recognised as an AI tell | One reported tutorial cue; no subtype, rate, model comparison, or human control | No general colon rule; not covered by design | Evidence cannot support a colon check or severity | Do not promote a general colon rule from this source | pending | not started |
| C10: Negative parallelism is publicly recognised as an AI tell, exemplified as `It’s not X; it’s Y` | Public-salience report; stronger sources exist; current article has two other detected candidates | #9 `no-negative-parallelisms`; fully covered and challenges current behaviour; a focused direct check recognises the exact semicolon form with one candidate, the full audit intentionally masks its quoted occurrence, and the body audit detects two separate unquoted human-look-alikes | Deliberate human use, quotation context, and cross-sentence forms need contextual interpretation | Use as a look-alike calibration case only; make no syntax or severity change from this card | pending | not started |
| C11: Generating prose to flesh out ideas can bypass part of the thinking performed during drafting, while writing may become easy after the right idea is found | Fairbanks's qualified craft argument; no controlled human, assisted, or model comparison | Rewrite/write process and meaning-preservation guidance; partly covered | No process measure distinguishes premature frictionlessness from ease after premise resolution or helpful assistance from premise substitution | Record the qualified process framing; never treat ease or fluency alone as adverse evidence; require direct writing-process studies before a product claim | pending | not started |
| C12: Drafting friction, doubt, and backtracking can expose a flawed premise or message that should be revised, discarded, or withheld | Two autobiographical examples and a craft argument, qualified by the source's statement that writing can become easy after resolving the idea; no measured comparison | Process safeguards and H21; partly covered | No assessment asks whether the premise survived challenge; coherence and repair cost remain distinct, and fluency alone cannot answer either | Decide whether conceptual coherence and local repairability belong as separate hypotheses; preserve the ease-after-resolution counterexample and do not infer provenance | rejected | not applicable |
| C13: Users say they want agreeable, compliant models, and Fairbanks predicts companies will not build systems that make human-like judgments | User-preference assertion plus Fairbanks's capability and incentive argument; the company forecast is not tested by the article | #21 and product-boundary guidance; partly covered | Phrase-level agreement residue does not establish user preference, capability, company incentives, or future design | Record the direct assertion and forecast separately; do not promote capability or inevitability claims | pending | not started |
| C14: In advice tasks, leading models affirmed users 49% more often than humans, and users preferred sycophantic responses | Secondary report of Cheng et al.; checked structured abstract covers 11 models, three datasets, three preregistered experiments, and 2,405 participants; tasks are interpersonal advice and conflict | #21 `no-collaborative-artifacts`; partly covered; the current body audit clears this fixed-phrase check | A clear phrase check does not assess premise-level affirmation; no finished-prose drafting condition | Ingest Cheng et al. separately and require task-matched writing-assistance evidence before premise-level product work | pending | not started |
| C15: Tone, diction, structure, missing reasoning, and facts may fail together, making local editing ineffective | Professional editor judgment and body analogy; no operational definition, sample, repair protocol, or comparison | #41 `genre_specific`, `generic_metaphors`, `underspecified_language`, `semantic_redundancy`, `referential_clarity`, H21, and `overall-signal-stacking`; partly covered; the surface-only audit flags signal stacking at 5/4, but no complete agent-assessed Audit was run | The aggregate check excludes factual support and does not measure coherence or edit cost; the named semantic registry checks operate separately | Prototype conceptual coherence and local repairability separately only after their product homes and success measures are approved | pending | not started |
| C16: A fluent metaphor can collapse under explanation while the model justifies it and later agrees with the user's rejection | One reproduced ChatGPT Pro interaction; model/version, date, full prompt context, and human comparison absent | #30, `generic_metaphors`, `underspecified_language`, and #21; partly covered | No cross-turn rationalisation assessment or prevalence evidence | Retain as a qualitative test case only; do not generalise beyond the interaction | approved | not applicable |
| C17: Words preferentially generated by ChatGPT increased abruptly in later spoken English | Secondary report of Yakura et al.; checked arXiv v3 abstract covers 740,249 hours, 360,445 YouTube academic talks, and 771,591 podcast episodes | #7, H24, H25, and source metadata; partly covered | The direct evidence is spoken English and does not establish written-prose direction, threshold, or causality for one text | Ingest Yakura et al. separately; require register-matched written corpora before changing written-prose vocabulary handling | pending | not started |
| C18: Humans may absorb model-associated language and cultural cues, making static public tells drift | Fairbanks's interpretation of the cited spoken-language result; plausible but not separately measured here | H24 and H25; partly covered | No written transfer study or update cadence for the project's word lists | Use as a drift warning; keep vocabulary claims dated and register-specific without changing product behavior from this card | pending | not started |
| C19: All substantially AI-generated writing is incoherent under close examination | Explicit universal author claim contradicted by the article's anecdotal evidence base; no systematic sample or null-result search | Product boundary and H3; challenges current behavior if treated as detector evidence | No prevalence, definition of substantial assistance, blinded rating, human control, or counterexample set | Record as unsupported overclaim and prohibit its use as source evidence for an authorship or universal-quality verdict | pending | not started |
| C20: AI-mediated communication will spread unstoppably, while human or older writing may become an artisanal or authenticated record | Forecast, analogy, and cultural framing; not a measured finding | H3 and provenance framing; partly covered | No forecast method, adoption data, authenticity method, or counterfactual test | Keep as framing only; take no product action | pending | not started |
| C21: Genuine confusion, doubt, internal struggle, and revision can carry meaning that polished generation erases | Craft argument, personal examples, and a final trade-off; no measured textual distinction | #35, #37, voice/process safeguards, and meaning preservation; partly covered and challenges guidance | Advice to insert a register break or imperfection can become cosmetic camouflage | Preserve genuine qualifications and revision history; review guidance only after evaluation and never manufacture irregularity | pending | not started |

## Recommendations

- **C01:** Record the message anecdotes as provenance/craft context only; require source-verified, baseline-aware data before any voice-convergence claim.
- **C02:** Record the trust-and-uncertainty context without deriving a prose check or prevalence claim.
- **C03:** Keep the publishing-space claim as dated reported context and ingest linked incidents separately before direct use.
- **C04:** Take no product action; require matched, register-controlled evaluation before threshold or severity changes.
- **C05:** Retain breezy-grandiose tone as a research example pending a definition and inter-rater test.
- **C06:** Record `writing tool` scope ambiguity and consider provenance metadata as a separate policy decision.
- **C07:** Use the camouflage argument as motivation for meaning-focused adversarial evaluation, not as direct check evidence.
- **C08:** If approved, evaluate #49 on licensed journalism look-alikes by genre, quotation, density, and purpose before changing severity.
- **C09:** Do not promote a general colon rule from this source.
- **C10:** Use the two detected unquoted instances as look-alikes and retain quotation masking for the recognised semicolon form; make no syntax or severity change from this card.
- **C11:** Record the qualified process framing, including that ease may follow premise resolution; never treat ease or fluency alone as adverse evidence.
- **C12:** Decide whether conceptual coherence and local repairability belong as separate hypotheses; preserve the ease-after-resolution counterexample, and let neither infer provenance.
- **C13:** Record the user-preference assertion and Fairbanks's company forecast separately without promoting capability or inevitability claims.
- **C14:** Ingest Cheng et al. separately and require writing-task transfer evidence before premise-level sycophancy work.
- **C15:** After C12, prototype coherence and repairability separately with blind ratings, matched samples, inter-rater agreement, overlap analysis, and false-positive review.
- **C16:** Retain the ChatGPT exchange as a qualitative test case only.
- **C17:** Ingest Yakura et al. separately and require register-matched written evidence before vocabulary changes.
- **C18:** Keep vocabulary sources dated and register-specific; make no product change from this interpretation.
- **C19:** Record the universal incoherence statement as unsupported and exclude it from authorship or universal-quality evidence.
- **C20:** Keep the artisanal-writing and inevitability forecast as framing only; take no product action.
- **C21:** Preserve real uncertainty and revision; never manufacture irregularity, autobiography, or error.

## Evaluation of approved changes

- C01: not applicable - pending recommendation; no product change requested.
- C02: not applicable - pending recommendation; no product change requested.
- C03: not applicable - pending recommendation; no product change requested.
- C04: not applicable - pending recommendation; no product change requested.
- C05: passed - commit fcdd906; test_judgement_json.py asserts the breezy-and-grandiose guidance is present in the tonal_uniformity prompt.
- C06: not applicable - pending recommendation; no product change requested.
- C07: not applicable - pending recommendation; no product change requested.
- C08: not applicable - pending recommendation; no product change requested.
- C09: not applicable - pending recommendation; no product change requested.
- C10: not applicable - pending recommendation; no product change requested.
- C11: not applicable - pending recommendation; no product change requested.
- C12: not applicable - rejected 2026-07-26 via DR-129; no product change implemented.
- C13: not applicable - pending recommendation; no product change requested.
- C14: not applicable - pending recommendation; no product change requested.
- C15: not applicable - pending recommendation; no product change requested.
- C16: not applicable - closed 2026-07-18 via DR-123; the qualitative interaction remains source-only and no cross-turn assessment was added.
- C17: not applicable - pending recommendation; no product change requested.
- C18: not applicable - pending recommendation; no product change requested.
- C19: not applicable - pending recommendation; no product change requested.
- C20: not applicable - pending recommendation; no product change requested.
- C21: not applicable - pending recommendation; no product change requested.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/fairbanks_review_2` (fresh source-dedicated re-review after `/root/fairbanks_review_1`)
- **Findings resolved:** Added the ease-after-premise-resolution counterexample; recorded exact live metric and check results; named the semantic registry coverage and incomplete-Audit boundary; separated user-preference assertion from Fairbanks's company forecast; and clarified through a focused direct check that the exact semicolon negative-parallelism form is recognised while its occurrence in the article is intentionally masked as quotation.
- **Unresolved findings:** none
