import json
import matplotlib.pyplot as plt

with open("benchmarks/results.json") as f:
    data = json.load(f)

tasks = [d["task_id"] for d in data]
steps = [d["steps"] for d in data]
latency = [d["latency"] for d in data]
memory_items = [d["memory_items"] for d in data]
retrieval_latency = [d["retrieval_latency"] for d in data]
step_reduction = [1 if d["step_reduced"] else 0 for d in data]

plt.figure()
plt.bar(tasks, steps)
plt.title("Steps per Task")
plt.ylabel("Steps")
plt.xlabel("Task")
plt.show()

plt.figure()
plt.bar(tasks, latency)
plt.title("Latency per Task")
plt.ylabel("Seconds")
plt.xlabel("Task")
plt.show()

plt.figure()
plt.bar(tasks, memory_items)
plt.title("Memory Growth per Task")
plt.ylabel("Items")
plt.xlabel("Task")
plt.show()

plt.figure()
plt.bar(tasks, retrieval_latency)
plt.title("Retrieval Latency per Task")
plt.ylabel("Items")
plt.xlabel("Task")
plt.show()

plt.figure()
plt.bar(tasks, step_reduction)
plt.title("Step Reduction (1 = Reduced)")
plt.ylabel("Reduction")
plt.xlabel("Task")
plt.show()