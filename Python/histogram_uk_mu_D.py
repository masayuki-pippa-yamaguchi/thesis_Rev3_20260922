# histogram_uk_mu_D.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV読込
df = pd.read_csv("panel_failure_sigma_mu_D_proxy.csv")

# 英国企業のみ抽出
df = df[df["company_id"].str.startswith("ENG", na=False)].copy()

# 対象変数
vars_target = ["mu_proxy", "D"]

# 数値化
for col in vars_target:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# inf, -inf を欠損値へ
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# ヒストグラム作成
for col in vars_target:

    plt.figure(figsize=(8, 5))

    plt.hist(
        df[col].dropna(),
        bins=30
    )

    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")

    plt.tight_layout()

    filename = f"{col}_histogram.png"
    plt.savefig(filename, dpi=300)

    print(f"保存完了: {filename}")

    plt.close()