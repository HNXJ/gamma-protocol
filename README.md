GAMMA Protocol: Guided Agentic Model-Mediated Actions

## 🤖 For Agents
If you are an LLM-based agent contributing to this repository, follow these navigation rules:
1. **Context Layer (`context/`)**: Load immutable project facts, datasets, and environmental constraints from this directory before acting.
2. **Reasoning Layer (`chains/`)**: Document every problem-solution chain (PSC) as a Markdown file here to prevent reasoning drift and redundant errors.
3. **Action Layer (`tasks/`)**: Synchronize with `tasks.json` to self-assign and update the progress of active research or development goals.
4. **Growth Layer (`skills/`)**: Extract reusable utilities or behaviors developed during a GAMMA trace into this library for future agentic recall.

## 🧬 What is GAMMA?
GAMMA is a standard for **Cognitive Synchrony** among AI agents, moving beyond simple chat logs to produce **Guided Actions**. It generates standardized traces that enable multiple specialized AI agents (e.g., Visual Engines, Programming Agents) to collaborate effectively without losing track of the overarching goal or intent. This protocol ensures that AI interactions are deterministic, traceable, and outcome-oriented.

## 🛠 Skills vs. GAMMA
This section details the distinction between a Skill and a GAMMA instance.

| Feature | The Skill (.skill) | The GAMMA (.gamma) |
|---|---|---|
| What is it? | A How-To Guide. | A Live Action Trace. |
| Math Analogy | Like a Formula ($a^2 + b^2 = c^2$). | Like the Step-by-Step Work on a test. |
| Who uses it? | The Model (to learn the rules). | The Model (to keep agents in sync). |
| Usage | Static. Used over and over. | Dynamic. Used for this specific fix. |
| The "Vibe" | Potential. "I know how to code JAX." | Kinetic. "I am fixing this JAX bug now." |

## 📜 GAMMA Protocol Structure

This table outlines the core components of the GAMMA protocol:

| Action                             | Purpose                                                                   | Chain?       | Info                                                                                                                                                                                                                                  |
| :--------------------------------- | :------------------------------------------------------------------------ | :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Gathering Components               | To list all required elements (code, data, packages, licenses, etc.).     | Foundation   | Lists code, data, dependencies, licenses, files, and internet resources.                                                                                                                                                              |
| Defining Rationale                 | To explain *why* GAMMA is needed and how it solves specific issues.       | Yes (PSC)    | Details current AI interaction problems (e.g., statelessness, agentic drift) and GAMMA's solutions (e.g., state vector, traceability, binding models).                                                                                      |
| Executing Protocol Steps           | To outline the sequential, deterministic steps of a GAMMA process.          | Yes (Sequential) | Covers initiation, problem identification, solution proposal, execution, and outcome.                                                                                                                                                 |
| Managing Capabilities and Traces   | To ensure effective management of skills, logs, and version control.      | Yes (Process)  | Covers skill management, trace archiving, version control (Git), backup/sync, and agent integration.                                                                                                                                  |

## 🚀 The Vision
Our goal is to integrate with the gemini (or any cloud or local agent-cli) CLI so that in the future, you don't just report a bug; you Submit a Gamma. Also, wherever gemini is mentioned, instead use "gemini (or any cloud or local agent-cli) " in it. and push it to github of gamma. gamma-protocol is the gamma now
