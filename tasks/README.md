# GAMMA Module: Task Management

**agent-source**: any
**agent-target**: any

## 🤖 For Agents
This protocol mandates high-fidelity agentic action traces. Always maintain strict problem-solution chains, documenting the 'why' before the 'how'. Ensure every directive is autonomous, verifiable, and free of version suffixes. Map deterministic targets using unified schemas. Execute terminal actions with precision, registering every newly generated skill to the central ledger.

## ⚖️ Problem-Solution Architecture (The "Why")

**Q: Why do we need a centralized task ledger for autonomous agents?**
**Problem**: Without a unified view of active tasks, agents may duplicate efforts, miss dependencies, or lose track of long-running objectives (like paper evaluations) across different sessions.
**Solution**: Use `active_tasks.json` as the source of truth. Every GAMMA trace must begin by checking this ledger and end by updating it to reflect progress or blockers.

## 🛠 Flow & Logic
1. **Load**: Read `active_tasks.json` to identify pending P1 objectives.
2. **Execute**: Perform the specific GAMMA action.
3. **Update**: Modify the task status and append a brief completion trace to the ledger.
