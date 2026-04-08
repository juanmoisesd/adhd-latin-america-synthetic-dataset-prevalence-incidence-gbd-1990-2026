# Threat Model

## 1. Assets
- Synthetic ADHD dataset (integrity).
- v13 Analytical Framework (correctness).
- Metadata and Lineage (traceability).

## 2. Adversaries
- Malicious actors attempting to inject false epidemiological trends.
- Automated bots trying to scrape or modify sensitive repo configurations.

## 3. Threat Vectors
- GitHub Actions compromise.
- Malicious dependency updates.
- Unauthorized metadata modification.

## 4. Mitigations
- Checksum verification for all data files.
- Cryptographic signatures for releases.
- SLSA L2/L3 compliance.
- Dependabot for vulnerability tracking.
