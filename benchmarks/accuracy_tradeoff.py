import json
import matplotlib.pyplot as plt

with open("benchmarks/results.json") as f:
    results = json.load(f)

latency = []
accuracy_proxy = []

for r in results:
    reasoning_ratio = (
        0.0 if r["steps"] == 0 else
        (0 if r["step_reduced"] else 1 / r["steps"])
    )

    acc = (
        0.5 * int(r["step_reduced"]) +
        0.3 * (1 - reasoning_ratio) +
        0.2 * r["max_similarity"]
    )

    latency.append(r["latency"])
    accuracy_proxy.append(acc)

points = sorted(zip(latency, accuracy_proxy))
pareto = []
best_acc = -1

for l, a in points:
    if a > best_acc:
        pareto.append((l, a))
        best_acc = a

pl, pa = zip(*pareto)
plt.plot(pl, pa, linestyle="--", marker="o", label="Pareto frontier")
plt.legend()

plt.figure()
plt.scatter(latency, accuracy_proxy)
plt.xlabel("Latency (seconds)")
plt.ylabel("Accuracy Proxy")
plt.title("Accuracy–Latency Tradeoff Curve")
plt.grid(True)
plt.show()

