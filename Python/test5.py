import pandas as pd

df = pd.read_csv("financial_data_uk_tidy_normalized_full.csv")

# Equity に関連する可能性がある項目を抽出
equity_candidates = [item for item in df["item"].unique()
                     if "equity" in item.lower()
                     or "net" in item.lower()
                     or "retained" in item.lower()
                     or "share" in item.lower()
                     or "profitandloss" in item.lower()
                     or "fund" in item.lower()]

print("Equity candidates:")
print(equity_candidates)

# Assets に関連する可能性がある項目を抽出
assets_candidates = [item for item in df["item"].unique()
                     if "asset" in item.lower()
                     or "fixed" in item.lower()
                     or "current" in item.lower()
                     or "noncurrent" in item.lower()
                     or "total" in item.lower()]

print("\nAssets candidates:")
print(assets_candidates)

# Liabilities に関連する可能性がある項目を抽出
liabilities_candidates = [item for item in df["item"].unique()
                          if "liabil" in item.lower()
                          or "creditor" in item.lower()
                          or "payable" in item.lower()
                          or "trade" in item.lower()
                          or "current" in item.lower()
                          or "noncurrent" in item.lower()
                          or "total" in item.lower()]

print("\nLiabilities candidates:")
print(liabilities_candidates)
