<!-- TODO Reviewed 11-23-2026. -->

# TODO

<!-- recommended-issue-order:start -->

## Ready and blocked work

Snapshot: November 23, 2026. GitHub Issues is enabled and has no open issues; this file tracks repository tasks, with links to local sections.

### Blocked

#### Human decisions and reviews

- [Category ownership and last-review metadata](#p1-documentation-quality) — needs an actual owner review; never invent dates.
- [Temporary/LLM file cleanup](#repository-maintenance) — needs an ownership decision per file.

<!-- recommended-issue-order:end -->

GitHub Issues is enabled, with zero open issues on 2026-11-22. This file is the authoritative task backlog.
Use American spelling and LF; record evidence before marking a task complete.

## P1: documentation quality

Problem: maintenance metadata still needs review.

- [ ] Add category ownership and last-review metadata after actual review.

Acceptance: category ownership and review dates reflect actual human review.

## P2: quality gates

Problem: Python checks alone do not validate the maintained documentation/tooling content.

Acceptance: maintained file types have runnable quality gates; commands and results are recorded.
Do not report skipped checks as passing or synchronize full runtime dependencies for formatting.

Validation (2026-11-22): fixed the hosted `just test` failure caused by hard-coded Docker feature version 1.10.1 after Dependabot updated the config and lock to 1.10.3. Local `just check-all` passes all 21 Python tests plus Ruff, dprint, and pinned markdownlint; `just hooks` also passes. Hosted `ci` run [#45111215683](https://github.com/john-cd/cheatsheets/actions/runs/45111215683) and `Prek checks` run [#45111215681](https://github.com/john-cd/cheatsheets/actions/runs/45111215681) both pass on commit `06368f4`.

## P2: dependencies, CI, and containers

Problem: updater coverage and runtime/cache behavior still require verification.

Validation (2026-11-23): the CI image built with the isolated `codex-cheatsheets-check-20261123` BuildKit builder, and the in-image MkDocs build completed. The default Docker Desktop builder still fails even for a minimal `/bin/sh` build (`exec format error`), so it was left untouched. A disposable container reported Python 3.15.2, uv 0.13.7, and just 1.59.0; its generated site served HTTP 200 at `http://127.0.0.1:18083/` with the expected HTML title and 68,442-byte response. The container was stopped; no existing images or caches were pruned. Hosted CI runs #45111215683 and #45111215681 pass. After PR #24 merged, develop push run [#45142181326](https://github.com/john-cd/cheatsheets/actions/runs/45142181326) passed both `validate` and `deploy`.

Acceptance: dependency roots have explicit coverage/dispositions, pins and build contexts agree,
and hosted/container behavior has logs. Local evidence: Compose base/override/CI configuration validated;
Python 3.15.2 and Docker CLI 29.9.3 run in the container; `just check` passes all 18 tests,
Ruff format, and Ruff lint; `just docs` and the CI image's MkDocs build pass. Schema parsing alone
is not runtime acceptance.

## P3: new content

Problem: requested subjects are not yet covered by reviewed cheat sheets.

Acceptance for each subject: a scoped page with use cases, checked examples, references,
and navigation/cross-links; distinguish proposals from published content.

## Repository maintenance

- [ ] Review candidate temporary/LLM files by ownership/history before cleanup. <!-- Partial (2026-11-22): the 12 archived `trash/` pages and 49 `.orig` snapshots are all tracked and have commit history; Git reports no untracked files. Their tracked history and review markers do not establish that they are disposable, so retain them pending an owner decision. -->

Acceptance: every cleanup target has a recorded disposition and no unrelated work is lost.
Human/account/host blockers belong here with their concrete prerequisites; no upstream-release
wait is currently inventoried. Add a release trigger and review date when one is identified.

## P2: tool pin maintenance

Problem: Dependabot does not update tool versions stored only in formatter configuration or command recipes.

- [ ] Add review-only update coverage for the `markdownlint-cli2` pin; retain `just deps-upgrade` as the manual fallback for other tool pins.

Implementation (2026-11-21): root `package.json` owns the exact `markdownlint-cli2` version; the Just recipe passes that version to `npx`, keeping downloads in `NPM_CONFIG_CACHE` under `CODE_PACKAGES_ROOT` without installing `node_modules` into the checkout. Monthly npm Dependabot updates are configured, and the Markdown workflow watches `package.json` and runs `just markdownlint` in an independent job so a network-dependent hook cannot skip the pinned CLI check. Updates remain review-only with no auto-merge. <!-- Partial (2026-11-23): hosted `Prek checks` run #45111215681 and Dependabot npm update run [#44962740852](https://github.com/john-cd/cheatsheets/actions/runs/44962740852) passed. No markdownlint-cli2 update PR was created; `0.24.2` remains the latest version. Keep this open for a later version update PR and its Markdown workflow run. --> `npm view markdownlint-cli2 version` returned 0.24.2. See [Dependabot version updates](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates) and [markdownlint-cli2 on npm](https://www.npmjs.com/package/markdownlint-cli2).

Acceptance: Dependabot creates reviewable npm update PRs, the Markdown workflow runs the pinned CLI and existing checks, and updates are not auto-merged.

## P2: documentation platform

Problem: Material for MkDocs is in maintenance mode, with upstream critical maintenance ending May 5, 2027.

Assessment (2026-11-21): tested Zensical 0.1.3 against the repository. The real build fails before rendering with `site_dir must be within project root` because `just docs` configures the required absolute external `MKDOCS_SITE_DIR`; this conflicts with the repository rule to keep generated output outside the checkout. A copy under `C:\temp` built successfully with relative `site/` output and no issues. All 84 HTML route paths, all 83 sitemap URLs, and heading IDs on every page matched the Material build; both search indexes contain 790 documents. Navigation destinations matched after normalizing absolute and relative URL forms, apart from Material's home link and a `javascript:void(0)` control. There is no explicit MkDocs `plugins:` list, and the current Markdown/PyMdown configuration, including the custom TOC slugify callable, built successfully in the trial. No redirect plugin or map is configured. Two parity decisions remain: Zensical documents `navigation.indexes` and `toc.integrate` as incompatible, and its rendered search lacks Material's suggestion and share controls. Publishing was not trialled: this repo deploys with `mkdocs gh-deploy` to `gh-pages`, while Zensical has no `gh-deploy` command; its documented Pages artifact workflow requires changing the Pages source and still needs validation for the custom URL and both main/develop deployment triggers. Decision: no-go for migration under the current output-path rule; keep MkDocs. Reopen migration work if Zensical supports external output or the repository's output policy changes, then trial the Pages workflow and resolve the navigation/search choices before switching. See the [Zensical migration guide](https://zensical.org/docs/compatibility/mkdocs/migration/), [plugin compatibility notes](https://zensical.org/docs/compatibility/mkdocs/plugins/), [Python Markdown extension compatibility](https://zensical.org/docs/compatibility/markdown/python-markdown-extensions/), [navigation](https://zensical.org/docs/setup/navigation/), [search](https://zensical.org/docs/setup/search/), and [publishing guide](https://zensical.org/docs/publish-your-site/).

Acceptance: a current-version trial records the migration decision and open compatibility gates; the production builder stays in place until output paths, navigation, search, and publishing are compatible.

## Repository review (2026-11-13)

Validation on 2026-11-12: `uv lock --check`, `uv sync --locked`, Ruff format/lint, 21 Python tests, 4 Node tests, `dprint check`, and the MkDocs build passed. `prek run --all-files` passed its built-in hooks, Markdown lint, and link check; its two Ruff hooks could not start because the repository's Just recipes could not launch the bundled Git Bash shell in this Windows sandbox (`NtCreateDirectoryObject` access denied). The equivalent Ruff checks passed directly. Hosted CI remains unavailable.

Validation on 2026-11-13: `just sync`, format, Ruff lint, Markdown lint, dprint, `just docs`, `prek run --all-files` (including the external link checker), `prek validate-config prek.toml`, and actionlint passed. Python and Node test suites were not run during this maintenance pass. Hosted CI remains unavailable.
