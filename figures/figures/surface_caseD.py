import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ==== 1. 日本語フォント設定 ====
# 環境に合わせて変更してください（例：IPAexGothic）
plt.rcParams["font.family"] = "IPAexGothic"
plt.rcParams["axes.unicode_minus"] = False

# ==== 2. パラメータ設定（ケースD：D=0.8, S=3） ====
D = 0.8
S = 3.0

mu_min, mu_max = -0.10, 0.10
sigma_min, sigma_max = 0.05, 0.50

mu_vals = np.linspace(mu_min, mu_max, 100)
sigma_vals = np.linspace(sigma_min, sigma_max, 100)
MU, SIGMA = np.meshgrid(mu_vals, sigma_vals)

# ==== 3. Z_lin と 倒産確率 p の計算 ====
Z_lin = MU - SIGMA + S - D
p = 1.0 / (1.0 + np.exp(-Z_lin))

# ==== 4. 3D サーフェスプロット ====
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
ax.set_title("ケースD：D=0.8, S=3（大手系・負債過多）", fontsize=14)

fig.colorbar(surf, shrink=0.5, aspect=10, label="倒産確率")

plt.tight_layout()

# LaTeX から読み込む図ファイルとして保存
plt.savefig("figures/surface_caseD.png", dpi=300)
plt.show()
