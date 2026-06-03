import pandas as pd
import os

print("=" * 80)
print("DAY 2 DATA CLEANING")
print("=" * 80)

raw_path = "data/raw"
processed_path = "data/processed"

os.makedirs(processed_path, exist_ok=True)

# ==========================
# 01 FUND MASTER
# ==========================

fund_master = pd.read_csv(f"{raw_path}/01_fund_master.csv")

fund_master = fund_master.drop_duplicates()

fund_master.to_csv(
    f"{processed_path}/01_fund_master_cleaned.csv",
    index=False
)

print("Fund Master Cleaned")

# ==========================
# 02 NAV HISTORY
# ==========================

nav = pd.read_csv(f"{raw_path}/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav = nav[
    nav["nav"] > 0
]

nav.to_csv(
    f"{processed_path}/02_nav_history_cleaned.csv",
    index=False
)

print("NAV History Cleaned")

# ==========================
# 03 AUM
# ==========================

aum = pd.read_csv(
    f"{raw_path}/03_aum_by_fund_house.csv"
)

aum = aum.drop_duplicates()

aum.to_csv(
    f"{processed_path}/03_aum_by_fund_house_cleaned.csv",
    index=False
)

print("AUM Cleaned")

# ==========================
# 04 SIP INFLOWS
# ==========================

sip = pd.read_csv(
    f"{raw_path}/04_monthly_sip_inflows.csv"
)

sip = sip.drop_duplicates()

sip.to_csv(
    f"{processed_path}/04_monthly_sip_inflows_cleaned.csv",
    index=False
)

print("SIP Cleaned")

# ==========================
# 05 CATEGORY INFLOWS
# ==========================

category = pd.read_csv(
    f"{raw_path}/05_category_inflows.csv"
)

category = category.drop_duplicates()

category.to_csv(
    f"{processed_path}/05_category_inflows_cleaned.csv",
    index=False
)

print("Category Inflows Cleaned")

# ==========================
# 06 FOLIO COUNT
# ==========================

folio = pd.read_csv(
    f"{raw_path}/06_industry_folio_count.csv"
)

folio = folio.drop_duplicates()

folio.to_csv(
    f"{processed_path}/06_industry_folio_count_cleaned.csv",
    index=False
)

print("Folio Count Cleaned")

# ==========================
# 07 SCHEME PERFORMANCE
# ==========================

performance = pd.read_csv(
    f"{raw_path}/07_scheme_performance.csv"
)

performance = performance[
    (
        performance["expense_ratio_pct"] >= 0.1
    )
    &
    (
        performance["expense_ratio_pct"] <= 2.5
    )
]

performance.to_csv(
    f"{processed_path}/07_scheme_performance_cleaned.csv",
    index=False
)

print("Scheme Performance Cleaned")

# ==========================
# 08 INVESTOR TRANSACTIONS
# ==========================

transactions = pd.read_csv(
    f"{raw_path}/08_investor_transactions.csv"
)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.title()
)

transactions = transactions[
    transactions["amount_inr"] > 0
]

valid_kyc = [
    "Verified",
    "Pending"
]

transactions = transactions[
    transactions["kyc_status"].isin(
        valid_kyc
    )
]

transactions.to_csv(
    f"{processed_path}/08_investor_transactions_cleaned.csv",
    index=False
)

print("Investor Transactions Cleaned")

# ==========================
# 09 PORTFOLIO
# ==========================

portfolio = pd.read_csv(
    f"{raw_path}/09_portfolio_holdings.csv"
)

portfolio = portfolio.drop_duplicates()

portfolio.to_csv(
    f"{processed_path}/09_portfolio_holdings_cleaned.csv",
    index=False
)

print("Portfolio Cleaned")

# ==========================
# 10 BENCHMARK
# ==========================

benchmark = pd.read_csv(
    f"{raw_path}/10_benchmark_indices.csv"
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

benchmark = benchmark.drop_duplicates()

benchmark.to_csv(
    f"{processed_path}/10_benchmark_indices_cleaned.csv",
    index=False
)

print("Benchmark Cleaned")

print("=" * 80)
print("ALL CLEANED FILES SAVED")
print("=" * 80)