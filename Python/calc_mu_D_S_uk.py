# calc_mu_D_S_uk.py

import pandas as pd

# 1. 結合済みパネルを読み込み
df = pd.read_csv("financial_data_uk.csv")

# 2. tidy形式（company, year, item, value）を横持ちに変換
#   → 各年度ごとに必要な財務指標を列として持つ形にする
panel = df.pivot_table(
    index=["company", "year"],
    columns="item",
    values="value"
).reset_index()

# 3. 数値列を float に変換（NA はそのまま）
for col in panel.columns:
    if col not in ["company", "year"]:
        panel[col] = pd.to_numeric(panel[col], errors="coerce")

# 4. ここから先が「まさゆきさんの研究固有の部分」
#    日本企業で使っている μ・D・S の式を、そのまま入れてください。

# --- 例：列名は panel の中から使う ---
# たとえば、TotalAssetsLessCurrentLiabilities, NetAssets などを使う場合：

# μ（例：まさゆきさんの定義に置き換えてください）
# panel["mu"] = （ここに日本企業と同じ μ の式）

# D（例：距離の定義）
# panel["D"] = （ここに日本企業と同じ D の式）

# S（例：スコア）
# panel["S"] = panel["mu"] - panel["D"]   # これは一例。実際の式に置き換えてください。

# 5. 計算結果を保存
panel.to_csv("financial_data_uk_with_S.csv", index=False)

print("✔ μ・D・S を計算したパネルを financial_data_uk_with_S.csv に保存しました")
print("行数:", len(panel))
print("列名:", list(panel.columns))
