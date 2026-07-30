# Byk3y/no-slop

## Metadata

- **URL:** https://github.com/Byk3y/no-slop
- **Author / owner:** Francis / GitHub repository owner Byk3y
- **Published:** initial and reviewed commit authored and committed 2026-04-08T01:01:22Z
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** practitioner prompt-constraint repository marketed as a prose linter
- **Evidence tier:** Conduit / catalogue sources
- **Review mode:** update
- **Stable identifier:** Git commit 98cd8fb016bf5c3467e646e23d7ce09234ec0b2b
- **Version / revision:** `main` at commit `98cd8fb016bf5c3467e646e23d7ce09234ec0b2b`, root tree `43e4eb82fe0406d97cc2bc38963674463431ab5b`; the archived incomplete snapshot recorded the same commit
- **Full-text status:** complete
- **Snapshot:** `snapshots/byk3y-no-slop.md`
- **Extraction method:** full Git clone over HTTPS, full-history verification, GitHub commit and non-truncated recursive-tree API checks, commit-pinned raw-file verification, `git archive`, and byte-preserving UTF-8 concatenation of all 10 tracked files
- **Snapshot SHA-256:** `198e6d93c66e97643f31b30bb236e5d6166c7bf7f72d8c503e4ee2f04b2b6d57`
- **Model / corpus scope:** no evaluated model or corpus. A Claude Opus 4.6 co-author footer appears in the initial commit, but the repository does not present that model as a test subject. The README attributes its rules to Wikipedia editors' observations without identifying texts, model versions, dates, labels, comparison groups, or measurements.
- **Access limitations:** none for the tracked repository at the pinned commit. The full non-shallow one-commit history was cloned, all 10 tracked files and exact commit metadata were preserved, the non-truncated recursive tree and exact API and raw-file URLs were recorded, and a pinned archive was saved at `snapshots/attachments/byk3y-no-slop-98cd8fb.tar.gz`. The source itself supplies no executable linter, test suite, corpus, benchmark, scored severity system, or per-rule evidence mapping.

## Summary

Byk3y/no-slop turns categories from Wikipedia's "Signs of AI writing" into prompt constraints intended to prevent unwanted prose during drafting. The complete record contains its canonical 13-rule skill, vocabulary list, three agent-support files, contribution guidance, licence, four annotated bad examples, four matched good rewrites, and a bonus PR pair. Those materials yield 19 distinct rule families plus four workflow, evidence, rewrite-integrity, and contribution-policy claims, but no executable detector or independent evaluation. The complete examples materially weaken the source's categorical treatment: its accepted React Query rewrite contains two triads and two em dashes in one paragraph, and every displayed good rewrite adds facts absent from its paired bad passage. The source remains useful as catalogue prior art and a set of exact candidates, but it cannot establish authorship, severity, thresholds, false-positive rates, or the effectiveness and factual safety of its blanket constraints. Against the live human-eyes project, six claims are fully covered, eleven are partly covered, one is not covered, and five challenge current behaviour.

## Main insights

- C01 to C19 capture all 19 rule families in the complete canonical skill and vocabulary file. C20 to C23 capture the workflow claim, evidence and credibility claim, rewrite-integrity counterexamples, and contribution policy. The complete example files add qualifications and counterexamples to existing claims rather than a new rule family, so the stable claim count remains 23.
- Fourteen families offer an exact word, phrase, count, position, or formatting route for candidate recognition. Five depend on semantic or contextual judgement because the source does not define an executable boundary.
- The source's only explicit prose-density threshold is a maximum of one em dash per paragraph. It also treats exactly three coordinated items as prohibited, limits bolding of a term to one introduction, and allows zero emoji unless requested. None of those thresholds is evaluated.
- The source presents categorical drafting rules, not severity levels. Its four conditional vocabulary entries and positive human-writing advice are stated exceptions, while the complete examples create unacknowledged exceptions: Good Example 1 uses two concrete triads and two em dashes in one paragraph despite the categorical rules.
- The live project already represents most named families, but often with different treatment. Human-eyes uses clustering for vocabulary, candidate recognition plus contextual interpretation for triads, any-occurrence recognition with genre gates for em dashes, and minimum counts for boldface and Unicode flair.
- The fresh independent reviewer's focused deterministic rerun found exact gaps rather than merely similar names: the live copula check caught six of eight named substitutions; the vague-attribution check caught three of five supplied examples; the challenges-and-prospects example triggered neither relevant conclusion check; the source's own participle-chain example cleared `no-superficial-ing`; a plain apology-plus-speculation example cleared `no-knowledge-cutoff-disclaimers`; and all four named collaborative phrases cleared `no-collaborative-artifacts`. The same rerun confirmed that the live triad recogniser surfaces both triads in Good Example 1 and the em-dash check counts both dashes.
- The README's rewrite and all five good examples introduce factual details absent from their paired source passages. Added details include library adoption, technology history, migration implementation, retry and transport behaviour, cryptographic algorithms, request limits, cookie attributes, and a deprecation period. No citations or source brief establish those additions.
- The source's global reliance on Wikipedia remains indirect evidence. Its per-rule wording does not identify the upstream section, study, model, register, date range, or human comparison that would justify a checker, severity, or threshold change.

