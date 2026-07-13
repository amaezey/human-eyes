# Evaluation rebuild forensic closeout

Date: 2026-07-14

Branch: `codex/fresh-evidence-benchmark`

Commit under recovery: `6e94e457ccc72b07ba56b4100625406e748f6d8a`

Nothing has been pushed. This document distinguishes recovered evidence from the failed experiment that was removed.

## What went wrong

The requested goal was simple: add new samples so development did not optimise around the same small corpus, then see whether the refactored checker treated the established and new samples better or worse. The failed rebuild replaced that goal with an invented “freshness” and contamination standard.

That change of objective caused four concrete failures:

1. AI prompts were coached around properties the checker measures, including paragraph variation, voice, candidness and imperfection. Responses were then rerolled or selected. This made the AI cohort unsuitable for measuring ordinary AI writing.
2. Work expanded into contamination searches, annotation machinery and repeated corpus reconstruction that the user had not requested and that did not improve the tool.
3. The work stopped at deterministic comparisons and incomplete agent-assessment artefacts instead of running the product's full current 15-record Audit lifecycle and reviewing the judgments.
4. Results were interpreted as if one flag were an authorship accusation. That led valid constructions, especially human-written and quoted triads, to be excluded instead of detected and contextualised.

The “freshness rule” was not an existing project requirement. It was introduced by the failed Codex session. The testing documentation now describes the actual objective: vary authors, genres, registers and prompts; do not coach AI writing; preserve provenance for reproducibility; and interpret per-check results rather than treating aggregate flag counts as authorship classification.

## What was removed and what was preserved

Removed:

- The coached, rerolled and human-rewrite AI experiment.
- Its prompts, generation records, contamination packets, match reviews, annotations, incomplete native-audit attempts and derived reports.
- The invalid aggregate `three-version-comparison.json`.

Preserved:

- The established five-pair corpus and its existing working tests.
- The ten collected human sources and source packets.
- Ten literal-first, uncoached AI responses created from ordinary subject, genre and approximate-length prompts.
- The historical refs: pre-refactor `56f262a18ba1271268ae98d7a49cba1e7a33a168` and May `f28a3706816d0ca5107196955a5d14418732a5af`.

## Checker changes recovered from the refactor

Markdown headings have been removed as a deterministic indicator and from signal stacking. Heading style remains available for manual review, but a heading no longer adds an AI-style finding.

Triad detection now reports the construction wherever it occurs, including human prose and quoted material. Quote context is carried separately as `quoted: true`; quotation affects interpretation, not recognition. Individual triads and document-level triad density remain separate findings.

The missed triads were caused by the refactored extractor, not quote masking. It restricted item length, prohibited internal function words, required narrow trailing boundaries and then filtered individual triads to abstract-noun suffixes. Explicit regression tests now cover every disputed example, including:

- `belonging, intimacy, and connection`
- `improvisation, sparring and discussion`
- `designed, practised, and maintained`
- `visible, versioned, and easy`
- `Not perfectly, but more often, and with less hesitation`
- `know when to engage, how to respond, and when a decision closes`
- `cultural, social, and technical`
- `have to risk receiving, admitting limits, or letting someone else do it`
- `Pleasure softens my edges, which makes service kinder and less controlling`

The agreed narrative sequence, `answers quickly, smooths things over, and then wonders why life`, remains excluded. Full-corpus review also removed newly exposed false candidates such as `in hospital, Didion and Dunne return`, `In ancient times, however...`, `say, wind or fire`, and clause fragments from Darwin and Woolf.

## Cross-version deterministic results

These are deterministic surface findings. A finding means the construction was detected; it is not an accusation and higher totals are not automatically better.

| Corpus and version | Human findings | AI findings | Mean AI minus human | AI-higher pairs | Ties | Human-higher pairs |
|---|---:|---:|---:|---:|---:|---:|
| Established, current | 37 | 46 | +1.8 | 3 | 1 | 1 |
| Established, pre-refactor | 46 | 42 | -0.8 | 2 | 1 | 2 |
| Established, May | 44 | 42 | -0.4 | 2 | 1 | 2 |
| Pilot additions, current | 34 | 36 | +0.2 | 4 | 2 | 4 |
| Pilot additions, pre-refactor | 35 | 26 | -0.9 | 4 | 0 | 6 |
| Pilot additions, May | 34 | 26 | -0.8 | 4 | 0 | 6 |

On the established corpus, the current checker materially changes the direction of the comparison: the mean pair gap moves from -0.8 pre-refactor to +1.8, with AI higher in three of five pairs, one tie and one human-higher pair. The gains come from the current check catalogue and corrected triad recognition, while heading removal reduces packaging-driven flags.

On the pilot additions, the gap moves from -0.9 pre-refactor to +0.2 current. Human source formatting, curly quotes, em dashes, real rhetorical repetition and list structure still produce four human-higher pairs, so the result is not a general authorship classifier. It shows both improvement and remaining sensitivity to published-human conventions.

The recovered checker initially produced human 34 / AI 28 on this corpus. The approved improvement pass added eight AI findings while leaving the human total unchanged:

