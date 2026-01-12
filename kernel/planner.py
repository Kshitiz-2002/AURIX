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
        Memory-based step reduction planner.
        """

        # MEMORY HIT → REDUCE STEPS
        if memory_context and len(memory_context) > 0:
            return Plan(steps=[
                PlanStep(
                    id=1,
                    description="Produce final answer using prior experience"
                )
            ])

        # NO MEMORY → FULL REASONING
        return Plan(steps=[
            PlanStep(
                id=1,
                description=f"Analyze the goal: {goal}"
            ),
            PlanStep(
                id=2,
                description="Produce final answer"
            )
        ])
