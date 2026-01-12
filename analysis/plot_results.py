import json
import matplotlib.pyplot as plt

with open("benchmarks/results.json") as f:
    data = json.load(f)

tasks = [d["task_id"] for d in data]
steps = [d["steps"] for d in data]
latency = [d["latency"] for d in data]

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
