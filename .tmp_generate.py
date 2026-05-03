import os
import re

repo_dir = "/Users/hamednejat/workspace/computational/gamma-protocol"

structure = {
    "core": ["planes.md", "principles.md", "system_overview.md", "repo_boundaries.md", "glossary.md"],
    "hellenic": ["README.md", "alpha.md", "beta.md", "gamma.md", "delta.md", "theta.md", "gamma_burst.md"],
    "gameplay": ["README.md", "events.md", "missions.md", "tournaments.md", "contests.md", "levels.md", "patches.md", "quests.md"],
    "agents": ["README.md", "agent_model.md", "identity.md", "permissions.md", "model_profiles.md", "inventory.md", "join_act_leave.md", "judge_roles.md"],
    "execution": ["README.md", "lifecycle.md", "task_flow.md", "continuous_execution.md", "safe_mode.md", "expectation_mode.md", "game_mode.md", "failure_recovery.md", "checkpointing.md"],
    "truth": ["README.md", "validation.md", "receipts.md", "truth_commit.md", "dispute_resolution.md", "conflict_reconciliation.md", "invalid_state.md"],
    "science": ["README.md", "evidence.md", "reproducibility.md", "citation.md", "scientific_claims.md", "gamma_science_boundary.md"],
    "analysis": ["README.md", "methods.md", "metrics.md", "evaluation.md", "statistical_reasoning.md", "gamma_analysis_boundary.md"],
    "collaboration": ["README.md", "communication.md", "contribution.md", "github_project.md", "github_app.md", "versioning.md", "agent_handoff.md"],
    "data": ["README.md", "integrity.md", "storage.md", "provenance.md", "text_first_policy.md", "secrets_policy.md"],
    "templates": ["README.md", "event_template.md", "mission_template.md", "tournament_template.md", "contest_template.md", "judge_report_template.md", "inventory_template.md", "model_profile_template.md", "receipt_template.md", "patch_note_template.md", "agent_handoff_template.md"],
    "audits": ["README.md", "theta_validation_prompt.md", "gamma_burst_commit_prompt.md"]
}

