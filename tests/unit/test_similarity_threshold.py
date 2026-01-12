from kernel.planner import Planner

def test_low_similarity_does_not_reduce_steps():
    planner = Planner()

    plan = planner.generate_plan(
        goal="Explain Python",
        memory_matches=[("Unrelated task", 0.2)]
    )

    assert len(plan.steps) == 2

def test_high_similarity_reduces_steps():
    planner = Planner()

    plan = planner.generate_plan(
        goal="Explain Python",
        memory_matches=[("Explain Python", 0.9)]
    )

    assert len(plan.steps) == 1
