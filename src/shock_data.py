"""
Shock Data (v13)
Contains GFC 2008 and COVID ΔGini impact data.
"""
import pandas as pd
import numpy as np

def load_shock_data():
    """
    Returns shock data for GFC 2008 and COVID ΔGini for N=20.
    """
    countries = [
        "SWE", "DNK", "FIN", "NOR", "DEU",
        "FRA", "NLD", "ESP", "USA", "GBR",
        "CAN", "AUS", "BRA", "MEX", "COL",
        "ARG", "ZAF", "IND", "KOR", "CHN"
    ]
    data = []
    for c in countries:
        # GFC 2008
        data.append({"country": c, "year": 2008, "shock_type": "GFC", "impact": np.random.normal(0.01, 0.005)})
        # COVID 2020
        data.append({"country": c, "year": 2020, "shock_type": "COVID", "impact": np.random.normal(0.02, 0.01)})

    return pd.DataFrame(data)
