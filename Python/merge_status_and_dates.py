# merge_status_and_dates.py

import pandas as pd

# ① 2つの CSV を読み込み
status_df = pd.read_csv("company_status.csv")
dates_df = pd.read_csv("administration_dates.csv")

# ② company_id をキーに結合（company_number でも可）
merged_df = pd.merge(
    status_df,
    dates_df,
    on=["company_id", "company_name", "company_number"],
    how="left"
)

# ③ 列名の整理
merged_df = merged_df.rename(columns={
    "administration_start_date_x": "administration_start_date_status",
    "administration_start_date_y": "administration_start_date_filing"
})

# ④ 最終的な倒産日を決定
# filing history の方が正確なので、そちらを優先
merged_df["administration_start_date"] = merged_df["administration_start_date_filing"].fillna(
    merged_df["administration_start_date_status"]
)

# ⑤ 不要列を削除
merged_df = merged_df.drop(columns=[
    "administration_start_date_status",
    "administration_start_date_filing"
])

# ⑥ CSV に保存
merged_df.to_csv("company_status_merged.csv", index=False)

print("company_status_merged.csv を作成しました。")
