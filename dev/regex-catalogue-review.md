# Deterministic catalogue review

This review treats regexes and structural measurements as candidate extractors, not authorship classification. `candidate_count` and `candidates` report recognition; `threshold_met` reports the check's policy decision; `context_suppressed` records a high-confidence genre exception.

The blind seed contains one example in many cells, so its rates are directional. Expand each tendency to 5–10 independently generated variants and matched controls before promoting any rate to a release gate.

## Action vocabulary

- **Keep:** the deterministic boundary is concrete and reasonably aligned with the documented violation.
- **Broaden:** the idea is deterministic, but the phrase or grammar catalogue is incomplete.
- **Contextualize:** recognition is useful, but genre or quoted-material exclusions must influence disposition.
- **Candidate only:** regex can focus attention, but semantic review should decide whether the prose violates the rule.
- **Merge:** share extraction or disposition with an overlapping check while preserving separate reporting when useful.

## Per-check matrix

| Check | Action | Review note |
|---|---|---|
| `no-em-dashes` | Contextualize | Preserve recognition, but suppress licensed literary dialogue and concise formal-report asides. Do not treat case as relevant. |
| `no-ai-vocabulary-clustering` | Contextualize | Keep paragraph clustering; mask quotations, code, URLs, and source examples. Merge shared vocabulary extraction with significance and promotional families. |
| `no-nonliteral-land-surface` | Broaden | Maintain literal/nonliteral disambiguation tests; expand grammatical subjects and inflections only from observed misses. |
| `overall-signal-stacking` | Keep | Aggregate only independent structural families; do not count several vocabulary lists as separate signals. |
| `no-manufactured-insight` | Candidate only | Phrase extraction is useful, but profundity and contrarian framing require semantic disposition. |
| `no-performed-candour` | Broaden | Cover contraction and subject variants; continue masking attributed quotations. |
| `no-staccato-sequences` | Contextualize | Sentence segmentation and genre are load-bearing. Dialogue, recipes, rubrics, and dramatic prose need exclusions. |
| `no-anaphora` | Candidate only | Repetition is easy to recognize but often deliberate rhetoric, poetry, dialogue, or academic contrast. |
| `no-collaborative-artifacts` | Keep | Concrete assistant residue is suitable for deterministic detection after quote/code masking. |
| `no-curly-quotes` | Contextualize | This is a house-style rule rather than an AI signal; keep it out of authorship-style interpretations. |
| `sentence-length-variance` | Contextualize | Retain as a coarse metric with genre and minimum-length gates; improve sentence segmentation first. |
| `no-promotional-language` | Broaden | The phrase list is incomplete and overlaps significance inflation; use word boundaries and inflection families. |
| `no-significance-inflation` | Candidate only | Single words such as “crucial” and “pivotal” need claim-level context. Share extraction with promotional language. |
| `no-negative-parallelisms` | Keep | This is the most thoroughly iterated regex family. Continue mutation tests for punctuation, clause order, subjects, and contractions. |
| `no-copula-avoidance` | Candidate only | “Serves as,” “features,” and “represents” are frequently literal. Semantic review should decide whether the construction is evasive. |
| `no-filler-phrases` | Broaden | Add spelling and line-break variants while retaining exact candidate spans. |
| `no-generic-conclusions` | Merge | Share conclusion extraction and context policy with signposted conclusions and tidy paragraph endings. |
| `no-false-concession-hedges` | Broaden | Cover hand/middle constructions, clause-order reversal, and intervening clauses; preserve concrete debate/report controls. |
| `no-placeholder-residue` | Contextualize | Finished prose should fail; actual templates, code, and review discussions should be suppressed. |
| `no-soft-scaffolding` | Broaden | Return below-threshold candidates; add variants only when repeated connective scaffolding is observed. |
| `no-orphaned-demonstratives` | Candidate only | Candidate extraction is reliable, but antecedent resolution is semantic. Thresholding alone cannot distinguish vague from clear reference. |
| `no-forced-triads` | Candidate only | Regex can identify triads, not whether they are forced. Merge extraction with triad density. |
| `no-superficial-ing` | Candidate only | Syntactic position is detectable; whether the participial clause adds information requires semantic review. |
| `no-ghost-spectral-density` | Contextualize | Preserve density measurement but gate poetry, fiction, criticism, and quoted source text. |
| `no-quietness-obsession` | Contextualize | Preserve density measurement but gate fiction, sensory description, and subject-matter uses. |
| `no-rhetorical-questions` | Candidate only | Recognize question-answer structures case-insensitively; interviews, teaching, polemic, and comedy require semantic disposition. |
| `no-excessive-lists` | Contextualize | Lists are normal in procedures, recipes, references, and API docs. Ratio alone is not sufficient. |
| `no-unicode-flair` | Contextualize | Exclude UI strings, real checklists, code, and quoted social content. Keep the Unicode ranges centralized. |
| `no-dramatic-transitions` | Broaden | Phrase family is narrow; paraphrased narrative pivots are better treated as candidates for semantic review. |
| `no-formulaic-openers` | Broaden | Add observed register variants, spelling changes, and line-break mutations; avoid generic sentence-start regexes. |
| `no-signposted-conclusions` | Contextualize | Suppress reports, troubleshooting guides, academic sections, and reference documentation. Merge policy with conclusion checks. |
| `no-markdown-headings` | Contextualize | Recognize ATX, setext, and plain-title variants, then suppress legitimate structured genres. |
| `no-parenthetical-headings` | Contextualize | Keep actual heading syntax narrow. Parenthetical body prose is not a heading and should not be swept in. |
| `no-corporate-ai-speak` | Broaden | Expand with blind, naturally produced jargon variants and inflections; use matched professional-prose controls. |
| `no-this-chains` | Keep | Consecutive sentence-start structure is deterministic; improve sentence segmentation and expose sub-threshold runs. |
| `no-excessive-hedging` | Contextualize | Count stacked modal and passive hedges, but suppress legitimate limitations and uncertainty reporting. |
| `no-countdown-negation` | Merge | Share negation parsing with negative parallelisms while preserving the repeated-sentence threshold. |
| `no-negation-density` | Contextualize | Preserve normalized density, but distinguish argumentative negation from instructions, legal text, and factual correction. |
| `paragraph-length-uniformity` | Contextualize | Keep the coefficient-of-variation metric; gate short forms and structurally constrained genres. |
| `no-tidy-paragraph-endings` | Candidate only | Generic ending phrases are candidates; paragraph-level rhetorical function requires semantic review. Merge conclusion extraction. |
| `no-bland-critical-template` | Candidate only | Review language is genre-specific and semantically broad; three lexical hits are not enough context by themselves. |
| `no-rubric-echoing` | Contextualize | Suppress rubrics discussed as subject matter and attributed examples; retain student-response candidate extraction. |
| `vocabulary-diversity` | Contextualize | Keep as a coarse length-normalized metric with genre gates; do not interpret it as authorship evidence alone. |
| `no-triad-density` | Merge | Reuse the same triad extractor as `no-forced-triads`, then apply document-length and density policy separately. |
| `no-section-scaffolding` | Contextualize | Repeated labels are legitimate in references, forms, templates, and procedural documentation. |
| `no-notability-claims` | Candidate only | Authority wording can be factual. Named-source and surrounding-evidence checks need semantic or citation-aware disposition. |
| `no-vague-attributions` | Candidate only | Candidate extraction is useful, but source naming can occur elsewhere in the sentence or preceding prose. |
| `no-boldface-overuse` | Contextualize | Preserve density measurement; exclude reference terms, UI labels, and documentation conventions. |
| `no-inline-header-lists` | Contextualize | Bold-label lists are legitimate in glossaries, API docs, specifications, and support material. |
| `no-compound-modifier-density` | Contextualize | Technical and professional registers legitimately require compounds. Expand spelling forms only with matched controls. |
| `no-knowledge-cutoff-disclaimers` | Keep | Model-meta disclaimers are concrete; suppress quoted examples and legitimate source-limitation prose. |

## Required evaluation matrix

For every check marked Broaden, Contextualize, Candidate only, or Merge, maintain:

1. Five to ten violation variants spanning case, contractions, spelling, punctuation, line breaks, inflection, number, intervening clauses, clause order, grammatical subject, and Markdown where applicable.
2. The same number of matched legitimate controls in the genres named above.
3. Candidate recall, threshold recall, specificity, and context-suppression counts reported separately.
4. A documented decision when a candidate is intentionally left to semantic review rather than promoted to a deterministic failure.
