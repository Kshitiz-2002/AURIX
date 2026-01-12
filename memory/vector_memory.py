import faiss
import numpy as np
from typing import List, Dict, Any, Tuple

from sentence_transformers import SentenceTransformer
from memory.interface import MemoryInterface, MemoryItem


class VectorMemory(MemoryInterface):
    """
    Vector-based semantic memory (RAG).
    CPU-first, GPU-optional.
    """

    def __init__(
        self,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
        use_gpu: bool = False
    ):
        self.embedder = SentenceTransformer(model_name)

        if use_gpu:
            self.embedder = self.embedder.to("cuda")

        self.dim = self.embedder.get_sentence_embedding_dimension()
        self.index = faiss.IndexFlatL2(self.dim)

        self.items: List[MemoryItem] = []

    def store(self, content: str, metadata: Dict[str, Any]) -> None:
        embedding = self.embedder.encode([content], convert_to_numpy=True)
        embedding = embedding.astype("float32")

        self.index.add(embedding)
        self.items.append(MemoryItem(content, metadata))

    def retrieve(self, query: str, k: int = 3) -> List[MemoryItem]:
        if len(self.items) == 0:
            return []

        query_vec = self.embedder.encode([query], convert_to_numpy=True)
        query_vec = query_vec.astype("float32")

        distances, indices = self.index.search(query_vec, min(k, len(self.items)))

        results = []
        for idx in indices[0]:
            if idx != -1:
                results.append(self.items[idx])

        return results

    def size(self) -> int:
        return len(self.items)
    
    def retrieve_with_scores(
        self,
        query: str,
        k: int = 3
    ) -> List[Tuple[MemoryItem, float]]:
        if len(self.items) == 0:
            return []

        query_vec = self.embedder.encode([query], convert_to_numpy=True).astype("float32")
        distances, indices = self.index.search(query_vec, min(k, len(self.items)))

        results = []
        for idx, dist in zip(indices[0], distances[0]):
            if idx != -1:
                similarity = 1 / (1 + dist)  # simple, monotonic
                results.append((self.items[idx], similarity))

        return results
