# sign_surface_p_combined.py  ← ファイル名

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams

rcParams['font.family'] = 'Yu Gothic'

# 軸の定義
D = np.linspace(0, 1.0, 50)
sigma = np.linspace(0, 1.0, 50)
Dg, Sg = np.meshgrid(D, sigma)

# μ の3種類
mu_values = [-0.10, 0.05, 0.50]
titles = ["赤字企業 μ=-0.10", "平均的収益性 μ=0.05", "超高収益企業 μ=0.50"]

# Figure 全体を作る
fig = plt.figure(figsize=(18, 6))

# z軸と色のスケールを統一
zmin = 0.0
zmax = 1.0

for i, (mu, title) in enumerate(zip(mu_values, titles), start=1):

    Z = mu - 1.2*Sg - 1.5*Dg
    p = 1 / (1 + np.exp(Z))

    ax = fig.add_subplot(1, 3, i, projection='3d')

    surf = ax.plot_surface(Dg, Sg, p, cmap='viridis',
                           vmin=zmin, vmax=zmax, alpha=0.85)

    ax.set_xlabel("負債比率 D", fontsize=10)
    ax.set_ylabel("市場ショック σ", fontsize=10)
    ax.set_zlabel("倒産確率 p", fontsize=10)
    ax.set_title(title, fontsize=12)

    ax.set_zlim(zmin, zmax)
    ax.view_init(elev=30, azim=230)  # 視点を統一

# カラーバーを共通で表示
fig.colorbar(surf, ax=fig.get_axes(), shrink=0.6, location='right')

plt.savefig("Python/figures/sign_surface_p_combined.png",
            dpi=300, bbox_inches='tight')
plt.close(fig)
