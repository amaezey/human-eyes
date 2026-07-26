# Futurism: Sports Illustrated published articles by fake, AI-generated writers

## Metadata

- **URL:** https://futurism.com/sports-illustrated-ai-generated-writers
- **Author / owner:** Maggie Harrison Dupré / Futurism
- **Published:** 2023-11-27T12:15:54-05:00
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** Investigative journalism / provenance reporting
- **Evidence tier:** Journalism / reported cases
- **Review mode:** update
- **Stable identifier:** Futurism WordPress post 305766
- **Version / revision:** page metadata dateModified 2023-11-27T12:15:54-05:00; prior Jina Reader capture extracted 2026-05-05
- **Full-text status:** complete
- **Snapshot:** `snapshots/futurism-sports-illustrated-ai-writers.md`
- **Extraction method:** Direct canonical HTML fetched with curl 8.7.1, parsed at `article#post-305766 .content-wrapper` with Beautiful Soup 4.14.3, transformed to Markdown with html2text 2025.4.15, and checked against the rendered page; all six claim-bearing in-body figures and three directly linked Generated Photos assets used for TheStreet matches were preserved
- **Snapshot SHA-256:** `6487700832394b099a66832544f013ae4ae756a43a1357e462892f088adc4950`
- **Model / corpus scope:** Models and versions unknown. English-language product-review articles and author profiles published under Sports Illustrated and TheStreet brands in The Arena Group portfolio, observed through linked 2021-2023 archives and reported in November 2023. Futurism explicitly describes the Sports Illustrated buying guides as affiliate-monetised; it does not establish an affiliate mechanism for TheStreet. No enumerated corpus, denominator, generation artefacts, or human comparison is supplied.
- **Access limitations:** No article-body text is missing. Site chrome and the non-claim-bearing hero image binary were omitted; the hero credit and six claim-bearing figures were retained. Linked archives and cited reporting were not separately ingested as sources in this one-source refresh.

## Summary

This 2,043-word Futurism investigation reports that Sports Illustrated and TheStreet review pages used apparently fictitious author personas, biographies, and headshots traceable to an AI-face marketplace; that personas and bylines were replaced without adequate disclosure; and that the relevant Sports Illustrated content disappeared after Futurism contacted The Arena Group. The report combines linked profile and article archives, six screenshots, two anonymous sources involved in the content, an on-record Arena Group response, and Futurism's interpretation. One anonymous source alleged that at least some article text was AI-generated, while Arena and contractor AdVon denied that allegation and said the articles were human-written and edited. The disagreement, absent model or corpus details, and isolated prose examples make this strong case-level provenance evidence but not reusable sentence-level authorship evidence.

## Main insights

- The strongest direct evidence concerns provenance: apparently nonexistent bylines, specific synthetic-headshot matches, invented biographies, silent persona rotation, silent byline reassignment, third-party production, and incomplete disclosure.
- The article preserves a material contradiction. A source involved in content creation said at least some articles were AI-generated; Arena relayed AdVon's denial and said writers used pseudonyms for privacy. The report does not independently resolve the text-generation question.
- Sports Illustrated removed the relevant authors and articles after Futurism's questions; Arena said it ended the AdVon relationship. Removal is evidence of a publication response, not proof of how the prose was produced.
- Two quoted article examples and one screenshot show awkward wording, sweeping unsupported assertions, and repeated list numbering. They are case examples without a systematic sample, human baseline, model/version, or prevalence measure.
- Futurism explicitly disclosed its parent Recurrent Ventures' prior and current AdVon relationships. That conflict/provenance disclosure is part of the evidence record.
- Cited claims about Men's Journal, CNET, Bankrate, G/O Media, BuzzFeed, Gannett, and Arena CEO Ross Levinsohn's earlier quality-over-volume position are indirect here and require their own direct-source reviews before they support separate project conclusions.

## Evidence and claims to extract

