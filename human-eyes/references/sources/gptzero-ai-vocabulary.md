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

## Skill-use audit

- **Good use:** Treat the 100 rows as a dated vendor candidate list; preserve their exact provenance; use the page's human-text and non-probability cautions; compare clustering behavior against matched registers before retaining severity.
- **Misuse / overclaim:** Do not infer authorship, probability, model family, plagiarism, dishonesty, or a document verdict from one or several phrase hits. Do not import GPTZero's detector accuracy, ESL, language, or mixed-document claims into human-eyes.
- **Unsupported use:** The page cannot validate the current three-item strong-warning threshold, exact substring matching, nested-match counting, register-general use, causal reinforcement-learning explanation, or any detector score.
- **Underused evidence:** The current checker stores all 100 phrases but does not preserve source ratios or data-quality anomalies and does not count distinct occurrences consistently.
- **Patterns left on the table:** Human look-alikes, quoted uses, deliberate rhetorical use, register-specific base rates, phrase co-occurrence, absolute counts, time drift, and uncertainty remain unmeasured.

## Matched patterns / rules

- Pattern #7, `no-ai-vocabulary-clustering`: exact 100-row phrase inventory is present; threshold behavior is challenged by nested matches and occurrence undercounting.
- `overall-signal-stacking`: GPTZero phrases contribute vocabulary points, but the source does not validate the project's weights or threshold.
- Pattern #1, `no-significance-inflation`: several source rows overlap significance and importance language; this is secondary construction coverage, not independent validation.
- Pattern #52, `sentence-length-variance`, and pattern #53, `vocabulary-diversity`: GPTZero's general burstiness and vocabulary framing is adjacent vendor context only, not support for project thresholds.
- `human-eyes/references/process.md`: the no-authorship boundary agrees with the page's warning against final verdicts.
- Root README source mapping for pattern #7 and overall signal stacking: the source is already labelled as vendor phrase-list and co-occurrence context.

## Associated hypotheses

- H3, detection is the wrong product category: the source's own non-probability and no-final-verdict cautions support a vocabulary or writing-aid boundary, not authorship classification.
- H7, five checks gate, rest advise: the source supports advisory treatment but does not validate the current strong-warning threshold.
- H24, register-specific vocabulary density: directly relevant because the page asserts matching while withholding the register, time, and distribution detail needed to reproduce it.
- H25, model-family versus generic-AI residue: model families are named without versions or allocation, so generic attribution remains unsupported.

## Questions / follow-up

- Obtain a versioned methodology, row-level counts, corpus dates, language and genre distributions, model versions, and revision history from GPTZero before using ratios as more than vendor candidate evidence.
- Ingest the linked accuracy benchmark, detector-release, and multilingual pages separately if any of their claims will support a project recommendation.
- Mae must decide whether to retain, revise, or remove the current exact-list threshold behavior described in C05-C07 and whether to correct the stale April revision wording described in C08.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none found; archived member SHA-256 5c71154b51d9591446c0e93d7da0c6389ecb617f8043b67d01cb002ba3886403 | `snapshots/archive/gptzero-ai-vocabulary/2026-05-05-5c71154b.tar` | 2026-05-05 | `49332702b80326ce431139565dc0784b4c9d09cd55be022d987fad31eb25cced` |
| current | none found | `snapshots/gptzero-ai-vocabulary.md` | 2026-07-15 | `66589d146d10633e54dd287bad8c9581a983c0f10573d481f51dda041c08579c` |

The prior card recorded no snapshot digest. Before replacement, the working snapshot was verified byte-for-byte against git commit `f28a3706816d0ca5107196955a5d14418732a5af`; both computed to raw snapshot SHA-256 `5c71154b51d9591446c0e93d7da0c6389ecb617f8043b67d01cb002ba3886403`. The exact prior Markdown bytes, including one source-capture trailing space, are preserved as the sole member `2026-05-05-5c71154b.md` inside the archived tar file; `tar -xOf ... | shasum -a 256` reproduces the raw digest. The table records the archive-container digest required to verify the resolved previous path. The new record adds the 90 rows omitted from that capture, preserves all 100 exact-ratio records in an attachment, removes page chrome, adds full provenance, and records the client-clock date behavior. The first 10 list rows and substantive FAQ claims are unchanged; no underlying list revision between the two retrievals can be established.

