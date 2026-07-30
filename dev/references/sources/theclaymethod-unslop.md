# theclaymethod/unslop

## Metadata

- **URL:** https://github.com/theclaymethod/unslop
- **Author / owner:** Clayton Kim / theclaymethod
- **Published:** initial commit 2026-02-08; reviewed revision committed 2026-07-07
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** first-party practitioner software repository, writing-pattern catalogue, and internal evaluation suite
- **Evidence tier:** Practitioner / teacher / editor essays; this is a practitioner tool with first-party tests and internal benchmarks, not independent validation of its pattern claims
- **Review mode:** new
- **Stable identifier:** commit 1e50bf273d59e6d98477005ec6a086643a6b27ea
- **Version / revision:** SKILL.md version 2.3.0 at commit 1e50bf273d59e6d98477005ec6a086643a6b27ea
- **Full-text status:** complete
- **Snapshot:** `snapshots/theclaymethod-unslop.md`
- **Extraction method:** Full Git clone over HTTPS, full-history fetch, `git archive`, and byte-preserving UTF-8 concatenation of all tracked files
- **Snapshot SHA-256:** `5eb1cd5d1cf2dc4ad61e48f6c1735f50a7b288131dd4a3a8b80f9a9a97e16d68`
- **Model / corpus scope:** English prose; 405 tracked files; 313 phrase entries, 77 structural patterns, and five silhouette metrics claimed in the README, although the pinned phrase scanner actually defines 82 structural regex entries; 479 deterministic script cases and 33 behavioural skill cases present at the pinned commit; silhouette separation corpus of eight human and twelve AI documents, with seven additional structure fixtures also used to build the human reference; recorded model-parity work dated 2026-07-06 and 2026-07-07 across named GPT, Claude, and open-weight models
- **Access limitations:** none for the repository text or pinned tree. The deterministic suite was rerun locally from the pinned archive with `python3 evals/run_adversarial.py`; it exited 1 after reporting 460 passes, one expected failure, and 18 regressions. Behavioural and live model-parity evaluations were not rerun because they require external model tools, including a prohibited Claude-backed path. Their results remain first-party reports. The local deterministic run used Python 3.9.6 on Darwin 25.5.0 arm64.

## Summary

`unslop` is an open-source agent skill and standard-library Python toolkit for detecting and rewriting English prose that carries machine-writing patterns. It combines a phrase scanner, a surface-structure scanner, a discourse-level silhouette scanner, guarded rewrite and suggestion flows, fact-preservation checks, voice profiling, and an eval-first contribution process. Much of its catalogue overlaps human-eyes. Its most distinct contribution is a five-metric attempt to score idea arrangement rather than isolated wording. That candidate is backed only by the repository's small internal corpus. The pinned checkout's official deterministic command also contradicts the README's test claim: it observed 460 passes, one expected failure, and 18 regressions across 479 cases, rather than the advertised 439 passes and one expected failure across 440 cases.

## Main insights

