from kernel.loop import CognitiveKernel


def test_kernel_updates_concept_graph():
    kernel = CognitiveKernel()
    kernel.load_task("Explain Python")
    kernel.run()

    stats = kernel.memory_manager.stats()
    assert stats["concept_nodes"] > 0
