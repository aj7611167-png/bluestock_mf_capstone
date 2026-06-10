import pandas as pd

score = pd.read_csv(
    "reports/fund_scorecard.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
).lower()

if risk == "low":
    result = score.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(3)

elif risk == "moderate":
    result = score.sort_values(
        "fund_score",
        ascending=False
    ).head(3)

else:
    result = score.sort_values(
        "cagr",
        ascending=False
    ).head(3)

print("\nTop 3 Recommended Funds:\n")

print(
    result[
        [
            "amfi_code",
            "sharpe_ratio",
            "fund_score",
            "cagr"
        ]
    ]
)