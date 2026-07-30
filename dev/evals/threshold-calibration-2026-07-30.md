# Threshold calibration (2026-07-30)

Record for DR-175: three of the sixteen inherited cut-offs move, thirteen stay.

## Method

Every declared value in `CHECK_THRESHOLDS` was mutated in memory, one key at a
time, and its check re-run alone across `samples/human-sourced` (63 documents)
and `samples/generated-ai` (49). Documents a check skips carry no verdict and are
excluded rather than counted clear, the correction DR-164's audit records. The
mechanism is DR-170's: the value under test is the one the check reads.

`no-boldface-overuse` and `no-tidy-paragraph-endings` gate on a count and a rate
together, so a single-key sweep leaves the count gate deciding everything. Both
were swept across a 6-by-5 grid of the two keys instead.

## The criterion was corrected before anything moved

The first pass ranked candidate values by the gap between the two corpora,
which treats the checker as an authorship detector. It is not one, and rule 1 of
`dev/decision-walkthrough-approach.md` has said so since the register opened. A
human document with flat paragraphs has flat paragraphs, and reporting it is the
check working rather than a cost to be minimised.

Two proposals died on that correction, both of which the gap criterion had
ranked first:

| proposal | what it did |
|---|---|
| `no-staccato-sequences` run 3 to 6 | stopped flagging 7 human documents, flagged no more generated ones |
| `overall-signal-stacking` score 4 to 5 | stopped flagging 14 human and 8 generated documents |

Neither found a wrong flag. Both only reported less.

## Three cut-offs moved

| check | from | to | generated flagged | human flagged |
|---|---|---|---|---|
| `paragraph-length-uniformity` | CV 0.18 | CV 0.26 | 15/45 to 31/45 | 3/58 to 10/58 |
| `no-excessive-hedging` | 3 found | 2 found | 5/49 to 12/49 | 3/63 to 7/63 |
| `no-tidy-paragraph-endings` | 3 found, 1.0 per 1000 | 1 found, 0.5 per 1000 | 0/49 to 9/49 | 1/63 to 4/63 |

Each stops where the next step costs as many human documents as it gains
generated ones. Hedging at 1 found is +9 and +9. Paragraph uniformity at 0.30 is
+6 and +5.

`no-tidy-paragraph-endings` was reachable only after both keys were swept
together. At 3 candidates the count gate held the check at 1 human document and
none generated, which read as a check no value could correct.

## The band that decided paragraph uniformity

Ten documents sit between CV 0.22 and 0.26, seven generated and three human. The
three human ones are `10-human-opinion` at 0.239, whose paragraphs run 58, 77,
65, 49, 81, 43, 45 and 58 words, and two Henneke Duistermaat marketing posts
written to a house template, at 0.225 and 0.257.

Mae ruled the band a correct catch on 2026-07-30. Uniform blocks are the finding
whoever produced them, so the question is whether the paragraphs are uniform and
not whether a person wrote them.

`10-human-opinion` is a human passthrough fixture in `test_grade.py`, so the
ruling has a test consequence recorded below.

## Thirteen stayed

| check | cut-off | why it did not move |
|---|---|---|
| `no-forced-triads` | 4.0 per 1000 | best value across 1.0 to 10.0 |
| `no-unicode-flair` | 2 found | identical result at 1 |
| `sentence-length-variance` | stdev 9.0 | 10 costs 7 human documents to gain 6 |
| `no-excessive-lists` | 8 items | same result at 3 through 8, worse above |
| `no-boldface-overuse` | 4 found, 2.0 per 1000 | no cell of 30 separates; generated sits at 1/49 throughout |
| `no-bland-critical-template` | 3 found | flat from 1 to 8 |
| `no-soft-scaffolding` | 2 found | 1 rests on 1 human and 5 generated documents |
| `no-compound-modifier-density` | 3 per sentence | 2 rests on a single generated document |
| `no-rhetorical-questions` | 1 found | fires only on human prose at every value; DR-174 |
| `no-heading-one-liners` | 2 found | same; DR-174 |
| `no-orphaned-demonstratives` | 3 found | same; DR-174 |
| `no-rubric-echoing` | 3 found | neither corpus contains the pattern; DR-164 cause 2 |
| `no-inline-header-lists` | 2 found | same |
| `no-symmetric-list-items` | 3 items | same |

`no-soft-scaffolding` and `no-compound-modifier-density` are the two the corpus
cannot answer. Whether one soft-scaffolding phrase or two compound modifiers in
a sentence is a fault is a source-evidence question, and 112 documents holding
six instances between them cannot settle it.

## Effect on shipped output

`overall-signal-stacking` rolls up the three moved checks. Across the corpora it
goes from 45/63 human and 45/49 generated to 48/63 and 46/49, so three human and
one generated document now cross the overall gate that did not before.

All 11 pinned render baselines were recaptured. They were already stale at HEAD:
`8849299` added `metric_number` to two checks after the last recapture, and the
one flagged-count change that runs downward, `21c-alamut-agora-museum` at 14 to
13, predates this work. Six documents gain a flag from the three moves.

Two test fixtures asserted the old hedging cut-off by requiring two hedges to
pass, and now assert the new one by requiring them to fail. Two tidy-endings
assertions did the same at two candidates. `paragraph-length-uniformity` and
`overall-signal-stacking` join the five checks already excluded from the
`10-human-opinion` passthrough loop, each with a comment naming its share, the
form DR-159, DR-66 and DR-79A used. `overall-signal-stacking` is the first
roll-up to carry such an exclusion, and it carries it only because a component
it sums does.
