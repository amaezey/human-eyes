# jalaalrd/anti-ai-slop-writing

## Metadata

- **URL:** https://github.com/jalaalrd/anti-ai-slop-writing
- **Alternate access URLs:** GitHub repository API `https://api.github.com/repos/jalaalrd/anti-ai-slop-writing`; commit API `https://api.github.com/repos/jalaalrd/anti-ai-slop-writing/commits/63255f9bbb75a265dc5786a04535cd033f487756`; recursive tree API `https://api.github.com/repos/jalaalrd/anti-ai-slop-writing/git/trees/63255f9bbb75a265dc5786a04535cd033f487756?recursive=1`; raw README `https://raw.githubusercontent.com/jalaalrd/anti-ai-slop-writing/63255f9bbb75a265dc5786a04535cd033f487756/README.md`; raw skill `https://raw.githubusercontent.com/jalaalrd/anti-ai-slop-writing/63255f9bbb75a265dc5786a04535cd033f487756/skills/anti-ai-slop-writing/SKILL.md`; raw banned-language reference `https://raw.githubusercontent.com/jalaalrd/anti-ai-slop-writing/63255f9bbb75a265dc5786a04535cd033f487756/skills/anti-ai-slop-writing/references/banned-words.md`
- **Author / owner:** Jalaaldeen, GitHub owner `jalaalrd`
- **Publisher:** `jalaalrd` on GitHub
- **Published:** repository created 2026-03-27; living repository reviewed at the commit below
- **Retrieved:** 2026-07-14
- **Extracted:** 2026-07-14
- **Source type:** practitioner agent-skill repository and prescriptive banned-language catalogue
- **Evidence tier:** Conduit / catalogue sources
- **Review mode:** update
- **Stable identifier:** Git commit 63255f9bbb75a265dc5786a04535cd033f487756
- **Version / revision:** commit `63255f9bbb75a265dc5786a04535cd033f487756`; prior pre-contract record reviewed the same commit
- **Full-text status:** complete
- **Snapshot:** `snapshots/jalaalrd-anti-ai-slop-writing.md`
- **Extraction method:** complete recursive GitHub API tree inspection plus commit-pinned raw Markdown copies of `README.md`, `skills/anti-ai-slop-writing/SKILL.md`, and `skills/anti-ai-slop-writing/references/banned-words.md`, concatenated into the preserved snapshot
- **Snapshot SHA-256:** `6ac610a07021e4f5752dfa349d6c06bc9b1aac34c44005a8382e05eab5fbc4ad`
- **Model / corpus scope:** prescriptive English-language catalogue naming ChatGPT, Claude, Grok, Gemini, and DeepSeek without versions, prompts, sample sizes, or human controls; vocabulary periods are labelled 2023 to mid 2024, mid 2024 to mid 2025, and mid 2025 onward
- **Access limitations:** no repository text used for this review is missing; the source does not identify or link the claimed Carnegie Mellon study, Buffer analysis, or X and Reddit evidence, and supplies no underlying corpus, measurements, implementation, or validation results

## Summary

This repository packages a hard-ban vocabulary and style catalogue as a portable agent skill. The preserved snapshot contains the complete reviewed repository text at one commit. Its useful contribution to human-eyes is a set of candidate strings, numeric lint proposals, channel-specific formatting prompts, factuality safeguards, voice questions, and a pre-output checklist. It is not empirical pattern evidence: it supplies no reproducible corpus, comparison group, model versions, rates, error analysis, or validation, and its cited research is not identifiable from the repository. The update therefore maps every claim to the live catalogue while leaving all product recommendations pending.

## Main insights

