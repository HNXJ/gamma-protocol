# GAMMA-BURST Migration Report: v0.4 Doctrine Alignment

## Summary
The \`gamma-protocol\` repository has been refactored to align with the v0.4 manuscript framing. The repository is now a Markdown-only doctrine and control-law layer.

## Key Changes
- **Markdown-Only Policy:** All non-markdown files (except \`.gitignore\` and \`.github/CODEOWNERS\`) have been removed or converted to Markdown.
- **Structural Reorganization:** Content has been reorganized into \`doctrine/\`, \`contracts/\`, \`schemas/\`, \`templates/\`, and \`docs/\`.
- **Game-Theoretic Alignment:** Doctrine has been updated to reflect scientific discovery as a repeated game among bounded agents.
- **Four-Plane Separation:** Sharpened the boundaries between Control, Execution, Truth, and Observation planes.
- **Neuroscience Claim Discipline:** Added formal rules for neuroscience-specific truth safety.

## Migration Ledger

| Original Path | Action | New Path / Destination | Reason |
|---|---|---|---|
| \`readme.md\` | Renamed/Updated | \`README.md\` | Canonical naming and content refresh. |
| \`harnesses/registry.json\` | Converted | \`schemas/registry_schema_spec.md\` | Enforce Markdown-only policy. |
| \`schemas/harness.schema.json\` | Converted | \`schemas/harness_schema_spec.md\` | Enforce Markdown-only policy. |
| \`schemas/registry.schema.json\` | Converted | \`schemas/registry_schema_spec.md\` | Enforce Markdown-only policy. |
| \`schemas/tools.schema.json\` | Converted | \`schemas/tools_schema_spec.md\` | Enforce Markdown-only policy. |
| \`template.gamma.json\` | Converted | \`templates/gamma_mission_template.md\` | Enforce Markdown-only policy. |
| \`gamma.gamma\` | Converted | \`doctrine/hellenic_stack.md\` | Enforce Markdown-only policy. |
| \`src/gamma_protocol/forge.py\` | Converted | \`docs/forge_utility_spec.md\` | Move code out of protocol repo; preserve spec. |
| \`tests/test_forge_output.py\` | Converted | \`docs/validation_playbook.md\` | Move tests out; preserve validation logic. |
| \`pyproject.toml\` | Removed | N/A | Protocol repo is not a Python package. |
| \`src/gamma_protocol/\` | Removed | N/A | Protocol repo does not house executable code. |
| \`tests/\` | Removed | N/A | Protocol repo does not house executable tests. |

## Exceptions Remaining
- \`.gitignore\`: Necessary for git maintenance.
- \`.github/CODEOWNERS\`: Necessary for repository governance.

