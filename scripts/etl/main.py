import os
import pandas as pd
import numpy as np

def generate_adhd_data():
    countries = ["Argentina", "Brazil", "Chile", "Colombia", "Mexico", "Peru", "Uruguay"]
    years = np.arange(1990, 2027)
    data = []

    np.random.seed(42)

    for country in countries:
        # Base prevalence and incidence for the country
        base_prev = np.random.uniform(2000, 3000)
        base_inc = np.random.uniform(80, 120)

        for year in years:
            # Linear trend with some noise
            trend = (year - 1990) * np.random.uniform(5, 15)
            prevalence = base_prev + trend + np.random.normal(0, 50)
            incidence = base_inc + (trend / 20) + np.random.normal(0, 5)
            cases = int(prevalence * np.random.uniform(500, 2000))

            data.append({
                "country": country,
                "year": int(year),
                "prevalence_rate": round(prevalence, 2),
                "incidence_rate": round(incidence, 2),
                "case_numbers": cases
            })

    df = pd.DataFrame(data)
    os.makedirs('data/analysis_ready', exist_ok=True)
    df.to_csv('data/analysis_ready/adhd_la_synthetic.csv', index=False)
    print(f"Generated {len(df)} records in data/analysis_ready/adhd_la_synthetic.csv")

if __name__ == "__main__":
    generate_adhd_data()
