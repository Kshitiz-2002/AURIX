from kernel.loop import CognitiveKernel

def test_reasoning_load_reduced_on_repeat_task():
    kernel = CognitiveKernel()

    # First run (no memory)
    kernel.load_task("Explain Python")
    kernel.run()
    first_load = kernel.last_reasoning_load

    # Second run (memory present)
    kernel.load_task("Explain Python")
    kernel.run()
    second_load = kernel.last_reasoning_load

    assert second_load < first_load

def test_reasoning_load_nonzero_for_new_task():
    kernel = CognitiveKernel()
    kernel.load_task("Design a new algorithm")
    kernel.run()

    assert kernel.last_reasoning_load > 0.0