## Decision history

- The previous reviewed card had no stable claim IDs, user-decision column, implementation-status column, or evaluation record. Its useful observations are retained as C01-C04 and C09.
- The previous card's broad `useful phrase list` mapping is reopened as C02-C07 because the complete list and live checker behavior were not preserved or tested.
- Existing project code already contains the 100 phrases, but no source-card decision record establishes approval of its threshold or overlap semantics. Recommendations affecting that implementation are therefore `pending` and `review required`, not retroactively marked implemented.
- No prior approved, rejected, or implemented source-card decision was removed.

## Project coverage

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: GPTZero describes AI Vocabulary as detecting frequent phrases and words used by ChatGPT, Gemini, and Claude in its dataset. | Direct vendor product description; no vocabulary-specific model versions, prompts, dates, allocation, language, or register. It identifies intended scope, not validated performance. | Partly covered: #7 and the source mappings identify GPTZero as a vendor phrase-list source; H25 tracks model-specific residue. | The project can read as model-general even though the page supplies only family names and opaque data. | Record the named families as unversioned vendor scope only; require model/date metadata before any model-general claim. Verify by source-card review only. | pending | not started |
| C02: The live client payload has 100 ranked phrase records; the page calls it Top 50, initially renders 10, and reveals all 100 with Show more. | Direct first-party client data and component code; all 100 rows preserved. The 50/100 discrepancy is internal to the source. | Fully covered for inventory: `GPTZERO_AI_PHRASES` and rendered pattern #7 contain the same 100 phrases in the same order after apostrophe normalization. | Project prose says April 2026 and does not record the source's 50/100 mismatch or stable data revision. | Retain the 100-item inventory only as vendor candidate evidence; add source-revision and mismatch notes if Mae approves. Verify list equality and regenerated catalogue. | pending | review required |
| C03: GPTZero says the ranking uses 3.3 million texts and compares AI frequency with human frequency; exact client ratios range from 181.5247457256 to 21.5615511894. | Direct vendor dataset and method headline; ratios are supplied, but absolute counts, denominators, uncertainty, and independent replication are absent. | Partly covered: pattern #7 names 3.3 million texts and the root README treats GPTZero as vendor examples; ratios are not used. | Evidence cannot validate severity, a three-item threshold, or document-level inference. | Keep ratios out of severity and authorship logic; preserve them only in the source attachment pending reproducible method details. Verify source documentation only. | pending | not started |
| C04: GPTZero says human documents are similarly uploaded and matched on subject matter, length, and unspecified other factors. | Direct vendor method statement; matching variables and `etc.` are not operationalized, and sampling, corpus dates, genres, languages, platforms, models, and lengths are undisclosed. | Partly covered: H24 calls for register-specific, time-sensitive vocabulary density; no live matcher implements that design. | Current flat list is not register-aware and has no time-decay or source-distribution controls. | Use C04 as a method requirement for H24 evaluation, not as proof that the current threshold is calibrated. Verify with a future matched-register experiment. | pending | not started |
| C05: All 100 phrases and constructed examples are direct vendor data; one curly apostrophe is normalized in the project. | Complete client payload; examples illustrate intended strings but are not human controls or empirical observations. | Fully covered for phrase recognition: a live normalized sequence comparison returned `True` for all 100 source rows against `GPTZERO_AI_PHRASES`. | Exact-list presence does not validate substring behavior, counting, threshold, context handling, or severity. | Preserve exact list coverage but treat recognition and threshold validity as separate questions. Verify with a source-list equality test plus matched legitimate controls before retaining severity. | pending | review required |
| C06: Six single source example sentences fail the project's three-item strong-warning check because nested words and overlapping phrases count separately. | Live project execution on the source's 100 example sentences; failures were rows 13, 42, 52, 64, 66, and 76. This is a project result, not a GPTZero result. | Challenges current behaviour: `check_ai_vocabulary` reports three signals for one source construction in each of those six examples. | One occurrence can be presented as a cluster, contrary to #7's claim that density means three or more and to the source's human-text caveat. | Evaluate span-deduplicated or source-construction-deduplicated counting and add the six examples as non-authorial threshold controls before deciding any code change. | pending | review required |
| C07: Repeating `provide a valuable insight` three times still counts as two distinct list labels, while one nested `provide a comprehensive overview` occurrence counts as three. | Live focused execution of `check_ai_vocabulary` and `vocabulary_signal_stacking_profile`; demonstrates distinct-membership counting rather than occurrence density. | Challenges current behaviour: the repeated case passes at 2, while the single nested case fails at 3 and receives two vocabulary-stack points. | Current evidence text says `AI words` and `total` but measures unique matched labels with overlapping substrings, not occurrences or non-overlapping spans. | Define the intended unit, add repeated and overlapping regression controls, and recalibrate threshold and evidence wording on matched human/AI text before retaining or changing behavior. | pending | review required |
| C08: The displayed Updated month and year come from `new Date()`, while the page says the list is updated regularly and provides no revision history. | Direct component-code observation plus page claim. The visible date proves retrieval-time rendering, not data freshness. | Not covered accurately: `grade.py` and pattern #7 hardcode `April 2026`; the prior snapshot displayed May and the current render July with identical first 10 rows. | Project/source metadata can mistake a client-clock label for a list revision. | Replace month-as-revision wording with retrieval date plus a preserved client-data digest if Mae approves; do not claim a data update without a changed payload. Verify catalogue render and source metadata. | pending | review required |
| C09: The page distinguishes vocabulary hits from its probability score and says fully human text may contain listed phrases; changing a phrase may or may not affect the score. | Direct vendor caution, though `NOT to our AI probability score` is malformed. The following human-text counterexample and `Sometimes yes, and sometimes no` qualification are clear. | Fully covered in principle: #7 says no single phrase proves AI writing; process guidance forbids authorship inference; root README calls the list vendor examples. | The current strong-warning overlap behavior can still overstate a single construction despite the written boundary. | Retain and surface the human-text and non-probability caveat wherever GPTZero phrases are reported; verify treatment with C06-C07 controls. | pending | review required |
| C10: GPTZero names perplexity, burstiness, and generic or repetitive style as common detector factors and says its proprietary model uses hundreds of factors. | Direct vendor product explanation; factors, weights, training, calibration, and ablations are undisclosed. | Partly covered as adjacent context only: #52 and #53 measure different local statistics; the project does not import GPTZero's proprietary score. | Similar labels could be mistaken for method equivalence or threshold support. | Take no product action; retain as opaque vendor context and keep it out of #52/#53 validation. Verify by source-card wording only. | pending | not started |
| C11: GPTZero claims 99% accuracy, under 2% false negatives, under 1% false positives, and 96.5% mixed-document accuracy, citing partners and internal testing. | Direct vendor-reported metrics with a linked benchmark not reviewed here; this page gives no dataset, threshold, confidence interval, subgroup, version, or protocol. | Not covered and not suitable for a human-eyes rule. Existing process forbids authorship verdicts. | No direct evidence here supports importing accuracy, mixed-text, or probability claims. | Do not promote these metrics; ingest and review the linked benchmark separately before any use. | pending | not started |
| C12: GPTZero says detector results should not punish or be a final verdict, no detector is perfect, longer inputs are stronger, and English prose is strongest. | Direct vendor limitation statements; no stratified results on this page. | Fully covered for the no-verdict boundary in process guidance; length and English-specific performance are not project thresholds. | The page cannot quantify how much length, language, genre, or mixed authorship changes accuracy. | Retain the no-verdict caution; do not import length or English thresholds without direct evidence. | pending | not started |
| C13: GPTZero claims ESL debiasing and a 1% ESL false-positive rate, plus support for five named languages. | Direct vendor claims; linked multilingual evidence was not reviewed and no subgroup protocol appears here. | Not covered; existing project sources separately warn about detector bias, but that does not validate GPTZero's claim. | The claim could be misread as independent fairness evidence. | Do not promote ESL or multilingual performance from this page; require direct subgroup evaluation. | pending | not started |
| C14: GPTZero names broad detector model families and says a latest release updated most training data with GPT-4.1, o3, Gemini 2.5, and Sonnet 4 material. | Direct vendor release summary on this page; the linked release was not reviewed, and vocabulary-feature allocation is unspecified. | Partly covered by H25's model/version metadata requirement; no project rule depends on these detector claims. | The page does not establish which models generated the vocabulary corpus or each phrase ratio. | Keep model names as unresolved product scope, not phrase-list provenance or model fingerprint evidence. | pending | not started |
| C15: GPTZero calls AI a stochastic parrot and attributes overuse to reinforcement training overfitting small training-data variations, while saying it has seen reports about amplification. | Vendor interpretation and indirect report; no cited experiment, model comparison, or causal test is supplied on the page. | Not used by the live checker; broader project documentation contains other mechanism claims but no need to attach this one. | The page cannot support a causal explanation for any phrase or ratio. | Take no further action; record the mechanism as unsupported interpretation and do not add it to pattern rationale. | pending | not started |
| C16: The public record contains internal data-quality and reporting anomalies, including 50 versus 100 rows, dynamic update dating, `ai_to_human_ration`, malformed phrases, and no null results or uncertainty. | Direct source and code inspection; these issues limit interpretation but do not prove the ratios are wrong. | Partly covered by general caution, but not documented in the current source mapping. | The project currently reproduces the list without preserving these quality boundaries beside it. | Add an explicit non-promotion/data-quality note if Mae approves; treat every phrase as a candidate pending matched controls, not a validated blacklist. | pending | not started |

