import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

# ============================================
# 1. スクレイピング関数（1ヶ月分）
# ============================================
def scrape_month(year, month):
    url = f"https://www.jepx.org/market/spot/{year}{month:02d}.html"
    print("取得中:", url)

    r = requests.get(url)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, "html.parser")

    table = soup.find("table")
    if table is None:
        print("表が見つかりません:", url)
        return []

    rows = table.find_all("tr")

    data = []
    for row in rows[1:]:
        cols = [c.get_text(strip=True) for c in row.find_all("td")]
        if len(cols) < 5:
            continue

        date_str = cols[0]
        system_price = cols[4]

        try:
            date = datetime.strptime(date_str, "%Y/%m/%d")
            price = float(system_price)
            data.append([date, price])
        except:
            continue

    return data

# ============================================
# 2. 全期間（2016/4〜2025/3）を取得
# ============================================
all_data = []

for year in range(2016, 2026):
    for month in range(1, 13):
        if (year == 2016 and month < 4):
            continue
        if (year == 2025 and month > 3):
            continue

        monthly_data = scrape_month(year, month)
        all_data.extend(monthly_data)

# ============================================
# 3. DataFrame 化
# ============================================
df = pd.DataFrame(all_data, columns=["date", "system_price"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

# ============================================
# 4. 月次標準偏差 σ を計算
# ============================================
monthly_sigma = (
    df.groupby(["year", "month"])["system_price"]
      .std()
      .reset_index()
      .rename(columns={"system_price": "sigma"})
)

print("\n=== 月次 σ（先頭5行） ===")
print(monthly_sigma.head())

# ============================================
# 5. CSV に保存
# ============================================
monthly_sigma.to_csv("jepx_monthly_sigma_2016_2025.csv", index=False, encoding="utf-8-sig")
print("\n保存しました: jepx_monthly_sigma_2016_2025.csv")
