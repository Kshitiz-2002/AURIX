from kernel.task import Plan, PlanStep

def test_reasoning_load_full_plan():
    plan = Plan(
        steps=[
            PlanStep(1, "Analyze", is_reasoning=True),
            PlanStep(2, "Answer", is_reasoning=False),
        ]
    )

    assert plan.reasoning_load == 0.5

def test_reasoning_load_no_reasoning():
    plan = Plan(
        steps=[
            PlanStep(1, "Answer", is_reasoning=False),
        ]
    )

    assert plan.reasoning_load == 0.0

def test_reasoning_load_light_reasoning():
    plan = Plan(
        steps=[
            PlanStep(1, "Light reasoning", is_reasoning=True),
        ]
    )

    assert plan.reasoning_load == 1.0
