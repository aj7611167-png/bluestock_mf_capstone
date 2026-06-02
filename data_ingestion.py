import pandas as pd
import os

DATA_PATH = "data/raw"

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("=" * 80)
print("BLUESTOCK MF DATA INGESTION")
print("=" * 80)

for file in files:

    file_path = os.path.join(DATA_PATH, file)

    try:
        df = pd.read_csv(file_path)

        print("\n" + "=" * 80)
        print(f"FILE : {file}")
        print("=" * 80)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error loading {file}: {e}")

print("\nData ingestion completed successfully.")