#!/usr/bin/env python3
import sys
import argparse
from datetime import datetime

def forge_gamma(args):
    """
    Problem: Manual formatting leads to divergence between documentation and action traces.
    Solution: Unified Forge enforcing mode-aware PSC (Problem-Solution-Chain) for Scientific and Debugging tasks.
    """
    digest = (
        "This protocol mandates high-fidelity agentic action traces. Before execution, "
        "agents MUST declare the GAMMA Mode (scientific or debugging). Always maintain "
        "strict Problem-Solution Chains (PSC), documenting the 'why' before the 'how'. "
        "Ensure every directive is autonomous, verifiable, and free of version suffixes. "
        "Map deterministic targets using unified schemas. Execute terminal actions with "
        "precision, registering every newly generated skill to the central ledger."
    )
    
    content = f"# GAMMA: {args.title}\n\n"
    content += f"**agent-source**: {args.source}\n"
    content += f"**agent-target**: {args.target}\n"
    content += f"**mode**: {args.mode}\n\n"
    content += f"## 🤖 For Agents\n{digest}\n\n"
    content += "## 1. Problem-Solution Architecture (The 'Why')\n\n"
    
    if args.mode == "scientific":
        content += "### 🧬 Scientific Mode (Research & Discovery)\n"
        content += f"- **Research Question**: {args.problem}\n"
        content += f"- **Corpus/Scope**: {args.scope}\n"
        content += f"- **Method/Evidence**: {args.solution}\n"
        content += f"- **Uncertainty**: {args.uncertainty or 'None stated.'}\n"
        content += f"- **Output Artifact**: {args.artifact}\n\n"
    else:
        content += "### 🛠 Debugging Mode (Fixes & Engineering)\n"
        content += f"- **Observed vs. Expected**: {args.problem}\n"
        content += f"- **Reproduction**: {args.repro}\n"
        content += f"- **Root-Cause Hypothesis**: {args.solution}\n"
        content += f"- **Patch Strategy**: {args.patch}\n"
        content += f"- **Validation & Rollback**: {args.validation}\n\n"
    
    content += "## 2. Skill Generation & Registration\n"
    content += f"**Capability**: {args.skill or 'Standardized execution'}\n"
    content += "- **Synaptic Gate**: Verified complexity <= 5; AST <= 4.\n\n"
    
    content += "## 3. Execution Logic & Finality\n"
    content += f"**Logic**: {args.logic}\n"
    content += "- **Non-Suffix**: Overwrite existing files; no _v2 or _final.\n"
    content += "- **Git**: Add -> Commit -> Push synchronized.\n\n"
    
    content += "## 4. Rules & Constraints\n"
    content += "- **Portability**: Relative paths only; no absolute references.\n"
    content += "- **Verifiability**: Action is incomplete until behavioral correctness is confirmed.\n"
    
    filename = f"{args.title.lower().replace(' ', '_')}.gamma"
    with open(filename, "w") as f:
        f.write(content)
    print(f"🔥 Successfully forged: {filename} ({args.mode} mode)")

def main():
    parser = argparse.ArgumentParser(description="Forge a standardized GAMMA trace (v1.1.0).")
    parser.add_argument("--mode", choices=["scientific", "debug"], required=True, help="GAMMA mode.")
    parser.add_argument("--title", required=True, help="Title of the GAMMA trace.")
    parser.add_argument("--problem", required=True, help="Research question (scientific) or failure description (debug).")
    parser.add_argument("--solution", required=True, help="Method/Evidence (scientific) or Root-cause/Fix (debug).")
    parser.add_argument("--logic", required=True, help=" Algorithmic steps taken.")
    
    # Optional / Mode-specific flags
    parser.add_argument("--source", default="gemini-cli")
    parser.add_argument("--target", default="all-any")
    parser.add_argument("--skill", help="Name of the newly generated skill.")
    
    # Scientific Mode flags
    parser.add_argument("--scope", default="Workspace", help="[Scientific] Corpus or dataset scope.")
    parser.add_argument("--artifact", default="Markdown", help="[Scientific] Target output artifact.")
    parser.add_argument("--uncertainty", help="[Scientific] Known gaps or limitations.")
    
    # Debugging Mode flags
    parser.add_argument("--repro", default="N/A", help="[Debug] Reproduction steps.")
    parser.add_argument("--patch", default="Surgical Fix", help="[Debug] Minimal-diff patch strategy.")
    parser.add_argument("--validation", default="Manual/Tests", help="[Debug] Testing and rollback plan.")
    
    args = parser.parse_args()
    forge_gamma(args)

if __name__ == "__main__":
    main()
