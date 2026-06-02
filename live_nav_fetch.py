import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, code in schemes.items():

    try:
        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            nav_df = pd.DataFrame(data["data"])

            nav_df.to_csv(
                f"data/raw/{scheme_name}_live_nav.csv",
                index=False
            )

            print(f"{scheme_name} saved successfully")

        else:
            print(f"Failed for {scheme_name}")

    except Exception as e:
        print(f"Error fetching {scheme_name}: {e}")