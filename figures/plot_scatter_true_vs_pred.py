# plot_scatter_true_vs_pred.py
import matplotlib.pyplot as plt

# 真の倒産確率（Step1 の p_true）
p_true = p_true  # Step1 で生成済み
p_pred = result.predict()

plt.figure(figsize=(7,5))
plt.scatter(p_true, p_pred, alpha=0.3)
plt.plot([0,1], [0,1], "r--", label="45-degree line")

plt.xlabel("True Default Probability")
plt.ylabel("Predicted Default Probability")
plt.title("True vs Predicted Default Probability (Spec A)")
plt.legend()
plt.tight_layout()
plt.savefig("figures/scatter_true_vs_pred.png", dpi=300)
plt.show()
