# plot_roc_curve.py
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# 仕様A の予測確率
y_true = df_proxy["default"]
y_pred = result.predict()

# ROC 曲線
fpr, tpr, _ = roc_curve(y_true, y_pred)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(7,5))
plt.plot(fpr, tpr, label=f"Spec A (AUC = {roc_auc:.3f})")
plt.plot([0,1], [0,1], "k--", label="Random Guess")

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve (Specification A)")
plt.legend()
plt.tight_layout()
plt.savefig("figures/roc_comparison.png", dpi=300)
plt.show()
