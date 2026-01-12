from memory.vector_memory import VectorMemory


def test_vector_store_and_retrieve():
    mem = VectorMemory(use_gpu=False)
    mem.store("Python is a programming language", {})

    results = mem.retrieve("What is Python?")
    assert len(results) >= 1
    assert "Python" in results[0].content
