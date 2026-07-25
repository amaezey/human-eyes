# Merrill, Chen, and Kumer: What are the clues that ChatGPT wrote something?

## Metadata

- **URL:** https://www.washingtonpost.com/technology/interactive/2025/how-detect-chatgpt-em-dash/
- **Author / owner:** Jeremy B. Merrill, Szu Yu Chen, and Emma Kumer
- **Published:** 2025-11-13; Yahoo syndication updated 2025-11-14 17:25 UTC
- **Retrieved:** 2026-07-16
- **Extracted:** 2026-07-16
- **Source type:** data journalism / corpus analysis
- **Evidence tier:** Journalism / reported cases
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** current canonical interactive updated 2025-11-13 and syndicated rendering updated 2025-11-14 17:25 UTC; prior 2026-05-05 syndicated capture archived by hash
- **Full-text status:** complete
- **Snapshot:** `snapshots/merrill-wapo-chatgpt-clues.md`
- **Extraction method:** complete Yahoo syndicated body; canonical Washington Post and Jina Reader cross-check; Jina extraction of all nine first-party chart PDFs; visual review of eight preserved syndicated chart renders and the archived first-party `approach` / `significant` PDF
- **Snapshot SHA-256:** `d4b80e1be938b17c278ddca69c33a50d8075cc45b95d7160f5402a8d0a1a3866`
- **Model / corpus scope:** 328,744 OpenAI GPT-4o messages of at least 10 words from 37,929 publicly shared, primarily English ChatGPT conversations; May 2024 through 2025-07-31; source platform ChatGPT; preserved through the Internet Archive from a list maintained by Henk Van Ess
- **Access limitations:** direct canonical command-line retrieval failed; the canonical reader view omits interactive panels. The complete prose came from the Yahoo syndication, all nine first-party chart PDFs were text-extracted, eight syndicated chart renders were preserved, and the omitted first-party `approach` / `significant` PDF was recovered through the Internet Archive. The source supplies no raw data, code, exact monthly table, uncertainty estimates, statistical tests, prompt/task distribution, or described construction of the human comparison corpus. Two inline methodological links were preserved but not treated as independently reviewed evidence.

## Summary

The Washington Post analyzed 328,744 GPT-4o messages from 37,929 publicly shared, primarily English ChatGPT conversations preserved by the Internet Archive. The dated May 2024-July 2025 corpus shows sharp within-model drift: emoji, em-dash, contraction, `core`, and `modern` use rose, while `delve` and five formal words fell; `not just X, but Y` appeared in 6 percent of July chats. This is large observational journalism about one selected public-share corpus, not a representative sample of ChatGPT use, a controlled model comparison, a validated detector, or a document-level authorship rule. Its most important contribution is evidence that public tells can rise, fall, and invert quickly.

## Main insights

- The article's measured unit is a GPT-4o message of at least 10 words in a publicly shared, primarily English conversation, not a document, user, prompt, or all-model response.
- By July 2025, 70 percent of sampled messages contained at least one emoji. The chart shows sparkles, light bulb, small blue diamond, pushpin, cross mark, fire, brain, and check mark; the check mark appeared in about 30 percent and the brain in about 25 percent. The article reports the check mark at 11 times the unspecified human comparison rate and the brain and small blue diamond at 10 times that rate.
- Em-dash presence rose from fewer than 1 in 10 responses a year earlier to more than half by summer 2025; the chart ends in the upper 70s. The article also names journalists as a human look-alike.
- Versions of `not just X, but Y` appeared in 6 percent of July 2025 chats. The source does not disclose the coding definition or a human baseline, so that rate cannot be assigned to the exact literal form alone.
- `delve` fell from a charted level just above 3 percent near the beginning of the series to 1 in 1,000 chats in July 2025. `ensure`, `various`, `crucial`, `significant`, and `approach` also fell.
- `you're` and `it's` rose to almost one-third of chats, while `don't` and `isn't` also rose. The article's suggestion that this might sound more human is interpretation, not a measured human comparison.
- `core` rose fivefold from the prior year and reached about 12 percent in July; `modern` exceeded 8 percent. These are dated model-specific shifts, not stable generic-AI words.
- The article says the patterns may help identify ChatGPT-assisted emails or documents, then explicitly warns that humans use them too. It does not validate a combination rule, threshold, error rate, probability, or authorship inference.
- The page discloses a Washington Post content partnership with OpenAI. The source does not say the partnership supplied, selected, or analyzed the corpus.

## Evidence and claims to extract

