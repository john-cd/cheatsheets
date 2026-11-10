# TODO

<!-- recommended-issue-order:start -->

## Ready and blocked work

Snapshot: November 10, 2026. GitHub Issues is disabled, so this file is the backlog; links point to local sections.

### Blocked

#### CI unavailable

- [Exercise hosted CI and deployment](#p2-dependencies-ci-and-containers) — hosted Actions is unavailable.

#### Human decisions and reviews

- [Category ownership and last-review metadata](#p1-documentation-quality) — needs an actual owner review; never invent dates.
- [Temporary/LLM file cleanup](#repository-maintenance) — needs an ownership decision per file.
- [New cheat sheet subjects](#p3-new-content) — owner deferred until maintenance work is complete.

#### Hardware, external host or account

- Recheck the 29 links unreachable from the sandbox with normal network access.

<!-- recommended-issue-order:end -->

GitHub Issues is disabled (reverified 2026-11-02). This is the authoritative backlog.
Use American spelling and LF; record evidence before marking a task complete.

## P1: documentation quality

Problem: maintenance metadata still needs review.

- [ ] Add category ownership and last-review metadata after actual review.

Acceptance: category ownership and review dates reflect actual human review.

## P2: quality gates

Problem: Python checks alone do not validate the maintained documentation/tooling content.

- [x] Confirm Ruff rules and scoped hooks without weakening stricter rules or examples.
- [x] Cover Markdown, TOML, YAML, and shell content with applicable format/lint commands.
- [x] Classify inconclusive HTTP statuses as blocked, retry unsupported HEAD requests with GET, and test CLI exit behavior.
- [x] Run read-only format/lint/prek checks; record versions, scope, and actual failures.
- [x] Keep README, AGENTS.md, CONFIGURATION.md, and WORKTREES.md synchronized.

Acceptance: maintained file types have runnable quality gates; commands and results are recorded.
Do not report skipped checks as passing or synchronize full runtime dependencies for formatting.

## P2: dependencies, CI, and containers

Problem: updater coverage and runtime/cache behavior still require verification.

- [x] Audit Dependabot roots for uv, Docker, Compose, devcontainers, and GitHub Actions.
- [x] Preserve lock ownership, registries, justified exclusions, and non-overlapping updates.
- [x] Validate workflow/local-action references, supported inputs, and security checks.
- [x] Use locked uv resolution and caches keyed by the owning lockfiles.
- [x] Pin exact Python, uv, Just, Docker CLI, and Docker feature versions; keep the local and container Python pins synchronized.
- [x] Validate Compose base/override, build/start the devcontainer, run its Python/Docker checks, and build the CI image.
- [ ] Exercise hosted CI.

Acceptance: dependency roots have explicit coverage/dispositions, pins and build contexts agree,
and hosted/container behavior has logs. Local evidence: Compose base/override/CI configuration validated;
Python 3.15.2 and Docker CLI 29.9.3 run in the container; `just check` passes all 18 tests,
Ruff format, and Ruff lint; `just docs` and the CI image's MkDocs build pass. Schema parsing alone
is not runtime acceptance.

## P3: new content

Problem: requested subjects are not yet covered by reviewed cheat sheets.

- [ ] Advanced GitHub Actions: reusable workflows, caching, and matrix builds.
- [ ] Platform engineering: golden paths, templates, and scorecards.
- [ ] Observability: OpenTelemetry and metrics/logs/traces correlation.
- [ ] AI engineering: RAG, prompt patterns, evaluation loops, and safety checks.
- [ ] Data contracts and schema evolution.
- [ ] Kubernetes security: PSA/PSS, RBAC, and network policies.
- [ ] Cloud workload FinOps.
- [ ] Incident response and postmortems.

Acceptance for each subject: a scoped page with use cases, checked examples, references,
and navigation/cross-links; distinguish proposals from published content.

## Repository maintenance

- [x] Review dirty worktrees and topic/backup branches; commit reviewed work separately.
- [x] Integrate useful work linearly into develop; retire only verified obsolete branches/worktrees.
- [ ] Review candidate temporary/LLM files by ownership/history before cleanup.
- [x] Preserve active work, unique commits, reusable caches, and permitted worktree slots.
- [x] Update WORKTREES.md with the reviewed dispositions.

Acceptance: every cleanup target has a recorded disposition and no unrelated work is lost.
Human/account/host blockers belong here with their concrete prerequisites; no upstream-release
wait is currently inventoried. Add a release trigger and review date when one is identified.
