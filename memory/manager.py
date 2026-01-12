from memory.interface import MemoryInterface


class MemoryManager:
    """
    Kernel-facing memory manager.
    """

    def __init__(self, memory: MemoryInterface):
        self.memory = memory

    def remember_task(self, goal: str, summary: str):
        self.memory.store(
            content=summary,
            metadata={"type": "episodic", "goal": goal}
        )

    def recall(self, query: str, k: int = 3):
        return self.memory.retrieve(query, k=k)

    def stats(self):
        return {
            "total_items": self.memory.size()
        }
