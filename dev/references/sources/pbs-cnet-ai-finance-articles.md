# Lauren Leffer / Gizmodo: CNET AI-generated finance articles

## Metadata

- **URL:** https://gizmodo.com/cnet-ai-chatgpt-news-robot-1849996151
- **Author / owner:** Lauren Leffer / Gizmodo
- **Published:** 2023-01-17T21:20:00+00:00; updated 2023-01-17T22:05:00+00:00
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** journalism / reported case and commentary
- **Evidence tier:** Journalism / reported cases
- **Review mode:** update
- **Stable identifier:** Gizmodo WordPress post 1849996151
- **Version / revision:** publisher `dateModified` 2023-01-17T22:05:00+00:00, retrieved 2026-07-17; prior 2026-05-05 snapshot archived by hash
- **Full-text status:** complete
- **Snapshot:** `snapshots/pbs-cnet-ai-finance-articles.md`
- **Extraction method:** direct canonical HTML downloaded with `curl`, primary article parsed with Python 3 and Beautiful Soup, and body and metadata compared with Jina Reader Markdown and publisher JSON-LD; raw HTML and lead image preserved
- **Snapshot SHA-256:** `9013ef1b01f20b5142e34d3aae9eb1cfa72e9f05958e88bda2a4d77c306db329`
- **Model / corpus scope:** CNET's late-2022 to January-2023 AI-assisted personal-finance explainers, including one compound-interest article; the article does not identify the AI engine, model family, model version, prompts, generation settings, or exact article dates beyond reporting more than two months of publication, 78 articles total, and up to 12 in one day; English-language US technology journalism
- **Access limitations:** none for the current Gizmodo article. The linked X record 1615364539083636742 exposed no recoverable post payload and is a bare link in the publisher HTML; no claim relies solely on it. The cited CNET compound-interest page is now substantially rewritten and retains only a summary correction, so the five original errors remain source-reported rather than independently reconstructed from the original CNET version. Cited CNET and Futurism pages were checked for attribution boundaries but are not recursively ingested here.

## Summary

Lauren Leffer's 17 January 2023 Gizmodo article reports that one CNET AI-assisted compound-interest explainer received at least five significant corrections, while CNET said every AI-assisted article had human editorial review. The 19-paragraph article also reports a 78-article, high-volume publishing experiment, changing byline disclosure, outside discovery of errors, a secondary accuracy review, and CNET's response. It contributes a dated journalism case about factual verification, correction history, disclosure, and editorial burden. It is not a controlled model study, a prose-style taxonomy, a prevalence estimate beyond the reported CNET set, or evidence for authorship inference.

## Main insights

- The article identifies five separate finance errors in one AI-assisted CNET explainer: two interest-calculation examples, CD compounding frequency, car-loan payments, and APR/APY conflation.
- CNET's public policy said AI-assisted drafts were reviewed, fact-checked, and edited by topical experts, yet the reported errors survived publication. A declared human-review step is therefore not evidence that every factual claim was verified.
- The source reports 78 AI-assisted articles over more than two months, up to 12 in one day, with disclosure initially behind a generic staff byline and later moved to a visible `CNET Money` byline statement.
- The source attributes discovery of some errors to Futurism and reports that CNET then added review notes and began a secondary accuracy review across its AI-assisted pieces.
- Leffer interprets generative editing as a different, high-attention task and connects volume, search optimization, and advertising incentives to editorial risk. Those workflow and business-motive claims are commentary, not measured causal results.
- The article supplies provenance and fact-checking context only. It names no reusable surface tell, model-specific writing habit, threshold, detector, comparison corpus, false-positive rate, or human-text control.

## Evidence and claims to extract

- **Direct source reviewed:** complete current Gizmodo post 1849996151, publisher modification timestamp 2023-01-17T22:05:00+00:00, with headline, deck, byline, lead image, 19 article-body paragraphs, 14 body links, CNET response, and update note; raw canonical HTML and lead image preserved.
- **Method and sample:** journalism based on Leffer's reading of one corrected CNET compound-interest article, linked Futurism reporting, CNET's public statement, byline/editor-note observations across CNET's reported 78-article set, and an emailed CNET PR response. There is no disclosed systematic sampling, raw dataset, archived article list, error-coding protocol, independent finance expert review, human comparison, or model/prompt metadata.
- **Direct versus cited evidence:** C07 and C11 include Leffer's page observations but their counts and scope are not accompanied by released data. C12 contains Gizmodo's direct outreach and CNET PR's quoted response. C02-C06 and C08 are reported through the cited CNET correction and Futurism reporting; the current CNET page corroborates broad savings/CD/loan corrections but not all original detail. C09 quotes CNET's directly linked policy statement, which remains accessible. C01, C10, C13-C15 contain reporter framing, interpretation, or boundary assessment rather than measured findings.
- **Important limits and counterexamples:** one publisher, one finance explainer for the enumerated errors, a short late-2022/January-2023 period, unnamed AI engine, no original output or complete before/after article pair, no audit of all 78 articles, no error prevalence, no comparison with human-written CNET articles, and no causal test of volume or incentives. The article itself contrasts CNET with the Associated Press's narrower template use, but that AP account is cited context rather than directly established here. Current CNET pages preserve human rewriting and correction evidence, not the complete original version.