- The repository implements three deterministic layers: phrase matching, surface structure, and discourse silhouette. It presents detection as the trust-bearing part of the product and generation as subordinate to those gates.
- The README's advertised structural-pattern count is stale or otherwise unreconciled with the pinned implementation: it says 77, while `scripts/banned_phrase_scan.py` defines 82 structural regex entries. The separate surface-structure scanner exposes 16 document metrics.
- The phrase layer overlaps many live human-eyes checks, including significance inflation, negative parallelism, vague attribution, corporate language, filler, rhetorical questions, chatbot residue, generic conclusions, and promotional language.
- Context handling is a central design choice. The scanner masks quotations, blockquotes, and code fences by default, gates ambiguous vocabulary by collocation, and pairs target examples with literal or domain-specific controls.
- Those phrase controls are not complete. `FP-06` remains an expected failure for a literal place use of `delve into`, documenting a regex limit rather than a cleanly protected literal sense.
- The structure scanner measures sentence-length coefficient of variation, paragraph coefficient of variation, triad density, short one-line paragraph share, connective openers, signpost density, repeated sentence openers, participial closers, and conclusion codas. It supplies limited `docs` and `social` carve-outs.
- The silhouette scanner measures scaffold openers, cue-role entropy, intro-to-body preview fulfilment, early-to-late callback content, and heading preview. It compares a weighted composite with a committed human reference and flags at 1.0.
- The silhouette evidence is internal and small. The README reports 12 of 12 AI documents flagged and 0 of 8 human documents flagged. The reference comments say its thresholds were validated on those fixtures, not on independent, naturalistic, or human-eyes corpora.
- The source also preserves a silhouette null result: deleting discourse cues lets the dedicated silhouette scanner miss a rigid document, while the paired surface-structure scanner still flags repeated openers. The source therefore treats the two scanners as joint fences rather than claiming that silhouette is independently robust.
- The repository uses categorical language that exceeds its evidence, including hard or always-a-tell labels, a default-zero em dash rule, and claims that the em dash is the most reliable punctuation tell. Those claims do not supply independent rates or register-matched human controls.
- The official deterministic command at the pinned commit reported `PASS 460`, `XFAIL 1`, and `FAIL 18`, then exited 1. The README instead reports 440 cases with 439 passes and one expected failure.
- The 18 failures fall into four visible clusters: catalogue and kata coverage (`DOC-09`, `DOC-10`), harvest and encoding (`HARV-06`, `HARV-07`, `HARV-08`, `HARV-15`, `ENC-05`), the complete contribution flow (`CONTRIB-01` to `CONTRIB-10`), and traversal rejection (`SLUG-01`).
- Several local failures expose concrete compatibility or source defects. `harvest_samples.py` evaluates `int | float` inside `isinstance`, which fails under Python 3.9 despite the README claiming Python 3.8 or later. `contribute.py` has a nested-quote f-string that is a syntax error under Python 3.9. `check_pattern_coverage.py` attempts to treat an inline Python command as a path and raises `OSError: [Errno 63] File name too long`.
- The rewrite flow diagnoses before reconstruction, extracts constraints, runs scanners, and requires fresh validation. Human-eyes already takes the same general approach with a complete Audit and stricter source-bound preservation.
- The suggestion flow requires span-minimal, non-overlapping replacements that remain clean in context and pass preservation when applied together. Human-eyes already requires a fresh complete Audit of each changed context and retains the supporting artefacts.
- The voice system harvests user writing, excludes assistant turns, flags suspected contamination, derives a profile and voice card, uses held-out samples, and refuses to invent uncovered dimensions. This is more elaborate than human-eyes' current source-preservation guidance, but it also accepts any supplied style without rights or attestation checks.
- The contribution workflow starts from a wild specimen, requires a red false-negative row before implementation, adds a literal-use protection row, and asks for publication approval. This is relevant to H10's proposed false-positive intake, but the pinned contribution suite does not execute successfully in the observed environment.
- The source also defines an eight-part rewrite rubric with a 32/40 pass threshold. Its own unevaluated behavioural rows identify that the rubric can reward bland removal, erase qualified reasoning, and over-process very short text. `SKILL-RUBRIC-01` goes further by requiring a new named actor, number, or example, which conflicts with the source skill's separate instruction not to invent first-person experience, anecdotes, or unsupported certainty.
- The source is English-only. Its model-parity, behavioural, and structure-climb results are first-party reports tied to named models and dates. They were not independently reproduced in this review.

## Evidence and claims to extract

