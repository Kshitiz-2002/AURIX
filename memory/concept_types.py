from dataclasses import dataclass


@dataclass
class ConceptNode:
    id: str
    label: str
    frequency: int = 0


@dataclass
class ConceptEdge:
    source: str
    target: str
    relation: str = "co_occurs"
    weight: float = 0.0