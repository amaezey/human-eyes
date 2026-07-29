# To do

Work Mae approved and queued rather than building. Every item's decision is already recorded in `dev/decision-register.md`; nothing here is a pending decision, and no new decision belongs in this file. The register stays the one decision surface.

Items 0, 0a and 0b are Mae's own project items and were never part of the source review. Everything below them came out of it.

Each item carries enough detail to be picked up cold.

---

## 0. DONE: pattern numbering scheme rebuilt (DR-158)

Landed 2026-07-27. Category-letter scheme: A Content patterns, B Language and grammar, C Style, D Communication, E Filler and hedging, F Sensory and atmospheric, G Structural tells, H Voice and register, S Signal stacking. 80 entries, no gaps, no sub-letters, and a new pattern joins its category without renumbering anything.

Mae superseded her own `#0` requirement on 2026-07-27 and gave the meta-check a letter instead, so it is S1.

The old-to-new mapping and the membership rule live in `dev/pattern-renumbering-migration.md`; that file is the permanent decoder for pattern numbers in older commits.

Six defects found while doing it are queued as DR-167 to DR-172 and are Mae's to rule on. None was fixed silently.

---

## 0a. DONE: cut-off verification test rebuilt so it tests the real property (DR-170)

Landed 2026-07-27 in `16d1706`; record closed 2026-07-28. The test mutates each declared
number in an in-memory copy of `CHECK_THRESHOLDS`, re-runs the check across the
153-document corpus, and requires some document's flag/clear outcome to move with it. A
declared key nothing reads now fails rather than dropping out of verification silently.

Measuring that way found seven declared numbers no check read, across five checks rather
than the three the corrected premise recorded. All seven are wired through
`threshold_value`, so one mechanism covers all 28 declared cut-offs. One of them,
`no-staccato-sequences.minimum_repeated_opener_run`, was a structural assumption rather
than a literal; honouring it as a run length moved the evidence string on 38 corpus
documents and the match list on 13. That is a shipped-output change and is called out in
DR-170's row rather than absorbed.

Verified by mutation on 2026-07-28: the suite passes unmutated, and each of the five holes
that defeated the first version now fails it. `UNVERIFIABLE` is empty, so the original
fifth mutation has no target; its successor falsifies a `BOUNDARY_UNWITNESSED` pin, and
that fails too.

Not done, and still optional: samples under `dev/evals/samples/` that would let
`no-inline-header-lists` and `no-rubric-echoing` be witnessed by the corpus instead of
pinned. Whether each cut-off is set *well*, rather than merely wired, is 0b's question.

---

## 0b. DONE: every check threshold audited against its observed distribution (DR-164)

Landed 2026-07-28. Record: `dev/evals/threshold-distribution-audit-2026-07-28.md`.

**No threshold sits outside its observed range.** No G9 case exists outside G9. That is
the question this item asked, and it is answered.

The three causes were separated before anything was proposed:

- Cause 1, threshold outside the range: none found.
- Cause 2, corpus holds no instance: four checks. Probe documents added under
  `samples/synthetic/`, outside the calibration split.
- Cause 3, length-biased comparison: two checks, `no-boldface-overuse` and
  `no-tidy-paragraph-endings`, now measured by count and rate together.

Still open, and smaller than the question this item opened: 16 of the 19 thresholded
checks carry inherited numbers with no calibration record arguing the value. Sitting
inside the range is not the same as sitting at the right point in it.

Also open, recorded and not acted on: three checks fire on human prose and never on
generated. Whether a pattern belongs in the catalogue is a source-evidence question and
Mae's to rule on, not a threshold sweep's.

---

## 0c. DONE: quote evidence from the draft, not from the masked copy

Found 2026-07-27 while rebuilding the cut-off test. Built 2026-07-27. Mae's own
item. Not a register row.

### What the item claimed, and what was true

The item named masking as the cause: lexical checks read a copy of the draft in
which quotations and machine-readable spans are blanked to spaces, so a match
spanning one came back with a hole in it. That is real, and it is 66 of the 1,918
bad quotes across the 153 corpus documents. It is not the main cause. Measured:

| cause | count | worst offenders |
|---|---|---|
| the check lowercased its match | 1,086 | `no-it-pronoun-rate` 929, `no-manufactured-insight` 47 |
| the check joined lines or collapsed whitespace | 622 | `no-curly-quotes` 477, `no-staccato-sequences` 84 |
| the match spanned a masked span | 66 | `no-curly-quotes` 37, `no-negative-parallelisms` 18 |
| composed from two spans on purpose | 144 | `no-passive-voice-rate` 118, `no-heading-one-liners` 26 |

