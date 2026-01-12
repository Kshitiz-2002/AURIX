from kernel.loop import CognitiveKernel


def test_concept_graph_enables_partial_reduction():
    kernel = CognitiveKernel()

    # First task populates concept graph
    kernel.load_task("Explain Python lists")
    kernel.run()

    # New but conceptually related task
    kernel.load_task("Explain Python tuples")
    kernel.run()

    plan = kernel.task.plan

    # Should reduce steps due to shared concepts
    assert plan.step_reduced is True

    # But should NOT be a full shortcut
    assert plan.reasoning_load > 0.0
    assert plan.reasoning_load <= 1.0

    # Single-step, light reasoning
    assert len(plan.steps) == 1
    assert plan.steps[0].is_reasoning is True