import time
import json
from kernel.loop import CognitiveKernel

results = []

with open("benchmarks/tasks.json") as f:
    tasks = json.load(f)

for task in tasks:
    kernel = CognitiveKernel()
    start = time.time()

    kernel.load_task(task["goal"])
    kernel.run()

    duration = time.time() - start
    steps = len(kernel.task.plan.steps)

    retrieval_start = time.time()
    _ = kernel.memory_manager.recall(task["goal"])
    retrieval_latency = time.time() - retrieval_start

    results.append({
        "task_id": task["id"],
        "completed": kernel.task.completed,
        "steps": steps,
        "used_memory": bool(kernel.memory_manager.recall(task["goal"])),
        "latency": duration,
        "memory_items": kernel.memory_manager.stats()["total_items"],
        "retrieval_latency": retrieval_latency
    })

with open("benchmarks/results.json", "w") as f:
    json.dump(results, f, indent=2)
