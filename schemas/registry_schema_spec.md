# Registry Schema Specification

The registry is the authoritative ledger of all registered harnesses, skills, and tools in the Gamma ecosystem.

## Registry Metadata
- **registry_id:** "gamma-central-registry".
- **version:** Schema version.
- **timestamp:** ISO 8601 update time.
- **maintainer:** "HNXJ (H. Nejat)".

## Entry Fields
- **entry_id:** Unique entry identifier.
- **type:** (harness, skill, tool, adapter).
- **harness_id:** Reference to the underlying harness/tool.
- **name:** Display name.
- **registration_date:** Timestamp of registration.
- **status:** (active, deprecated, experimental, archived).
- **plane:** Associated GAMMA plane.
- **protocol:** Governing Hellenic protocol.
- **location:** Relative path to the definition or implementation doctrine.

