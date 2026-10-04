import requests
import pandas as pd
import time

API_KEY = "11d2be6a-cab1-446b-b736-d6345c9b6982"   # ←あなたの API Key

# 36社のテンプレート
companies = [
    ("BGI001","British Gas Trading Ltd","03078711"),
    ("BGI002","EDF Energy Customers Ltd","02228297"),
    ("BGI003","E.ON UK Ltd","03782443"),
    ("BGI004","Scottish Power Energy Retail Ltd","SC190287"),
    ("BGI005","Octopus Energy Ltd","09263424"),
    ("BGI006","OVO Energy Ltd","06890795"),
    ("BGI007","Shell Energy Retail Ltd","03603172"),
    ("ENG001","SSE Energy Supply Ltd","03757502"),
    ("ENG002","Axpo UK Ltd","06600942"),
    ("ENG003","Bryt Energy Ltd","10167351"),
    ("ENG004","Brook Green Supply Ltd","09910619"),
    ("ENG005","Corona Energy Retail Ltd","03241002"),
    ("ENG006","Hudson Energy Supply UK Ltd","07489042"),
    ("ENG007","Utilita Energy Ltd","04849181"),
    ("ENG008","Good Energy Ltd","03899612"),
    ("ENG009","Ecotricity Ltd","03043412"),
    ("ENG010","ESB Energy","09688977"),
    ("ENG011","Rebel Energy","10952085"),
    ("ENG012","Zog Energy","08222325"),
    ("ENG013","SmartestEnergy Ltd","03994598"),
    ("ENG014","Bulb Energy Ltd","08469555"),
    ("ENG015","Avro Energy Ltd","09174794"),
    ("ENG016","Green Supplier Ltd","11042716"),
    ("ENG017","People's Energy Ltd","SC522897"),
    ("ENG018","Pure Planet Ltd","09735688"),
    ("ENG019","Igloo Energy Supply Ltd","09812716"),
    ("ENG020","Symbio Energy Ltd","07999360"),
    ("ENG021","HUB Energy Ltd","15216264"),
    ("ENG022","Neon Reef Ltd","10871657"),
    ("ENG023","Together Energy Ltd","SC533489"),
    ("ENG024","Orbit Energy","09933313"),
    ("ENG025","ESB Energy Retail Ltd","09688977"),
    ("ENG026","Outfox the Market (Foxglove Energy Supply Ltd)","10434389"),
    ("ENG027","Entice Energy Supply Ltd","10145964"),
    ("ENG028","Bluegreen Energy Services Ltd","11449956"),
    ("ENG029","Avro Energy Trading Ltd","09174794"),
]

def get_company_status(company_number):
    """Companies House API からステータスと倒産日を取得"""
    url = f"https://api.company-information.service.gov.uk/company/{company_number}"
    response = requests.get(url, auth=(API_KEY, ""))

    if response.status_code != 200:
        return None, None

    data = response.json()

    # 会社ステータス
    status = data.get("company_status", None)

    # 倒産日（Administration 開始日）
    admin_date = data.get("date_of_cessation", None)

    return status, admin_date


# 結果を格納するリスト
records = []

for cid, name, number in companies:
    print(f"Fetching: {cid} {name} ({number})")
    status, insolvency_date = get_company_status(number)
    records.append([cid, name, number, status, insolvency_date])
    time.sleep(0.5)  # API 負荷軽減

# DataFrame に変換
df = pd.DataFrame(records, columns=[
    "company_id", "company_name", "company_number",
    "company_status", "administration_start_date"
])

# CSV に保存
df.to_csv("company_status.csv", index=False)
print("company_status.csv を作成しました。")
