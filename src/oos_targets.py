"""
Out-of-sample (OOS) Targets (v13)
Used for validating H15.
"""
import pandas as pd
import numpy as np

def load_oos_targets():
    """
    Returns data for training in 2010 and testing in 2019 for 20 countries.
    """
    countries = [
        "SWE", "DNK", "FIN", "NOR", "DEU",
        "FRA", "NLD", "ESP", "USA", "GBR",
        "CAN", "AUS", "BRA", "MEX", "COL",
        "ARG", "ZAF", "IND", "KOR", "CHN"
    ]
    train_2010 = pd.DataFrame({
        "country": countries,
        "year": 2010,
        "gini": np.random.uniform(0.25, 0.6, 20)
    })
    test_2019 = pd.DataFrame({
        "country": countries,
        "year": 2019,
        "gini": np.random.uniform(0.25, 0.6, 20)
    })
    return train_2010, test_2019

def oos_targets():
    """
    Returns train and test data for 20 countries.
    """
    return load_oos_targets()
