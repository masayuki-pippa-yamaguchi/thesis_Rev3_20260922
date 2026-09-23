# bs_surface_caseA.py
# Case A: D=0.3, S=0（独立系・財務健全）

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# --- 日本語フォント設定（IPAexGothic） ---
matplotlib.rcParams['font.family'] = 'IPAexGothic'

# --- B&S の係数設定 ---
alpha = 0.0
beta_mu = -4.0
beta_sigma = 3.0
beta_S = -0.8
beta_D = 2.0

# --- グリッド設定 ---
mu_vals = np.linspace(-0.10, 0.10, 100)
sigma_vals = np.linspace(0.05, 0.50, 100)
MU, SIGMA = np.meshgrid(mu_vals, sigma_vals)

# --- Case A パラメータ ---
S = 0
D = 0.3

# --- B&S 型倒産確率 ---
Z = (alpha
     + beta_mu * MU
     + beta_sigma * SIGMA
     + beta_S * S
     + beta_D * D)

P = 1 / (1 + np.exp(-Z))

# --- プロット ---
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(MU, SIGMA, P, cmap='viridis', edgecolor='none')

ax.set_xlabel(r'$\mu$（収益性）')
ax.set_ylabel(r'$\sigma$（市場ショック）')
ax.set_zlabel('倒産確率')
ax.set_title('B&S 倒産確率サーフェス：ケースA（D=0.3, S=0）')

fig.colorbar(surf, shrink=0.5, aspect=10)
plt.tight_layout()

# --- 保存 ---
plt.savefig('figures/bs_surface_caseA.png', dpi=300)
plt.close()

