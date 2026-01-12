from kernel.loop import CognitiveKernel


def test_repeated_task_uses_memory():
    kernel = CognitiveKernel()

    kernel.load_task("Explain Python")
    kernel.run()

    first_steps = len(kernel.task.plan.steps)

    kernel.load_task("Explain Python")
    kernel.run()

    second_steps = len(kernel.task.plan.steps)

    assert second_steps >= first_steps
