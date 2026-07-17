# #53 windowed type-token calibration, 2026-07-17

Calibration record for the vocabulary-diversity direction flip. Corpus: `dev/evals/samples/human-sourced` (73 eligible texts) and `dev/evals/samples/generated-ai` (58 eligible), texts of 150+ stripped words. Decision: Mae, 2026-07-17 (two-tier: flag at 0.71, upper tier at 0.74).

## Why the old rule was replaced

Whole-text type-token ratio, flagging at or below 0.40, measured on this corpus: flags 64% of human samples and 9% of generated samples. The direction was backwards in practice, consistent with El Attar et al., Suvanto et al., and the Przystalski surface run.

Raw whole-text ratio by length band (AI higher in every band; both fall with length):

| Text length | Human mean | AI mean |
|---|---|---|
| 150-400 words | 0.57 | 0.66 |
| 400-800 words | 0.49 | 0.55 |
| 800+ words | 0.34 | 0.46 |

Human samples run longer (median 1,474 words vs 823), so a single whole-text threshold cannot be fair across lengths.

## The replacement metric

Mean type-token ratio over sliding 150-word windows, 25-word step. Distributions:

| Group | p25 | median | p75 |
|---|---|---|---|
| Human (n=73) | 0.610 | 0.651 | 0.682 |
| Generated (n=58) | 0.706 | 0.722 | 0.746 |

Threshold trade-off:

| Flag at | Generated flagged | Human flagged |
|---|---|---|
| 0.69 | 88% | 23% |
| 0.70 | 79% | 18% |
| **0.71 (chosen)** | **71%** | **10%** |
| 0.72 | 55% | 3% |
| 0.73 | 45% | 1% |
| 0.74 (upper tier) | 38% | 0% |

0.74 was the highest windowed score observed among human samples, so the evidence line marks values from 0.74 as above the observed human range.

## Limits

Mixed genres and models, 131 samples, no per-genre calibration. Re-run this measurement when the corpus grows or the sample mix changes; the thresholds are corpus-tuned, not universal.
