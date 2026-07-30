# human-eyes

Claude Code skill for auditing and rewriting prose that carries common AI-writing tells.

## Tooling safety

- When the active agent is Codex, Codex must never invoke `claude`, the Claude Code CLI, the Anthropic API, or any Claude-backed agent or review workflow unless the user's current message expressly permits Codex to use Claude for that exact task. A request to evaluate, review, test, or run `/human-eyes` does not give Codex permission to use Claude. Codex must ask first and wait for the answer. This restriction applies to Codex using Claude; it is not a restriction on Claude itself.
- Never execute `/opt/homebrew/bin/rg` in this repository. That binary carries macOS provenance metadata and repeatedly triggers a blocking Gatekeeper dialog stating that Apple cannot verify `rg` is free of malware.
- Agents and review workflows are allowed. They must not execute `/opt/homebrew/bin/rg`.
- When using another agent in this repository, explicitly instruct it to use `grep`, `find`, Python file traversal, or `git grep` instead of `rg`.
- Do not ask the user to approve, open, or remove the quarantined binary as part of ordinary repository work. Avoid it.

## Git closeout and worktree visibility

- `git push` updates the remote branch only. It does not update other local checkouts, worktrees, or running agent sessions. Do not imply Claude, Codex, or another agent will see pushed or merged changes until that checkout fetches, pulls, or is otherwise updated.
- After any push or merge, run `git status --short --branch` in the checkout you changed and report the branch, cleanliness, and upstream state.
- After a PR merge, explicitly say whether this checkout was updated to the merge commit.
- If Claude or another agent is expected to continue in a different checkout, update that named checkout only when it is clean and safe to fast-forward. If it is dirty, detached, or on another branch, report that instead of changing it.
- When a different checkout needs manual sync, give the exact commands:

```bash
git fetch --prune
git switch main
git pull --ff-only
```

- Never rely on the remote merge alone as proof that local Claude/Codex sessions have the new files. Worktrees are separate local filesystems.
