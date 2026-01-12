from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class PlanStep:
    id: int
    description: str
    is_reasoning: bool = False
    tool: Optional[str] = None
    status: str = "PENDING"
    result: Optional[str] = None


@dataclass
class Plan:
    steps: List[PlanStep] = field(default_factory=list)
    current_step: int = 0
    max_similarity: float = 0.0
    step_reduced: bool = False
    reasoning_steps: int = 0

    def next_step(self) -> Optional[PlanStep]:
        if self.current_step < len(self.steps):
            return self.steps[self.current_step]
        return None

    def mark_done(self, result: str):
        step = self.steps[self.current_step]
        step.status = "DONE"
        step.result = result
        self.current_step += 1

    def mark_failed(self, error: str):
        step = self.steps[self.current_step]
        step.status = "FAILED"
        step.result = error
        self.current_step += 1

    @property
    def reasoning_load(self) -> float:
        if not self.steps:
            return 0.0
        reasoning = sum(1 for s in self.steps if s.is_reasoning)
        return reasoning / len(self.steps)

    @property
    def reduced(self) -> bool:
        return self.step_reduced


@dataclass
class Task:
    goal: str
    constraints: str = ""
    plan: Optional[Plan] = None
    completed: bool = False
