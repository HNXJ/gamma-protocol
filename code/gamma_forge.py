import sys
import argparse

def forge_gamma(title, problem, solution, logic, source="gemini-cli", target="any"):
    """
    Problem: Manual formatting of GAMMA traces leads to inconsistent headers and missing directives.
    Solution: A Python-based Forge that enforces the PSC (Problem-Solution-Chain) architecture.
    """
    digest = (
        "This protocol mandates high-fidelity agentic action traces. Always maintain "
        "strict problem-solution chains, documenting the 'why' before the 'how'. "
        "Ensure every directive is autonomous, verifiable, and free of version suffixes. "
        "Map deterministic targets using unified schemas. Execute terminal actions with "
        "precision, registering every newly generated skill to the central ledger."
    )
    
    content = f"# GAMMA: {title}\n\n"
    content += f"**agent-source**: {source}\n"
    content += f"**agent-target**: {target}\n\n"
    content += f"## 🤖 For Agents\n{digest}\n\n"
    content += "## 1. Problem-Solution Architecture (The 'Why')\n\n"
    content += f"**Q: What is the primary bottleneck for this action?**\n"
    content += f"**Problem**: {problem}\n"
    content += f"**Solution**: {solution}\n\n"
    content += "## 2. Execution Logic & Finality\n"
    content += f"**Logic**: {logic}\n\n"
    content += "## 3. Rules & Constraints\n"
    content += "- **Non-Suffix**: Overwrite existing files; no _v2 or _final.\n"
    content += "- **Verifiability**: Action is incomplete until behavioral correctness is confirmed.\n"
    
    filename = f"{title.lower().replace(' ', '_')}.gamma"
    with open(filename, "w") as f:
        f.write(content)
    print(f"🔥 Successfully forged: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Forge a standardized GAMMA trace.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--problem", required=True)
    parser.add_argument("--solution", required=True)
    parser.add_argument("--logic", required=True)
    args = parser.parse_args()
    forge_gamma(args.title, args.problem, args.solution, args.logic)
