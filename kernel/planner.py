from kernel.task import Plan, PlanStep


class Planner:
    def generate_plan(self, goal: str, constraints: str = "") -> Plan:
        """
        Generate a bounded, executable plan.
        MUST return ≤ 5 steps.
        MUST avoid hallucinated tools.
        """

        # Placeholder logic (replace with model later)
        steps = [
            PlanStep(
                id=1,
                description=f"Analyze the goal: {goal}"
            ),
            PlanStep(
                id=2,
                description="Produce final answer"
            )
        ]
        return Plan(steps=steps)
