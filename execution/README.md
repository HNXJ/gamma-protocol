# Agent Execution: Lifecycle and Modes

## Execution Lifecycle

1. **Join** - Agent enters the system, loads inventory
2. **Onboard** - Agent reads protocol, understands state
3. **Act** - Agent executes work within harness
4. **Checkpoint** - Agent saves state every 30-60 min
5. **Handoff** - Agent passes work to next agent (if needed)
6. **Leave** - Agent exits cleanly, inventory preserved

## Execution Modes

- **Safe Mode**: Minimal operations, crash recovery
- **Expectation Mode**: Onboarding mode, agent learns state before acting
- **Game Mode**: Full participation, agent acts freely within harness

---

© 2026 HNXJ(H.Nejat) / BASTOSLAB / VANDERBILT UNIVERSITY
