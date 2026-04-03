# Skill: MLLM Speed Estimator (TPS)

## 🧬 Description
Calculates the Tokens Per Second (TPS) for a reasoning model output based on character count and duration.

## 🛠 Usage
```python
def log_speed_stats(paper_name, model_name, tokens_in, tokens_out, duration):
    tps = tokens_out / duration if duration > 0 else 0
    log_msg = f"SPEED STATS: {model_name} on {paper_name} : {tps:.2f} TPS"
    print(log_msg)
    return tps
```

## 📜 Metadata
- **Agent**: `mllm-orchestrator`
- **Context**: `MLLM-Pipeline-v2`
- **Extracted**: 2026-04-02
