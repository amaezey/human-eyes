# Testing methodology

Human-eyes tests both its pattern coverage and the quality of its edits. The committed comparative corpus measures how often matched human and AI samples trigger the grader. Additional corpora vary the sampled authors, genres, registers, and prompts so development does not optimise around the same few texts. The release gates measure whether requested patterns are removed without damaging acceptable prose.

## Complete repository test suite

Run every evaluation test as its own script:

```bash
for test_file in $(find dev/evals/tests -maxdepth 1 -type f -name 'test_*.py' | sort); do
  python3 "$test_file" || exit 1
done
```

Do not use `python3 -m unittest discover` as the full-suite command. Several established tests are executable contract scripts that intentionally exit after reporting their assertions, so importing them through discovery produces loader errors even when their tests pass.

## Comparative baseline

Five matched topics have three samples each: a human original, an AI fresh-write from the same kind of brief, and an AI rewrite of the human original. The comparison tests whether human prose triggers fewer flags than AI prose in the same register. It lives in `dev/evals/corpus.json`, and the iteration harness reports total, strong, and context-warning gaps.

The frozen skill in `dev/skill-workspace/skill-snapshot/` supplies the before/after comparison for each iteration. Do not modify it.

Run the evidence-aware paired benchmark with:

```bash
python3 dev/evals/harness/run_evidence_benchmark.py
```

The command deliberately exits with status 2 while required provenance or agent-assessed audits are missing. Its report separates candidate density from final threshold decisions, excludes house-style checks from separation claims, exposes pair reversals, and records runtime. An incomplete report is diagnostic evidence, not a benchmark result.

Candidate recognition and threshold firing answer different questions. A candidate can be correctly recognised while remaining below a document-level density threshold; tests and reports must not count that as a regex miss. Statistical checks may instead expose aggregate findings without lexical spans.

This is a calibration and regression corpus, not a held-out claim. Its sources and generated counterparts are already present in the repository and may have informed pattern development. Use it to detect changes between iterations, not to describe a new-sample result.

## Additional comparison corpora

Add a new corpus when the current samples have become too narrow for useful development feedback. "New" means newly selected for that evaluation round; it is not a claim that prior exposure contaminates a text or invalidates the established corpus.

Choose samples to increase useful variation:

- Broaden human authors, genres, registers, eras, and source types.
- Generate literal-first AI responses from ordinary task prompts, without coaching the model to add or remove human-eyes tendencies.
- Keep coached, rerolled, or human-rewrite AI samples out of the main new-corpus comparison. They answer different experimental questions and must be labelled separately if retained at all.
- Record source and generation provenance so a result can be reproduced and interpreted.
- Keep compared documents close enough in body-prose length that length-sensitive checks receive similar opportunity to fire, or report length-normalised results alongside raw findings.

Before grading, normalise packaging rather than prose:

- Remove titles, standfirsts, author biographies, subscription prompts, captions, related-story modules, and front matter from both sides.
- Preserve body punctuation, paragraph boundaries, spelling, and wording.
- Give both sides the same structural treatment so packaging does not dominate the comparison.
- Stop excerpts at paragraph or sentence boundaries. Do not truncate a human sample mid-sentence merely to reach an exact word count.

Keep exploratory samples and reports out of `dev/evals/samples/style-held-out/`. That directory is reserved for release gates. Review provenance, licence, construction method, and intended role before promoting exploratory material into a committed comparison corpus.

### Complete-audit requirement

Human-versus-AI corpus comparisons must use complete Audits. Surface-only output is useful for deterministic rule development, but it is incomplete and must not be presented as the result of a human-versus-AI benchmark unless the experiment is explicitly limited to the surface layer.

For every sample:

1. Read the version's `SKILL.md` and `judgement.json`; do not assume current CLI or schema behavior applies to an older revision.
2. Run `preflight` when that version supports bound work bundles. For a legacy version, create the complete judgement overlay its CLI expects.
3. Read the complete body prose and supply exactly one schema-valid answer for every agent-assessment registry record, with exact evidence substrings for flagged answers.
4. Run the version's complete audit command and require `coverage_mode: full` and `audit_status: complete` where its audit schema exposes those fields.
5. Verify the agent-assessed total matches the registry size. For legacy output, verify every registry item appears in `human_report.agent_judgement`.

Agent-assessed readings are model-assisted measurements. Apply the same rubric and decision standard to every sample, preserve the answer bundles with the run artefacts, and report agent-assessed and deterministic results separately so readers can see where the gap came from. Internal schemas may retain `semantic_*` field names for compatibility; that does not make the judgments deterministic semantic analysis.

### Cross-version comparisons

Run the same normalised input files against explicit immutable revisions. Record the ref, commit SHA, and date for each version. Do not use branch names or a moving tag without also resolving them to a commit.

Each version owns its own deterministic pattern and agent-assessment registries. Build fresh work bundles or legacy judgement overlays from that version's files; never reuse a current bundle with an older grader. Because registry sizes can differ, report:

- Deterministic findings, agent-assessed findings, and combined findings per document.
- Hard/strong findings separately from context warnings.
- Pairwise AI-minus-human gaps.
- Aggregate findings and findings per available check for each version.
- Newly added or removed checks and whether they fired.

