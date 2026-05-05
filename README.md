# Gamma Protocol

## Role in Gamma Labyrinth
Markdown-only Control/Doctrine authority; no runtime code or live schemas.

## Plane Classification
Control/Doctrine Plane.

## Truth-Safety Note
`truth_mode: truth_safe_unverified`. This repository defines the rules for truth commitment but does not store scientific truth itself.

## Coordination
Refer to GitHub Project `gamma` for tasks and issues.

## Guidelines
Agents must verify branch/status before work.

## Ignore Rules
This repository ignores `.DS_Store`, `*.npy`, `*.mat`, and `*.html`.

---

"Protocol is not truth. Protocol defines how truth may be committed."

## 1. What Gamma Protocol Is
Gamma Protocol is the canonical doctrine and governance layer for the Gamma scientific discovery game. It defines the rules, agent contracts, validation expectations, and the structural boundaries of the Gamma universe. It serves as the legal and logical framework that ensures scientific integrity through receipt-backed transitions and strict plane separation.

## 2. What Gamma Protocol Is Not
This repository is **not** a runtime environment. It does **not** contain executable solvers, UI code, active truth state, or scientific results. It is a Markdown-only specification. Any code found within the Gamma ecosystem belongs in the dedicated execution or observation repos.

## 3. Gamma Arena Goal
Gamma Arena is an open-world online scientific discovery game where humans and AI agents propose, test, audit, falsify, and expand mechanistic scientific worlds.
- **AI-Accelerated Scientific Discovery:** Utilizing agentic systems to traverse the massive hypothesis space of modern science.
- **Neuroscience-First:** The initial domain focus is biophysical neuron/circuit modeling and predictive coding evidence maps.
- **Open-World Game:** A persistent environment where scientific progress is achieved through competitive and collaborative gameplay.
- **Game-Theoretic Governance:** Treating discovery as a repeated game among bounded agents with formal payoff surfaces and falsification discipline.

## 4. The Four Planes
Gamma enforces a strict separation of concerns across four planes:
- **Control Plane:** Missions, quests, patches, rules, gates, and scoring. (Housed in \`gamma-protocol\`)
- **Execution Plane:** Bounded runs, simulations, and solver attempts. (Housed in \`gamma\`)
- **Truth Plane:** Receipt-backed committed state only. (Housed in \`gamma\` backend storage)
- **Observation Plane:** Dashboards, reports, and spectator views. (Housed in \`gamma-arena\` and public pages)

## 5. Player / Harness Separation
A central tenet of Gamma is the separation between the player (the actor) and the harness (the environment).
- **Players:** Propose hypotheses, missions, and actions. They can be humans, LLMs, or specialized agents.
- **Harnesses:** Define legal tools, timeouts, and validation gates. They prevent players from changing the conditions of their own success.
*"A player may propose a move; only a harness-constrained, receipt-backed gate can make that move count."*

## 6. Quests, Patches, Scores, and Receipts
- **Quests:** Bounded action spaces for players to achieve specific scientific subgoals.
- **Patches:** Proposed changes to the scientific world state.
- **Scores:** Model-rated evaluations of progress (not truth).
- **Receipts:** Immutable evidence of moves actually made in the execution plane.

## 7. Game-Theoretic Scientific Governance
Gamma treats scientific discovery as a repeated game among bounded agents. This involves roles, incentives, anti-collusion controls, and formal scoring rubrics. Negative results and falsifiers are explicitly recorded as progress.

## 8. Neuroscience Claim Discipline
- Literature evidence maps are model-rated evidence, not biological truth.
- Simulation outputs are execution artifacts until committed through a truth gate.
- Null and zero are distinct in evidence maps.
- No assertion of current biological state is allowed within the protocol itself.

## 9. Hellenic Protocol Stack
The Hellenic stack defines the agentic workflow:
- **BETA:** Read-only audit and grounding.
- **ALPHA:** Supervised planning and decomposition.
- **GAMMA:** Exact execution manifest.
- **DELTA:** Conflict reconciliation.
- **THETA:** Post-execution validation / autopsy.
- **GAMMA-BURST:** Major doctrine or repository migrations.

## 10. Repository Boundaries
- **gamma-protocol:** Markdown doctrine, rules, and schemas.
- **gamma:** Backend runtime, orchestration, and truth gates.
- **gamma-arena:** Front-end dashboard and observation.
- **gamma-science:** Scientific source models and manuscripts.

## 11. Markdown-Only Repository Policy
This repository follows a strict Markdown-only policy. No executable code or packaging machinery is permitted. Only \`.md\`, \`.gitignore\`, and \`CODEOWNERS\` are exempt.

## 12. Required Agent Reading Order
1. \`README.md\`
2. \`doctrine/gamma_arena_doctrine.md\`
3. \`doctrine/four_plane_architecture.md\`
4. \`contracts/agent_contract.md\`
5. \`docs/glossary.md\`

## 13. Migration Status
The repository is currently undergoing a GAMMA-BURST migration to align with the v0.4 manuscript framing. See \`docs/migration_report.md\` for details.

## 14. Non-Truth Warning
Nothing in this repository constitutes validated biological truth. All scientific claims must be backed by receipts stored in the truth plane.

© 2026 HNXJ(H.Nejat) / BASTOSLAB / VANDERBILT UNIVERSITY

## Coordination

This repository follows the [GAMMA-BUS Coordination Doctrine](GEMINI.md). Agents should refer to `GEMINI.md` for specific instructions and coordination rules.