## Skill-use audit

- **Good use:** support #41 journalism review for claim tracing, source checking, AI-assistance disclosure, byline provenance, correction notes, and the gap between a declared review process and verified factual accuracy.
- **Misuse / overclaim:** treating five errors in one article as an error rate for CNET, ChatGPT, an unnamed AI engine, all AI-assisted journalism, or current models; claiming that human review inevitably fails; inferring authorship from factual mistakes, generic bylines, or search-oriented subject matter.
- **Unsupported use:** lexical, punctuation, rhythm, tone, sentence-length, vocabulary, SEO-style, or detector thresholds; model-family attribution; a causal claim that advertising or publication volume produced the errors; an authorship verdict.
- **Underused evidence:** correction history and visible disclosure are useful provenance records, while `human-eyes/references/process.md` correctly warns that a prose Audit does not establish factual fidelity. The live #41 journalism branch covers traceability and disclosure but does not explicitly ask reviewers to inspect correction history or compare pre- and post-correction versions.
- **Patterns left on the table:** no prose pattern. A bounded future #41/process decision could add correction-history and before/after verification prompts, with ordinary human corrections and transparent AI assistance as controls.

## Matched patterns / rules

- #41 `genre_specific` journalism agent assessment in `human-eyes/scripts/judgement.json`: checks unsupported claims, verifiable links, bylines, dates, quotes, provenance, and undisclosed generated or third-party content.
- #41 catalogue text in `human-eyes/scripts/patterns.json` and `human-eyes/references/patterns.md`: asks whether journalism facts trace to named sources but does not make the source's correction-history comparison explicit.
- `human-eyes/references/process.md`: preserves facts, quotations, citations, names, dates, links, and qualifications; states that an Audit checks writing patterns and does not prove factual fidelity.
- `dev/references/sources/pattern-opportunities.md`: already lists Gizmodo/CNET under the promoted source-grounding, fact-checking, and claim-verification opportunity.
- Root `README.md` #41 evidence summary already uses Gizmodo/CNET for journalism provenance and correction history.

## Associated hypotheses

- None directly supported. The previous card mapped H12 `Genre-aware threshold calibration`, but this article contains no threshold, matched-register comparison, detector result, or prose-feature distribution. It remains useful genre context for #41, not evidence for H12.

## Questions / follow-up

- Can a complete archived pre-correction CNET article, its full correction notice, and the full 78-article list be preserved in separate source records if Mae wants error prevalence or before/after analysis?
- Should #41 journalism review explicitly ask for correction-history and pre/post comparison when a public correction exists, while treating corrections as evidence of a functioning process rather than an authorship cue?
- Should the process guide distinguish declared editorial review from completed source-by-source factual verification, without implying that AI-assisted material is uniquely or inevitably erroneous?

## Update provenance

The prior card and manifest recorded no snapshot SHA-256. Before replacement, the exact 6,521-byte working snapshot was hashed as `763294093845b9372b6231562186d82dcae0ced9ef281018c81b308a923f68ac`, verified byte-for-byte against the `c42b1457d81f` checkout's committed version, and archived without transformation.

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | Gizmodo WordPress post 1849996151; pre-contract capture | `snapshots/archive/pbs-cnet-ai-finance-articles/2026-05-05-763294093845.md` | 2026-05-05 | `763294093845b9372b6231562186d82dcae0ced9ef281018c81b308a923f68ac` |
| current | Gizmodo WordPress post 1849996151 | `snapshots/pbs-cnet-ai-finance-articles.md` | 2026-07-17 | `9013ef1b01f20b5142e34d3aae9eb1cfa72e9f05958e88bda2a4d77c306db329` |

## Decision history