The 1,086 needed a second look. Most were `no-it-pronoun-rate` handing back bare
pronouns, and those strings were already the writer's own — only the offset
computed for them pointed at the wrong occurrence of the same word. Counting a
wrong offset as a wrong quote overstated the defect. The strings that genuinely
were not on the writer's page numbered 797.

The item also named the wrong place to fix it. `_evidence_envelope` builds
`quoted_phrases` from `_extract_quoted_phrases`, which reads `matches` — not
`candidates`. Recutting inside `_candidate_records`, as the item proposed, would
have corrected the candidate records and left the audit a reader sees identical.

### What was built

The first of the item's two shapes, moved to the right place.
`recut_matches_from_draft` (`grade.py:958`) sits in `_wrap_check` and rewrites
`matches` before anything reads them. A match already found in the draft is left
alone. Anything else is relocated with a pattern that ignores case, matches any
whitespace where the check left one space, and matches exactly *n* characters
where it left a run of *n* blanks — masking preserves length, so that span is
exact rather than a guess. The located text is then cut from the draft.

The second shape — teaching some thirty checks to return spans — was not built.
It is exact where this is a relocation, but it costs a differential test per
check, and it would not fix the 144 composed phrases either.

Mae's three decisions, 2026-07-27:

- **Whitespace collapses for display.** A restored quote carries the writer's
  words and capitals but not their line breaks, so a paragraph-length quote still
  renders on one line.
- **Positions are not published.** The recut works out where every quote sits,
  but nothing reads a location, so `_evidence_envelope` still emits
  `"locations": []` — now with a comment saying that is deliberate.
- **Repeated boilerplate takes the first match.** Six quotes are word-for-word
  repeats within one document, so the quote is right either way and only the
  unpublished offset could name the wrong copy.

### Result

19,962 of 20,106 quoted phrases now carry the writer's own words and capitals.
The remaining 144 are `no-passive-voice-rate` and `no-heading-one-liners`, which
compose a phrase from two spans by design and were already allow-listed.

`test_phrase_capture_coverage.py` was the gate and it was weak in two ways that
hid all of this: it lowercased both sides before comparing, and it passed a check
that produced one true quote among thirty mangled ones. It is now case-sensitive
and checks every phrase. Run against the old grader it reports 79 failures;
against the new one, none. The masked-span pin is removed.

One thing is knowingly left. Many checks build their `evidence` string inside
themselves, before the wrapper can reach the matches, so `raw["evidence"]` in the
machine contract can still read back the pre-recut text. No reader sees it — the
rendered block quotes `quoted_phrases` only — and fixing it means editing each
check, which is the shape that was not built.

## 0d. DONE: rate checks report the rate and quote nothing

Found 2026-07-27, same pass as 0c. Built 2026-07-28. Mae's own item. Not a
register row.

### What a reader saw

`no-it-pronoun-rate` counted 34 uses of `it`, worked out that this was 21.3 per
1000 words against a limit of 18, and then showed the reader:

> ⚠ It-pronoun rate: `"It", "it", "it" (+31 more)`

The rate — the whole finding — appeared nowhere. On the worst document the list
ran to 267 entries, and `--full-report` has no cap, so it rendered all 267.

### Mae's decision, 2026-07-28

Rate only, naming the word or feature being counted. The same line now reads:

> ⚠ It-pronoun rate: 34 `it` pronoun(s) at 21.3 per 1000 words (flag at 18.0)

### Scope

The six Biber and Xia feature-rate checks, patterns B7 to B12:
`no-nominalisation-rate`, `no-that-relative-rate`, `no-participial-clause-rate`,
`no-passive-voice-rate`, `no-it-pronoun-rate`, `no-latinate-verb-rate`. They share
one function, `_biber_rate_check` (`grade.py:2479`), so this is one edit.

Four other checks state a rate and were deliberately left quoting:
`no-forced-triads`, `no-staccato-sequences`, `no-negation-density` and
`no-quietness-obsession`. Their quotes are sentences or multi-word phrases a
reader can find on the page — `'medical language, social performance, and the
collapse'` — not a bare word repeated. The complaint was never list length; it was
that the list said nothing. Where it still says something it stays.

### What changed with it

- `candidate_count` still carries the true count, as the item required. It is read
  by `run_regex_catalogue_audit.py`, summed by `run_three_version_comparison.py`,
  asserted across `test_regex_robustness.py`, and used by the cut-off test.
- The six moved into `STATISTICAL_CHECKS`. They had been classed `lexical`, which
  described them until they stopped carrying phrases. That set is read nowhere but
  the wrapper, so the move is contained.
- `aggregate_finding` flips to true on 34 baseline records. The field means "this
  record has no spans", which is now the case for them.
- `no-passive-voice-rate` leaves the composed-phrase allow-list in
  `test_phrase_capture_coverage.py`. It was there because it quoted `"be ordered"`
  for "be carefully ordered", a phrase not on the writer's page; it no longer
  quotes at all. That removes 118 of the 144 quotes item 0c could not repair.
  `no-heading-one-liners` and its 26 are the only ones left.

