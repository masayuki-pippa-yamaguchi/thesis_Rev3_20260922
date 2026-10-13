# ordered_logit_probability_curve_jp_with_cutpoints.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit  # ロジスティック関数 Λ(x)

# 日本語フォント設定
plt.rcParams['font.family'] = 'MS Gothic'
plt.rcParams['axes.unicode_minus'] = False

# ------------------------------------------------------------
# 1. 推定結果（日本企業）の cutpoint
# ------------------------------------------------------------
tau1 = 2.9675
tau2 = 0.9964

# ------------------------------------------------------------
# 2. 潜在変数 xβ の範囲（-2 ～ 2）
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

# --- cutpoint の縦線（赤の破線） ---
plt.axvline(x=tau1, color='red', linestyle='--', linewidth=1.5, label="cutpoint τ1")
plt.axvline(x=tau2, color='red', linestyle='--', linewidth=1.5, label="cutpoint τ2")

plt.xlabel("潜在変数 $x\\beta$", fontsize=12)
plt.ylabel("確率", fontsize=12)
plt.title("Ordered Logit に基づく倒産ステージ確率曲線（日本企業）", fontsize=14)

plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)

# ------------------------------------------------------------
# 5. PNG 出力
# ------------------------------------------------------------
plt.savefig("ordered_logit_probability_curve_jp_with_cutpoints.png",
            dpi=300, bbox_inches="tight")
plt.close()

print("PNG ファイル 'ordered_logit_probability_curve_jp_with_cutpoints.png' を出力しました。")
