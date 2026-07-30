# Turnitin: Using the AI Writing Report

## Metadata

- **URL:** https://guides.turnitin.com/hc/en-us/articles/22774058814093-Using-the-AI-Writing-Report
- **Author / owner:** Turnitin
- **Published:** 2023-12-29; living page edited 2026-03-06
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** first-party vendor product documentation
- **Evidence tier:** Vendor / detector pages
- **Review mode:** update
- **Stable identifier:** Turnitin Guides / Zendesk article 22774058814093
- **Version / revision:** official API `edited_at` 2026-03-06T15:18:31Z; prior snapshot body recorded as retrieved 2026-05-05 and byte-identical to the fresh Jina body
- **Full-text status:** complete
- **Snapshot:** `snapshots/turnitin-ai-writing-detection.md`
- **Extraction method:** unauthenticated first-party Zendesk API JSON fetched with `curl -L --compressed`, body checked against Jina Reader Markdown, and all ten first-party PNG attachments downloaded and visually inspected
- **Snapshot SHA-256:** `017124001aa0fb5b4ca0aa0fce36402ba310270ac73a21e4b8684669e180da62`
- **Model / corpus scope:** Turnitin discloses no detector model build, training corpus, evaluation sample, validation protocol, or calibration data on this page. Product scope is qualifying long-form prose of 300-30,000 words in English, Spanish, or Japanese; only the English detector is said to include AI-paraphrasing and AI-bypasser detection. Non-prose, poetry, scripts, code, bullets, tables, and annotated bibliographies are outside reliable detection on this page.
- **Access limitations:** direct canonical HTML returned HTTP 403, but the first-party API exposed the complete published body and metadata. The body, its structure, and all ten images were preserved. The linked Turnitin FAQ and file-requirements page were opened to establish direct-versus-linked boundaries; the 538-line FAQ remains a separate, non-ingested living source.

## Summary

Turnitin's living first-party guide explains the AI Writing Report's output categories, interface states, eligible text and file conditions, language-specific capabilities, and limitations. It is useful to human-eyes as vendor evidence for cautious report interpretation: Turnitin says its model can misidentify human, AI-generated, and AI-paraphrased text and must not be the sole basis for adverse action. It is not a validation study, supplies no reusable prose features, and publishes no model version, evaluation sample, calibration, subgroup result, or independent benchmark on this page. The refresh preserves the complete official body (1,102 whitespace-separated rendered-text tokens) and all ten product screenshots; the article text is unchanged from the archived Jina body, while provenance, image evidence, claim coverage, and project comparison are new.

## Main insights

- Turnitin frames the report as a review aid, not a misconduct verdict, and explicitly requires further scrutiny, human judgment, and organisation-specific academic policy.
- The displayed percentage concerns only qualifying long-form prose and is independent of Turnitin's Similarity Score; a mixed-format document can have percentage/highlight disparities.
- The page defines two English report categories: likely AI-generated text, possibly modified by a bypasser, and likely AI-generated text likely modified by an AI paraphraser or word spinner. Spanish and Japanese lack the paraphrase/bypasser capabilities described here.
- The vendor says false positives occur and that its testing found a higher incidence `between 0 and 19`. The page suppresses scores and highlights above 0% and below 20%, but uses three slightly different boundary formulations: `between 0 and 19`, `between 0 and 20`, and `above 0% and below the 20% threshold`.
- A displayed 0% means the model did not identify qualifying text as likely AI/AI-altered; it does not establish that the whole document is human-written.
- Product constraints and examples are not transferable human-eyes thresholds. The page gives no sentence-level feature inventory, calibrated authorship probability, current detector build, corpus, methods, or independently checked performance result.
- The main screenshot's 56% score and 24%/32% breakdown are interface illustrations only, not a reported study result.

## Evidence and claims to extract

- **Direct source reviewed:** complete published body of Turnitin Guides / Zendesk article 22774058814093 at API `edited_at` 2026-03-06T15:18:31Z, plus all ten first-party image attachments. The official API body has 5 second-level headings, 10 third-level headings, 1 fourth-level heading, 34 paragraphs, 12 list items, 11 links, and 10 images.
- **Method and sample:** first-party product documentation, not an empirical paper. The page reports product semantics and vendor testing language but publishes no detector version, model family, training/evaluation corpus, sample size, comparison group, annotation method, uncertainty, subgroup analysis, or raw results. Its operational scope is 300-30,000 words of long-form prose, files under 100 MB, `.docx`/`.pdf`/`.txt`/`.rtf`, and English/Spanish/Japanese.
- **Direct versus cited evidence:** C01-C19 record the page's direct product statements, visible screenshots, or reviewer-observed omissions. The final method link, separate file-requirements page, and any FAQ-only accuracy, bias, training, model, or classroom claims are linked first-party evidence but are not direct evidence from this card's reviewed source.
- **Important limits and counterexamples:** Turnitin expressly admits human-text false positives and AI/AI-paraphrase misidentification, excludes several genres and formats, distinguishes qualifying text from the full document, and says mixed writing types can create score/highlight disparity. The page's threshold wording is internally imprecise at the boundary, and its illustrative 56% report cannot establish calibration or accuracy.

## Matched patterns / rules

- `human-eyes/references/process.md`, Product boundary: reports do not infer who or what wrote text.
- `human-eyes/scripts/patterns.json` and generated `human-eyes/references/patterns.md`, evidence framing: clusters and individual phrases are not authorship proof; warnings and user review are preferred to accusations.
- `dev/TESTING.md`, benchmark-report requirement: say that human-eyes measures prose patterns and does not classify authorship.
- `dev/hypotheses.md` H3, Drop detection framing entirely: directionally supported as product-framing context, not as an empirical test of H3.
- `dev/references/sources/pattern-opportunities.md`, Detector-output caveat wording and Do Not Promote rows.
- No direct Turnitin-supported pattern or deterministic checker.

## Associated hypotheses

- H3, Drop detection framing entirely: the source's human-review and non-sole-basis language supports the risk framing, but the source is vendor documentation rather than validation of the proposed reframe.
- H2, Comparison-engine product reframe: current wording says it aligns with Turnitin, but this reviewed page says the AI percentage is different from and independent of the Similarity Score. The source does not support H2's claimed alignment.
- H8, Audience-specific audit and prescriptive voices: Turnitin is named elsewhere as product precedent, but this article does not compare writer/instructor surfaces or validate a two-voice design.
