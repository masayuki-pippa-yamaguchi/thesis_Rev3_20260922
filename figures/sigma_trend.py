import pandas as pd
import matplotlib.pyplot as plt
import os

# データの場所
DATA_DIR = r"D:\texlive\2026\work\figure\JEPX_Spot_Price_Data"
panel_path = os.path.join(DATA_DIR, "panel_data_with_sigma.csv")

# CSV 読み込み
df = pd.read_csv(panel_path, encoding="cp932")

# x 軸は単純な月番号にする（固まらない）
x = range(len(df))

plt.figure(figsize=(12, 4))
plt.plot(x, df["sigma"], color="navy", linewidth=1.2)

plt.title("Monthly Market Shock (sigma)", fontsize=14)
plt.xlabel("Month index", fontsize=12)
plt.ylabel("sigma", fontsize=12)

# 目盛りを間引く（これが非常に重要）
plt.xticks(
    ticks=range(0, len(df), 12),
    labels=[str(i) for i in range(0, len(df), 12)],
    rotation=45
)

plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

plt.savefig("sigma_trend.pdf")
print("sigma_trend.pdf を作成しました。")