- **Direct source reviewed:** The complete current canonical page for Futurism WordPress post 305766, with JSON-LD `dateModified` 2023-11-27T12:15:54-05:00, 44 non-empty body text blocks, two blockquotes, and six in-body figures; the archived 2026-05-05 Jina Reader capture was compared with the current direct-HTML extraction.
- **Method and sample:** Futurism linked archived Sports Illustrated and TheStreet profiles and articles, matched profile images to Generated Photos listings, quoted two anonymous people involved in content creation, obtained a post-publication Arena Group statement, and reproduced six screenshots. The article names Drew Ortiz, Sora Tanaka, Domino Abrams, Denise McNamara, and Nicole Merrifield but gives no total sample, search protocol, model, version, detector test, or systematic human comparison.
- **Direct versus cited evidence:** C01-C11 and C15 report the investigation's observations, interviews, response, screenshots, or interpretations. C12-C13 and C17 repeat linked reporting or a cited interview and remain indirect in this record. C14 is the author's normative synthesis. C16 is this review's evidence-boundary assessment.
- **Important limits and counterexamples:** Arena/AdVon denied AI-generated article text while acknowledging third-party content and pseudonyms; the article's anonymous sources are not named; “doesn't seem to exist” is an investigation finding rather than proof of nonexistence; no generation artefacts or forensic method are supplied; the prose examples are isolated; and Futurism disclosed a parent-company relationship with AdVon. No claim can establish authorship from prose alone.

## Skill-use audit

- **Good use:** Support #41 journalism review for byline, bio, headshot, archive history, silent reattribution, vendor/affiliate provenance, disclosure, source conflict, and link verification.
- **Misuse / overclaim:** Do not state as settled fact that AdVon generated the article text, treat content removal as proof, or infer AI authorship from the two prose examples or one formatting failure.
- **Unsupported use:** The source supplies no lexical, rhythm, punctuation, sentence-length, vocabulary, detector-threshold, model-family, or aggregate prevalence evidence.
- **Underused evidence:** The current #41 branch covers most provenance categories but does not explicitly distinguish protected anonymous sourcing from vague attribution, ask whether silent byline reassignment has an editor's note, or require conflict-of-interest disclosure review.
- **Patterns left on the table:** Contextual handling for anonymous sources, explicit byline-change history, correction/editor-note checks, and publisher/reporter vendor relationships. These are manual journalism-review candidates, not regex rules or authorship signals.

## Matched patterns / rules

- `human-eyes/scripts/judgement.json` record `genre_specific`, journalism sub-record: partly or fully covers unsupported claims, sourcing, byline/bio/headshot verification, broken links, unverifiable quotations, vendor/affiliate provenance, and non-disclosure.
- `human-eyes/scripts/patterns.json` `_meta.evidence_body` and generated `human-eyes/references/patterns.md` cite this article for #41 fake bylines, fake bios, AI headshots, affiliate-review provenance, undisclosed generated content, and byline laundering. The “undisclosed generated content” phrase needs a disputed-claim qualifier.
- `human-eyes/references/sources/pattern-opportunities.md` promotes Futurism under source-grounding, fact-checking, and claim verification for #41 journalism/academic manual checks.
- `human-eyes/references/process.md` product boundary correctly prevents provenance findings from becoming authorship claims.
- No deterministic check establishes any of C01-C17. A surface-only grader result would not be a complete Audit and is unnecessary for the source's manual provenance claims.

## Associated hypotheses

- H12, genre-aware threshold calibration, supports keeping journalism provenance review separate from generic prose thresholds; this source does not test H12's threshold claim.
- Proposed evaluation question: can reviewers reliably distinguish legitimate protected anonymous sourcing from unsupported vague attribution while still detecting undisclosed vendor and byline provenance?

## Questions / follow-up

