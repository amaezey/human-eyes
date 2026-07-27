# Pattern renumbering migration (DR-158)

The mapping and order of work for DR-158. Approved 2026-07-26; scheme, membership rule, and the
disposition of the uncatalogued detectors settled by Mae on 2026-07-27. Landed the same day; see
Outcome at the end.

## The scheme

A category letter followed by a position within that category. `A1`, `B14`, `H17`. The eight existing
categories keep their names and order, and Signal stacking becomes a ninth:

| letter | category | members |
|---|---|---|
| A | Content patterns | 7 |
| B | Language and grammar | 14 |
| C | Style | 9 |
| D | Communication | 6 |
| E | Filler and hedging | 9 |
| F | Sensory and atmospheric | 3 |
| G | Structural tells | 13 |
| H | Voice and register | 17 |
| S | Signal stacking | 1 |

The aggregate meta-check is `S1` in its own Signal stacking category. Mae superseded her earlier `#0`
requirement on 2026-07-27: a letter leaves the scheme with no special form for any parser, generator,
or test to carry.

A new pattern joins its category at the next free position and renumbers nothing. The letter forms
also make migration self-checking: a surviving `#47` anywhere in the repository is visibly an
old-scheme reference, where a surviving `1.12` under a decimal scheme would still have read as
plausible.

## The membership rule

