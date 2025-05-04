# ClinicalTurn — Human Explanation

A ClinicalTurn is a **single unit of reasoning**. It’s the moment a doctor thinks:  
"This lab result suggests X." Or "I believe the symptom points toward Y."

Every ClinicalTurn captures:
- What was said/thought (`narrative`)
- Why it was said (linked to an official medical concept — `semantic anchor`)
- What influenced this moment (echoes from earlier thoughts)
- What the doctor intended to do (e.g., rule out, confirm, explore)

### Example (Plain English):

1. Doctor sees jaundice → suspects hepatitis (ICD-10 K70.1)
2. Later doubts it because labs are off → this doubt is an “echo”
