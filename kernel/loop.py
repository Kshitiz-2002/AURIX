from kernel.state import CognitiveState
from kernel.task import Task
from kernel.planner import Planner

from memory.vector_memory import VectorMemory
from memory.manager import MemoryManager


class CognitiveKernel:
    """
    Central cognitive control loop.
    """

    def __init__(self, similarity_threshold: float = 0.75):
        self.state = CognitiveState.INIT
        self.task: Task | None = None

        # Planner with configurable confidence threshold
        self.planner = Planner(similarity_threshold=similarity_threshold)

        # Memory system
        self.memory_manager = MemoryManager(VectorMemory(use_gpu=False))

        # Instrumentation (for benchmarks & research)
        self.last_memory_matches = []
        self.last_max_similarity: float = 0.0
        self.last_latency: float = 0.0

        self.error_message: str | None = None

    def load_task(self, goal: str, constraints: str = ""):
        self.task = Task(goal=goal, constraints=constraints)
        self.state = CognitiveState.INTERPRET

    def run(self):
        import time

        start = time.time()

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

        self.last_latency = time.time() - start

    def _interpret(self):
        self.state = CognitiveState.PLAN

    def _plan(self):
        # Retrieve memory with similarity scores
        matches = self.memory_manager.recall_with_confidence(self.task.goal)
        self.last_memory_matches = matches
        memory_matches = []
        
        for item, score in matches:
            boosted_score = score
        
            # Exact task identity match → full confidence
            if item.metadata.get("goal") == self.task.goal:
                boosted_score = 1.0
        
            memory_matches.append((item.content, boosted_score))
        self.last_max_similarity = (
            max(score for _, score in memory_matches)
            if memory_matches else 0.0
        )


        plan = self.planner.generate_plan(
            goal=self.task.goal,
            constraints=self.task.constraints,
            memory_matches=memory_matches,
        )

        if plan is None:
            raise RuntimeError("Planner returned None")

        self.last_max_similarity = plan.max_similarity
        self.task.plan = plan

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

            # Store episodic memory ONLY on successful completion
            summary = f"Completed task: {self.task.goal}"
            self.memory_manager.remember_task(self.task.goal, summary)

            self.state = CognitiveState.DONE
        else:
            self.state = CognitiveState.ACT
