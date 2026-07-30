# Aranya / Poetly: Poetry and Artificial Intelligence

## Metadata

- **URL:** https://poetly.substack.com/p/poetry-and-artificial-intelligence
- **Author / owner:** Aranya, as recorded by the existing source catalogue; the preserved extraction does not display a byline
- **Published:** 2025-07-16
- **Retrieved:** 2026-05-05
- **Extracted:** 2026-05-05
- **Source type:** practitioner poetry commentary
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** public Substack post as preserved 2026-05-05; published timestamp `2025-07-16T14:35:15+00:00`; prior raw capture SHA-256 `d6324f0bde6676d6f4b483d072bb390066eeff1d198c7d499e14d5d2d3da8e2c`
- **Full-text status:** partial
- **Snapshot:** `snapshots/aranya-poetly-ai-poetry.md`
- **Extraction method:** preserved 2026-05-05 Jina Reader URL-to-Markdown extraction
- **Snapshot SHA-256:** `5cdedafa04aab6d7468bed82049f60bcde395733569dc86ed84aa5cacb1db9d2`
- **Model / corpus scope:** English-language practitioner essay on poetry, student answers, research use, and creative process; one unspecified ChatGPT version prompted once with three words to produce a poem; unspecified poetry-editing and anthology experience; an unlinked Indian Instagram poetry-page incident; no disclosed corpus, comparison group, output, prompt wording, model version, date, or measurement method
- **Access limitations:** The accessible prose article text, block quotation, links, and three footnotes are preserved. The content-bearing opening Poetry Daily poem is only an embedded-image URL; its image bytes were not preserved and its text was not transcribed, so the snapshot is partial under the user's no-rescrape waiver. The capture does not expose a byline, post ID, revision history, the reported Instagram statement, the author's test poem, student-answer examples, or evidence behind the climate-cost and Grok asides. No fresh scrape was attempted for this update.

## Summary

Aranya's Poetly essay is a first-person practitioner reflection on AI, poetry, teaching, research assistance, marketing adoption, and revision. Its strongest contribution to human-eyes is process-oriented: compare generated poetry with a writer's own archive, inspect documented revision traces, and verify AI-assisted research rather than trusting polished output. Its observations about passable poetry, student-answer confidence, marketing-executive confidence, corporate adoption, human intuition, error, spontaneity, and randomness are anecdotal or interpretive, not measured detector evidence. The post does not supply the aphorism-density, negate-and-redefine, or mood-word-accumulation taxonomy previously inherited through `dev/research/vollmer.md`.

## Main insights

- The author presents AI as a potentially useful OCR, literature-search, research-assistance, editing, and poetry-prompt tool, while requiring citation checks and human review.
- A single undisclosed three-word prompt produced what the author judged a passable poem; no prompt, output, model version, date, rubric, or comparison sample is supplied.
- The essay says phrase- or stanza-level origin may be impossible to distinguish, yet later says the author still believes a whole poem can be recognised as bot-written. This tension argues against extracting a deterministic authorship rule.
- The student-writing cues are qualitative: generalisation, scholarly-sounding depth, formal confidence, sophistication, and surface polish. The source gives no examples, rates, controls, or false-positive analysis.
- In the same paragraph, the author generalises from student answers to AI text, compares its confidence to a young marketing executive, says corporate cultures have embraced AI, reports that friends' employers encourage paid subscriptions, and quotes those friends as saying human intervention remains necessary. These are analogy, interpretation, and second-hand anecdote, not marketing-copy measurements or corporate-adoption data.
- The source's most concrete poetry guidance concerns process: multiple revision interfaces, pauses, old fragments, mistakes, precise testimony, and a writer-owned archive comparison.
- The Campbell McGrath revision account is quoted from another interview and remains indirect evidence here.
- The Instagram poetry incident is reported without a link, underlying poems, disclosure evidence, or independent verification; community allegation and post removal do not validate a textual detector.
- The author explicitly marks climate-cost and Grok-complaint asides as uncertain, making them examples of claims that require source verification rather than evidence for a human-eyes rule.

