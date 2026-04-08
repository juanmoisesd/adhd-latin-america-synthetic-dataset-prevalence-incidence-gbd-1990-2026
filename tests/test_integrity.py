import pandas as pd
import pytest
import os

def test_file_exists():
    assert os.path.exists("data/raw/adhd_data.csv")

def test_no_nulls():
    df = pd.read_csv("data/raw/adhd_data.csv")
    assert df.isnull().sum().sum() == 0

def test_country_count():
    df = pd.read_csv("data/raw/adhd_data.csv")
    assert len(df["country"].unique()) == 20

def test_year_range():
    df = pd.read_csv("data/raw/adhd_data.csv")
    assert df["year"].min() == 1990
    assert df["year"].max() == 2026

def test_positive_values():
    df = pd.read_csv("data/raw/adhd_data.csv")
    assert (df["prevalence"] >= 0).all()
    assert (df["incidence"] >= 0).all()
    assert (df["n_cases"] >= 0).all()
