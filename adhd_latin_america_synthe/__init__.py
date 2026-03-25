"""ADHD in Latin America: Synthetic Dataset on Prevalence, Incidence and Case Numbers (GBD-based, 1990–
DOI: https://github.com/juanmoisesd/adhd-latin-america-synthetic-dataset-prevalence-incidence-gbd-1990-2026 | GitHub: https://github.com/juanmoisesd/adhd-latin-america-synthetic-dataset-prevalence-incidence-gbd-1990-2026"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd, io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="https://github.com/juanmoisesd/adhd-latin-america-synthetic-dataset-prevalence-incidence-gbd-1990-2026".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs: raise ValueError("No CSV files found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite(): return f'de la Serna, Juan Moisés (2025). ADHD in Latin America: Synthetic Dataset on Prevalence, Incidence and Case Numbe. Zenodo. https://github.com/juanmoisesd/adhd-latin-america-synthetic-dataset-prevalence-incidence-gbd-1990-2026'
def info(): print(f"Dataset: ADHD in Latin America: Synthetic Dataset on Prevalence, Incidence and Case Numbe\nDOI: https://github.com/juanmoisesd/adhd-latin-america-synthetic-dataset-prevalence-incidence-gbd-1990-2026\nGitHub: https://github.com/juanmoisesd/adhd-latin-america-synthetic-dataset-prevalence-incidence-gbd-1990-2026")