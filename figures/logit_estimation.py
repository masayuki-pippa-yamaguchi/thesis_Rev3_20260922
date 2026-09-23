import pandas as pd
import statsmodels.api as sm
import os

# ============================================================
# 1. データフォルダ（Masayuki さんの環境）
# ============================================================
DATA_DIR = r"D:\texlive\2026\work\figure\JEPX_Spot_Price_Data"

# ============================================================
# 2. panel_data_with_sigma.csv を読み込み（cp932）
# ============================================================
panel_path = os.path.join(DATA_DIR, "panel_data_with_sigma.csv")
df = pd.read_csv(panel_path, encoding="cp932")

# ============================================================
# 3. 説明変数と目的変数を準備
# ============================================================
X = df[["D", "S", "sigma"]]
y = df["default"]

# 数値に強制変換（念のため）
X = X.apply(pd.to_numeric, errors="coerce")
y = pd.to_numeric(y, errors="coerce")

# NaN を除去
data = pd.concat([y, X], axis=1).dropna()

y = data["default"]
X = data[["D", "S", "sigma"]]

# 定数項を追加
X = sm.add_constant(X)

# ============================================================
# 4. ロジット推計
# ============================================================
model = sm.Logit(y, X)
result = model.fit()

# ============================================================
# 5. 結果を表示
# ============================================================
print(result.summary())
