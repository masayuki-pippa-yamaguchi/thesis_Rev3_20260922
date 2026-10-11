import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("electricity_sigma_proxy_2013_2023.csv", parse_dates=["date"])

plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["roll_std_3m"], label="3-month rolling std (σ proxy)")
plt.xlabel("Date")
plt.ylabel("Rolling Std")
plt.title("Electricity Price Volatility (σ proxy)")
plt.grid(True)
plt.legend()

plt.savefig("sigma_proxy_plot.png", dpi=300, bbox_inches="tight")
