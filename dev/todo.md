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

## 0a. FIRST: rebuild the cut-off verification test so it tests the real property (DR-170)

Approved 2026-07-27, option a. Do this before 0b: DR-164 sweeps every cut-off, and it
should not be built on top of a guard that cannot fail.

### What is wrong

`dev/evals/tests/test_threshold_declarations.py` was written to catch a check
reporting one cut-off while enforcing another. `CHECK_THRESHOLDS` in
`human-eyes/scripts/grade.py` is attached to every result as `result["threshold"]`
at `grade.py:4096`, so the declared number reaches the audit report a reader sees.

The test was built on the claim that only two checks read that table and the other
seventeen carry literals. **That claim is false.** Sixteen checks read the declared
value through `threshold_value(check_id, key, default)` at `grade.py:2176`. The
original search looked for `CHECK_THRESHOLDS.get("` with a quoted check name and so
never saw the generic helper. For those sixteen the test compares the table against
itself and cannot fail.

Only three checks can genuinely diverge, and two of those are pinned in the test's
own `UNVERIFIABLE` set.

### Four holes, each proven by mutation

Reproduce these before you start; if any no longer reproduces, say so rather than
assuming the note is stale.

| mutation | current result |
|---|---|
| add a check id that does not exist to `UNVERIFIABLE` | passes |
| rename a key inside a `CHECK_THRESHOLDS` entry (e.g. `minimum_candidates` to `minimum_hits`) | that check silently drops out of verification; passes |
| add an extra key to a threshold dict | same silent drop; passes |
| move a statistic cut-off from `0.18` to `0.184` | the rounding tolerance forgives it; passes. `0.19` correctly fails |
| make a pinned check flag every document, contradicting its stated pin reason | passes, and prints the false reason as fact |

### What to build

Assert the property directly: **the declared value is the value that governs
behaviour.** For each of the 19 declared cut-offs, mutate the declared number in a
copy of the threshold table, run the check over corpus documents that sit either
side of it, and assert the flag/clear outcome moves with the declaration. A check
that ignores its declaration will not move, and that is the failure.

Constraints that make or break it:

- **Mutate a copy, never the file.** `grade.py` is loaded by import in the test;
  monkeypatch `grade.CHECK_THRESHOLDS` in memory and restore it. Never write to
  `human-eyes/scripts/grade.py` from a test.
- **Every declared key must be reached, not just the first.** The silent-drop holes
  above exist because the test keyed on a dict shape (`set(spec) == {"minimum_candidates"}`)
  and skipped anything else. Iterate the keys the table actually declares and fail
  on a key no check consumes, rather than skipping it.
- **`UNVERIFIABLE` must be validated, not trusted.** Every id in it must exist in
  `grade.ALL_CHECKS`, and its stated reason must be checked where checkable: a pin
  saying "no document flags it" must fail if a document flags it.
- **Keep the DR-79 lesson.** Where the corpus genuinely cannot straddle a cut-off,
  report it and fail if the unverifiable set grows without a reason. Silence must
  not read as agreement.
- Drop the evidence-string count fallback and the display-rounding tolerance if the
  mutation approach removes the need for them. They exist only because the current
  design reads numbers out of human-readable strings.

### Verify the test itself

A guard that cannot fail is what produced this item, so prove it fires before
trusting a pass. Re-run all five mutations in the table above and confirm each one
now fails, and confirm the suite passes unmutated. State each result.

Two checks (`no-inline-header-lists`, `no-rubric-echoing`) are pinned only because
no corpus document flags them. `test_grade.py` already proves both fire on
synthetic text, so one or two targeted samples under `dev/evals/samples/` would
unpin them. That is optional and separate; do not add samples to make a mutation
pass.

### Do not touch

`dev/evals/samples/`, `dev/evals/preserved-agent-audits-*`,
`dev/evals/three-version-*.json` and `dev/skill-workspace/skill-snapshot/` are
measurement baselines. Editing them moves what every calibration is measured
against, and the DR-158 sweep already had to revert seven such files.

### Also correct

DR-170's register row and the commit message of `7fca3c1` both state the false
premise. Correct the row when you close this; the commit message stays as history
and the row should say so.

---

## 0b. Audit every check threshold against its observed distribution (DR-164)

Approved 2026-07-26. Mae's own item; also never part of the source review.

DR-79 found G9 `sentence-length-variance` had never fired on any of the 108 corpus documents, because its inherited threshold of 4 sat below the entire observed range. Its test passed the whole time, because the fixture is prose hand-written to be flat at a value real writing never reaches.

**Method:** for each check, sweep its metric over both corpora, print the observed range, and ask whether the threshold sits inside it. 11 checks carry a calibration record under `dev/evals/`; the rest do not. Corrected 2026-07-27: 19 checks declare a cut-off in `CHECK_THRESHOLDS` and 16 of them read it through `threshold_value(check_id, key, default)` at `grade.py:2176`, so the declared value is usually the enforced one. Only three carry a literal that could diverge. Item 0a settles how that is verified; do it first.

**A first smoke pass found 18 checks that never flag a generated document and 19 that flag more human documents than generated. That pass is an inventory, not a finding.** Three different causes produce those symptoms and they need opposite responses:

