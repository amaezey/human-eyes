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
    if len(finding_sets[-1]) > len(finding_sets[0]):
        return {"passed": False, "reason": "required-finding count increased"}
    return {
        "passed": not finding_sets[-1],
        "reason": "clean" if not finding_sets[-1] else "required findings remain",
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
    return subprocess.run(command, cwd=ROOT, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