- **Direct source reviewed:** canonical interactive updated 2025-11-13, complete Yahoo syndication updated 2025-11-14 17:25 UTC, all nine one-page first-party chart PDF extractions, eight preserved syndicated chart renders, and the archived first-party bytes and rendered pixels of the ninth `approach` / `significant` PDF.
- **Method and sample:** descriptive time-series analysis of 328,744 GPT-4o messages of at least 10 words from 37,929 publicly shared, primarily English conversations, May 2024-July 2025. Conversations were preserved by the Internet Archive from Henk Van Ess's list. The article names human comparison rates only for selected emojis and does not describe that comparison corpus.
- **Direct versus cited evidence:** C01-C03 and C05-C10 are source-reported measurements or disclosed method facts. C04 combines a measured GPT-4o series with an unmeasured journalist counterexample; C08 also includes the authors' interpretation that contractions might sound more human. C11 is the authors' drift interpretation beyond the observed July endpoint, and C12 is the authors' use claim plus explicit human-look-alike limitation. The linked public-share explainer and Henk Van Ess list are provenance pointers, not independently reviewed evidence and not support for any project recommendation.
- **Important limits and counterexamples:** self-selected public-share corpus; GPT-4o only; primarily English; minimum 10-word messages; unknown prompt/task and user composition; conversation clustering not discussed; no raw counts by month, uncertainty, statistical tests, code, or representativeness claim; human comparison unspecified except for reported emoji ratios; journalists explicitly named as em-dash users; all cues explicitly allowed in human writing.

## Skill-use audit

- **Good use:** dated GPT-4o evidence for public-tell drift; candidate examples for #7, #9, #31a, and #49; corpus/model/date metadata for H24 and H25; explicit human-look-alike and no-authorship cautions.
- **Misuse / overclaim:** using a July 2025 message-level prevalence as a current document threshold, applying any rate to another model or language, treating a publicly shared corpus as representative of private ChatGPT use, or converting the patterns into a probability of assistance.
- **Unsupported use:** generic LLM claims; causal claims about training, prompting, alignment, or product updates; a validated emoji, em-dash, contraction, or vocabulary detector; a single-document authorship verdict; an exact current rate after July 2025.
- **Underused evidence:** the source directly shows fast direction changes and tell decay, including falling `delve` and formal-word rates alongside rising contractions and punctuation. The live catalogue records drift hypotheses but still uses undated flat wording and fail-on-any behavior in some mapped checks.
- **Patterns left on the table:** contraction rise as counterevidence to simplistic formality heuristics; separate human-comparison provenance; one-candidate emoji recognition below the current #31a threshold; `core` and `modern` as dated research candidates rather than blacklist additions.

## Matched patterns / rules

- #7 `no-ai-vocabulary-clustering`: directly recognizes `delve` and `crucial` but requires three vocabulary candidates in one paragraph; does not recognize standalone `core`, `modern`, `ensure`, `various`, `significant`, or `approach` as #7 candidates.
- #9 `no-negative-parallelisms`: directly recognizes `not just X, but Y` and fails one occurrence.
- #31a `no-unicode-flair`, including the folded emoji entry: recognizes all eight charted symbols (sparkles, light bulb, small blue diamond, pushpin, cross mark, fire, brain, and check mark), but each isolated symbol is one candidate and the aggregate finding requires two candidates.
- #49 `no-em-dashes`: recognizes every U+2014 occurrence and fails on any; context gates can suppress the finding in inferred formal-report, dialogue, or fiction contexts.
- H24 `Register-specific vocabulary density` and H25 `Model-family versus generic-AI residue` directly frame the source's drift and model/date limits.
- `human-eyes/references/process.md` product boundary forbids authorship inference and matches the source's explicit human-look-alike warning.

## Associated hypotheses

- H1 `Continuous calibrated register-distance score per pattern`: the source supplies a dated distributional example but no register-matched human baseline beyond selected emoji ratios.
- H7 `Five-check gating grader plus 38-pattern advisory catalogue`: the em-dash trajectory is relevant to calibration, but this source cannot select a gate or threshold.
- H24 `Register-specific vocabulary density`: directly supported by the simultaneous rise and fall of named words in one model/time series.
- H25 `Model-family versus generic-AI residue`: directly supported; every measured rate is GPT-4o-, corpus-, and date-bound.

## Questions / follow-up

- Can The Post's monthly aggregate data, analysis code, prompt/task mix, conversation-level clustering method, and human comparison corpus be obtained for independent evaluation?
- Should #49's fail-on-any and strong-warning behavior be re-evaluated against matched human and GPT-4o prose rather than treated as supported by this source?
- Should #31a retain a two-candidate threshold, and should it distinguish decorative use from ordinary emoji-bearing chat, headings, checklists, quotations, and UI text?
- Should falling `delve` and formal-word rates trigger a dated review of #7 evidence wording before `core` or `modern` is considered?

