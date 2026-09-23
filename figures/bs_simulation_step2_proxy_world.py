# % bs_simulation_step2_proxy_world.py
# % B&S 推定式シミュレーション：Step 2（proxy の生成）
# % 著者：Masayuki さんの論文用コード

import numpy as np
import pandas as pd

np.random.seed(123)

# ---------------------------------------------------------
# 1. Step1 の結果（df_true.csv）を読み込む
# ---------------------------------------------------------

df_true = pd.read_csv("figures/df_true.csv")

# ---------------------------------------------------------
# 2. 観測誤差（proxy のノイズ）を生成
# ---------------------------------------------------------

eps_mu1 = np.random.normal(0, 0.01, size=len(df_true))   # μ proxy1 の誤差
eps_mu2 = np.random.normal(0, 0.02, size=len(df_true))   # μ proxy2 の誤差
eta_sigma = np.random.normal(0, 0.02, size=len(df_true)) # σ proxy の誤差
xi_D = np.random.normal(0, 0.05, size=len(df_true))      # D proxy の誤差

# ---------------------------------------------------------
# 3. μ の proxy（2種類）
# ---------------------------------------------------------

# 営業利益率に近い proxy（精度が高い）
df_true["mu_proxy1"] = df_true["mu_true"] + eps_mu1

# 貸借対照表ベースの proxy（精度が低い）
df_true["mu_proxy2"] = 0.8 * df_true["mu_true"] + eps_mu2

# ---------------------------------------------------------
# 4. σ の proxy（スポット依存度などを模したもの）
# ---------------------------------------------------------

df_true["sigma_proxy"] = 0.7 * df_true["sigma_true"] + eta_sigma

# ---------------------------------------------------------
# 5. S の proxy（誤分類を含む）
# ---------------------------------------------------------

S_proxy = []
for s in df_true["S_true"]:
    if np.random.rand() < 0.9:
        S_proxy.append(s)       # 90% は正しく観測
    else:
        S_proxy.append(max(0, s - 1))  # 10% は1段階低く誤分類

df_true["S_proxy"] = S_proxy

# ---------------------------------------------------------
# 6. D の proxy（インバランス負担などの noisy proxy）
# ---------------------------------------------------------

df_true["D_proxy"] = df_true["D_true"] + xi_D

# ---------------------------------------------------------
# 7. proxy データフレームとしてまとめる
# ---------------------------------------------------------

df_proxy = df_true[[
    "mu_proxy1", "mu_proxy2",
    "sigma_proxy", "S_proxy", "D_proxy",
    "default", "p_true"
]]

# ---------------------------------------------------------
# 8. 出力確認
# ---------------------------------------------------------

print(df_proxy.head())

# ---------------------------------------------------------
# 9. CSV 保存（Step3 で読み込む）
# ---------------------------------------------------------

df_proxy.to_csv("figures/df_proxy.csv", index=False)
