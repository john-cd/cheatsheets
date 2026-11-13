# TODO

<!-- recommended-issue-order:start -->

## Ready and blocked work

Snapshot: November 13, 2026. GitHub Issues is disabled, so this file is the backlog; links point to local sections.

### Blocked

#### CI unavailable

- [Exercise hosted CI and deployment](#p2-dependencies-ci-and-containers) — hosted Actions is unavailable.

#### Human decisions and reviews

- [Category ownership and last-review metadata](#p1-documentation-quality) — needs an actual owner review; never invent dates.
- [Temporary/LLM file cleanup](#repository-maintenance) — needs an ownership decision per file.
- [New cheat sheet subjects](#p3-new-content) — owner deferred until maintenance work is complete.

#### Hardware, external host or account

- Recheck the 44 URLs that `just links` classified as 15 blocked responses and 29 network failures (418 checked, 0 confirmed broken); distinguish intentional teaching placeholders from unavailable destinations.

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

## P2: tool pin maintenance

Problem: Dependabot does not update tool versions stored only in formatter configuration or command recipes.

- [ ] Consider a review-only updater for dprint plugin and `npx` CLI pins; retain `just deps-upgrade` as the manual fallback.

Current disposition (2026-11-12): `just deps-upgrade` already refreshes uv, dprint plugin, and prek pins, but does not update the `markdownlint-cli2` version in `justfile`. Keep this task open; do not automate PR creation until hosted Actions is available for workflow validation.

Acceptance: custom tool pins receive reviewable updates with formatter, lint, and CI evidence; updates are not auto-merged.

## P2: documentation platform

Problem: Material for MkDocs is in maintenance mode, with upstream critical maintenance ending May 5, 2027.

- [ ] Evaluate a gradual Zensical migration, including this site's plugins, customizations, deployment, and rendered page parity.

Assessment (2026-11-12): the lock currently resolves Material for MkDocs 9.8.1. A trial of Zensical 0.0.68 could read the existing project but rejected the required external `MKDOCS_SITE_DIR` with `site_dir must be within project root`. This repository keeps generated output outside the checkout. Zensical's migration guide also notes that `gh-deploy` is not provided, so the Pages publishing workflow needs a replacement. Keep Material for MkDocs while its critical-fix window remains open; complete a build-output and deployment parity trial before switching. See the [Zensical migration guide](https://zensical.org/docs/compatibility/mkdocs/migration/), [plugin compatibility notes](https://zensical.org/docs/compatibility/mkdocs/plugins/), and [Material maintenance timeline](https://squidfunk.github.io/mkdocs-material/changelog/).

Acceptance: a tested migration decision preserves URLs, navigation, redirects, search, and publishing behavior.

## Repository review (2026-11-13)

- [x] Give the docs toolchain a reproducible compatibility check: `just sync` and `just docs` passed using Python 3.15.2, and `just links` checked 418 URLs with 0 confirmed broken (44 remain blocked or unreachable as detailed above). The current locked MkDocs plugins install and build on the pinned interpreter.
- [x] Remove `mkdocs-minify-plugin` and `mkdocs-redirects`; neither is enabled in `mkdocs.yml`, and removing them also removes their unused transitive dependencies. Update the container-pin test to check the Compose-to-Dockerfile build-argument wiring.

Validation on 2026-11-12: `uv lock --check`, `uv sync --locked`, Ruff format/lint, 21 Python tests, 4 Node tests, `dprint check`, and the MkDocs build passed. `prek run --all-files` passed its built-in hooks, Markdown lint, and link check; its two Ruff hooks could not start because the repository's Just recipes could not launch the bundled Git Bash shell in this Windows sandbox (`NtCreateDirectoryObject` access denied). The equivalent Ruff checks passed directly. Hosted CI remains unavailable.

- [x] Refresh supported tool pins and GitHub Actions references. CI now pins checkout, Python, Node, and dprint actions to immutable revisions; read-only workflows disable persisted checkout credentials, and the deploy job retains its required push credential. Python and Node runtime pins remain at their current releases.
- [x] Re-resolve dependency and formatter pins. `just deps-upgrade` and `just uv tree --outdated` found no newer compatible package pins; dprint plugins, prek hook revisions, and markdownlint-cli2 are current. The minimum prek version is aligned with the installed 0.5.7 tool.

Validation on 2026-11-13: `just sync`, format, Ruff lint, Markdown lint, dprint, `just docs`, `prek run --all-files` (including the external link checker), `prek validate-config prek.toml`, and actionlint passed. Python and Node test suites were not run during this maintenance pass. Hosted CI remains unavailable.
