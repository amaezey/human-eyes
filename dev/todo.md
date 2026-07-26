# To do

Work Mae approved and queued rather than building. Every item's decision is already recorded in `dev/decision-register.md`; nothing here is a pending decision, and no new decision belongs in this file. The register stays the one decision surface.

Items 0 and 0b are Mae's own project items and were never part of the source review. Everything below them came out of it.

Each item carries enough detail to be picked up cold.

---

## 0. FIRST: rebuild the pattern numbering scheme (DR-158)

Approved 2026-07-26. Mae's own item; it was never part of the source review.

The scheme has drifted. Numbered patterns run past their own count with gaps, four sub-letter variants (23a, 31a, 35a, 35b) sit alongside plain numbers, and the aggregate meta-check `overall-signal-stacking` carries no number at all. The generated preamble's count sentence and category ranges have gone stale twice already.

**Mae's requirements:**

- no sub-letter variants
- the meta-check listed as #0
- numbers renumbered so they match the actual count
- every pattern correctly categorised
- a scheme that absorbs a new pattern without renumbering the rest — a category prefix (A1, B1) or category-major decimals (1.1)

**This is not an in-place edit.** Pattern numbers are load-bearing in `human-eyes/scripts/patterns.json`, generated `patterns.md`, the root `README.md` table, `SKILL.md`, every source card's coverage claims, `dev/decision-register.md`, and the test suite. It needs a migration plan and an old-to-new mapping table produced first.

**Two guards to check whenever a number moves**, both learned the hard way in DR-155 and DR-156: `UNCHECKED` in `test_patterns_md_generator.py`, and `_GROUP_A` in `test_grade.py`, which pins the numbers that must carry a Detection marker. Also check `_extra_entries` in `patterns.json` — manual catalogue entries carry a number and no `check_id`.

---

## 0b. Audit every check threshold against its observed distribution (DR-164)

Approved 2026-07-26. Mae's own item; also never part of the source review.

DR-79 found #52 `sentence-length-variance` had never fired on any of the 108 corpus documents, because its inherited threshold of 4 sat below the entire observed range. Its test passed the whole time, because the fixture is prose hand-written to be flat at a value real writing never reaches.

**Method:** for each check, sweep its metric over both corpora, print the observed range, and ask whether the threshold sits inside it. 11 checks carry a calibration record under `dev/evals/`; the other 43 do not, 15 of them declaring a threshold in `CHECK_THRESHOLDS` and the rest carrying bare numeric literals.

**A first smoke pass found 18 checks that never flag a generated document and 19 that flag more human documents than generated. That pass is an inventory, not a finding.** Three different causes produce those symptoms and they need opposite responses:

1. A threshold outside the observed range is a defect. That is #52.
2. A corpus holding no instance of the target is silent, not broken. DR-153's SWBST frame and DR-116's emoji rerun are both this.
3. For any check firing on one occurrence, a share-of-documents comparison is length-biased. The human corpus averages 2,172 words per document against the generated corpus's 1,051, which is exactly how #25 was misreported as running backwards during DR-66. Rate checks are immune; one-occurrence checks are not.

Separate the three before proposing anything, and bring each threshold to Mae as its own decision.

---

## 1. Fiction branch of #41 (DR-23, DR-52 to DR-58)

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

## 2. Student and academic branches of #41 (DR-41, DR-131)

Readable from the text and not currently covered:

- plot summary substituting for analysis (student branch)
- uneven quality across rubric criteria, excellent in some and poor in others (student branch)
- incorrect or awkward technical-term use (academic branch)
- data described as too clean: smooth trends, no noise, no error bars (academic branch)

**Deterministic candidate, nothing catches it today.** Belcher's four named banal theses: hero's journey, tradition versus modernity, individual versus community, boundaries destabilised. Proposed home was a one-occurrence branch of #40 `no-rubric-echoing`, whose existing rubric branch needs three occurrences.

**Not buildable.** Checking a quotation against the assigned text needs the assigned text, which the tool does not have. Twisted basic facts need the outside world. Keystroke replay is not text.

**DR-41 is close to already covered.** The student branch already says "surface polish masking weak argument", which is what its source describes.

**Carry the false-positive record into any prompt wording.** These same sources supply the sharpest such evidence in the library: teachers missed at least one of six trials 84% of the time, the trials they got wrong contained the *better* student essays, poor grammar does not indicate AI use, and a writer with dysgraphia describes AI as what let them show what they knew.

---

## 3. Journalism and #41 branch guidance (DR-27)

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

## 6. Mae's own queue items, still pending in the register

These two are *not* approved and still need her ruling. Listed here only so they are visible alongside the rest.

- **DR-164** — audit every check threshold against its observed distribution. Came out of DR-79 finding that #52 had never fired on any real document because its threshold sat below the entire observed range. Fourteen checks now carry a calibration record; the rest do not. A first smoke pass found 18 checks that never flag a generated document and 19 that flag more human documents than generated ones, but that pass is an inventory, not a finding: three different causes produce those symptoms and need opposite responses. Read DR-164's Change cell before acting on any of it.
- **DR-158** — rebuild the pattern numbering scheme. No sub-letter variants, the aggregate meta-check listed as #0, numbers matching the real count, categories corrected, and a scheme that absorbs new patterns without renumbering. Numbers are load-bearing across `patterns.json`, generated `patterns.md`, the root README table, `SKILL.md`, every source card, the register, and the tests, so it needs a migration plan and an old-to-new mapping.