## Recommendations

- C01: Record named model families as unversioned vendor scope only.
- C02: Retain the exact 100-item inventory only as candidate evidence and correct its provenance wording.
- C03: Preserve ratios in the source record but keep them out of severity and authorship logic.
- C04: Use the opaque matching claim as a future H24 evaluation requirement, not validation.
- C05: Keep source-list equality separate from threshold validity and add a deterministic equality test only if approved.
- C06: Evaluate non-overlapping span or construction deduplication with the six source-example controls.
- C07: Define and test the counting unit for repeated and nested matches before retaining current evidence wording.
- C08: Replace the stale month-as-revision claim with retrieval date and client-data digest if approved.
- C09: Retain and surface the human-text and non-probability caveat.
- C10: Take no product action on proprietary perplexity, burstiness, or style framing.
- C11: Do not promote vendor accuracy metrics without a separate direct review.
- C12: Retain the no-final-verdict boundary; do not import unsupported length or language thresholds.
- C13: Do not promote ESL or multilingual performance claims from this page.
- C14: Keep detector model names out of vocabulary-list provenance and model fingerprint claims.
- C15: Take no further action on the unsupported causal explanation.
- C16: Add a source-quality non-promotion note and require matched controls before treating phrases as validated signals.

## Evaluation of approved changes

