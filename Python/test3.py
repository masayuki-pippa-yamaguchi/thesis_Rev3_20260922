import pandas as pd

df_status = pd.read_csv("company_status_with_stage_clean_final.csv")
print(sorted(df_status["company_name"].unique()))
