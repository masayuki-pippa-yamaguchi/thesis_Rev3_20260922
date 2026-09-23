# ファイル名：contour_caseC.py

import matplotlib
matplotlib.use("Agg")  # 非GUIで安定動作

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# 日本語フォント設定
plt.rcParams["font.family"] = "IPAexGothic"
plt.rcParams["axes.unicode_minus"] = False

# ---- ケースC ----
D = 0.8
S = 0.0

# ---- μ・σ のグリッド ----
mu_vals = np.linspace(-0.10, 0.10, 200)
sigma_vals = np.linspace(0.05, 0.50, 200)
MU, SIGMA = np.meshgrid(mu_vals, sigma_vals)

# ---- Z と p ----
Z = MU - SIGMA + S - D
p = 1 / (1 + np.exp(-Z))

# ---- 等高線プロット ----
fig, ax = plt.subplots(figsize=(7, 6))

cont = ax.contourf(
    MU, SIGMA, p,
    levels=20,
    cmap=cm.viridis
)

# Z=0（倒産境界線）を強調
boundary = ax.contour(
    MU, SIGMA, Z,
    levels=[0],
    colors='red',
    linewidths=2
)

ax.clabel(boundary, fmt="Z=0", fontsize=10)

ax.set_xlabel(r"$\mu$", fontsize=12)
ax.set_ylabel(r"$\sigma$", fontsize=12)
ax.set_title("ケースC：倒産確率の等高線図（top view）", fontsize=14)

fig.colorbar(cont, label="倒産確率 p")

plt.tight_layout()
plt.savefig("contour_caseC.png", dpi=300)