## Evidence and claims to extract

- **Direct source reviewed:** Partial preserved text of the public Poetly Substack post captured by Jina Reader on 2026-05-05; the accessible prose, links, quotation, and footnotes are present, but the content-bearing opening poem image was not preserved or transcribed under the user's no-rescrape waiver. The update was compared with the archived raw capture at `snapshots/archive/aranya-poetly-ai-poetry/2026-05-05-d6324f0bde66.md`.
- **Method and sample:** First-person practitioner commentary, not a study. Direct observations include one unspecified ChatGPT poetry generation, the author's unspecified experience as a poetry editor and anthologist, unspecified student answers and university practices, and the author's own revision routine. Reported material includes one unlinked Instagram poetry-page incident and unspecified friends' reports about company-paid AI tools and continuing manual intervention. The essay is in English and names no model version, sampling frame, output length, control group, annotation method, or quantitative result.
- **Direct versus cited evidence:** C01-C04, C06-C10, and C13-C16 are the author's observations, analogies, interpretations, or recommendations. C05 is a reported incident whose underlying evidence is unavailable. C11 records the author's explicitly uncertain claims rather than treating them as established facts. C12 is a quotation from a linked Campbell McGrath interview and is indirect until that source receives its own review. C16 combines the author's marketing-executive analogy and corporate-adoption assertion with second-hand reports from unnamed friends; it is not direct evidence about marketing prose or adoption rates.
- **Important limits and counterexamples:** C04's phrase-level indistinguishability claim conflicts with C05's confidence in whole-poem intuition. The author supplies no known-human comparison, blind test, verified AI provenance, false-positive cases, prompts, outputs, or error analysis. Human generalisation, confidence, formal register, revision neatness, mistakes, and spontaneity are all plausible look-alikes. The article's contemptuous and colloquial register also demonstrates that human writing can be uneven, forceful, digressive, and internally uncertain without yielding a reusable detector threshold.

## Matched patterns / rules

- Pattern H10 `genre_specific`, poetry branch in `human-eyes/scripts/judgement.json`: process traces, surprise or breakage, and revision depth; partial coverage for C02, C09, and C12-C14 only. C07's subjective quality and prompt-use claims, C10's technology analogy, and C15's proposed archive exercise are not covered. The branch's `concrete perception` wording is live project context, not evidence supplied by Aranya.
- Pattern H10 `genre_specific`, academic and student-essay branches: citation support, weak evidence beneath polish, and student-level or draft-history context; partial coverage for C01, C06, C08, and C11. C03's assessment policy and the technology-opacity part of C09 are not covered.
- Pattern H10 `genre_specific`, marketing-email branch: no coverage for C16. Its copy-level watchlist does not test a marketing-executive confidence analogy, corporate adoption, employer-paid subscriptions, or reported need for manual intervention.
- `human-eyes/references/process.md`, closed-source and meaning-preservation guidance: exact-source verification and no invented research or factual claims; partial coverage for C01, C08, and C11.
- Root `README.md` product boundary: human-eyes reports patterns rather than classifying authorship; appropriate handling for C04-C05.
- Focused deterministic evidence: `python3 human-eyes/scripts/grade.py audit dev/references/sources/snapshots/aranya-poetly-ai-poetry.md --surface-only` returned `audit_status: incomplete`, `no-manufactured-insight: clear`, and `no-vague-attributions: clear`. Its other findings include snapshot-template and preserved-footer material, so this surface-only run is not a complete Audit and does not validate the author's semantic cues.
- No direct support for pattern F2 quietness, F3 mood-setting, B3 contrived contrast, F2 hypothesis on aphoristic closure, or any deterministic poetry rule.

## Associated hypotheses

- None. The essay supplies no thresholds, calibration data, or pattern-density comparison.
- No new hypothesis should be promoted from the author's unmeasured authorship intuitions, single prompt, corporate-adoption anecdotes, or claims about machine error and randomness.
