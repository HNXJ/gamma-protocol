# Repository File Policy

The \`gamma-protocol\` repository is the doctrine and control-law layer for the Gamma ecosystem.

## Markdown-Only Rule
- Only Markdown (\`.md\`) files are allowed for normative content.
- Code (\`.py\`, \`.js\`, etc.), packaging (\`.toml\`, \`.yaml\`), and runtime artifacts (\`.json\`) are forbidden.

## Exceptions
- \`.gitignore\`
- \`.github/CODEOWNERS\`
- Github Actions workflows (\`.yml\`) provided they only enforce documentation/markdown policy.

## Enforcement
Any non-markdown file added to the repo must be either converted to Markdown, moved to a code-bearing repo, or documented as a strictly necessary exception in the migration report.

