from kernel.loop import CognitiveKernel


def test_repeated_task_reduces_steps():
    kernel = CognitiveKernel()

    # First run (no memory)
    kernel.load_task("Explain Python")
    kernel.run()
    first_steps = len(kernel.task.plan.steps)

    # Second run (memory present)
    kernel.load_task("Explain Python")
    kernel.run()
    second_steps = len(kernel.task.plan.steps)

    assert second_steps < first_steps
