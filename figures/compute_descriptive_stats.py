import pandas as pd
import os

DATA_DIR = r"D:\texlive\2026\work\figure\JEPX_Spot_Price_Data"
panel_path = os.path.join(DATA_DIR, "panel_data_with_sigma.csv")

df = pd.read_csv(panel_path, encoding="cp932")

# 必要な変数だけ抽出
vars = ["sigma", "S", "D", "default"]

desc = df[vars].describe()
print(desc)
