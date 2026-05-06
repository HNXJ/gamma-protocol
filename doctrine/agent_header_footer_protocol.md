# Gamma Labyrinth Global Header/Footer Alignment Protocol

This protocol is mandatory for all Gamma Labyrinth agents to ensure machine-scannable identity and timing synchronization across the Control, Execution, Truth, and Observation planes.

## Mandatory Format
Every task report, handoff, issue comment, and durable worker log must begin with a header and end with a footer in this exact format:

`[model-llm-name][root-location][yyyymmdd-hhmm]`

---

## Field Specifications

### 1. `model-llm-name`
- Must be the actual runtime/model string reported by the harness or metadata.
- **Disambiguation Rule**: Front-end/Browser agents (Antigravity) must append `(antigravity)` to the model name to avoid confusion with CLI agents.
- **Example (CLI)**: `gemini-3.1-flash-lite`
- **Example (Antigravity)**: `gemini-3-flash (antigravity)`
- If unknown: `unknown_model_do_not_guess`

### 2. `root-location`
- Must be the active workspace root or repo root.
- Use normalized forward slashes.
- **Example**: `D:/workspace/gemini-gamma-labyrinth/repos/gamma`
- If unknown: `unknown_root_do_not_guess`

### 3. `yyyymmdd-hhmm`
- 4-digit year, 2-digit month, 2-digit day, hyphen, 24-hour hour, 2-digit minute.
- **Example**: `20260506-2358`

---

## Required Report Skeleton
Agents must structure their detailed reports between the header and footer using the following skeleton:

1. **Agent/model/host**
2. **Repo/workspace**
3. **Plane**
4. **Task status**: PASS / PARTIAL / STOP / BLOCKED
5. **Files changed**, if any
6. **Commands run**, if any
7. **Validation evidence**
8. **Truth status** (`truth_mode: truth_safe_unverified` default)
9. **What was not done**
10. **Remaining blockers**
11. **Next single safe action**

---

## Doctrine Context
Reports, transcripts, and model outputs are not biological Truth-plane state. No secrets (tokens, keys, passwords) are permitted in headers, footers, or reports.

---
*Last Updated: 20260506-1230*
