# GAMMA Chain: Unified Prompt Standardization

**agent-source**: any
**agent-target**: any

## 🧠 For Agents
This protocol mandates high-fidelity agentic action traces. Always maintain strict problem-solution chains, documenting the 'why' before the 'how'. Ensure every directive is autonomous, verifiable, and free of version suffixes. Map deterministic targets using unified schemas. Execute terminal actions with precision, registering every newly generated skill to the central ledger.

## 1. Problem-Solution Architecture (The "Why")

**Q: Why do prompts often fail across different LLM architectures (e.g., Llama vs. Gemma)?**
**Problem**: Each model has its own bias regarding token sensitivity, system prompt formatting, and task interpretation. A prompt that works on one architecture may produce noisy or hallucinatory results on another, leading to inconsistent GAMMA traces.
**Solution**: Implement a `unified_prompt_standardizer`. This chain strips model-specific biases and maps instructions to a deterministic, high-fidelity schema that focuses on structural constraints (word counts, JSON schemas, LaTeX macros) rather than conversational filler.

**Q: How do we maintain a consistent "Scientific Lexicon" across diverse agents?**
**Problem**: Different agents (Research vs. Coding) may use inconsistent terminology for the same neuroscientific constructs (e.g., "Predictive Coding" vs. "HPC Theory").
**Solution**: Embed a "Banned Word List" and a "Mandatory Glossary" into the unified prompt chain. This ensures all agents use the exact same terminology defined in the root `HPC/hpc-36-reference.md`.

## 2. Skill Generation & Registration
**Action**: The prompt standardizer should be implemented as a middleware for all LLM calls.
- **Logic**: Use a standardized prompt template that includes explicit sections for `DIRECTIVE`, `CONSTRAINTS`, `GLOSSARY`, and `EXPECTED_OUTPUT_SCHEMA`.
- **Registration**: This standardization chain is registered as a root MCP skill to be automatically prepended to every task.

## 3. Rules, Cautions & Limitations
- **Determinism**: The standardizer must never alter the empirical logic of the prompt.
- **No Hallucinations**: It must strictly enforce valid schema keys and bibliography identifiers.
- **Scientific Caution**: When mapping constructs, if an ambiguity exists, the chain must halt and trigger the `user_decision_router`.