- Mae must decide whether to qualify the live `patterns.json` / generated `patterns.md` description so reported but disputed AI-generated article text is not presented as settled.
- Mae must decide whether to test additions to #41 for editor-note/byline history, conflict disclosures, and contextual anonymous-source handling.
- Direct ingestion of the linked archives or other publishers' incidents is separate work if those inherited claims are to support project decisions.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none recorded; snapshot hash 14cec391 | `snapshots/archive/futurism-sports-illustrated-ai-writers/2026-05-05-14cec391.md` | 2026-05-05 | `14cec39176eb85fb45ee40b6962f7ba155be3fdff8cdf1d30973732428e82f07` |
| current | Futurism WordPress post 305766 | `snapshots/futurism-sports-illustrated-ai-writers.md` | 2026-07-15 | `6487700832394b099a66832544f013ae4ae756a43a1357e462892f088adc4950` |

The prior 102-line Jina Reader capture and current direct-HTML capture contain the same 44 substantive text blocks. The refresh removes newsletter chrome, fixes extraction-time spacing defects, adds complete current provenance and structural verification, and preserves all six claim-bearing figures locally. No substantive article paragraph was added, removed, or corrected between the compared captures.

## Decision history

- C02, C07, C08, C15 approved 2026-07-26 via DR-27: Mae queued this work for later rather than ruling on its shape now. No checker, registry, or test change has been made and implementation has not started.
- The 2026-05-05 legacy card had no claim IDs, user-decision fields, or implementation statuses. Its broad #41/H12 provenance mapping is retained but decomposed into C01-C17. All recommendations are pending because no prior claim-keyed approval can be reconciled.
- C10 approved 2026-07-17 by Mae under decision-register row DR-111: five items were added to the #41 journalism watchlist in the `genre_specific` record of `human-eyes/scripts/judgement.json` (commit 88a04bb), including correction history, suspiciously uniform or too-perfectly placed quotes, repeated stock names and uniform titles, scene-setting openings that omit basic context, and human look-alike guards. The C10 boundary stands: the volleyball line, finance claims, and list-numbering screenshot are not promoted as AI-writing evidence. All other rows remain pending.

## Project coverage

