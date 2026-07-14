# Source-ingestion quality gates

Use this checklist for each new or updated card. A card does not pass because its Markdown renders or its metadata fields are populated.

## Full-text gate

- The snapshot contains the complete accessible source, not an abstract, search snippet, reader summary, login page, JavaScript shell, or bot challenge.
- The extraction was checked against the rendered source at the beginning, middle, and end.
- Page count, section order, tables, notes, captions, appendices, and references were checked where applicable.
- Any missing or transformed material is named precisely.
- A partial or unavailable source leaves the ingestion blocked.

## Provenance gate

- The canonical URL and every alternate access route are recorded.
- A URL-free local source uses an explicit local-file identity rather than an invented URL.
- Author or owner, publisher, publication and retrieval dates, source type, and evidence tier are present.
- DOI, revision, commit, or version is recorded when one exists; otherwise the card says `none found`.
- The extraction method is reproducible enough for another reviewer to repeat.
- The snapshot path resolves under `snapshots/`, contains no `..` component, does not escape through a symlink, and its SHA-256 matches the exact saved bytes.
- An update preserves the prior reviewed revision and names both versions compared.
- The previous update snapshot resolves under `snapshots/archive/`; previous and current paths resolve to distinct files.
- The Update provenance table names prior/current identifiers, paths, retrieval dates, and digests; the current identifier, retrieval date, snapshot, and digest match Metadata; and both files match their recorded hashes.
- Direct findings, cited claims, author interpretation, and reviewer inference remain distinguishable.

## Extraction gate

- Every relevant positive finding, null result, counterexample, limit, and qualification has a claim ID.
- Method, sample, comparison group, model/version, time, genre, platform, language, and length scope are recorded when relevant.
- Exact examples are attributed and short enough to avoid replacing the source.
- No aggregate result is presented as a single-document authorship rule.
- Any cited source used for a project conclusion has its own direct review or is marked indirect and unresolved.

## Project-comparison gate

- Every claim row names the exact project implementation, guidance, test, card, or hypothesis inspected.
- Live code was inspected for executable coverage.
- Uncertain deterministic coverage was run and its actual output recorded.
- Surface-only output is not described as a complete Audit.
- Coverage uses one of: fully covered, partly covered, not covered, or challenges current behaviour.
- Frequency, clustering, genre, quotation, formatting, deliberate use, and human look-alikes are considered where relevant.

## Recommendation and status gate

- Every claim has one recommendation, including `record only` or `take no further action` where appropriate.
- Recommendations follow from the evidence and coverage review.
- Required tests or evaluation are named.
- User decision and implementation status are separate and accurate.
- Decision and implementation status cells use the exact canonical lowercase values and follow the permitted transition table.
- Every `implemented` claim has its own `- Cnn: passed - <verification command/result>` line under `Evaluation of approved changes`; other claims may record independent not-applicable outcomes.
- No recommendation is presented as implemented before the corresponding project diff and verification exist.
- Product changes stop at pending recommendations unless the user requested implementation.

## Source-record verification gate

Use a read-only independent reviewer that did not perform the extraction whenever subagents are available. This is a generic source-record review, not a required invocation of `ce-doc-review`. Give the reviewer the finished card, preserved full text, relevant project evidence, and these lenses:

- **Evidence reviewer:** checks whether the card says what the source supports, with the same scope and uncertainty.
- **Provenance reviewer:** checks identity, version, access route, archive history, snapshot integrity, and directness.
- **Project reviewer:** checks each coverage claim against the live checker, registry, guidance, tests, and hypotheses.
- **Decision reviewer:** checks that recommendations, user decisions, and implementation statuses cannot be confused.
- **Completeness reviewer:** checks the full source against the claim inventory for omissions.

The reviewer reports findings without editing. The ingesting agent resolves them and requests a focused recheck after material changes. Resolve material findings before setting `Review status: passed`. Record unresolved material findings rather than hiding them in prose.

If subagents are unavailable, perform the same checks as a self-review and record `self-review fallback: subagents unavailable`. Otherwise record `independent source-record reviewer: <agent name>`.

`ce-doc-review` may be added as a coherence/feasibility pass when available, but it is not required. The source-specific lenses above remain mandatory because a plan-oriented document review cannot establish source-to-claim fidelity.

If the check cannot pass, keep `Review status: failed`, name the unresolved evidence problem, and stop before approval or implementation. A new blocked record is not added to the accepted source index. A blocked update does not replace the currently reviewed card or snapshot. Report those consequences to the user and ask directly for the evidence, access, or decision required to continue.

## Deterministic gate

The validator must pass for the exact card. `git diff --check` must pass for the card, snapshot, manifest, `sources/README.md`, `pattern-opportunities.md`, and the root source index when applicable. Inspect untracked files directly, then inspect the final diff and `git status --short --branch` so unrelated or user-owned edits are not accidentally staged or rewritten.
