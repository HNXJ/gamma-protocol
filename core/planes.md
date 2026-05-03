# Four-Plane Architecture

- **Control Plane**: Planning and coordination.
- **Execution Plane**: Agent workflow and generation.
- **Truth Plane**: Validated output, requiring receipts.
- **Observation Plane**: UI and rendering.

Explicitly forbid:
- UI-derived truth.
- Project-board-derived truth.
- Proposal-derived truth.
- Execution-output-derived truth without receipts.
- Manual truth mutation.