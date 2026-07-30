# Threshold distribution audit (2026-07-28)

Record for DR-164: every declared cut-off measured against the range real documents
produce.

## The question

DR-79 found G9 `sentence-length-variance` had never fired on any corpus document,
because its inherited threshold of 4 sat below the entire observed range. Its test
passed throughout, on a fixture hand-written to be flat at a value real prose never
reaches. This audit asks whether any other cut-off is in that position.

A first smoke pass reported 18 checks that never flag a generated document and 19 that
flag more human documents than generated. That pass was an inventory, not a finding.
Three causes produce those symptoms and need opposite responses:

1. A threshold outside the observed range is a defect. That is G9.
2. A corpus holding no instance of the target is silent, not broken.
3. For a check firing on one occurrence, a share-of-documents comparison is
   length-biased.

## Corpus

`dev/evals/samples/human-sourced`, 63 documents, mean 2,254 words, against
`dev/evals/samples/generated-ai`, 49 documents, mean 1,027 words. The human documents
average **2.2 times the length** of the generated ones, which is what makes cause 3
live rather than theoretical, and is how E5 was misreported as running backwards
during DR-66.

## Two cut-offs could not be measured until they were instrumented

`sentence-length-variance` and `paragraph-length-uniformity` decide on a standard
deviation and a coefficient of variation the result never carried. Both flagged
documents while reporting no number a reader or a sweep could see. `metric_number` was
added to each in `8849299`, additively; no existing field moved. This also explains a
gap DR-170 recorded without diagnosing — both are among the cut-offs its test could
only mark consumption-only, because with no exposed metric there is nothing to assert
a boundary against.

## Result: no threshold sits outside its observed range

| check | declared | human range | generated range | flagged h/g |
|---|---|---|---|---|
| `no-bland-critical-template` | 3 candidates | 0–0 | 0–11 | 0% / 2% |
| `no-boldface-overuse` | 4 candidates | 0–9 | 0–15 | 8% / 2% |
| `no-compound-modifier-density` | 3 per sentence | 0–0 | 0–0 | 0% / 0% |
| `no-excessive-hedging` | 3 candidates | 0–5 | 0–7 | 5% / 10% |
| `no-excessive-lists` | 8 items | 0–36 | 0–36 | 0% / 10% |
| `no-forced-triads` | 4.0 per 1000 | 0–24 | 0–20 | 22% / 65% |
| `no-heading-one-liners` | 2 candidates | 0–8 | 0–0 | 8% / 0% |
| `no-inline-header-lists` | 2 candidates | 0–0 | 0–0 | 0% / 0% |
| `no-orphaned-demonstratives` | 3 candidates | 0–3 | 0–1 | 2% / 0% |
| `no-rhetorical-questions` | 1 candidate | 0–10 | 0–0 | 11% / 0% |
| `no-rubric-echoing` | 3 candidates | 0–0 | 0–0 | 0% / 0% |
| `no-soft-scaffolding` | 2 candidates | 0–1 | 0–10 | 0% / 2% |
| `no-staccato-sequences` | run of 3 | 0–121 | 0–204 | 59% / 69% |
| `no-symmetric-list-items` | 3 items | 0–0 | 0–0 | 0% / 0% |
| `no-tidy-paragraph-endings` | 3 candidates | 0–3 | 0–2 | 2% / 0% |
| `no-unicode-flair` | 2 candidates | 0–4 | 0–11 | 2% / 4% |
| `overall-signal-stacking` | score 4 | 0–11 | 0–9 | 71% / 92% |
| `paragraph-length-uniformity` | CV 0.18 | 0.124–3.01 | 0.077–0.846 | 5% / 31% |
| `sentence-length-variance` | stdev 9.0 | 6.47–22.0 | 4.45–17.2 | 13% / 71% |

**No G9 case exists outside G9.** Every cut-off either sits inside the range its corpus
produces, or its target does not occur at all. G9 itself now sits mid-range on both
corpora, which is what DR-79A's recalibration to 9 achieved.

