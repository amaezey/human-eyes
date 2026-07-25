# Xia feature rate calibration (2026-07-26)

Record for DR-66: two new rate checks, #68 `no-passive-voice-rate` and #69
`no-it-pronoun-rate`, a rate branch added to #25 `no-staccato-sequences`, and
the decision not to build a past-tense check.

## The source

Xia, Stańczak, and Roth, *Explaining Generalization of AI-Generated Text
Detectors Through Linguistic Analysis*, EACL 2026. The authors trained
XLM-RoBERTa and DeBERTa classifiers over 516,000 texts spanning four domains,
seven generator configurations, and six prompt strategies, then correlated each
classifier's transfer accuracy against shifts in 80 surface linguistic features.

Four features carry its strongest correlations: past tense, passive voice, the
"It" pronoun, and the count of short sentences.

## The paper supplies no direction

This is the important thing about the source, and the reason every threshold
here comes from project measurement rather than from the paper.

Its reported values are Pearson correlations between *detector accuracy* and
*shifts in the human-AI feature gap* between training and test configurations,
per its equation 5. They are not measurements of which group writes more of a
feature. A 0.416 correlation for past tense says a detector's transfer accuracy
moves with changes in the past-tense gap; it does not say generated prose
carries more past tense.

The paper's only directional statements about these features are inherited from
cited work. Its passive-voice sentence, "Human-written texts have been shown to
contain more passive voice than AI-generated texts (Georgiou, 2024)", is
background, not a finding of this paper, and the project corpora contradict it.
C09 on the source card flags exactly this class of statement, and it held up.

## Definitions

Taken from the paper's appendix A.4:

- **Past tenses** - "the fraction of the text covered by verbs in past, present
  and future tenses ... the incidence of past tenses is the number of verbs in
  past simple, past continuous, past perfect or past perfect continuous".
- **Passive voice** - "the incidence of passive and active voice as the
  frequency of verbs in passive or active voice".
- **"It" pronoun** - StyloMetrix per-pronoun frequency, reported as a fraction
  of tokens. Possessive `its` is a determiner and is excluded.
- **Short sentences** - "the number of very long (35 words or more) and very
  short (10 words or less) sentences in each text", following Desaire et al.

## Instrument

No POS tagger is available, and none was needed for three of the four features.
The detectors were unit-tested against 39 hand-labelled cases before any corpus
number was read, covering the constructions that must match and the ones that
must not: progressives, copula-plus-adjective, present passives, present
perfects, attributive `-ed` forms, and possessive `its`.

Past simple is the exception. A bare `-ed` form is ambiguous between a verb and
a deverbal adjective, and no surface rule resolves it. Two counters were built:

- **strict** - only unambiguous heads: `was`/`were`/`had` constructions and
  irregular past forms, which are never adjectives in these shapes.
- **broad** - strict plus regular `-ed` forms outside attributive position.

The two agreeing is what makes the past-tense null trustworthy.

## Corpus

`dev/evals/samples/human-sourced` against `dev/evals/samples/generated-ai`,
documents of 300 words or more: 62 human, 46 generated, the same set the Biber
calibration used. The human corpus holds 135k words against the generated
corpus's 48k, so every figure is a rate per 1000 words.

## Measured

| feature | human /1k | AI /1k | ratio | human median | AI median | median ratio |
|---|---|---|---|---|---|---|
| past tense, broad | 39.29 | 38.06 | **0.97x** | 28.21 | 20.66 | **0.73x** |
| past tense, strict | 24.71 | 19.62 | **0.79x** | 14.53 | 8.09 | **0.56x** |
| passive voice | 4.66 | 6.47 | 1.39x | 3.66 | 5.57 | 1.52x |
| `it` pronoun | 13.83 | 19.31 | 1.40x | 10.96 | 17.84 | 1.63x |
| short sentences | 19.05 | 34.96 | 1.84x | 18.74 | 29.32 | 1.56x |

Short sentences are also 34.9% of human sentences against 44.6% of generated
ones, and mean sentence length runs 18.2 against 12.8. Both figures survive
dropping list lines, so the gap is not a lists artefact.

## Thresholds

| check | threshold | AI flagged | human flagged |
|---|---|---|---|
| #68 passive voice | 5.0 per 1000 | 57% | 29% |
| #69 `it` pronoun | 18.0 per 1000 | 50% | 18% |
| #25 short-sentence branch | 30.0 per 1000 | 48% | 21% |

Minimum length is 300 words for all three, matching #10 and #65 to #67. For
reference the catalogue already carries #10 at 66%/24%, #65 at 70%/24%, #66 at
52%/27%, and #67 at 70%/37%. #69's 18% is the narrowest human flag rate of the
rate family.

## Passive voice: why the null control did not refute it

Measured over irregular participles only, an unambiguous subset, passive voice
runs 1.40 human against 1.47 generated, a flat 1.05x. That could have meant the
1.39x was an artefact of `be` plus an `-ed` adjective.

Sampling the actual matches settled it. The generated corpus's extra passives
are ordinary regular-verb passives: `be operationalised`, `is prioritised`,
`are disrupted`, `be exacerbated`, `is situated`. The human corpus's regular
passives look the same: `was launched`, `is transferred`, `are governed`. The
irregular subset is flat because irregular verbs are the older Germanic core;
the register difference sits in the Latinate verbs, which are regular. The
control split the feature rather than refuting it.

A ratio alone cannot distinguish an artefact from a finding. Read the matches.

## Short sentences: folded into #25 rather than numbered

The rate separates cleanly at 48% against 21%, but #25 `no-staccato-sequences`
already flagged 15 of the 22 generated documents the rate branch would catch,
through its consecutive-run and repeated-opener branches. Mae chose to widen
#25 rather than create a pattern number for territory an existing check already
half-covered. The branch adds 7 generated findings and 2 human ones.

### A comparison that does not work for one-occurrence checks

#25's two older branches appeared to run backwards: before this change the check
flagged 39% of generated documents against 50% of human ones. That reading was
wrong, and the reason is worth keeping.

A share-of-documents comparison is length-biased whenever the check fires on one
occurrence anywhere in the text. The human corpus averages 2,172 words per
document against the generated corpus's 1,051, so it gets roughly twice the
chances to contain a single qualifying occurrence. Measured as a rate per 1000
words, both branches run the right way:

| #25 branch | human /1k | AI /1k | ratio |
|---|---|---|---|
| runs of 3+ short sentences | 0.49 | 0.89 | 1.82x |
| repeated-opener pairs | 0.48 | 1.20 | 2.50x |

Truncating every document to its first 1000 words holds the direction: 1.38x and
1.83x. #25 separates the corpora. Nothing about it needs changing.

Any future flag-share figure quoted for a one-occurrence check across these two
corpora carries the same bias. Rate checks are not affected, because the
threshold is already normalised by length.

## Past tense: no check

Both counters put human prose at or above generated prose: 0.97x and 0.79x by
aggregate rate, 0.73x and 0.56x by document median. Nothing was built. This is
the second clean null of this kind, after phrasal coordination in DR-159.

The likely reason is genre rather than register. Past tense tracks narrative and
reportage, and the human corpus carries more of both.

## "It" pronoun: a rate with no construction under it

The lift is spread across uses rather than concentrated. Placeholder-subject
`it` (`it is worth noting`, `it turns out`) runs 6.37 human against 8.27
generated, 1.30x. Ordinary back-reference runs 7.46 against 11.04, 1.48x. So a
narrower check on the expletive frame alone would have been the weaker of the
two halves. The check measures the whole habit, and its guidance is to name the
thing rather than to rewrite one phrase family.