**Every detector that fires on a single text gets a number and a catalogue entry.** That covers
programmatic checks in `grade.py` and agent-judgement records in `judgement.json` alike, and it does
not matter whether the finding quotes a span: `G9` (old #52) and `B12` (old #71) are draft-wide
statistics and are catalogue members.

One exception, and the rule states it rather than leaving it as a gap: `rewrite_stance_drift` reads a
rewrite against the source that produced it. Two texts are required, so there is no draft-level
before/after to show, and it stays a registered record with no number.

Before this rule the catalogue had no stated membership test, and five things had accumulated in the
space that left. The programmatic side was already consistent — 66 checks in `grade.py`, 66 entries
in `patterns.json`, exact in both directions. Every discrepancy was on the agent side, where the 20
records were getting three different treatments with no decision behind any of them.

## Counts

| | before | after |
|---|---|---|
| numbered catalogue entries | 72 | 79 |
| unnumbered aggregate | 1 (`overall-signal-stacking`) | 0; it is `S1` |
| gaps in the sequence | 5 (6, 11, 54, 55, 61) | none possible |
| sub-letter variants | 4 (23a, 31a, 35a, 35b) | none |
| numbered but absent from `patterns.md` | 3 (54, 55, 61) | none |
| live detectors with no number | 5 | 1, by stated exception |
| README table rows vs `patterns.md` entries | 75 vs 72 | 79 vs 79 |

Seven entries are new to the catalogue. Four already had a number somewhere and were missing their
entry; three had no number at all. Each is marked in the mapping below.

## Mapping

### Content patterns

| new | old | pattern | lane | check or record | note |
|---|---|---|---|---|---|
| `A1` | 1 | Significance inflation | programmatic | `no-significance-inflation` |  |
| `A2` | 2 | Notability claims | programmatic | `no-notability-claims` |  |
| `A3` | 3 | Superficial -ing analyses | programmatic | `no-superficial-ing` |  |
| `A4` | 4 | Promotional language | programmatic | `no-promotional-language` |  |
| `A5` | 5 | Vague attributions | programmatic | `no-vague-attributions` |  |
| `A6` | 12 | False ranges | programmatic | `no-false-ranges` |  |
| `A7` | — | Internal consistency | agent judgement | `internal_consistency` | judgement record, no number anywhere |

### Language and grammar

| new | old | pattern | lane | check or record | note |
|---|---|---|---|---|---|
| `B1` | 7 | AI vocabulary words | programmatic | `no-ai-vocabulary-clustering` |  |
| `B2` | 8 | Copula avoidance | programmatic | `no-copula-avoidance` |  |
| `B3` | 9 | Negative parallelism | programmatic | `no-negative-parallelisms` |  |
| `B4` | 10 | Rule of three | programmatic | `no-forced-triads` |  |
| `B5` | 53 | Vocabulary diversity | programmatic | `vocabulary-diversity` |  |
| `B6` | 64 | Mixed spelling conventions | programmatic | `no-mixed-spelling-conventions` |  |
| `B7` | 65 | Nominalisation rate | programmatic | `no-nominalisation-rate` |  |
| `B8` | 66 | Subject `that` relative rate | programmatic | `no-that-relative-rate` |  |
| `B9` | 67 | Present participial clause rate | programmatic | `no-participial-clause-rate` |  |
| `B10` | 68 | Passive voice rate | programmatic | `no-passive-voice-rate` |  |
| `B11` | 69 | `it` pronoun rate | programmatic | `no-it-pronoun-rate` |  |
| `B12` | 70 | Latinate verb rate | programmatic | `no-latinate-verb-rate` |  |
| `B13` | 71 | Word length average | programmatic | `word-length-average` |  |
| `B14` | 73 | Concreteness average | programmatic | `concreteness-average` |  |

### Style

| new | old | pattern | lane | check or record | note |
|---|---|---|---|---|---|
| `C1` | 13 | Boldface overuse | programmatic | `no-boldface-overuse` |  |
| `C2` | 14 | Inline-header lists | programmatic | `no-inline-header-lists` |  |
| `C3` | 15 | Title case in headings | programmatic | `no-title-case-headings` |  |
| `C4` | 16 | Emojis | folded | `no-unicode-flair` |  |
| `C5` | 17 | Curly quotation marks | programmatic | `no-curly-quotes` |  |
| `C6` | 18 | Hyphenated compound modifier overuse | programmatic | `no-compound-modifier-density` |  |
| `C7` | 49 | Em dashes | programmatic | `no-em-dashes` |  |
| `C8` | 57 | Parenthetical headings | programmatic | `no-parenthetical-headings` |  |
| `C9` | 72 | Mixed-script words | programmatic | `no-mixed-script-words` |  |

### Communication

| new | old | pattern | lane | check or record | note |
|---|---|---|---|---|---|
| `D1` | 19 | Collaborative artifacts | programmatic | `no-collaborative-artifacts` |  |
| `D2` | 20 | Knowledge-cutoff disclaimers | programmatic | `no-knowledge-cutoff-disclaimers` |  |
| `D3` | 21 | Sycophantic/servile tone | folded | `no-collaborative-artifacts` |  |
| `D4` | 62 | Formulaic social-post frames | programmatic | `no-formulaic-social-posts` |  |
| `D5` | 61 | Unprompted caveats | agent judgement | `unprompted_caveats` | README row + judgement record, no catalogue entry |
| `D6` | — | Audience knowledge mismatch | agent judgement | `audience_knowledge_mismatch` | judgement record, no number anywhere |

### Filler and hedging

| new | old | pattern | lane | check or record | note |
|---|---|---|---|---|---|
| `E1` | 22 | Filler phrases | programmatic | `no-filler-phrases` |  |
| `E2` | 23 | Excessive hedging | programmatic | `no-excessive-hedging` |  |
| `E3` | 23a | False concession hedges | programmatic | `no-false-concession-hedges` |  |
| `E4` | 24 | Generic positive conclusions | programmatic | `no-generic-conclusions` |  |
| `E5` | 25 | Staccato rhythm in extended contexts | programmatic | `no-staccato-sequences` |  |
| `E6` | 47 | Soft scaffolding | programmatic | `no-soft-scaffolding` |  |
| `E7` | 48 | Dense negation | programmatic | `no-negation-density` |  |
| `E8` | 50 | Formulaic openers | programmatic | `no-formulaic-openers` |  |
| `E9` | 60 | Modal qualifier stacks | programmatic | `no-modal-stacks` |  |

### Sensory and atmospheric

| new | old | pattern | lane | check or record | note |
|---|---|---|---|---|---|
| `F1` | 26 | Ghost/spectral language | programmatic | `no-ghost-spectral-density` |  |
| `F2` | 27 | Quietness obsession | programmatic | `no-quietness-obsession` |  |
| `F3` | 28 | Forced synesthesia | agent judgement | `None` |  |

### Structural tells

| new | old | pattern | lane | check or record | note |
|---|---|---|---|---|---|
| `G1` | 29 | Mid-sentence rhetorical questions | programmatic | `no-rhetorical-questions` |  |
| `G2` | 30 | Generic/ungrounded metaphors | agent judgement | `None` |  |
| `G3` | 31 | Excessive list-making | programmatic | `no-excessive-lists` |  |
| `G4` | 31a | Unicode flair | programmatic | `no-unicode-flair` |  |
| `G5` | 32 | Dramatic narrative transitions | programmatic | `no-dramatic-transitions` |  |
| `G6` | 38 | Section scaffolding | programmatic | `no-section-scaffolding` |  |
| `G7` | 42 | Manufactured insight framing | programmatic | `no-manufactured-insight` |  |
| `G8` | 44 | Signposted conclusions | programmatic | `no-signposted-conclusions` |  |
| `G9` | 52 | Sentence length variance | programmatic | `sentence-length-variance` |  |
| `G10` | 59 | One-line sections under headings | programmatic | `no-heading-one-liners` |  |
| `G11` | 63 | Symmetric list items | programmatic | `no-symmetric-list-items` |  |
| `G12` | — | Paragraph length uniformity | programmatic | `paragraph-length-uniformity` | live check, no number |
| `G13` | 54 | Structural monotony | agent judgement | `structural_monotony` | README row + judgement record, no catalogue entry |

### Voice and register

| new | old | pattern | lane | check or record | note |
|---|---|---|---|---|---|
| `H1` | 33 | Countdown negation | programmatic | `no-countdown-negation` |  |
| `H2` | 34 | Per-paragraph miniature conclusions | programmatic | `no-tidy-paragraph-endings` |  |
| `H3` | 35 | Tonal uniformity / register lock | agent judgement | `None` |  |
| `H4` | 35a | Orphaned demonstratives | programmatic | `no-orphaned-demonstratives` |  |
| `H5` | 35b | Repeated 'This …' chains | programmatic | `no-this-chains` |  |
| `H6` | 36 | Faux specificity | agent judgement | `None` |  |
| `H7` | 37 | Neutrality collapse | agent judgement | `None` |  |
| `H8` | 39 | Template and placeholder residue | programmatic | `no-placeholder-residue` |  |
| `H9` | 40 | Rubric echoing | programmatic | `no-rubric-echoing` |  |
| `H10` | 41 | Genre-specific manual checks | agent judgement | `None` |  |
| `H11` | 43 | Corporate AI-speak | programmatic | `no-corporate-ai-speak` |  |
| `H12` | 45 | Nonliteral land/surface phrasing | programmatic | `no-nonliteral-land-surface` |  |
| `H13` | 46 | Bland critical template | programmatic | `no-bland-critical-template` |  |
| `H14` | 51 | Mechanical repeated sentence starts | programmatic | `no-anaphora` |  |
| `H15` | 56 | Performed candour and vulnerability | programmatic | `no-performed-candour` |  |
| `H16` | 58 | Mechanical repeated paragraph starts | programmatic | `no-paragraph-anaphora` |  |
| `H17` | — | Change narration | agent judgement | `change_narration` | judgement record, no number anywhere |
| — | 55 | Even jargon distribution | retired | — | briefly B15, then H18; **retired 2026-07-27 under DR-168** because the level checks already cover it. See `dev/evals/jargon-evenness-measurement-2026-07-27.md` |

### Signal stacking

| new | old | pattern | lane | check or record | note |
|---|---|---|---|---|---|
| `S1` | — | Signal stacking from stacked AI tells | programmatic | `overall-signal-stacking` | aggregate meta-check; Mae ruled #0 |

## Order of work

Each step verifies before the next begins.

1. **Land the rule and the mapping.** This file, plus the DR-158 register row corrected. Its Change
   cell currently names `SKILL.md` as carrying pattern numbers, which it does not — there is no
   `#NN`, no `pattern N`, no numeric reference of any kind in its 137 lines. The same cell's counts
   predate #65 to #73. Verify: no product file touched.

2. **Author the seven new catalogue entries.** `A7`, `H18` (since retired), `D5`, `D6`, `G12`, `G13`, `H17`. Each
   needs the same shape every other entry carries, including a before/after. This is reader-facing
   prose and the only step in the migration that writes new product copy. Verify: the seven render,
   and `patterns.md` reaches 79 entries plus `#0`.

3. **Derive the preamble count and the TOC ranges from the data.** Both are free-text blobs in
   `_meta` today and no test asserts either, which is why they have gone stale twice and are stale
   now: the preamble claims 62 patterns, and five of the nine TOC ranges omit members
   (`Language and grammar` is missing 68 to 71 and 73, `Style` 72, `Filler and hedging` 60,
   `Structural tells` 59 and 63, `Voice and register` 58). Under the letter scheme a range is just
   the category letter and its count, so both become generated. Verify: a new generator test fails
   when a pattern is added without the preamble following.

4. **Renumber `patterns.json`.** `pattern_number` on each entry and each `_extra_entries` member.
   `pattern_ref` in `judgement.json` remaps to whatever its current target is, unchanged in meaning
   (see the open item below). Verify: the generator reproduces `patterns.md` byte-for-byte apart from
   the intended number changes.

5. **Fix the two test parsers.** `_GROUP_A` in `test_grade.py:1717` is a list of bare integers and
   its heading parser is `^### (\d+)([a-z])?\.\s`, which matches no letter-prefixed heading; left
   alone it silently finds nothing and fails every Group A pattern. `UNCHECKED` in
   `test_patterns_md_generator.py:60` keys extras by number but is an empty set, so it survives the
   change as long as it stays empty. Verify: both tests fail before the parser fix and pass after.

6. **Delete `JUDGEMENT_REF_FALLBACK`.** The renderer map at `dev/tools/render_patterns_md.py:263`
   exists only because 54, 55 and 61 had no `patterns.json` entry. Once step 2 gives them one, the
   reference lives in `judgement.json` and the map is dead. Verify: removed, and the three entries
   still render their Detection lines.

7. **Sweep the reference surfaces**, largest last so a mistake is caught while the blast radius is
   small: `grade.py` (3), `judgement.json` (1), README table (79 rows), `docs/` (202),
   `dev/evals` (298), `hypotheses.md` (28), the register (366), the walkthrough (195), and
   `dev/references/sources/` (4,409 across 99 cards). Verify after each: no bare `#NN` pattern
   reference survives outside a quoted historical decision, and `validate_source.py` passes on every
   card.

8. **Full gate.** Every test file as its own script per `dev/TESTING.md`, the generated-pattern
   check, `validate_source.py`, and `reconcile_register.py` at zero.

## Constraints carried in

- `reconcile_register.py` matches a character class that excludes `/`, and `validate_source.py`
  asserts the literal `(card-basename.md)` appears in the sources README. Neither reads pattern
  numbers, so neither constrains this work, but both gate the card sweep in step 7.
- Source cards state a snapshot SHA-256 that `validate_source.py` enforces. Editing a snapshot means
  updating its declared hash. Snapshots are quoted source material and hold no pattern numbers of
  this project's own, so step 7 must not touch them.

## Open item, needs its own row

`pattern_ref` is inert for six of the thirteen records that carry one. `derive_detection` returns at
the programmatic branch first, so a ref pointing at a pattern whose check already owns the Detection
line is never read: `formulaic_parallelism` (10), `semantic_redundancy` (34),
`underspecified_language` (43), `context_leakage` (19), `performed_candour` (42),
`vacuous_connection` (22). The other seven point at entries with no programmatic check and are read.

One of the inert six is wrong on its face. `performed_candour` points at old #42 Manufactured insight
framing, while old #56 Performed candour and vulnerability is the pattern that names it and whose own
Detection prose cites the record. Nothing renders incorrectly today because the ref is never read.

Step 4 remaps all thirteen refs mechanically, preserving each target exactly, including that one.
Correcting `pattern_ref` semantics changes what the registry asserts and belongs to its own decision,
not to a renumbering.

## Outcome, 2026-07-27

Landed. 80 entries, 5,453 references rewritten across 131 tracked files, full test loop green, `render_patterns_md.py --check` clean, `reconcile_register.py` at 0, every source card still passing `validate_source.py` apart from the four non-cards and two documented exceptions that already failed.

### Sweep false positives, found in review

Three classes of `#N` are not pattern references, and the deny-list missed two of
them. Anyone repeating a sweep needs all three:

- **`#N` meaning "number one".** `NY Times #1 best sellers` became `NY Times A1
  best sellers` in the human corpus. The guard tested for `ranked #` and correctly
  found none, because the phrasing here is `Times #1`. Testing for the wrong
  phrasing and reading the zero as safety is the failure, not the missing word.
- **Markdown anchor links.** `[Introduction](#1)` became `[Introduction](A1)`,
  breaking five links in one corpus sample.
- **`PR #N`, `Finding #N`, `survivor #N`.** These the deny-list did catch.

**Corpus samples, preserved agent audits and comparison artifacts are measurement
data, not documentation, and must never be swept.** `dev/evals/samples/`,
`dev/evals/preserved-agent-audits-*` and `dev/evals/three-version-*.json` were
reverted for that reason, the same reason `dev/skill-workspace/skill-snapshot/`
was excluded. Editing them changes the baseline every calibration is measured
against. The DR-168 measurement was re-run on the restored files and returned
identical figures, so nothing recorded there depended on the corruption.

Left as old labels on purpose: retired 6, 11 and 10a, which have no new id; `PR #N`, `Finding #N` and `survivor #N`, which are not pattern references; `#3382`, a GitHub issue; and a hex colour in `render_audit_html.py`. `docs/` is gitignored and untracked, so its `PR #5` and `survivor #2` references were never in scope.

Six defects surfaced and were queued rather than fixed: DR-167 (`performed_candour` points at the wrong entry; six refs inert), DR-168 (H18's SAGE citation unsupported; H18 since retired after measurement), DR-169 (`audience_knowledge_mismatch` shipped with no row, against a claim that runs the opposite way), DR-170 (`paragraph-length-uniformity` declares thresholds it never reads, and has no calibration record), DR-171 (H2's SAGE citation unsupported; the sources index is complete apart from one deliberate retirement tombstone, correcting an unverified 19-card claim), DR-172 (H18's category, and two categories with no preamble).
