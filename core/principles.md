# Foundational Principles

## Core Tenets

### 1. Ontology-Constrained Play

Scientific discovery in Gamma operates under explicit ontological constraints. Agents cannot claim arbitrary truths. All claims must conform to defined ontologies and evidence standards.

- Constraints are intentional, not limitations.
- Ontologies are documented in gamma-science.
- Violations are marked as invalid, never silently ignored.

### 2. Scientific Reliability

Truth is sacred. Processes that maintain truth integrity are non-negotiable.

- Receipts are mandatory for truth commits.
- Validation gates are not optional.
- Invalid states are quarantined, never overwritten.
- Audit trails are immutable.

### 3. No Idle Models

Agents should never wait passively. If truth is pending, agents continue provisional work clearly marked as provisional.

- Provisional work is labeled as such.
- Provisional work never mutates canon truth.
- When truth arrives, provisional work is reconciled.
- Agents default to useful work while waiting.

### 4. Patch-Dependent Evolution

When patches change truth state, all affected provisional work must be reconciled.

- Patches are versioned events.
- Patch impact is documented.
- Agents are notified of patches.
- Provisional work is marked stale if affected.

### 5. Never-Ending Game

Gamma has no win condition. The game continues indefinitely.

- Missions are episodic, not terminal.
- Patches change the game state.
- New evidence changes accepted canon.
- The system adapts but continues.

### 6. Decentralized Participation

Multiple agents and humans can participate across multiple repos.

- Inventory is isolated per agent.
- Work is coordinated via GitHub Project board.
- Handoffs are explicit.
- Conflicts are resolved via DELTA protocol.

### 7. Isolated Inventories

Each agent has exactly one writable workspace (inventory).

- Inventory is portable and resumable.
- Inventory is text-first.
- Inventory contains context, tasks, outputs, evidence, checkpoints.
- Writing outside inventory requires explicit authorization.

### 8. Text-First Persistence

All persistent state is text-based. No large binary artifacts.

- Markdown, JSON, CSV, code, config only.
- No generated images hoarded in repos.
- No serialized Python objects.
- Links to external artifacts are acceptable; embedding is not.

### 9. Receipt-Backed Truth

Truth cannot exist without receipts.

- Receipt is mandatory for any truth claim.
- Receipt includes timestamp, signer, validation checks.
- Receipt links to source run, mission, and provenance.
- Receipts are never deleted, only archived.

### 10. Minimal Core, Expandable Ecosystem

The core system (gamma + gamma-protocol) is kept minimal. Extensibility happens in science, analysis, and arena.

- Core logic is stable.
- Extensions add domains without breaking core.
- Dependencies are explicit.
- Minimal core makes truth gates auditable.

### 11. Frontend Does Not Invent Truth

The UI (gamma-arena) must never create truth.

- Arena reflects truth that exists in gamma backend.
- Arena can propose new missions or observations.
- Arena cannot mutate truth state.
- If arena shows an inconsistency, arena is wrong, not truth.

### 12. Backend Owns Truth-Bearing Gates

Only gamma backend can commit truth.

- gamma-protocol defines the rules.
- gamma-science validates evidence.
- gamma-analysis produces metrics.
- But gamma backend is the sole truth mutator.

## Anti-Patterns and Why They Are Dangerous

### Anti-Pattern: "The Model Said So, So It's True"

**Why dangerous**: Conflates Execution with Truth. Model outputs are proposals, never automatically truth.

**Consequence**: Stale, invalid, or contradictory claims become accepted without validation.

**Correct approach**: Model outputs → Evidence → Receipt → Truth.

### Anti-Pattern: "We'll Mark It As Truth, Validation Later"

**Why dangerous**: Creates invalid state that must later be quarantined, audit trail is broken.

**Consequence**: System cannot recover true history. Downstream work based on invalid truth fails silently.

**Correct approach**: Validate first, commit only valid state.

### Anti-Pattern: "The Dashboard Shows It, So It's Decided"

**Why dangerous**: Confuses Observation with Control or Truth. Dashboard reflects state; it doesn't create it.

**Consequence**: UI bugs become organizational decisions. External observers believe unvalidated claims.

**Correct approach**: Dashboard is output, not input.

### Anti-Pattern: "Update the Truth File Directly"

**Why dangerous**: Bypasses receipt gate, breaks audit trail, violates Receipt principle.

**Consequence**: Silent mutations, lost provenance, impossible to reconcile conflicts.

**Correct approach**: Only backend gates can mutate truth files.

### Anti-Pattern: "These Provisional Results Count Toward Next Level"

**Why dangerous**: Treats uncertain evidence as committed. If underlying truth changes, next level is invalid.

**Consequence**: Wasteful rework, compounding errors, false progression.

**Correct approach**: Provisional work is acknowledged as provisional. Progression depends on receipted truth only.

### Anti-Pattern: "No One's Using That, Let's Delete It"

**Why dangerous**: May be audit trail, may be needed for dispute resolution, may be historical record.

**Consequence**: Lost provenance, impossible to audit past decisions, can't replay history.

**Correct approach**: Archive instead of delete. Retain full history.

### Anti-Pattern: "Let's Bypass the Judge This Time"

**Why dangerous**: Judge validation exists to catch errors. Skipping it accumulates invalid state.

**Consequence**: Invalid truth commits, system loses coherence.

**Correct approach**: Judge validation is non-negotiable for truth commits.

### Anti-Pattern: "We'll Sort Out Permissions Later"

**Why dangerous**: Agents can write outside inventory, colliding with each other's work.

**Consequence**: Lost work, merge conflicts, overlapping mutations.

**Correct approach**: Inventory isolation from the start. Explicit handoffs for cross-inventory work.

---

© 2026 HNXJ(H.Nejat) / BASTOSLAB / VANDERBILT UNIVERSITY
