# TODO

## Completed in this pass

- [x] Reviewed repository structure, automation, cheatsheets, and code artifacts.
- [x] Fixed pre-commit hook configuration for `markdown-link-check` (`v3.14.2` tag format).
- [x] Fixed markdown-link-check JSON config to avoid runtime crashes.
- [x] Updated CI platform/tooling versions:
  - [x] `actions/checkout` updated to `v6` in markdown lint workflow.
  - [x] `actions/setup-python` updated to `v6` in markdown lint workflow.
  - [x] Python version bumped from `3.12` to `3.13` in markdown lint workflow.
  - [x] Added PR validation flow in CI with Python + Node setup.
- [x] Added automated tests outside cheatsheet pages:
  - [x] `tests/test_docs_quality.py` for docs structure/quality checks.
  - [x] `tests/gatherStats.test.js` for `docs/includes/gatherStats.js`.
- [x] Improved all cheatsheets missing key structure by adding headings/sections/examples where needed.
- [x] Refreshed known outdated links in cheatsheets (Java, Scala and related references).
- [x] Fixed an address normalization bug in `gatherStats.js` and made helper logic testable.

## Follow-up fixes and suggestions

- [ ] Replace remaining legacy/outdated external references that are still reachable but suboptimal.
- [ ] Expand MkDocs nav to include all published docs pages now present under `docs/`.
- [ ] Add ownership/maintenance metadata per cheatsheet category (last review date, maintainer).
- [ ] Add link health checks that distinguish blocked-network failures from true dead links.

## Additional cheatsheet subjects to add

- [ ] GitHub Actions (advanced pipelines, reusable workflows, caching, matrix builds)
- [ ] Platform Engineering (golden paths, templates, scorecards)
- [ ] Observability (OpenTelemetry, metrics/logs/traces correlation)
- [ ] AI Engineering (RAG basics, prompt patterns, eval loops, safety checks)
- [ ] Data Contracts and Schema Evolution
- [ ] Kubernetes Security (PSA/PSS, RBAC patterns, network policies)
- [ ] FinOps for Cloud Workloads
- [ ] Incident Response and Postmortems
