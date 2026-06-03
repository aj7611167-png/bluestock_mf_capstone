-- 1. Top 5 Funds by AUM

SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 3. Total Transactions by State

SELECT
state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 4. Expense Ratio Below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5. Top Funds by 5 Year Return

SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 6. Average Transaction Amount

SELECT
AVG(amount_inr)
FROM fact_transactions;

-- 7. Transactions By Type

SELECT
transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 8. Fund Count By Category

SELECT
category,
COUNT(*)
FROM dim_fund
GROUP BY category;

-- 9. Highest NAV Recorded

SELECT
MAX(nav)
FROM fact_nav;

-- 10. Total AUM By Fund House

SELECT
fund_house,
SUM(aum_crore)
FROM fact_aum
GROUP BY fund_house;