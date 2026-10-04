import pandas as pd

df = pd.read_csv("financial_data_uk_tidy_clean.csv")

# 欠損状況を企業別に確認
missing = df[df["item"].isin(["TotalAssets", "TotalLiabilities", "Equity"])]

pivot = missing.pivot_table(
    index="company",
    columns="item",
    values="value",
    aggfunc="count"
)

print(pivot)
