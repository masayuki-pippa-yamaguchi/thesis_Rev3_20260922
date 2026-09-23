# dd_normal_plot.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(-3.5, 3.5, 400)
y = norm.pdf(x)

DD = -1.2
y_DD = norm.pdf(DD)

plt.figure(figsize=(6, 4))
plt.plot(x, y, color='black', linewidth=2)

# DD の赤線
plt.plot([DD, DD], [0, y_DD], color='red', linewidth=2)

# ★ ここを調整：y 座標を少し下げる
plt.text(DD, -0.06, 'DD', color='red', ha='center')

# 塗りつぶし
x_fill = np.linspace(-3.5, DD, 200)
plt.fill_between(x_fill, norm.pdf(x_fill), color='blue', alpha=0.2)

plt.xlabel("Z")
plt.ylabel("Density")
plt.xlim(-3.5, 3.5)
plt.ylim(0, 0.45)
plt.grid(False)

plt.savefig("dd_normal.png", dpi=300, bbox_inches='tight')
plt.savefig("dd_normal.pdf", bbox_inches='tight')
