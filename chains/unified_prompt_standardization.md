# Reasoning Chain: Unified Prompt Standardization

## 1. Problem Identification
- **Issue**: MLLM evaluations were using decoupled prompt fragments, leading to inconsistent model responses across different reasoning runs.
- **Goal**: Implement a "Single Source of Truth" prompt format containing `Instructions`, `Glossary`, `Input`, and `Output Examples`.

## 2. Solution Proposal
- **Action**: Refactor `mllm_pipeline.py` to hardcode prompt components as global constants.
- **Implementation**:
    - `HPC_INSTRUCTIONS`: Role and analysis guardrails.
    - `HPC_RULES`: Strict order of evaluation.
    - `HPC_OUTPUT_EXAMPLE`: Precise JSON/Reasoning schema.

## 3. Execution & Outcome
- **Step**: Unified all fragments into a single formatted string.
- **Verification**: TPS logging and monitor dashboard confirm stable 1000+ token reasoning outputs.
- **Trace**: [gamma-260402-001]