- C01: not applicable - pending recommendation; no product change made.
- C02: not applicable - pending recommendation; no product change made.
- C03: not applicable - pending recommendation; no product change made.
- C04: not applicable - pending recommendation; no product change made.
- C05: not applicable - pending recommendation; no product change made.
- C06: not applicable - pending recommendation; no product change made.
- C07: not applicable - pending recommendation; no product change made.
- C08: not applicable - pending recommendation; no product change made.
- C09: not applicable - pending recommendation; no product change made.
- C10: not applicable - pending recommendation; no product change made.
- C11: not applicable - pending recommendation; no product change made.
- C12: not applicable - pending recommendation; no product change made.
- C13: not applicable - pending recommendation; no product change made.
- C14: not applicable - pending recommendation; no product change made.
- C15: not applicable - pending recommendation; no product change made.
- C16: not applicable - pending recommendation; no product change made.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: /root/gptzero_review_4 (fresh source-dedicated final provenance re-review); prior fresh reviews by /root/gptzero_review_3 and /root/gptzero_review_2; /root/gptzero_review_1 was interrupted before returning a report
- **Reviewer isolation:** fresh source-dedicated agent; one source only; not reused
- **Findings resolved:** /root/gptzero_review_2 found one material direct-versus-project attribution error; the Evidence section now assigns live executions to C06-C07, vendor-reported metrics to C11, and unsupported indirect causal wording to C15. /root/gptzero_review_3 verified the correction and all five lenses with zero material or non-material findings. The exact prior Markdown was subsequently placed in a tar archive so its source trailing space remains byte-exact while the repository diff stays whitespace-clean. /root/gptzero_review_4 verified the tar container, sole archived member, both digests, and all five lenses with zero material or non-material findings.
- **Unresolved findings:** none
