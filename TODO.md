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

Implementation (2026-11-21): root `package.json` owns the exact `markdownlint-cli2` version; the Just recipe passes that version to `npx`, keeping downloads in `NPM_CONFIG_CACHE` under `CODE_PACKAGES_ROOT` without installing `node_modules` into the checkout. Monthly npm Dependabot updates are configured, and the Markdown workflow watches `package.json` and runs `just markdownlint` alongside the existing hooks. Updates remain review-only with no auto-merge. Local elevated checks passed; keep this task open until a hosted Dependabot update PR and its Markdown workflow run confirm the service-side behavior. npm listed 0.24.2 as latest on this date. See [Dependabot version updates](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates) and [markdownlint-cli2 on npm](https://www.npmjs.com/package/markdownlint-cli2).

Acceptance: Dependabot creates reviewable npm update PRs, the Markdown workflow runs the pinned CLI and existing checks, and updates are not auto-merged.

## P2: documentation platform

Problem: Material for MkDocs is in maintenance mode, with upstream critical maintenance ending May 5, 2027.

- [x] Evaluate a gradual Zensical migration, including output paths, plugins and Markdown extensions, navigation, search, publishing, and rendered page parity.

Assessment (2026-11-21): tested Zensical 0.1.3 against the repository. The real build fails before rendering with `site_dir must be within project root` because `just docs` configures the required absolute external `MKDOCS_SITE_DIR`; this conflicts with the repository rule to keep generated output outside the checkout. A copy under `C:\temp` built successfully with relative `site/` output and no issues. All 84 HTML route paths, all 83 sitemap URLs, and heading IDs on every page matched the Material build; both search indexes contain 790 documents. Navigation destinations matched after normalizing absolute and relative URL forms, apart from Material's home link and a `javascript:void(0)` control. There is no explicit MkDocs `plugins:` list, and the current Markdown/PyMdown configuration, including the custom TOC slugify callable, built successfully in the trial. No redirect plugin or map is configured. Two parity decisions remain: Zensical documents `navigation.indexes` and `toc.integrate` as incompatible, and its rendered search lacks Material's suggestion and share controls. Publishing was not trialled: this repo deploys with `mkdocs gh-deploy` to `gh-pages`, while Zensical has no `gh-deploy` command; its documented Pages artifact workflow requires changing the Pages source and still needs validation for the custom URL and both main/develop deployment triggers. Decision: no-go for migration under the current output-path rule; keep MkDocs. Reopen migration work if Zensical supports external output or the repository's output policy changes, then trial the Pages workflow and resolve the navigation/search choices before switching. See the [Zensical migration guide](https://zensical.org/docs/compatibility/mkdocs/migration/), [plugin compatibility notes](https://zensical.org/docs/compatibility/mkdocs/plugins/), [Python Markdown extension compatibility](https://zensical.org/docs/compatibility/markdown/python-markdown-extensions/), [navigation](https://zensical.org/docs/setup/navigation/), [search](https://zensical.org/docs/setup/search/), and [publishing guide](https://zensical.org/docs/publish-your-site/).

Acceptance: a current-version trial records the migration decision and open compatibility gates; the production builder stays in place until output paths, navigation, search, and publishing are compatible.

## Repository review (2026-11-13)

Validation on 2026-11-12: `uv lock --check`, `uv sync --locked`, Ruff format/lint, 21 Python tests, 4 Node tests, `dprint check`, and the MkDocs build passed. `prek run --all-files` passed its built-in hooks, Markdown lint, and link check; its two Ruff hooks could not start because the repository's Just recipes could not launch the bundled Git Bash shell in this Windows sandbox (`NtCreateDirectoryObject` access denied). The equivalent Ruff checks passed directly. Hosted CI remains unavailable.

Validation on 2026-11-13: `just sync`, format, Ruff lint, Markdown lint, dprint, `just docs`, `prek run --all-files` (including the external link checker), `prek validate-config prek.toml`, and actionlint passed. Python and Node test suites were not run during this maintenance pass. Hosted CI remains unavailable.
