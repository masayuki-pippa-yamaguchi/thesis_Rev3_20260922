# logit_surface_sigma_D.py
#
# ロジット推計の係数を用いて、
# 倒産確率 p(σ, D) の 3D サーフェスを描画し、
# logit_surface_sigma_D.pdf として保存する。

import matplotlib.pyplot as plt
from matplotlib import font_manager

# 日本語フォントの設定（IPAexフォント）
plt.rcParams['font.family'] = 'IPAexGothic'

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (for 3D projection)

# ==== 1. ロジット推計結果の係数を設定 ====
# ここは Masayuki さんの推計結果に合わせて書き換えてください。
beta0 = -3.0   # 切片
beta1 =  2.0   # σ の係数
beta3 =  1.5   # D の係数
beta4 =  3.0   # σ×D の係数

# ==== 2. 描画範囲の設定 ====
# σ: 市場ショック指標（例：-3 ～ 3）
# D: 負債比率（例：0 ～ 1）
sigma_min, sigma_max = -3.0, 3.0
D_min, D_max         =  0.0, 1.0

n_sigma = 100
n_D     = 100

sigma_grid = np.linspace(sigma_min, sigma_max, n_sigma)
D_grid     = np.linspace(D_min, D_max, n_D)

Sigma, D = np.meshgrid(sigma_grid, D_grid)

# ==== 3. ロジット関数による倒産確率の計算 ====
# p(σ, D) = 1 / (1 + exp( - (β0 + β1 σ + β3 D + β4 σ D) ))
linear_term = beta0 + beta1 * Sigma + beta3 * D + beta4 * Sigma * D
P = 1.0 / (1.0 + np.exp(-linear_term))

# ==== 4. 3D サーフェスプロット ====
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(
    Sigma, D, P,
    cmap=cm.viridis,
    linewidth=0,
    antialiased=True
)

ax.set_xlabel(r'$\sigma$ (市場ショック)', fontsize=12)
ax.set_ylabel(r'$D$ (負債比率)', fontsize=12)
ax.set_zlabel(r'$p(\sigma, D)$ (倒産確率)', fontsize=12)

ax.set_title('ロジット推計に基づく倒産確率サーフェス', fontsize=13)

fig.colorbar(surf, shrink=0.6, aspect=10, label='倒産確率')

plt.tight_layout()

# ==== 5. PDF ファイルとして保存 ====
output_filename = 'logit_surface_sigma_D.pdf'
plt.savefig(output_filename)
print(f'{output_filename} を作成しました。')

plt.close(fig)
