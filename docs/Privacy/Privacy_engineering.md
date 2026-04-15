---
title: Privacy Engineering
tags: privacy
---

# Privacy Engineering

## Interesting Links

[Homomorphic Encryption](https://conferences.oreilly.com/artificial-intelligence/ai-ca/public/schedule/detail/76797)

## Technical Implementations for GDPR/CCPA

### Data Minimization

Collect only what is strictly necessary. Strip PII (Personally Identifiable Information) early in data pipelines.

### Data Anonymization and Pseudonymization

- **Anonymization**: Irreversibly altering data so it cannot identify individuals.
- **Pseudonymization**: Replacing identifiers with artificial identifiers (keys), where the mapping is stored securely.

### Right to be Forgotten (Data Erasure)

- Implement soft-deletes with bounded retention periods.
- Ensure automated jobs clean up hard-deleted data across all replicas and backups.

### Encryption

- **At Rest**: Transparent Data Encryption (TDE), encrypted EBS/S3 volumes.
- **In Transit**: Enforce TLS 1.2+ for all communications.
