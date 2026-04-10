# Security Policy

## Integrity Measures

To ensure the highest level of data integrity and prevent tampering, this repository implements a multi-layered cryptographic verification system:

1.  **SHA256 & SHA512 Checksums**: Every file in the repository is hashed.
2.  **Merkle Manifest**: A Merkle tree is generated for all repository files. The root hash provides a single point of verification for the entire state of the repository.
3.  **SLSA Provenance**: We provide SLSA (Supply-chain Levels for Software Artifacts) provenance for the synthetic data generation process.
4.  **In-Toto Attestations**: Metadata about the build environment and data transformations are captured in in-toto link files.

## Verifying Integrity

You can verify the integrity of this repository by running the included verification script:

```bash
bash scripts/security/verify_repo.sh
```

## Reporting a Vulnerability

If you discover a security vulnerability within this project, please follow the instructions in [VULNERABILITY_DISCLOSURE.md](VULNERABILITY_DISCLOSURE.md).
