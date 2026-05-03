# The Four Planes: Architecture and Boundaries

## Overview

Gamma operates under strict four-plane architecture to maintain system integrity and clarity of purpose.

| Plane | Purpose | Allowed Artifacts | Forbidden | Truth-Bearing |
|---|---|---|---|---|
| **Control** | Missions, rules, proposals | Protocol docs, mission specs, governance | Runtime code, UI, truth commits | No |
| **Execution** | Agent runs, simulations, operations | Model outputs, logs, test results | Truth mutations, direct commits | No |
| **Truth** | Validated, receipt-backed state | Receipts, adapter-mediated commits | Proposals, unvalidated claims | **Yes** |
| **Observation** | Reports, dashboards, UI, visualization | Dashboards, UI pages, reports | Truth claims, backend logic | No |

## Critical Mandate

**Never confuse proposal, execution result, committed truth, and observation.**

## Plane Definitions

### Control Plane

**Purpose**: Where intentions become missions. Where rules are written and enforced.

**Owned by**: Protocol layer, project governance, mission designers.

**Contains**:
- Mission specifications
- Protocol doctrine
- Harness contracts
- Rules and governance
- GitHub Project items
- Proposals and plans

**Must never contain**:
- Runtime code execution
- Live truth state
- UI rendering logic
- Unvalidated truth claims

**Example artifacts**: `gameplay/missions.md`, `collaboration/github_project.md`, `templates/mission_template.md`

### Execution Plane

**Purpose**: Where agents work. Where simulations run. Where code executes.

**Owned by**: Agents, harnesses, runtime environments.

**Contains**:
- Model outputs
- Runtime logs
- Simulation results
- Agent traces
- Intermediate computations
- Evidence candidates

**Must never contain**:
- Truth mutations (only proposals)
- Backend committed state
- UI logic for observation

**Output classification**: Results are proposals until validated and receipted.

**Example artifacts**: Agent run logs, model outputs, evidence packages.

### Truth Plane

**Purpose**: Canonical committed state. The single source of ground truth.

**Owned by**: Backend, receipts, validation gates.

**Contains only**:
- Receipt-backed validated state
- Adapter-mediated commits
- Judge-signed decisions
- Canonical reference values

**Mutation rules**:
- Requires receipt
- Requires judge signature or backend gate
- Requires validation checks
- Requires full provenance

**Never contains**:
- Proposals
- Model-rated scores (unless receipted)
- Unvalidated claims
- Speculation

**Source of truth**: All truth queries must point to receipted state in the gamma backend.

### Observation Plane

**Purpose**: What humans and external systems see. Reports and dashboards.

**Owned by**: Frontend, UI, dashboards, public pages.

**Contains**:
- Dashboard visualizations
- Public reports
- UI state
- Summary pages
- Derived reports

**Must never contain**:
- Backend logic
- Truth mutations
- Operator controls visible to public
- Unvalidated claims presented as truth

**Relationship to truth**: Observation must accurately reflect truth, but observation itself is not truth.

## Artifact Classification Table

| Artifact Type | Plane | Truth-Bearing | Judge-Signable | Receipt-Backable |
|---|---|---|---|---|
| GitHub Project item | Control | No | No | No |
| GitHub Issue | Control | No | No | No |
| Pull Request | Control | No | No | No |
| Protocol document | Control | No | No | No |
| Dashboard text | Observation | No | No | No |
| UI dashboard | Observation | No | No | No |
| Model output | Execution | No | No | No |
| Runtime log | Execution | No | No | No |
| Agent trace | Execution | No | No | No |
| Receipt | Truth | **Yes** | **Yes** | **Yes** |
| Committed truth file | Truth | **Yes** | **Yes** | **Yes** |
| Judge report | Control/Truth | Conditional | **Yes** | **Yes** |
| Scientific claim (unreceipted) | Proposal | No | No | No |
| Evidence package | Execution | No | No | Can be |
| Tournament result | Observation | No | No | No |

## Cross-Plane Boundary Rules

### Control → Execution
- Control plane can specify missions.
- Control cannot inspect or veto live execution results.
- Execution reports back to Control for status updates.

### Execution → Truth
- Execution produces evidence.
- Evidence becomes truth only via receipt validation.
- Unvalidated execution outputs are proposals, never truth.

### Truth → Observation
- Truth must flow into observation.
- Observation displays truth, but may also display proposals (clearly marked).
- Observation cannot contradict truth.

### Observation → Control
- Observation can inform policy updates.
- User feedback from observation may trigger new Control-plane missions.
- But observation itself cannot mutate truth.

## Failure Modes

### Confusing Execution with Truth
**Danger**: Claiming a model output is canonical truth without receipt.

**Correct pattern**:
1. Model produces output (Execution plane).
2. Output becomes evidence (Execution → Observation).
3. Receipt validates output (Execution → Truth).
4. Only then is it canonical truth (Truth plane).

### Frontend Inventing Truth
**Danger**: Dashboard shows a value, and that value becomes accepted as truth.

**Correct pattern**:
- Dashboard (Observation) displays what is in Truth plane.
- Dashboard never creates truth; it reflects it.
- If dashboard shows a value not in Truth plane, it's a dashboard bug, not a truth commit.

### Bypassing Receipts
**Danger**: Declaring truth without validation gate.

**Correct pattern**:
- No truth commit without receipt.
- Receipt must be signed or backed by backend gate.
- Receipt must include validation checks.

### Stale Artifacts as Current State
**Danger**: Treating an old output file as current truth.

**Correct pattern**:
- Truth queries point to current Truth plane state.
- Archives of old truth are labeled as historical.
- Current != historical; maintain clear version markers.

## Judge Report Relationship

Judge reports are **Control-plane artifacts that can propose Truth-plane mutations**.

- Judge report is not automatically truth.
- Judge report + PASS decision + valid receipt = authorization to commit truth.
- Judge report is evaluated in Control plane.
- Receipt is executed in Truth plane.

---

© 2026 HNXJ(H.Nejat) / BASTOSLAB / VANDERBILT UNIVERSITY
