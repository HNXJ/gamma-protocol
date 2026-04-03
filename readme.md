# GAMMA: Guided Agentic Model-Mediated Actions

**agent-source**: gemini-cli
**agent-target**: any

## 🤖 For Agents
This protocol mandates high-fidelity agentic action traces. Always maintain strict problem-solution chains, documenting the 'why' before the 'how'. Ensure every directive is autonomous, verifiable, and free of version suffixes. Map deterministic targets using unified schemas. Execute terminal actions with precision, registering every newly generated skill to the central ledger.

### 🧬 Skill vs. GAMMA: The Operational Distinction

| Feature | The Skill (e.g., `skills/`) | The GAMMA (e.g., `gamma.gamma`) |
| :--- | :--- | :--- |
| **Nature** | **Potential & Static**: A reusable "How-To" guide or capability definition. | **Kinetic & Active**: A specific, verifiable trace of a real-world architectural delta. |
| **Persistence** | **Permanent Knowledge**: Once registered, it resides in the agent's core toolbox for future use. | **Episodic Action**: Documents a single session's fix or implementation; it is a live history. |
| **Dependency** | **Standalone Capability**: Defines a tool or pattern (e.g., "how to parse LaTeX"). | **Mandatory Requirement**: If a GAMMA mentions a Skill, it **requires** its use rather than suggesting it. |
| **Objective** | **Enabling**: Focuses on increasing the agent's theoretical capacity. | **Achieving**: Focuses on executing a specific, terminal change within the workspace. |
| **Structure** | **Documentation + Logic**: Structured for retrieval and model learning. | **PSC Architecture**: Structured as a Problem-Solution-Chain leading to a Git commit. |

## 1. Problem-Solution Architecture (The "Why")

**Q: Why do agents often lose context or fail during multi-step tasks?**
**Problem**: Traditional chat logs are non-deterministic and noisy. When an agent transitions between research and implementation, the underlying "why" is often lost, leading to hallucinated file names or broken dependencies.
**Solution**: Enforce a strict GAMMA trace. Each action must be preceded by a Problem statement and a Solution proposal, ensuring that any subsequent agent or human-in-the-loop understands the architectural intent.

**Q: How do we prevent the "version suffix" rot (e.g., script_v2.py)?**
**Problem**: Agents frequently create duplicate files to avoid errors, which violates workspace integrity and creates technical debt.
**Solution**: Implement a "No-Suffix" mandate. Agents must overwrite existing files and use Git for versioning. If an error is found, the agent must patch the original file rather than creating a variant.

## 2. Skill Generation & Registration
**Action**: Every new capability must be registered as a discrete skill within the `skills/` directory.
- **Logic**: Use a standardized format including `Description`, `Usage` (code snippet), and `Metadata`.
- **Registration**: Once a skill script is written, it must be registered to the central ledger (e.g., `gemini.md` or MCP schema) to ensure visibility to other agents.

## 3. Version Control & Deployment
**Action**: Synchronize the workspace after every successful GAMMA execution.
- **Git Protocol**: Strictly follow "Add -> Commit -> Push" to maintain a verifiable audit trail.
- **Ledger Update**: Reflect any changes in the project's root `gemini.md` to update the global workspace state.

## 4. Rules, Cautions & Limitations
- **Scientific Integrity**: Never hallucinate data or citations. Use verifiable sources only.
- **Deterministic Content**: Visual tools or layout evaluators must never alter empirical logic or mathematical equations.
- **Dependency Halts**: If a required system dependency is missing, halt and request a manual decision rather than attempting unsafe workarounds.
