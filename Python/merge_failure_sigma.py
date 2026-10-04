# merge_failure_sigma.py

import pandas as pd

# --- ファイル読み込み ---
df_status = pd.read_csv("company_status_with_stage_clean_final.csv")
df_sigma  = pd.read_csv("electricity_sigma_proxy_2013_2023.csv")

# --- σデータを年次に集計（平均値を使用） ---
df_sigma["year"] = pd.to_datetime(df_sigma["date"]).dt.year
df_sigma_yearly = df_sigma.groupby("year", as_index=False).agg({
    "pct_change": "mean",
    "abs_change": "mean",
    "roll_std_3m": "mean"
})

# --- 倒産データの整形 ---
df_status["administration_start_date"] = pd.to_datetime(
    df_status["administration_start_date"], errors="coerce"
)
df_status["failure_year"] = df_status["administration_start_date"].dt.year

# --- 企業 × 年 のパネルを作成 ---
years = list(range(2013, 2023 + 1))
companies = df_status["company_id"].unique()

panel = pd.DataFrame(
    [(cid, y) for cid in companies for y in years],
    columns=["company_id", "year"]
)

# --- 倒産データを結合 ---
df_panel = panel.merge(df_status[["company_id", "failure_year", "failure_stage"]],
                       on="company_id", how="left")

# --- t−1, t−2, t−3 を作成 ---
df_panel["t_minus_1"] = df_panel["failure_year"] - 1
df_panel["t_minus_2"] = df_panel["failure_year"] - 2
df_panel["t_minus_3"] = df_panel["failure_year"] - 3

# --- 年次 σ を結合 ---
df_panel = df_panel.merge(df_sigma_yearly, on="year", how="left")

# --- t−1 の σ ---
df_panel = df_panel.merge(
    df_sigma_yearly.rename(columns={
        "year": "t_minus_1",
        "pct_change": "pct_t_minus_1",
        "abs_change": "abs_t_minus_1",
        "roll_std_3m": "roll_t_minus_1"
    }),
    on="t_minus_1",
    how="left"
)

# --- t−2 の σ ---
df_panel = df_panel.merge(
    df_sigma_yearly.rename(columns={
        "year": "t_minus_2",
        "pct_change": "pct_t_minus_2",
        "abs_change": "abs_t_minus_2",
        "roll_std_3m": "roll_t_minus_2"
    }),
    on="t_minus_2",
    how="left"
)

# --- t−3 の σ ---
df_panel = df_panel.merge(
    df_sigma_yearly.rename(columns={
        "year": "t_minus_3",
        "pct_change": "pct_t_minus_3",
        "abs_change": "abs_t_minus_3",
        "roll_std_3m": "roll_t_minus_3"
    }),
    on="t_minus_3",
    how="left"
)

# --- 保存 ---
df_panel.to_csv("panel_failure_sigma.csv", index=False)

print(df_panel.head())
print(df_panel.tail())
print("行数:", len(df_panel))
