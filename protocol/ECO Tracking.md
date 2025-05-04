## FIN™ Protocol — ECO Tracking

**Version 1.0 • Authored by Augusto Ochoa Ughini, MD**

---

### Abstract

ECO Tracking (Echo-Consequence Observation) is a semantic and cognitive tracking mechanism used to evaluate how clinical decisions, observations, or errors reverberate across the diagnostic narrative. It provides temporal traceability and enables pattern recognition in reasoning trajectories.

---

### Objective

To design a reproducible system that captures the echoes of prior decisions and their semantic consequences across the clinical timeline. This allows the FIN Protocol to simulate not just decisions, but their aftershocks and cascades.

---

### Conceptual Foundation

ECO Tracking draws from:
- Systems thinking and causal loop modeling
- Medical error tracing (e.g., WHO's International Classification for Patient Safety)
- Temporal logic and diagnostic delay analysis

In FIN, an echo is defined as:

> The semantic footprint of a prior action, which influences or contaminates subsequent reasoning.

---

### Specification

Each `ClinicalTurn` object contains an optional `echo` field:

```python
class ClinicalTurn:
    def __init__(self, turn_id, narrative, semantic_anchor, echo=None):
        self.turn_id = turn_id
        self.narrative = narrative
        self.semantic_anchor = semantic_anchor
        self.echo = echo  # List of echo objects with source, impact, and timestamp
```

Echoes may include:
- Reused assumptions
- Diagnostic inertia
- Bias propagation
- Redundant testing
- Decision fatigue

---

### Use Case

A misinterpreted ultrasound in Turn 03 may cause an echo that affects surgical planning in Turn 07. Tracking this allows the model to simulate human-like clinical blind spots or diagnostic resilience.

---

### Metrics and Metadata

Each echo may be annotated with:
- `echo_source_id`
- `impact_level`: qualitative or numeric scale
- `echo_type`: e.g., cognitive, procedural, emotional
- `timestamp`

These can later be aggregated for reasoning audits.

---

### Clinical and Research Relevance

ECO Tracking supports:
- Simulation of diagnostic cascades
- Validation of hindsight bias in model retrospectives
- Longitudinal auditing of simulated cases

It makes FIN simulations temporally sensitive and behaviorally rich.

---

### Authorship and Licensing

This document is part of the FIN Protocol Framework. Licensed under CC-BY 4.0.

Augusto Ochoa Ughini, MD  
Radiologist · Cognitive Systems Architect  
ORCID: https://orcid.org/0009-0008-2406-2835
