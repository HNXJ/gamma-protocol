# Harness Schema Specification

Harnesses are structured task wrappers that define input contracts, execution environments, output contracts, and validation criteria.

## Required Fields
- **harness_id:** Unique identifier (kebab-case).
- **name:** Human-readable name.
- **description:** Purpose and scope.
- **plane:** The GAMMA plane (Control, Execution, Truth, Observation).
- **protocol:** The Hellenic protocol (BETA, ALPHA, GAMMA, DELTA, THETA, GAMMA-BURST).
- **input_contract:** Definition of required and optional input fields.
- **output_contract:** Definition of guaranteed output fields and schema.
- **execution_environment:** Specifies the runtime (python, bash, node, docker) and dependencies.

## Optional Fields
- **version:** Semantic version (MAJOR.MINOR.PATCH).
- **author:** Creator/maintainer.
- **validation_criteria:** Conditions that must be satisfied for success.
- **rejection_criteria:** Conditions that cause failure.
- **forbidden_actions:** Explicitly prohibited operations.
- **required_evidence:** Artifacts that must be produced for the receipt.

