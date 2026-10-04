# normalize_items_uk_final.py

import pandas as pd

df = pd.read_csv("financial_data_uk_tidy_clean.csv")

# --- 完全版正規化辞書（あなたの tidy データ専用） ---

equity_aliases = {
    "Equity": "Equity", "EquityTotal": "Equity",
    "NetAssets": "Equity", "Net_assets": "Equity", "net_assets": "Equity",
    "NetLiabilities": "Equity",  # 符号反転は後で処理
    "NetCurrentAssets": "Equity", "Net_current_assets": "Equity",
    "NetCurrentLiabilities": "Equity",  # 要注意だが統一
    "share_capital": "Equity", "share_premium": "Equity",
    "retained_earnings": "Equity", "Retained_earnings": "Equity",
    "ProfitAndLoss": "Equity", "ProfitAndLossAccount": "Equity",
    "CalledUpShareCapitalNotPaid": "Equity"
}

assets_aliases = {
    "TotalAssets": "TotalAssets", "total_assets": "TotalAssets",
    "Total_assets": "TotalAssets",
    "TotalAssetsLessCurrentLiabilities": "TotalAssets",
    "Total_noncurrent_assets": "TotalAssets",
    "TotalFixedAssets": "TotalAssets",
    "Fixed_assets_total": "TotalAssets",
    "CurrentAssets": "TotalAssets", "CurrentAssetsTotal": "TotalAssets",
    "Current_assets_total": "TotalAssets", "total_current_assets": "TotalAssets",
    "total_fixed_assets": "TotalAssets",
    "IntangibleAssets": "TotalAssets", "Intangible_assets": "TotalAssets",
    "TangibleAssets": "TotalAssets", "Tangible_assets": "TotalAssets",
    "Other_assets": "TotalAssets",
    "RightOfUseAssets": "TotalAssets"
}

liabilities_aliases = {
    "TotalLiabilities": "TotalLiabilities", "total_liabilities": "TotalLiabilities",
    "Total_liabilities": "TotalLiabilities",
    "TotalCurrentLiabilities": "TotalLiabilities",
    "current_liabilities_total": "TotalLiabilities",
    "noncurrent_liabilities_total": "TotalLiabilities",
    "Creditors_over_1y": "TotalLiabilities",
    "Creditors_within_1y": "TotalLiabilities",
    "Trade_payables_current": "TotalLiabilities",
    "TradeAndOtherPayables": "TotalLiabilities",
    "LongTermLiabilities": "TotalLiabilities",
    "LongTermPayables": "TotalLiabilities",
    "LeaseLiabilitiesCurrent": "TotalLiabilities",
    "LeaseLiabilitiesNonCurrent": "TotalLiabilities",
    "VAT_payable": "TotalLiabilities",
    "TaxPayable": "TotalLiabilities",
    "GroupLiabilitiesNonCurrent": "TotalLiabilities",
    "NonCurrentLiabilities": "TotalLiabilities"
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

df.to_csv("financial_data_uk_tidy_normalized_final.csv", index=False)

print("完全版項目名正規化が完了しました。")
print(sorted(df["item"].unique()))
