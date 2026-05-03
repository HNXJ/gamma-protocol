# GAMMA Protocol: Exact Execution

## Purpose

GAMMA is precise, scoped execution. You follow a detailed manifest and execute each step, producing evidence and a receipt.

GAMMA is where actual work happens.

## When to Use

- You have a detailed ALPHA plan or specification
- The task is well-defined with clear inputs and outputs
- You are ready to create artifacts, code, commits

## When NOT to Use

- The task is not yet clear (run ALPHA first)
- You don't know the current state (run BETA first)
- The task is a one-time massive refactor (use GAMMA-BURST instead)

## Input Contract

- Detailed specification or plan (from ALPHA)
- Manifest: ordered list of actions
- Acceptance criteria
- Receipt template

## Output Contract

- Completed work
- Receipt documenting execution
- Evidence package
- All artifacts committed and pushed
- Final report

## Required Evidence

- All commits are made with clear messages
- All tests pass or blockers are documented
- All outputs are verified
- Receipt is complete and signed
- No secrets in any committed file

## Forbidden Actions

- Ignore failures silently
- Skip tests
- Commit secrets
- Deviate from plan without updating plan first
- Push untested code to production without approval

## Final Report Format

**GAMMA Execution Report: [Task Name]**

1. **Manifest Execution** - Each step: ✓ done / ⚠ warning / ✗ failed
2. **Commits** - List of all commits with SHAs
3. **Evidence** - Links to produced artifacts
4. **Receipt** - Receipt document
5. **Validation Results** - Tests passed, checks passed
6. **Issues Encountered** - Problems and resolutions
7. **Deviations** - Any changes to the plan and why

---

© 2026 HNXJ(H.Nejat) / BASTOSLAB / VANDERBILT UNIVERSITY
