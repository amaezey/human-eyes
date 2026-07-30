# New AI corpus deterministic false-negative review

Date: 2026-07-13

## Scope and decision meanings

This review covers the ten AI documents in `dev/evals/samples/pilot-additions-01/generated-ai/` against the current deterministic catalogue. The source of recorded checker decisions is `dev/evals/three-version-pilot-additions-comparison.json`.

Each proposed exception to a checker `clear` result is classified as:

- **Miss:** the document contains a construction that the check says it recognises, but no candidate was reported.
- **Suppressed:** a candidate exists, but a document-level threshold prevented a finding.
- **Evidence gap:** the construction may have been inspected internally, but the clear result does not expose enough evidence to verify that decision.
- **Catalogue gap:** the prose exhibits the documented tendency, but the implemented vocabulary or grammar covers only a narrower form.
- **Contextual control:** the form is present but is not clearly a misuse in this document.

The corpus text was never altered. Checker changes described as approved below were implemented only after the candidate review and explicit boundary decisions; thresholds changed only where stated.

## Corpus-wide result

Before this improvement pass, the recovered checker recorded 28 findings across the ten AI documents. Direct review found four high-confidence false-negative families:

1. Clause-form and prepositional triads in AI-03 are not recognised.
2. List-heavy AI-04 remains clear because list density uses bullet lines divided by all physical lines.
3. Product-release promotional claims in AI-07 fall outside the tourism-oriented promotional lexicon.
4. Clear results hide sub-threshold candidates, preventing recognition failures from being distinguished from threshold decisions.

The approved fixes now produce 36 AI findings while human findings remain 34. Candidate-only recognition also improved without forcing every candidate across a document threshold.

## Decision review by document

### AI-01: personal reflective open letter

Recorded findings: anaphora, curly quotes, negative parallelism, individual triads, and triad density.

| Clear check reviewed | Passage or evidence | Proposed decision |
|---|---|---|
| `no-rhetorical-questions` | `Should I not simply be thankful?` followed by `But gratitude and criticism are not opposites.` | **Miss plus suppression.** The recogniser excludes answers beginning with `But`, and the check requires two candidates. The candidate should be exposed even if the document stays below threshold. |
| `no-tidy-paragraph-endings` | Existing checker candidate: `That is why I cannot stay quiet about the way some of our neighbours are being treated.` | **Suppressed.** One candidate is recorded; threshold is three. Current final status is internally consistent but the comparison report should expose the candidate. |
| `no-manufactured-insight` | `That small experience corrected something in me.` | **Possible catalogue gap.** It announces an insight, but the following explanation is specific. Proposed contextual control unless the check is intended to surface every explicit revelation frame. |
| `no-excessive-lists` | Six consecutive imperative recommendations occur as prose rather than Markdown bullets. | **Contextual control.** This is enumerative rhetoric, not list formatting under the current check definition. |
| Remaining clear checks | No independent construction matching their current documented deterministic definitions was found. | **No proposed change.** |

### AI-02: technology memoir

Recorded findings: individual triads, triad density, and paragraph-length uniformity.

| Clear check reviewed | Passage or evidence | Proposed decision |
|---|---|---|
| `no-nonliteral-land-surface` | `as if it were a map out of the wilderness` | **Possible catalogue gap.** This is a nonliteral terrain metaphor, but not the catalogue's common `navigate the landscape/terrain` template. Requires a boundary decision. |
| `no-manufactured-insight` | `It taught me that not knowing was not a verdict. It was simply the first stage of finding out.` | **Possible catalogue gap.** The polished lesson structure fits the tendency more closely than the current phrase list recognises. |
| `no-tidy-paragraph-endings` | Several paragraphs end in self-contained reflective resolutions, including the final two sentences. | **Evidence gap.** The clear output reports zero candidates; the lexical ending templates are too narrow to evaluate this form. |
| Remaining clear checks | No independent construction matching their current documented deterministic definitions was found. | **No proposed change.** |

### AI-03: personal newsletter

Recorded findings: none.

| Clear check reviewed | Passage or evidence | Proposed decision |
|---|---|---|
| `no-forced-triads` | `travel less often, stay longer when we do, and use trains where they are practical` | **Miss.** Three coordinated verb phrases. |
| `no-forced-triads` | `for our relatives, for our budget, and for a climate that every future family gathering will depend on` | **Miss.** Three coordinated prepositional phrases. |
| `no-triad-density` | Depends on the two missed candidates; the document is also below the current four-candidate density threshold. | **Suppressed, not a density finding.** Candidate count should be two after recognition is fixed. |
| `no-negative-parallelisms` | `Our annual trip was more than a habit; it was proof...` | **Contextual control.** It is a direct elaboration, not the targeted `not X but Y` reframe. |
| Remaining clear checks | No independent construction matching their current documented deterministic definitions was found. | **No proposed change.** |

