# GAMMA Skill: MLLM Speed Estimator (TPS)

**agent-source**: mllm-orchestrator
**agent-target**: any

## 🧠 For Agents
This protocol mandates high-fidelity agentic action traces. Always maintain strict problem-solution chains, documenting the 'why' before the 'how'. Ensure every directive is autonomous, verifiable, and free of version suffixes. Map deterministic targets using unified schemas. Execute terminal actions with precision, registering every newly generated skill to the central ledger.

## 🧬 Problem-Solution Architecture (The "Why")

**Q: Why do we need a standardized TPS estimator for MLLM outputs?**
**Problem**: Without a clear metric for inference speed, it's impossible to optimize the orchestration of multiple models (e.g., Qwen-VL vs. Gemma-4) or to detect performance bottlenecks on the remote Mac.
**Solution**: Implement a Python-based speed estimator that calculates Tokens Per Second (TPS) based on output character count and wall-clock duration. This provides empirical data to drive model selection and port mapping.

## 🛠 Skill Implementation

```python
import time

def log_speed_stats(paper_name, model_name, tokens_in, tokens_out, duration):
    """
    Problem: Inconsistent performance reporting across different MLLM models.
    Solution: Standardized TPS calculation logic for persistent logging.
    """
    tps = tokens_out / duration if duration > 0 else 0
    log_msg = f"SPEED STATS: {model_name} on {paper_name} : {tps:.2f} TPS"
    
    # Logic: Append stats to a project-specific speed ledger
    with open("logs/mllm_speed_ledger.txt", "a") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {log_msg}\n")
    
    return tps
```

## 📜 Metadata & Deployment
- **Category**: Performance Optimization
- **Trigger**: Automatic calculation after every `run_evaluation_phase` completion.
- **Ledger**: Registered to `/Users/HN/MLLM/logs/` as the primary performance audit trail.
- **Non-Suffix**: This script replaces all previous telemetry methods without version increments.

```