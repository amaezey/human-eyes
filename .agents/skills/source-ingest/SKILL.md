---
name: source-ingest
description: >-
  Ingests a new source into the human-eyes evidence library or refreshes an
  existing source. Use when the user supplies a source URL or file, asks to add
  research or practitioner evidence, or asks to update, refresh, re-extract, or
  re-review a card under dev/references/sources.
---

# Source ingest

Create a complete, reviewable evidence record for one source. Preserve the direct source, separate its claims from project decisions, compare every relevant claim with the live project, and stop for approval before implementing recommendations unless the user expressly requested implementation.

## Resolve the checkout

Find the active repository root from the current working directory. It must contain:

- `dev/references/sources/README.md`
- `dev/references/sources/TEMPLATE.md`
- `dev/references/sources/snapshots/MANIFEST.md`

If those files are absent, ask for the `human-eyes` checkout path. Do not write into an installed release copy or guess which checkout the user meant.

Set these paths conceptually:

- `REPO_ROOT`: the checkout root.
- `SOURCES_DIR`: `$REPO_ROOT/dev/references/sources`.
- `SKILL_DIR`: the directory containing this `SKILL.md`.

Read the checkout's `AGENTS.md` before using tools. Obey its restrictions, including model/provider and command restrictions. A source-review request does not grant permission to call a prohibited provider.

## Establish the mode

Infer the mode from the source URL, stable identifier, or requested card:

- **New source:** no existing card records the same source.
- **Update:** an existing card records the source, or the user asks to refresh it.

Search source cards, the manifest, and snapshots by canonical URL, DOI or other stable identifier, title, author, and likely slug before deciding a source is new. Treat a publisher page, preprint, accepted manuscript, and final paper as versions of one work unless they contain materially separate evidence.

Ask a blocking question only when identity is genuinely ambiguous, the user supplied several sources without a requested order, or a decision would change which work is preserved.

## Read the operating contract

Before extraction, read in full:

1. `$SOURCES_DIR/README.md`
2. `$SOURCES_DIR/TEMPLATE.md`
3. `$SOURCES_DIR/SNAPSHOT_TEMPLATE.md`
4. `$SOURCES_DIR/snapshots/MANIFEST.md`
5. `$SKILL_DIR/references/quality-gates.md`

For project comparison, also inspect the current versions of:

- `human-eyes/scripts/patterns.json`
- `human-eyes/scripts/judgement.json`
- `human-eyes/references/patterns.md`
- `human-eyes/references/process.md`
- `dev/references/sources/pattern-opportunities.md`
- `dev/hypotheses.md`, `STRATEGY.md`, and `dev/TESTING.md` when present

Do not rely on remembered catalogue contents or a prior source review.

## Acquire and preserve the direct source

Read the source itself. Search results, snippets, Wikipedia summaries, press coverage, abstracts, and another card do not substitute for full text.

Use the least lossy available route:

1. Direct HTML or first-party plain text.
2. Publisher, repository, or author-hosted PDF/DOCX and a complete local extraction.
3. Official API, revision endpoint, raw repository file, or rendered browser page.
4. An accessible accepted manuscript or archived first-party version when the canonical version is blocked.

For PDFs, preserve and extract every page, including appendices, tables, footnotes, captions, and references when they bear on claims. For repository sources, record the commit SHA and preserve every file used. For social posts or threads, preserve the complete thread, timestamps, attachments needed to understand it, and stable post identifiers. For living pages, record the revision or content version.

Inspect the beginning, middle, and end of the extraction and compare headings, page count, section order, tables, notes, and references with the rendered source. Do not call an abstract, reader summary, login page, bot challenge, empty JavaScript shell, or truncated extraction complete.

If full text is inaccessible, try the applicable routes above. Record what failed and what remains unavailable. Stop and tell the user that ingestion cannot pass the full-text gate; do not silently downgrade to a summary and do not create a completed-looking card.

## Preserve an update without erasing history

Before replacing an existing snapshot:

1. Verify its recorded SHA-256 against the bytes on disk.
2. Preserve it under `snapshots/archive/<slug>/<retrieved-date>-<revision-or-short-hash>.md` if that exact version is not already archived.
3. Record the previous and reviewed identifiers or hashes in the updated card.
4. Compare the two snapshots and identify additions, removals, corrections, and unchanged material.

Never overwrite the only copy of a reviewed revision. A changed retrieval date alone is not evidence that the source changed.

## Record provenance

Create the snapshot from `SNAPSHOT_TEMPLATE.md`. Record:

- canonical URL and every accessed alternate URL; for a source supplied only as a local file, record `none; local file: <repo-relative-or-user-supplied-name>` rather than inventing a URL;
- title, author or owner, publisher, publication date, and retrieval date;
- DOI, revision ID, commit SHA, version, or an explicit `none found`;
- extraction route and tools used;
- complete, partial, or unavailable full-text status;
- access failures, omissions, transformations, and OCR limitations;
- model family/version, corpus dates, genre, platform, language, and sample scope when relevant.

