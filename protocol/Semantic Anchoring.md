## FIN™ Protocol — Semantic Anchoring

**Version 1.0 • Authored by Augusto Ochoa Ughini, MD**

---

### Abstract

Semantic Anchoring is the foundational method used in the FIN Protocol to link narrative reasoning to standardized ontological terms, such as ICD-10, SNOMED CT, or FHIR elements. This mechanism enables symbolic alignment between human clinical reasoning and machine-readable structure.

---

### Purpose

To ensure every element of diagnostic narrative can be:
- Mapped to structured medical knowledge
- Audited through semantic traceability
- Evaluated by symbolic or algorithmic systems

---

### Mechanism

Each `ClinicalTurn` in a simulated case includes a `semantic_anchor`, which is a structured tag containing:

- `anchor_code`: the ontology code (e.g., ICD-10: K74.6)
- `anchor_label`: the human-readable label
- `anchor_type`: the source ontology
- `confidence_score`: optional float [0.0–1.0] if probabilistic

```python
{
  "anchor_code": "K74.6",
  "anchor_label": "Other and unspecified cirrhosis of liver",
  "anchor_type": "ICD-10",
  "confidence_score": 0.94
}
```

---

### Standards Supported

- **ICD-10**: disease classification
- **SNOMED CT**: clinical terminology
- **LOINC**: lab codes and units
- **UMLS**: composite meta-thesaurus
- **FHIR CodeSystem**: structured medical record interface

---

### Rationale

Semantic anchoring is what allows:
- Reasoning steps to be meaningfully compared
- Outputs to be integrated with EHR or clinical systems
- The FIN Protocol to be interoperable and explainable

---

### Applications

- Clinical AI model alignment
- Human-AI collaboration in diagnosis
- Narrative quality control
- Semantic versioning of case evolution

---

### Authorship and Licensing

This document is part of the FIN Protocol Framework. Licensed under CC-BY 4.0.

Augusto Ochoa Ughini, MD  
Radiologist · Cognitive Systems Architect  
ORCID: https://orcid.org/0009-0008-2406-2835
