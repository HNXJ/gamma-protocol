# Four-Plane Architecture

Gamma enforces a strict separation of concerns across four distinct planes to ensure scientific integrity and operational stability.

## 1. Control Plane
- **Role:** Governance, planning, and policy.
- **Artifacts:** Missions, quests, patches, rules, and scoring rubrics.
- **Repository:** \`gamma-protocol\`.

## 2. Execution Plane
- **Role:** Actualization of actions and simulations.
- **Artifacts:** Execution logs, intermediate artifacts, and raw outputs.
- **Repository:** \`gamma\` (runtime).

## 3. Truth Plane
- **Role:** Persistent, verified world state.
- **Artifacts:** Receipts, committed patches, and verified evidence maps.
- **Repository:** \`gamma\` (backend storage/persistence).

## 4. Observation Plane
- **Role:** Presentation and spectator feedback.
- **Artifacts:** Dashboards, visualizations, and public reports.
- **Repository:** \`gamma-arena\` (UI).

