# company_status_clean.py

import pandas as pd

df = pd.read_csv("company_status_with_stage.csv")

# --- company_id の不可視文字を除去 ---
df["company_id"] = df["company_id"].astype(str).str.strip()

# --- 空行を削除 ---
df = df[df["company_id"].notna() & (df["company_id"] != "")]

# --- 完全重複行を削除 ---
df = df.drop_duplicates()

# --- company_id の重複を削除（最初の1行だけ残す） ---
df = df.drop_duplicates(subset=["company_id"], keep="first")

# --- 保存 ---
df.to_csv("company_status_with_stage_clean.csv", index=False)

print("重複削除完了。行数:", len(df))
print(df.head())
