# Triad density calibration (2026-07-25)

Record for DR-19G: the direction and threshold of pattern B4, and the retirement of #10a.

## The question

B4 `no-forced-triads` failed on any single three-part construction. #10a `no-triad-density` failed at four or more triads in prose of 300+ words. Both called the same extractor, `extract_triad_candidates`, so #10a's condition was a strict subset of B4's and could never fail without B4 having already failed. The density check never changed a verdict.

The Wikipedia cleanup guide (C15) says an isolated triad is not overuse and asks that recognition and verdict stay separate. That framing was tested rather than adopted.

## Corpus

`dev/evals/samples/human-sourced` (55 documents of 300+ words, 47 of them 21st century, median 1,813 words) against `dev/evals/samples/generated-ai` (38 documents of 300+ words, median 923 words). Rates are per 1000 words, so the length difference between the two sets does not drive the comparison.

## Counting does not separate the groups

| documents containing | human | AI |
|---|---|---|
| at least 1 triad | 95% | 100% |
| at least 2 triads | 89% | 95% |
| at least 3 triads | 82% | 79% |
| at least 4 triads | 71% | 74% |

At every count, human and generated prose are indistinguishable. B4's one-triad verdict flagged 95% of human documents. #10a's four-triad threshold was cleared by 71% of them, because a long document accumulates triads whatever wrote it.

## Rate does separate them

Median triads per 1000 words: **2.68 human, 5.33 AI**. Roughly double.

| threshold per 1000 words | AI flagged | human flagged |
|---|---|---|
| 3.0 | 74% | 44% |
| 3.5 | 71% | 25% |
| **4.0** | **66%** | **24%** |
| 4.5 | 58% | 16% |
| 5.0 | 53% | 15% |
| 5.5 | 47% | 9% |
| 6.0 | 42% | 7% |

## Ruling

Both checks were consolidated into one, measured as a rate, at **4.0 per 1000 words** in prose of **300 words or more**. B4 keeps its context-warning severity. #10a is retired.

The 300-word floor is inherited from the retired #10a. It has no effect on these figures, since every document in both corpora exceeds it; it stops the check speaking about texts too short to measure a rate.

4.5 was proposed as the knee of the curve. 4.0 was chosen, accepting 8 points more human flagging for 8 points more AI coverage.

## Limits

Two corpora from one project, not held out. The threshold describes where these two sets separate, not a general population rate. A single triad is still recognised and reported as a candidate; only the verdict now depends on the rate.
