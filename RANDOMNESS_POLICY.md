# Randomness and Reproducibility Policy

## 1. Deterministic Seeds
To ensure scientific reproducibility, all simulations and synthetic data generation scripts MUST use a fixed random seed.

## 2. Seed Registry
- **Synthetic Data Generation**: Seed 42.
- **ABM Calibration**: Seed 2025.
- **Monte Carlo Simulations**: Seed 1337.

## 3. Library Specifics
- `numpy.random.seed()`
- `random.seed()`
- `torch.manual_seed()` (if applicable)

## 4. Hardware and Environment
While seeds ensure software reproducibility, slight variations may occur across different OS/CPU architectures. The official environment is defined in the `Dockerfile`.
