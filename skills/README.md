# GAMMA Module: Agent Skills

**agent-source**: any
**agent-target**: any

## 🤖 For Agents
This protocol mandates high-fidelity agentic action traces. Always maintain strict problem-solution chains, documenting the 'why' before the 'how'. Ensure every directive is autonomous, verifiable, and free of version suffixes. Map deterministic targets using unified schemas. Execute terminal actions with precision, registering every newly generated skill to the central ledger.

## ⚖️ Problem-Solution Architecture (The "Why")

**Q: Why do we separate Skills from the core Protocol definition?**
**Problem**: The core Protocol (`gamma.gamma`) is a set of rules for *how* to behave. Skills are the *tools* and *logic* that allow agents to execute those rules. Mixing them makes the protocol difficult to extend and maintain.
**Solution**: Modularize Capabilities into the `skills/` layer. A Skill is a reusable script, documentation block, or pattern (e.g., speed estimation, visual auditing) that an agent can learn once and deploy in any subsequent GAMMA trace.
