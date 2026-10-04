import pandas as pd

df_fin = pd.read_csv("financial_data_uk_tidy.csv")

print(sorted(df_fin["company"].unique()))
