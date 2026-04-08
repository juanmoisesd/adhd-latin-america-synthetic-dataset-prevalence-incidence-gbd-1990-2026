"""
Gini Timeseries (v13)
Generate/load timeseries for 20 countries.
"""
import pandas as pd
import numpy as np

def generate_timeseries(n_countries=20, n_obs=20):
    """
    Generate timeseries for 20 countries, 20 observations each (e.g., 2000-2019).
    """
    countries = [
        "SWE", "DNK", "FIN", "NOR", "DEU",
        "FRA", "NLD", "ESP", "USA", "GBR",
        "CAN", "AUS", "BRA", "MEX", "COL",
        "ARG", "ZAF", "IND", "KOR", "CHN"
    ]
    years = list(range(2000, 2000 + n_obs))
    data = []

    for c in countries:
        # Initial base Gini for the country
        base = 0.35 if c not in ["BRA", "MEX", "COL", "ARG", "ZAF"] else 0.5
        if c in ["SWE", "DNK", "FIN", "NOR"]: base = 0.28

        for y in years:
            # Random walk + trend
            val = base + (y-2000)*0.001 + np.random.normal(0, 0.005)
            data.append({"country": c, "year": y, "gini": val})

    return pd.DataFrame(data)

def load_gini_data():
    """
    Load Gini data for 20 countries and 20 observations each.
    """
    return generate_timeseries(20, 20)