content_map = {
    "core/planes.md": "# Four-Plane Architecture\n\n- **Control Plane**: Planning and coordination.\n- **Execution Plane**: Agent workflow and generation.\n- **Truth Plane**: Validated output, requiring receipts.\n- **Observation Plane**: UI and rendering.\n\nExplicitly forbid:\n- UI-derived truth.\n- Project-board-derived truth.\n- Proposal-derived truth.\n- Execution-output-derived truth without receipts.\n- Manual truth mutation.",
    "core/repo_boundaries.md": "# Five-Repo Ecosystem\n\n- `gamma` = runtime/core/base.\n- `gamma-protocol` = doctrine/rules/governance.\n- `gamma-arena` = UI/interface/observation only.\n- `gamma-science` = scientific evidence/citation/validity/canon.\n- `gamma-analysis` = math/statistics/computation/evaluation methods.",
    "hellenic/README.md": "# Hellenic Stack\n\nDefines the operational stack for agents:\n- ALPHA = planning.\n- BETA = audit/grounding.\n- GAMMA = exact execution.\n- DELTA = conflict/inconsistency reconciliation.\n- THETA = post-execution validation.\n- GAMMA-BURST = one-time major refactor/migration.",
    "hellenic/alpha.md": "# ALPHA\n**Planning Phase**\n- Inputs: Goal, current state\n- Outputs: Action plan\n- Allowed actions: Read state, map files\n- Forbidden actions: Modify truth, write code\n- Validation format: Plan validation",
    "hellenic/beta.md": "# BETA\n**Audit/Grounding Phase**\n- Inputs: Pre-existing repository state\n- Outputs: Audit report\n- Allowed actions: Run read-only audits (`git status`, `find`, `grep`)\n- Forbidden actions: Modify files\n- Validation format: Threat/secret scan report",
    "hellenic/gamma.md": "# GAMMA\n**Exact Execution Phase**\n- Inputs: Audited state, ALPHA plan\n- Outputs: Code execution, artifacts\n- Allowed actions: Script generation, environment interaction\n- Forbidden actions: Bypassing Safe Mode without explicit directives\n- Validation format: Execution logs",
    "hellenic/delta.md": "# DELTA\n**Reconciliation Phase**\n- Inputs: Conflicting outputs\n- Outputs: Merged resolution\n- Allowed actions: Diff resolution, logic patches\n- Forbidden actions: Blindly overriding truth planes\n- Validation format: Diff matrix",
    "hellenic/theta.md": "# THETA\n**Post-Execution Validation Phase**\n- Inputs: Execution artifacts\n- Outputs: Validation receipt\n- Allowed actions: Run tests, secret scans\n- Forbidden actions: Falsifying success\n- Validation format: Pass/Fail + Metrics",
    "hellenic/gamma_burst.md": "# GAMMA-BURST\n**One-Time Refactor Phase**\n- Inputs: System-wide mandate\n- Outputs: Full architectural refactor\n- Allowed actions: Core systemic changes\n- Forbidden actions: Leaving system in unstable state\n- Validation format: Comprehensive integration report",
    "execution/continuous_execution.md": "# Continuous Execution Doctrine\n\n\"Models are never idle.\"\n\nEven when data is wrong, truth is pending, patches are pending, or environment is partially broken, agents should continue with safe provisional work:\n- audit\n- summarize\n- prepare rerun manifests\n- improve inventory\n- validate old outputs\n- literature/evidence review if permitted\n- reconcile after patches",
    "execution/safe_mode.md": "# Safe Mode\n\nMinimal non-crashing fallback room. Use this mode for diagnosis when Game Mode fails.",
    "execution/expectation_mode.md": "# Expectation Mode\n\nOnboarding/spectator/orientation layer.",
    "execution/game_mode.md": "# Game Mode\n\nFull active participation and truth generation capabilities.",
    "agents/inventory.md": "# Agent Inventory Doctrine\n\nEach agent has exactly one inventory.\n\nInventory is:\n- writable workspace\n- persistent memory\n- output locker\n- portable\n- reloadable\n- text-first\n- isolated\n\nMinimum inventory:\n- `context.md`\n- `current_task.md`\n- `skills/`\n- `outputs/`\n- `evidence/`\n- `checkpoints/`\n- `handoff.md`",
    "truth/receipts.md": "# Truth/Receipt Doctrine\n\nTruth requires receipts. Without a receipt, a claim is not truth.\n\nReceipt fields:\n- `receipt_id`\n- `timestamp`\n- `source run`\n- `mission/event`\n- `input state reference/hash`\n- `output state reference/hash`\n- `adapter/gate`\n- `validation checks`\n- `rejected invalids`\n- `NaN/inf checks if numerical`\n- `commit decision`\n- `judge/signer if applicable`\n- `provenance`\n- `reproducibility instructions`",
    "collaboration/github_project.md": "# GitHub Project Doctrine\n\nGitHub Project is a planning/coordination/control artifact.\n- It is not truth.\n- It does not store secrets.\n- Agents should use Project items for cross-repo communication and handoff.",
    "collaboration/github_app.md": "# GitHub App Doctrine\n\nGitHub App is a scoped access mechanism.\n- It is not truth.\n- It does not store secrets.",
    "data/secrets_policy.md": "# Secrets Doctrine\n\nMarkdown may mention only secret reference names or expected environment variable names. Never include raw values.\n\nForbidden secrets include:\n- PATs\n- GitHub App private keys\n- `.pem` files\n- API keys\n- Supabase keys\n- database URLs\n- passwords\n- tokens",
    "science/gamma_science_boundary.md": "# Gamma Science Boundary\n\nThis boundary separates general doctrine from scientific evidence.\n- `gamma-science` governs validity criteria and citations.\n- Doctrine repo (`gamma-protocol`) points here but does not host the scientific claims themselves.",
    "analysis/gamma_analysis_boundary.md": "# Gamma Analysis Boundary\n\nThis boundary outlines the methodology split.\n- `gamma-analysis` holds computation, statistics, and evaluation methods.\n- `gamma-protocol` governs how those methods integrate into the overall workflow."
}

# Generate the files
for folder, files in structure.items():
    folder_path = os.path.join(repo_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder_path, file)
        content = content_map.get(f"{folder}/{file}", f"# {file.replace('.md', '').replace('_', ' ').title()}\n\nStandard operating doctrine for {file}.")
        with open(file_path, "w") as f:
            f.write(content)

# Update README.md
readme_path = os.path.join(repo_dir, "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r") as f:
        readme_content = f.read()
        
    # Remove stale doctrine using exact text replacements where necessary or robust regex
    # The regex removes lines containing forbidden permutations
    stale_pattern = re.compile(r".*(UI.*truth|dashboard.*truth|truth.*dashboard|manual.*truth|committed truth|runtime truth|proposal.*truth|execution.*truth|GitHub Project.*truth|project board.*truth).*\n", re.IGNORECASE)
    readme_content = stale_pattern.sub("", readme_content)
    
    with open(readme_path, "w") as f:
        f.write(readme_content)

print("SUCCESS")
