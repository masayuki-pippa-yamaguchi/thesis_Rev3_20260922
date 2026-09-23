# sign_surface_mu_wide.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams

rcParams['font.family'] = 'Yu Gothic'

D = np.linspace(0, 1.0, 50)
sigma = np.linspace(0, 1.0, 50)
Dg, Sg = np.meshgrid(D, sigma)

mu_values = [-0.10, 0.05, 0.50]
titles = ["赤字企業 μ=-0.10", "平均的収益性 μ=0.05", "超高収益企業 μ=0.50"]

vmin = -2
vmax = 2

for mu, title in zip(mu_values, titles):

    Z = mu - 1.2*Sg - 1.5*Dg

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(Dg, Sg, Z, cmap='viridis', alpha=0.85,
                           vmin=vmin, vmax=vmax)

    ax.set_xlabel("負債比率 D", fontsize=12)
    ax.set_ylabel("市場ショック σ", fontsize=12)
    ax.set_zlabel("倒産距離 Z", fontsize=12)
    ax.set_title(f"倒産距離 Z の構造：{title}", fontsize=14)

    # ファイル名は ASCII の "-" に強制変換
    safe_mu = str(mu).replace("−", "-")

    plt.savefig(f"Python/figures/sign_surface_mu_{safe_mu}.png",
                dpi=300, bbox_inches='tight')
    plt.close(fig)
