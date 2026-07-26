# To do

Work Mae approved on 2026-07-26 and queued rather than building. Every item's decision is already recorded in `dev/decision-register.md`; nothing here is a pending decision, and no new decision belongs in this file. The register stays the one decision surface.

Each item carries enough detail to be picked up cold.

---

## 0. FIRST: screen Cheng and Yakura, and close DR-28

Both sources DR-28 was blocked on were ingested 2026-07-26. DR-28 is still `pending` in the register and is the next row to work. Nothing below this item starts until it is done.

**Cheng et al., *Science* 391, eaec8352 (2026), sycophancy.** 37 claims, `cheng-social-sycophancy.md`. The paper prints its transcripts, so the phrasing is recoverable even though sycophancy is conversational. Its AI replies open by validating the reader, praise their intentions, and end on a coaching question; the human replies give a verdict with no preamble. The ingesting agent extracted roughly forty exact forms in these families:

- validation openers — `It makes sense that you`, `It's completely understandable to`, `It sounds like you're`, `It's good that you've`, `It's natural for`, `it's reasonable to feel`
- praise of the reader — `which is commendable`, `shows your integrity`, `I commend`
- paragraph-final coaching questions — `How are you feeling`, `What have you learned`, `Have you spoken to`
- motive reframes — `Your choice was made with the intention of`, `It seems like you were considering`
- one empathy declaration — `I can hear your pain`
- denial-of-implication riders — `it doesn't mean you care about her any less`

Plus one agent-judgement candidate the paper measures directly (P < 0.001): whether an advice reply engages the other party's perspective or only the reader's account.

**Two bounds on all of it.** The paper's own *non-sycophantic* condition uses the same opener family, so these forms mark AI advice register rather than sycophancy. And the paper publishes no phrase list, count, or frequency for anything it quotes.

**Yakura et al., arXiv 2409.01754v4, vocabulary.** 30 claims, `yakura-llm-influence-spoken-communication.md`. Its word list is already ruled and shipped through DR-165, which added 26 words to #7. What remains unruled on that card is everything except C01 and C03.

**Nothing on either card has been verified against the live checker by the main session.** Both agents' reports were relayed untested. The Yakura word list was tested afterwards and 16 of 27 words turned out to appear in neither corpus. Test before presenting.

**The corpora cannot settle the Cheng forms.** They hold no chat replies at all, so a zero here means silent, not absent — the same situation already recorded for technical writing in `dev/decision-walkthrough-approach.md`.

**Two further ingests are named and not queued.** The Cheng supplementary materials hold the LLM-judge rubric that defines affirmation operationally (Science returned 403), and the Dryad deposit holds the generated responses, which would give the project the advice-reply corpus it currently lacks.

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
