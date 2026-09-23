# ファイル名：surface_diff_B_minus_C.py

import matplotlib
matplotlib.use("Agg")  # 非GUIで安定動作

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

plt.rcParams["font.family"] = "IPAexGothic"
plt.rcParams["axes.unicode_minus"] = False

# ---- ケースB（大企業・財務安定）----
D_B = 0.3
S_B = 3.0

# ---- ケースC（地方電力・資本支援なし）----
D_C = 0.8
S_C = 0.0

# 共通の μ・σ グリッド（ここは第6章の元の範囲に合わせてもよい）
mu_vals = np.linspace(-0.10, 0.10, 100)
sigma_vals = np.linspace(0.05, 0.50, 100)
MU, SIGMA = np.meshgrid(mu_vals, sigma_vals)

# 各ケースの Z と p
Z_B = MU - SIGMA + S_B - D_B
Z_C = MU - SIGMA + S_C - D_C

p_B = 1 / (1 + np.exp(-Z_B))
p_C = 1 / (1 + np.exp(-Z_C))

# 差分：大企業 − 地方電力
delta_p = p_B - p_C

# 3D サーフェス（差分）
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
ax.set_zlabel(r"$\Delta p = p_{\mathrm{B}} - p_{\mathrm{C}}$", fontsize=12)
ax.set_title("倒産確率差分：大企業（ケースB）− 地方電力・支援なし（ケースC）", fontsize=14)

fig.colorbar(surf, shrink=0.5, aspect=10, label=r"$\Delta p$")

plt.tight_layout()

plt.savefig("surface_diff_B_minus_C.png", dpi=300)
