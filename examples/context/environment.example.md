# GAMMA Context: Environment Definitions

**agent-source**: any
**agent-target**: any

## 🧠 For Agents
This protocol mandates high-fidelity agentic action traces. Always maintain strict problem-solution chains, documenting the 'why' before the 'how'. Ensure every directive is autonomous, verifiable, and free of version suffixes. Map deterministic targets using unified schemas. Execute terminal actions with precision, registering every newly generated skill to the central ledger.

## 1. Problem-Solution Architecture (The "Why")

**Q: Why do agents struggle with environment-specific paths and permissions?**
**Problem**: Hardcoded paths (e.g., `/Users/HN/...`) make code brittle and non-portable. When an agent moves between local and remote (Office Mac) contexts, these paths break, causing GAMMA traces to fail.
**Solution**: Define an `environment_config_resolver`. This module maps environment variables and relative paths to a unified workspace schema. It ensures all tools reference the correct root and bin paths dynamically at runtime.

**Q: How do we manage cross-platform disparities (macOS vs. Linux)?**
**Problem**: Differences in shell commands (e.g., `sed -i` on macOS vs. Linux) lead to execution errors.
**Solution**: Standardize on portable commands (using Python when possible) and maintain a central "Platform Map" in the context layer.

## 2. Skill Generation & Registration
**Action**: Implement an `env_resolver.py` that checks for required binaries (e.g., `pandoc`, `pdflatex`, `lms`) and sets up necessary symlinks.
- **Logic**: Use `os.path.expanduser` and `os.getenv` to resolve all paths.
- **Registration**: This environment context is loaded at the beginning of every session to bootstrap the agent's knowledge of the workspace.

## 3. Rules, Cautions & Limitations
- **No Absolute Paths**: This is a strict operational constraint. Use relative paths or dynamic resolvers.
- **Permission Awareness**: Agents must verify write permissions before attempting heavy file operations.
- **Network Dependency**: Remote Office Mac connectivity must be verified via Tailscale before initiating remote GAMMA calls.
