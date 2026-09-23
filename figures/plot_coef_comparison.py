# plot_coef_comparison.py
import numpy as np
import matplotlib.pyplot as plt

# 真の係数
true_coef = {
    "mu": 1.0,
    "sigma": -1.0,
    "S": 0.8,
    "D": -1.2
}

# 推定係数（Notebook 内の result を使用）
estimated_coef = {
    "mu": result.params["mu"],
    "sigma": result.params["sigma"],
    "S": result.params["S"],
    "D": result.params["D"]
}

labels = list(true_coef.keys())
true_vals = [true_coef[k] for k in labels]
est_vals = [estimated_coef[k] for k in labels]

x = np.arange(len(labels))
width = 0.35

plt.figure(figsize=(8,5))
plt.bar(x - width/2, true_vals, width, label="True Coef")
plt.bar(x + width/2, est_vals, width, label="Estimated Coef")

plt.xticks(x, labels)
plt.ylabel("Coefficient Value")
plt.title("True vs Estimated Coefficients (Specification A)")
plt.legend()
plt.tight_layout()
plt.savefig("figures/coef_comparison.png", dpi=300)
plt.show()
