# Repository configuration

Reviewed 2026-11-01. This is the consistency plan and reference for `cheatsheets`.
Keep this file, README, contributor guidance, and configuration comments synchronized.

## Consistency plan

1. Share LF/UTF-8 editing defaults and language formatting conventions.
2. Align lint baselines while preserving stricter rules, domain limits, and teaching examples.
3. Enumerate maintained dependency roots and use predictable monthly grouped updates.
4. Isolate checkout outputs, align dependency compiler flags, and make CI caches configuration-aware.
5. Validate format/lint and representative builds; measure cold/warm time and output size before
   promoting further optimization changes. Keep platform and integration blockers visible in TODO.

## File ownership

| Files | Convention |
| --- | --- |
| `.editorconfig`, `.gitattributes` | UTF-8 and LF, four-space Rust/Python, two-space configuration; preserve Markdown hard breaks and binary attributes. |
| `.gitignore`, `.dockerignore`, `.aiexclude` | Exclude outputs, compiler caches, environments, and worktrees; keep maintained configuration and lockfiles reviewable. Ignore files are not a security boundary. |
| `AGENTS.md`, `CONTRIBUTING.md`, `README.md` | Keep repository-specific commands, ownership, and examples; link this reference. |
| `Cargo.toml`, `clippy.toml`, `rustfmt.toml` | Workspace lint inheritance and a common baseline; preserve explicit exceptions and package compatibility requirements. |
| `pyproject.toml`, `uv.lock` | Ruff uses 100 columns and LF; explicit default E4/E7/E9/F lint selection. Keep project Python pins and locked resolution. |
| `prek.toml` | Keep the existing repository hook set and pinned hook revisions. Run the configured formatter and linter rather than duplicating policy in hooks. |
| `deny.toml`, `nextest.toml` | Keep dependency-license exceptions, test filters, and resource/time limits local. Nextest normally discovers `.config/nextest.toml`; a Cargo profile is selected separately. |
| `.github/`, `.devcontainer/`, `Dockerfile*` | Preserve deployment/platform behavior; align package coverage and cache inputs. Keep compiler/Python pins compatible with manifests and lockfiles. |

## Dependency updates

Dependabot runs monthly on Monday at 6:00 a.m. Pacific with grouped minor/patch updates. These are
the maintained roots; workspace members share their root manifest/lockfile. Immutable parser,
test-book, and malformed-manifest fixtures are excluded intentionally. Revisit this table and
`.github/dependabot.yml` whenever a manifest, Dockerfile, chart, or local action is added.
Python uv workspace members share the root lock; they do not need overlapping update entries.

| Ecosystem | Roots |
| --- | --- |
| `uv` | `/` |
| `docker` | `/.devcontainer` |
| `docker-compose` | `/.devcontainer` |
| `devcontainers` | `/` |
| `github-actions` | `/` |

GitHub Actions uses `/` for workflows and explicit directories for nested composite actions.
Dependabot can update supported toolchain files, container images/features, charts, and packages;
it does not update arbitrary version strings in shell scripts or custom formatter-pin files.

## CI caches

Rust-cache entries include toolchain/environment inputs plus workflow, job, architecture, and
Cargo-config/lockfile hashes. Save Rust artifact caches only on pushes to the default branch;
pull requests restore caches. Include the separate `build` directory for intermediate artifacts.
Keep specialized coverage, target, feature, and release jobs isolated. sccache is pinned where
installed, and incremental compilation stays disabled, including when using GitHub caches.
An artifact cache does not make Rust incremental compilation compatible with sccache.
Python workflows use setup-uv caching keyed by `uv.lock`, and commands retain `--locked`.
Container builds retain their existing cargo-chef/BuildKit strategy; when cooking dependencies,
use the same compiler, features, profile, target, flags, and build paths as the application build.

## Python environments

Use `just env`, `just uv sync --locked`, `just fmt`, and `just lint`. The project Justfile assigns
repo/project/worktree-specific external environments, caches, and outputs through
`CODE_PYTHON_ENV_ROOT`, `CODE_PYTHON_BUILD_ROOT`, and `CODE_PYTHON_OUTPUT_ROOT`.
Rust target/build/sccache links are unnecessary for this Python-only repository. Preserve
intentional broken or historical teaching examples; document exceptions where they are owned.

## Validation evidence

Validation results and remaining prerequisites are recorded here before the topic is committed.
No cross-platform performance improvement is claimed from configuration inspection alone.

## References

- [Cargo profiles](https://doc.rust-lang.org/cargo/reference/profiles.html) and
  [configuration precedence](https://doc.rust-lang.org/cargo/reference/config.html).
- [sccache Rust limitations](https://github.com/mozilla/sccache/blob/main/docs/Rust.md).
- [Dependabot options](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference).
- [Rust 1.90 LLD default](https://blog.rust-lang.org/2025/09/01/rust-lld-on-1.90.0-stable/),
  [LLD platforms](https://lld.llvm.org/), [mold](https://github.com/rui314/mold),
  [sold recommendation](https://github.com/bluewhalesystems/sold), and [Wild support](https://github.com/wild-linker/wild).
- [rust-analyzer target directory](https://rust-analyzer.github.io/book/configuration.html#rust-analyzercargotargetdir).
