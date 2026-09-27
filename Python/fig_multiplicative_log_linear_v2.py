# fig_multiplicative_log_linear_v2.py

import numpy as np
import matplotlib.pyplot as plt
import os

# 保存先ディレクトリ（あなたの環境に合わせて固定）
OUTDIR = r"d:\texlive\2026\work\thesis_Rev3_20260922\Python\figures"

# -----------------------------
# (a) multiplicative structure
# -----------------------------
t = np.linspace(0, 5, 500)
mu = 1.0
sigma = 0.15

np.random.seed(0)
W = np.random.normal(0, np.sqrt(1/500), size=500).cumsum()
V = np.exp(mu * t + sigma * W)

plt.figure(figsize=(5, 3))
plt.plot(t, V, color="darkblue")
plt.title("Multiplicative structure (clear exponential growth)")
plt.xlabel("Time")
plt.ylabel("Firm value V(t)")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "multiplicative_structure.png"), dpi=300)
plt.close()

# -----------------------------
# (b) log transform
# -----------------------------
logV = np.log(V)

plt.figure(figsize=(5, 3))
plt.plot(t, logV, color="darkgreen")
plt.title("Log transform: log(V(t)) becomes additive")
plt.xlabel("Time")
plt.ylabel("log V(t)")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "log_transform.png"), dpi=300)
plt.close()

# -----------------------------
# (c) linear DD structure
# -----------------------------
V_ratio = np.linspace(0.5, 2.0, 200)
DD = np.log(V_ratio)

plt.figure(figsize=(5, 3))
plt.plot(V_ratio, DD, color="darkred")
plt.axhline(0, color="black", linestyle="--", linewidth=1)
plt.title("Linear DD structure: log(V/F)")
plt.xlabel("V / F")
plt.ylabel("Distance to Default (DD)")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "linear_dd.png"), dpi=300)
plt.close()