## Update provenance

The prior card and manifest recorded no snapshot digest. Before replacement, the exact prior 4,129-byte snapshot was hashed as `02b49c0a98cab15651b98f17aadc5f93e7b64f5334beb3ce684cb34ea61c0b3c`, verified byte-for-byte against the committed `f28a370` version, and archived without transformation.

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none found; pre-contract syndicated capture | `snapshots/archive/merrill-wapo-chatgpt-clues/2026-05-05-02b49c0a98ca.md` | 2026-05-05 | `02b49c0a98cab15651b98f17aadc5f93e7b64f5334beb3ce684cb34ea61c0b3c` |
| current | none found | `snapshots/merrill-wapo-chatgpt-clues.md` | 2026-07-16 | `d4b80e1be938b17c278ddca69c33a50d8075cc45b95d7160f5402a8d0a1a3866` |

## Decision history

- DR-109 rejected 2026-07-26 (C04): the `strong 2026 AI-style fingerprint` wording in #49 stays as written. The date- and model-specific evidence objection is not actioned and no citation changes.
- The prior card used no claim IDs, user-decision states, or implementation statuses. It broadly mapped the source to #7, #9, #31a, and #49 and asked whether emoji, `core`, and `modern` should enter the catalogue. This update reopens those mappings as C02-C10 because the complete charts expose drift, human-look-alike, and threshold limits absent from the pre-contract record. No prior user approval or completed product change is inferred.
- C02 approved 2026-07-17 (DR-116): the calibration ran and could not test the question, since no library corpus contains emoji-bearing genres; Mae ruled the threshold unchanged at 2. The 70 percent chat-prevalence figure has no human baseline and anchors nothing.

## Prior-to-current comparison

- **Added:** contract metadata, verified prior digest and archive path, complete syndicated prose, nine-chart inventory, nine preserved attachments, claim IDs C01-C12, source/method boundaries, deterministic project-coverage checks, recommendation states, decision history, and independent review fields.
- **Corrected:** the canonical byline names Jeremy B. Merrill, Szu Yu Chen, and Emma Kumer, whereas the prior syndicated capture attributed only Merrill. The corpus is limited to GPT-4o messages of at least 10 words from 37,929 publicly shared primarily-English conversations; the prior card's broad “English messages” shorthand omitted these selection limits. The refresh also separates measured rates from the authors' journalist, human-likeness, continued-evolution, and spotting interpretations.
- **Removed:** no substantive source claim. The old unqualified prompt to consider adding emoji, `core`, and `modern` as tells is replaced by claim-specific pending `test-adapt` / `do not adopt` recommendations.
- **Unchanged:** source identity, canonical URL, broad mappings to #7, #9, #31a, and #49, and the source's core warning that humans can use every named pattern.
- C06 rejected 2026-07-18 via DR-127: `delve` remains a programmatic #7 match with no date-based demotion, suppression, or evaluation gate.

## Project coverage

