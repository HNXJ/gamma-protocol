GAMMA Protocol: Guided Agentic Model-Mediated Actions

Welcome to the GAMMA Protocol.

## 🧬 What is GAMMA?
GAMMA is a standard for **Cognitive Synchrony** among AI agents, moving beyond simple chat logs to produce **Guided Actions**. It generates standardized traces that enable multiple specialized AI agents (e.g., Visual Engines, Programming Agents) to collaborate effectively without losing track of the overarching goal or intent. This protocol ensures that AI interactions are deterministic, traceable, and outcome-oriented.

---

### 1. Ingredients

This section outlines the essential components required for executing or defining a GAMMA protocol:

*   **Code & Artifacts:** Python 3.11+, JAX & Optax (for biophysics), MLX (for LLMs), Git & GitHub CLI (`gh`).
*   **Data & Knowledge:** Relevant neurophysiological theories (e.g., Gamma oscillations, PLV, MMN), agentic framework concepts (multi-agent hand-offs, Mediator patterns).
*   **Dependencies:** Access to `github.com` for repository management, Gemini API for mediation.
*   **Licenses:** MIT License for open-source standard.
*   **Files:** `.gamma` (action trace), `.skill` (agent capability), `.md` (documentation).
*   **Internet:** URLs for package repositories, model access, and collaboration platforms.

---

### 2. Problem-Solution-Chain

GAMMA addresses critical challenges in multi-agent AI collaboration:

*   **Problem:** Current AI interactions are often "stateless," leading to "Agentic Drift." When specialized agents (e.g., a Visual Agent identifying a bug and a Coder Agent fixing it) collaborate, the original intent can be lost in translation, resulting in miscommunication and inefficient problem-solving.
    *   **Solution:** The GAMMA Protocol mandates a shared "State Vector" (the `.gamma` file) that all agents read and write to. This ensures agents remain "Phase-Locked" and maintain a unified understanding of the task and its evolution.
*   **Problem:** Standard AI interactions lack a traceable record of intent and justification, making debugging and learning difficult.
    *   **Solution:** Every GAMMA instance must include a Problem-Solution-Chain, documenting the reasoning behind choices, challenges encountered, and the rationale for specific methods chosen. This creates a learnable "Trace" for AI models.
*   **Problem:** Integrating diverse agent capabilities (e.g., analysis, coding, domain-specific logic) requires a cohesive framework.
    *   **Solution:** GAMMA acts as the $40\text{Hz}$ oscillation for AI, binding specialized models into a single, guided action, analogous to Gamma waves binding neural information for conscious perception.

---

### 3. Actions

This section details the sequential and deterministic steps involved in a GAMMA process, ensuring clear execution:

*   **Initiation:** Define the `[IDENTIFIER]`, `[COGNITIVE_STATE]` (Goal, Mediator, Agents), and `[INGREDIENTS]` for the specific GAMMA task.
*   **Problem Identification:** Clearly articulate the core problem or mismatch that necessitates the action.
*   **Solution Proposal:** Agents leverage their skills to propose a solution, supported by the Problem-Solution-Chain.
*   **Execution:** Implement the solution via concrete `[ACTIONS]`, such as code modifications, file updates, or package installations. These actions must be deterministic and repeatable.
*   **Outcome:** Every GAMMA process must conclude with a tangible `[DELTA]`—a real Action that resolves the identified problem.

---

### 4. Skill Making and Organization

Effective management of AI capabilities and collaboration traces is crucial for long-term AI development and memory.

*   **Skill Management:** Agent capabilities are codified as `.skill` files, representing persistent knowledge.
*   **Trace Archiving:** For every successful GAMMA execution, a trace (`.gamma` file) or an updated `README.md` summary must be generated to document the specific action taken.
*   **Version Control:** All code, protocol definitions (`.gamma`), skill definitions (`.skill`), and documentation (`.md`) are managed using Git. Changes are committed and pushed to a designated repository (e.g., `github.com/nyx/gamma-protocol`).
*   **Backup & Synchronization:** Git is the primary method for backing up and synchronizing work. Only code and content are pushed; sensitive data such as API keys or private information must be excluded.
*   **Agent Integration:** The Gemini CLI (or any cloud or local agent-cli) can utilize the GAMMA protocol to manage multi-agent workflows, ensuring agents remain "phase-locked" and actions are traceable.
