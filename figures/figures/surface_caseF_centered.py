# ファイル名：surface_caseF_centered.py

import matplotlib
matplotlib.use("Agg")  # GUI を完全に無効化して安定化

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# 日本語フォント設定
plt.rcParams["font.family"] = "IPAexGothic"
plt.rcParams["axes.unicode_minus"] = False

# ==== ケースFのパラメータ ====
D = 0.5
S = 2.0

# Z ≈ 0 の中心値（崖の位置）
center = D - S   # = -1.5

# ==== μ・σ の範囲を Z ≈ 0 に寄せる ====
mu_vals = np.linspace(center - 0.1, center + 0.1, 100)
sigma_vals = np.linspace(center - 0.1, center + 0.1, 100)

MU, SIGMA = np.meshgrid(mu_vals, sigma_vals)

# ==== Z と p ====
Z = MU - SIGMA + S - D
p = 1 / (1 + np.exp(-Z))

# ==== 3D プロット ====
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

surf = ax.plot_surface(
    MU, SIGMA, p,
    cmap=cm.viridis,
    linewidth=0,
    antialiased=True,
)

# 真横視点
ax.view_init(elev=20, azim=0)

ax.set_xlabel(r"$\mu$", fontsize=12)
ax.set_ylabel(r"$\sigma$", fontsize=12)
ax.set_zlabel("倒産確率 p", fontsize=12)
ax.set_title("ケースF：Z≈0 付近を中心にした倒産確率サーフェス", fontsize=14)

fig.colorbar(surf, shrink=0.5, aspect=10)

plt.tight_layout()

# ==== PNG 保存 ====
plt.savefig("surface_caseF_centered.png", dpi=300)
