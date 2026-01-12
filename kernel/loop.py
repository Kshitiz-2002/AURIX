from kernel.state import CognitiveState
from kernel.task import Task
from kernel.planner import Planner


class CognitiveKernel:
    def __init__(self):
        self.state = CognitiveState.INIT
        self.task: Task | None = None
        self.planner = Planner()
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

        # Placeholder execution
        result = f"Executed: {step.description}"
        self.task.plan.mark_done(result)
        self.state = CognitiveState.OBSERVE

    def _observe(self):
        self.state = CognitiveState.DECIDE

    def _decide(self):
        if self.task.plan.next_step() is None:
            self.task.completed = True
            self.state = CognitiveState.DONE
        else:
            self.state = CognitiveState.ACT
