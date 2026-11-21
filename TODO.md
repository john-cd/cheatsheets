<!-- TODO Reviewed ??-??-2026. -->

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

Acceptance: maintained file types have runnable quality gates; commands and results are recorded.
Do not report skipped checks as passing or synchronize full runtime dependencies for formatting.

## P2: dependencies, CI, and containers

Problem: updater coverage and runtime/cache behavior still require verification.

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

- [ ] Review candidate temporary/LLM files by ownership/history before cleanup.

Acceptance: every cleanup target has a recorded disposition and no unrelated work is lost.
Human/account/host blockers belong here with their concrete prerequisites; no upstream-release
wait is currently inventoried. Add a release trigger and review date when one is identified.

## P2: tool pin maintenance

Problem: Dependabot does not update tool versions stored only in formatter configuration or command recipes.

- [ ] Add review-only update coverage for the `markdownlint-cli2` pin; retain `just deps-upgrade` as the manual fallback for other tool pins.

Assessment (2026-11-21): `justfile` pins `markdownlint-cli2` only inside an `npx` command (`0.24.1`), so the current Dependabot ecosystems cannot update it. Current CI runs `just hooks`, which uses the separate `markdownlint-cli` hook; it does not run `just markdownlint`. Recommended path: declare `markdownlint-cli2` as an exact root npm development dependency, commit the npm lockfile, point the Just recipe at the local binary, and add monthly npm Dependabot updates. Add `npm ci` and `just markdownlint` to PR CI so each reviewable update is checked; keep auto-merge disabled. This adds npm metadata and install work but avoids a custom workflow token. A custom workflow that edits the inline pin and opens PRs is possible, but PR checks created with `GITHUB_TOKEN` can require manual approval. Validate the selected CI path on hosted Actions before adopting it. npm listed 0.24.2 as latest on this date while the repository pins 0.24.1. See [Dependabot version updates](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates), [GITHUB_TOKEN workflow behavior](https://docs.github.com/en/actions/concepts/security/github_token), and [markdownlint-cli2 on npm](https://www.npmjs.com/package/markdownlint-cli2).

Acceptance: `markdownlint-cli2` updates arrive as reviewable PRs, PR CI runs the pinned CLI and existing checks, and updates are not auto-merged.

## P2: documentation platform

Problem: Material for MkDocs is in maintenance mode, with upstream critical maintenance ending May 5, 2027.

- [ ] Evaluate a gradual Zensical migration, including this site's plugins, customizations, deployment, and rendered page parity.

Assessment (2026-11-12): the lock currently resolves Material for MkDocs 9.8.1. A trial of Zensical 0.0.68 could read the existing project but rejected the required external `MKDOCS_SITE_DIR` with `site_dir must be within project root`. This repository keeps generated output outside the checkout. Zensical's migration guide also notes that `gh-deploy` is not provided, so the Pages publishing workflow needs a replacement. Keep Material for MkDocs while its critical-fix window remains open; complete a build-output and deployment parity trial before switching. See the [Zensical migration guide](https://zensical.org/docs/compatibility/mkdocs/migration/), [plugin compatibility notes](https://zensical.org/docs/compatibility/mkdocs/plugins/), and [Material maintenance timeline](https://squidfunk.github.io/mkdocs-material/changelog/).

Acceptance: a tested migration decision preserves URLs, navigation, redirects, search, and publishing behavior.

## Repository review (2026-11-13)

Validation on 2026-11-12: `uv lock --check`, `uv sync --locked`, Ruff format/lint, 21 Python tests, 4 Node tests, `dprint check`, and the MkDocs build passed. `prek run --all-files` passed its built-in hooks, Markdown lint, and link check; its two Ruff hooks could not start because the repository's Just recipes could not launch the bundled Git Bash shell in this Windows sandbox (`NtCreateDirectoryObject` access denied). The equivalent Ruff checks passed directly. Hosted CI remains unavailable.

Validation on 2026-11-13: `just sync`, format, Ruff lint, Markdown lint, dprint, `just docs`, `prek run --all-files` (including the external link checker), `prek validate-config prek.toml`, and actionlint passed. Python and Node test suites were not run during this maintenance pass. Hosted CI remains unavailable.