### AI-04: professional programme email

Recorded findings: individual triads and triad density.

| Clear check reviewed | Passage or evidence | Proposed decision |
|---|---|---|
| `no-excessive-lists` | Five programme bullets followed by five numbered feedback questions. | **Threshold-design false negative.** Ten list items do not reach 30% of all physical lines because blank and prose lines inflate the denominator. The check should report blocks and item counts before applying a contextual threshold. |
| `no-inline-header-lists` | `participants will have:` and `following questions:` introduce two genuine lists. | **Contextual control.** These are list introductions, not inline faux headings under the current definition. |
| `no-promotional-language` | `essential help`, `more reliable approach`, `useful in practice`, `generous with both their time and expertise` | **Possible catalogue gap, likely contextual control.** Positive institutional language is present, but it is not strong product/tourism hype. |
| Remaining clear checks | No independent construction matching their current documented deterministic definitions was found. | **No proposed change.** |

### AI-05: workplace standards update

Recorded findings: curly quotes and an individual triad.

| Clear check reviewed | Passage or evidence | Proposed decision |
|---|---|---|
| `no-excessive-lists` | Four-item decision list. | **Suppressed/contextual control.** The list is real and operationally justified. It should be recognised as a list block without necessarily producing a misuse finding. |
| `no-triad-density` | Existing candidate is the subject-line triad `progress, open issues, and August decisions`; document is 250 words and below the 300-word density floor. | **Suppressed.** No density finding is warranted under the current threshold, but the reason must remain visible. |
| `no-corporate-ai-speak` | Standards-project terminology such as `aligned`, `implementation partners`, and `external review`. | **Contextual control.** Domain-specific and tied to concrete work rather than the targeted vague corporate clichés. |
| Remaining clear checks | No independent construction matching their current documented deterministic definitions was found. | **No proposed change.** |

### AI-06: business strategy report

Recorded findings: individual triads and triad density.

| Clear check reviewed | Passage or evidence | Proposed decision |
|---|---|---|
| `no-soft-scaffolding` / `no-formulaic-openers` | Paragraphs begin `A major priority...`, `The body also considered...`, `Another area of work...`, `Regional participation remained...`, `Throughout the year...`, and `In 2019–20...`. | **Catalogue gap.** Repeated balanced report scaffolding is present, but current patterns recognise only a small fixed phrase set. Whether to expand deterministic coverage requires legitimate report controls. |
| `paragraph-length-uniformity` | Seven similarly shaped report paragraphs. | **Needs measured review.** The current coefficient-of-variation threshold clears it; visual similarity alone is not enough to override the metric. Preserve as clear unless the paragraph metric itself is redesigned. |
| `no-significance-inflation` | `A major priority`, `important theme`, and `significant strengths`. | **Contextual control.** The report supplies the substantive priority or strengths; these are not automatically unsupported historical inflation. |
| Remaining clear checks | No independent construction matching their current documented deterministic definitions was found. | **No proposed change.** |

### AI-07: browser release announcement

Recorded finding: an individual triad. Two triad candidates remain below density threshold.

| Clear check reviewed | Passage or evidence | Proposed decision |
|---|---|---|
| `no-promotional-language` | `faster and more responsive`, `quicker page loading`, `uses memory more efficiently`, `becomes usable sooner`, `produce smoother scrolling`, and `the benefit should be apparent`. | **Catalogue false negative.** This is product-release promotional language, while the current lexicon is dominated by tourism and generic superlatives. Claims with concrete measurements would be legitimate controls; this text mostly provides no figures. |
| `no-triad-density` | Existing candidates: `JavaScript execution, graphics rendering and network request scheduling`; `opening the browser menu, selecting Help, and choosing About`. | **Suppressed.** Two candidates are below the four-candidate threshold. |
| `no-vague-attributions` | `In our testing` without linked results. | **Contextual control under the current attribution definition.** It is first-party attribution, not an unnamed appeal to experts or studies. Unsupported specificity belongs to agent assessment. |
| `no-generic-conclusions` | Closing thanks and promise of continued work. | **Contextual control.** Genre-appropriate release-note close; not one of the generic positive future templates. |
| Remaining clear checks | No independent construction matching their current documented deterministic definitions was found. | **No proposed change.** |

### AI-08: student autoethnographic essay

Recorded findings: em dashes, curly quotes, negative parallelism, individual triads, and triad density.

| Clear check reviewed | Passage or evidence | Proposed decision |
|---|---|---|
| `no-rubric-echoing` | `Writing autoethnographically requires me to connect these memories to a wider structure...` | **Possible catalogue gap.** This sounds like assignment-language mirroring, but a single sentence cannot establish rubric echo without the source brief. Preserve as unresolved unless the prompt contains matching terminology. |
| `no-false-concession-hedges` | `Yet I do not want to turn this account into a simple story of deprivation or resilience.` | **Contextual control.** The paragraph makes and supports a specific qualification rather than landing in an empty middle. |
| `no-manufactured-insight` | `This concealment complicates the university’s promise of equal opportunity.` | **Contextual control.** Direct claim followed by concrete mechanisms. |
| Remaining clear checks | No independent construction matching their current documented deterministic definitions was found. | **No proposed change.** |

