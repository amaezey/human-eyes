# NousResearch/autonovel: ANTI-SLOP

## Metadata

- **URL:** https://github.com/NousResearch/autonovel/blob/master/ANTI-SLOP.md
- **Author / owner:** NousResearch
- **Published:** none found; living GitHub repository reviewed from the `master` branch
- **Retrieved:** 2026-07-14
- **Extracted:** 2026-07-15
- **Source type:** practitioner project reference for an autonomous novel-writing and editing pipeline
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** none found; `master` branch as retrieved 2026-07-14
- **Version / revision:** current contract extraction from the preserved `master` branch snapshot; the previous pre-contract card used the same source bytes
- **Full-text status:** complete
- **Snapshot:** `snapshots/nousresearch-autonovel-anti-slop.md`
- **Extraction method:** existing GitHub Markdown snapshot containing complete `ANTI-SLOP.md` and repository `README.md` files from the `master` branch; no refetch in this update
- **Snapshot SHA-256:** `f365ff47f24fb66fb659058dcdb3d5fd71d3e5f1b7b63519ce0f06d9138c5f92`
- **Model / corpus scope:** generated English fiction in the autonovel pipeline; the README names Anthropic Sonnet and Opus model families without versions and reports one 79,456-word novel; the anti-slop lists have no disclosed model set, comparison corpus, collection dates, sample counts, or error analysis
- **Access limitations:** no text is missing from the two reviewed files; the pre-contract retrieval did not preserve a commit SHA or revision URL, and linked papers, tools, datasets, and vocabulary analyses were not independently reviewed for this card

## Summary

This practitioner guide supplies vocabulary lists, structural review prompts, register-specific editing advice, detector descriptions, and a mechanical checklist used within an autonomous fiction pipeline. Its strongest contribution to human-eyes is as a catalogue of candidate surfaces and fiction-editing prompts. It does not validate its vocabulary tiers, numeric cut-offs, detector claims, or authorship language against a disclosed human comparison corpus. Comparison with the live project finds substantial partial coverage, including stronger context and non-authorship safeguards, while exposing a direct threshold conflict for em dashes and several unimplemented list, transition, and document-structure heuristics.

## Main insights

- The source separates 22 Tier 1 vocabulary items, 24 Tier 2 items, and 26 Tier 3 filler templates. Tier 1 calls for rewriting every occurrence, Tier 2 triggers at three items in one paragraph, and Tier 3 calls for deletion.
- The live `no-ai-vocabulary-clustering` check recognises 11 of the 22 Tier 1 rows and 18 of the 24 Tier 2 rows in focused candidate tests, but it only fails when three recognised items cluster in one paragraph. This is partial coverage, not adoption of the source's tier scheme.
- Only six of the 26 Tier 3 templates were individually surfaced by the most relevant live deterministic checks in focused tests: `It's worth noting that`, `In conclusion`, `To summarize`, `In today's fast-paced world`, `At the end of the day`, and `Not just X, but Y`. The remaining templates require broader matching or contextual assessment.
- Structural claims about paragraph templates, symmetry, list grammar, list nesting, list lengths, transition openings, false depth, sentence and paragraph variation, voice, and topic-swappable generality range from partial coverage to no direct implementation.
- The source permits one or two em dashes per page and proposes a rewrite trigger above two per page, representing the mark as two ASCII hyphens in its prose and examples. The live `no-em-dashes` check recognises any U+2014 occurrence but not the source's displayed `--` form. Its context gate suppresses U+2014 findings only for text matching narrow dialogue-or-fiction or formal-report formats, despite catalogue guidance that literary prose can use the mark deliberately.
- Focused tests found that `no-collaborative-artifacts` recognises only two of the source's four sycophantic-opening examples. The live catalogue describes broader coverage than the executable pattern set provides.
- The source's perplexity, Pangram, EQ-Bench, GPTZero, slop-forensics, detector accuracy, and human-recognition statements are inherited claims. The preserved files do not reproduce the cited methods, datasets, calibration, or results.
- The source itself warns about false positives, short-text unreliability, model drift, non-native English bias, and the effect of editing. Those caveats conflict with its own language about dead giveaways and universal rewrite rules.
- The parent pipeline separates mechanical regex checks from model judgement for prose quality, voice, character distinctiveness, and beat coverage. Its score thresholds and production history do not validate the anti-slop list.

