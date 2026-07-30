# Onur Solmaz: kill-ai-smell skill and ai-smell stylometric corpus

## Metadata

- **URL:** https://github.com/osolmaz/tools/tree/main/agents/skills/kill-ai-smell; https://github.com/osolmaz/ai-smell; linked but not preserved or reviewed: https://solmaz.io/ai-de-smeller
- **Author / owner:** Onur Solmaz (osolmaz)
- **Published:** none stated for the reviewed files; the corpus README says the attributed AI pages were fetched on 2026-07-13; living GitHub repositories
- **Retrieved:** 2026-07-14
- **Extracted:** 2026-07-15
- **Source type:** practitioner de-smelling skill, deterministic checker, evidence note, and self-collected corpus report
- **Evidence tier:** Practitioner / teacher / editor essay with attached corpus analysis; measured findings remain limited to one author, one asserted model, one register pairing, and 18 labelled documents
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** unchanged 2026-07-14 capture from the moving `main` branches; prior pre-contract capture archived; no commit SHA was recorded
- **Full-text status:** complete
- **Snapshot:** `snapshots/solmaz-kill-ai-smell.md`
- **Extraction method:** direct raw GitHub files fetched from raw.githubusercontent.com at branch main; GitHub Contents API used to confirm the tools tree; complete reviewed text of SKILL.md, check.py, evidence.md, and the ai-smell README concatenated into Markdown
- **Access routes:** `https://raw.githubusercontent.com/osolmaz/tools/main/agents/skills/kill-ai-smell/SKILL.md`; `https://raw.githubusercontent.com/osolmaz/tools/main/agents/skills/kill-ai-smell/check.py`; `https://raw.githubusercontent.com/osolmaz/tools/main/agents/skills/kill-ai-smell/evidence.md`; `https://raw.githubusercontent.com/osolmaz/ai-smell/main/README.md`; tools tree confirmed through `https://api.github.com/repos/osolmaz/tools/contents/agents/skills/kill-ai-smell?ref=main`
- **Snapshot SHA-256:** `6d4a0248916a8fe2dd53dd203983f018b1fd181766ca6e6073837f501c3897ed`
- **Model / corpus scope:** ten English OpenClaw landing pages attributed by the author to GPT 5.5, fetched 2026-07-13, totalling 4,853 prose words; eight pre-LLM English human texts from 2000 to 2019 and 2016 to 2017 repository tags, totalling 15,317 words; 42 unlabelled long-form tweet samples; one skill-compliant control described by the preserved source as known AI, with no model or generation tool named in the snapshot
- **Access limitations:** complete text is preserved for the four reviewed source files. The snapshot does not embed the linked corpus documents, analysis scripts, result files, experiment journal, blog post, generation prompts, raw model outputs, or per-page authorship records. No repository commit SHA was preserved, and the claimed GPT 5.5 provenance cannot be independently reconstructed from the snapshot.

## Summary

Solmaz presents a writing skill, a standard-library checker, and an 18-document comparison between ten landing pages he attributes to GPT 5.5 and eight pre-LLM human texts. The strongest reported findings include narrow exact triads, labelled-bullet share, sentence flow, and the paired MTLD and Zipf lexical axes, while register controls weaken first-person and raw TTR claims. The source also preserves null results and identifies several skill or checker rules that lack matching measurements. For human-eyes, the source contributes useful candidates and calibration cautions, but it does not validate a classifier or justify single-document authorship conclusions. The live catalogue partly covers many concepts while using materially different recognisers or thresholds, and it is directly challenged on low TTR, any-em-dash severity, blanket contrast treatment, and register lock.

## Main insights

- Narrow exact triads above 3 per 1,000 words and labelled bullets above 30 per cent of all bullets each separate the source's 18 labelled documents, but both results need transfer and minimum-support testing before product use.
- Mean longest punctuation-free sentence run below 10 is the source's strongest reported rhythm result. It is absent from the live checker and is not equivalent to sentence-length variance.
- MTLD and mean Zipf frequency point towards high lexical novelty and less common connective vocabulary in the attributed AI set. Raw TTR overlaps and becomes register-sensitive after README controls.
- The source's own evidence weakens or contradicts several categorical ideas, including Title Case as an AI sign, first person, raw TTR, and order-only rhythm statistics. The separate project comparison at `docs/research/2026-07-14-solmaz-ai-de-smeller-comparison.md` records that linked results not preserved here do not support a blanket `not just` rule or validate the colon-pivot subtype from raw colon frequency.
- Extreme em-dash density is one-directional evidence in this corpus. Some attributed AI pages use fewer em dashes than a human README, and one uses none.
- Several hard checker rules and skill prohibitions are editorial positions without published corpus distributions. Checker severity is not evidence strength.
- The operational advice to restructure rather than substitute tokens, rerun checks after each edit, and treat a clean surface sweep as incomplete is consistent with the live project process.

