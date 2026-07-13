---
name: human-eyes
description: >-
  Audits and edits prose that uses writing habits commonly associated with
  machine-generated text. Use for audits, suggestions, rewrites, or new drafts
  when the user wants to remove AI-feeling phrasing, rhythm, structure, or voice.
---

# Human-eyes

Human-eyes is an opinionated writing-cleanup skill. It identifies specific constructions the reader wants removed and never classifies authorship.

The writer controls every edit. Audit is the default action. Suggestions, Rewrite, and Write run only when requested.

## Resolve the skill directory

Resolve `SKILL_DIR` to the absolute directory containing this `SKILL.md` before running any command. Call scripts and read references through `SKILL_DIR`; do not assume the current working directory is the repository.

## Choose the action

| Action | Use when | Result |
|---|---|---|
| Audit | The user supplies prose for review or does not request an edit | Complete deterministic and semantic findings |
| Suggestions | The user asks how to fix audited prose | One context-validated replacement per finding |
| Rewrite | The user asks for revised source prose | Source Audit, revised prose, fresh output Audit, change report |
| Write | The user supplies a brief without a draft | Draft, complete Audit, change report |

If intent is ambiguous, default to Audit. Never treat a surface-only scan as an Audit.

## Run a complete Audit

Save the exact input to a temporary UTF-8 Markdown file. Preserve source punctuation and line breaks.

Create a private work bundle:

```bash
python3 "$SKILL_DIR/scripts/grade.py" preflight "$INPUT_PATH" --work-bundle "$WORK_PATH"
```

When preserved slide or caption boundaries are available, supply a structure manifest:

```bash
python3 "$SKILL_DIR/scripts/grade.py" preflight "$INPUT_PATH" --work-bundle "$WORK_PATH" --structure-manifest "$STRUCTURE_PATH"
```

Read the complete input, `scripts/judgement.json`, and the bundle's `semantic_candidates`. Fill `semantic_answers` with exactly one answer for every current registry record. Candidates focus attention but do not limit the reading.

Each semantic answer contains only:

- `id`: the registry ID.
- `status`: `clear` or `flagged`, derived from `flagged_when`.
- `answer`: the exact shape required by `answer_schema`.
- `evidence`: a list of exact input substrings. Use an empty list for a clear answer with no quoted evidence.

For a list answer, every item's first field is an exact input substring. Explain the missing antecedent, criterion, information, context, or logical relationship in the item's second field. Do not add severity; the grader owns severity.

Write the completed bundle back to `WORK_PATH`, then render the Audit:

```bash
python3 "$SKILL_DIR/scripts/grade.py" audit "$INPUT_PATH" --work-bundle "$WORK_PATH" --format markdown --depth balanced
```

Use `--full-report` when the user asks for complete coverage tables. Use `--format json` when a later action needs structured findings. Print Markdown output without paraphrasing quoted evidence.

If the bundle is missing, partial, stale, malformed, or contradictory, stop and repair the semantic reading. Do not render a completed-looking Audit.

## Use surface-only mode

Surface-only mode exists for deterministic development checks:

```bash
python3 "$SKILL_DIR/scripts/grade.py" audit "$INPUT_PATH" --surface-only --format markdown --depth all
```

The result is incomplete. Do not offer or run Suggestions, Rewrite, or Write from it.

If Python or the grader is unavailable, report the limitation and stop. A manual scan cannot satisfy complete Audit coverage.

## Produce Suggestions

Run a complete source Audit first. Read `references/alternatives.md` for lexical findings and `references/process.md` for structural findings.

For each proposed replacement:

1. Apply the replacement to a copy of its surrounding sentence or paragraph.
2. Save the changed context as a new input.
3. Create and complete a new work bundle.
4. Run a complete Audit of the changed context.
5. Return the suggestion only when it clears the target finding without introducing another required finding.

These are completion requirements, not advice. Do not return a replacement based only on reading it. For every returned replacement, retain the changed-context path, its new work-bundle path, and the successful Audit result in the working transcript. If any of those three artefacts is absent, omit the replacement and state that it was not validated. Never claim or imply context validation when only the source was audited.

The changed-context file contains the complete original surrounding paragraph with exactly one proposed replacement applied. Do not validate a bare replacement, combine unrelated replacements into a collage, or audit wording different from the wording returned. Read each changed paragraph and answer all 15 semantic records for that paragraph. Never bulk-fill semantic answers as clear. A schema-valid bundle with fabricated clear answers is not a complete Audit.

Keep quotations, facts, stance, and factual qualifications unchanged. A suggestion count matches the finding count unless a finding cannot be repaired without changing meaning; name the constraint instead of inventing a replacement.

## Produce a Rewrite

Run a complete source Audit, then read `references/process.md` and `references/voice.md`.

Use Balanced depth unless the user requests All. Balanced repairs hard failures and strong warnings and reviews contextual findings against meaning. All attempts to repair every finding while preserving the source.

Save the rewrite as a new file. Create a new work bundle and complete a fresh Audit. Never reuse the source bundle. Revise and repeat for no more than three passes.

Before editing, extract every direct quotation, citation, name, date, link, stated quantity, and explicitly qualified claim into a protected-literals list. Protect the complete sentence for claims containing modality or limits such as `may`, `might`, `can`, `could`, `often`, `sometimes`, `especially`, `particularly`, `limited`, or `uncertain`. After each pass, compare the rewrite against that list. Reject a pass that removes or changes a protected literal unless the user explicitly authorised that change. An improved finding set does not override failed preservation.

Treat the source as a closed factual record just as Write treats the brief. Do not add a new recommendation, threshold, safety criterion, source description, research claim, process, or consequence. Do not insert Audit commentary into the rewritten document: phrases such as `the draft`, `unnamed here`, `needs a source`, and `before publication` belong in Remaining findings, not the prose.

Record the required finding IDs after each pass. Stop if a pass introduces a new required finding or if the sets alternate between two states. Report the regression or oscillation instead of continuing.

Return:

- The source Audit.
- The rewritten prose.
- A compact change report using `Changes made`, `Preserved`, and `Remaining findings`.

If required findings remain after the third pass, list them. Do not claim completion.

## Produce new writing

Draft from the supplied brief without inventing facts, personal experience, opinions, emotion, humour, uncertainty, or names. Read `references/voice.md` before drafting.

Before drafting, create a private brief-facts list containing only claims explicitly supplied by the user. After drafting, inspect every concrete person, organisation, date, deadline, process step, dataset role, cause, consequence, notification, status, measurement, and commitment. Delete anything that cannot be traced to the brief-facts list. Plausible standard procedure is still invented detail. When the requested length cannot be reached without new facts, return a shorter factual draft or ask for the missing information; do not pad with fabricated process.

Save the draft, create a work bundle, complete every semantic answer, and run a full Audit. Revise and re-audit for no more than three passes. Return the draft and compact change report only after a clean required-finding result, or return the residual findings at the limit.

Record required finding IDs after every pass and stop on newly introduced findings or alternating sets.

## Preserve meaning

The source or brief controls argument, facts, examples, stance, genre, point of view, and factual uncertainty. Do not manufacture irregularity to make prose appear human. Do not add a parenthetical doubt, forced register change, anecdote, or personal detail.

Every generated heading must contain no parentheses. Every generated demonstrative and definite description needs an identifiable referent. Remove performed candour, relevance padding, redundant recap, counted slogans, unsupported evaluation, empty connections, staccato filler, and prose aimed at absent chat context.

## Keep the product boundary

Describe the construction, reading problem, and edit. Do not estimate provenance, assign a probability, accuse the writer, or call the result proof of authorship.
