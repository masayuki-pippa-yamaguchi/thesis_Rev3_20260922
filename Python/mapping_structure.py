# mapping_structure.py

import matplotlib.pyplot as plt
from matplotlib import font_manager

# 日本語フォント設定（IPAexGothic）
plt.rcParams['font.family'] = 'IPAexGothic'

fig, ax = plt.subplots(figsize=(8, 12))

# ボックススタイル（塗りなし）
box_style = dict(boxstyle="round,pad=0.4", fc="none", ec="black", lw=1.5)

# --- ノード配置（縦方向の階層構造） ---
ax.text(0.5, 0.90, "Merton 型構造モデル\n倒産距離：DD", bbox=box_style, ha="center")
ax.text(0.5, 0.75, "B&S 推定式\nproxyDD によるロジット推定", bbox=box_style, ha="center")
ax.text(0.5, 0.60, "本研究の潜在変数モデル\nZ* = aμ* - bσ* + cS* - dD*", bbox=box_style, ha="center")
ax.text(0.5, 0.45, "Ordered Logit（理論編：4段階）\n閾値：τ1, τ2, τ3", bbox=box_style, ha="center")
ax.text(0.5, 0.30, "Ordered Logit（実証編：3段階）\n観測可能性に基づく 3 区分", bbox=box_style, ha="center")

# --- 矢印（縦方向に正確に接続） ---
arrow_style = dict(arrowstyle="->", lw=2)

ax.annotate("", xy=(0.5, 0.78), xytext=(0.5, 0.87), arrowprops=arrow_style)
ax.annotate("", xy=(0.5, 0.63), xytext=(0.5, 0.72), arrowprops=arrow_style)
ax.annotate("", xy=(0.5, 0.48), xytext=(0.5, 0.57), arrowprops=arrow_style)
ax.annotate("", xy=(0.5, 0.33), xytext=(0.5, 0.42), arrowprops=arrow_style)

ax.axis("off")

plt.savefig("mapping_structure_vertical.png", dpi=300, bbox_inches="tight")
plt.show()
