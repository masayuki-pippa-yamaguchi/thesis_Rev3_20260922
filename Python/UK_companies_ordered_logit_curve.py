import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit  # ロジットCDF
import matplotlib.font_manager as fm

# --- 日本語フォント設定（Windows） ---
plt.rcParams['font.family'] = 'Meiryo'   # ← これが最重要

# --- Ordered Logit の推定結果（あなたの結果） ---
beta_mu = 9.822e-07
beta_D  = -0.000769

tau_01 = 0.4464
tau_12 = -0.9635
tau_23 = -0.3568

# --- 線形予測子 xβ の範囲 ---
xb = np.linspace(-1, 1, 300)

# --- ロジットCDF ---
def F(z):
    return expit(z)

# --- 各カテゴリの確率 ---
P0 = F(tau_01 - xb)
P1 = F(tau_12 - xb) - F(tau_01 - xb)
P2 = F(tau_23 - xb) - F(tau_12 - xb)
P3 = 1 - F(tau_23 - xb)

# --- 描画 ---
plt.figure(figsize=(8,6))
plt.plot(xb, P0, label="ステージ0（Active）")
plt.plot(xb, P1, label="ステージ1（Administration）")
plt.plot(xb, P2, label="ステージ2（Liquidation）")
plt.plot(xb, P3, label="ステージ3（Dissolved）")

plt.xlabel("潜在変数 xβ")
plt.ylabel("確率")
plt.title("Ordered Logit に基づく倒産ステージ確率曲線（英国新電力企業）")
plt.legend()
plt.grid(True)

# --- PNG 保存 ---
plt.savefig("ordered_logit_probability_curves_uk.png", dpi=300, bbox_inches='tight')

print("PNG ファイルを保存しました： ordered_logit_probability_curves_uk.png")
