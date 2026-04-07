# GAMMA: Guided Agentic Model-Mediated Actions

**agent-source**: gemini-cli
**agent-target**: all-any
**mode**: documentation

## 🤖 For Agents
This protocol mandates high-fidelity agentic action traces. Before execution, agents MUST declare the **GAMMA Mode** (`scientific` or `debugging`). Always maintain strict Problem-Solution Chains (PSC), documenting the 'why' before the 'how'. Ensure every directive is autonomous, verifiable, and free of version suffixes. Map deterministic targets using unified schemas. Execute terminal actions with precision, registering every newly generated skill to the central ledger.

### 🧬 Skill vs. GAMMA: The Operational Distinction

| Feature | The Skill (e.g., `skills/`) | The GAMMA (e.g., `gamma.gamma`) |
| :--- | :--- | :--- |
| **Nature** | **Potential & Static**: A reusable, project-agnostic "How-To" guide or capability definition. | **Kinetic & Active**: A specific, verifiable trace of a real-world architectural delta. |
| **Persistence** | **Permanent Knowledge**: Resides in the agent's core toolbox for future use. | **Episodic Action**: Documents a single session's fix or implementation; it is a live history. |
| **Constraint** | **Rule of 3**: Only create if the pattern is expected to recur in 3+ unrelated contexts. | **Case-Specific**: Must mention the actual target artifact or issue being addressed. |
| **Objective** | **Enabling**: Focuses on increasing the agent's theoretical capacity. | **Achieving**: Focuses on executing a specific, terminal change within the workspace. |

## 🚀 Installation & Global Forge

The GAMMA Forge is the authoritative Python utility for generating standardized `.gamma` traces.

```bash
# Install via PyPI
pip install gamma-protocol

# Usage: Scientific Mode
gamma-forge --mode scientific --title "HPC Analysis" --problem "Inconsistent TPS" --solution "TPS Estimator" --scope "31 papers" --evidence "TPS Log"

# Usage: Debugging Mode
gamma-forge --mode debug --title "Fix SSH" --problem "SSH Timeout" --solution "Multiplexing" --repro "ssh -v" --patch "ControlMaster"
```

## 1. Problem-Solution Architecture (The "Why")

### 🧬 Scientific Mode (Research & Discovery)
For scientific reasoning, the PSC must establish an empirical basis:
- **Research Question/Claim**: The specific hypothesis or data query.
- **Corpus/Scope**: The papers, datasets, or codebases being inspected.
- **Method/Evidence**: The tool or logic used to extract or compare findings.
- **Uncertainty/Limitations**: Known gaps or confidence levels in the deduction.
- **Output Artifact**: The resulting Markdown, JSON, or visualization.

### 🛠 Debugging Mode (Fixes & Engineering)
For technical fixes, the PSC must ensure structural integrity:
- **Observed vs. Expected**: Clear description of the failure state and target state.
- **Reproduction**: Exact steps or script to trigger the error.
- **Root-Cause Hypothesis**: The underlying reason for the failure.
- **Patch Strategy**: The minimal-diff approach to resolve the issue.
- **Validation & Rollback**: Testing plan and risk assessment.

## 2. Skill Generation & Registration (The "Synaptic Gate")
Only reusable, project-agnostic capabilities become Skills. Every Skill MUST satisfy the **Kolmogorov-Proxy Constraints**:
1. **Cyclomatic Complexity (v(G)) <= 5**: Prevent deeply nested, spaghetti logic.
2. **AST Depth <= 4**: Force-prune logic into simple primitives.
3. **No Episodic Data**: Zero references to machine-specific paths or temporary project names.
4. **Registration**: Skills must be registered to the central ledger (e.g., `gemini.md`) to be visible to other agents.

## 3. Version Control & Finality
- **Non-Suffix**: No `_v2`, `_new`, `_final`. Always overwrite existing files.
- **Git Protocol**: Every GAMMA execution must end with a standard `Add -> Commit -> Push` audit trail.
- **Ledger Update**: Reflect the final state in the project's root `gemini.md` (or equivalent) to synchronize global context.

## 4. Rules, Cautions & Limitations
- **Verifiability**: An action is incomplete until its behavioral correctness is verified through automated tests or visual audit.
- **Portability**: No absolute paths (`/Users/...`). Resolve all paths dynamically or relative to the workspace root.
- **Scientific Integrity**: Citations must be verifiable. Never hallucinate data.
- **Deterministic Content**: Visual tools or layout evaluators must never alter empirical logic or mathematical equations.

---
*For the original story and design philosophy, see [docs/story.md](docs/story.md).*
