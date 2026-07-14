# Dik, Erdem, and Dik: GPTZero accuracy by essay length

## Metadata

- **URL:** https://arxiv.org/abs/2506.23517
- **Authors:** Selin Dik, Osman Erdem, and Mehmet Dik
- **Published:** 2025-06-30
- **Extracted:** 2026-07-14
- **Source type:** Detector evaluation
- **Evidence tier:** Academic preprint / small empirical comparison
- **Extraction status:** reviewed from complete saved PDF text
- **Full text snapshot:** `snapshots/dik-gptzero-accuracy.md`

## Study design

- Tests 78 essays: 28 generated with ChatGPT 3.5 or 4o and 50 human-written essays.
- Divides essays into short (`40–100` words), medium (`100–350`), and long (`350–800`) groups.
- Submits each essay to GPTZero and records its AI probability and classification.

## Direct findings

- GPTZero classified all 28 AI essays as AI in the reported confusion matrix.
- It classified 42 of 50 human essays as human and misclassified 8 as AI.
- The human false-positive rate was therefore `16%`; the overall error rate was `10.3%`.
- Short and long human-written texts produced more inaccurate or false-positive results than medium-length texts.
- Medium-length human text was the most accurate group in this sample, but the authors explicitly state that its results still fluctuated and could not be predicted reliably every time.

## Authors' recommended follow-up

- Use more human and AI texts.
- Include mixed human/AI texts rather than only pure examples.
- Continue investigating what causes human false positives.
- Explore factors beyond word count.

## Project incorporation

- **No prose-pattern evidence:** the paper evaluates GPTZero's classifications. It does not identify words, syntax, formatting, or other AI writing misuse for a human-eyes check.
- **No GPTZero use case for human-eyes:** human-eyes does not need to integrate, benchmark, or evaluate GPTZero on the basis of this source.
- **Mixed-assistance test-corpus candidate:** the authors recommend future work on text containing both human and AI writing. For human-eyes, that suggests testing whether its existing checks still find a local AI-misused pattern when it appears inside otherwise human prose.
- **Length as a possible stress-test dimension only:** GPTZero's results varied across short, medium, and long essays. That result cannot be transferred to human-eyes, but human-eyes could separately test its own density- and context-dependent checks across lengths.
- **The human false-positive result is a finding about GPTZero, not a human-eyes objective or constraint.** Human-eyes may flag a pattern in human writing; this source does not change that project stance.

## Recommendations for human-eyes

1. Do not create or change a prose check from this paper.
2. Consider adding mixed human/AI and AI-edited-human samples to the human-eyes evaluation corpus.
3. Optionally inspect human-eyes' own results across short, medium, and long samples; treat this as a new project experiment, not as a conclusion supplied by Dik.
4. Keep the GPTZero accuracy and false-positive results in the source record as findings about that product, without turning them into a human-eyes restriction.

These recommendations do not require a prose rule. No checker, threshold, process file, or evaluation fixture was changed as part of this source-card work.

## Matched patterns / rules

- No direct pattern/rule match
- Mixed-assistance evaluation-corpus design
- Optional length-stratified stress testing

## Associated hypotheses

- H1 calibrated register-distance scoring
- H12 genre-aware threshold calibration
- H14 calibration golden set