- The package separates a concise instruction file from an on-demand banned-language reference and requires both a pre-writing load and a final self-check.
- Its lexical catalogue overlaps several live human-eyes checks, but the source uses blanket bans where human-eyes generally uses clustering, density, genre, quotation, and deliberate-use controls.
- Its model-specific first-word lists and era labels are unmeasured. They support provenance questions, not model attribution or a generic authorship rule.
- Several structural proposals have live analogues, including triads, staccato sequences, sentence-length variance, repeated section structure, excessive lists, and tidy paragraph endings. The live thresholds and constructs are not identical to the source's rules.
- The source's factuality and voice advice partly aligns with the project's closed-record and voice-preservation process, but advice to add friction, personal detail, humour, doubt, or roughness conflicts with that process when the source or brief does not supply those facts.
- The repository says it catches 10 structural patterns, while its skill lists 11 structural rules. Its final em-dash self-check is also stricter than the body rule for pieces long enough to permit more than one under the stated rate.
- The source's strongest claims, including that uniform sentence length is the single most measurable signal and that certain constructions immediately signal AI authorship, have no evidence in the repository and exceed human-eyes' product boundary.

## Evidence and claims to extract

- **Direct source reviewed:** the complete recursive repository tree and the three substantive Markdown files preserved in `snapshots/jalaalrd-anti-ai-slop-writing.md`, all at Git commit `63255f9bbb75a265dc5786a04535cd033f487756`.
- **Method and sample:** qualitative review of one English-language practitioner repository. The source names five model families and three broad vocabulary periods but provides no model versions, prompts, sample sizes, collection dates, human comparison, annotation method, text-length controls, or evaluation.
- **Direct versus cited evidence:** C01 to C58 are direct descriptions of rules, lists, examples, packaging, unsupported interpretations, or internal inconsistencies in the repository. None is an empirical result measured by the repository. The named Carnegie Mellon, Wikipedia, Buffer, X, and Reddit inputs are indirect and unresolved because the repository does not identify them sufficiently for direct review.
- **Important limits and counterexamples:** the rules are prescriptive catalogue observations, not authorship evidence. Human writers legitimately use every listed word, punctuation mark, sentence shape, list form, and rhetorical device in context. The source provides no precision, recall, prevalence, false-positive analysis, comparison group, or before-and-after compliance test. Its rigid bans can penalise genre conventions and deliberate voice.

## Matched patterns / rules

- Deterministic checks: `no-ai-vocabulary-clustering`, `no-promotional-language`, `no-corporate-ai-speak`, `no-significance-inflation`, `no-filler-phrases`, `no-formulaic-openers`, `no-negative-parallelisms`, `no-collaborative-artifacts`, `no-generic-conclusions`, `no-signposted-conclusions`, `no-forced-triads`, `sentence-length-variance`, `no-staccato-sequences`, `no-excessive-hedging`, `no-false-concession-hedges`, `no-section-scaffolding`, `paragraph-length-uniformity`, `no-tidy-paragraph-endings`, `no-excessive-lists`, `no-em-dashes`, `no-boldface-overuse`, `no-inline-header-lists`, `no-unicode-flair`, `no-vague-attributions`, and `vocabulary-diversity`.
- Agent assessments: `structural_monotony`, `tonal_uniformity`, `faux_specificity`, `neutrality_collapse`, `underspecified_language`, `formulaic_parallelism`, `semantic_redundancy`, `vacuous_connection`, and `genre_specific` in `human-eyes/scripts/judgement.json`.
- Process guidance: `human-eyes/references/process.md` preserves source meaning, treats source text and briefs as closed factual records, prohibits invented experience and detail, and requires complete audits of generated prose.
- Skill routing and action requirements: `human-eyes/SKILL.md` makes Audit the default, requires complete Audits, and limits Write to a supplied brief.
- Product boundary and evaluation controls: `STRATEGY.md` and `dev/TESTING.md` require contextual treatment, matched comparisons, provenance, weak-case reporting, and no individual-document authorship classification.

## Associated hypotheses

- H1, continuous calibrated register-distance scores rather than unqualified binary thresholds.
- H3, remove detection and authorship framing.
- H8, audience-aware voice by invocation surface.
- H9, similar-species and legitimate-use disambiguation for each pattern.
- H12, genre-aware threshold calibration.
- H21, low information density and wrong sentence subjects.
- H22, long-tail compression and grammatical standardisation.
- H24, register-specific and time-sensitive vocabulary density.
- H25, model-family versus generic-AI residue.
