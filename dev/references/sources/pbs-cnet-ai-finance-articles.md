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

## Matched patterns / rules

- H10 `genre_specific` journalism agent assessment in `human-eyes/scripts/judgement.json`: checks unsupported claims, verifiable links, bylines, dates, quotes, provenance, and undisclosed generated or third-party content.
- H10 catalogue text in `human-eyes/scripts/patterns.json` and `human-eyes/references/patterns.md`: asks whether journalism facts trace to named sources but does not make the source's correction-history comparison explicit.
- `human-eyes/references/process.md`: preserves facts, quotations, citations, names, dates, links, and qualifications; states that an Audit checks writing patterns and does not prove factual fidelity.
- `dev/references/sources/pattern-opportunities.md`: already lists Gizmodo/CNET under the promoted source-grounding, fact-checking, and claim-verification opportunity.
- Root `README.md` H10 evidence summary already uses Gizmodo/CNET for journalism provenance and correction history.

## Associated hypotheses

- None directly supported. The previous card mapped H12 `Genre-aware threshold calibration`, but this article contains no threshold, matched-register comparison, detector result, or prose-feature distribution. It remains useful genre context for H10, not evidence for H12.

## Prior-to-current comparison

- **Added:** current contract metadata, stable post identifier and modification timestamp, exact prior digest and archive, raw HTML and lead-image attachments, 19-paragraph structure verification, claims C01-C15, direct/cited/interpretive boundaries, live project comparison, pending decisions, and independent-review fields.
- **Corrected:** the old summary said the compound-interest article had to be corrected “after misstating the calculation,” which collapsed five reported errors into one. The refresh separates all five, distinguishes the CNET review-policy quotation from actual verification, and replaces the old unsupported H12 mapping with genre-context only.
- **Removed:** no substantive Gizmodo body text or reported incident. The inherited mention of an “original PBS/AP URL” is removed because the reviewed source is Gizmodo post 1849996151 and no PBS/AP source identity or failed URL was preserved in the old provenance.
- **Unchanged:** canonical Gizmodo identity, Lauren Leffer byline, 2023-01-17 publication date, journalism evidence tier, and use as provenance, correction, factual-verification, and editorial-process context rather than style evidence.
