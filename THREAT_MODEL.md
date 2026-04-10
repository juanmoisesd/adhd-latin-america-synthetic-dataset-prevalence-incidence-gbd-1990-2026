# Threat Model

## Scope

This threat model covers the ADHD Latin America synthetic dataset repository, including its data generation scripts, metadata, and dashboard.

## Assets

-   **Synthetic Dataset**: The primary product of the repository.
-   **Integrity Metadata**: Checksums, Merkle manifests, and attestations.
-   **Source Code**: ETL scripts and dashboard logic.

## Threats & Mitigations

| Threat | Description | Mitigation |
| :--- | :--- | :--- |
| **Data Tampering** | An attacker modifies the synthetic data to introduce bias or incorrect trends. | Multi-layered integrity checks (SHA, Merkle) and SLSA provenance. |
| **Metadata Forgery** | An attacker modifies checksums or manifests to hide data tampering. | Future implementation: Digital signatures (minisign/cosign) for manifests. |
| **Pipeline Poisoning** | Malicious code is injected into the ETL pipeline. | SLSA Level 2+ practices, CI/CD security workflows, and code reviews. |
| **Dependency Vulnerabilities** | Vulnerabilities in Python libraries (pandas, jsonschema). | Dependabot alerts and regular security scanning (Bandit). |

## Risk Assessment

The primary risk is the loss of trust in the synthetic data's provenance. By providing verifiable cryptographic proofs of the data's origin and state, we minimize this risk.
