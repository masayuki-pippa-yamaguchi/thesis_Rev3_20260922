# ordered_logit_probability_curves_uk_with_cutpoints.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit  # ロジットCDF
import matplotlib.font_manager as fm

# --- 日本語フォント設定（Windows） ---
plt.rcParams['font.family'] = 'Meiryo'

# --- Ordered Logit の推定結果（英国企業） ---
beta_mu = 0.000001656
beta_D  = -0.000746
beta_sigma = -0.020693   # abs_change の係数

# --- cutpoint（英国企業） ---
cut1 = 0.2289
cut2 = -0.9332
cut3 = -0.3374

# --- 線形予測子 xβ の範囲 ---
xb = np.linspace(-1, 1, 300)

# --- ロジットCDF ---
def F(z):
    return expit(z)

# --- 各カテゴリの確率 ---
P0 = F(cut1 - xb)
P1 = F(cut2 - xb) - F(cut1 - xb)
P2 = F(cut3 - xb) - F(cut2 - xb)
P3 = 1 - F(cut3 - xb)

# --- 描画 ---
plt.figure(figsize=(8,6))
plt.plot(xb, P0, label="ステージ0（Active）")
plt.plot(xb, P1, label="ステージ1（Administration）")
plt.plot(xb, P2, label="ステージ2（Liquidation）")
plt.plot(xb, P3, label="ステージ3（Dissolved）")

# --- cutpoint の縦線（赤の破線） ---
plt.axvline(x=cut1, color='red', linestyle='--', linewidth=1.5, label="cut1")
plt.axvline(x=cut2, color='red', linestyle='--', linewidth=1.5, label="cut2")
plt.axvline(x=cut3, color='red', linestyle='--', linewidth=1.5, label="cut3")

plt.xlabel("潜在変数 xβ")
plt.ylabel("確率")
plt.title("Ordered Logit に基づく倒産ステージ確率曲線（英国新電力企業）")
plt.legend()
plt.grid(True)

# --- PNG 保存 ---
plt.savefig("ordered_logit_probability_curves_uk_with_cutpoints.png",
            dpi=300, bbox_inches='tight')

print("PNG ファイルを保存しました： ordered_logit_probability_curves_uk_with_cutpoints.png")
