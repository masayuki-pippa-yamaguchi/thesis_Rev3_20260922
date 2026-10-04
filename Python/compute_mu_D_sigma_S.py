# compute_mu_D_sigma_S.py

import pandas as pd
import numpy as np

df = pd.read_csv("financial_data_with_status.csv")

# ★ 追加：value を数値化
df["value"] = pd.to_numeric(df["value"], errors="coerce")

# tidy → 横持ち
df_wide = df.pivot_table(
    index=["company", "year"],
    columns="item",
    values="value"
).reset_index()

# ③ total_assets の log-diff（μ）を計算
df_wide = df_wide.sort_values(["company", "year"])
df_wide["log_assets"] = np.log(df_wide["total_assets"])
df_wide["mu_logdiff"] = df_wide.groupby("company")["log_assets"].diff()

# ④ D（負債比率）を計算
df_wide["D"] = df_wide["total_liabilities"] / df_wide["total_assets"]

# ⑤ σ（スポット価格ボラティリティ）を読み込み
# 例：spot_price_volatility.csv に company, year, sigma が入っていると仮定
sigma_df = pd.read_csv("spot_price_volatility.csv")

# 企業 × 年度で結合
df_wide = pd.merge(
    df_wide,
    sigma_df,
    on=["company", "year"],
    how="left"
)

# ⑥ S（潜在倒産リスク指標）を計算
# ※ あなたの日本企業分析で使った式に合わせてください
# 例：S = mu_logdiff - D + sigma
df_wide["S"] = df_wide["mu_logdiff"] - df_wide["D"] + df_wide["sigma"]

# ⑦ 倒産ステージを再結合
status_df = df[["company", "failure_stage", "administration_start_date"]].drop_duplicates()
df_final = pd.merge(df_wide, status_df, on="company", how="left")

# ⑧ 保存
df_final.to_csv("financial_data_with_S.csv", index=False)

print("financial_data_with_S.csv を作成しました。")
