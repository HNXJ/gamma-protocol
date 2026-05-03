# GAMMA-BURST Protocol: Major Reconstruction

## Purpose

GAMMA-BURST is a one-time, large-scale refactor or reconstruction. It's a specialization of GAMMA designed for massive, coordinated changes across multiple repos or systems.

Use GAMMA-BURST when the scope is so large that normal GAMMA + THETA isn't sufficient.

## When to Use

- Reconstructing an entire subsystem
- Multi-repo refactor affecting core logic
- Breaking changes to protocol or schema
- System-wide architectural changes

## When NOT to Use

- Small, scoped changes (use GAMMA)
- Simple bug fixes (use GAMMA)
- Incremental improvements (use GAMMA)

## Input Contract

**Everything GAMMA requires, PLUS:**

- Preflight BETA audit (mandatory)
- Rollback point identified (commit SHA or checkpoint)
- Exact file manifest with expected changes
- Risk assessment
- Communication plan

## Output Contract

**Everything GAMMA produces, PLUS:**

- Pre-execution BETA report
- Exact file manifest with actual changes
- Post-execution THETA validation
- Final diff summary
- Rollback instructions

## Required Evidence (Mandatory Checklist)

- [ ] BETA preflight completed and documented
- [ ] Rollback point identified
- [ ] File manifest created (before execution)
- [ ] All dependencies resolved
- [ ] Communication sent to affected teams
- [ ] Backup created or snapshot taken
- [ ] Execution completed
- [ ] THETA validation completed
- [ ] All commits are documented
- [ ] Final manifest matches actual changes
- [ ] Diff summary reviewed
- [ ] Tests pass or blockers documented

## Forbidden Actions

- Skip BETA preflight
- Lose rollback point
- Deviate from manifest without updating it
- Skip THETA validation
- Leave things in partial state

## Pre-Execution Checklist

1. **Preflight BETA**
   - Current state audited
   - Risks identified
   - Dependencies mapped
   - All affected systems known

2. **Rollback Plan**
   - Rollback point identified and verified
   - Rollback procedure documented
   - Rollback tested (if possible)

3. **Manifest**
   - List all files to be created
   - List all files to be modified
   - List all files to be deleted
   - For each: expected changes

4. **Communication**
   - Teams notified
   - Blockers identified
   - Decision-makers aligned

## Execution Phase

Follow standard GAMMA with extra care:
- Commit frequently
- Document each major step
- Stop and escalate if manifest deviates significantly
- Do not skip checkpoints

## Post-Execution Validation (THETA)

1. **Final Manifest**
   - Compare expected vs. actual
   - Account for any deviations
   - Document changes to plan

2. **Diff Summary**
   - Generate complete diff
   - Review for unexpected changes
   - Check for secrets or artifacts
   - Validate against original manifest

3. **Full Test Suite**
   - All tests pass or explicitly documented
   - No regressions in unrelated systems
   - Performance impact assessed

4. **Sign-Off**
   - THETA validator confirms everything
   - Judge approves major change
   - Communication sent to affected teams

## Final Report Format

**GAMMA-BURST Report: [System Name]**

1. **Preflight BETA Summary** - Key findings
2. **Rollback Point** - Commit SHA + instructions
3. **Expected Manifest** - Files to be created/modified/deleted
4. **Execution Summary** - Steps taken, deviations from plan
5. **Commits** - All commit SHAs in order
6. **Actual Manifest** - What was actually created/modified/deleted
7. **Diff Summary** - Overall changes, grouped by impact
8. **THETA Validation** - Complete sign-off
9. **Risks Mitigated** - How preflight risks were addressed
10. **Lessons Learned** - What to do better next time

---

© 2026 HNXJ(H.Nejat) / BASTOSLAB / VANDERBILT UNIVERSITY
