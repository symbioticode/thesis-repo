# PoC — Epistemic Interface Contract (CLAIM)
## Protocol for belief fusion and human escalation

This Proof of Concept demonstrates the Transferable Belief Model (TBM) and the CLAIM protocol in a distributed cognitive system.

## Setup

```bash
pip install -r requirements.txt
```

## Running scenarios

- **Scenario A (Naive combination)**: Demonstrates the problem of blind fusion without conflict detection.
  ```bash
  python scenarios/scenario_a_sans_claim.py
  ```

- **Scenario B (CLAIM protocol)**: Demonstrates the detection of conflict, TBM combination, and human escalation.
  ```bash
  python scenarios/scenario_b_avec_claim.py
  ```

## Structure

- `claim/`: Core logic (structures, validator, combinator, orchestrator).
- `scenarios/`: Demonstration scripts.
- `tests/`: Unit tests for core logic.
- `graph.yaml`: Layer 1 SYNAPSE MVP configuration.
