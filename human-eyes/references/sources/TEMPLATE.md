# <Source title>

## Metadata

- **URL:** <canonical source URL, or `none; local file: <name>` when no URL exists>
- **Author / owner:** <person or organisation>
- **Published:** <date, range, or none found>
- **Retrieved:** <YYYY-MM-DD>
- **Extracted:** <YYYY-MM-DD>
- **Source type:** <peer-reviewed study, preprint, first-party documentation, journalism, practitioner observation, vendor analysis, catalogue, or other precise type>
- **Evidence tier:** <tier from README.md>
- **Review mode:** <new or update>
- **Stable identifier:** <DOI, revision ID, commit SHA, report number, or none found>
- **Version / revision:** <reviewed version and prior version for an update, or none found>
- **Full-text status:** <complete, partial, or unavailable>
- **Snapshot:** `snapshots/<card-slug>.md`
- **Extraction method:** <direct HTML, PDF-to-text, repository raw files, browser transcription, or other reproducible method>
- **Snapshot SHA-256:** `<64-character digest of the final snapshot bytes>`
- **Model / corpus scope:** <models, versions, corpus dates, genre, platform, language, sample, or not applicable>
- **Access limitations:** <none or exact inaccessible/omitted/transformed material>

## Summary

<One compact paragraph describing the source, method, sample, contribution to human-eyes, and material scope limits.>

## Main insights

- <Finding, null result, counterexample, qualification, or process insight.>

## Evidence and claims to extract

- **Direct source reviewed:** <what exact source/version was read>
- **Method and sample:** <method, sample, comparison group, dates, models, genre, platform, language, and text length>
- **Direct versus cited evidence:** <which claim IDs are measured here and which are inherited from cited work>
- **Important limits and counterexamples:** <uncertainty, conflicts, human comparisons, and unanswered questions>

## Skill-use audit

- **Good use:** <what the source can support in human-eyes>
- **Misuse / overclaim:** <what would exceed its evidence>
- **Unsupported use:** <claims, genres, models, or decisions it cannot support>
- **Underused evidence:** <relevant evidence the project does not yet use>
- **Patterns left on the table:** <relevant examples, qualifications, or challenges not represented>

## Matched patterns / rules

- <Exact check, agent assessment, guidance, test, or none>

## Associated hypotheses

- <Existing hypothesis ID and name, proposed hypothesis, or none>

## Questions / follow-up

- <Missing access, unresolved source question, evidence to retrieve, or none>

## Update provenance

For a new source, write `Not applicable: initial ingestion.` For an update, complete this table. Paths must contain no `..` components. The previous snapshot must resolve under `snapshots/archive/`, the current snapshot must resolve under `snapshots/`, and they must resolve to distinct files. The current stable identifier, snapshot, retrieval date, and digest must exactly match Metadata.

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | <prior revision, DOI, commit, or hash> | `snapshots/archive/<slug>/<date>-<revision-or-short-hash>.md` | <YYYY-MM-DD> | `<64-character digest>` |
| current | <reviewed revision, DOI, commit, or hash> | `snapshots/<card-slug>.md` | <YYYY-MM-DD> | `<64-character digest>` |

## Decision history

- <For a new source, write `None: initial review.` For an update, preserve removed or superseded claim IDs, their prior decisions and implementation statuses, the reviewed revision, and why the current review reopened or retired them.>

## Project coverage

This is the authoritative review table. Give every relevant source claim or example a stable claim ID in the first cell.

Escape any literal pipe within a table cell as `\|`; an unescaped extra pipe makes the row invalid.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: <claim or exact example> | <source type, evidence basis, directness, scope, support, uncertainty, and human comparison> | <exact check, assessment, guidance, test, source card, or hypothesis; coverage status; actual result if run> | <missing implementation, mapping, explanation, control, or test> | <proposed change or take no further action; affected files; required verification> | pending | not started |

## Recommendations

- C01: <Decision-ready recommendation matching the authoritative table. Keep pending work separate from completed changes.>

## Evaluation of approved changes

- <For every implemented claim, write `Cnn: passed - <verification command/result>` after this list marker. Give each claim its own line. For pending, rejected, or no-product-change claims, use a separate claim-keyed not-applicable line.>

## Document review

- **Review status:** <pending, passed, or failed>
- **Review method:** <`independent source-record reviewer: <agent name>` or `self-review fallback: subagents unavailable`, plus any optional review method>
- **Findings resolved:** <material findings fixed, or none>
- **Unresolved findings:** <none, or exact finding that prevents a pass>
