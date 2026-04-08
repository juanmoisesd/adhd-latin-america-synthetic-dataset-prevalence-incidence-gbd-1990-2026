# Data Transformations

## 1. Generation (v1.0.0)
- Initial simulation of ADHD cases using Monte Carlo methods based on IHME ranges.
- Variables: `country`, `year`, `val`.

## 2. Cleaning & Standardization (v1.2.0)
- Renaming columns to `prevalence`, `incidence`, `n_cases`.
- Standardizing country names.
- Rounding float values to 3 decimal places for prevalence.
- Converting absolute case numbers to integers.

## 3. Analysis Ready Format
- Exporting to CSV and preparing SQL schemas.
- Adding comprehensive metadata fields.
