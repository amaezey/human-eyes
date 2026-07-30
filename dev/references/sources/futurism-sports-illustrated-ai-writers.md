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

## Matched patterns / rules

- `human-eyes/scripts/judgement.json` record `genre_specific`, journalism sub-record: partly or fully covers unsupported claims, sourcing, byline/bio/headshot verification, broken links, unverifiable quotations, vendor/affiliate provenance, and non-disclosure.
- `human-eyes/scripts/patterns.json` `_meta.evidence_body` and generated `human-eyes/references/patterns.md` cite this article for H10 fake bylines, fake bios, AI headshots, affiliate-review provenance, undisclosed generated content, and byline laundering. The “undisclosed generated content” phrase needs a disputed-claim qualifier.
- `dev/references/sources/pattern-opportunities.md` promotes Futurism under source-grounding, fact-checking, and claim verification for H10 journalism/academic manual checks.
- `human-eyes/references/process.md` product boundary correctly prevents provenance findings from becoming authorship claims.
- No deterministic check establishes any of C01-C17. A surface-only grader result would not be a complete Audit and is unnecessary for the source's manual provenance claims.

## Associated hypotheses

- H12, genre-aware threshold calibration, supports keeping journalism provenance review separate from generic prose thresholds; this source does not test H12's threshold claim.
- Proposed evaluation question: can reviewers reliably distinguish legitimate protected anonymous sourcing from unsupported vague attribution while still detecting undisclosed vendor and byline provenance?
