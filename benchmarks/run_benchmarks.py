import time
import json
from kernel.loop import CognitiveKernel

results = []

kernel = CognitiveKernel()
with open("benchmarks/tasks.json") as f:
    tasks = json.load(f)

for task in tasks:
    start = time.time()

    kernel.load_task(task["goal"])
    kernel.run()

    duration = time.time() - start
    steps = len(kernel.task.plan.steps)

    retrieval_start = time.time()
    _ = kernel.memory_manager.recall(task["goal"])
    retrieval_latency = time.time() - retrieval_start

    matches = kernel.last_memory_matches 
    max_score = (
        float(max(score for _, score in matches))
        if matches else 0.0
    )

    results.append({
        "task_id": task["id"],
        "completed": kernel.task.completed,
        "steps": steps,
        "step_reduced": steps < 2,
        "used_memory": bool(kernel.memory_manager.recall(task["goal"])),
        "latency": duration,
        "memory_items": kernel.memory_manager.stats()["total_items"],
        "retrieval_latency": retrieval_latency,
        "max_similarity": max_score,
        "reasoning_ratio": (
            kernel.task.plan.reasoning_steps /
            len(kernel.task.plan.steps)
        ),
        "overconfidence": (
            kernel.task.plan.reduced and
            kernel.last_max_similarity < 0.85
        ),
        "reasoning_load": kernel.last_reasoning_load
    })

with open("benchmarks/results.json", "w") as f:
    json.dump(results, f, indent=2)