## Evidence and claims to extract

- **Direct source reviewed:** the complete 10-file tracked tree at commit `98cd8fb016bf5c3467e646e23d7ce09234ec0b2b`: `CONTRIBUTING.md`, `LICENSE`, `README.md`, `SKILL.md`, `agents/claude-code.md`, `agents/codex.md`, `agents/cursor.md`, `banned-vocabulary.md`, `examples/bad-examples.md`, and `examples/good-examples.md`. The root tree is `43e4eb82fe0406d97cc2bc38963674463431ab5b`.
- **Method and sample:** complete extraction and claim scan of all 27,868 source bytes. This is a rule catalogue with four annotated bad examples, four matched good rewrites, and one bonus bad/good PR pair, not an empirical sample. It provides no labelled corpus, model comparison, human baseline, prompt set, register split, text-length scope, or evaluation run.
- **Direct versus cited evidence:** C01 to C20 and C22 to C23 are direct repository statements, examples, or counterexamples. C21 records direct source assertions whose support is inherited globally from Wikipedia and remains indirect. No individual no-slop rule carries its own upstream evidence.
- **Important limits and counterexamples:** the complete repository has no executable linter despite the product description; exact activation and matching behaviour is unspecified; the canonical skill and reduced agent configurations differ; Good Example 1 violates the source's categorical triad and em-dash limits; all five good rewrites introduce unsupported details; technical, geographic, rhetorical, literary, quoted, accessibility, and house-style uses can resemble prohibited forms; and no source result supports a document-level authorship verdict or universal removal rule.
- **Focused project comparison:** the fresh independent reviewer inspected the live implementation and passed the complete preserved examples and concise enumerations directly to the relevant functions in `human-eyes/scripts/grade.py`. These are deterministic surface checks only, not a complete human-eyes Audit. Actual results are recorded claim by claim in the coverage table.

## Matched patterns / rules

- `no-ai-vocabulary-clustering`, `no-nonliteral-land-surface`, pattern B1, and H24 for high-frequency and conditional vocabulary.
- `no-copula-avoidance`, `no-promotional-language`, `no-vague-attributions`, `no-significance-inflation`, and `underspecified_language` for wording, hype, attribution, and unsupported evaluation.
- `no-forced-triads`, `formulaic_parallelism`, and `no-negative-parallelisms` for structural formulas.
- Pattern #6, `no-generic-conclusions`, and `no-signposted-conclusions` for challenges, outlook, and section-summary endings.
- `no-superficial-ing` for present-participle filler. Elegant variation matched former pattern #11, removed 2026-07-25 through DR-156.
- `no-em-dashes`, `no-collaborative-artifacts`, `context_leakage`, and `no-knowledge-cutoff-disclaimers` for punctuation and assistant residue.
- `no-boldface-overuse`, `no-unicode-flair`, manual pattern C3 title case, and `no-signposted-conclusions` for formatting.
- `sentence-length-variance`, `faux_specificity`, `tonal_uniformity`, and `genre_specific` for parts of the positive human-writing guidance.
- `human-eyes/SKILL.md`, `references/process.md`, `sources/README.md`, and the source-ingest quality gates for workflow, factual preservation, and evidence governance.

## Associated hypotheses

- H3, drop detection framing entirely.
- H7, five-check gating plus an advisory catalogue.
- H9, similar-species disambiguation per pattern.
- H11, manufactured insight is register-coded in long-form essay, including the `not just X, it's Z` construction now recognised as negative parallelism.
- H12, genre-aware threshold calibration.
- H24, register-specific vocabulary density instead of flat one-word blacklists.