Raw totals alone can make a larger registry look more discriminating. The load-bearing version result is whether the pairwise and normalised AI-minus-human gap improves without a disproportionate rise in human findings.

### Benchmark report checklist

A report is complete when it includes:

- Human source title, author, publication year, genre, and URL.
- AI generation provenance, model or agent where known, prompt constraints, and word count.
- Any known corpus overlap that materially affects the stated experiment; do not invent a universal contamination or freshness requirement.
- Packaging removed during normalisation.
- Exact version refs and registry sizes.
- Per-pair deterministic, agent-assessed, total, and hard/strong counts.
- Aggregate and normalised gaps.
- Reversed or weak pairs, not only successful separations.
- False positives and likely genre or formatting confounds.
- A clear statement that human-eyes measures prose patterns and does not classify authorship.

## Release gates

The release suite measures:

- Rejected-pattern recall.

## Deterministic catalogue robustness

The blind regex seed was generated by independent Claude subagents that received natural-language violation descriptions but no detector code, regexes, thresholds, or matching examples. Its labels are normalized to `violation` and `legitimate_control` in the committed JSONL file.

Run the property tests and regenerate the per-check report with:

```bash
python3 dev/evals/tests/test_regex_robustness.py
python3 dev/evals/harness/run_regex_catalogue_audit.py
```

The property suite requires all 50 checks to produce case-invariant decisions across the complete seed. It also covers contractions, British/American spelling, punctuation, line breaks, inflection, singular/plural forms, intervening clauses, reordered clauses, grammatical-subject changes, and Markdown variants for representative regex families.

`dev/evals/regex-catalogue-report.json` reports overall and per-check recall, specificity, false-positive rate, expected checks, actual failures, and unmapped tendencies. The 60-sample seed is directional rather than a release gate: most tendency cells contain only one sample. Expand each cell to 5–10 independently generated variants and matched controls before treating the rates as stable.

The review disposition for every deterministic check lives in [`regex-catalogue-review.md`](regex-catalogue-review.md).
- Acceptable counterpart cleanliness.
- Legitimate near-match preservation.
- Protected fact, qualification, quotation, and stance preservation.
- Complete-audit coverage.
- Suggestion and generation cleanliness.
- Revision convergence within three passes.

Run the held-out style gates:

```bash
python3 dev/evals/tests/test_style_release_gates.py
```

Held-out cases live in `dev/evals/samples/style-held-out/`. Do not copy their wording into skill prompts, catalogue examples, or implementation guidance. Development examples live separately in `dev/evals/samples/style-pairs/`.

## Grader and registry tests

```bash
python3 dev/evals/tests/test_grade.py
python3 dev/evals/tests/test_requested_style_patterns.py
python3 dev/evals/tests/test_audit_work_bundle.py
python3 dev/evals/tests/test_judgement_json.py
python3 dev/evals/tests/test_registries.py
python3 dev/evals/tests/test_agent_judgement_render.py
python3 dev/evals/tests/test_house_style.py
```

These tests cover deterministic rules, agent-assessment schemas, exact evidence spans, bundle bindings, complete coverage, generated guidance, and report rendering.

## Direct grader use

Create a work bundle, complete its agent-assessed answers, and run a full Audit:

```bash
python3 human-eyes/scripts/grade.py preflight path/to/text.md --work-bundle /tmp/human-eyes-work.json
python3 human-eyes/scripts/grade.py audit path/to/text.md --work-bundle /tmp/human-eyes-work.json --format json
```

Do not run the second command until `semantic_answers` contains one valid answer for every current `judgement.json` record. A completed-looking report without full, source-bound agent-assessment coverage is invalid.

For deterministic development output:

```bash
python3 human-eyes/scripts/grade.py audit path/to/text.md --surface-only --format json
```

Surface-only output is incomplete, cannot unlock generative actions, and is not a substitute for a complete comparative benchmark.

## Model-backed lifecycle suite

```bash
python3 dev/evals/harness/run_action_evals.py --executor codex --workers 8 --suite action-lifecycle
```

The wrapper resolves Skill Creator from `HUMAN_EYES_SKILL_CREATOR_PATH` or the installed Codex plugin cache. The fixed suite checks full Audit coverage, surface-only gating, suggestion contamination, fresh rewrite bindings, Write coverage, residual reporting, installed-path resolution, and convergence.

## Render regression

```bash
python3 dev/evals/harness/diff_renders.py --verify
```

Use `--capture` only after inspecting and accepting every intentional report change.

## Results

Current performance lives in the generated block in `README.md` and in full at `dev/skill-workspace/latest-performance-report.md`. Each iteration also writes a dated report under `dev/skill-workspace/reports/`.

The committed comparison baseline, fresh matched-pair benchmarks, and writing-cleanup gates answer different questions. A release must retain comparative coverage and pass the removal, preservation, audit-completeness, and convergence gates. Fresh benchmarks add evidence about generalisation, but they do not replace the repeatable committed baseline.

Open hypotheses remain in [`hypotheses.md`](hypotheses.md).