- AI-03: corrected clause-form and repeated-preposition triad recognition (+1).
- AI-04: list-block/item thresholding catches ten items across two blocks (+1).
- AI-07: product-performance promotional claims (+1).
- AI-02: nonliteral map/terrain framing (+1).
- AI-02: explicit lesson framing (+1), which also moves the existing aggregate signal-stacking check across its threshold (+1). These two findings are related, not independent evidence.
- AI-06: repeated report scaffolding (+1).
- AI-10: significance/value emphasis framing (+1).

The tidy-ending expansion changes candidate visibility rather than totals: the fresh AI cohort has four candidates across three documents and the human cohort has none; no document reaches the retained three-ending threshold. The established corpus gains no new final finding from the later boundary families. Its one-human/one-AI increase relative to the earlier closeout comes from corrected triad recognition, not the fresh-corpus-specific rule work.

Full data is in `dev/evals/three-version-established-comparison.json` and `dev/evals/three-version-pilot-additions-comparison.json`.

## Agent-assessed evidence status

The retained pilot-addition run contains 300/300 schema-valid answers for its 20 documents. Rebinding those answers to current work bundles proves that the current grader accepts their schemas, evidence substrings and registry coverage. It does not rerun an agent or establish that the judgments are correct.

That retained run flags 11/150 human answers and 14/150 AI answers. Document review found substantial judgment problems: `tonal_uniformity` accounts for 12 of the 25 total flags and is usually supported by one sentence, while the agent returned zero `faux_specificity` and zero `formulaic_parallelism` findings despite plausible AI passages. The genre taxonomy also forces poor substitutions, and empty list answers require no rationale. These counts are therefore diagnostic output, not a validated performance result.

No equivalent established-corpus agent execution through the human-eyes skill was run. A later Codex session manually authored answers for those documents and passed them through `grade.py`; that tested bundle construction, schema validation and rendering, not agent judgment. Those artefacts and every conclusion derived from them have been removed.

There is consequently no valid agent-assessed comparison between the established corpus and the pilot additions. The pilot-only document review remains in `dev/evals/pilot-additions-agent-assessed-review.md`. A proper comparison requires fresh, preserved agent executions using the skill on both corpora under the same instructions, followed by evaluation against a separately reviewed reference set.

## Validation actually run

All 20 `dev/evals/tests/test_*.py` files pass when run directly. This includes grader behavior, registries, work-bundle binding, audit contracts, rendering, requested patterns, phrase capture, regex robustness, release gates, comparison harnesses and action-runner contracts.

The regex seed reports 0.750 directional recall, 0.857 specificity and 0.143 false-positive rate. Its cells are sparse, so these are diagnostic figures rather than stable performance estimates.

All 11 report-render baselines were inspected before capture. No check status changed in the final evidence-shape refresh. The accepted differences expose existing `scene lands` and `the uncomfortable truth` candidates instead of mislabelling them as aggregate findings, and add consistent empty `matches` fields. Baseline verification passes after capture.

The model-backed lifecycle harness itself was broken: it hard-coded every qualitative assertion to failed instead of running Skill Creator's grader. That missing grading stage is restored. Iteration 10 ran eight skill-guided LLM executions and eight independent graders without executor or grader errors. The result was 13/17 assertions passed (77.1% mean case pass rate), with failures in Suggestions validation, Write fidelity and Rewrite preservation. The skill protocol was then hardened at those failure points. Focused reruns passed Write 2/2 on Codex, convergence/preservation 3/3 on Claude, and Suggestions 2/2 on Claude. The final Suggestions grader verified 46 complete surrounding-paragraph contexts with fresh bundles, 15-record agent-assessed readings and Audits. The full lifecycle history and evidence is in `dev/evals/action-lifecycle-iteration-10-report.md`.

## Pragmatic testing approach from here

1. Keep the established corpus as the stable regression baseline.
2. Keep the pilot additions as a second, varied diagnostic set. Add or replace samples periodically to broaden coverage, not to satisfy a contamination doctrine.
3. Generate ordinary literal-first AI responses. Do not coach, rewrite, reroll or select against checker results.
4. Report per-check candidate recognition, threshold decisions and pair reversals before aggregate totals.
5. Run both deterministic and full agent-assessed paths. Review the agent's actual evidence and treatment of every flagged or suspiciously clear judgment.
6. Improve agent-assessed measurement next: require multi-passage evidence for document-level states, add the missing genres, and require short rationales for clear answers. Do not put agent judgment inside deterministic behavior.
7. Rerun the complete lifecycle suite on Codex after its external usage window resets; the three original failure areas now pass focused independently graded reruns, including cross-model validation.

## Bottom line

The failed coached corpus and its derived claims are gone; the established tests remain; the varied pilot additions remain; the checker treats headings and triads according to the agreed behavior; and both deterministic sets have reproducible current/pre-refactor/May results. The retained pilot agent output has a document-level error review, but the established agent run and the cross-corpus agent comparison remain unperformed.

The valid evidence says the refactor moved the deterministic needle strongly on the established corpus, while the false-negative pass moved the pilot additions from -0.9 pre-refactor and -0.6 at recovered-current to +0.2 after approved fixes. No claim about comparative agent performance is supported by the current artefacts.
