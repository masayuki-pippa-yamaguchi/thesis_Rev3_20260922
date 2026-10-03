# merge_uk_tidy_to_financial_data_uk.py

import pandas as pd
import glob

# tidy CSV が保存されているフォルダ
folder = r"D:\Keio\work\uk_tidy\\"

# フォルダ内の CSV ファイル一覧を取得
files = glob.glob(folder + "*.csv")

print("対象ファイル数:", len(files))

df_list = []

for f in files:
    print("結合中:", f)
    df = pd.read_csv(f)
    df_list.append(df)

# 全社の tidy データを結合
financial_data_uk = pd.concat(df_list, ignore_index=True)

# NA統一（念のため再度実施）
financial_data_uk = financial_data_uk.replace(["", " ", "　", "NA", "na", "?"], pd.NA)

# 保存
financial_data_uk.to_csv("financial_data_uk.csv", index=False)

print("✔ financial_data_uk.csv を作成しました")
print("行数:", len(financial_data_uk))
