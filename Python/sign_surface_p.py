# sign_surface_p.py  ← ファイル名

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

for mu, title in zip(mu_values, titles):

    # Z_lin の計算
    Z = mu - 1.2*Sg - 1.5*Dg

    # 倒産確率 p = Λ(-Z)
    p = 1 / (1 + np.exp(Z))

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(Dg, Sg, p, cmap='viridis', alpha=0.85)

    ax.set_xlabel("負債比率 D", fontsize=12)
    ax.set_ylabel("市場ショック σ", fontsize=12)
    ax.set_zlabel("倒産確率 p", fontsize=12)
    ax.set_title(f"倒産確率 p の構造：{title}", fontsize=14)

    # ファイル名は ASCII の "-" に統一
    safe_mu = str(mu).replace("−", "-")

    plt.savefig(f"Python/figures/sign_surface_p_{safe_mu}.png",
                dpi=300, bbox_inches='tight')
    plt.close(fig)
