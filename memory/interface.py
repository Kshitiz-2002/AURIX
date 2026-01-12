from abc import ABC, abstractmethod
from typing import List, Dict, Any 

class MemoryItem:
    def __init__(self, content: str, metadata: Dict[str, Any]):
        self.content = content
        self.metadata = metadata
        


class MemoryInterface(ABC):
    """
    Cognitive Memory Interface
    """
    @abstractmethod
    def store(self, content: str, metadata: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def retrieve(self, query: str, k: int = 3) -> List[MemoryItem]:
        pass

    @abstractmethod
    def size(self) -> int:
        pass