# DELTA Protocol: Conflict Resolution and Reconciliation

## Purpose

DELTA resolves conflicts. When two claims contradict, when patches invalidate work, when stale state is detected, DELTA reconciles and makes truth whole again.

## When to Use

- Two agents claim different truth
- A patch invalidates provisional work
- Evidence contradicts canonical truth
- Claims are STALE, DISPUTED, or LOCAL_ONLY
- Merge conflicts exist that aren't trivial

## When NOT to Use

- No conflict exists
- Conflict is simple and agent-resolvable (resolve locally, then DELTA to document)

## Input Contract

- Conflicting claims with evidence
- Timestamps and sources
- Current state snapshots
- Patch details (if applicable)

## Output Contract

- Reconciliation decision
- Claim classification table (VERIFIED / DISPUTED / STALE / LOCAL_ONLY / NEEDS_BACKEND_RECEIPT / NEEDS_BROWSER_VALIDATION)
- Guidance on next steps
- If needed: escalation to human decision-maker

## Required Evidence

- All conflicting sources cited
- Timestamps for each claim
- Logic explaining the decision

## Forbidden Actions

- Ignore conflicts
- Declare one side "obviously right" without evidence
- Modify claims without acknowledgment
- Hide conflicts; always surface them

## Claim Classification Table

| Class | Definition | Resolution |
|---|---|---|
| VERIFIED | Multiple independent sources confirm | Declared truth |
| DISPUTED | Sources disagree, evidence inconclusive | Escalate to judge |
| STALE | Was true, now invalidated by patch | Mark stale, do not use |
| LOCAL_ONLY | Only exists in one agent's inventory | Propose for canon if others agree |
| NEEDS_BACKEND_RECEIPT | Claim requires backend validation | Request receipt from gamma backend |
| NEEDS_BROWSER_VALIDATION | Claim is about UI state | Validate via gamma-arena browser test |

## Final Report Format

**DELTA Reconciliation: [Conflict Name]**

1. **Conflicting Claims** - What claims contradict
2. **Evidence for Each** - Sources and timestamps
3. **Timeline** - When each claim was made
4. **Analysis** - Why they conflict
5. **Claim Classification** - Table showing each claim's status
6. **Decision** - Which is truth (or escalation reason)
7. **Action Items** - What happens next
8. **Acknowledgments** - Document that conflict was addressed

---

© 2026 HNXJ(H.Nejat) / BASTOSLAB / VANDERBILT UNIVERSITY
