from kernel.planner import Planner

def test_reasoning_ratio_reduced_plan():
    planner = Planner(similarity_threshold=0.5)
    plan = planner.generate_plan(
        goal="Explain Python",
        memory_matches=[("Explain Python", 0.9)]
    )

    assert plan.reduced
    assert plan.reasoning_steps == 0

def test_reasoning_ratio_reduced_plan():
    planner = Planner(similarity_threshold=0.5)
    plan = planner.generate_plan(
        goal="Explain Python",
        memory_matches=[("Explain Python", 0.9)]
    )

    assert plan.reduced
    assert plan.reasoning_steps == 0
