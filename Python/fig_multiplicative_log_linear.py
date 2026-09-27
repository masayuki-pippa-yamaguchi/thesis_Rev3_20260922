# fig_multiplicative_log_linear.py

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# (a) multiplicative structure
# -----------------------------
t = np.linspace(0, 1, 200)
mu = 0.5
sigma = 0.4
np.random.seed(0)
W = np.random.normal(0, np.sqrt(1/200), size=200).cumsum()
V = np.exp(mu * t + sigma * W)  # GBM のイメージ

plt.figure(figsize=(5, 3))
plt.plot(t, V, color="darkblue")
plt.title("Multiplicative structure (GBM-like)")
plt.xlabel("Time")
plt.ylabel("Firm value V(t)")
plt.tight_layout()
plt.savefig("multiplicative_structure.png", dpi=300)
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
plt.savefig("log_transform.png", dpi=300)
plt.close()

# -----------------------------
# (c) linear DD structure
# -----------------------------
V_ratio = np.linspace(0.5, 2.0, 200)
DD = np.log(V_ratio)  # 倒産距離の線形構造（log(V/F)）

plt.figure(figsize=(5, 3))
plt.plot(V_ratio, DD, color="darkred")
plt.axhline(0, color="black", linestyle="--", linewidth=1)
plt.title("Linear DD structure: log(V/F)")
plt.xlabel("V / F")
plt.ylabel("Distance to Default (DD)")
plt.tight_layout()
plt.savefig("linear_dd.png", dpi=300)
plt.close()
