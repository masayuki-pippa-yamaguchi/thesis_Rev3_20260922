# compute_mu_D_proxy_uk.py

import pandas as pd

# --- 財務データ読み込み（tidy 化済み） ---
df_fin = pd.read_csv("financial_data_uk_tidy_normalized_final3.csv")

# --- μ と D に必要な項目だけ抽出 ---
items_needed = ["TotalAssets", "TotalLiabilities", "Equity"]
df_fin = df_fin[df_fin["item"].isin(items_needed)]

# --- year を int に変換 ---
df_fin["year"] = df_fin["year"].astype(str).str[:4].astype(int)

# --- wide 形式に変換（company × year × item） ---
df_fin_wide = df_fin.pivot_table(
    index=["company", "year"],
    columns="item",
    values="value",
    aggfunc="first"
).reset_index()

# --- μ（代理変数）と D を計算 ---
df_fin_wide["mu_proxy"] = df_fin_wide["Equity"] / df_fin_wide["TotalAssets"]
df_fin_wide["D"]        = df_fin_wide["TotalLiabilities"] / df_fin_wide["TotalAssets"]

# --- company_id を付与するためのマッピング ---
df_status = pd.read_csv("company_status_with_stage_clean_final.csv")
mapping = df_status[["company_id", "company_name"]].rename(
    columns={"company_name": "company"}
)

df_fin_wide = df_fin_wide.merge(mapping, on="company", how="left")

# --- panel_failure_sigma.csv と結合 ---
df_panel = pd.read_csv("panel_failure_sigma.csv")

# 念のため df_panel["year"] も int に統一
df_panel["year"] = df_panel["year"].astype(int)

df_final = df_panel.merge(
    df_fin_wide[["company_id", "year", "mu_proxy", "D"]],
    on=["company_id", "year"],
    how="left"
)

# --- 保存 ---
df_final.to_csv("panel_failure_sigma_mu_D_proxy.csv", index=False)

print(df_final.head())
print(df_final.tail())
print("行数:", len(df_final))

# --- ロジット推定用に NaN を除外 ---
df_final_clean = df_final.dropna(subset=["mu_proxy", "D"])
df_final_clean.to_csv("panel_failure_sigma_mu_D_proxy_clean.csv", index=False)

print("ロジット推定用データの行数:", len(df_final_clean))