## Evidence and claims to extract

- **Direct source reviewed:** the complete preserved `ANTI-SLOP.md` and repository `README.md` files retrieved from the `master` branch on 2026-07-14. The current snapshot and archived pre-contract copy have identical SHA-256 values.
- **Method and sample:** practitioner rules used in an autonomous English novel-writing pipeline. The README reports a first novel of 79,456 words and names Sonnet and Opus families without versions. The source supplies no human comparison sample, model-by-model sample, corpus period, annotation process, false-positive count, precision, recall, or validation of its tiers and thresholds.
- **Direct versus cited evidence:** C01 to C11 and C15 are direct descriptions, prescriptions, examples, or workflow statements in the reviewed repository files. C12 to C14 and C17 summarise detector and statistical claims that the source inherits from linked work without reproducing the underlying evidence. C16 combines direct checklist prompts with an inherited detector-signal claim about missing personal markers.
- **Important limits and counterexamples:** many listed words have legitimate literal or register-specific uses; fiction can deliberately use symmetry, lists, hedges, repetition, and em dashes; the source's checklist mixes candidate recognition, editing preference, and provenance language; detector caveats undermine single-surface verdicts; and the repository's successful production claim does not establish rule accuracy.

## Matched patterns / rules

- Pattern B1, `no-ai-vocabulary-clustering`, recognises a subset of both vocabulary tiers and fails at three recognised items in a paragraph. `overall-signal-stacking` uses vocabulary only as one component alongside structural evidence.
- Pattern E1, `no-filler-phrases`; pattern E6, `no-soft-scaffolding`; pattern E8, `no-formulaic-openers`; and `no-signposted-conclusions` cover parts of Tier 3.
- Pattern B3, `no-negative-parallelisms`, directly recognises `not just X, but Y` and related negative-positive reframes. H11 records a matched-corpus challenge to treating the construction as straightforward AI evidence.
- Pattern C7, `no-em-dashes`, recognises any U+2014 em dash, but not the source's displayed `--` form, with narrow dialogue-or-fiction and formal-report context gates in `grade.py`. This conflicts with the source's density thresholds and with the catalogue's own literary-prose tolerance note.
- Pattern G3, `no-excessive-lists`, measures list-line share and list-block counts; patterns B4 recognise triads and triad density; pattern C2 covers inline-header lists. None implements three-level nesting, three-or-five item list lengths, repeated grammatical starts, or semantic misuse of lists.
- `structural_monotony`, `formulaic_parallelism`, `semantic_redundancy`, `paragraph-length-uniformity`, `no-tidy-paragraph-endings`, `tonal_uniformity`, `faux_specificity`, `generic_metaphors`, and `genre_specific` provide partial semantic and structural coverage.
- Pattern E2, `no-excessive-hedging`, fails at three recognised impersonal hedge constructions, while B1, E1, E6, E8, and `no-anaphora` cover only parts of the source's transition and opening lists.
- Pattern D1, `no-collaborative-artifacts`, recognises two of the four named sycophantic openings in focused tests: `Great question!` and `Absolutely! Let me explain...`. It does not recognise `That's an excellent point.` or `You raise an important consideration.` even though the live catalogue presents closely related sycophancy coverage. Pattern G7, `no-manufactured-insight`, and the `context_leakage` and `semantic_redundancy` assessments cover parts of false-depth and pasted-chat residue.
- Pattern G9, `sentence-length-variance`, pattern B5, `vocabulary-diversity`, and `paragraph-length-uniformity` are adjacent to the source's statistical signals but do not implement its claimed perplexity, MATTR, entropy, trigram, or classifier features.
- `STRATEGY.md`, `human-eyes/references/process.md`, and `dev/TESTING.md` require specific evidence, contextual treatment, matched comparisons, weak-case reporting, and no individual-document authorship verdict.

## Associated hypotheses

- H3, drop detection framing entirely.
- H9, field-guide disambiguation for legitimate look-alikes.
- H11, manufactured insight and negative parallelism are register-coded in long-form essay.
- H12, genre-aware threshold calibration.
- H22, long-tail compression and grammatical standardisation.
- H24, register-specific vocabulary density.
- H25, model-family versus generic-AI residue.
- Proposed follow-up: test whether list shape, transition openings, and punctuation density add useful evidence after register, length, quotation, and deliberate-use controls.
