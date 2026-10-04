# compute_mu_D.py

import pandas as pd
import numpy as np

df = pd.read_csv("financial_data_with_status.csv")

df["value"] = pd.to_numeric(df["value"], errors="coerce")

df_wide = df.pivot_table(
    index=["company", "year"],
    columns="item",
    values="value"
).reset_index()

df_wide = df_wide.sort_values(["company", "year"])
df_wide["log_assets"] = np.log(df_wide["total_assets"])
df_wide["mu_logdiff"] = df_wide.groupby("company")["log_assets"].diff()

df_wide["D"] = df_wide["total_liabilities"] / df_wide["total_assets"]

status_df = df[["company", "failure_stage", "administration_start_date"]].drop_duplicates()
df_final = pd.merge(df_wide, status_df, on="company", how="left")

df_final.to_csv("financial_data_with_mu_D.csv", index=False)

print("financial_data_with_mu_D.csv を作成しました。")