This is the authoritative review table. Every recommendation is pending except C10, approved and implemented 2026-07-17 under DR-111.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Futurism found no external presence or publishing history for Drew Ortiz and matched his Sports Illustrated headshot to an AI-face marketplace listing. | Direct case-level reporting backed by linked archive and preserved screenshots; “doesn't seem to exist” is appropriately qualified and is not universal proof. | #41 journalism byline, bio, and headshot verification; fully covered as a manual review prompt. | No deterministic verification and none is warranted from one case. | Retain as case evidence for #41; verify with current and archived profiles in use. | pending | not started |
| C02: A protected anonymous source involved in the content said there were many fake authors and described fabricated bios. | Direct interview evidence, but the source is unnamed and no count or sampling frame is supplied. | #41 checks vague sourcing and unverifiable quotes; partly covered because legitimate protected anonymity needs contextual handling. | The live prompt could overflag responsible anonymous sourcing or understate its evidentiary limit. | Test contextual guidance that distinguishes explained protected anonymity from empty authority phrases; do not add a regex. | approved | not started |
| C03: A second protected anonymous source said at least some article text was AI-generated. | Directly reported allegation from an involved source; disputed by Arena/AdVon; no generation artefact, model, detector method, or count. | challenges current behaviour: #41 supports claim and source review, but the live evidence sentence presents “undisclosed generated content” without the dispute. | The catalogue evidence wording exceeds the source while the manual prompt cannot resolve authorship. | Qualify the catalogue evidence sentence as a reported but disputed allegation; make no authorship rule. Rejected 2026-07-26 (DR-140): Mae left the catalogue sentence as it stands, so undisclosed generated content is still listed alongside the five verified findings. The dispute is recorded here: the claim rests on one protected anonymous source and Arena Group and AdVon denied it. | rejected | not applicable |
| C04: The relevant Sports Illustrated personas and articles disappeared after Futurism contacted Arena. | Direct temporal observation reported by Futurism; removal does not prove why the content was created. | #41 fake or disappearing bylines; fully covered manually. | Removal could be misread as proof of generation. | Retain with the explicit non-causal qualification and archived-link check. | pending | not started |
| C05: Arena said the product reviews were licensed from AdVon and human-written and edited; that AdVon used counter-plagiarism and counter-AI software; that pseudonyms protected writer privacy; and that Arena continually monitored partners, was already reviewing AdVon, removed the content, and ended the partnership. | On-record counterstatement reproduced in full; it acknowledges third-party production and pseudonyms while denying AI-written text. Its workflow and software assertions are Arena/AdVon claims, not independently verified results. | #41 vendor/affiliate provenance, disclosure, sourcing, and quote verification; fully covered. | The project should preserve both allegation and the complete denial rather than select one or treat claimed checking software as proof. | Retain as the counterevidence boundary; no product change beyond the C03 wording correction. | pending | not started |
| C06: Futurism said Arena's response did not address the apparently nonexistent personas and synthetic headshots. | Author analysis anchored to the response and screenshots; stronger for unresolved provenance than text generation. | #41 byline/bio/headshot verification; fully covered. | None beyond keeping persona evidence separate from prose authorship. | Record only; take no further product action. | pending | not started |
| C07: Personas were rotated and their articles silently reattributed; Sports Illustrated supplied no editor's note, while the reported TheStreet reattributions supplied no AI-use disclosure. | Direct archive comparison reported for both brands, with the editor-note finding stated only for Sports Illustrated; no full denominator. A later Sports Illustrated replacement had no headshot, and later TheStreet replacement bylines used profile pictures not found for sale on the identified marketplace, so successor personas do not all carry the same synthetic-headshot evidence. | #41 fake or disappearing bylines and live evidence-body “byline laundering”; partly covered. | The journalism watchlist does not explicitly ask for byline-change history, editor's notes, reattribution disclosure, or changed replacement evidence. | Test adding archive/byline-history and editor-note questions to #41 with legitimate correction and syndication controls. | approved | not started |
| C08: Sports Illustrated articles lacked AI or fictitious-author disclosure and later received only a third-party/editorial-involvement disclaimer; TheStreet reattributions were reported without AI-use disclosure. | Direct brand-specific page observations; only Sports Illustrated is reported to have gained the third-party disclaimer. | #41 combines generated or third-party content non-disclosure; partly covered because it does not distinguish brand, vendor, pseudonym, AI-use, or editorial-involvement disclosures. | The combined wording can collapse materially different disclosure types. | Add evaluation cases distinguishing vendor, pseudonym, AI-use, and editorial-involvement disclosures before changing guidance. | approved | not started |
| C09: Futurism reported fictitious personas, synthetic-headshot matches, deletion, and reattribution at TheStreet; its review title page still advertised deleted contributors and linked deleted profiles. | Direct case reporting with named profiles, archive links, and preserved screenshots; the stale directory is a concrete broken-link/provenance artefact. Later replacement bylines had profile pictures not found for sale on the identified marketplace, and this is not a systematic portfolio census. | #41 journalism provenance and broken-link checks; fully covered. | No project gap beyond retaining the replacement-state and sample-limit qualifications. | Retain as a bounded second brand example; take no further product action. | pending | not started |
| C10: The report quotes an awkward volleyball line and sweeping finance claims, and shows a five-item list numbered “1” throughout. | Isolated linked examples and one preserved screenshot; authorship allegation remains disputed and no human baseline or prevalence exists. | partly covered: #41 catches weakly sourced claims and provenance, while formatting checks do not specifically establish repeated-list-number errors. | These examples cannot validate a reusable style tell or authorship rule. | Use only as journalism fact/format QA fixtures if separately approved; do not promote as AI-writing evidence. | approved | implemented |
| C11: Futurism connects Sports Illustrated's affiliate buying guides, undisclosed provenance, accountability, and reader trust. | Sports Illustrated's affiliate mechanism and publication practices are observed; no affiliate mechanism is established for TheStreet, and trust/accountability effects are author interpretation without a reader study. | #41 vendor/affiliate provenance; partly covered. | The project can inspect provenance but cannot claim a TheStreet affiliate mechanism or measured trust effects. | Preserve as Sports Illustrated-scoped editorial rationale, clearly labelled interpretation; no product change. | pending | not started |
| C12: The article says an earlier Men's Journal AI health story contained errors and received a large correction. | Indirect claim through linked Futurism reporting not reviewed in this run. | #41 factual and correction checks conceptually cover it; partly covered because direct source coverage is not established here. | Separate source evidence is required. | Do not promote from this card; ingest the linked report separately if needed. | pending | not started |
| C13: The article cites CNET, Bankrate, G/O Media, BuzzFeed, and Gannett incidents involving errors, plagiarism, or poor generated copy, and says CNET corrected more than half its AI-generated articles. | Indirect synthesis of linked reporting; the “more than half” quantity and all heterogeneous publisher outcomes remain unverified in this record. | #41 and the separate Gizmodo/CNET card provide partial conceptual coverage; partly covered because they do not validate every incident or this quantitative claim. | Recursive evidence would blur source boundaries. | Keep as indirect context and require source-specific ingestion for any new claim. | pending | not started |
| C14: The author argues that undisclosed generated journalism is unethical and that publishers' AI experiments have repeatedly backfired. | Normative and generalising author interpretation based on reported cases, not an empirical rate or universal result. | `process.md` product boundary and #41 provenance review; fully covered as interpretation, not a rule. | None if directness stays explicit. | Record only; do not encode the universal or normative wording as a detector claim. | pending | not started |
| C15: Futurism discloses that Recurrent Ventures worked with AdVon in 2022 to distribute selected Recurrent-written content on third-party e-commerce platforms, currently tests commerce content internationally with AdVon for selected brands excluding Futurism, and has never published AdVon content on Futurism or other Recurrent sites. | First-party conflict/provenance disclosure within the source; all relationship and exclusion terms are publisher-reported. | partly covered: #41 covers vendor provenance but does not explicitly ask reviewers to inspect reporter/publisher conflicts. | Conflict-disclosure review is absent from the journalism watchlist. | Test a #41 conflict-of-interest disclosure prompt with normal corporate relationships and disclosed syndication as controls. | approved | not started |
| C16: The source cannot establish sentence-level AI tells, model attribution, prevalence, or authorship from prose alone. | Reviewer boundary derived from missing model/corpus/method data, disputed generation, isolated examples, and no human comparison. | challenges current behaviour: evidence-tier guidance and `process.md` enforce the boundary, but the live evidence sentence omits the disputed status of generated article text. | The catalogue wording remains inconsistent with the project's otherwise correct non-authorship boundary. | Enforce this boundary in the card and correct only the catalogue wording identified in C03 if Mae approves. Rejected 2026-07-26 (DR-140): the boundary stays on this card and the catalogue wording is unchanged, since C03 was not corrected. No authorship, model-attribution, or prevalence claim is drawn from this source. | rejected | not applicable |
| C17: Arena CEO Ross Levinsohn earlier told The Wall Street Journal that the company's AI effort was about quality rather than maximising output, saying “better is better.” | Indirect cited interview used as a publisher-position counterpoint; the Wall Street Journal source was not reviewed here, and the later reported practices test rather than verify that stated intent. | #41 can compare public claims with publication evidence; partly covered because this cited interview has no direct source record in this run. | The project must not treat a stated policy as proof of implementation or as direct Futurism evidence. | Keep as indirect counterexample context; ingest the cited interview separately before any policy-compliance conclusion. | pending | not started |