1. A threshold outside the observed range is a defect. That is G9.
2. A corpus holding no instance of the target is silent, not broken. DR-153's SWBST frame and DR-116's emoji rerun are both this.
3. For any check firing on one occurrence, a share-of-documents comparison is length-biased. The human corpus averages 2,172 words per document against the generated corpus's 1,051, which is exactly how E5 was misreported as running backwards during DR-66. Rate checks are immune; one-occurrence checks are not.

Separate the three before proposing anything, and bring each threshold to Mae as its own decision.

---

## 0c. Quote evidence from the draft, not from the masked copy

Found 2026-07-27 while rebuilding the cut-off test. Mae's own item. Not yet a register row.

### What a reader sees

`21c-nyt-opinionator-i-know-what-you-think-of-me.md` contains:

> Tim Kreider is the author of "We Learn Nothing," a collection of essays and cartoons

`no-manufactured-insight` flags it and quotes it back as:

> `tim kreider is the author of                     a collection of essays`

The book title has become 21 spaces and the capitals are gone. The evidence is
the one part of an audit a writer checks against their own page, and this is not
their sentence.

### Cause

One cause, two symptoms. `_wrap_check` (`grade.py:4087`) runs lexical checks over
a masked copy: `mask_non_prose` blanks quotations, code and front matter so
patterns cannot match inside them. `_mask_non_prose_patterns` (`grade.py:927`)
overwrites those characters with spaces **in place**, so the masked copy is the
same length as the draft and every offset still lines up.

The checks then return their matches as strings cut from that masked copy.
`_candidate_records` (`grade.py:958`) receives the original text and tries to
find each string in it with `folded_text.find(value.casefold())`. For a match
that spans a masked region the string no longer exists in the draft, so:

- the quoted phrase keeps the blanks and the lowercasing, and
- the lookup fails, leaving `start` and `end` as `None`.

Some checks lowercase as well — `count_pattern_matches` (`grade.py:862`) runs
`re.findall` over `text.lower()` — so casing is lost even where nothing is masked.

### Measured over the 153 sample documents

| symptom | count |
|---|---|
| flagged phrases containing a masked hole | 66, across 7 checks |
| worst offenders | `no-curly-quotes` 37, `no-negative-parallelisms` 18, `no-anaphora` 4 |
| candidates with no locatable offset | 750+, led by `no-curly-quotes` 517 and `no-staccato-sequences` 87 |

### The fix, and why it is one place not thirty

Because masking preserves length and position, the offsets found in the masked
copy are valid offsets into the draft. So the shared wrapper can recut every
match from the original text rather than each check being taught to do it.

Two shapes, and the choice between them is the decision:

- **Recut in `_candidate_records`.** When the verbatim lookup fails, rebuild the
  search as a pattern that treats each run of two or more spaces as "anything",
  locate the span, and take `original_text[start:end]` as the phrase. Contained,
  no check signatures change, but it is a reconstruction and can mislocate a
  phrase that repeats.
- **Have checks return spans.** Checks would return `(start, end)` alongside or
  instead of strings, and the wrapper cuts from the draft. Exact, and it also
  fixes the `None` offsets properly, but it touches every lexical check.

Do not fix this check by check. `no-manufactured-insight` is the example, not the
bug.

### Before starting

`start`/`end` are currently computed and read by nothing — `_evidence_envelope`
emits `"locations": []` with the comment that location tracking is not wired
through. Decide whether this work also wires locations through or deliberately
leaves them unread, and say which.

### Verify

Re-quote all 153 documents and assert every quoted phrase appears verbatim in the
draft it came from. `test_phrase_capture_coverage.py` already asserts a version of
this and carries an allow-list for phrases that are legitimately composed
(`no-heading-one-liners` joins a heading to the line under it) plus a pin naming
this defect. Both should shrink as this lands; the pin should be removed.

---

## 0d. Decide what rate checks should quote

Found 2026-07-27, same pass. Mae's own item. Not yet a register row.

### What a reader sees

`no-it-pronoun-rate` reports a rate — 36 pronouns at 30.6 per 1000 words — and
then quotes **267 separate entries**: `"It", "it", "it", "it", …`. The finding is
the density; the list of every occurrence adds nothing to it and buries it.

Normal reports are protected by `LAYER_1_PHRASE_CAP = 3` in
`_format_quoted_phrases` (`grade.py:5350`), which shows three and appends
`(+N more)`. `--full-report` mode deliberately has no cap and renders all 267.

### Measured over the 153 sample documents

| check | longest quote list |
|---|---|
| `no-it-pronoun-rate` | 267 |
| `no-nominalisation-rate` | 185 |
| `no-passive-voice-rate` | 97 |

15 checks exceed 12 phrases on at least one document.

### The question

A rate check's evidence is the number. What should it quote — nothing, a bounded
sample, or every hit for a reader who asked for everything? The three answers give
three different products and this is a judgement about the report, not a defect
with a correct answer.

`no-ghost-spectral-density` was deduplicated on 2026-07-27 so it prints `"hidden"`
rather than `"hidden", "hidden", "hidden"`, and its true count is carried
separately in `candidate_count`. That is a precedent for one answer, not a ruling:
it was done to undo a regression introduced the same day, and was not extended to
any other check.

Whatever is chosen, `candidate_count` must keep carrying the real count — it is
read by `run_regex_catalogue_audit.py`, summed by `run_three_version_comparison.py`,
asserted across `test_regex_robustness.py`, and used by the cut-off test to check
that a declared threshold is the enforced one.

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
