# clean_blank_to_NA_uk_tidy.py

import pandas as pd
import glob

# tidy CSV が保存されているフォルダ
folder = r"D:\Keio\work\uk_tidy\\"

# フォルダ内の CSV ファイル一覧を取得
files = glob.glob(folder + "*.csv")

print("対象ファイル数:", len(files))

# 空白・文字列NA・スペースなどを NA に統一するための置換リスト
to_na = ["", " ", "　", "NA", "na", "?", None]

for f in files:
    print("処理中:", f)
    
    # CSV 読み込み
    df = pd.read_csv(f)
    
    # 空白・文字列NAなどをすべて NA に統一
    df = df.replace(to_na, pd.NA)
    
    # 上書き保存
    df.to_csv(f, index=False)

print("✔ 全ファイルの空白 → NA 統一処理が完了しました。")
