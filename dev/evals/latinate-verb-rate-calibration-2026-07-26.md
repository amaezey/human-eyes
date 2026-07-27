# Latinate verb rate calibration (2026-07-26)

Record for DR-21: new check B12 `no-latinate-verb-rate`, and why the source's own word list could not be used directly.

## The source

Wikipedia's *Signs of AI writing*, claim C13: "Plain verbs may be replaced by stiff or euphemistic synonyms such as `authored`, `relocated`, `utilized`, `attempted`, and `passed away`." The page is an uncited editor inventory. It supplies five words, no counts, no sample, no model set, and no comparison data.

All five were already ruled before this row reached its final component. DR-21B rejected `authored`, `relocated`, `attempted`, and `passed away` as B1 clustering candidates: the project corpora contain none of the four in the generated samples, while `passed away` occurs once in the human ones. `utilized` was already matched through B1's existing `utilize` stem.

So nothing the source supplies was left to add. The list below is the project's, built from the habit the source names rather than from its examples.

## The list

Forty-four verbs, grouped in `grade.py` by inflection so the pattern matches verb forms only:

- **Drop-e (26):** initiate, terminate, demonstrate, indicate, illustrate, acquire, procure, purchase, require, necessitate, generate, reside, inquire, provide, contemplate, determine, execute, disseminate, observe, cease, discontinue, utilize, utilise, facilitate, commence, relocate
- **Plain consonant (11):** assist, obtain, construct, inhabit, inform, maintain, retain, ascertain, encounter, alter, depart
- **Sibilant (2):** furnish, diminish
- **`-y` (4):** notify, identify, modify, rectify
- **Doubling (1):** transmit

Nouns and adjectives built on the same stems are not matched: `information`, `assistant`, `department`, `residents`, `alternative`, `requirement`, `construction`, `executive`, `transmission`. A unit test pins this.

Eleven further candidates are excluded: `aid`, `request`, `permit`, `increase`, `decrease`, `conduct`, `produce`, `author`, `consider`, `dwell`, `attempt`. They were first set aside on the judgement that each is an ordinary noun as often as a verb, which is not a reason on its own. Measured afterwards:

| list | human median | generated median | ratio | best separation |
|---|---|---|---|---|
| the 44 that shipped | 1.07 | 2.51 | 2.35x | 38 points at 2.0 or 2.5 |
| the 11 alone | 0.78 | 0.75 | 0.96x | 12 points |
| all 55 together | 2.07 | 4.26 | 2.06x | 38 points at 4.0 |

The eleven run marginally more often in human prose than generated, and adding them buys no separation, only a higher threshold and more matches to read. The exclusion holds on the measurement rather than on the judgement that prompted it.

## Corpus

`dev/evals/samples/human-sourced` against `dev/evals/samples/generated-ai`, documents of 300 words or more after front matter is stripped: 62 human (134,707 words), 46 generated (48,375 words). The human corpus holds 2.8 times the words, so every figure is a rate per 1000 words. Raw counts would favour the longer corpus and point the wrong way.

## Result

| measure | human | generated | ratio |
|---|---|---|---|
| aggregate rate per 1000 words | 1.57 | 3.25 | 2.07x |
| document median | 1.07 | 2.51 | 2.35x |

Threshold sweep, share of documents flagged:

| threshold | human | generated | separation |
|---|---|---|---|
| 2.0 | 23% | 61% | 38 |
| **2.5** | **15%** | **52%** | **38** |
| 3.0 | 13% | 41% | 28 |
| 3.5 | 11% | 37% | 26 |

2.0 and 2.5 separate equally. 2.5 was chosen as the quieter of the two: it flags eight fewer human documents for nine fewer generated ones.

Against the rate checks already shipped, measured the same way on the same corpora:

| check | human | generated | separation |
|---|---|---|---|
| G9 sentence variance | 11% | 72% | 60 |
| B4 triads | 23% | 70% | 47 |
| B7 nominalisation | 27% | 70% | 42 |
| **B12 Latinate verbs** | **15%** | **52%** | **38** |
| B9 participial | 37% | 70% | 32 |
| B11 `it` pronoun | 18% | 50% | 32 |
| B8 subject `that` relative | 27% | 54% | 27 |
| B10 passive voice | 29% | 57% | 27 |

Mid-table on separation, second lowest on the human flag rate.

## Three routes were measured, not one

**As B1 clustering candidates.** The individual words are worthless to B1. Adding the twelve that separate best moves B1 from 10% of human documents and 7% of generated ones to 16% and 17%, which is no discrimination at all. B1 fires from occurrence counts in a paragraph, and single occurrences of common verbs like `require` and `provide` are everywhere in both corpora.

**Folded into B7 as one count.** Nominalisations plus Latinate verbs under one threshold reaches 53 points of separation at 33.0, better than either alone. It was rejected on structure rather than on the number: B7 matches six word *endings* and grows on its own as English does, while this list is curated and grows only when someone adds a word. Putting them under one threshold means a hand-edit to the list silently moves the behaviour of a morphological rule.

**As its own check.** What shipped.

## Two mistakes worth recording

**The overlap test used earlier was invalid.** The first pass rejected this check because it flagged few documents that B7 did not already flag. Running the entire live registry over both corpora shows all 108 documents already fail something, so "documents nothing else catches" is zero for every check in the catalogue. It cannot discriminate between a good check and a bad one and must not be used again.

**The first regex undercounted.** A rough matcher built as `stem + (e?s|e?d|ing|ies|ied|ying)?` misses the `-ing` forms of drop-e verbs, so `providing`, `generating`, `facilitating`, `identified`, and `transmitted` never matched. It reported 10% human and 50% generated; the correct matcher reports 15% and 52%. Numbers taken from a throwaway regex were quoted to Mae before the real one existed. Build the matcher the check will actually use, then measure.
