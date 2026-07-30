# blader/humanizer

## Metadata

- **URL:** https://github.com/blader/humanizer
- **Author / owner:** Siqi Chen / blader
- **Published:** initial commit 2026-01-17; reviewed revision committed 2026-06-29
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** first-party practitioner skill repository and writing-pattern catalogue
- **Evidence tier:** Conduit / catalogue sources
- **Review mode:** update
- **Stable identifier:** commit 1b48564898e999219882660237fde01bf4843a0f
- **Version / revision:** SKILL.md and plugin version 2.8.2 at commit 1b48564898e999219882660237fde01bf4843a0f; previous reviewed capture was an unpinned README whose version history ended at 2.5.1
- **Full-text status:** complete
- **Snapshot:** `snapshots/blader-humanizer.md`
- **Extraction method:** full Git clone over HTTPS, history and tree verification, `git archive`, and byte-preserving UTF-8 concatenation of every tracked file
- **Snapshot SHA-256:** `64049e20de5e65fa8deae28699cd16b3f2cbc77d93433c910e24a400c8c9c485`
- **Model / corpus scope:** English-language prompt guidance for unspecified LLMs and prose genres; compatibility is declared `any-agent`. The source supplies 33 named pattern families, constructed before/after examples, one composite rewrite demonstration, process instructions, and qualitative false-positive controls, but no model versions, prompts used to establish the catalogue, corpus dates, measured sample, comparison group, prevalence, accuracy, reader study, or independent evaluation.
- **Access limitations:** none for the reviewed commit tree. All six tracked files and the complete commit tree are preserved. The linked Wikipedia pages and plugin-schema URLs were not recursively ingested; claims inherited from Wikipedia remain indirect. The repository contains no executable detector, test suite, or outcome data: `SKILL.md` is the runtime prompt.

## Summary

`blader/humanizer` is the prompt-only practitioner skill from which human-eyes records its lineage. The complete pinned repository replaces the former README-only record and exposes the actual version 2.8.2 instructions: identify 33 named patterns, preserve topic and approximate scope, optionally imitate a supplied writing sample, create a draft, critique that draft as “obviously AI generated”, and return a final rewrite with no em or en dashes. It also contains an explicit false-positive section, positive “human writing” heuristics, and a worked Lisbon rewrite. Human-eyes overlaps with most catalogue families but has a stricter Audit boundary, source-bound preservation, separate deterministic and agent-assessed registries, contextual thresholds, and no-authorship reporting. This complete source changes the migration record materially, but it remains lineage and practitioner prior art rather than independent evidence that a pattern is AI-specific or that the rewrite procedure works.

## Main insights

- The repository is useful as lineage, implementation, and migration evidence. It is not empirical validation: its pattern explanations, before/after rows, false-positive guidance, “human” indicators, and composite example have no disclosed measured corpus, comparison group, rates, model versions, independent raters, or outcome evaluation.
- The actual implementation is a 622-line Markdown prompt, not a deterministic detector. “33 Patterns Detected” means the model is instructed to scan for 33 categories; the repository does not establish reproducible candidate recognition, thresholds, recall, specificity, or rewrite success.
- The full skill adds four families absent from the old 2.5.1 capture: diff-anchored writing, manufactured punchlines/staccato drama, aphorism formulas, and conversational rhetorical openers. Human-eyes fully recognises the source's staccato example, partly overlaps the aphorism and candid-opener ideas, and does not recognise the exact diff-anchored, signposting, fragmented-header, aphorism, or `Honestly?` examples with the closest deterministic checks.
- The source now includes useful qualifications: second-hand text, quotations, common transitions, curly quotes, em dashes, formal vocabulary, polish, and isolated short sentences are not reliable indicators alone; clusters matter. These are qualitative practitioner cautions, not measured false-positive rates.
- The skill's dash policy is internally inconsistent. Pattern 14 and the final-output gate require zero em or en dashes, while the false-positive section says em dashes alone are not reliable and should count only with a formulaic sales-like rhythm. Human-eyes also recognises any em dash but documents contextual and deliberate-use qualifications; this source cannot justify a hard cut.
- The source's “personality and soul” advice permits adding opinions, first person, humour, tangents, and “mess” when voice calls for it, but its task also requires preserving meaning and matching the intended register. Human-eyes is stricter: it forbids adding any unsupplied opinion, experience, humour, emotion, doubt, or personal detail.
- README.md and SKILL.md are not perfectly aligned despite AGENTS.md calling the skill the source of truth. The README's curly-quotes table still renders the same curly form in both columns, its compound-modifier summary says to drop common hyphens, and its pattern-21 summary names only cutoff disclaimers; SKILL.md correctly shows straight quotes, limits de-hyphenation to predicate position, and expands pattern 21 to speculative gap-filling.
- README.md's version history reports that version 2.6.0 removed a model-fingerprinting subsection. This repository-history statement supports the migration record and aligns with human-eyes' no-authorship boundary, but it is not empirical evidence that fingerprinting is invalid and does not come from the old partial snapshot.
- The pinned tree verifies version 2.8.2, 33 unique numbered patterns in both README and SKILL, six tracked files, 39 commits, and MIT licensing. It contains no tests or executable implementation, so repository completeness does not upgrade the catalogue's evidence tier.