## Recommendations

- C01: Retain as manual #41 case evidence and require live/archive verification in use.
- C02: Test contextual anonymous-source guidance; do not add a regex.
- C03: Qualify the catalogue evidence sentence as “reported but disputed undisclosed AI-generated content”; make no authorship rule.
- C04: Retain disappearance evidence with a non-causal qualification.
- C05: Preserve the full Arena/AdVon counterstatement as the evidence boundary.
- C06: Record only; keep persona evidence separate from prose authorship.
- C07: Test #41 archive/byline-history and editor-note questions with legitimate controls.
- C08: Evaluate disclosure-type distinctions before changing guidance.
- C09: Retain as a bounded second brand example; take no further product action.
- C10: Use only as optional journalism QA fixtures; do not promote as AI-writing evidence.
- C11: Preserve the trust/accountability rationale as author interpretation; no product change.
- C12: Do not promote; ingest the linked Men's Journal report separately if needed.
- C13: Keep as indirect context; require source-specific ingestion for new claims.
- C14: Record only; do not encode the normative generalisation as a detector claim.
- C15: Test a conflict-of-interest disclosure prompt with legitimate controls.
- C16: Preserve the non-authorship boundary and align the C03 catalogue wording if approved.
- C17: Keep the cited quality-over-volume position as indirect counterexample context; require separate ingestion before a compliance conclusion.

