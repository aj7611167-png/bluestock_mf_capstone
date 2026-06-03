import pandas as pd
from sqlalchemy import create_engine

print("=" * 80)
print("LOADING DATA INTO SQLITE")
print("=" * 80)

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

# Fund Dimension
fund = pd.read_csv(
    "data/processed/01_fund_master_cleaned.csv"
)

fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("dim_fund loaded")

# NAV Fact
nav = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("fact_nav loaded")

# AUM Fact
aum = pd.read_csv(
    "data/processed/03_aum_by_fund_house_cleaned.csv"
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("fact_aum loaded")

# Transactions Fact
transactions = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("fact_transactions loaded")

# Performance Fact
performance = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("fact_performance loaded")

print("=" * 80)
print("DATABASE CREATED SUCCESSFULLY")
print("=" * 80)