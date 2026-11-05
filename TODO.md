# TODO

<!-- recommended-issue-order:start -->

## Recommended work order

Snapshot: November 3, 2026. GitHub Issues is disabled, so links below point to the authoritative local tasks.
Read top to bottom: quick wins, then priority work. Recheck source and prior
validation before implementing. Existing acceptance details remain below.

### Ready: quick wins

- ~~Reconcile worktree guidance and document the owning commands~~ — Done: slots `a`–`j` everywhere (verified `j` accepted, `k` rejected by `scripts/env.just`).

### Ready: priority order

- ~~Finish scoped quality gates and link classification~~ — Done 2026-11-04. Evidence: ruff 0.15.5, prek 0.5.7, dprint 0.64.3, markdownlint-cli2 0.24.0 all pass; `just links` found 5 broken and 30 unreachable links (sandbox network), not yet fixed.
- ~~Audit updater roots, action inputs and lock/cache ownership~~ — Done 2026-11-04 (roots cover uv, docker, compose, devcontainers, actions; CI uses `--locked` and `uv.lock`-keyed caches; `docker compose config` validates). Pin alignment (CI uv unpinned vs `.devcontainer/.env` 0.12.17) and runtime acceptance remain open.
- [Review branch/worktree ownership](#repository-maintenance) — Read-only comparison first; preserve unique and active work.

### Blocked or deferred

- [Add proposed cheat sheets one subject at a time](#p3-new-content) — Defer until existing documentation and maintenance work is complete.
- [Hosted CI/deployment and devcontainer runtime acceptance](#p2-dependencies-ci-and-containers) — Needs Actions/deployment access and a working container host; configuration fixes remain ready.
- [Ownership, review dates and cleanup decisions](#p1-documentation-quality) — Needs actual owner/human review; never invent dates or treat markers as completed reviews.

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
- [x] Add link checks that distinguish blocked networks from broken destinations.
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

## Review follow-up: November 2, 2026

Reviewed published `develop` at `efb06ed4da10ae8e5966f8bee47c6bb806f764de`.
Remaining follow-up work refines the existing quality and CI baseline:

- [x] **P2: Reconcile worktree policy.** `AGENTS.md` limits slots to `a`, `b`, and `c`,
      while README and WORKTREES.md permit `a` through `j`. Use one documented set that
      agrees with `scripts/env.just`; verify permitted and rejected slots without moving
      existing worktrees. Preserve the independent empty `main` history.
- [x] **P3: State the Python/documentation contract in AGENTS.md.** Keep the shared
      storage and Git rules, but add the owning unittest, Node test, MkDocs, and
      configuration-check commands from README and Justfile. Keep this documentation
      repository's historical-content exceptions explicit instead of importing Rust rules.

Validation: Python 3.15.2 parsed the tracked Python test source; every tracked TOML file
parsed; `prek validate-config D:/code/cheatsheets/prek.toml` passed. All configured local
action references resolve. dprint failed as recorded above. These are syntax/configuration
checks, not a site-build, full-hook, container, or hosted-deployment pass.
