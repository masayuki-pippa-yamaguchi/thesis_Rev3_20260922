import pandas as pd

df = pd.read_csv("financial_data_uk_tidy_clean.csv")

# --- 完全版正規化辞書 ---

equity_aliases = {
    "Equity": "Equity", "TotalEquity": "Equity", "Equity_total": "Equity",
    "ShareholdersFunds": "Equity", "NetAssets": "Equity", "Net_assets": "Equity",
    "net_assets": "Equity", "RetainedEarnings": "Equity", "Retained_earnings": "Equity",
    "RetainedEarningsOrPL": "Equity", "ProfitAndLossReserves": "Equity",
    "Share_capital": "Equity", "ShareCapital": "Equity",
    "Share_premium": "Equity", "SharePremium": "Equity",
    "SharePremiumAccount": "Equity"
}

assets_aliases = {
    "TotalAssets": "TotalAssets", "total_assets": "TotalAssets",
    "Total_assets_less": "TotalAssets", "Total_assets_less_current_liabilities": "TotalAssets",
    "Total_current_assets": "TotalAssets", "total_current_assets": "TotalAssets",
    "Total_fixed_assets": "TotalAssets", "total_fixed_assets": "TotalAssets",
    "FixedAssetsTotal": "TotalAssets", "fixed_assets_total": "TotalAssets",
    "TotalNonCurrentAssets": "TotalAssets", "TotalCurrentAssets": "TotalAssets",
    "current_assets_total": "TotalAssets"
}

liabilities_aliases = {
    "TotalLiabilities": "TotalLiabilities", "total_liabilities": "TotalLiabilities",
    "Total_current_liabilities": "TotalLiabilities",
    "CurrentLiabilitiesWithin1Y": "TotalLiabilities",
    "creditors_after_1y": "TotalLiabilities", "creditors_within_1y": "TotalLiabilities",
    "CreditorsAfter1Y": "TotalLiabilities", "Creditors_GT1Y": "TotalLiabilities",
    "Creditors_LT1Y": "TotalLiabilities", "CreditorsWithin1Y": "TotalLiabilities",
    "CreditorsWithinOneYear": "TotalLiabilities",
    "Trade_payables_current": "TotalLiabilities",
    "TradePayables": "TotalLiabilities", "Trade_payables": "TotalLiabilities"
}

def normalize_item(item):
    if item in equity_aliases:
        return "Equity"
    if item in assets_aliases:
        return "TotalAssets"
    if item in liabilities_aliases:
        return "TotalLiabilities"
    return item

df["item"] = df["item"].apply(normalize_item)

df.to_csv("financial_data_uk_tidy_normalized_full.csv", index=False)

print("完全版項目名正規化が完了しました。")
print(sorted(df["item"].unique()))
