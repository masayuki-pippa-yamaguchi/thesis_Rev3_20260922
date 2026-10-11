import pandas as pd
import matplotlib.pyplot as plt

# CSV の読み込み（date を datetime 型に変換）
df = pd.read_csv("electricity_sigma_proxy_2013_2023.csv", parse_dates=["date"])

# 図のサイズ設定
plt.figure(figsize=(12, 6))

# スポット価格の時系列プロット
plt.plot(df["date"], df["price"], label="Spot Price (GBP/MWh)", color="tab:blue")

# 軸ラベル・タイトル
plt.xlabel("Date")
plt.ylabel("Price (GBP/MWh)")
plt.title("UK Wholesale Electricity Spot Price (2013–2023)")

# グリッドと凡例
plt.grid(True)
plt.legend()

# PNG 保存
plt.savefig("spot_price_plot.png", dpi=300, bbox_inches="tight")
