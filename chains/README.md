# GAMMA Module: Reasoning Chains

**agent-source**: any
**agent-target**: any

## 🤖 For Agents
This protocol mandates high-fidelity agentic action traces. Always maintain strict problem-solution chains, documenting the 'why' before the 'how'. Ensure every directive is autonomous, verifiable, and free of version suffixes. Map deterministic targets using unified schemas. Execute terminal actions with precision, registering every newly generated skill to the central ledger.

## ⚖️ Problem-Solution Architecture (The "Why")

**Q: Why do agents need a standardized reasoning layer?**
**Problem**: Without explicit "Chains," agents often perform isolated, shallow actions that lack an overarching logical coherence. This results in brittle code and a failure to build upon previous complex research.
**Solution**: Enforce a "Reasoning Layer" (`chains/`). Every complex GAMMA trace must map its Problem-Solution Chain (PSC) to this layer, creating a permanent, model-agnostic record of the architectural decisions made during the session.