- **Direct source reviewed:** the complete 405-file tree at commit `1e50bf273d59e6d98477005ec6a086643a6b27ea`, including `README.md`, `SKILL.md`, all scanner implementations, the complete catalogue, all eval definitions and fixtures, command references, product doctrine, recorded decisions, and the pinned archive `snapshots/attachments/theclaymethod-unslop-1e50bf2.tar.gz`.
- **Method and sample:** first-party software implementation and internal evaluation artefacts. The pinned `evals/adversarial-evals.json` contains 479 script-target cases and 33 skill-target cases. The silhouette layer uses a committed reference and a reported validation set of eight human and twelve AI documents. The behavioural benchmark has 33 cases, split by the repository into tune, holdout, and holdback groups. Recorded live model comparisons are dated 2026-07-06 and 2026-07-07.
- **Direct versus cited evidence:** C01 to C12 and C14 are direct implementation, documentation, test-definition, or locally executed-suite observations from the repository. C13 records first-party model-run results that were read but not rerun. Background pattern claims inherited from Wikipedia and other sources remain indirect and cannot gain stronger evidence merely because `unslop` implements them.
- **Important limits and counterexamples:** most pattern families are not supported by independent prevalence or false-positive estimates; the silhouette corpus is small and internal; the phrase catalogue mixes candidate detection with categorical severity; genre handling is limited; the project is English-only; the README's structural-pattern and suite counts do not match the pinned implementation and eval file; the rewrite rubric conflicts with both its own behavioural safeguards and the skill's non-invention instruction; and the official deterministic suite exits unsuccessfully under the locally available Python version despite a stated Python 3.8 or later requirement.

## Matched patterns / rules

- Phrase overlap: live implementations of `no-significance-inflation`, `no-negative-parallelisms`, `no-vague-attributions`, `no-corporate-ai-speak`, `no-filler-phrases`, `no-collaborative-artifacts`, `no-knowledge-cutoff-disclaimers`, `no-generic-conclusions`, and `no-copula-avoidance` recognise representative `unslop` constructions. `no-ai-vocabulary-clustering` provides density-level overlap. `no-rhetorical-questions`, `no-promotional-language`, `no-false-concession-hedges`, and `no-compound-modifier-density` provide only partial family overlap because their thresholds or accepted forms do not cover several exact source examples.
- Surface-structure overlap is partial and definition-sensitive. Focused live-check calls on the source fixtures confirmed `sentence-length-variance` on `struct01_uniform_essay.md`, `no-staccato-sequences` on `struct07_staccato.md`, `no-anaphora` on `struct13_opener_repetition.md`, `no-superficial-ing` on `struct14_participial.md`, and general list-density coverage on `struct05_bold_listicle.md`. The similarly named `paragraph-length-uniformity`, the then-separate #10a density check (retired 2026-07-25 via DR-19G), `no-formulaic-openers`, `no-generic-conclusions`, and `no-tidy-paragraph-endings` checks did not cover the corresponding source fixtures in this focused run; `no-section-scaffolding` and `overall-signal-stacking` remain conceptually adjacent rather than equivalents.
- Manual and process overlap: `structural_monotony`, `tonal_uniformity`, `genre_specific`, and `formulaic_parallelism` in `human-eyes/scripts/judgement.json`; structure repair, source preservation, and fresh-audit requirements in `human-eyes/SKILL.md`, `human-eyes/references/process.md`, and `human-eyes/references/voice.md`.
- Distinct candidate family: no live human-eyes check directly computes `scaffold_opener_share`, `role_entropy_bits`, `preview_fulfillment`, `callback_content`, `heading_preview`, or `silhouette_penalty`.
- Severity challenge: human-eyes uses contextual severities and a non-authorship boundary. It does not support importing `unslop`'s hard or always-a-tell labels from this source alone.
- Rewrite-evaluation challenge: human-eyes has no 32/40 quality score, treats the source as a closed factual record, forbids invented specifics, and tells reports not to add a score or fixed-count checklist. This conflicts with `unslop`'s rubric and its `SKILL-RUBRIC-01` requirement for a new named actor, number, or example.

## Associated hypotheses

- H1, continuous calibrated register-distance score per pattern.
- H3, drop detection framing entirely.
- H7, five-check gating plus advisory catalogue.
- H9, similar-species disambiguation per pattern.
- H10, user-reported false-positive intake.
- H12, genre-aware threshold calibration.
- H17, calibration golden set gating grader changes.
- H20, severity calibration of agent-judgement items.
- H25, model-family versus generic-AI residue.
- Proposed follow-up: evaluate discourse-silhouette metrics as separate, interpretable candidates before considering any aggregate score or active rule.
