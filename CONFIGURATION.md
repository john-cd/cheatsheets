# Repository configuration

Reviewed 2026-11-01. This is the consistency plan and reference for `cheatsheets`.
<!-- TODO Reviewed ??-??-2026 -->

Keep this file, README, contributor guidance, and configuration comments synchronized.

## Consistency plan

1. Share UTF-8 and LF editing defaults while preserving repository-specific examples.
2. Keep Python versions, dependency pins, formatting, and lint rules consistent across local tasks and CI.
3. Maintain the declared dependency roots and predictable grouped updates.
4. Keep Python environments, caches, build files, and generated output in their configured external roots.
5. Validate formatting and lint locally; record platform or integration checks that remain unavailable.

## File ownership

| Files | Convention |
| --- | --- |
| `.editorconfig`, `.gitattributes` | Use UTF-8 and LF; use four-space Python indentation and two-space configuration indentation. |
| `.gitignore`, `.dockerignore`, `.aiexclude` | Exclude Python environments, caches, generated outputs, and worktrees; keep maintained configuration and lockfiles reviewable. Ignore files are not a security boundary. |
| `AGENTS.md`, `CONTRIBUTING.md`, `README.md` | Keep repository-specific commands, ownership, and examples; link this reference. |
| `pyproject.toml`, `uv.lock`, `.python-version` | Keep Python versions, dependency resolution, and Python tooling configuration in sync. |
| `prek.toml`, `dprint.json*` | Maintain the configured hooks and documentation formatting rules where these files are present. |
| `.github/`, `.devcontainer/`, `Dockerfile*` | Preserve workflow and container behavior; keep Python pins, dependency installation, and lockfile usage consistent. |

## Dependency updates

Dependabot runs monthly on Monday at 6:00 a.m. Pacific with grouped minor/patch updates. The maintained roots are the Python project at `/`, Docker and Compose under `/.devcontainer`, devcontainer features at `/`, and GitHub Actions at `/`. Revisit this section and `.github/dependabot.yml` whenever a dependency root, Dockerfile, chart, or local action is added.

| Ecosystem | Roots |
| --- | --- |
| `uv` | `/` |
| `docker` | `/.devcontainer` |
| `docker-compose` | `/.devcontainer` |
| `devcontainers` | `/` |
| `github-actions` | `/` |

GitHub Actions uses `/` for workflows and explicit directories for nested composite actions. Dependabot can update supported tool versions, container images/features, charts, and packages; it does not update arbitrary version strings in shell scripts or custom formatter-pin files.

## CI caches

Key Python dependency caches by the operating system, Python version, and `uv.lock`. Keep package caches separate from per-project and per-worktree build and output directories. Container builds should install from the committed lockfile and retain the repository's existing uv or pip caching strategy.

## Python environments

Use `just env`, `just uv sync --locked`, `just fmt`, and `just lint`. The project Justfile assigns repository/project/worktree-specific external environments, caches, and outputs through `CODE_PYTHON_ENV_ROOT`, `CODE_PYTHON_BUILD_ROOT`, and `CODE_PYTHON_OUTPUT_ROOT`. Preserve intentional broken or historical teaching examples; document exceptions where they are owned.

## Validation evidence

Record validation results and remaining prerequisites before integrating the topic. Do not claim cross-platform behavior from configuration inspection alone.

## References

- [Dependabot options](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference).
