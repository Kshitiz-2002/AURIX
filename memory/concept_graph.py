from typing import Dict, Set
import re

from memory.concept_types import ConceptNode, ConceptEdge


class ConceptGraph:
    """
    Lightweight semantic concept graph.
    """

    def __init__(self):
        self.nodes: Dict[str, ConceptNode] = {}
        self.edges: Dict[tuple, ConceptEdge] = {}

    def _extract_concepts(self, text: str) -> Set[str]:
        tokens = re.findall(r"[a-zA-Z]{3,}", text.lower())
        return set(tokens)

    def add_task(self, goal: str, plan=None) -> None:
        concepts = self._extract_concepts(goal)

        for c in concepts:
            if c not in self.nodes:
                self.nodes[c] = ConceptNode(id=c, label=c, frequency=0)
            self.nodes[c].frequency += 1

        for src in concepts:
            for tgt in concepts:
                if src == tgt:
                    continue
                key = (src, tgt)
                if key not in self.edges:
                    self.edges[key] = ConceptEdge(source=src, target=tgt)
                self.edges[key].weight += 1.0

    def graph_support_score(self, goal: str) -> float:
        concepts = self._extract_concepts(goal)
        if not concepts:
            return 0.0
        known = sum(1 for c in concepts if c in self.nodes)
        return known / len(concepts)

    def stats(self) -> dict:
        return {
            "concept_nodes": len(self.nodes),
            "concept_edges": len(self.edges),
        }

    # Compatibility helpers
    def add_concepts(self, task: str, concepts: Set[str]) -> None:
        for c in concepts:
            if c not in self.nodes:
                self.nodes[c] = ConceptNode(id=c, label=c, frequency=0)
            self.nodes[c].frequency += 1

    def support_score(self, task: str, concepts: Set[str]) -> float:
        if not concepts:
            return 0.0
        known = sum(1 for c in concepts if c in self.nodes)
        return known / len(concepts)