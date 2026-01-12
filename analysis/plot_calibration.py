import json
import matplotlib.pyplot as plt

with open("analysis/calibration_results.json") as f:
    data = json.load(f)

thresholds = [d["threshold"] for d in data]
step_reduction = [d["step_reduction"] for d in data]

plt.figure()
plt.plot(thresholds, step_reduction, marker="o")
plt.xlabel("Similarity Threshold")
plt.ylabel("Steps Reduced")
plt.title("Memory Confidence Calibration Curve")
plt.grid(True)
plt.show()
