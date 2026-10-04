import pandas as pd

df = pd.read_csv("financial_data_uk_tidy.csv")
print(sorted(df["item"].unique()))
