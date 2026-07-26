# Word length calibration (2026-07-26)

Record for DR-97: new check #71 `word-length-average`, and why it ships against its source's stated direction.

## The measure

The mean length in characters of every word in the piece. Letters and internal apostrophes count; Markdown punctuation, numerals, and symbols do not. Fails at 4.80 or above in prose of 300 words or more, at context-warning severity.

It quotes nothing. There is no offending span, because the signal is the register of the whole draft. It reports a metric string instead, the same way #52 and #53 do.

## The source points the other way

Sussman and Carter, claim C08: average word length **fell** 6.6% between their 2020 and 2024 corpora, from 7.188 to 6.715 characters, Cohen's d of -0.182.

That is the opposite direction to the one measured here, and the check ships on this project's measurement rather than theirs. The reasons are mechanical, not about evidence grade:

- Their corpora carry no AI labels. The 2024 set is treated as more AI-influenced because of its date, which is a temporal association rather than a measurement of AI use.
- The two corpora come from different acquisition sources (Kaggle and Meltwater) at very unequal sizes, 970,919 posts against 20,000.
- Their absolute values, 7.188 and 6.715 characters per word, sit far above ordinary English prose, which suggests their tokenisation counts something this project's does not, probably URLs, hashtags, or handles. The card records that units and tokenisation are unspecified.
- The effect they report is small, d = -0.182.

This project's corpora are directly labelled human and generated, and four documents exist as a human original beside its AI rewrite. That is the stronger design for this question, so it decides it. The Sussman and Carter direction is recorded rather than dismissed: if a labelled social-media corpus is ever added here, this is the first check to re-measure.

## Corpus

`dev/evals/samples/human-sourced` against `dev/evals/samples/generated-ai`, documents of 300 words or more after front matter is stripped: 62 human, 46 generated.

## Result

| measure | human | generated | ratio |
|---|---|---|---|
| document median | 4.58 | 4.95 | 1.08 |

The two groups barely overlap despite the small gap in medians, because both distributions are tight:

```
chars per word   human                       generated
4.0 - 4.2        ###
4.2 - 4.4        #########
4.4 - 4.6        ##################          ######
4.6 - 4.8        #####################       ##########
------------------------------- line at 4.80 -------------------------------
4.8 - 5.0        #####                       #########
5.0 - 5.5        ###                         ################
5.5 - 7.0                                    #####
```

| threshold | human | generated | separation |
|---|---|---|---|
| **4.80** | **13%** | **67%** | **54** |

That is the second widest separation in the catalogue, behind #52's 60 points and ahead of #65's 51 and #10's 47.

## Two controls

**Genre.** The human corpus holds a run of nineteenth-century fiction, which uses short words: Gilman at 3.91, Poe and Austen at 4.00. If the result were genre rather than authorship, removing them would collapse it. Excluding every nineteenth-century document leaves 54 points at 4.79, unchanged.

**Paired documents.** Four documents exist as a human original and its AI rewrite. All four rise:

| original | rewrite |
|---|---|
| 4.69 | 5.07 |
| 4.81 | 5.50 |
| 3.93 | 5.79 |
| 4.58 | 5.02 |

Unanimous, though four pairs is a small number and cannot carry the result alone.

## Overlap with #65

Of the 30 generated documents this check flags, #65 `no-nominalisation-rate` already flags 27. Of the 8 human documents, #65 already flags 6. Nominalisations are long words, so the two measures move together.

Three arguments against adding it were raised and none survived:

- **"It duplicates #65."** It flags 3 generated documents #65 misses, and it separates better, 54 points against 51.
- **"It gives the writer nothing to act on."** Metric-only checks are explicitly supported: `test_phrase_capture_coverage.py` carries an allow-list for checks whose signal is a draft-wide number, and #52, #53 and #10 all sit in it. #52 is the strongest check in the catalogue and names no sentence.
- **"Two correlated checks inflate signal stacking."** They do not. `overall-signal-stacking` runs off a fixed list of 13 checks and neither #65 nor #71 is on it.

## What the fixtures do and do not prove

The failing fixture is council-report prose at 5.98 characters per word, inside the observed generated range, where four documents exceed 5.5. The passing fixture is plain narrative at 3.27.

Neither sits near 4.80, so the threshold itself is pinned separately with words of controlled length: 400 five-letter words must fail and 400 four-letter words must pass. A fixture written to trip a check proves the code path runs and says nothing about whether the threshold sits where prose lives, which is how #52 went three years without ever firing.
