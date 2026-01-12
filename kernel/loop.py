from kernel.state import CognitiveState
from kernel.task import Task
from kernel.planner import Planner

from memory.vector_memory import VectorMemory
from memory.manager import MemoryManager


class CognitiveKernel:
    def __init__(self):
        self.state = CognitiveState.INIT
        self.task: Task | None = None

        self.planner = Planner()

        # ✅ MEMORY IS NOW FIRST-CLASS
        self.memory_manager = MemoryManager(VectorMemory(use_gpu=False))

        self.error_message: str | None = None

    def load_task(self, goal: str, constraints: str = ""):
        self.task = Task(goal=goal, constraints=constraints)
        self.state = CognitiveState.INTERPRET

    def run(self):
        while self.state not in (CognitiveState.DONE, CognitiveState.ERROR):
            try:
                if self.state == CognitiveState.INTERPRET:
                    self._interpret()
                elif self.state == CognitiveState.PLAN:
                    self._plan()
                elif self.state == CognitiveState.ACT:
                    self._act()
                elif self.state == CognitiveState.OBSERVE:
                    self._observe()
                elif self.state == CognitiveState.DECIDE:
                    self._decide()
            except Exception as e:
                self.error_message = str(e)
                self.state = CognitiveState.ERROR

    def _interpret(self):
        self.state = CognitiveState.PLAN

    def _plan(self):
        # 🔹 Recall memory (safe even if empty)
        _ = self.memory_manager.recall(self.task.goal)

        self.task.plan = self.planner.generate_plan(
            self.task.goal,
            self.task.constraints
        )

        self.state = CognitiveState.ACT

    def _act(self):
        step = self.task.plan.next_step()
        if step is None:
            self.state = CognitiveState.DECIDE
            return

        result = f"Executed: {step.description}"
        self.task.plan.mark_done(result)

        self.state = CognitiveState.OBSERVE

    def _observe(self):
        self.state = CognitiveState.DECIDE

    def _decide(self):
        if self.task.plan.next_step() is None:
            self.task.completed = True

            # ✅ Store episodic memory ONLY on completion
            summary = f"Completed task: {self.task.goal}"
            self.memory_manager.remember_task(self.task.goal, summary)

            self.state = CognitiveState.DONE
        else:
            self.state = CognitiveState.ACT
