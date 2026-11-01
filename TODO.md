# TODO

GitHub Issues are currently disabled for this repository, so this file is the authoritative backlog for the remaining follow-up tasks.

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

## Configuration alignment (2026-11-01)

The configuration-alignment work is integrated into `develop` in focused commits.

GitHub Issues is disabled for this repository, so the remaining tasks are recorded here.

### [P2] Finish shared formatting, lint, and hook policy validation

Ruff formatting completed locally; finish lint and CI evidence without pulling the full application stack into formatting hooks.

#### Acceptance criteria

- [ ] Review the local Rustfmt/Clippy and/or Ruff changes and commit formatting separately from behavior changes. Use the pinned formatter, American spelling, UTF-8, and LF.
- [ ] Align the Ruff baseline without weakening existing stronger rules; retain documented lesson/example exceptions and project Python pins.
- [ ] Make formatter/linter hooks operate on the appropriate languages/projects. Avoid whole-workspace auto-formatting during unrelated configuration commits and avoid full runtime dependency synchronization for Python quality checks.
- [ ] Run the owning Just/Cargo Make format and read-only lint commands. Record exact scope, platform, versions, and remaining failures; fix causes rather than applying unsafe blanket fixes or claiming skipped hooks passed.
- [ ] Keep `AGENTS.md`, `CONTRIBUTING.md` where present, `README.md`, `CONFIGURATION.md`, `TODO.md`, and `WORKTREES.md` consistent with the final commands and exceptions.

Validation: repository format/lint recipes, relevant `prek` hooks, configuration parsing, and `git diff --check`. Pure formatting changes do not require unrelated application test suites.

### [P2] Complete dependency-update coverage and consistent CI caching

Dependency-update roots and caching conventions differ across the repositories. Changes are pending locally and need schema/runtime verification before acceptance.

## Audited roots

- `uv`: `/`
- `docker`: `/.devcontainer`
- `docker-compose`: `/.devcontainer`
- `devcontainers`: `/`
- `github-actions`: `/`

### Acceptance criteria

- [ ] Verify these roots against tracked manifests, independent workspaces, Python/uv projects, nested local actions, Dockerfiles/Compose files, devcontainers, charts, submodules, and supported toolchain files. Add omissions; keep immutable/malformed test fixtures intentionally excluded and documented.
- [ ] Validate Dependabot syntax and ecosystem/directory rules. Preserve repository-specific ignores/registries; avoid overlapping updates and replace pip coverage with uv where lock ownership requires it. Do not assume custom shell/version-pin strings are automatically updated.
- [ ] Use locked uv resolution and setup-uv caching keyed by the correct lockfiles. Validate the new/existing Python quality jobs and project-specific environment/output paths.
- [ ] Review all workflow/composite-action references and supported inputs with actionlint and relevant security checks. Keep toolchain, container, Python, formatter, and workflow pins compatible; verify Docker COPY contexts retain required source/configuration and omit local outputs/cache links.
- [ ] Exercise applicable hosted Linux/Windows/macOS jobs and container builds when prerequisites are available. Report unavailable CI/services/credentials explicitly, and fix failures in focused commits.
- [ ] Synchronize `.github` workflow documentation, `CONFIGURATION.md`, README/contributor guidance, TODO, and worktree notes with verified behavior.

Do not close on YAML parsing alone: attach command results and hosted-run evidence, or keep unmet criteria open. Existing shipping/security/test policies should be preserved unless a reviewed fix requires a change.
