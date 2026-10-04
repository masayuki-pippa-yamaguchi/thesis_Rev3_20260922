# electricity_sigma_proxy.py

import pandas as pd

# CSV 読み込み
df = pd.read_csv(r"D:\texlive\2026\work\thesis_Rev3_20260922\Python\electricity-prices-day-a.csv")

# 列名を整形
df.columns = ["date", "price"]

# 日付を datetime に変換
df["date"] = pd.to_datetime(df["date"])

# 年月だけにする（YYYY-MM）
df["year_month"] = df["date"].dt.to_period("M").astype(str)

# 時系列順に並べ替え
df = df.sort_values("date").reset_index(drop=True)

# --- σ の代理変数を作成 ---

# ① 前月比（変動率）
df["pct_change"] = df["price"].pct_change()

# ② 前月差（絶対変動幅）
df["abs_change"] = df["price"].diff().abs()

# ③ 過去3ヶ月の移動標準偏差（Rolling Std）
df["roll_std_3m"] = df["price"].rolling(window=3).std()

# 2013〜2023 の期間だけ抽出（研究対象期間）
df_period = df[(df["date"] >= "2013-01-01") & (df["date"] <= "2023-12-31")]

# 結果確認
print(df_period.head())
print(df_period.tail())

# 必要なら CSV に保存
df_period.to_csv("electricity_sigma_proxy_2013_2023.csv", index=False)