- The prior card had no stable claim IDs, user decisions, implementation statuses, or approved product changes. It broadly mapped the article to #41, provenance residue, factual-error/correction-history context, and H12. This update retires the unsupported H12 mapping, separates the five error examples and the reporter's interpretations, and reopens all recommendations as `pending`. No earlier product approval or implementation is inferred.
- C08 and C09 approved 2026-07-17 by Mae under decision-register row DR-111: five items were added to the #41 journalism watchlist in the `genre_specific` record of `human-eyes/scripts/judgement.json` (commit 88a04bb). The correction-history question (does the outlet's correction record check out for this piece) implements C08, and with the human look-alike guard it directs reviewers to check the correction record rather than accept declared editorial review as verification (C09). Corrections stay review prompts, never accusations or authorship evidence. All other rows remain pending.
- C15 approved 2026-07-25 via DR-139: the H12 mapping is retired. `dev/hypotheses.md` does not cite this source, and the #41 provenance, fact-checking, and correction-history mapping stands.

## Prior-to-current comparison

- **Added:** current contract metadata, stable post identifier and modification timestamp, exact prior digest and archive, raw HTML and lead-image attachments, 19-paragraph structure verification, claims C01-C15, direct/cited/interpretive boundaries, live project comparison, pending decisions, and independent-review fields.
- **Corrected:** the old summary said the compound-interest article had to be corrected “after misstating the calculation,” which collapsed five reported errors into one. The refresh separates all five, distinguishes the CNET review-policy quotation from actual verification, and replaces the old unsupported H12 mapping with genre-context only.
- **Removed:** no substantive Gizmodo body text or reported incident. The inherited mention of an “original PBS/AP URL” is removed because the reviewed source is Gizmodo post 1849996151 and no PBS/AP source identity or failed URL was preserved in the old provenance.
- **Unchanged:** canonical Gizmodo identity, Lauren Leffer byline, 2023-01-17 publication date, journalism evidence tier, and use as provenance, correction, factual-verification, and editorial-process context rather than style evidence.

## Project coverage

