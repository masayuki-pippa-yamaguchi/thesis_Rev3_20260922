# % bs_simulation_step3_logit_estimation.py
# % B&S 推定式シミュレーション：Step 3（ロジット推定）
# % 著者：Masayuki さんの論文用コード

import numpy as np
import pandas as pd
import statsmodels.api as sm

# ---------------------------------------------------------
# 1. Step2 の結果（df_proxy.csv）を読み込む
# ---------------------------------------------------------

df = pd.read_csv("figures/df_proxy.csv")

# ---------------------------------------------------------
# 2. ロジット推定を行う関数
# ---------------------------------------------------------

def run_logit(df, X_cols, y_col="default"):
    X = df[X_cols]
    X = sm.add_constant(X)  # 切片を追加
    y = df[y_col]
    model = sm.Logit(y, X)
    result = model.fit(disp=False)
    return result

# ---------------------------------------------------------
# 3. 仕様A〜D の説明変数セット
# ---------------------------------------------------------

specs = {
    "A": ["mu_proxy1", "sigma_proxy", "S_proxy", "D_proxy"],  # 理想的 proxy
    "B": ["mu_proxy2", "sigma_proxy", "S_proxy", "D_proxy"],  # μ を BS proxy に置換
    "C": ["mu_proxy1", "sigma_proxy", "S_proxy", "D_proxy"],  # D を粗い proxy に置換（後で変更可）
    "D": ["mu_proxy2", "sigma_proxy", "S_proxy", "D_proxy"],  # μ と D を粗い proxy に置換
}

# ---------------------------------------------------------
# 4. 推定結果を保存する辞書
# ---------------------------------------------------------

results = {}
coef_table = pd.DataFrame()

# ---------------------------------------------------------
# 5. 各仕様についてロジット推定を実行
# ---------------------------------------------------------

for spec_name, X_cols in specs.items():
    print(f"Running Logit for specification {spec_name} ...")
    res = run_logit(df, X_cols)
    results[spec_name] = res

    # 係数を表にまとめる
    coef = res.params
    coef.name = spec_name
    coef_table = pd.concat([coef_table, coef], axis=1)

    # 予測値を保存（ROC 曲線用）
    df[f"pred_{spec_name}"] = res.predict()

# ---------------------------------------------------------
# 6. 推定係数の出力
# ---------------------------------------------------------

print("\n=== 推定係数（仕様A〜D） ===")
print(coef_table)

# ---------------------------------------------------------
# 7. 推定係数を CSV 保存（Step4 の可視化で使用）
# ---------------------------------------------------------

coef_table.to_csv("figures/logit_coefficients.csv")

# ---------------------------------------------------------
# 8. 予測値を CSV 保存（ROC 曲線・散布図で使用）
# ---------------------------------------------------------

df.to_csv("figures/df_logit_results.csv", index=False)