Figures above are as measured on 2026-07-28, before the changes recorded below.

## Cause 2: four checks are silent because the corpus was

`no-compound-modifier-density`, `no-inline-header-lists`, `no-rubric-echoing` and
`no-symmetric-list-items` returned zero on all 112 documents. The threshold is not
implicated; there was nothing to measure it against. Lowering any of them would have
changed nothing except what a future document trips over.

Two probe documents were added under `samples/synthetic/` in `fb1b158`, one at each
cut-off and one a step below, so the declaration test can watch the flag turn on
between them. They are deliberately outside the human/generated split: hand-written
prose is evidence that a detector fires, never evidence about how often real prose
produces a pattern, and putting it in the calibration corpora would corrupt every rate
this project measures.

The corpus remains thin for these four. Widening it with real documents is a corpus
decision, not a threshold one, and is not claimed here.

## Cause 3: two checks read backwards until length is accounted for

Six checks showed a higher share of human documents flagged. For four, the occurrence
rate agrees with the share, so the reading is real and small. For two it did not:

| check | share of docs h/g | per 1000 words h/g |
|---|---|---|
| `no-boldface-overuse` | 8% / 2% | 0.25 / 0.30 |
| `no-tidy-paragraph-endings` | 2% / 0% | 0.06 / 0.20 |

Both were counting raw occurrences, so a longer document reached the cut-off more
readily whatever wrote it — the DR-66 error reproduced. Both now require the count and
a rate, in `954d056`: the count stays as a noise gate so short fixtures still flag, and
the rate removes the length bias. Tidy endings corrects to 9% generated against 6%
human.

`no-orphaned-demonstratives` is the same shape at a smaller scale — 11% of human
documents hold one against 4% of generated, but only a 7,078-word document accumulates
three. It is left unchanged and named here rather than swept in.

## What this audit does not answer

Whether a cut-off is wired is DR-170's question and is settled. Whether it sits inside
the observed range is this one, and is settled: none is outside.

Whether it sits at the **best** point in that range is neither. A threshold can be
inside the range and still badly placed. Of the 19 checks carrying a threshold, three
have a calibration record arguing a specific value — `sentence-length-variance`,
`no-forced-triads`, `no-unicode-flair`. The other 16 are inherited numbers nobody has
defended. That is a smaller and better-defined question than the one DR-164 opened, and
it is left open rather than quietly closed. (The eleven calibration records under
`dev/evals/` mostly belong to checks that carry no threshold, which is where the "11
checks carry a calibration record" note in `dev/todo.md` came from; it counts the wrong
set.)

`paragraph-length-uniformity` declares two gates, so no single one of them is its
boundary and it stays consumption-only in DR-170's test. `sentence-length-variance`
declares one and is now asserted exactly across 144 documents, with no tolerance
invented for the decimal: the metric is continuous and documents fall either side of
9.0, so a witness pair became a straddle.

Three checks fire on human prose and never on generated —
`no-rhetorical-questions` at 11%/0%, `no-heading-one-liners` at 8%/0%,
`no-orphaned-demonstratives` at 2%/0%. Whether a pattern belongs in the catalogue is a
question for the source evidence, not for a threshold sweep, and 49
generated documents cannot settle it. Recorded, not acted on.

## Method

`grade.CHECK_THRESHOLDS` read directly, each check run over both corpora unmodified.
Two errors were found and corrected in the sweep itself before these numbers were
trusted, both of the same family — absence read as data. Flag counts were first
compared across corpora of unequal size, which reported `no-staccato-sequences` as
firing more on human prose when 37 of 63 is a smaller share than 34 of 49. And
documents a check *skips* carry no metric, so falling back to `candidate_count`
recorded them as a genuine zero; five of 63 human and four of 49 generated documents
are skipped by `paragraph-length-uniformity`, and one generated document by
`sentence-length-variance`. Those are excluded above rather than counted as zeroes.
