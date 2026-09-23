import matplotlib.pyplot as plt
from matplotlib import font_manager

# IPAexGothic を絶対パスで指定（最も確実）
plt.rcParams['font.family'] = 'IPAexGothic'
plt.rcParams['font.sans-serif'] = ['IPAexGothic']

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ------------------------------------------------------------
# ロジット関数
# ------------------------------------------------------------
def logistic(x):
    return 1 / (1 + np.exp(-x))

# ------------------------------------------------------------
# パラメータ設定
# ------------------------------------------------------------
gamma_mu_sigma = -1.0   # μ×σ の相互作用（負：収益性がショックを緩和）
gamma_S_D = 1.0         # S×D の相互作用（正：支援能力が負債過多を緩和）

# 固定値（ケースE/Fなどに合わせて調整可能）
S_fixed = 1
D_fixed = 0.5
mu_fixed = 0.0
sigma_fixed = 0.2

# ------------------------------------------------------------
# 1. μ×σ の相互作用の差分サーフェス
# ------------------------------------------------------------

mu_vals = np.linspace(-0.10, 0.10, 50)
sigma_vals = np.linspace(0.05, 0.50, 50)
MU, SIGMA = np.meshgrid(mu_vals, sigma_vals)

# 相互作用なし
Z_base = MU - SIGMA + S_fixed - D_fixed
p_base = logistic(Z_base)

# 相互作用あり
Z_int = MU - SIGMA + S_fixed - D_fixed + gamma_mu_sigma * (MU * SIGMA)
p_int = logistic(Z_int)

# 差分
delta_p = p_int - p_base

# 図の描画
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(MU, SIGMA, delta_p, cmap='coolwarm', edgecolor='none')

ax.set_title("収益性 μ と市場ショック σ の相互作用による倒産確率差分 Δp", fontsize=12)
ax.set_xlabel("収益性 μ", fontsize=11)
ax.set_ylabel("市場ショック σ", fontsize=11)
ax.set_zlabel("倒産確率差分 Δp", fontsize=11)

plt.tight_layout()
plt.savefig("figures/interaction_mu_sigma_surface.png", dpi=300)
plt.close()


# ------------------------------------------------------------
# 2. S×D の相互作用の差分サーフェス
# ------------------------------------------------------------

S_vals = np.linspace(0, 3, 50)
D_vals = np.linspace(0.3, 0.8, 50)
S_grid, D_grid = np.meshgrid(S_vals, D_vals)

# 相互作用なし
Z_base_SD = mu_fixed - sigma_fixed + S_grid - D_grid
p_base_SD = logistic(Z_base_SD)

# 相互作用あり
Z_int_SD = mu_fixed - sigma_fixed + S_grid - D_grid + gamma_S_D * (S_grid * D_grid)
p_int_SD = logistic(Z_int_SD)

# 差分
delta_p_SD = p_int_SD - p_base_SD

# 図の描画
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(S_grid, D_grid, delta_p_SD, cmap='viridis', edgecolor='none')

ax.set_title("支援能力 S と負債比率 D の相互作用による倒産確率差分 Δp", fontsize=12)
ax.set_xlabel("支援能力 S", fontsize=11)
ax.set_ylabel("負債比率 D", fontsize=11)
ax.set_zlabel("倒産確率差分 Δp", fontsize=11)

plt.tight_layout()
plt.savefig("figures/interaction_S_D_surface.png", dpi=300)
plt.close()

print("日本語ラベルの図を生成しました。figures フォルダを確認してください。")
