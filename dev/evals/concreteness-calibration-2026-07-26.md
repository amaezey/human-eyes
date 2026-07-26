# Concreteness calibration (2026-07-26)

Record for DR-84: new check #73 `concreteness-average`, and the data file it needs.

## The measure

Every word in the draft is looked up in Brysbaert, Warriner and Kuperman's concreteness norms: 39,954 English words rated from 1 (fully abstract, `justice`) to 5 (fully concrete, `hammer`) by human raters. The check takes the mean across content words and fails at 2.915 or below, in prose of 100 words or more, at context-warning severity.

The norms ship in the repo as `human-eyes/references/brysbaert-concreteness.csv`, 614 KB, the same shape as the Kobak excess-vocabulary file already there.

## The source supplies no direction

El Attar et al. name psycholinguistic features as one of four feature areas and report that removing them sometimes improves their classifier. They give no direction, no threshold, and no word list. Both come from measurement here.

## Function words had to come out

The norms rate function words as maximally abstract: `the` 1.43, `a` 1.46, `because` 1.22, `if` 1.19, `would` 1.12. In any real document they are the most common words, so a mean over all rated words tracks function-word density rather than whether the writer names things.

| measured over | human | generated | separation |
|---|---|---|---|
| all rated words | 2.525 | 2.428 | 32 points at 2.457 |
| **content words only** | **2.972** | **2.820** | **38 points at 2.915** |

Excluding them both widens the separation and makes the number mean what it claims to mean. This was found by reading which words were dragging a human fixture below the threshold, not by fitting to that fixture: it flags either way.

## Result

At 2.915 the check flags 67% of generated documents and 29% of human ones. That places it between #71 word length (54 points) and #70 Latinate verbs (38 points) in the catalogue.

## Two controls

**Genre.** Excluding every nineteenth-century document, which is where the most concrete human prose sits, leaves the separation unchanged.

**Paired documents.** Four documents exist as a human original and its AI rewrite. Measured over all rated words, three of four move toward the abstract but two move by 0.004 and 0.029, and one moves the wrong way. This is the weakest control of any check shipped today and it is recorded as such: four pairs cannot carry a result, and the corpus-level separation is what the check rests on.

## Overlap, and why it was built anyway

Of the 28 generated documents the all-words version flagged, #71 word length already flagged 23, and #71 plus #65 together left one document that nothing else caught.

Overlap was raised as an objection and rejected, correctly. There is no project rule against two checks firing on the same document, and abstractness and word length are not the same finding even though they correlate. A character count tells a writer their words are long. This tells them their words name categories instead of things, which is the direction a rewrite needs.

The same faulty reasoning had been applied twice earlier in the same session, against #70 and against this check.

## Performance

Measured over the 108 corpus documents:

| | cost |
|---|---|
| whole check registry | 407 ms per document |
| this check | 0.32 ms per document, 0.1% of a run |
| loading the norms at import | 32 ms, once |
| the file on disk | 614 KB |

## What is not covered

DR-84's two other feature areas close with this row. Morphology was measured earlier the same day and its best measure shipped as #71 word length; the rest (syllables per word, derivational suffix density, `-ed`/`-ing` density) measure the same signal more weakly. Information-theoretic features need a language model to compute how predictable each word is, which the product does not run. That is the same blocker that closed DR-99.
