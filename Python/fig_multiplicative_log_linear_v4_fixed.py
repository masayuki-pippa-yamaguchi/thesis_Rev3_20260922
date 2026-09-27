# fig_multiplicative_log_linear_v4_fixed.py

import numpy as np
import matplotlib.pyplot as plt
import os

OUTDIR = "d:/texlive/2026/work/thesis_Rev3_20260922"
os.makedirs(OUTDIR, exist_ok=True)

# -----------------------------
# (c) linear DD structure（保存安定版）
# -----------------------------
log_ratio = np.linspace(-1.0, 1.0, 200)
DD = log_ratio

plt.figure(figsize=(5, 3))
plt.plot(log_ratio, DD, color="darkred", label="DD = log(V/F)")
plt.scatter(log_ratio[::20], DD[::20], color="black", s=10)  # ← 点を追加
plt.grid(True)  # ← グリッドを追加
plt.title("(c) Linear DD structure")
plt.xlabel("log(V/F)")
plt.ylabel("DD")
plt.legend()
plt.tight_layout()
plt.savefig(f"{OUTDIR}/linear_dd.png", dpi=300)
plt.close()