This is the authoritative review table. The relevant live coverage is manual #41 agent assessment and closed-source/factual-preservation process guidance; no deterministic surface check claims to verify finance facts, correction history, or provenance, so no surface-only run is presented as coverage.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Leffer frames ChatGPT as capable of fluid prose while fabricating or bungling facts. | Reporter framing supported by linked examples, not a controlled or quantified model result; no model version, prompt, corpus, comparison, or error rate. | partly covered by #41 journalism's unsupported-claim and source-tracing prompts and by the process warning that prose Audit is not factual verification. | The project should not generalize this 2023 framing to all models or treat fluent prose as evidence of factual error. | **record only:** retain as dated rationale for separate factual verification; make no model-wide claim or checker change. | pending | not started |
| C02: The corrected compound-interest article reportedly treated a $10,300 ending balance as $10,300 of interest instead of $300. | Source-reported example attributed to CNET's correction through Gizmodo/Futurism; the current rewritten CNET page shows the correct $300 and $10,300 values but not the complete original wording. | partly covered by #41's fact/source tracing and process factual-preservation guidance. | Neither #41 nor any deterministic check performs finance arithmetic or compares corrected versions. | **test-adapt:** if correction-history review is approved, use this as a dated evaluation example with the archived original and legitimate arithmetic controls; do not create a prose tell. | pending | not started |
| C03: A second interest example reportedly repeated the first calculation error. | Source-reported but not reproduced or quoted in enough detail to independently reconstruct; no current original version preserved. | partly covered by #41's fact/source tracing. | The specific second example cannot be verified from this source record alone. | **record only:** preserve the reported second error as indirect and unresolved; require the original CNET version before using it in evaluation or guidance. | pending | not started |
| C04: The article reportedly said one-year CDs compound only annually, although CD compounding frequency varies. | Source-reported correction; the current CNET page retains a summary correction naming CDs and now discusses varying compounding frequencies. | partly covered by #41 fact tracing and current pattern-opportunities source-grounding context. | No runtime check verifies product-specific finance claims; a correction summary does not preserve the original sentence. | **test-adapt:** use only as correction-history/source-grounding context after the original version is preserved; no universal AI-error rule. | pending | not started |
| C05: The article reportedly miscalculated payments on a five-year car loan at 4 percent. | Source-reported correction; the current CNET page's summary names loan-payment errors but no longer preserves the original calculation. | partly covered by #41 fact tracing. | Exact principal, payment amount, formula, and original text are absent here, so independent arithmetic verification is impossible. | **record only:** retain the bounded reported error; require the original article before creating an evaluation case. | pending | not started |
| C06: The article reportedly conflated APR and APY and gave bad advice. | Source-reported correction without the original advice text; the current CNET article now distinguishes APY and compounding. | partly covered by #41 fact tracing and process source preservation. | The scope and consequence of the bad advice cannot be reconstructed from the current page. | **record only:** preserve as an indirect correction claim; do not infer a generic terminology tell or severity. | pending | not started |
| C07: CNET reportedly published 78 AI-assisted articles over more than two months, up to 12 in one day, first under `CNET Money Staff` and then `CNET Money`, with disclosure initially behind the byline description. | Journalism report combining page observations, linked reporting, and CNET's statement; no released 78-item inventory or date-by-date count in this source. | fully covered conceptually by #41's byline, provenance, and undisclosed-generated-content prompts; root README already cites Gizmodo/CNET for provenance. | The count and disclosure chronology remain source-reported, not independently audited across all 78 items. | **record only:** retain the dated count and byline chronology with attribution and no prevalence inference. | pending | not started |
| C08: Gizmodo says CNET corrected the article only after Futurism alerted it to some errors. | Indirect claim explicitly attributed to Futurism; the two linked Futurism pages were accessible but are separate sources and not recursively ingested here. | partly covered by #41 source tracing; pattern-opportunities promotes claim verification. | #41 does not explicitly ask who discovered a correction or compare the public correction timeline. | **test-adapt:** consider a correction-history question in #41/process guidance after direct review of the original and correction timeline; do not treat outside discovery as authorship evidence. | approved | implemented |
| C09: CNET said each AI-assisted article was reviewed, fact-checked, and edited by a topical editor and carried an editor name, yet reported errors survived. | CNET policy is directly quoted and remains accessible; the contrast with the errors is the reporter's inference from the case. One article cannot estimate review failure rate. | partly covered by #41 fact/source tracing and by process guidance that Audit does not establish factual fidelity. | A declared workflow can be confused with verification completed; the project does not currently state this distinction in #41. | **adopt:** clarify, if Mae approves, that disclosed review is provenance evidence rather than proof every factual claim was verified; documentation and report-language tests required. | approved | implemented |
| C10: Leffer argues AI-output editing requires an exacting phrase-by-phrase review, that high volume raises editor burden, and that failure becomes inevitable. | Reporter interpretation from the CNET incident; no editor study, workload measure, human comparison, or causal test. | not covered as an empirical product rule, appropriately; process guidance already requires protected-fact comparison for all rewriting. | `inevitable` exceeds what one reported case can establish, and human-written work also needs fact checking. | **do not adopt:** do not encode inevitability, unique AI burden, or an AI-only review rule from this source; retain only the general need for factual verification. | pending | not started |
| C11: Nearly all CNET AI-written articles reportedly carried a note saying they were being reviewed for accuracy and would receive corrections if needed. | Leffer's page observation without a released item-level list or exact numerator; dated to publication. | partly covered by #41 provenance and disclosure prompts. | Current #41 does not explicitly inspect editor notes or correction status, and `nearly all` cannot be independently reproduced here. | **record only:** retain the dated observation; require item-level preservation before quantitative use. | pending | not started |
| C12: CNET PR said it was actively reviewing all AI-assisted pieces and would issue necessary corrections under its correction policy. | Directly quoted emailed PR statement added in the 5:05 p.m. update; CNET referred Gizmodo to its earlier policy but did not answer whether the secondary review used the same editor, a different editor, or an AI fact-checker. It states an intended process, not an outcome audit. | partly covered as provenance/process context by #41 and the source card; no runtime checker tracks promised review against review design or outcomes. | The review mechanics remain unknown, and the source does not report the eventual results or number of later corrections. | **record only:** preserve the commitment, unanswered process questions, and outcome gap; do not state that the review was completed or successful. | pending | not started |
| C13: Leffer contrasts CNET's open-ended explainer generation with the Associated Press's narrower AI use in preset templates intended to free journalists for other work. | Cited contextual comparison and author interpretation; the AP page is not a controlled comparator and was not separately ingested here. | not covered as a product rule, appropriately; #41 is genre-specific but not workflow-specific. | The source cannot establish comparative accuracy, labor effects, or best practice across the two systems. | **do not adopt:** make no template-versus-generation policy claim until the AP practice and outcomes receive direct review. | pending | not started |
| C14: Leffer argues CNET's general explainers were search-optimized and that ad revenue, low AI overhead, and high volume can subordinate accuracy to SEO. | Reporter interpretation based on article format and digital-media incentives; no traffic, revenue, cost, ranking, editorial, or causal data are supplied. | not covered as a style or provenance rule, appropriately. #41 does include affiliate/vendor provenance but not inferred business motive. | Search-oriented topics and plain-language question headlines are common human journalism and cannot establish provenance or motive. | **do not adopt:** do not create an SEO-style, headline, motive, or authorship check from this source; retain as dated editorial commentary only. | pending | not started |
| C15: The source concerns factual accuracy, disclosure, correction history, and workflow; it supplies no reusable prose tell or authorship evidence. | Boundary derived from the complete article and its absence of style comparison, model metadata, rates, thresholds, or human-text controls. | fully covered by the process product boundary, catalogue no-single-proof framing, #41 manual treatment, and the existing pattern-opportunities source-grounding row. | Shared summaries should keep the source out of lexical/rhythm evidence and H12 threshold support. | **adopt:** keep Gizmodo/CNET mapped only to #41 provenance, factual verification, correction history, and no-authorship context; retire the old H12 mapping. | approved | not applicable |

