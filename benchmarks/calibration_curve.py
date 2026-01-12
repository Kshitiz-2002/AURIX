import json
from kernel.loop import CognitiveKernel

THRESHOLDS = [0.3, 0.5, 0.7, 0.85, 0.9]
TASK = "Explain Python"

results = []

for tau in THRESHOLDS:
    kernel = CognitiveKernel(similarity_threshold=tau)

    # First run (no memory)
    kernel.load_task(TASK)
    kernel.run()
    base_steps = len(kernel.task.plan.steps)

    # Second run (memory available)
    kernel.load_task(TASK)
    kernel.run()

    reduced_steps = len(kernel.task.plan.steps)

    results.append({
        "threshold": tau,
        "base_steps": base_steps,
        "reduced_steps": reduced_steps,
        "step_reduction": base_steps - reduced_steps,
        "max_similarity": float(kernel.last_max_similarity),
        "latency": kernel.last_latency
    })

with open("analysis/calibration_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("Calibration complete.")
