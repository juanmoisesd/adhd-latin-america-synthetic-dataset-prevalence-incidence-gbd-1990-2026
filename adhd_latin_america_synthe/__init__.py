"""ADHD in Latin America: Synthetic Dataset on Prevalence, Incidence and Case Numbers (GBD-based, 1990-2026)
DOI: 10.5281/zenodo.19145316 | GitHub: https://github.com/juanmoisesd/adhd-latin-america-synthetic-dataset-prevalence-incidence-gbd-1990-2026"""

__version__ = "1.2.0"
__author__ = "de la Serna, Juan Moisés"

import pandas as pd
import io
import os

try:
    import requests
except ImportError:
    requests = None

def load_data(filename=None):
    """
    Load dataset. First looks in local data/ directory, then attempts to download from Zenodo.
    Returns pandas DataFrame.
    """
    # Try local first
    local_path = os.path.join("data", filename if filename else "adhd_latam_gbd_synthetic.csv")
    if os.path.exists(local_path):
        return pd.read_csv(local_path)

    if requests is None:
        raise ImportError("The 'requests' library is required for remote data loading. Install with: pip install requests")

    # Zenodo Record ID from DOI 10.5281/zenodo.19145316
    rid = "19145316"
    try:
        response = requests.get(f"https://zenodo.org/api/records/{rid}", timeout=30)
        response.raise_for_status()
        meta = response.json()
    except Exception as e:
        raise RuntimeError(f"Failed to fetch metadata from Zenodo: {e}")

    csvs = [f for f in meta.get("files", []) if f["key"].endswith(".csv")]
    if not csvs:
        raise ValueError("No CSV files found in the Zenodo record.")

    # Selection logic
    if filename:
        f = next((x for x in csvs if x["key"] == filename), None)
        if f is None:
            available = [x["key"] for x in csvs]
            raise ValueError(f"File '{filename}' not found. Available: {available}")
    else:
        f = csvs[0]

    try:
        data_resp = requests.get(f["links"]["self"], timeout=60)
        data_resp.raise_for_status()
        return pd.read_csv(io.StringIO(data_resp.text))
    except Exception as e:
        raise RuntimeError(f"Failed to download data from Zenodo: {e}")

def cite():
    return (
        "De la Serna Tuya, J. M. (2026). ADHD in Latin America: "
        "Synthetic Dataset on Prevalence, Incidence and Case Numbers (GBD-based, 1990–2026). "
        "Figshare. https://doi.org/10.6084/m9.figshare.31743112"
    )

def info():
    print("Dataset: ADHD in Latin America: Synthetic Dataset (GBD-based, 1990-2026)")
    print("Author: Juan Moisés de la Serna Tuya")
    print("DOI (Zenodo): 10.5281/zenodo.19145316")
    print("GitHub: https://github.com/juanmoisesd/adhd-latin-america-synthetic-dataset-prevalence-incidence-gbd-1990-2026")
