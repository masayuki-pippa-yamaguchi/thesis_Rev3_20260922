# normalize_items_uk_final2.py

import pandas as pd

df = pd.read_csv("financial_data_uk_tidy_clean.csv")

# --- 完全版正規化辞書（あなたの tidy データ専用） ---

equity_aliases = {
    "Equity": "Equity", "Equity_total": "Equity", "EquityTotal": "Equity",
    "TotalEquity": "Equity",
    "NetAssets": "Equity", "Net_assets": "Equity", "net_assets": "Equity",
    "RetainedEarnings": "Equity", "RetainedEarningsOrPL": "Equity",
    "retained_earnings": "Equity", "Retained_earnings": "Equity",
    "ShareCapital": "Equity", "Share_capital": "Equity",
    "SharePremium": "Equity", "Share_premium": "Equity",
    "SharePremiumAccount": "Equity",
    "ShareholdersFunds": "Equity",
    "ProfitAndLossReserves": "Equity",
    "ProfitAndLoss": "Equity", "ProfitAndLossAccount": "Equity",
    "CalledUpShareCapitalNotPaid": "Equity"
}

assets_aliases = {
    "TotalAssets": "TotalAssets", "Total_assets": "TotalAssets",
    "total_assets": "TotalAssets",
    "TotalCurrentAssets": "TotalAssets",
    "TotalNonCurrentAssets": "TotalAssets",
    "TotalFixedAssets": "TotalAssets",
    "FixedAssetsTotal": "TotalAssets", "fixed_assets_total": "TotalAssets",
    "CurrentAssets": "TotalAssets", "CurrentAssetsTotal": "TotalAssets",
    "Current_assets_total": "TotalAssets", "current_assets_total": "TotalAssets",
    "total_current_assets": "TotalAssets",
    "total_fixed_assets": "TotalAssets",
    "Total_assets_less": "TotalAssets",
    "Total_assets_less_current_liabilities": "TotalAssets",
    "Total_noncurrent_assets": "TotalAssets",
    "IntangibleAssets": "TotalAssets", "Intangible_assets": "TotalAssets",
    "TangibleAssets": "TotalAssets", "Tangible_assets": "TotalAssets",
    "Other_assets": "TotalAssets",
    "Property_plant_equipment": "TotalAssets",
    "RightOfUseAssets": "TotalAssets"
}

liabilities_aliases = {
    "TotalLiabilities": "TotalLiabilities", "Total_liabilities": "TotalLiabilities",
    "total_liabilities": "TotalLiabilities",
    "Total_current_liabilities": "TotalLiabilities",
    "current_liabilities_total": "TotalLiabilities",
    "noncurrent_liabilities_total": "TotalLiabilities",
    "Creditors_GT1Y": "TotalLiabilities",
    "Creditors_LT1Y": "TotalLiabilities",
    "CreditorsAfter1Y": "TotalLiabilities",
    "CreditorsWithin1Y": "TotalLiabilities",
    "CreditorsWithinOneYear": "TotalLiabilities",
    "creditors_after_1y": "TotalLiabilities",
    "creditors_within_1y": "TotalLiabilities",
    "Trade_payables_current": "TotalLiabilities",
    "TradePayables": "TotalLiabilities",
    "Trade_payables": "TotalLiabilities",
    "TradeAndOtherPayables": "TotalLiabilities",
    "LongTermLiabilities": "TotalLiabilities",
    "LongTermPayables": "TotalLiabilities",
    "LeaseLiabilitiesCurrent": "TotalLiabilities",
    "LeaseLiabilitiesNonCurrent": "TotalLiabilities",
    "VAT_payable": "TotalLiabilities",
    "TaxPayable": "TotalLiabilities",
    "OtherCreditors": "TotalLiabilities",
    "OtherCurrentLiabilities": "TotalLiabilities",
    "OtherLiabilitiesNonCurrent": "TotalLiabilities",
    "GroupLiabilitiesNonCurrent": "TotalLiabilities"
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

df.to_csv("financial_data_uk_tidy_normalized_final2.csv", index=False)

print("完全版項目名正規化（最終版）が完了しました。")
print(sorted(df["item"].unique()))
