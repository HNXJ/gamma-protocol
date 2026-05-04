# Tools Schema Specification

Tools are executable components that perform specific computational or operational tasks within a harness.

## Core Fields
- **tool_id:** Unique identifier.
- **name:** Human-readable name.
- **description:** Capabilities and purpose.
- **type:** (computational, validation, transformation, analysis, adapter, utility).
- **input_contract:** Mapping of parameters to types and requirements.
- **output_contract:** Return type and semantics.

## Implementation Details
- **language:** (python, javascript, typescript, bash, go, rust).
- **location:** Path to implementation in the execution repo.
- **dependencies:** Required libraries or modules.

