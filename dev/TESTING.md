# Testing methodology

Human-eyes tests both its pattern coverage and the quality of its edits. The comparative corpus measures how often matched human and AI samples trigger the grader. The release gates measure whether requested patterns are removed without damaging acceptable prose.

## Comparative baseline

Five matched topics have three samples each: a human original, an AI fresh-write from the same kind of brief, and an AI rewrite of the human original. The comparison tests whether human prose triggers fewer flags than AI prose in the same register. It lives in `dev/evals/corpus.json`, and the iteration harness reports total, strong, and context-warning gaps.

The frozen skill in `dev/skill-workspace/skill-snapshot/` supplies the before/after comparison for each iteration. Do not modify it.

## Release gates

The release suite measures:

- Rejected-pattern recall.
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

These tests cover deterministic rules, semantic schemas, exact evidence spans, bundle bindings, complete coverage, generated guidance, and report rendering.

## Direct grader use

Create a work bundle, complete its semantic answers, and run a full Audit:

```bash
python3 human-eyes/scripts/grade.py preflight path/to/text.md --work-bundle /tmp/human-eyes-work.json
python3 human-eyes/scripts/grade.py audit path/to/text.md --work-bundle /tmp/human-eyes-work.json --format json
```

For deterministic development output:

```bash
python3 human-eyes/scripts/grade.py audit path/to/text.md --surface-only --format json
```

Surface-only output is incomplete and cannot unlock generative actions.

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

The comparison baseline and the writing-cleanup gates answer different questions. A release must retain comparative coverage and pass the removal, preservation, audit-completeness, and convergence gates.

Open hypotheses remain in [`hypotheses.md`](hypotheses.md).
