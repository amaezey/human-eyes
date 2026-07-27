# How evenly specialist vocabulary sits within a draft (2026-07-27)

Measured while closing DR-168. **No check was built.** This record exists so the
result is not lost and so nobody measures it again from scratch.

## The question

`even_jargon_distribution`, retired under DR-168, claimed that human writers bunch
their specialist words where they know the material and thin out elsewhere, while
generated prose spreads the same words evenly. Nothing in the source library
supported the claim, and a search of the published literature found nobody had
measured it. So it was measured here.

## Method

150-word windows with a 25-word step, the same windowing `vocabulary-diversity`
(B5) already uses, so the catalogue keeps one convention. For each window, the
share of content words that are 9 letters or longer. Across the windows, the
standard deviation over the mean. Low means evenly spread.

Corpora: `dev/evals/samples/human-sourced` (63 documents) and
`dev/evals/samples/generated-ai` (46 measurable; 3 skipped as shorter than one
window).

Two other definitions of "specialist" were tried: words absent from the 40,000-word
Brysbaert concreteness list, and words rated below 2.5 for concreteness. Both
separated the corpora in the same direction but less sharply, so long words carried
the measure.

## Result: the claim holds

| | human | generated |
|---|---|---|
| lowest | 0.164 | 0.049 |
| 5th percentile | 0.219 | 0.105 |
| median | 0.326 | 0.222 |
| 95th percentile | 0.512 | 0.433 |
| highest | 0.667 | 0.484 |

Generated prose spreads long words more evenly. The best single cut-off, 0.238,
flags 27 of 46 generated documents and 7 of 63 human ones: **76% accuracy** against
a 57% baseline from always guessing human.

An earlier pass reported 80%. That figure was fitted on the same documents it was
measured over. 76% is the figure from the sweep above and is still optimistic for
the same reason; a shipped threshold would need a held-out check.

Two controls that a length or restatement artefact would have failed:

- **Length.** The human corpus runs to a 1,600-word median against 846 generated.
  Restricting both to the overlapping 453 to 3,537-word band leaves 56 human and 44
  generated documents and moves accuracy to 78%. Not a length artefact, and worth
  stating because length bias is what made E5 look reversed in DR-66.
- **Mean versus spread.** Generated prose uses *more* long words (0.204 against
  0.157) and *more* abstract words (0.411 against 0.378) while spreading them more
  evenly. The level and the spread move in opposite directions, so the spread is not
  a restatement of the level.

## Why no check was built

The three checks that already measure the *level* of this vocabulary catch **42 of
the 46 generated documents between them**: B5 `vocabulary-diversity`, B13
`word-length-average`, B14 `concreteness-average`.

On the four generated documents all three miss, the spread measure at 0.238 flags
**none of them**, and flags 2 of the 41 human documents that also slip through. So
where a fourth check could add coverage it adds none, and costs false positives.
Where the spread does separate the corpora is among documents the level checks have
already flagged, which is confirmation rather than coverage.

That is not the overlap the standing rule protects. "Overlap is not a reason to
reject a check" covers a measure with independent signal that happens to co-fire,
which is also why "catches documents nothing else catches" was ruled out as a test.
This measure has no signal on the cases that slip through.

Caveat on strength: four documents is too small a sample to separate "adds nothing"
from "not enough data to tell". The 42-of-46 figure does not depend on that sample
and is the load-bearing number.

## What this supports

Read it as corroborating context for B13 and B14 rather than as a pattern of its
own. Generated prose in these corpora reaches for long, abstract words *and*
distributes them flatly. B13 and B14 already flag the first, which turns out to be
enough.

If the level checks are ever loosened or retired, this measure is worth
re-testing: it becomes load-bearing only once the level checks stop catching those
42 documents.

Reproduce with the method above; no script was committed, because the measure is
not part of the product.
