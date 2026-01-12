from kernel.loop import CognitiveKernel

def test_multi_step_execution():
    kernel = CognitiveKernel()
    kernel.load_task("Write a simple algorithm")

    kernel.run()

    assert kernel.task.completed
    assert len(kernel.task.plan.steps) >= 2
