# CaseSimulation — Human Explanation

This is the full **clinical reasoning timeline**.  
It connects individual thoughts (`ClinicalTurn`s) into a narrative chain.

### What does it do?

- Stores all steps of a diagnostic simulation
- Tracks when it started
- Exports the entire thought process in structured JSON

### Analogy

Think of a **CaseSimulation** as a full **conversation with yourself** over time.  
Each turn is a moment of thinking — and together they tell a story.

> "The patient had jaundice."  
> → "I thought it was hepatitis."  
> → "But the labs didn’t match."  
> → "I changed my mind to biliary obstruction."

This entire reasoning sequence is the simulation.
