# Gamma Event Composition Rule

An event or quest is defined by component set, composition rule, initial state, update rule, output contract, judge rule, and evidence logging.

## Minimal dynamic event

Prompt(n) = A + P(n) + B

A = role/problem/objective/task frame  
P(n) = current state packet  
B = rules/output skeleton/anti-drift/stop conditions  

## Reverse-order control test

Prompt(n) = B + P(n) + A

## Static independent event

Prompt(i) = A + C + T(i) + B

Each T(i) is evaluated independently unless explicitly linked.

## Logging requirement

Each turn should log:
- event_id
- turn_index
- composition_order
- components_used
- a_sha256
- p_sha256
- b_sha256
- c_sha256 when present
- full_prompt_sha256
- response_sha256
- judge_verdict
- truth_mode
- truth_bearing_run
- mock_transport
- secret_redaction_pass

## Placement rule

Control/world event YAML belongs in gamma-labyrinth/events/.
Markdown doctrine belongs in gamma-protocol/doctrine/events/.
Runtime-loaded event configs may later live in gamma/config/events/ after adapter implementation.
