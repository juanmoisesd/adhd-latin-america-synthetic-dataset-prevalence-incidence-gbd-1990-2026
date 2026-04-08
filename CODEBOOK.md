# Codebook: ADHD Latin America Synthetic Dataset

## Dataset Identification
- **Title**: ADHD in Latin America: Synthetic Dataset
- **Version**: 1.2.0
- **Authors**: Juan Moisés de la Serna Tuya

## Methodology
The dataset is generated via simulation using regional trends derived from the Global Burden of Disease (GBD) studies. National-level estimates for 20 Latin American countries are provided.

## Variables
1. **country**: Name of the country (20 unique values).
2. **year**: Year of the estimation (1990-2026).
3. **prevalence**: Estimated prevalence percentage of ADHD in the population.
4. **incidence**: Estimated incidence rate (new cases per year).
5. **n_cases**: Total estimated number of ADHD cases.

## Usage
Data is provided in CSV format in `data/raw/adhd_data.csv`.
