"""
Early Warning Signals (EWS) for Critical Transitions
v13 framework
"""
import numpy as np

def analytical_ews(x, ss_c=0.45):
    """
    Computes early warning signal. Should peak at ss_c.
    Common EWS are increase in variance or autocorrelation.
    """
    alpha = 20
    # Peak at ss_c using a narrow Gaussian or derivative of sigmoid
    return np.exp(-alpha * (x - ss_c)**2)

def rolling_variance(series, window=5):
    """
    Computes rolling variance for a time series.
    """
    if len(series) < window:
        return np.zeros_like(series)
    return series.rolling(window=window).var().fillna(0)
