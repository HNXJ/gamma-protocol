# Agent Skill: GAMMA_ORCHESTRATOR

## Objective
To mediate between specialized agents and ensure every solution is grounded in a Problem-Solution-Chain.

## Rules for Agents
1. **Verification:** Check the `ingredients` before starting. If a package is missing, the first "Action" must be to install it.
2. **Determinism:** The "Actions" section must be clear enough that a simple script could execute it.
3. **Memory:** Always save a `readme.md` summary of what you did.

## How to make a GAMMA
- Step 1: Identify the **Mismatch** (The Problem).
- Step 2: Use your **Skills** to propose a **Solution**.
- Step 3: Write the **Actions** to fix the file.
- Step 4: Record the **Delta**.