# Forge Utility Specification

The Forge is a doctrine-enforcement utility (historically implemented as \`forge.py\`) that ensures all agentic action traces follow the standardized GAMMA format.

## Core Mandate
Enforce high-fidelity action traces through mode-aware Problem-Solution Chains (PSC).

## Modes
- **Scientific:** For research and discovery tasks. Requires research question, corpus scope, and evidence.
- **Debug:** For engineering and fixes. Requires failure description, reproduction steps, root cause, and patch strategy.

## Structural Requirements
- **Title:** Clear objective of the trace.
- **Agent Attribution:** source and target agent identities.
- **Problem-Solution Architecture:** The 'why' before the 'how'.
- **Skill Registration:** Documentation of newly generated capabilities.
- **Logic & Finality:** Step-by-step execution logic and confirmation of correctness.

## Constraints
- No version suffixes on files.
- Relative paths only.
- Mandatory behavioral verification.

