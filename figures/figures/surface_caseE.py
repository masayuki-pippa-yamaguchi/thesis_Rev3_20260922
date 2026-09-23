import matplotlib
# ==== GUI を安定させるために QtAgg を使用 ====
matplotlib.use("QtAgg")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ==== 1. 日本語フォント設定 ====
plt.rcParams["font.family"] = "IPAexGothic"   # 環境に合わせて変更
plt.rcParams["axes.unicode_minus"] = False

# ==== 2. パラメータ設定（ケースE：D=0.5, S=1） ====
D = 0.5
S = 1.0

mu_vals = np.linspace(-0.10, 0.10, 100)
sigma_vals = np.linspace(0.05, 0.50, 100)
MU, SIGMA = np.meshgrid(mu_vals, sigma_vals)

# ==== 3. Z_lin と p ====
Z_lin = MU - SIGMA + S - D
p = 1.0 / (1.0 + np.exp(-Z_lin))

# ==== 4. 3D サーフェス ====
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

surf = ax.plot_surface(
    MU, SIGMA, p,
    cmap=cm.viridis,
    linewidth=0,
    antialiased=True,
)

ax.set_xlabel(r"$\mu$（収益性）", fontsize=12)
ax.set_ylabel(r"$\sigma$（市場ショック）", fontsize=12)
ax.set_zlabel("倒産確率 $p$", fontsize=12)
ax.set_title("ケースE：D=0.5, S=1（地域新電力）", fontsize=14)

fig.colorbar(surf, shrink=0.5, aspect=10, label="倒産確率")

plt.tight_layout()

# ==== PNG 保存 ====
plt.savefig("figures/surface_caseE.png", dpi=300)

# ==== GUI 表示 ====
plt.show()
