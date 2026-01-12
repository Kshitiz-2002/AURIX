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

    results.append({
        "task_id": task["id"],
        "completed": kernel.task.completed,
        "steps": steps,
        "latency": duration,
        "memory_items": kernel.memory_manager.stats()["total_items"]
    })

with open("benchmarks/results.json", "w") as f:
    json.dump(results, f, indent=2)
