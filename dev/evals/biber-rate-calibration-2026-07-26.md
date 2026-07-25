# Biber feature rate calibration (2026-07-26)

Record for DR-159: three new rate checks, #65 `no-nominalisation-rate`, #66 `no-that-relative-rate`, and #67 `no-participial-clause-rate`, and the decision not to build a fourth.

## The source

Reinhart et al., *Do LLMs write like humans?*, PNAS, February 2025. Six models each continued a human-written 500-word chunk; each continuation was compared against the actual next 500 words by the same author. Sixty-six features from Douglas Biber's tagset, tagged with `pseudobibeR` over dependency-parsed text.

Four features are named in the paper's body as the cluster instruction-tuned models overuse, with GPT-4o rates against paired human text:

| feature | paper's rate | paired Cohen's d |
|---|---|---|
| present participial clauses | 5.3x | 1.38 |
| `that` clauses as subject | 2.6x | 0.77 |
| nominalisations | 2.1x | 1.23 |
| phrasal coordination | 1.9x | 0.81 |

## Definitions

Taken verbatim from the paper's appendix feature table, not paraphrased. Two of the four were initially implemented against the wrong construction and had to be rebuilt:

- **Nominalisations** — "nouns formed from adjectives or verbs, such as development or robustness".
- **`That` clauses as subject** — "'That' relative clauses in subject position", example "the dog that bit me". This is a relative clause, not a sentence beginning with "That". `That` clauses in object position ("the dog that I saw") and `that` verb and adjective complements ("I said that he went", "I'm glad that you like it") are separate features in the same tagset and are excluded.
- **Present participial clauses** — "Adverbial clauses used as present participles", example "Stuffing his mouth with cookies, Joe ran out the door". Gerunds ("Participial forms functioning as nouns") and present participial postnominal reduced relatives ("The event causing this decline") are separate features. Progressives are not participial clauses.
- **Phrasal coordination** — "Pairs of nouns, verbs, adjectives, or adverbs connected by a coordinating conjunction", example "The nouns and verbs are coordinated". Distinct from clausal coordination.

## No parser was required

The paper tagged with a dependency parser. Three of the four features are recoverable from surface form without one, and the detectors were unit-tested against the paper's own examples before any corpus number was trusted. The subject-relative detector was built against fifteen hand-labelled cases and gets all fifteen right, including "the dog that bit me" and the four constructions that must not match.

## Corpus

`dev/evals/samples/human-sourced` against `dev/evals/samples/generated-ai`, documents of 300 words or more: 62 human, 46 generated. The human corpus holds 137k words against the generated corpus's 49k, so every figure is a rate per 1000 words. Raw counts would favour the longer corpus and point the wrong way.

## Measured

| feature | human /1k | AI /1k | ratio | paper |
|---|---|---|---|---|
| nominalisations | 21.79 | 36.82 | 1.81x | 2.1x |
| present participial clauses | 3.85 | 5.49 | 1.48x | 5.3x |
| `that` relatives, subject position | 2.59 | 3.75 | 1.45x | 2.6x |
| phrasal coordination | 13.36 | 10.29 | **0.85x** | 1.9x |

Control: `that` relatives in **object** position run 0.56x, the opposite direction. The subject/object split behaves as the tagset predicts, which is what makes the 1.45x credible rather than an artefact of the regex.

## Thresholds

| check | threshold | AI flagged | human flagged |
|---|---|---|---|
| #65 nominalisations | 29.0 per 1000 | 70% | 24% |
| #66 subject relatives | 3.5 per 1000 | 52% | 27% |
| #67 participial clauses | 4.4 per 1000 | 70% | 37% |

Minimum length is 300 words for all three, matching #10. Raising it to 500 or 600 improves separation, but 500 also happens to exclude the two human fixtures in `test_grade.py` that these checks flag, so it was rejected as fitting the instrument to the fixtures.

For reference #10 `no-forced-triads` sits at 66% AI and 24% human. #65 matches that precedent. #67's 37% is the widest human flag rate in the catalogue.

## Consequence for the human fixtures

Two human reference documents in the test suite now trip these checks: the 476-word opinion piece runs 39.9 nominalisations and 4.2 subject relatives per 1000 words, and the instructional piece runs 6.7 subject relatives. Both are true positives under the definitions, and both sit inside the flagged share the calibration predicts. They are added to the documented exclusion set rather than having the thresholds moved.

## Phrasal coordination: no check

Measured properly the feature runs **0.85x**, more common in human writing than generated. The project corpora do not reproduce the paper's 1.9x. No check was built.

An earlier measurement of three-item lists (`X, Y, and Z`) returned 1.81x and was briefly mistaken for this feature. A three-item list is a tricolon, which #10 already measures, so that figure was rediscovering an existing check rather than finding a new one.

## Two mistakes worth not repeating

Both features whose definitions were assumed rather than read produced measurements that looked like the paper's figures by coincidence: 2.61x against a reported 2.6x, and 1.81x against a reported 1.9x. Both were measuring different constructions. Read the appendix definition before writing the regex.

A five-pair subset of the corpus (human essays and their AI rewrites) was used at one point to overturn the full-corpus result. It has no power: the subject-relative feature does not occur even once across those five documents, so the subset returns zero and can only ever fail a feature. Sample size before conclusion.
