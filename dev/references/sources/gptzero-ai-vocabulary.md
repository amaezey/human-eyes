# GPTZero: AI Vocabulary

## Metadata

- **URL:** https://gptzero.me/ai-vocabulary
- **Author / owner:** GPTZero
- **Published:** Living page; no publication date found
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** Vendor vocabulary guide and detector product page
- **Evidence tier:** Vendor / detector pages
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** Current client data module 577058 in `07zk.cz9f.bgi.js`, retrieved 2026-07-15; previous capture displayed Updated May 2026 and had no stable identifier
- **Full-text status:** complete
- **Snapshot:** `snapshots/gptzero-ai-vocabulary.md`
- **Extraction method:** Direct first-party HTML and client JavaScript fetched with `curl -fsSL --compressed`; 100-row JSON payload decoded losslessly from client module 577058; direct HTML and rendered text cross-checked
- **Snapshot SHA-256:** `66589d146d10633e54dd287bad8c9581a983c0f10573d481f51dda041c08579c`
- **Model / corpus scope:** GPTZero says 3.3 million AI and human texts, with human documents matched on subject matter and length among unspecified other factors; page names ChatGPT, Gemini, and Claude for the vocabulary feature and names broader current detector families, but gives no vocabulary-corpus dates, language, genre, platform, text-length distribution, model versions, prompts, sampling frame, counts by class, or row-level uncertainty
- **Access limitations:** No access barrier. Complete page claims, all 100 client-data rows, all examples, and 13 FAQs were preserved. The linked accuracy benchmark, model-release, and multilingual pages were not recursively ingested, so their inherited claims remain unresolved. The interactive scanner was not exercised.

## Summary

GPTZero's living vendor page publishes a client-side array of 100 phrases, exact AI-to-human ratios, and constructed example sentences while labelling the table and two FAQs as a Top 50 list. It says the ranking comes from 3.3 million AI and human texts, with subject matter and length used for matching, but does not expose class counts, corpus dates, model versions, prompts, language or genre distributions, absolute frequencies, uncertainty, or enough method to reproduce the ratios. The refreshed record preserves all 100 rows rather than the prior snapshot's first 10. It confirms the project's lexical inventory exactly, strengthens the boundary that vocabulary is not an authorship or probability verdict, and exposes two live coverage problems: nested list entries can make one source example trip the three-item strong-warning threshold, while repeating one phrase three times still counts as one list member.

## Main insights

- The client dataset contains 100 ranked records even though the page heading says `Top 50 AI Words and Phrases`; the table initially renders 10 and `Show more` reveals the full array.
- Exact ratios run from 181.5247457256 for `provide a valuable insight` to 21.5615511894 for `stand in stark contrast`; the UI rounds them to 182x and 22x.
- The page attributes its ranking to 3.3 million texts and says AI texts are compared with similarly uploaded human documents based on subject matter, length, and unspecified other factors.
- The source supplies no absolute phrase counts, AI/human denominators, corpus dates, model-version allocation, prompts, language or genre breakdown, uncertainty, train/test separation, or independent replication.
- The page explicitly separates the vocabulary tool from an AI probability score and says a fully human text may contain listed phrases. Its sentence `NOT to our AI probability score` is malformed, so the following human-text example carries the clearest boundary.
- The visible `Updated <month> <year>` label is generated from the viewer's clock with `new Date()`; it is not a source revision identifier and does not establish that the data changed that month.
- The page says the public list is updated regularly, but supplies no revision history. The first 10 current rows are identical to the prior May capture; the earlier snapshot omitted rows 11-100, so the refresh establishes preservation completeness rather than a 90-row source addition.
- The client data and page have quality anomalies: the source field is named `ai_to_human_ration`; the heading says 50 while 100 rows render; and entries such as `a serf reminder`, `despite the face`, and `analysis of the data to analyze and use` are malformed or noisy.
- The project's `GPTZERO_AI_PHRASES` list matches all 100 current source phrases in order after apostrophe normalization.
- Six single source example sentences currently fail `no-ai-vocabulary-clustering` because nested base words and overlapping phrases count separately: rows 13, 42, 52, 64, 66, and 76.
- Repeating one listed phrase three times does not meet the current three-item threshold because membership is counted once per list entry, not once per occurrence.
- GPTZero's accuracy, mixed-document, ESL, language, model, and causal statements are vendor claims or reports linked to other pages; this page does not provide their underlying evidence.

## Evidence and claims to extract

- **Direct source reviewed:** Canonical page retrieved 2026-07-15; direct HTML; first-party client chunks `07zk.cz9f.bgi.js` and `152swr_6vbnzi.js`; complete 100-record module 577058 preserved as `snapshots/attachments/gptzero-ai-vocabulary-2026-07-15-client-data.json`.
- **Method and sample:** GPTZero says it regularly scans millions of AI texts and compares them with similarly uploaded human documents based on subject matter, length, and unspecified other criteria. The page says the ranking uses 3.3 million texts, but gives no class counts, sampling or upload dates, deduplication, model versions, prompts, language or genre composition, text-length distribution, absolute n-gram counts, confidence intervals, statistical tests, or independent reproduction.
- **Direct versus cited evidence:** C01-C05, C08-C10, C12-C14, and C16 are direct page or client-code observations or vendor assertions. C11 reports GPTZero's internal testing and linked partners rather than evidence reproduced here. C15 is GPTZero's unsupported causal interpretation and includes the indirect `We've seen reports` wording. C06-C07 are live-project execution results, not source results.
- **Important limits and counterexamples:** The page says human text can contain listed phrases, detector results should not punish or serve as final verdicts, no detector is perfect, longer inputs are stronger than shorter ones, and English prose is the strongest setting. No source null result, human phrase example, absolute frequency, uncertainty estimate, or per-register comparison is supplied. The 50/100 mismatch, dynamic date, malformed rows, opaque matching, and missing revision history prevent the ratios from setting a human-eyes severity or authorship threshold.

## Matched patterns / rules

- Pattern B1, `no-ai-vocabulary-clustering`: exact 100-row phrase inventory is present; threshold behavior is challenged by nested matches and occurrence undercounting.
- `overall-signal-stacking`: GPTZero phrases contribute vocabulary points, but the source does not validate the project's weights or threshold.
- Pattern A1, `no-significance-inflation`: several source rows overlap significance and importance language; this is secondary construction coverage, not independent validation.
- Pattern G9, `sentence-length-variance`, and pattern B5, `vocabulary-diversity`: GPTZero's general burstiness and vocabulary framing is adjacent vendor context only, not support for project thresholds.
- `human-eyes/references/process.md`: the no-authorship boundary agrees with the page's warning against final verdicts.
- Root README source mapping for pattern B1 and overall signal stacking: the source is already labelled as vendor phrase-list and co-occurrence context.

## Associated hypotheses

- H3, detection is the wrong product category: the source's own non-probability and no-final-verdict cautions support a vocabulary or writing-aid boundary, not authorship classification.
- H7, five checks gate, rest advise: the source supports advisory treatment but does not validate the current strong-warning threshold.
- H24, register-specific vocabulary density: directly relevant because the page asserts matching while withholding the register, time, and distribution detail needed to reproduce it.
- H25, model-family versus generic-AI residue: model families are named without versions or allocation, so generic attribution remains unsupported.
