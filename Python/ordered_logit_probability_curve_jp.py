# ordered_logit_probability_curve_jp.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit  # ロジスティック関数 Λ(x)

# 日本語フォント設定（警告を消す）
plt.rcParams['font.family'] = 'MS Gothic'
plt.rcParams['axes.unicode_minus'] = False

# ------------------------------------------------------------
# 1. 推定結果（日本企業）の係数と cutpoint を手動で入力
# ------------------------------------------------------------

beta_debt = 0.6262
beta_asset = -1.2143
beta_sigma = 0.0708

tau1 = 2.9675
tau2 = 0.9964

# ------------------------------------------------------------
# 2. 潜在変数 xβ の範囲を設定（論文用に -2 ～ 2）
# ------------------------------------------------------------

x_beta = np.linspace(-2, 2, 400)

# ------------------------------------------------------------
# 3. Ordered Logit の確率式
# ------------------------------------------------------------

P0 = expit(tau1 - x_beta)
P1 = expit(tau2 - x_beta) - expit(tau1 - x_beta)
P2 = 1 - expit(tau2 - x_beta)

# ------------------------------------------------------------
# 4. 図の描画
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(x_beta, P0, label="Stage 0（存続）", linewidth=2)
plt.plot(x_beta, P1, label="Stage 1（財務悪化）", linewidth=2)
plt.plot(x_beta, P2, label="Stage 2（倒産）", linewidth=2)

plt.xlabel("潜在変数 $x\\beta$", fontsize=12)
plt.ylabel("確率", fontsize=12)
plt.title("Ordered Logit に基づく倒産ステージ確率曲線（日本企業）", fontsize=14)

plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)

# ------------------------------------------------------------
# 5. PNG 出力
# ------------------------------------------------------------

plt.savefig("ordered_logit_probability_curve_jp.png", dpi=300, bbox_inches="tight")
plt.close()

print("PNG ファイル 'ordered_logit_probability_curve_jp.png' を出力しました。")