Save the snapshot, then compute its SHA-256 from the final bytes. Put that digest in the source card and manifest. Do not add the digest to the snapshot after hashing it.

Keep the requested source as the hard scope boundary. Open a cited source when needed to determine whether an inherited claim is direct, accurate, or suitable for a recommendation, but do not recursively ingest it in the same run. Record it as indirect evidence and a follow-up item. Ask before starting a separate ingestion, including when direct review is required before a recommendation can proceed.

## Extract every relevant claim

Read the preserved full text, not only the introduction and conclusion. Capture all relevant:

- phrases, constructions, vocabulary, formatting, structure, rhythm, tone, workflow residue, and provenance failures;
- methods, samples, comparisons, measurements, negative results, counterexamples, and limitations;
- rewriting, editing, evaluation, and process findings;
- model, time, genre, platform, language, and length boundaries;
- distinctions between direct results, author interpretation, cited claims, and your own inference.

Assign stable claim IDs such as `C01`, `C02`, and `C03` within the card. Preserve exact examples only when needed and keep quotations short. Do not infer a threshold, causal result, or document-level verdict from aggregate or anecdotal evidence.

## Compare every claim with the live project

For each claim ID:

1. Locate the exact check, registry record, guidance, fixture, source mapping, or hypothesis that might cover it.
2. Read the implementation, not only the rendered catalogue.
3. Run the focused deterministic check when coverage is uncertain.
4. Label coverage `fully covered`, `partly covered`, `not covered`, or `challenges current behaviour`.
5. Record what the implementation actually finds, what is missing, and which controls matter.

Surface-only output proves deterministic coverage only. It is not a complete human-eyes Audit. If a complete Audit is relevant, use the bound work-bundle procedure in `dev/TESTING.md` and preserve its evidence.

Keep the source claim, evidence assessment, live-project result, and recommendation in separate columns. Documentation that names a pattern does not prove that the checker detects it.

## Write the evidence record

For a new source, copy `TEMPLATE.md` into a kebab-case card name. For an update, preserve useful existing analysis but bring the entire card up to the current template.

Complete every section. Use the Project coverage table as the single authoritative review table. Give every claim one row, one recommendation, a user decision, and an implementation status. `pending` is a decision state; `not started` is an implementation state. Never imply that a recommendation was implemented merely because it appears in the card.

Escape a literal pipe inside any table cell as `\|`. An unescaped extra pipe creates a malformed row and fails validation.

Use these exact lowercase statuses:

- **User decision:** `pending`, `approved`, `approved with changes`, or `rejected`.
- **Implementation status:** `not started`, `in progress`, `implemented`, `review required`, `blocked`, `superseded`, or `not applicable`.

The allowed transitions are:

- `pending` with `not started` or `review required`;
- `approved` or `approved with changes` with `not started`, `in progress`, `implemented`, `blocked`, or `not applicable`;
- `rejected` with `not applicable` or `superseded`.

Before using `approved with changes`, rewrite the recommendation row to the wording the user approved. Use `implemented` only after the named verification passes and `Evaluation of approved changes` contains a claim-keyed line shaped `- Cnn: passed - <verification command/result>`. Give each implemented claim its own line; pending, rejected, or non-product-change claims may have separate not-applicable lines.

For an updated source, reconcile decisions before reporting:

- Keep the current status for a claim only after confirming its evidence and meaning are materially unchanged.
- Reset a new or materially changed claim to `pending` and `not started`.
- If changed evidence supported a product change that still exists, use `pending` and `review required` until the user decides whether to retain, revise, or reverse it.
- Move removed or superseded claims and their prior decisions to `Decision history`; do not delete the record.
- Record any implementation affected by a removed or weakened claim as a decision required from the user.

Update all applicable indexes:

- `snapshots/MANIFEST.md` with one row containing the card, URL, snapshot, extraction method, retrieval date, stable identifier, digest, and full-text status; append the provenance details in the Method cell so the existing four-column manifest remains valid;
- `sources/README.md` in the correct evidence category;
- the root `README.md` source list when that list is present;
- `pattern-opportunities.md` for promoted evidence, explicit non-promotions, or deferred candidates.

Do not change checkers, registries, tests, hypotheses, or product guidance during the review phase unless the user already requested implementation.

## Isolate every source work unit

Treat one source as one context boundary. If a request contains multiple sources, create a separate work unit for each source and complete extraction, card drafting, review, and validation independently.

- Never assign more than one source to the same ingesting subagent or reviewer.
- Never reuse an agent, thread, reviewer task, or prior named reviewer for a second source, even sequentially or after it becomes idle.
- Never cross-review active ingestions. A reviewer assigned to source A must not review source B, compare source B's draft, or receive source B's source text, card, findings, or reviewer context.
- Spawn a fresh reviewer for exactly one source after that source's extraction is drafted. The reviewer must not have extracted that source or participated in any other source ingestion in the request or batch.
- Give the reviewer only that source's card, snapshot, identity and version, plus the source-specific project files or executed-check evidence needed to verify coverage. The reviewer may inspect existing library records when they are relevant project evidence, but must not be tasked with reviewing another new or updated source.
- Keep focused rechecks with the same dedicated reviewer for that same source so its context remains intact. Never give that reviewer a second source.
- If agent capacity is limited, process sources sequentially and spawn a fresh reviewer for each one. If subagents are unavailable entirely, fall back to a recorded self-review rather than skipping review, and never borrow an agent assigned to another source.

