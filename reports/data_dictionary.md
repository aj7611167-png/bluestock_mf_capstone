# Data Dictionary

## 01 Fund Master

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | AMFI Scheme Code |
| fund_house | Text | Mutual Fund House |
| scheme_name | Text | Scheme Name |
| category | Text | Scheme Category |
| sub_category | Text | Scheme Sub Category |

---

## 02 NAV History

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Scheme Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

---

## 03 AUM By Fund House

| Column | Data Type | Description |
|----------|----------|----------|
| fund_house | Text | Fund House |
| aum_crore | Float | Assets Under Management |
| date | Date | Reporting Date |

---

## 04 Monthly SIP Inflows

Tracks SIP inflows, SIP accounts and growth metrics.

---

## 05 Category Inflows

Tracks category-wise mutual fund inflows.

---

## 06 Industry Folio Count

Tracks folio growth across categories.

---

## 07 Scheme Performance

Contains returns, alpha, beta, sharpe ratio and expense ratio.

---

## 08 Investor Transactions

Contains investor transaction level records.

---

## 09 Portfolio Holdings

Contains scheme portfolio holdings.

---

## 10 Benchmark Indices

Contains benchmark index historical values.