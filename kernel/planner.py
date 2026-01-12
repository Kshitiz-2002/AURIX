from kernel.task import Plan, PlanStep
from typing import List, Tuple

SIMILARITY_THRESHOLD = 0.75  

class Planner:
    def generate_plan(
        self,
        goal: str,
        constraints: str = "",
        memory_context: List[str] | None = None, 
        memory_matches: List[Tuple[str, float]] | None = None
    ) -> Plan:
        if memory_context and not memory_matches:
            memory_matches = [(text, 0.9) for text in memory_context]
            
        high_confidence = False

        if memory_matches:
            max_similarity = max(score for _, score in memory_matches)
            high_confidence = max_similarity >= SIMILARITY_THRESHOLD

        if high_confidence:
            return Plan(steps=[
                PlanStep(
                    id=1,
                    description="Produce final answer using high-confidence prior experience"
                )
            ])

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