## Evidence and claims to extract

- **Direct source reviewed:** all six tracked files at commit `1b48564898e999219882660237fde01bf4843a0f`: `.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`, `AGENTS.md`, `LICENSE`, `README.md`, and the runtime `SKILL.md`. The full tree is preserved in the snapshot and `snapshots/attachments/blader-humanizer-1b48564.tar.gz`.
- **Method and sample:** first-party Markdown prompt, package metadata, documentation, constructed examples, and one source-provided composite rewrite. SKILL.md supplies 33 named pattern sections, a voice-calibration procedure, register-conditioned personality guidance, false-positive and human-writing heuristics, and a draft-audit-final workflow. It supplies no measured sample or executable evaluation.
- **Direct versus cited evidence:** C01-C02, C04, C06-C37, and C39-C46 are direct repository instructions, examples, metadata, or version claims. C03, C05, and C38 are inherited or quoted Wikipedia claims. None of the pattern rows becomes independent AI-versus-human evidence merely because a prompt implements it.
- **Important limits and counterexamples:** unspecified models, dates, genres beyond broad prose categories, languages beyond English examples, prevalence, thresholds, accuracy, and external validation. The source does contain qualitative human look-alikes and cluster cautions, plus internal contradictions and README/SKILL drift. Focused live-project calls are surface-only mechanism checks, not complete Audits and not evidence of authorship.

## Matched patterns / rules

- Direct deterministic descendants or close equivalents: `no-significance-inflation`, `no-notability-claims`, `no-superficial-ing`, `no-promotional-language`, `no-vague-attributions`, `no-ai-vocabulary-clustering`, `no-copula-avoidance`, `no-negative-parallelisms`, `no-forced-triads`, `no-em-dashes`, `no-boldface-overuse`, `no-inline-header-lists`, `no-unicode-flair`, `no-curly-quotes`, `no-collaborative-artifacts`, `no-knowledge-cutoff-disclaimers`, `no-filler-phrases`, `no-excessive-hedging`, `no-generic-conclusions`, `no-compound-modifier-density`, `no-formulaic-openers`, and `no-staccato-sequences`.
- Folded or split descendants: tailing negation also relates to `no-negation-density` and `no-countdown-negation`; emojis are folded into `no-unicode-flair`; sycophancy is folded into `no-collaborative-artifacts`; triad accumulation is measured by `no-forced-triads` as a rate per 1000 words; persuasive authority framing overlaps `no-formulaic-openers` and `no-manufactured-insight`.
- Catalogue descendants at the time of review: formulaic challenges sections, synonym cycling, false ranges, and title-case headings in `_extra_entries`, all carrying a pattern number with no check behind them. That state is resolved: A6 false ranges became programmatic through DR-157, C3 title case through DR-21G, and #6 and #11 were removed through DR-155 and DR-156. C17's documentation objection applied to #11's repetition-penalty wording, which no longer exists in the catalogue.
- Partial agent-assessed descendant: `underspecified_language` in `judgement.json` asks for the missing criterion, property, actor, or action; this can cover the missing-actor/action aspect of C19 but is not a general passive-voice check.
- Partial conceptual overlap for newer families: `no-manufactured-insight`, `generic_metaphors`, `performed_candour`, `no-performed-candour`, and `no-rhetorical-questions` cover adjacent aphoristic or candid mechanisms, but the exact source examples stay clear in focused deterministic calls; `human-eyes/references/process.md` discourages change narration but no check recognises the diff-anchored example.
- No equivalent live entry established by this source: a general passive-voice check, formulaic-challenges enforcement, the two signposting-announcement examples, the fragmented-header example, or exact diff-anchored writing coverage.
- Workflow descendants: the current `human-eyes/SKILL.md`, `human-eyes/references/process.md`, and `dev/TESTING.md` replace the source's generic audit-and-second-rewrite statement with complete Audit, source-preservation, changed-context validation, and bounded revision requirements.

## Associated hypotheses

- H1, continuous calibrated register-distance score per pattern: relevant because inherited examples behave differently under current thresholds.
- H9, field-guide voice with similar-species disambiguation per pattern: relevant because the upstream catalogue supplies no human look-alikes or context controls.
- H12, genre-aware threshold calibration: relevant because the source makes broad cross-genre rules without a genre sample.
- H14, AGENTS.md, STATUS.md, active-plan invariant, docs/solutions: relevant to preserving lineage and migration state as project documentation.
- H17, calibration golden set gating grader changes: required before any inherited gap becomes a product change.
- H24, Bayesian severity from co-occurrence rather than isolated signals: relevant to the source's cluster caution and its contradictory zero-dash rule.
- H25, model-family versus generic-AI residue: relevant because the source names no model or version behind any pattern claim.
