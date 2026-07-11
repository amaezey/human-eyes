#!/usr/bin/env python3
"""Run the fixed model-backed action lifecycle suite."""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HARNESS = Path(__file__).with_name("run_skill_creator_iteration.py")
EVALS = ROOT / "dev/evals/evals.json"

SUITES = {
    "action-lifecycle": [
        "audit-requires-complete-judgement",
        "surface-only-blocks-actions",
        "suggestion-rejects-new-slop",
        "rewrite-rebinds-audit",
        "write-fresh-audit",
        "revision-limit-reports-residuals",
        "installed-path-resolution",
        "revision-convergence",
    ]
}


def evaluate_convergence(passes):
    """Evaluate required-finding sets from at most three generated revisions."""
    finding_sets = [frozenset(items) for items in passes]
    if not finding_sets or len(finding_sets) > 3:
        return {"passed": False, "reason": "expected one to three revision passes"}
    for index in range(2, len(finding_sets)):
        if finding_sets[index] == finding_sets[index - 2] != finding_sets[index - 1]:
            return {"passed": False, "reason": "finding sets oscillate"}
    for previous, current in zip(finding_sets, finding_sets[1:]):
        if current - previous:
            return {"passed": False, "reason": "new required findings were introduced"}
    return {
        "passed": True,
        "reason": "clean" if not finding_sets[-1] else "stable residual findings remain",
    }


def version_key(path):
    name = path.parent.parent.name
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", name)
    return tuple(map(int, match.groups())) if match else (-1, -1, -1)


def resolve_skill_creator():
    explicit = os.environ.get("HUMAN_EYES_SKILL_CREATOR_PATH")
    if explicit:
        candidates = [Path(explicit).expanduser()]
    else:
        codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
        root = codex_home / "plugins/cache/claude-plugins-official/skill-creator"
        candidates = [path.parent for path in root.glob("*/skills/skill-creator/SKILL.md")]
    candidates = [path.resolve() for path in candidates if (path / "SKILL.md").is_file()]
    if not candidates:
        raise SystemExit(
            "Skill Creator was not found. Install the skill-creator plugin or set "
            "HUMAN_EYES_SKILL_CREATOR_PATH to its skills/skill-creator directory."
        )
    versioned = [path for path in candidates if version_key(path) != (-1, -1, -1)]
    if versioned:
        return max(versioned, key=version_key)
    if len(candidates) == 1:
        return candidates[0]
    raise SystemExit(
        "Skill Creator resolution is ambiguous. Set HUMAN_EYES_SKILL_CREATOR_PATH explicitly."
    )


def failed_lifecycle_runs(iteration_path, names):
    failures = []
    for name in names:
        matches = list(iteration_path.glob(f"eval-*-{name}/with_skill/run-1"))
        if len(matches) != 1:
            failures.append(f"{name}: expected one run directory, found {len(matches)}")
            continue
        run_dir = matches[0]
        response_path = run_dir / "outputs/response.md"
        metrics_path = run_dir / "outputs/metrics.json"
        grading_path = run_dir / "grading.json"
        missing = [
            path.name for path in (response_path, metrics_path, grading_path) if not path.is_file()
        ]
        if missing:
            failures.append(f"{name}: missing {', '.join(missing)}")
            continue
        response = response_path.read_text()
        metrics = json.loads(metrics_path.read_text())
        grading = json.loads(grading_path.read_text())
        if not response.strip() or response.startswith("ERROR:"):
            failures.append(f"{name}: empty or failed executor response")
        elif metrics.get("errors_encountered", 0) > 0:
            failures.append(f"{name}: executor reported an error")
        elif grading.get("summary", {}).get("failed", 0) > 0:
            failures.append(f"{name}: one or more assertions did not pass")
    return failures


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", choices=sorted(SUITES), default="action-lifecycle")
    parser.add_argument("--executor", choices=["claude", "codex"], default="codex")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--iteration", type=int, default=1)
    parser.add_argument("--print-command", action="store_true")
    args = parser.parse_args(argv)

    names = SUITES[args.suite]
    available = {item["name"] for item in json.loads(EVALS.read_text())["evals"]}
    missing = sorted(set(names) - available)
    if missing:
        raise SystemExit(f"action lifecycle evals are missing from evals.json: {missing}")
    skill_creator = resolve_skill_creator()
    command = [
        sys.executable,
        str(HARNESS),
        "--skill-creator-path",
        str(skill_creator),
        "--executor",
        args.executor,
        "--workers",
        str(args.workers),
        "--iteration",
        str(args.iteration),
        "--only",
        ",".join(names),
    ]
    if args.print_command:
        print(" ".join(command))
        return 0
    returncode = subprocess.run(command, cwd=ROOT, check=False).returncode
    if returncode:
        return returncode
    failures = failed_lifecycle_runs(
        ROOT / "dev/skill-workspace" / f"iteration-{args.iteration}",
        names,
    )
    if failures:
        print("action lifecycle did not pass:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
