# Evidence Map Schema Specification

Evidence maps are the primary artifacts for recording scientific grounding and findings.

## Fields
- **source_id:** Reference to the source (paper, dataset, simulation).
- **agent_id:** The agent that extracted the data.
- **confidence_score:** (0.0 to 1.0) model-rated confidence.
- **falsification_links:** References to evidence that contradicts this finding.
- **mechanistic_layer:** The level of description (e.g., synaptic, circuit, behavioral).
- **receipt_link:** Link to the execution receipt that produced this map.

