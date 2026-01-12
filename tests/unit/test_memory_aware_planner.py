from kernel.planner import Planner


def test_planner_uses_memory():
    planner = Planner()

    plan = planner.generate_plan(
        goal="Explain Python",
        memory_context=["Completed task: Explain Python"]
    )

    assert len(plan.steps) == 3
    assert "Reuse prior knowledge" in plan.steps[0].description
