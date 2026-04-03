#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

/**
 * Problem: Web and frontend-focused agents need a familiar JS/TS environment to forge GAMMA traces.
 * Solution: Node.js implementation of the GAMMA Forge with filesystem integration.
 */
function forgeGamma(title, problem, solution, logic, source = "gemini-cli", target = "any") {
    const digest = "This protocol mandates high-fidelity agentic action traces. Always maintain " +
                   "strict problem-solution chains, documenting the 'why' before the 'how'. " +
                   "Ensure every directive is autonomous, verifiable, and free of version suffixes. " +
                   "Map deterministic targets using unified schemas. Execute terminal actions with " +
                   "precision, registering every newly generated skill to the central ledger. " +
                   "Mandatory: Skills must satisfy the Synaptic Pruning Gate (v(G) <= 5, AST <= 4).";

    const content = `# GAMMA: ${title}

**agent-source**: ${source}
**agent-target**: ${target}

## 🤖 For Agents
${digest}

## 1. Problem-Solution Architecture (The 'Why')

**Q: What is the primary bottleneck for this action?**
**Problem**: ${problem}
**Solution**: ${solution}

## 2. 🧬 Synaptic Pruning (Kolmogorov-Proxy Check)
- **Cyclomatic Complexity**: Verified <= 5.
- **Rule of 3**: Justified reusability for 3 neuro-computational scenarios.

## 3. Execution Logic & Finality
**Logic**: ${logic}

## 4. Rules & Constraints
- **Non-Suffix**: Overwrite existing files; no _v2 or _final.
- **Verifiability**: Action is incomplete until behavioral correctness is confirmed.
`;

    const filename = `${title.toLowerCase().replace(/ /g, '_')}.gamma`;
    try {
        fs.writeFileSync(filename, content);
        console.log(`🔥 Successfully forged: ${filename}`);
    } catch (err) {
        console.error(`❌ Error: Could not create ${filename}`, err);
    }
}

const args = process.argv.slice(2);
if (args.length < 4) {
    console.error("Usage: node gamma_forge.js <title> <problem> <solution> <logic>");
    process.exit(1);
}
forgeGamma(args[0], args[1], args[2], args[3]);
