# Repository Requirements (User Request)

The user has requested a high-standard research repository structure ("0.001% standard") with the following components:

## A. Identidad, citación y versiones
- README.md
- README_es.md
- README_en.md
- ABSTRACT_es.md
- ABSTRACT_en.md
- CITATION.cff
- CITATION.bib
- CITATION.ris
- CITATION.csl.json
- VERSION
- CHANGELOG.md
- RELEASE_NOTES.md
- AUTHORS.md
- CONTRIBUTORS.md

## B. Legal, ética y cumplimiento
- LICENSE
- TERMS_OF_USE.md
- DATA_USE_AGREEMENT.md
- ETHICS.md
- PRIVACY.md
- DATA_PROTECTION.md
- SENSITIVE_FIELDS.md
- CONSENT_AND_REUSE.md
- DEIDENTIFICATION_PROTOCOL.md
- RETENTION_POLICY.md
- DEPRECATION_POLICY.md

## C. Metadatos interoperables (FAIR máximo)
- datacite.json
- dataset_description.json (schema.org JSON-LD)
- dcat-ap.json
- datapackage.json (Frictionless)
- codemeta.json
- ro-crate-metadata.json
- KEYWORDS.md
- RELATED_IDENTIFIERS.csv
- ORCID.yml

## D. Datos, esquema y semántica
- data/raw/
- data/clean/
- data/analysis_ready/
- CODEBOOK.md
- data_dictionary.csv
- schema.json
- sql/schema.sql
- UNITS_AND_CONVENTIONS.md
- MISSING_VALUES.md
- VALUE_LABELS.csv

## E. Provenance y trazabilidad (forense)
- PROVENANCE.md
- lineage/lineage.yaml
- lineage/prov.jsonld
- lineage/prov.ttl
- SOURCES.md
- source_registry.csv
- TRANSFORMATIONS.md
- scripts/etl/
- workflow/Snakefile o workflow/main.nf

## F. Calidad y validación
- QUALITY_REPORT.md
- quality/validation_report.json
- quality/validation_report.html
- quality/expectations/
- tests/test_schema.py
- tests/test_integrity.py
- BIAS_AND_LIMITATIONS.md
- DRIFT_BASELINE.json

## G. Reproducibilidad computacional
- requirements.txt
- environment.lock.yml
- Dockerfile
- docker-compose.yml
- Makefile
- run.sh
- notebooks/01_quickstart.ipynb
- examples/python/
- examples/r/
- examples/sql/
- RANDOMNESS_POLICY.md

## H. Integridad criptográfica y seguridad
- checksums.sha256
- checksums.sha512
- checksums.blake3
- manifest.json
- manifest.merkle
- signatures/minisign.pub
- signatures/release.minisig
- signatures/cosign.sig
- attestations/slsa-provenance.json
- attestations/in-toto.layout
- attestations/in-toto.link
- sbom.spdx.json
- sbom.cyclonedx.json
- timestamp/rfc3161.tsr
- tuf/root.json
- tuf/targets.json
- tuf/snapshot.json
- tuf/timestamp.json
- SECURITY.md
- THREAT_MODEL.md
- VULNERABILITY_DISCLOSURE.md
- INCIDENT_RESPONSE.md

## I. Gobernanza y operación
- GOVERNANCE.md
- RISK_REGISTER.md
- BUSINESS_CONTINUITY.md
- SUPPORT.md
- FAQ.md
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- MAINTAINERS.md

## J. Automatización CI/CD de datos
- .github/workflows/validate.yml
- .github/workflows/release.yml
- .github/workflows/security.yml
- .github/workflows/sign.yml
- .github/dependabot.yml

## Specific Advanced Requirements
- Firmas + atestaciones (cosign, in-toto, SLSA)
- Metadatos múltiples (DataCite + RO-Crate + DCAT + schema.org)
- Manifiesto con Merkle + sellado de tiempo
- Política formal de deprecación + DOI canónico por familia
- Validación automática en cada release