## Evaluation of approved changes

- C01: not applicable - pending recommendation; no product change made.
- C02: not applicable - pending recommendation; no product change made.
- C03: not applicable - ruled 2026-07-26; no product change.
- C04: not applicable - pending recommendation; no product change made.
- C05: not applicable - pending recommendation; no product change made.
- C06: not applicable - pending recommendation; no product change made.
- C07: not applicable - pending recommendation; no product change made.
- C08: not applicable - pending recommendation; no product change made.
- C09: not applicable - pending recommendation; no product change made.
- C10: passed - commit 88a04bb (DR-111) added five journalism watchlist items to the `genre_specific` record and its embedded prompt line in `human-eyes/scripts/judgement.json`; `python3 -m unittest dev.evals.tests.test_judgement_json` passes on 2026-07-17. No AI-writing rule was made from the C10 examples.
- C11: not applicable - pending recommendation; no product change made.
- C12: not applicable - pending recommendation; no product change made.
- C13: not applicable - pending recommendation; no product change made.
- C14: not applicable - pending recommendation; no product change made.
- C15: not applicable - pending recommendation; no product change made.
- C16: not applicable - ruled 2026-07-26; no product change.
- C17: not applicable - pending recommendation; no product change made.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/review_futurism_si_final_once`; additional independent source-record reviewer: `/root/review_futurism_si_fast_once`; fresh focused re-reviewers: `/root/rereview_futurism_si_once` and `/root/rereview_futurism_si_final_once`. Initial reviewer `/root/review_futurism_si_once` was interrupted before findings after the author added three source-evidence attachments and was not reused.
- **Reviewer isolation:** fresh source-dedicated agent; one source only; not reused
- **Findings resolved:** All three findings from `/root/review_futurism_si_final_once`, all six findings from `/root/review_futurism_si_fast_once`, and all six findings from `/root/rereview_futurism_si_once` were resolved. The card now preserves the indirect Ross Levinsohn quality-over-volume counterpoint, complete Arena/AdVon workflow claims, the CNET “more than half” correction quantity as indirect, exact figure URLs, brand-specific affiliate/disclosure/editor-note scopes, successor-state limits, the stale TheStreet contributor-directory artefact, the complete Recurrent/AdVon relationship disclosure, and canonical coverage labels. `/root/rereview_futurism_si_final_once` verified C01-C17, the prior fixes, live project mappings, archive integrity, the current snapshot digest, and all nine attachment hashes and returned PASS with no findings.
- **Unresolved findings:** none
