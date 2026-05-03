# Gamma

## One-sentence definition
Gamma is a protocolized scientific discovery game where LLM agents act under bounded harnesses, execute missions, emit receipts, and change truth only through validated backend gates.

## What Gamma is

**The Core Concept**:
> Gamma is the engine. Gamma Protocol is the law. Gamma Arena is the world. Harnesses are equipment. Missions are quests. Receipts are proof.

The core equation of Gamma is:
**agent identity + harness + mission + validator + receipt + observation**

## Core repos
The Gamma system is distributed across three primary repositories, each with a distinct and non-overlapping role:

| Repo | Role | Owns | Must not own |
| :--- | :--- | :--- | :--- |
| **gamma-protocol** | Protocol Layer | Schemas, harnesses, missions, receipts, doctrine, scientific evaluation contracts. | Live runtime state, UI rendering code, heavy engine logic. |

## Non-core resource repos
The following repositories are utilized as resources, tools, or publication surfaces but are not core game-engine components:
- **glllm-gemdev**: Reference source for MLLM scientific evaluation pipelines.
- **jbiophysic**: Scientific and biophysical research library.
- **hnxj.github.io**: Public publishing and observation surface for project visibility.

## Four-plane doctrine
To maintain system integrity, Gamma operates under a strict four-plane doctrine:
1. **Control**: Proposal and planning of activities.
2. **Execution**: The actual performance of tasks by agents within harnesses.
3. **Truth**: The validated, receipt-backed state committed to the backend.
4. **Observation**: Reports, visualizations, and UI representations of the state.


## Current truth discipline
Truth in Gamma is a privileged state:
- Truth is not whatever the UI shows.
- Truth is not whatever a model says.
- Truth is not whatever a local artifact claims.
- Truth requires **validated backend execution and receipts**.

**Recovery State Note**:
- Ghost N=12 was invalidated as a smoke-test corruption.
- Receipt-backed local truth was recovered to N=11.
- Runtime restart is a separate event from truth recovery.
- All future truth claims must explicitly cite verifiable receipts.

## Player model
Gamma utilizes a structured participant model:
- **1 Judge**: The final arbiter of mission success and protocol compliance.
- **4 Flexible Players**: Agents with distinct identities and capabilities.

**Players** are persistent identities. **Harnesses** define temporary capability contracts. **Missions** define specific tasks. **Receipts** record the empirical history of what actually occurred.

## Harnesses
A **harness** is a bounded capability contract. It specifies the tools an agent can use, the repositories it can access, forbidden side effects, expected output schemas, validation criteria, and receipt requirements.

- Harnesses may appear as **gear/loadout** in the Gamma Arena UI.
- The backend and protocol canonical term is always "harness."
- Harness selection is governed by the Control plane.

### Examples:
- **Scientific Evaluation Harness: HPC** (Primary target)
- **Backend Programmer Harness** (Deferred)
- **Frontend Observation Harness** (Deferred)
- **Browser Validation Harness** (Deferred)

## Scientific Evaluation Harness
The Scientific Evaluation Harness enables a merged evaluation capability including:
- Glossary and factors
- Contexts and study metadata
- Scoring rules and null vs. zero distinction
- Prompt provenance and reasoning logs
- CSV/JSONL/table outputs
- Validation and observation artifacts

**Constraint**: Scientific evaluation outputs are model-rated evidence maps, not biological truth commits.

## Ontology Tournament: HPC
An **Ontology Tournament** is an observation-plane scientific event. In the HPC tournament, the Council evaluates predictive-processing literature against the HPC ontology.

- **Terminology**: ontology-constrained model evaluations, model-rated evidence support, council-scored evidence space.
- **Classification**: Observation-plane scientific event.
- **Avoid**: Claims of "proved," "confirmed truth," or "biological truth." Substrate truth remains unchanged by tournament results.

## Minimal architecture
`gamma-protocol` defines legal contracts
↓
`gamma` executes contracts and commits truth
↓

## What must never happen
- The frontend invents truth.
- The public UI exposes operator controls.
- Model-rated scores mutate substrate truth.
- A PASS is declared without simulation execution and validation.
- Smoke tests write to canonical truth paths.
- Receipts are bypassed.
- Stale artifacts are treated as committed state.

## Missions
- **[Continuous Growth (N → N+1)](missions/continuous_growth.md)**: The prime mission for neural substrate expansion.

## Near-term roadmap
1. [x] Create [Global Doctrine](GLOBAL_GAMMA.md).
2. [x] Define [Continuous Growth Mission](missions/continuous_growth.md).
3. Create minimal harness schema.

## Contributor / agent rules
- Use cheap agents (e.g., standard models) for grep/search.
- Use **Claude-cowork** for critique and REVISE/REJECT gates.
- Use **Claude-code** for scoped high-quality edits.
- Use **Gemini back agents** for backend truth/receipts/runtime.
- Use **Antigravity** for frontend/browser validation.
- Use **GPT-gamma** for prompt orchestration and doctrine.

## License / status
**Status**: Active research prototype.
**License**: See repository license if present.
