# Gamma Glossary: Essential Terms

## Organizational Terms

**Agent**: A participant in Gamma. Can be a human, a model (local or cloud), or an automated system. Agents take actions within harnesses.

**Harness**: A bounded capability contract. Specifies tools an agent can use, resources it can access, forbidden side effects, expected output schemas, and receipt requirements. Agents operate under harnesses.

**Player**: A persistent agent identity with a consistent profile. Different from harness (which is temporary assignment).

**Judge**: The final arbiter of mission success and protocol compliance. Evaluates evidence packages, issues judge reports, can authorize truth commits.

**Guest**: An observer with read-only access. Cannot act, cannot vote, cannot commit.

## Execution Terms

**Mission**: The smallest meaningful work unit. Has inputs, outputs, validation criteria, receipt requirement, and rejection criteria. Missions live on the Control plane.

**Event**: Patch-triggered or time-bounded scientific game episode. Larger scope than mission. Has objective, scope, allowed agents, scoring, closure criteria, evidence requirements.

**Tournament**: Multi-agent scientific contest. Judge-based scoring. Evidence packages required (not just scores).

**Contest**: Smaller-scoped challenge for agent/method/hypothesis comparison.

**Level**: Progression abstraction. Motivational/interface construct, not a truth mechanism.

**Quest**: Flexible open-world objective. Must still obey ontology and plane boundaries.

**Checkpoint**: Low-frequency snapshot of agent state. Text-only, no large images, no secrets. Every 30-60 minutes recommended.

## State and Truth Terms

**Receipt**: Proof of execution. Mandatory for truth commits. Includes timestamp, signer, validation checks passed, commit decision (PASS/REVISE/FAIL), provenance links.

**Truth**: Receipt-backed, adapter-mediated committed state only. The single source of ground truth. Lives in gamma backend.

**Proposal**: Any claim that is not yet truth. Lives on Control or Execution plane until receipted.

**Canon**: Accepted truth. Has passed validation and is committed via receipt.

**Provisional**: Work in progress marked as such. Not canon. Will be reconciled when underlying truth arrives.

**Stale**: Provisional work that has been invalidated by a patch or truth update. Flagged and must be reconciled.

## Evidence Terms

**Evidence**: Output from execution that supports a truth claim. Becomes canon only if receipted and validated.

**Evidence Package**: Collection of artifacts supporting a scientific claim. Required for tournaments and contests.

**Reproducibility**: Complete documentation of how to re-run an agent and get the same result. Includes inputs, method, parameters, hardware, results.

**Validation Check**: A gate that evidence must pass. Examples: NaN/Inf check, bounds check, consistency check, citation check.

**Claim**: A statement asserting something is true. Becomes canon only via receipt-backed evidence.

## Plane Terms

**Control**: Where intentions become missions. Where rules are written. Where governance lives.

**Execution**: Where agents work. Where simulations run. Where code executes. Outputs are proposals until receipted.

**Truth**: Canonical committed state. Receipt-backed only. Single source of ground truth.

**Observation**: What humans see. Dashboards, UI, reports. Reflects truth but does not create it.

## Agreement and Policy Terms

**Ontology**: Explicit set of constraints on what scientific claims can be made. Defined in gamma-science. Agents cannot violate ontology constraints.

**Receipt**: See Receipt under State and Truth Terms.

**Harness**: See Harness under Organizational Terms.

**Protocol**: A Hellenic protocol (BETA, ALPHA, GAMMA, DELTA, THETA, GAMMA-BURST). Defines workflow for a task type.

**Patch**: Versioned change event. Reconciliation instructions required. Effect on provisional work must be stated. Affected agents must be notified.

**Inventory**: Each agent has exactly one writable workspace. Contains context.md, current_task.md, skills/, outputs/, evidence/, checkpoints/, handoff.md.

## Motion and Change Terms

**Reconciliation**: Process of aligning provisional work after a patch or truth update. Required DELTA input if conflicts exist.

**Rebase**: Pulling latest truth and re-validating provisional work. Different from merge (no manual conflict resolution).

**Rollback**: Returning to a prior checkpoint. Used in disaster recovery.

**Escalation**: Moving a conflict or blocker to human decision-maker or judge.

## Validation Terms

**Judge Report**: Control-plane artifact documenting judge evaluation. Decision is PASS/REVISE/FAIL. Not automatically truth; needs receipt.

**Validation Criteria**: Specific checks that evidence must pass. Defined in mission specs and receipt schema.

**Acceptance Criteria**: Definition of when a mission is complete. Defined in mission spec.

**Rejection Criteria**: Explicit list of conditions that cause mission rejection or send to REVISE. Defined in mission spec.

---

© 2026 HNXJ(H.Nejat) / BASTOSLAB / VANDERBILT UNIVERSITY
