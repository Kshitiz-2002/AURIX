from kernel.task import Plan, PlanStep
from typing import List


class Planner:
    def generate_plan(
        self,
        goal: str,
        constraints: str = "",
        memory_context: List[str] | None = None
    ) -> Plan:
        """
        Memory-aware plan generation.
        """

        steps = []

        if memory_context:
            steps.append(
                PlanStep(
                    id=1,
                    description="Reuse prior knowledge relevant to the task"
                )
            )

        steps.append(
            PlanStep(
                id=len(steps) + 1,
                description=f"Analyze the goal: {goal}"
            )
        )

        steps.append(
            PlanStep(
                id=len(steps) + 1,
                description="Produce final answer"
            )
        )

        return Plan(steps=steps)
