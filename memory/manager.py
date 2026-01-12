from memory.interface import MemoryInterface
from memory.concept_graph import ConceptGraph


class MemoryManager:
    """
    Kernel-facing memory manager.
    """

    def __init__(self, memory: MemoryInterface):
        self.memory = memory
        self.concept_graph = ConceptGraph()

    def remember_task(self, goal: str, summary: str, plan=None):
        self.memory.store(
            content=summary,
            metadata={"type": "episodic", "goal": goal},
        )
        self.concept_graph.add_task(goal, plan)

    def recall(self, query: str, k: int = 3):
        return self.memory.retrieve(query, k=k)

    def recall_with_confidence(self, query: str):
        if hasattr(self.memory, "retrieve_with_scores"):
            return self.memory.retrieve_with_scores(query)
        return []

    def graph_support(self, goal: str) -> float:
        return self.concept_graph.graph_support_score(goal)

    def stats(self):
        stats = {"total_items": self.memory.size()}
        stats.update(self.concept_graph.stats())
        return stats