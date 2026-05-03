# The Five-Repo Ecosystem: Boundaries and Ownership

## Repository Matrix

| Repo | Primary Owner | Role | In-Scope Contents | Out-of-Scope Contents |
|---|---|---|---|---|
| `gamma` | Backend team | Runtime execution, truth gates, solver, adapter, receipt validation | Runtime code, solver logic, truth-bearing adapters, valid receipt checkers, backend state persistence | UI code, protocol doctrine, scientific validation logic, analysis scripts, frontend |
| `gamma-protocol` | Doctrine team | Law and governance layer | Schemas, missions, harnesses, protocols, doctrine, rules, governance | Runtime code, UI, secrets, hardcoded truth claims, binary artifacts |
| `gamma-arena` | Frontend team | Observation and player interface | UI, dashboards, player cards, visualizations, agent coordination UI | Backend logic, truth gates, hardcoded scientific claims, execution engine |
| `gamma-science` | Science team | Scientific validity and canon | Citations, evidence standards, reproducibility criteria, claim acceptance norms, validity matrices | Runtime execution, UI rendering, backend persistence, analysis algorithms, general governance |
| `gamma-analysis` | Analysis team | Quantitative methods and metrics | Statistical methods, metrics definitions, evaluation pipelines, algorithms, uncertainty quantification | Truth plane state, UI claims, backend logic, governance doctrine, scientific claim authority |

## Detailed Boundaries

### gamma (Backend Engine)

**Role**: The timeless kernel. Executes missions, validates truth, gates receipts.

**Must contain**:
- Runtime execution logic
- Solver and adapter implementations
- Receipt validators
- Truth-bearing gates
- Persistence layer
- Logging and audit trails

**Must not contain**:
- UI or frontend code
- Protocol doctrine (doctrinal comments ok, not doctrine files)
- Secrets or API keys (use environment variables only)
- Hardcoded scientific state
- Analysis scripts

**When a developer says "I need to...":
| Developer says | Correct repo | Why |
|---|---|---|
| "I need to add a new solver method" | gamma | Runtime logic |
| "I need to validate receipts differently" | gamma | Truth gate |
| "I need to add a dashboard for solver status" | gamma-arena | UI is not backend |
| "I need to define what makes a valid receipt" | gamma-protocol | Doctrine layer |
| "I need to run evaluation metrics" | gamma-analysis | Metrics belong to analysis |

### gamma-protocol (Law Layer)

**Role**: Written operating law. All rules, schemas, contracts, missions.

**Must contain**:
- Mission specifications
- Harness contracts
- Hellenic protocols
- Governance rules
- Schema definitions
- Doctrine and principles
- Templates for standardized artifacts

**Must not contain**:
- Runtime code (beyond existing forge utility)
- UI code
- Secrets or API keys
- Hardcoded truth values
- Binary files or generated images
- Vague placeholders

**Example correct content**:
- `missions/continuous_growth.md` - mission spec with placeholder for N
- `templates/receipt_template.md` - standardized receipt form
- `hellenic/gamma.md` - protocol for exact execution
- `agents/permissions.md` - role-based capability definitions

### gamma-arena (Frontend World)

**Role**: Observation surface. What players see. Game UI.

**Must contain**:
- React/Vue/frontend components
- Dashboard pages
- Agent/player cards
- Mission tracking UI
- Visualization code

**Must not contain**:
- Backend execution logic
- Truth validation gates
- Scientific evaluation logic
- Raw solver code

**Invariant**: Arena reflects truth, does not create it.

### gamma-science (Scientific Validity)

**Role**: Scientific canon and evidence standards. What counts as valid evidence.

**Must contain**:
- Citation collections
- Evidence standards
- Reproducibility criteria
- Scientific claim acceptance norms
- Validity matrices
- Reference material
- Literature reviews

**Must not contain**:
- Runtime execution code
- UI or frontend code
- Secrets
- General project governance (belongs in gamma-protocol)
- Truth mutations

**Example**: "For a claim about neural efficiency to be accepted, it must cite peer-reviewed literature and pass these reproducibility checks: [list]."

### gamma-analysis (Quantitative Methods)

**Role**: How to measure, evaluate, compare. Metrics and statistical logic.

**Must contain**:
- Statistical methods documentation
- Metric definitions
- Evaluation pipelines
- Algorithms for analysis
- Uncertainty quantification methods
- Benchmark designs
- Data processing logic

**Must not contain**:
- Committed truth state
- UI claims
- Backend persistence logic
- General governance

**Example**: "Tokens Per Second (TPS) is calculated as output_tokens / duration_seconds. Uncertainty is [formula]. When TPS varies more than 10%, flag as anomalous."

## Cross-Repo Handoff Rules

### gamma → gamma-protocol
**Direction**: "We need a new contract for this mission."

**Trigger**: Backend wants to document a new capability or constrain an agent.

**Output**: gamma-protocol adds mission spec or updates harness schema.

### gamma-protocol → gamma
**Direction**: "This mission is now specified. Implement the truth-bearing logic."

**Trigger**: Mission is fully specified, ready for backend implementation.

**Output**: gamma adds runtime support, receipt validator, or truth gate.

### gamma-arena → gamma-protocol
**Direction**: "Players need this capability. Update the mission spec."

**Trigger**: UI designers want to offer a new player action.

**Output**: gamma-protocol documents the new mission, harness, or rule.

### gamma-science → gamma-protocol
**Direction**: "Scientific evidence standards updated. Update acceptance criteria."

**Trigger**: New evidence standards or validity rules established.

**Output**: gamma-protocol updates evidence acceptance norms.

### gamma-analysis → gamma-protocol
**Direction**: "Metric defined. Add to evaluation template."

**Trigger**: New metric is scientifically sound, standardized.

**Output**: gamma-protocol adds metric to templates or mission specs.

## Conflict Resolution

If two repos claim ownership of a piece of work:

1. **Consult core/planes.md**: What plane does the work touch?
2. **Consult repo roles**: Which repo owns that plane?
3. **If still ambiguous, escalate**: Use DELTA protocol in gamma-protocol/hellenic/delta.md.

---

© 2026 HNXJ(H.Nejat) / BASTOSLAB / VANDERBILT UNIVERSITY