## Verify the finished source record

This is an independent semantic review, not an invocation of `ce-doc-review`. Run it after the card and indexes are drafted and before deterministic validation.

Spawn one fresh, read-only, source-dedicated generic reviewer that did not perform the extraction and has not participated in another source ingestion in the request or batch. Give it the card, snapshot, source identity and version, relevant project files or executed-check evidence, and the five lenses below. Instruct it to return concrete findings without editing files. Obey the checkout's provider and tool restrictions in the reviewer prompt.

The ingesting agent resolves the findings. If a fix materially changes claims, provenance, coverage, recommendations, or statuses, ask the same source-dedicated reviewer to check the affected material again. Do not use that reviewer for any other source. Use same-agent review only when subagents are unavailable, and record `self-review fallback: subagents unavailable` as the review method.

1. **Source fidelity:** compare every claim row with the preserved full text. Confirm that wording, scope, qualifications, counterexamples, and direct-versus-cited attribution still match.
2. **Provenance:** confirm the source identity, reviewed version, access routes, snapshot, archive history, and hashes.
3. **Project coverage:** reopen every cited checker, registry, guide, test, source card, or hypothesis and confirm the coverage statement is accurate.
4. **Decision integrity:** confirm each recommendation has the right claim ID and that decision, implementation, and evaluation states agree.
5. **Completeness:** scan the source again for relevant findings, null results, limits, or examples omitted from the card.
6. Fix each material discrepancy and record what changed under `## Document review`.

If `ce-doc-review` is installed or the user requests it, it may be used as an additional coherence/feasibility pass. It is optional and cannot replace the checks above.

Record either `independent source-record reviewer: <agent name or task ID>` or the explicit self-review fallback under `Review method`. When the review ran with a fresh dedicated reviewer, also record `Reviewer isolation: fresh source-dedicated agent; one source only; not reused`. The gate passes only when `Review status` is `passed` and `Unresolved findings` is `none`. If a material finding cannot be resolved, leave the gate failed and report it to the user.

## When ingestion cannot pass

Do not present a blocked record as ingested, ask for recommendation approval, or make product changes. Every blocked path ends with a direct user handoff; never merely stop.

- **Ambiguous source identity:** do not create or replace library files. Show the competing identities or versions and ask the user which one to ingest.
- **Partial or unavailable full text:** report the routes attempted and exact missing material. Do not add the card to the source index or replace an existing card or snapshot. Ask the user for an accessible file or alternate link, or whether to stop without ingestion. Preserve a clearly marked draft only when the user asks to keep partial work.
- **Broken provenance or snapshot integrity:** retry or correct the provenance. If it cannot be repaired, do not index the new record and do not replace the current reviewed version. Ask the user for the authoritative source/version or an intact copy; do not offer to waive the gate.
- **Unresolved independent-review finding:** set `Review status` to `failed`, record the exact finding, and do not treat recommendations as decision-ready. Ask for the missing evidence or the specific source/project decision needed to resolve it.
- **Deterministic validation failure:** fix mechanical errors and rerun the validator without asking. If the failure reflects missing evidence or a contract conflict that cannot be fixed within the source record, leave it failed and ask the user for the missing input or permission to handle the tooling issue as separate work.

In every blocked case, state what remains unchanged, what draft material was preserved, the exact blocker, and the user input or source access needed to continue, then ask a direct question. For an update, explicitly tell the user that the previously reviewed card, snapshot, decisions, and indexes remain authoritative until the candidate update passes.

## Run deterministic quality gates

Validate the exact card:

```bash
python3 "$SKILL_DIR/scripts/validate_source.py" "$CARD_PATH"
```

Then run:

```bash
git diff --check -- "$CARD_PATH" "$SNAPSHOT_PATH" \
  "$SOURCES_DIR/README.md" "$SOURCES_DIR/snapshots/MANIFEST.md" \
  "$SOURCES_DIR/pattern-opportunities.md" "$REPO_ROOT/README.md"

git status --short --branch
```

Inspect the named files directly as well as the final diff because new cards and snapshots may still be untracked. Report the branch, cleanliness, upstream state, and any unrelated user-owned changes. Do not weaken the validator or mark a field `not applicable` merely to get a pass.

## Report and stop for decisions

Lead with what the source changed in the project's understanding. State what was already known, current coverage, genuinely new or challenging evidence, the size of the change, access limitations, and the decisions required.

Show the complete authoritative review table. Unless implementation was expressly requested, stop here and ask the user to approve, reject, or modify the pending recommendations.

After approval, implement only approved rows, run the relevant tests and evaluation from `dev/TESTING.md`, update decision and implementation statuses, repeat document review and validation, and report what changed and what remains.
