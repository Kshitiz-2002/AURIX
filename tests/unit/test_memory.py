from memory.simple_memory import SimpleMemory


def test_store_and_retrieve():
    mem = SimpleMemory()
    mem.store("Python is a programming language", {})

    results = mem.retrieve("python")
    assert len(results) == 1
    assert "Python" in results[0].content
