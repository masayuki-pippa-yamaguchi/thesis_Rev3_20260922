# sign_surface.py  ← ファイル名

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams

# 日本語フォント
rcParams['font.family'] = 'Yu Gothic'

# 軸の定義
D = np.linspace(0, 1.0, 50)      # 負債比率
sigma = np.linspace(0, 1.0, 50)  # 市場ショック
Dg, Sg = np.meshgrid(D, sigma)

# μ を複数の値で変化させる
mu_values = [0.02, 0.05, 0.08]   # 収益性の例

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

for mu in mu_values:
    Z = mu - 1.2*Sg - 1.5*Dg   # 倒産距離の線形構造（例）
    ax.plot_surface(Dg, Sg, Z, alpha=0.5, cmap='viridis')

# 軸ラベル
ax.set_xlabel("負債比率 D", fontsize=12)
ax.set_ylabel("市場ショック σ", fontsize=12)
ax.set_zlabel("倒産距離 Z", fontsize=12)
ax.set_title("倒産距離 Z の構造（符号条件の視覚化）", fontsize=14)

plt.savefig("sign_surface.png", dpi=300, bbox_inches='tight')
plt.show()
