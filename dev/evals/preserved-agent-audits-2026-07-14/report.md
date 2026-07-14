# Preserved agent-assessed Audit and independent review

Date: 2026-07-14

All 35 documents received a fresh 15-record Audit under one fixed instruction wrapper. All 525 judgments were then reviewed in separate Codex contexts.

## Agent-assessed flags

| Corpus cohort | Documents | Agent flags | Determinate reviewed flags | Unresolved reviews | Total judgments |
|---|---:|---:|---:|---:|---:|
| established::human | 5 | 27 | 24 | 46 | 75 |
| established::ai_fresh | 5 | 43 | 28 | 24 | 75 |
| established::ai_rewrite | 5 | 34 | 20 | 23 | 75 |
| pilot_additions::human | 10 | 30 | 26 | 81 | 150 |
| pilot_additions::ai | 10 | 49 | 16 | 60 | 150 |

## Independent-review verdicts

| Verdict | Count |
|---|---:|
| supported | 232 |
| overcall | 40 |
| undercall | 19 |
| misclassified | 29 |
| insufficient_evidence | 205 |

Determinate reviewed flags apply supported judgments, remove overcalls, and add undercalls. They are a lower bound, not a replacement score: misclassified and insufficient-evidence judgments remain unresolved.

## Judgment reliability by record

| Record | Agent flags | Supported | Overcall | Undercall | Misclassified | Insufficient evidence |
|---|---:|---:|---:|---:|---:|---:|
| structural_monotony | 20 | 2 | 1 | 3 | 3 | 26 |
| tonal_uniformity | 25 | 2 | 1 | 7 | 1 | 24 |
| faux_specificity | 13 | 19 | 4 | 0 | 0 | 12 |
| neutrality_collapse | 0 | 9 | 0 | 0 | 0 | 26 |
| even_jargon_distribution | 1 | 1 | 1 | 1 | 17 | 15 |
| forced_synesthesia | 3 | 18 | 0 | 0 | 2 | 15 |
| generic_metaphors | 21 | 26 | 3 | 3 | 0 | 3 |
| referential_clarity | 5 | 18 | 1 | 1 | 1 | 14 |
| formulaic_parallelism | 20 | 23 | 5 | 0 | 0 | 7 |
| semantic_redundancy | 21 | 17 | 11 | 1 | 0 | 6 |
| underspecified_language | 33 | 29 | 4 | 1 | 0 | 1 |
| context_leakage | 7 | 17 | 4 | 1 | 0 | 13 |
| performed_candour | 6 | 20 | 1 | 0 | 0 | 14 |
| vacuous_connection | 6 | 15 | 4 | 0 | 0 | 16 |
| genre_specific | 2 | 16 | 0 | 1 | 5 | 13 |

## Interpretation

- The raw agent run flags established AI-fresh prose +16 more times than established human prose, and AI rewrites +7 more times.
- The raw agent run flags pilot AI prose +19 more times than pilot human prose.
- Independent review does not validate those gaps as a performance score. Insufficient-evidence judgments are intentionally unresolved, and overcalls are concentrated in broad semantic categories such as redundancy and formulaic parallelism.
- The largest category-definition problem is even_jargon_distribution; most disagreements concern the registry's forced choice between clumped, natural, and uniform distribution.
- Tonal_uniformity remains unstable: reviewers both removed genre-appropriate uniformity flags and found missed uniformity, while many answers lacked enough preserved evidence to adjudicate.

## Preservation and limitations

- Annotator prompts, raw events, native work bundles, and full Audit JSON are retained per document.
- Reviewer prompts, raw events, and one verdict for every registry judgment are retained per document.
- Reviewer citation validation found 5 non-exact evidence strings; these are retained as quality issues and were not silently repaired.
- Corpus and cohort labels were absent from model prompts; `index.json` restores the mapping for analysis.
- These are model judgments, not authorship ground truth. Review disagreement is evidence about judgment reliability.
