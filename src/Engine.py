# src/Engine.py

from ClinicalTurn import ClinicalTurn, SemanticAnchor, Echo
from CaseSimulation import CaseSimulation


class SimulationEngine:
    def __init__(self, description: str = ""):
        self.simulation = CaseSimulation(description=description)

    def step(self, narrative: str, code: str, label: str, source: str, confidence: float = None, echoes: list = None, intent: str = None):
        anchor = SemanticAnchor(code=code, label=label, source=source, confidence=confidence)
        echo_objs = [Echo(**e) for e in echoes] if echoes else []

        turn = ClinicalTurn(
            narrative=narrative,
            anchor=anchor,
            echoes=echo_objs,
            intent=intent
        )

        self.simulation.add_turn(turn)

    def export(self):
        return self.simulation.export_json()

    def summary(self):
        return self.simulation.get_summary()
