# src/CaseSimulation.py

from typing import List, Dict
from ClinicalTurn import ClinicalTurn
import uuid
from datetime import datetime


class CaseSimulation:
    def __init__(self, case_id: str = None, description: str = ""):
        self.simulation_id = case_id or str(uuid.uuid4())
        self.description = description
        self.start_time = datetime.utcnow().isoformat()
        self.turns: List[ClinicalTurn] = []

    def add_turn(self, turn: ClinicalTurn):
        self.turns.append(turn)

    def get_summary(self) -> Dict:
        return {
            "simulation_id": self.simulation_id,
            "description": self.description,
            "total_turns": len(self.turns),
            "start_time": self.start_time
        }

    def export_json(self) -> Dict:
        return {
            "simulation_id": self.simulation_id,
            "description": self.description,
            "start_time": self.start_time,
            "turns": [turn.to_dict() for turn in self.turns]
        }
