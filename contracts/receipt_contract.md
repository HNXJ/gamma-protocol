# Receipt Contract

A receipt is the immutable proof of execution.

## Mandatory Fields
- **timestamp:** UTC timestamp of execution.
- **agent_id:** Identity of the player.
- **harness_id:** Identity of the harness used.
- **input_digest:** Hash of the quest/input.
- **output_artifacts:** Links to or hashes of the generated artifacts.
- **exit_code:** The outcome of the execution process.

