# src/ClinicalTurn.py

from typing import Optional, List, Dict
from datetime import datetime
import uuid


class SemanticAnchor:
    def __init__(self, code: str, label: str, source: str, confidence: Optional[float] = None):
        self.code = code
        self.label = label
        self.source = source
        self.confidence = confidence

    def to_dict(self) -> Dict:
        return {
            "anchor_code": self.code,
            "anchor_label": self.label,
            "anchor_type": self.source,
            "confidence_score": self.confidence
        }


class Echo:
    def __init__(self, source_id: str, impact_level: str, echo_type: str, comment: Optional[str] = None):
        self.source_id = source_id
        self.impact_level = impact_level
        self.echo_type = echo_type
        self.comment = comment
        self.timestamp = datetime.utcnow().isoformat()

    def to_dict(self) -> Dict:
        return {
            "source_id": self.source_id,
            "impact_level": self.impact_level,
            "echo_type": self.echo_type,
            "comment": self.comment,
            "timestamp": self.timestamp
        }


class ClinicalTurn:
    def __init__(
        self,
        narrative: str,
        anchor: SemanticAnchor,
        echoes: Optional[List[Echo]] = None,
        intent: Optional[str] = None
    ):
        self.turn_id = str(uuid.uuid4())
        self.timestamp = datetime.utcnow().isoformat()
        self.narrative = narrative
        self.anchor = anchor
        self.echoes = echoes or []
        self.intent = intent

    def to_dict(self) -> Dict:
        return {
            "turn_id": self.turn_id,
            "timestamp": self.timestamp,
            "narrative": self.narrative,
            "semantic_anchor": self.anchor.to_dict(),
            "echoes": [e.to_dict() for e in self.echoes],
            "intent": self.intent
        }
