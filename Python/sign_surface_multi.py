# sign_surface_multi.py  ← ファイル名

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams

# 日本語フォント設定
rcParams['font.family'] = 'Yu Gothic'

# 軸の定義
D = np.linspace(0, 1.0, 50)
sigma = np.linspace(0, 1.0, 50)
Dg, Sg = np.meshgrid(D, sigma)

# μ の変化を3枚の静止画で表現
mu_values = [0.02, 0.05, 0.08]   # 収益性の例
titles = ["低収益性 μ=0.02", "中収益性 μ=0.05", "高収益性 μ=0.08"]

for mu, title in zip(mu_values, titles):

    Z = mu - 1.2*Sg - 1.5*Dg   # 倒産距離の線形構造（例）

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(Dg, Sg, Z, cmap='viridis', alpha=0.8)

    ax.set_xlabel("負債比率 D", fontsize=12)
    ax.set_ylabel("市場ショック σ", fontsize=12)
    ax.set_zlabel("倒産距離 Z", fontsize=12)
    ax.set_title(f"倒産距離 Z の構造：{title}", fontsize=14)

    plt.savefig(f"sign_surface_{mu}.png", dpi=300, bbox_inches='tight')
    plt.close(fig)   # ← これが重要（次の図へ進む）
