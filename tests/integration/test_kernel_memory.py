from kernel.loop import CognitiveKernel


def test_kernel_stores_memory():
    kernel = CognitiveKernel()
    kernel.load_task("Explain Python")
    kernel.run()

    stats = kernel.memory_manager.stats()
    assert stats["total_items"] == 1
