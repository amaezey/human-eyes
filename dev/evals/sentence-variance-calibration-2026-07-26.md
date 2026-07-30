# Sentence-variance calibration (2026-07-26)

Record for DR-79A: G9 `sentence-length-variance` moves from a standard
deviation threshold of 4 to 9, and no average-sentence-length check was built.

## The check was inert

G9 fails a document when the standard deviation of its sentence word counts
drops to 4 or below. Measured across the 62-human and 46-generated documents of
300 words or more, it flagged **zero of 108**.

The reason is that the threshold sits underneath the entire observed range. The
flattest document in either corpus reaches 4.4. Human prose runs a median 12.3
and generated prose 7.6.

The threshold dates to the initial commit. No source supplied it. DR-04 changed
G9's eligibility rule in 2026-07-17 and did not touch it. The one source that
proposed a concrete number, AI Detectors' 15-to-20-word sentence band, was
explicitly rejected as unvalidated.

The check itself works. Handed artificially uniform prose it fails correctly,
which is why its test fixture passes: that fixture is hand-written to be flat at
SD 0.66, a value real prose never reaches.

**A check that returns clean on every document reads the same as a check that
measures nothing.** Compare the threshold against the observed distribution, not
against the pass rate.

## Threshold

| SD threshold | generated flagged | human flagged |
|---|---|---|
| 4 (inherited) | 0% | 0% |
| 7 | 33% | 5% |
| 8 | 54% | 8% |
| **9 (chosen)** | **72%** | **11%** |
| 10 | 85% | 23% |

At 9 this is the widest separation in the catalogue. For reference B7 runs
70%/24%, B4 66%/24%, B10 57%/29%, B8 52%/27%, B11 50%/18%, and the E5
short-sentence branch 48%/21%.

## Two confound checks

**Era.** The human corpus holds eight pre-1950 literary documents whose long
sentences could inflate the human side on their own. They sit at a median SD of
14.4 against 12.0 for the modern human documents. Dropping them entirely leaves
the separation intact, so the result is not an artefact of corpus vintage.

**Matched pairs.** Four human documents in the corpus have a generated rewrite
of the same piece. Mean sentence length falls in every one: 27.3 to 19.1, 24.9
to 14.3, 20.0 to 15.6, 16.4 to 12.0. Four pairs has no power on its own, and
DR-159's second lesson warns against using a subset this small to overturn a
larger result. Used here only as corroboration of a 108-document finding, not as
evidence in its own right.

## Not affected by the one-occurrence length bias

The DR-66 close established that share-of-documents comparisons are
length-biased for checks firing on a single occurrence, because the human corpus
averages 2,172 words per document against the generated corpus's 1,051. G9 is a
document-level statistic over every sentence, so its threshold is already
normalised and the bias does not apply. The same holds for the mean.

## Average sentence length: DR-79B, folded into E5

Lu et al. list sentence length among six classifier inputs and supply no
direction or threshold for any of them, so the direction was measured here.
Generated prose averages 13.9 words per sentence against 17.7 for human prose,
holding at 13.9 against 17.5 with the pre-1950 documents removed.

| mean-length threshold | generated flagged | human flagged |
|---|---|---|
| 13 words | 43% | 8% |
| 15 words | 70% | 19% |

15.0 was chosen, in prose of 300 words or more, folded into E5 rather than
given a pattern number. That follows the DR-66 precedent for the short-sentence
rate: existing check, adjacent territory, no new number.

Two figures for the same branch, both true and easy to confuse:

- **Within E5**, it adds 9 generated and 3 human documents, taking E5 from
  54% to 74% on generated prose and 53% to 58% on human prose.
- **Against the union of the retuned G9 and E5**, it adds 1 generated
  document and 0 human ones, because mean and standard deviation correlate at
  r=0.71 and the G9 retune already absorbs most of the territory.

The second figure is the one that matters for deciding whether the project
gained coverage; the first is the one that matters for reading E5's rates.

Fixing a broken check absorbed most of what a new one would have caught. Check
whether an existing mechanism is merely miscalibrated before proposing an
adjacent one.

## Evidence the branch surfaces

A mean is a document-level finding with no offending span, but a bare number is
not usable. The branch quotes up to five prose sentences whose length sits
within three words of the mean, which is a real illustration of the band rather
than an allow-list exemption from `test_phrase_capture_coverage.py`.

## Other DR-79 features

Of the six static features Lu et al. name, type-token ratio is already B5. Noun
ratio and verb ratio need a part-of-speech tagger; average dependency depth and
distance need a parser. No tagger or parser is installed, and unlike the
Reinhart features in DR-159, none of these four has a defensible surface proxy.
B7 already counts one slice of noun-heaviness through nominalisation suffixes.

The paper's 128 syntax-semantic n-gram features are learned model inputs and
cannot be enumerated from the publication.

## Fixture consequence

`samples/human-sourced/legacy/10-human-opinion.md` runs SD 7.56 across 36
sentences and now flags. It is excluded from the human-passthrough loop in
`test_grade.py`, alongside the DR-159 and DR-66 rate checks, on the same
principle: these checks flag a calibrated share of human prose by design, and
raising a threshold to clear one fixture fits the instrument to the fixture.