## Recommendations

- C01: **record only** as dated rationale for factual verification, without a model-wide accuracy claim.
- C02: **test-adapt** as a correction-history evaluation example only after the original CNET version and arithmetic controls are preserved.
- C03: **record only** as an indirect unresolved second example pending the original CNET text.
- C04: **test-adapt** only as a before/after source-grounding example after the original is preserved.
- C05: **record only** pending the original loan example and sufficient values for arithmetic verification.
- C06: **record only** as an indirect terminology/advice correction, not a prose pattern.
- C07: **record only** with attribution, dates, and no prevalence inference beyond the reported CNET set.
- C08: **test-adapt** a correction-history prompt only after direct review of the correction timeline.
- C09: **adopt** the distinction between declared review and completed claim verification if Mae approves a documentation change.
- C10: **do not adopt** inevitability or a unique AI-only editorial-burden rule from this case.
- C11: **record only** the dated editor-note observation pending an item-level archive.
- C12: **record only** CNET's stated review commitment without implying completion or success.
- C13: **do not adopt** a template-versus-generation policy claim without direct AP review.
- C14: **do not adopt** an SEO-style, headline, business-motive, or authorship check.
- C15: **adopt** the bounded #41 provenance/fact-checking/correction-history mapping and retire H12 support.

## Evaluation of approved changes

- C01: not applicable - recommendation pending; no product change made.
- C02: not applicable - recommendation pending; no product change made.
- C03: not applicable - recommendation pending; no product change made.
- C04: not applicable - recommendation pending; no product change made.
- C05: not applicable - recommendation pending; no product change made.
- C06: not applicable - recommendation pending; no product change made.
- C07: not applicable - recommendation pending; no product change made.
- C08: passed - commit 88a04bb (DR-111) added the correction-history question to the #41 journalism watchlist in the `genre_specific` record and its embedded prompt line in `human-eyes/scripts/judgement.json`; `python3 -m unittest dev.evals.tests.test_judgement_json` passes on 2026-07-17. Outside discovery of a correction is not treated as authorship evidence.
- C09: passed - commit 88a04bb (DR-111) added the correction-history question and the human look-alike guard to the #41 journalism watchlist in `human-eyes/scripts/judgement.json`, directing reviewers to check the correction record rather than accept declared review as verification and to report findings as review prompts, never accusations; `python3 -m unittest dev.evals.tests.test_judgement_json` passes on 2026-07-17.
- C10: not applicable - recommendation pending; no product change made.
- C11: not applicable - recommendation pending; no product change made.
- C12: not applicable - recommendation pending; no product change made.
- C13: not applicable - recommendation pending; no product change made.
- C14: not applicable - recommendation pending; no product change made.
- C15: not applicable - mapping retirement only; no checker, hypothesis, or test changed.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/pbs_cnet_source_reviewer`, fresh, source-dedicated, and read-only; five-lens review followed by a same-reviewer focused re-check of materially changed C09 and C12 coverage, evidence, and decision text
- **Findings resolved:** two material findings resolved: C09's coverage changed from fully to partly covered because #41 lacks the declared-review/completed-verification distinction; C12 now preserves CNET PR's non-answer about secondary-review mechanics, unknown outcomes, and partly covered status
- **Unresolved findings:** none
