# company_status_clean_final.py

import pandas as pd

df = pd.read_csv("company_status_with_stage.csv")

# --- 不可視文字を除去 ---
df["company_id"] = df["company_id"].astype(str).str.strip()
df["company_number"] = df["company_number"].astype(str).str.strip()

# --- ENG025 を削除 ---
df = df[df["company_id"] != "ENG025"]

# --- Avro Energy Ltd と Avro Energy Trading Ltd を統合 ---
# company_number が同じ "09174794" の企業を一旦削除
df = df[df["company_number"] != "09174794"]

# 代表として ENG015 を残す
df_avro = pd.DataFrame([{
    "company_id": "ENG015",
    "company_name": "Avro Energy Ltd",
    "company_number": "09174794",
    "company_status": "liquidation",
    "administration_start_date": "2022-10-03",
    "failure_stage": 2
}])

df = pd.concat([df, df_avro], ignore_index=True)

# --- 完全重複行を削除 ---
df = df.drop_duplicates()

# --- company_id の重複を削除 ---
df = df.drop_duplicates(subset=["company_id"], keep="first")

# --- 保存 ---
df.to_csv("company_status_with_stage_clean_final.csv", index=False)

print("最終クリーニング完了。行数:", len(df))
print(df)
