# Engine — Human Explanation

The Engine is what **runs a clinical simulation**. It’s the interactive part.

This is where you say:
> "The patient presented with symptom X"  
> "I believed it was disease Y"  
> "I was influenced by a prior lab"  
> "Save this step"

### What does it do?

- Adds each thought (`step()`)
- Tracks all steps (`summary()`)
- Exports all reasoning as structured data (`export()`)

### Analogy

Think of this like a **clinical notebook with a brain**:
Each time you think, it logs what you thought, why, and what you meant to do.  
You can play this back later, audit it, or feed it to an AI.

This is the command center of the FIN Protocol.
