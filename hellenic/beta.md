# BETA Protocol: Audit, Ground, Risk Discovery

## Purpose

BETA is read-only discovery. You enter a system unfamiliar to you and audit:
- Current state
- What is working
- What is broken
- What are the risks
- What is the ground truth

BETA produces a grounding document that serves as the foundation for ALPHA planning.

## When to Use

- Starting work in an unfamiliar codebase or system
- Investigating a reported bug or issue
- Understanding current project state before proposing changes
- Discovering failure modes or risks

## When NOT to Use

- You already understand the system fully
- The task is simple and well-specified
- You have an emergency that requires immediate action (jump to GAMMA with caution)

## Input Contract

What must be provided before starting BETA:

- Task description or question to answer
- Scope boundaries (which repos, systems, files are in-scope)
- What information is needed to answer the question

## Output Contract

What BETA produces:

- Current State Report: factual description of what exists
- Risk Report: identified risks, missing pieces, inconsistencies
- Grounding Document: what you learned, what is true
- Next Steps Recommendation: what to do next (ALPHA, more BETA, escalate, etc.)

## Required Evidence

What constitutes acceptable BETA completion:

- All claims are sourced (file paths, line numbers, URLs)
- All findings are factual (what is, not what should be)
- No changes made to the system
- Read-only access only
- Clear distinction between facts and hypotheses

## Forbidden Actions

Do not:
- Modify any files
- Run destructive commands
- Make assumptions without verification
- Create branches or commits
- Change configuration

## Final Report Format

**BETA Report: [System Name]**

1. **Current State** - What is actually there
2. **Working Well** - What is functioning
3. **Problems Found** - Issues and inconsistencies
4. **Risks Identified** - Potential failure modes
5. **Knowledge Gaps** - What is unclear
6. **Grounding** - What is confirmed as true
7. **Next Steps** - Recommendation for next protocol

---

© 2026 HNXJ(H.Nejat) / BASTOSLAB / VANDERBILT UNIVERSITY
