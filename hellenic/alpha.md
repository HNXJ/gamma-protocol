# ALPHA Protocol: Planning and Architecture

## Purpose

ALPHA is design and planning. You take a problem and produce a detailed solution architecture, decomposition plan, and task list.

ALPHA output feeds directly into GAMMA execution.

## When to Use

- Before implementing a complex feature
- Designing a multi-repo change
- Breaking down an ambiguous task
- Planning a refactor

## When NOT to Use

- Simple, single-file fixes (go straight to GAMMA)
- BETA hasn't been run yet (run BETA first to ground)
- You already have a detailed plan (skip to GAMMA)

## Input Contract

- Problem statement or task description
- Scope and constraints
- Known limitations or blockers
- Stakeholders and decision-makers

## Output Contract

- Architecture design document
- Task decomposition with estimated effort
- Risk identification and mitigation
- Dependency graph
- Recommended protocol sequence

## Required Evidence

- All design decisions justified
- All risks identified
- All dependencies called out
- All assumptions listed
- No implementation details that belong in GAMMA

## Forbidden Actions

- Do not implement code
- Do not create branches
- Do not commit changes
- Do not assume you know everything (if uncertain, add to Risk section)

## Final Report Format

**ALPHA Plan: [Feature/System Name]**

1. **Problem** - What are we solving
2. **Constraints** - Limitations we must respect
3. **Architecture** - Overall design
4. **Task Decomposition** - Ordered list of work items with effort estimates
5. **Risks** - What could go wrong and mitigations
6. **Dependencies** - What must happen before what
7. **Decision Points** - Where human input is needed
8. **Recommended Sequence** - BETA→ALPHA→GAMMA→THETA or alternate flow

---

© 2026 HNXJ(H.Nejat) / BASTOSLAB / VANDERBILT UNIVERSITY
