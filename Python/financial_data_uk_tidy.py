# financial_data_uk_tidy.py

import pandas as pd
import numpy as np

# --- ファイル読み込み ---
df = pd.read_csv("financial_data_uk.csv")

# --- company, year, item の重複を検出 ---
# 数値列を float に変換
df["value"] = pd.to_numeric(df["value"], errors="coerce")

# --- tidy 化ルール ---
def resolve_duplicates(group):
    """
    同じ company-year-item に複数行ある場合の処理：
    1. 非欠損値を優先
    2. 正負混在 → 正の値を優先
    3. 絶対値が大きい値を優先
    """
    g = group.dropna(subset=["value"])

    if len(g) == 0:
        return group.iloc[0]  # 全欠損ならそのまま返す

    # 正負混在 → 正の値を優先
    positives = g[g["value"] >= 0]
    if len(positives) > 0:
        g = positives

    # 絶対値が最大の値を採用
    idx = g["value"].abs().idxmax()
    return g.loc[idx]

# --- tidy 化実行 ---
df_tidy = df.groupby(["company", "year", "item"], as_index=False).apply(resolve_duplicates)

# groupby の副作用で index が階層化するためリセット
df_tidy = df_tidy.reset_index(drop=True)

# --- 保存 ---
df_tidy.to_csv("financial_data_uk_tidy.csv", index=False)

print("Tidy 化完了。行数:", len(df_tidy))
print(df_tidy.head())
