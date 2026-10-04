# clean_financial_names_uk.py

import pandas as pd

df = pd.read_csv("financial_data_uk_tidy.csv")

# --- 対象外企業の除外 ---
exclude_list = [
    "Conrad Energy (Trading) Ltd",
    "Crown Gas and Power 2 Ltd",
    "Dyce Energy Ltd",
    "Edgware Energy Ltd",
    "Equinicity Ltd",
    "EPG Energy Ltd",
    "company"
]

df = df[~df["company"].isin(exclude_list)]

# --- 正規化マッピング ---
name_mapping = {
    "British Gas TradingTrading Ltd": "British Gas Trading Ltd",
    "CORONA ENERGY RETAIL 1 LIMITED": "Corona Energy Retail Ltd",
    "Orbit Energy Ltd": "Orbit Energy",
    "REBEL ENERGY SUPPLY LIMITED": "Rebel Energy",
    "SHELL ENERGY UK LIMITED": "Shell Energy Retail Ltd",
    "BGI Trading Ltd": "British Gas Trading Ltd",
    "PEOPLE'S ENERGY (SUPPLY) LIMITED": "People's Energy Ltd",
}

df["company"] = df["company"].replace(name_mapping)

# --- 保存 ---
df.to_csv("financial_data_uk_tidy_clean.csv", index=False)

print("企業名の正規化と除外が完了しました。")
print(sorted(df["company"].unique()))
