# Player / Harness Contract

The separation between the Player and the Harness is the fundamental security boundary in Gamma.

## The Player
- Proposes moves.
- Implements strategies.
- Is responsible for the content of the scientific claim.
- Can be human or agentic.

## The Harness
- Defines legal moves.
- Constraints tool usage.
- Enforces timeouts and safety policies.
- Generates immutable receipts.

## The Boundary
A player must never be able to modify the harness that governs their own execution. Any attempt to bypass harness constraints is a violation of the protocol and leads to immediate invalidation of the move.