No document changed outcome. Across the 11 pinned baselines the only fields that
moved were the evidence shape of those six checks.

---

## 1. Fiction branch of H10 (DR-23, DR-52 to DR-58)

Eight rows, seven of them the StoryScope paper, all extending `genre_specific`'s existing fiction branch in `human-eyes/scripts/judgement.json`.

| row | what a model would read the story for |
|---|---|
| DR-52 | themes and morals stated outright; dialogue carrying philosophical debate |
| DR-53 | single-track causality, absent subplots, endings that resolve inside themselves |
| DR-54 | linear time with little delayed revelation |
| DR-55 | embodied emotion, smell, setting used as a mirror for a character's state |
| DR-56 | named references, reader address, fourth-wall breaks — **inverted**, their absence is the signal |
| DR-57 | whether a story's combination of narrative features is common or rare |
| DR-58 | version-specific narrative fingerprints; the model and date must be recorded because they drift |
| DR-23 | locked tense and point of view, redemption-arc endings, both-sides conclusions |

**Two constraints to pull forward.** DR-90 and DR-91 were closed on 2026-07-26 and their caution now lives only in `russell-storyscope-ai-fiction.md`: the paper's narrative features shift substantially depending on how the text was extracted, and again by document length and topic. Anything built here inherits that.

**DR-55 and DR-56 are absence-shaped.** DR-78 declined to build an absence-based check, and Mae explicitly declined to turn that into a standing rule, so both are open on their own terms and need their own ruling before anything is built.

Present as one consolidated decision, not eight. The DR-135 precedent applies: ask separately only where the proposed product action materially differs.

---

## 2. Student and academic branches of H10 (DR-41, DR-131)

Readable from the text and not currently covered:

- plot summary substituting for analysis (student branch)
- uneven quality across rubric criteria, excellent in some and poor in others (student branch)
- incorrect or awkward technical-term use (academic branch)
- data described as too clean: smooth trends, no noise, no error bars (academic branch)

**Deterministic candidate, nothing catches it today.** Belcher's four named banal theses: hero's journey, tradition versus modernity, individual versus community, boundaries destabilised. Proposed home was a one-occurrence branch of H9 `no-rubric-echoing`, whose existing rubric branch needs three occurrences.

**Not buildable.** Checking a quotation against the assigned text needs the assigned text, which the tool does not have. Twisted basic facts need the outside world. Keystroke replay is not text.

**DR-41 is close to already covered.** The student branch already says "surface polish masking weak argument", which is what its source describes.

**Carry the false-positive record into any prompt wording.** These same sources supply the sharpest such evidence in the library: teachers missed at least one of six trials 84% of the time, the trials they got wrong contained the *better* student essays, poor grammar does not indicate AI use, and a writer with dysgraphia describes AI as what let them show what they knew.

---

## 3. Journalism and H10 branch guidance (DR-27)

Journalism provenance prompts, engagement-marker pedagogy, and craft guidance for the existing `genre_specific` branches.

The journalism branch already carries the product's only safeguard wording: "deadline prose and house style are human look-alikes, so report findings as review prompts, never accusations." That is the model for what the student and academic branches would gain under item 2.

---

## 4. Rewrite fidelity (DR-24)

The only queued agent-judgement row not tied to a genre. Two components, both readings of a rewrite against the brief that produced it:

- an explicit instruction in the brief that the rewrite ignores; the source's example is "answer without giving me a list", answered with a list
- cliché swapped for cliché rather than removed

It bears on the Rewrite action rather than on any genre. The nearest existing record is `rewrite_stance_drift` (DR-136A), which covers stance rather than instruction-following.

The row also names the ArgRewrite corpus, which its screening note treated separately.

---

## 5. Xia evaluation methodology (DR-160 to DR-163)

None of these changes the checker. They are about how this project runs its own experiments.

- **DR-160** — multiple-hypothesis correction and a null-result ledger. Every calibration so far has swept many candidate features and reported the winners; there is no record of what was measured and rejected. This is the one with immediate bite: it would have caught the phrasal-coordination and past-tense nulls being recorded only in prose.
- **DR-161** — a raw versus residue-cleaned paired evaluation lane. Whether findings hold once formulaic openings, headings and other residue are stripped from the corpora.
- **DR-162** — the detector and evaluator architecture hypothesis. Models trained on the same material rely on different features.
- **DR-163** — direction-specific generator-transfer reporting. Detectors trained on one model's output transfer poorly to another's.

---

Mae's own two items, DR-158 and DR-164, are items 0 and 0b above. Both were approved on 2026-07-26 with the instruction to build them. Nothing in this file is awaiting a ruling.
