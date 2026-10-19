# identify_outliers_mu_D.py

import pandas as pd
import numpy as np

df = pd.read_csv("panel_failure_sigma_mu_D_proxy.csv")

df = df[df["company_id"].str.startswith("ENG", na=False)]

for col in ["mu_proxy", "D"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.replace([np.inf, -np.inf], np.nan, inplace=True)

print("\n===== mu_proxy 上位10件 =====")
print(df.nlargest(10, "mu_proxy")[["company_id","year","mu_proxy"]])

print("\n===== mu_proxy 下位10件 =====")
print(df.nsmallest(10, "mu_proxy")[["company_id","year","mu_proxy"]])

print("\n===== D 上位10件 =====")
print(df.nlargest(10, "D")[["company_id","year","D"]])

print("\n===== D 下位10件 =====")
print(df.nsmallest(10, "D")[["company_id","year","D"]])