This is the authoritative review table. Focused deterministic results below came from the live `human-eyes/scripts/grade.py` implementations on 2026-07-16; they are surface-only coverage checks, not complete Audits.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: The study uses 328,744 GPT-4o messages of at least 10 words from 37,929 publicly shared, primarily English conversations preserved by the Internet Archive, May 2024-July 2025; The Post discloses an OpenAI content partnership. | Direct method and provenance disclosure in data journalism. Large message count but self-selected public shares, one model, unknown task mix, no clustering method, raw data, uncertainty, or partnership role in the analysis. | fully covered by this card's metadata and the source-record contract; H25 supplies the model-family boundary; no runtime check applies. | Shared source summaries currently name Merrill without these selection and partnership limits. | **adopt:** retain the complete model, date, selection, message-length, archive-route, and partnership metadata wherever this source is summarized; documentation verification only. | pending | not started |
| C02: By July 2025, 70 percent of sampled messages contained at least one emoji; the chart shows sparkles, light bulb, small blue diamond, pushpin, cross mark, fire, brain, and check mark, with the check mark near 30 percent and brain near 25 percent. | Direct descriptive result and chart for GPT-4o public-share messages. No human baseline for “any emoji,” no uncertainty, and no genre/task split. | partly covered by #31a `no-unicode-flair`; live focused checks recognize each of the eight charted symbols as one candidate, and each passes alone because the threshold is two. | #31a is a decorative-format rule, not a prevalence model; the source's message-level `at least one` measure does not establish that one emoji is a violation. | **test-adapt:** preserve candidate recognition, then evaluate the two-candidate threshold with matched chat, professional prose, UI, checklist, quotation, and social-post controls before any threshold decision. | approved | implemented |
| C03: The check mark was 11 times the unspecified human comparison rate; the brain and small blue diamond were 10 times the human rate. | Direct source-reported ratios, but the human corpus, matching, counts, and uncertainty are undisclosed. The brain/diamond sentence is ambiguous about whether the reported 10-times ratio applies to each, though the prose grammatically groups them. | partly covered by #31a candidate recognition; the live checker does not identify source-specific emoji types or human-comparison provenance. | No matched-human evidence is reproducible from the page, and a ratio cannot be converted into an authorship probability. | **test-adapt:** treat these three symbols as dated research candidates and seek the comparison data before changing #31a severity, threshold, or report language. | pending | review required |
| C04: Em-dash presence rose from fewer than 1 in 10 messages a year earlier to more than half by summer 2025; the chart ends in the upper 70s, while journalists are an explicit human look-alike. | Direct GPT-4o public-share time series and author-reported human counterexample. No matched human rate, task control, causal explanation, or document-level validation. | challenges current behaviour in #49 `no-em-dashes`: the live focused check finds each U+2014 and fails on any; the catalogue calls it a strong 2026 fingerprint, while this source is dated to July 2025, message-level, model-specific, and explicitly non-exclusive. | The source supports candidate recognition and drift monitoring, not fail-on-any, strong severity, current-2026 wording, or mandatory removal. | **test-adapt:** re-evaluate #49 occurrence/density, genre gates, severity, date wording, and matched-human false positives; do not retain or reverse the current behavior on this source alone. | pending | review required |
| C05: Versions of `not just X, but Y` appeared in 6 percent of July 2025 sampled chats. | Direct source-reported GPT-4o rate, but the article does not disclose which variants counted, a human comparator, raw count, uncertainty, or contextual coding. | partly covered for a literal-form example by #9 `no-negative-parallelisms`; the focused check on `It is not just X, but Y.` finds one occurrence and fails. The source rate cannot be assigned to that exact regex surface without the coding definition. | The WaPo rate cannot establish #9's recall, validate its strong severity or every-occurrence policy, or support an authorship signal; the live rule cites separate Atlantic/Pangram evidence for human comparison. | **test-adapt:** retain the dated 6 percent result as variant-family context, obtain the source coding definition, and test the live regex against included and excluded variants before using Merrill to support coverage or severity. | pending | review required |
| C06: `delve` fell from just above 3 percent near the start of the chart to 1 in 1,000 chats in July 2025. | Direct time series and endpoint in one GPT-4o public-share corpus. No human comparator or explanation for the decline. | challenges current #7 wording: `delve` is a candidate, but the focused single-word example passes because #7 requires three candidates; H24/H25 recognize drift. | Static wording that treats `delve` as a current generic tell can outlive the measured spike. The source does not justify removing candidate recognition or setting a new threshold. | **test-adapt:** date-stamp the Merrill evidence and measure `delve` in current matched registers/models before retaining, demoting, or removing its role in #7. | rejected | not applicable |
| C07: `ensure`, `various`, `crucial`, `significant`, and `approach` all declined over the series. | Direct article statement plus two charts; exact monthly values are not printed. No human comparator, causal account, or claim that absence is human-like. | partly covered: #7 recognizes standalone `crucial` but not the other four as standalone candidates; the focused five-word sentence yields only one #7 candidate and passes. `significant` can appear inside separate phrase and significance checks. | The source is counterevidence to adding these as an undated flat list and does not validate absence as a human signal. | **do not adopt:** do not add the five words as standalone violations from this source; use their decline to audit stale evidence wording and future date metadata. | pending | review required |
| C08: `you're` and `it's` rose to almost one-third of chats; `don't` and `isn't` also rose. The article says this might make ChatGPT sound more human. | Direct time series; “might help” is author interpretation. No human comparison, model-control experiment, or evidence that contractions distinguish authorship. | not covered as a contraction-frequency rule, appropriately. #9 recognizes contractions only when they form negative parallelism; the focused contraction sentence fires #9 for its contrast, not for contraction frequency. Robustness tests include contractions as syntax variants. | A contraction-presence or absence rule would overread a changing, style-sensitive feature. | **do not adopt:** add no contraction-frequency tell; retain the result as drift and false-shortcut evidence in future evaluation design. | pending | not started |
| C09: `core` was five times more common than a year earlier and reached about 12 percent in July 2025. | Direct article result and chart in one dated GPT-4o corpus. No human baseline, sense disambiguation, or task split. | partly covered: #7 lists the phrase `at its core`, but the live focused sentence with standalone `core` produces zero #7 candidates and passes. | The source does not establish that standalone `core` is specific, harmful, or current outside this corpus. | **test-adapt:** keep `core` out of the standalone blacklist; test sense-, phrase-, model-, date-, and register-specific frequency before any catalogue proposal. | pending | not started |
| C10: `modern` exceeded 8 percent in July 2025 after rising from the prior year. | Direct article result and chart in one dated GPT-4o corpus. No human baseline, sense disambiguation, or task split. | not covered by #7; the live focused standalone example produces zero #7 candidates and passes. | A common adjective with one model-specific rise has weak standalone specificity. | **do not adopt:** do not add standalone `modern`; retain it only as a dated H24/H25 research example unless matched comparison evidence appears. | pending | not started |
| C11: The authors say language probably continued to evolve after the July endpoint. | Author interpretation grounded in observed within-series changes, not a measurement beyond July. | fully covered conceptually by H24, H25, and existing pattern-opportunities rows on source-date/model metadata and model-family residue. | Open hypotheses are not runtime safeguards, and source summaries can still omit dates. | **adopt:** treat model/version/date metadata as mandatory for imported examples and schedule drift review rather than implying the July rates are current. | pending | not started |
| C12: The patterns might help spot ChatGPT-assisted emails/documents, but every pattern can also appear in human writing. | Author interpretation plus explicit limitation. The article provides no combination rule, validation set, error rate, probability, or authorship ground truth. | fully covered by `human-eyes/references/process.md`'s product boundary and the catalogue's general cluster/no-single-proof framing; challenged locally where #49 still fails any U+2014. | Source-level caveats must travel with mapped rule citations; surface output is not an authorship verdict or complete Audit. | **adopt:** keep the no-authorship and human-look-alike boundary explicit in every Merrill mapping; take no detector or attribution claim from this source. | pending | not started |

