# sign_structure.py  ← ファイル名

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import rcParams

# 日本語フォント設定（環境に応じて変更）
# Windows なら "MS Gothic" や "Yu Gothic" が入っていることが多いです。
rcParams['font.family'] = 'Yu Gothic'  # うまくいかなければ 'MS Gothic' に変更

fig, ax = plt.subplots(figsize=(6, 8))

def draw_box(x, y, text):
    ax.add_patch(
        patches.FancyBboxPatch(
            (x, y), 3.0, 0.9,
            boxstyle="round,pad=0.3",
            linewidth=1.2,
            edgecolor="black",
            facecolor="white"
        )
    )
    ax.text(x + 1.5, y + 0.45, text, ha='center', va='center', fontsize=11)

# ノード配置（縦方向をきれいに揃える）
draw_box(0.0, 6.0, r"$\mu$\n収益性")
draw_box(3.5, 6.0, r"$\sigma$\n市場ショック")
draw_box(7.0, 6.0, r"$D$\n負債比率")

draw_box(3.5, 4.2, r"$Z_{\text{lin}}$\n倒産距離")
draw_box(3.5, 2.4, r"$p=\Lambda(-Z_{\text{lin}})$\n倒産確率")
draw_box(3.5, 0.6, r"倒産ステージ\n$\{0,1,2\}$")

# 矢印（始点・終点をきちんと揃える）
ax.annotate("", xy=(3.5, 4.2), xytext=(1.5, 6.0), arrowprops=dict(arrowstyle="->"))
ax.text(2.0, 5.2, "-", fontsize=13)

ax.annotate("", xy=(3.5, 4.2), xytext=(5.0, 6.0), arrowprops=dict(arrowstyle="->"))
ax.text(5.3, 5.2, "+", fontsize=13)

ax.annotate("", xy=(3.5, 4.2), xytext=(8.5, 6.0), arrowprops=dict(arrowstyle="->"))
ax.text(8.8, 5.2, "+", fontsize=13)

ax.annotate("", xy=(3.5, 2.4), xytext=(3.5, 4.2), arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(3.5, 0.6), xytext=(3.5, 2.4), arrowprops=dict(arrowstyle="->"))

# 軸の非表示
ax.set_xlim(-0.5, 10.0)
ax.set_ylim(0.0, 7.5)
ax.axis('off')

plt.savefig("sign_structure.png", dpi=300, bbox_inches='tight')
plt.show()
