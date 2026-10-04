# add_failure_stage.py

import pandas as pd

# ① 結合済み CSV を読み込み
df = pd.read_csv("company_status_merged.csv")

# ② 倒産ステージ付与関数
def assign_stage(status):
    status = str(status).lower()

    if status == "active":
        return 0
    elif status in ["administration", "insolvency-proceedings"]:
        return 1
    elif status == "liquidation":
        return 2
    elif status == "dissolved":
        return 3
    else:
        return None  # 想定外の値が来た場合

# ③ 新しい列 failure_stage を作成
df["failure_stage"] = df["company_status"].apply(assign_stage)

# ④ CSV に保存
df.to_csv("company_status_with_stage.csv", index=False)

print("company_status_with_stage.csv を作成しました。")
