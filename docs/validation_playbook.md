# Validation Playbook

This playbook defines the procedures for validating Gamma execution artifacts and doctrine compliance.

## Doctrine Validation
- Ensure all repository changes follow the Markdown-only policy.
- Verify that no secrets or credentials are present.
- Confirm that all scientific claims are marked as proposals until validated by a receipt.

## Execution Trace Validation
- Verify the presence of mode-aware PSC (Problem-Solution Chain).
- Check for correct agent attribution.
- Confirm that all actions include a behavioral verification step.

## Receipt Auditing
- Validate the cryptographic hashes of artifacts.
- Cross-reference timestamps with execution logs.
- Verify that the harness used matches the quest's requirements.

