from kernel.loop import CognitiveKernel


def test_only_repeated_task_reduces_steps():
    kernel = CognitiveKernel()

    kernel.load_task("What is Python?")
    kernel.run()
    steps_first = len(kernel.task.plan.steps)

    kernel.load_task("Plan a project")
    kernel.run()
    steps_second = len(kernel.task.plan.steps)

    kernel.load_task("What is Python?")
    kernel.run()
    steps_third = len(kernel.task.plan.steps)

    assert steps_first == 2
    assert steps_second == 2
    assert steps_third == 1
