from kernel.task import Plan, PlanStep
from typing import List, Tuple, Optional

DEFAULT_SIMILARITY_THRESHOLD = 0.75
PARTIAL_GRAPH_THRESHOLD = 0.4


class Planner:
    """
    Memory-aware planner with confidence-gated step reduction.
    """

    def __init__(self, similarity_threshold: float = DEFAULT_SIMILARITY_THRESHOLD):
        self.similarity_threshold = similarity_threshold

    def generate_plan(
        self,
        goal: str,
        constraints: str = "",
        memory_context: Optional[List[str]] = None,
        memory_matches: Optional[List[Tuple[str, float]]] = None,
        graph_support: float = 0.0,
    ) -> Plan:

        # Backward compatibility
        if memory_context and not memory_matches:
            memory_matches = [(text, 0.9) for text in memory_context]

        max_similarity = 0.0
        high_confidence = False

        if memory_matches:
            max_similarity = max(score for _, score in memory_matches)
            high_confidence = max_similarity >= self.similarity_threshold

        # ---- Full shortcut (episodic memory) ----
        if high_confidence:
            return Plan(
                steps=[
                    PlanStep(
                        id=1,
                        description="Produce final answer using high-confidence prior experience",
                        is_reasoning=False,
                    )
                ],
                max_similarity=max_similarity,
                step_reduced=True,
                reasoning_steps=0,
            )

        # ---- Partial shortcut (concept graph) ----
        if graph_support >= PARTIAL_GRAPH_THRESHOLD:
            return Plan(
                steps=[
                    PlanStep(
                        id=1,
                        description="Produce final answer with light reasoning using known concepts",
                        is_reasoning=True,
                    )
                ],
                max_similarity=max_similarity,
                step_reduced=True,
                reasoning_steps=1,
            )

        # ---- Full reasoning ----
        return Plan(
            steps=[
                PlanStep(
                    id=1,
                    description=f"Analyze the goal: {goal}",
                    is_reasoning=True,
                ),
                PlanStep(
                    id=2,
                    description="Produce final answer",
                    is_reasoning=False,
                ),
            ],
            max_similarity=max_similarity,
            step_reduced=False,
            reasoning_steps=1,
        )
