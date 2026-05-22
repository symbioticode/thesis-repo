# Epistemic Interface Contract in Distributed Cognitive Systems
## A convergence study across knowledge management, inter-session continuity, and real-time ISR fusion

**Status** : Work in progress — thesis + PoC
**PI** : Andrei
**Timeline** : Thesis J1-J3 · PoC J1-J5

---

## The Question

Several systems developed independently, in distinct constrained domains, have converged
toward the same structural invariants. Is this convergence accidental — an artifact of
a shared cognitive substrate — or does it reflect a real, domain-independent constraint?

This work documents the convergence, proposes a unified formalization, and builds a
minimal proof of concept.

## Repository Structure

```
.
├── MASTER_BRIEF.md          ← single source of truth for all agents
├── AGENT_HANDOFF.md         ← daily coordination between Jules and Claude Code
├── thesis/                  ← written by Jules
│   ├── ch0_genese.md
│   ├── ch1_probleme.md
│   ├── ch2_convergence.md
│   ├── ch3_formalisation.md
│   ├── ch4_implementation.md
│   └── ch5_poc.md
├── poc/                     ← built by Claude Code
│   ├── README.md
│   ├── requirements.txt
│   ├── claim/
│   │   ├── structures.py
│   │   ├── validator.py
│   │   ├── combinator.py
│   │   └── orchestrator.py
│   ├── scenarios/
│   │   ├── scenario_a_sans_claim.py
│   │   └── scenario_b_avec_claim.py
│   └── tests/
└── corpus/
    ├── frameworks/          ← source documents
    └── references/          ← refs.bib
```

## The Three Invariants

Observed independently across six frameworks and validated against three external
domains (FDA GxP, NATO STANAG 4559, NIH genomic audit):

1. **Emitter/interpreter separation** — a node never interprets its own state
2. **Explicit epistemic lifecycle** — every knowledge unit carries a status
3. **Human escalation on unresolved conflict** — the machine never arbitrates alone

## Running the PoC

```bash
pip install -r poc/requirements.txt
python poc/scenarios/scenario_a_sans_claim.py  # demonstrates the problem
python poc/scenarios/scenario_b_avec_claim.py  # demonstrates the solution
```

## Thesis Abstract

*(to be written by Jules after J2)*

---

*Read MASTER_BRIEF.md before contributing anything to this repository.*