### AI-09: literary criticism

Recorded findings: curly quotes, negative parallelism, copula avoidance, individual triads, and triad density.

| Clear check reviewed | Passage or evidence | Proposed decision |
|---|---|---|
| `no-false-concession-hedges` | `This transformation should not be dismissed as mere distortion.` | **Contextual control.** The following sentences name concrete artistic consequences; it is substantive qualification rather than fake balance. |
| `no-bland-critical-template` | Repeated balanced critical structure: selection, alteration, feedback, concession, synthesis. | **Possible catalogue gap.** The document exhibits the broader template described by the rule, but current deterministic phrases do not capture discourse structure. No deterministic expansion has been approved. |
| `no-tidy-paragraph-endings` | Paragraphs repeatedly close with polished mini-theses such as `The selection was already an interpretation.` | **Approved and implemented as candidate recognition.** The check now recognises compact abstract-interpretation closures and balanced semicolon closures with two independent clauses. Literal states and subordinate fragments are controls; quoted occurrences remain candidates with quoted metadata. The existing three-ending document threshold is unchanged. AI-09 exposes two candidates but remains document-level clear. |
| Remaining clear checks | No independent construction matching their current documented deterministic definitions was found. | **No proposed change.** |

### AI-10: government report

Recorded findings: curly quotes, individual triads, and triad density.

| Clear check reviewed | Passage or evidence | Proposed decision |
|---|---|---|
| `no-significance-inflation` | `They also underline the value of regular primary-care relationships.` | **Approved and implemented.** The deterministic family now recognises `underline`, `underscore`, `highlight`, and British/American `emphasise` variants followed by `the importance/value/significance of`. Literal uses such as underlining or highlighting text remain controls. This adds one AI candidate in the fresh corpus and no new human or established-corpus candidates. |
| `no-generic-conclusions` | `The findings support continued work... Future survey cycles will...` | **Contextual control.** Standard report recommendation and monitoring statement, not an empty upbeat ending. |
| `no-vague-attributions` | `Some respondents`, `a proportion of patients`, and `survey responses`. | **Contextual control.** The survey is the named evidence source; these are population descriptions rather than vague appeals to authority. |
| `no-excessive-hedging` | `may increase`, `were more likely`, `warrant further investigation`, and explicit survey limitations. | **Contextual control.** Appropriate epistemic qualification for survey evidence. |
| Remaining clear checks | No independent construction matching their current documented deterministic definitions was found. | **No proposed change.** |

## Approved classifications and remaining controls

### High-confidence bugs implemented

1. Recognise both missed AI-03 triads.
2. Replace or supplement list-line ratio with list-block and item-count evidence; do not automatically call every operational list a misuse.
3. Add product-release promotional candidates represented by AI-07, with factual/quantified controls.
4. Expose recognised candidates even when a document remains below a density threshold.

### Boundary decisions

1. **Approved and implemented:** informational subjects framed as maps, compasses, or roadmaps through figurative terrain, including `map out of the wilderness`; literal geographic navigation remains a control.
2. **Approved and implemented:** explicit polished lesson constructions such as `It taught me that...`; concrete instruction such as learning how to replace a battery remains a control.
3. **Approved and implemented:** repeated report paragraph scaffolding, with a two-candidate document threshold and mid-sentence controls.
4. **Approved and implemented:** `underline the value` joins significance-inflation candidates through a general grammatical family with literal-use controls.
5. **Approved and implemented:** recognise compact abstract-interpretation and balanced-semicolon closures as candidates while retaining the existing three-ending document threshold.

## Current conclusion

The original AI total of 28 was understated. The approved high-confidence fixes raised it to 31: AI-03 triad recognition, AI-04 list thresholding, and AI-07 product-promotion recognition each added one document-level finding. The approved boundary families then added five more findings: one nonliteral-terrain finding on AI-02; a manufactured-insight finding plus the related signal-stacking threshold on AI-02; one report-scaffolding finding on AI-06; and one significance-emphasis finding on AI-10. Tidy critical closures add four visible candidates across three AI documents but no document-level finding because the existing three-ending threshold remains in place.

The final deterministic result is human 34 / AI 36, mean pair gap +0.2. This does not make aggregate detection the objective or turn findings into authorship accusations. It shows that candidate-level false-negative review found reusable grammatical and structural gaps, improved AI-side recognition without increasing fresh-corpus human findings, and preserved threshold/context distinctions.
