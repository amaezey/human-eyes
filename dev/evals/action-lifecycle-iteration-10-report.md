# Action lifecycle iteration 10

Date: 2026-07-12

Source artefacts: `dev/skill-workspace/iteration-10/`

The repaired harness ran eight skill-guided LLM executions and then graded each transcript and final response in a separate fresh grader context using Skill Creator's supplied `agents/grader.md` instructions. All eight executors and all eight graders completed.

Result: 13/17 assertions passed. Skill Creator reports 77.1% because it averages the eight case pass rates; the direct assertion rate is 76.5%. Five cases passed completely.

| Case | Result | Grader finding |
|---|---:|---|
| Full Audit coverage | 2/2 | All 15 semantic records were completed; no authorship inference. |
| Surface-only action gate | 2/2 | Explicitly labelled incomplete and refused Suggestions. |
| Suggestion validation | 0/2 | No replacement-specific context audits were run. One suggestion introduced the unsupported definite description `the day's main commitment`. |
| Rewrite audit rebinding | 2/2 | Separate source and rewrite bundles/Audits; meaning and qualifications preserved. |
| Fresh Write and Audit | 1/2 | Complete 49+15 Audit, but invented numerous operational facts absent from the brief. |
| Three-pass residual reporting | 2/2 | Exactly three revision passes; remaining contextual curly-quote finding disclosed. |
| Installed-path resolution | 2/2 | Complete Audit ran outside the repository using absolute installed-skill paths. |
| Revision convergence | 2/3 | Required finding sets decreased on every pass and stopped at three; direct quotations were removed or paraphrased. |

## Confirmed failures

1. Suggestions are returned without the context re-audit required by the skill. This is a workflow failure, not merely an undesirable replacement.
2. Suggestion generation can introduce the same class of unsupported definite description it was explicitly told to reject.
3. Write can pass a complete deterministic and semantic Audit while inventing unsupported process facts. The Audit is not currently enforcing brief fidelity.
4. Rewrite convergence can improve finding sets while deleting protected quotations. Decreasing finding counts do not establish meaning preservation.

## Focused fixes and reruns

The skill completion protocol was hardened without changing the assertions:

- Suggestions now require the complete original surrounding paragraph, one replacement per context, a fresh bundle, a genuine 15-record semantic reading, a successful Audit, and exact agreement between audited and returned wording. Blanket all-clear semantic answers and collaged fragments are explicitly invalid.
- Write treats the brief as a closed factual source and removes plausible workflow detail that the brief did not supply.
- Rewrite protects complete qualified factual sentences, treats the source as a closed factual record, and forbids Audit commentary inside rewritten prose.
- The Claude adapter now retains its stream transcript so independent graders can verify tool use and intermediate Audits.

Focused independently graded results:

| Iteration | Executor | Case | Result |
|---|---|---|---:|
| 11 | Codex | Write | 2/2 |
| 11 | Codex | Suggestions | 1/2; returned wording clean, but context validation used fragments/collages and fabricated all-clear semantic answers |
| 11 | Codex | Convergence | 2/3; quotations survived, but factual modality and source stance changed |
| 12 | Claude | Convergence after preservation hardening | 3/3 |
| 13 | Claude | Suggestions after validation and transcript hardening | 2/2 |

Iteration 13's grader verified 46 replacement cases. Each used the complete surrounding paragraph, a fresh preflight and bundle, all 15 semantic records, and a successful Audit; the grader also independently scanned the returned replacements for the prohibited constructions.

The three iteration-10 failures have therefore passed focused reruns. A same-model full Codex rerun remains useful after its external usage window resets; the focused Claude results are additional cross-model evidence, not a claim that model variance is eliminated.

## Harness correction

The previous lifecycle runner never graded qualitative assertions. It hard-coded every non-programmatic assertion to `passed: false`, then aggregated those placeholders as a 0% product result. Iteration 10 restores the intended Skill Creator grading stage. Ungraded qualitative assertions now raise a grader error; they can no longer silently become product failures.
