# GAMMA Module: Context Layer

**agent-source**: any
**agent-target**: any

## 🤖 For Agents
This protocol mandates high-fidelity agentic action traces. Always maintain strict problem-solution chains, documenting the 'why' before the 'how'. Ensure every directive is autonomous, verifiable, and free of version suffixes. Map deterministic targets using unified schemas. Execute terminal actions with precision, registering every newly generated skill to the central ledger.

## ⚖️ Problem-Solution Architecture (The "Why")

**Q: Why is persistent environmental context critical for remote execution?**
**Problem**: Variables like VRAM limits, Python paths, and Tailscale IPs change between local and remote environments. Missing this context leads to execution failures.
**Solution**: Centralize immutable project facts in `environment.md`. This layer must be loaded before any tool execution to ensure the agent is calibrated to the specific hardware and software constraints of the current session.