## Evidence and claims to extract

- **Direct source reviewed:** the complete preserved 2026-07-14 text of `kill-ai-smell` SKILL.md, check.py, evidence.md, and the ai-smell README, with digest `6d4a0248916a8fe2dd53dd203983f018b1fd181766ca6e6073837f501c3897ed`.
- **Method and sample:** descriptive and exploratory stylometry over ten attributed GPT 5.5 English landing pages and eight pre-LLM English human controls, including three register-matched historical READMEs. The source also reports 42 unlabelled tweet samples and one instructed AI self-control. Rates are normalised per 1,000 words where stated. The source describes about fifty exploratory flow experiments and leave-one-out performance, but the underlying scripts, journal, results, and corpus files are linked rather than embedded in this snapshot.
- **Direct versus cited evidence:** C02 to C15 and C19 to C22 report measurements, rules, nulls, or operating claims stated directly in the preserved files. C16 to C18 are direct skill or checker positions whose empirical basis is absent or incomplete. The earlier identity and heading guidance named by the source remains indirect here because those upstream materials were not separately ingested for this card.
- **Important limits and counterexamples:** AI provenance is the author's assertion; no prompts or generation logs are preserved; the labelled corpus has one asserted model, one landing-page register, and 18 documents; the tweet set has no human or AI ground truth; the self-control is coached; several numeric boundaries were selected on the same material used to report separation; aggregate differences do not prove authorship for one document.

## Matched patterns / rules

- `no-forced-triads` (B4): related but broader and differently thresholded than Solmaz's narrow exact-triad rate.
- `no-inline-header-lists` (C2) and `no-excessive-lists` (G3): related but do not calculate labelled bullets as a share of all bullets with Solmaz's separators.
- `sentence-length-variance` (G9), `no-staccato-sequences` (E5), and `paragraph-length-uniformity`: related rhythm measures, not sentence flow.
- `vocabulary-diversity` (B5), `no-ai-vocabulary-clustering` (B1), and H24: relevant lexical coverage; B5 is directly challenged. Former #11 synonym cycling was removed 2026-07-25 through DR-156.
- `no-em-dashes` (C7), `no-negative-parallelisms` (B3), `no-false-concession-hedges` (E3), `no-filler-phrases` (E1), `no-excessive-hedging` (E2), and `no-signposted-conclusions` (G8): live treatment exists but differs from the source's evidence and uncertainty.
- `no-anaphora` (H14), `no-this-chains` (H5), `formulaic_parallelism`, `structural_monotony`, `semantic_redundancy`, and `no-section-scaffolding` (G6): partial coverage for repeated forms and templates.
- `no-copula-avoidance` (B2), `no-formulaic-openers` (E8), and `genre_specific`: adjacent to identity position and register controls, but not equivalent.
- Title Case guidance (C3), `no-rhetorical-questions` (G1), `no-unicode-flair` (G4 and C4), and `tonal_uniformity` (H3): partial or conflicting coverage for heading form, rhetoric, emoji use, and register.
- `human-eyes/references/process.md`, `STRATEGY.md`, and `dev/TESTING.md`: cover restructuring, executed resweeps, complete-audit requirements, matched controls, provenance, and the non-authorship boundary.

## Associated hypotheses

- H1, continuous calibrated register-distance score per pattern.
- H3, drop detection framing entirely.
- H7, five-check gating grader plus advisory catalogue.
- H9, field-guide voice with similar-species disambiguation.
- H11, manufactured insight is register-coded in long-form essay.
- H12, genre-aware threshold calibration.
- H13, sentence-length mean as a grader check.
- H22, long-tail compression and grammatical standardisation.
- H24, register-specific vocabulary density.
- H25, model-family versus generic-AI residue.
- H27, performative profundity and aphoristic closure.
