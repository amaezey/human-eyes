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

## Matched patterns / rules

- B1 `no-ai-vocabulary-clustering`: directly recognizes `delve` and `crucial` but requires three vocabulary candidates in one paragraph; does not recognize standalone `core`, `modern`, `ensure`, `various`, `significant`, or `approach` as B1 candidates.
- B3 `no-negative-parallelisms`: directly recognizes `not just X, but Y` and fails one occurrence.
- G4 `no-unicode-flair`, including the folded emoji entry: recognizes all eight charted symbols (sparkles, light bulb, small blue diamond, pushpin, cross mark, fire, brain, and check mark), but each isolated symbol is one candidate and the aggregate finding requires two candidates.
- C7 `no-em-dashes`: recognizes every U+2014 occurrence and fails on any; context gates can suppress the finding in inferred formal-report, dialogue, or fiction contexts.
- H24 `Register-specific vocabulary density` and H25 `Model-family versus generic-AI residue` directly frame the source's drift and model/date limits.
- `human-eyes/references/process.md` product boundary forbids authorship inference and matches the source's explicit human-look-alike warning.

## Associated hypotheses

- H1 `Continuous calibrated register-distance score per pattern`: the source supplies a dated distributional example but no register-matched human baseline beyond selected emoji ratios.
- H7 `Five-check gating grader plus 38-pattern advisory catalogue`: the em-dash trajectory is relevant to calibration, but this source cannot select a gate or threshold.
- H24 `Register-specific vocabulary density`: directly supported by the simultaneous rise and fall of named words in one model/time series.
- H25 `Model-family versus generic-AI residue`: directly supported; every measured rate is GPT-4o-, corpus-, and date-bound.

## Prior-to-current comparison

- **Added:** contract metadata, verified prior digest and archive path, complete syndicated prose, nine-chart inventory, nine preserved attachments, claim IDs C01-C12, source/method boundaries, deterministic project-coverage checks, recommendation states, decision history, and independent review fields.
- **Corrected:** the canonical byline names Jeremy B. Merrill, Szu Yu Chen, and Emma Kumer, whereas the prior syndicated capture attributed only Merrill. The corpus is limited to GPT-4o messages of at least 10 words from 37,929 publicly shared primarily-English conversations; the prior card's broad “English messages” shorthand omitted these selection limits. The refresh also separates measured rates from the authors' journalist, human-likeness, continued-evolution, and spotting interpretations.
- **Removed:** no substantive source claim. The old unqualified prompt to consider adding emoji, `core`, and `modern` as tells is replaced by claim-specific pending `test-adapt` / `do not adopt` recommendations.
- **Unchanged:** source identity, canonical URL, broad mappings to B1, B3, G4, and C7, and the source's core warning that humans can use every named pattern.
- C06 rejected 2026-07-18 via DR-127: `delve` remains a programmatic B1 match with no date-based demotion, suppression, or evaluation gate.
