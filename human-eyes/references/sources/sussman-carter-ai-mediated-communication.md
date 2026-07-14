# Sussman and Carter: AI-mediated communication, complexity, and sentiment

## Metadata

- **URL:** https://arxiv.org/abs/2504.19556
- **Authors:** Kristen Sussman and Daniel Carter
- **Published:** 2025-04-28; Companion Proceedings of the ACM Web Conference 2025
- **Extracted:** 2026-07-14
- **Source type:** Empirical computational communication study
- **Evidence tier:** Conference companion paper / empirical
- **Extraction status:** reviewed from complete saved PDF text
- **Full text snapshot:** `snapshots/sussman-carter-ai-mediated-communication.md`

## Study design

- Compares 970,919 tweets mentioning Donald Trump from the 2020 US election period with 20,000 tweets from the corresponding 2024 election period.
- Measures Flesch-Kincaid readability and sentiment polarity.
- Separately prompts an AI-mediated communication system to improve example tweets and compares original and rewritten text qualitatively and with cosine similarity.

## Direct findings

- Mean sentiment polarity increased from `0.04` in 2020 to `0.12` in 2024.
- Neutral tweets fell from `54.8%` to `39.8%`; positive tweets rose from `28.6%` to `45.9%`.
- The paper reports higher readability scores and interprets them as lower linguistic complexity and more accessible wording.
- AI-improved examples add future-oriented solutions and direct calls to action such as choosing leaders, unity, and next steps.
- Two original/rewrite pairs had cosine similarities of `0.376` and `0.398`; the authors describe substantial linguistic restructuring while retaining the core message.
- The paper explicitly notes that political climate, platform dynamics, audience changes, and the distinctive communication context prevent clean isolation of AI as the only cause of the 2020-to-2024 shift.

## Project incorporation

- **#4 promotional language — adds evidence:** the aggregate corpus shifted towards more positive and less neutral expression.
- **#24 generic positive conclusions — expands the check:** the AI rewrites added prescriptions and calls to action that were absent from the originals, including choosing better leaders and calling for unity.
- **#37 neutrality/stance — challenges a one-way account:** AI rewriting can erase a position through false balance, but these examples moved in the other direction by adding a more positive, prescriptive stance.
- **New rewrite-fidelity candidate:** when the task is only to improve clarity or engagement, check whether the rewrite invents a solution, next step, call to action, or political prescription that the source never made.
- **Structural/readability research:** shorter words and higher readability are potential corpus measurements. The paper does not establish them as a document-level prose check.
- **Rewrite magnitude:** the low cosine-similarity examples show extensive rewording under an apparently limited improvement instruction. This is evidence for comparing the rewrite with its source, not a standalone surface tell.

## Recommendations for human-eyes

1. Add this source to #4's evidence for generic positive/promotional drift.
2. Expand #24 to include invented future solutions, prescriptions, unity appeals, next steps, and calls to action.
3. Consider a rewrite-fidelity assessment for changes that add a position or proposed solution absent from the source.
4. Treat sentiment, readability, and rewrite magnitude as potential corpus measurements rather than automatic document findings.
5. Keep the paper's time/corpus comparison distinct from Wikipedia's older-model-versus-newer-model interpretation.

These are recommendations from the evidence review. No checker, rule, threshold, or fixture was changed as part of this source-card work.

## Matched patterns / rules

- #4 promotional language
- #24 generic positive conclusions
- #37 neutrality / stance context
- #41 social-media and political-communication genre context
- rewrite semantic-preservation process

## Associated hypotheses

- H12 genre-aware threshold calibration
- H24 register-specific vocabulary density
- H25 model-family and time-specific residue
