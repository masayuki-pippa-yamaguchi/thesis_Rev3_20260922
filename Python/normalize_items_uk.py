# normalize_items_uk.py

import pandas as pd

df = pd.read_csv("financial_data_uk_tidy_clean.csv")

# --- 正規化辞書 ---

equity_aliases = {
    "Equity": "Equity",
    "EquityTotal": "Equity",
    "Equity_total": "Equity",
    "ShareholdersFunds": "Equity",
    "NetAssets": "Equity",
    "Net_assets": "Equity",
    "NetLiabilities": "Equity",  # 符号反転が必要だがまずは統一
    "RetainedEarnings": "Equity",
    "RetainedEarningsOrPL": "Equity",
    "ProfitAndLossReserves": "Equity"
}

assets_aliases = {
    "TotalAssets": "TotalAssets",
    "Total_assets": "TotalAssets",
    "TotalAssetsLessCurrentLiabilities": "TotalAssets",
    "Total_current_assets": "TotalAssets",
    "Total_fixed_assets": "TotalAssets",
    "TotalNonCurrentAssets": "TotalAssets",
    "TotalCurrentAssets": "TotalAssets"
}

liabilities_aliases = {
    "TotalLiabilities": "TotalLiabilities",
    "Total_liabilities": "TotalLiabilities",
    "CurrentLiabilities": "TotalLiabilities",
    "NonCurrentLiabilities": "TotalLiabilities",
    "creditors_after_1y": "TotalLiabilities",
    "creditors_within_1y": "TotalLiabilities",
    "current_liabilities_total": "TotalLiabilities",
    "noncurrent_liabilities_total": "TotalLiabilities"
}

# --- item の正規化 ---
def normalize_item(item):
    if item in equity_aliases:
        return equity_aliases[item]
    if item in assets_aliases:
        return assets_aliases[item]
    if item in liabilities_aliases:
        return liabilities_aliases[item]
    return item

df["item"] = df["item"].apply(normalize_item)

df.to_csv("financial_data_uk_tidy_normalized.csv", index=False)

print("項目名の正規化が完了しました。")
print(sorted(df["item"].unique()))