## Recommendations

- C01: **adopt** the complete provenance, sample, model, date, selection, length, and partnership limits in source summaries.
- C02: **test-adapt** #31a's candidate threshold with matched genre and formatting controls; make no immediate threshold change.
- C03: **test-adapt** the selected emoji ratios only after the human comparison corpus becomes inspectable.
- C04: **test-adapt** #49's occurrence/density, genre, severity, and date behavior; this source does not validate fail-on-any.
- C05: **test-adapt** the live #9 regex against the source's undisclosed variant family; keep the dated 6 percent result as context, not exact-form validation.
- C06: Keep `delve` in programmatic #7 without date-based demotion, suppression, or a new evaluation gate.
- C07: **do not adopt** the five declining formal words as standalone violations; use them to audit stale evidence wording.
- C08: **do not adopt** contraction presence or absence as a tell; preserve the result as drift evidence.
- C09: **test-adapt** standalone `core` only with sense-, model-, date-, and register-aware controls.
- C10: **do not adopt** standalone `modern` from this source.
- C11: **adopt** mandatory model/version/date metadata and scheduled drift review for imported examples.
- C12: **adopt** the explicit human-look-alike and no-authorship boundary; make no detector claim.

## Evaluation of approved changes

- C01: not applicable - recommendation pending; no product change made.
- C02: passed - the DR-116 calibration ran 2026-07-17 (`dev/evals/unicode-flair-calibration-2026-07-17.md`) and could not test the threshold: the library corpora are essays (1/55 human and 2/38 generated texts contained any symbol) and the genre fixtures were constructed, not sampled, so no like-for-like emoji measurement exists. Mae ruled the threshold stays at 2 as the no-evidence default. Candidate recognition was verified live, including variation-selector forms.
- C03: not applicable - recommendation pending; no product change made.
- C04: not applicable - recommendation pending; existing #49 behavior marked review required.
- C05: not applicable - recommendation pending; existing #9 behavior marked review required.
- C06: not applicable - rejected via DR-127; `delve` remains in #7 and the detector is unchanged.
- C07: not applicable - recommendation pending; existing #7 mapping marked review required.
- C08: not applicable - recommendation pending; no product change made.
- C09: not applicable - recommendation pending; no product change made.
- C10: not applicable - recommendation pending; no product change made.
- C11: not applicable - recommendation pending; no product change made.
- C12: not applicable - recommendation pending; no product change made.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/merrill_source_reviewer`, fresh, source-dedicated, and read-only; five-lens semantic review followed by same-reviewer focused checks of materially changed provenance, claims, coverage, recommendations, status, and comparison text
- **Findings resolved:** seven initial findings resolved; the first focused re-check left one byline-comparison finding, which was corrected and passed a second focused re-check
- **Unresolved findings:** none
