# normalize_items_uk_final3.py

import pandas as pd

df = pd.read_csv("financial_data_uk_tidy_clean.csv")

def classify_item(item):

    item_lower = item.lower()

    # --- Equity ---
    if ("equity" in item_lower or
        "netassets" in item_lower or
        "net_assets" in item_lower or
        "netliabilities" in item_lower or
        "retained" in item_lower or
        "sharecapital" in item_lower or
        "share_capital" in item_lower or
        "sharepremium" in item_lower or
        "share_premium" in item_lower or
        "profitandloss" in item_lower or
        "profit_and_loss" in item_lower or
        "calledupsharecapital" in item_lower or
        "shareholdersfunds" in item_lower):
        return "Equity"

    # --- TotalAssets ---
    if ("asset" in item_lower or
        "currentassets" in item_lower or
        "fixedassets" in item_lower or
        "intangibleassets" in item_lower or
        "tangibleassets" in item_lower or
        "rightofuseassets" in item_lower or
        "totalassets" in item_lower or
        "total_assets" in item_lower or
        "totalcurrentassets" in item_lower or
        "totalnoncurrentassets" in item_lower):
        return "TotalAssets"

    # --- TotalLiabilities ---
    if ("liabil" in item_lower or
        "creditor" in item_lower or
        "payable" in item_lower or
        "tradepayables" in item_lower or
        "trade_payables" in item_lower or
        "totalcurrentliabilities" in item_lower or
        "total_liabilities" in item_lower or
        "totalcurrentliabilities" in item_lower):
        return "TotalLiabilities"

    return item

df["item"] = df["item"].apply(classify_item)

df.to_csv("financial_data_uk_tidy_normalized_final3.csv", index=False)

print("部分一致による完全正規化が完了しました。")
print(sorted(df["item"].unique()))
