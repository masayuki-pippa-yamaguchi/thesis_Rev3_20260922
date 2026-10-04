# merge_financial_and_status.py

import pandas as pd

# ① 財務データ（年度 × 企業）
financial_df = pd.read_csv("financial_data_uk.csv")

# ② 倒産ステージ付き企業属性データ（企業単位）
status_df = pd.read_csv("company_status_with_stage.csv")

# ③ company（財務データ） と company_name（ステータス）で結合
merged_df = pd.merge(
    financial_df,
    status_df,
    left_on="company",
    right_on="company_name",
    how="left"
)

# ④ 結合結果を保存
merged_df.to_csv("financial_data_with_status.csv", index=False)

print("financial_data_with_status.csv を作成しました。")
