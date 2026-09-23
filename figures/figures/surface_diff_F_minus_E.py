# ファイル名：surface_diff_F_minus_E.py

import matplotlib
matplotlib.use("Agg")  # 非GUIで安定動作

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# 日本語フォント設定
plt.rcParams["font.family"] = "IPAexGothic"
plt.rcParams["axes.unicode_minus"] = False

# ---- ケースE（地域新電力）----
D_E = 0.5
S_E = 1.0

# ---- ケースF（商社系）----
D_F = 0.5
S_F = 2.0

# ---- 共通の μ・σ グリッド ----
mu_vals = np.linspace(-0.10, 0.10, 100)
sigma_vals = np.linspace(0.05, 0.50, 100)
MU, SIGMA = np.meshgrid(mu_vals, sigma_vals)

# ---- 各ケースの Z と p ----
Z_E = MU - SIGMA + S_E - D_E
Z_F = MU - SIGMA + S_F - D_F

p_E = 1 / (1 + np.exp(-Z_E))
p_F = 1 / (1 + np.exp(-Z_F))

# ---- 差分 Δp = pF − pE ----
delta_p = p_F - p_E

# ---- 3D プロット ----
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

surf = ax.plot_surface(
    MU, SIGMA, delta_p,
    cmap=cm.coolwarm,
    linewidth=0,
    antialiased=True,
)

ax.view_init(elev=20, azim=0)

ax.set_xlabel(r"$\mu$", fontsize=12)
ax.set_ylabel(r"$\sigma$", fontsize=12)
ax.set_zlabel(r"$\Delta p = p_{\mathrm{F}} - p_{\mathrm{E}}$", fontsize=12)
ax.set_title("倒産確率差分：商社系（ケースF）− 地域新電力（ケースE）", fontsize=14)

fig.colorbar(surf, shrink=0.5, aspect=10, label=r"$\Delta p$")

plt.tight_layout()

plt.savefig("surface_diff_F_minus_E.png", dpi=300)
