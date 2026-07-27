# False ranges (A6): corpus calibration, 2026-07-25

Measured before building the check, to decide whether the stacked `from X to Y`
shape separates the corpora or whether the pattern needs meaning the grader
does not have.

## Method

Every document of 50 words or more under `dev/evals/samples/human-sourced`,
`dev/evals/samples/pilot-additions-01/human-sourced` (human) and
`dev/evals/samples/generated-ai`, `dev/evals/samples/pilot-additions-01/generated-ai`,
`dev/evals/samples/pilot-additions-01/raw-ai` (generated). Sentences split on
terminal punctuation. A pair is `from` … `to` within one sentence, with at most
70 characters and no clause-ending punctuation between the two words.

## Result

| | Documents | Words | Stacked sentences | Rate per 1000 words | Single pairs | Rate per 1000 words |
|---|---|---|---|---|---|---|
| Human | 73 | 141,806 | 2 | 0.014 | 86 | 0.61 |
| Generated | 68 | 58,288 | 4 | 0.069 | 28 | 0.48 |

Stacked pairs run about five times more often in the generated corpora. The
single-pair control moves the other way: one `from X to Y` is slightly more
common in human prose. That contrast is why the check requires stacking and
never speaks about a single pair.

## What this does not establish

The stacked counts are 2 and 4 sentences. The ratio would move with more data.
Direction is consistent across both corpora and the single-pair control
supports it, which is what the decision rested on.

Reading the same data as document percentages understates the difference (3%
against 6%) because the generated corpora hold well under half the words. Rate
per 1000 words is the comparable figure.

## Decision

DR-157, approved by Mae 2026-07-25. Catalogue entry A6 becomes programmatic
`no-false-ranges` at context warning: one sentence stacking two or more pairs
produces a finding. The semantic reading, whether a single pair's endpoints sit
on a shared scale, was not adopted.
