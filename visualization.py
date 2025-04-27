import matplotlib.pyplot as plt
import numpy as np

# Data
steps = [
    "Handwritten",
    "Inbuilt (Baseline)",
    "+ Random Search",
    "+ Hist Method",
    "+ itertools"
]

squarederror_times = [81.14, 72.32, 13.43, 8.82, 7.08]
squaredlogerror_times = [83.46, 71.22, 14.44, 11.52, 9.85]

nyu_purple = "#57068c"
nyu_light_purple = "#bfa5d7"

# Plot
plt.figure(figsize=(10, 6))

# reg:squarederror 用实线
plt.plot(steps, squarederror_times, marker='o', label="reg:squarederror", color=nyu_purple, linewidth=2, linestyle='-')

# reg:squaredlogerror 用虚线
plt.plot(steps, squaredlogerror_times, marker='s', label="reg:squaredlogerror", color=nyu_light_purple, linewidth=2, linestyle='--')

# Titles and labels
plt.title("Training Time per Objective Function (Optimization Steps)", fontsize=18, fontweight='bold')
plt.xlabel("Optimization Step", fontsize=14)
plt.ylabel("Total Training Time (seconds)", fontsize=14)

# Grid and layout
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=15)
plt.legend(fontsize=12)
plt.tight_layout()

plt.show()