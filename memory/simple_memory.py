from typing import List, Dict, Any
from memory.interface import MemoryInterface, MemoryItem


class SimpleMemory(MemoryInterface):
    """
    Naive keyword-based cognitive memory.
    CPU-only, deterministic, testable.
    """

    def __init__(self):
        self._store: List[MemoryItem] = []

    def store(self, content: str, metadata: Dict[str, Any]) -> None:
        item = MemoryItem(content=content, metadata=metadata)
        self._store.append(item)

    def retrieve(self, query: str, k: int = 3) -> List[MemoryItem]:
        query = query.lower()
        scored = []

        for item in self._store:
            score = sum(
                1 for word in query.split()
                if word in item.content.lower()
            )
            if score > 0:
                scored.append((score, item))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [item for _, item in scored[:k]]

    def size(self) -> int:
        return len(self._store)
