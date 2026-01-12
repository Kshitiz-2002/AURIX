from kernel.planner import Planner


def test_planner_reduces_steps_with_memory():
    planner = Planner()

    plan = planner.generate_plan(
        goal="Explain Python",
        memory_context=["Completed task: Explain Python"]
    )

    assert len(plan.steps) == 1
    assert "prior experience" in plan.steps[0].description
