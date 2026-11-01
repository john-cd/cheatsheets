# TODO

GitHub Issues is disabled (verified 2026-11-01). This is the authoritative backlog.
Use American spelling and LF; record evidence before marking a task complete.

## P1: documentation quality

Problem: navigation, references, and maintenance metadata still need review.

- [ ] Replace reachable but obsolete references; retain intentional historical context.
- [ ] Include all published docs pages in MkDocs navigation.
- [ ] Add category ownership and last-review metadata after actual review.
- [ ] Add CONTRIBUTING.md with setup, format/lint/test/build commands and README links.

Acceptance: navigation covers published pages, links resolve or have documented exceptions,
and contributor instructions match the configured commands.

## P2: quality gates

Problem: Python checks alone do not validate the maintained documentation/tooling content.

- [ ] Confirm Ruff rules and scoped hooks without weakening stricter rules or examples.
- [ ] Cover Markdown, TOML, YAML, and shell content with applicable format/lint commands.
- [ ] Add link checks that distinguish blocked networks from broken destinations.
- [ ] Run read-only format/lint/prek checks; record versions, scope, and actual failures.
- [ ] Keep README, AGENTS.md, CONFIGURATION.md, and WORKTREES.md synchronized.

Acceptance: maintained file types have runnable quality gates; commands and results are recorded.
Do not report skipped checks as passing or synchronize full runtime dependencies for formatting.

## P2: dependencies, CI, and containers

Problem: updater coverage and runtime/cache behavior still require verification.

- [ ] Audit Dependabot roots for uv, Docker, Compose, devcontainers, and GitHub Actions.
- [ ] Preserve lock ownership, registries, justified exclusions, and non-overlapping updates.
- [ ] Validate workflow/local-action references, supported inputs, and security checks.
- [ ] Use locked uv resolution and caches keyed by the owning lockfiles.
- [ ] Pin reasonable software/image/feature versions in the central version source.
- [ ] Validate Compose base/override, build/start the devcontainer, and exercise hosted CI.

Acceptance: dependency roots have explicit coverage/dispositions, pins and build contexts agree,
and hosted/container behavior has logs. Schema parsing alone is not runtime acceptance.

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

- [ ] Review dirty worktrees and topic/backup branches; commit reviewed work separately.
- [ ] Integrate useful work linearly into develop; retire only verified obsolete branches/worktrees.
- [ ] Review candidate temporary/LLM files by ownership/history before cleanup.
- [ ] Preserve active work, unique commits, reusable caches, and permitted worktree slots.
- [ ] Update WORKTREES.md with the reviewed dispositions.

Acceptance: every cleanup target has a recorded disposition and no unrelated work is lost.
Human/account/host blockers belong here with their concrete prerequisites; no upstream-release
wait is currently inventoried. Add a release trigger and review date when one is identified.
