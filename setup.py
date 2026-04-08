from setuptools import setup, find_packages

setup(
    name="adhd-latin-america-synthetic-dataset-prevalence-incidence-gbd-1990-2026",
    version="1.2.0",
    description="ADHD in Latin America: Synthetic Dataset on Prevalence, Incidence and Case Numbers (GBD-based, 1990–2026)",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/adhd-latin-america-synthetic-dataset-prevalence-incidence-gbd-1990-2026",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0",
        "requests>=2.26.0",
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "statsmodels>=0.13.0"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
    ],
    keywords="zenodo, open-data, dataset, ADHD, epidemiology, Latin America",
)
