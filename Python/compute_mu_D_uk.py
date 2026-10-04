# compute_mu_D_uk.py

import pandas as pd

# --- 財務データ読み込み（tidy 化済み） ---
df_fin = pd.read_csv("financial_data_uk_tidy.csv")

# --- EBIT を補完するロジック ---
# EBIT が存在しない場合は OperatingProfit を EBIT として扱う
df_fin["item"] = df_fin["item"].replace({"OperatingProfit": "EBIT"})

# --- 必要な項目だけ抽出 ---
items_needed = ["TotalAssets", "TotalLiabilities", "EBIT"]
df_fin = df_fin[df_fin["item"].isin(items_needed)]

# --- wide 形式に変換（company × year × item） ---
df_fin_wide = df_fin.pivot_table(
    index=["company", "year"],
    columns="item",
    values="value",
    aggfunc="first"
).reset_index()

# --- μ（収益性）と D（負債負担）を計算 ---
df_fin_wide["mu"] = df_fin_wide["EBIT"] / df_fin_wide["TotalAssets"]
df_fin_wide["D"]  = df_fin_wide["TotalLiabilities"] / df_fin_wide["TotalAssets"]

# --- company_id を付与するためのマッピング ---
df_status = pd.read_csv("company_status_with_stage_clean_final.csv")
mapping = df_status[["company_id", "company_name"]].rename(
    columns={"company_name": "company"}
)

df_fin_wide = df_fin_wide.merge(mapping, on="company", how="left")

# --- panel_failure_sigma.csv と結合 ---
df_panel = pd.read_csv("panel_failure_sigma.csv")

df_final = df_panel.merge(
    df_fin_wide[["company_id", "year", "mu", "D"]],
    on=["company_id", "year"],
    how="left"
)

# --- 保存 ---
df_final.to_csv("panel_failure_sigma_mu_D.csv", index=False)

print(df_final.head())
print(df_final.tail())
print("行数:", len(df_final))
