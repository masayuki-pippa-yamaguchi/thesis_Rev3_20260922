# descriptive_stats_uk_mu_D.py

import pandas as pd
import numpy as np

# CSV読込
df = pd.read_csv("panel_failure_sigma_mu_D_proxy.csv")

# 英国企業のみ抽出
df_uk = df[df["company_id"].str.startswith("ENG", na=False)].copy()

# 記述統計対象変数
vars_target = ["mu_proxy", "D"]

# 数値化
for col in vars_target:
    df_uk[col] = pd.to_numeric(df_uk[col], errors="coerce")

# inf, -inf を欠損値へ変換
df_uk.replace([np.inf, -np.inf], np.nan, inplace=True)

# 記述統計量
desc = pd.DataFrame({
    "N": df_uk[vars_target].count(),
    "Mean": df_uk[vars_target].mean(),
    "Std": df_uk[vars_target].std(),
    "Min": df_uk[vars_target].min(),
    "Median": df_uk[vars_target].median(),
    "Max": df_uk[vars_target].max()
})

# 小数点以下4桁
desc = desc.round(4)

print("\n=== UK Firms Descriptive Statistics ===\n")
print(desc)

# CSV保存
desc.to_csv("uk_descriptive_statistics.csv")

print("\n保存完了 : uk_descriptive_statistics.csv")