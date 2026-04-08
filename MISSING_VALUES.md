# Missing Values Handling

## 1. Zero Tolerance
In this synthetic dataset, there are **no missing values**. Every country and year within the defined range (1990-2026) contains complete estimates.

## 2. Convention for Future Updates
Should future updates include missing data, the following conventions will be used:
- **Null / NaN**: For strictly missing values.
- **-999**: Indicator for data suppressed due to uncertainty.
- **NA**: For non-applicable fields.

## 3. Data Integrity
Integrity tests (`tests/test_integrity.py`) automatically check for the presence of null values in the CSV files.
