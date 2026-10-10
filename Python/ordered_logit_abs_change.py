# ordered_logit_abs_change.py

import pandas as pd
import numpy as np
from statsmodels.miscmodels.ordinal_model import OrderedModel

# --- データ読み込み ---
df = pd.read_csv("panel_failure_sigma_mu_D_proxy_clean.csv")

# --- failure_stage を int に変換 ---
df["failure_stage"] = pd.to_numeric(df["failure_stage"], errors="coerce").astype("Int64")

# --- NaN と inf を除外 ---
df = df.dropna(subset=["failure_stage"])
df = df.replace([np.inf, -np.inf], np.nan)

# --- 必要な変数だけ抽出 ---
df2 = df[["failure_stage", "mu_proxy", "D", "abs_change"]].dropna()

# --- 説明変数 ---
X = df2[["mu_proxy", "D", "abs_change"]]

# --- 目的変数 ---
y = df2["failure_stage"].astype(int)

# --- Ordered Logit モデル ---
model = OrderedModel(y, X, distr='logit')

# --- 推定 ---
res = model.fit(method='bfgs')

# --- 結果表示 ---
print(res.summary())

# --- オッズ比 ---
params = res.params
odds_ratios = pd.DataFrame({
    "coef": params,
    "odds_ratio": np.exp(params)
})
print("\nOdds Ratios:")
print(odds_ratios)
