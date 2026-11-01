# Cheatsheets

[John's Cheatsheets](https://john-cd.com/cheatsheets/)

[John's Main Website](https://john-cd.com)

## Repo structure

This website is generated using [MkDocs](https://mkdocs.org) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

The source Markdown files are found in the `docs` folder. The generated HTML / JS is written to the external output path configured by the project Justfile. There is also a `drafts` folder for Markdown files that are not ready for publication.

`.devcontainer` contains the [Dev Container](https://code.visualstudio.com/docs/devcontainers/containers) file and associated [Docker Compose](https://docs.docker.com/compose/) and [Dockerfile](https://docs.docker.com/reference/dockerfile/) setup. `github/workflows` contains the GitHub Action continuous deployment workflow.

## Contributing

### Install

If you use [Visual Studio Code](https://code.visualstudio.com/), install the [Dev Container extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). Otherwise, consider the [Dev Container CLI](https://containers.dev/supporting#devcontainer-cli). `Dev Container` allows you to edit and test the web site within a `Docker` container.

Alternatively, install Just, Python 3.15, `uv`, and [Docker](https://www.docker.com/) on your development machine.

```powershell
just env
just sync
just uv tool install prek
just hooks-install
```

### Basic MkDocs Commands

- `just uv run mkdocs serve` starts the live-reloading docs server.
- `just uv run mkdocs build` builds the documentation site.
- `just uv run mkdocs --help` prints the command help.

### Validation and tests

```bash
just hooks
just uv run python -m unittest discover -s tests -p "test_*.py"
node --test tests/*.test.js
just uv run mkdocs build
```

Within a Dev Container, you may need to use `mkdocs serve --dev-addr 0.0.0.00:8000`.

### Docker Compose

To test the Docker Compose setup, try

```bash
docker compose -f .devcontainer/compose.yaml -f .devcontainer/compose.override.yaml up --build
docker compose down
```

and

```bash
docker compose -f .devcontainer/compose.yaml -f .devcontainer/compose-ci.yaml up --build
docker compose down
```

You may also build the image directly, e.g.: `docker build --file .devcontainer/Dockerfile --target dev --tag johncd/cheatsheets:latest .`
To push an image to your registry, use `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/) docs for more detail on building and pushing.
`uv.lock` pins the MkDocs environment and `.python-version` selects Python 3.15. Use `just env` to display the active worktree, Python environment, cache, build, output, uv, prek, and temporary-directory settings.

Python caches and generated outputs use per-repository, per-project, per-worktree subdirectories under `CODE_PYTHON_BUILD_ROOT` and `CODE_PYTHON_OUTPUT_ROOT`; MkDocs writes to the configured output subdirectory for the active worktree. Python environments and package caches use `CODE_PYTHON_ENV_ROOT` and `CODE_PACKAGES_ROOT`. The roots are configurable through environment variables. Windows defaults are `D:\packages\uv\environments`, `D:\temp\python-build`, `D:\temp\python-output`, `D:\packages`, `C:\tools`, and `D:\temp` (with `C:\temp` as fallback); Unix-like defaults use native home directories and the existing `TMPDIR` or `/tmp`. `CODE_BUILD_ROOT`, `CODE_TARGET_ROOT`, and `CODE_SCCACHE_ROOT` are reserved for Rust/Cargo tooling.

## Python tooling

Install Just and uv; Windows recipes use Git Bash. Each Python project has a
Justfile. Environment variables are defined in `scripts/env.just`, imported
by those Justfiles; no Python environment wrapper is required.

- `just env` — this repository.

From a project's directory, run `just sync`, `just fmt`, `just lint`, or
`just check`. `just --list` shows its available tasks. Named validation tasks
use `uv run --locked`; `just uv <args...>` forwards arbitrary uv commands and
`just run <command...>` runs a command in the locked environment.

`just hooks-install` installs the repository's prek hooks; `just hooks` runs
them against all files. Install prek first if needed with `just uv tool install prek`.

Virtual environments use `CODE_PYTHON_ENV_ROOT/<repo>/<project>/<slot>`.
Caches and generated files use matching paths under `CODE_PYTHON_BUILD_ROOT`
and `CODE_PYTHON_OUTPUT_ROOT`. The main checkout uses slot `main`; linked
worktrees use their letter. Configure `CODE_PACKAGES_ROOT` for uv/pip/prek
caches and `CODE_TOOLS_ROOT` for uv-managed interpreters and tools.
Windows defaults are `D:/packages`, `C:/tools`, and `D:/temp` for temporary
files; Unix uses `~/.local/share`, `~/.local/tools`, and native temporary paths.
`CODE_PYTHON_ENV_ROOT` defaults to `<packages>/uv/environments`; build and output
roots default to `<temp>/python-build` and `<temp>/python-output`.
`just env` prints the resolved values. `just uv build` routes distributions to the external
output directory unless an explicit `--out-dir` or `-o` is supplied.

## Checkout and storage policy

The primary checkout uses `develop`; `main` is an independent empty branch.
Auxiliary worktrees belong under `.worktrees/`, with names one lowercase letter from a through j only.
Storage roots are configurable through `CODE_REPOS_ROOT`, `CODE_TEMP_ROOT`,
`CODE_PACKAGES_ROOT`, and `CODE_TOOLS_ROOT`. Windows defaults are `D:/code`,
`D:/temp` (`C:/temp` fallback), `D:/packages`, and `C:/tools` respectively.
Unix uses native home/cache/temp paths. A root override changes destinations;
it does not move existing installations. Use `CODE_PYTHON_ENV_ROOT`,
`CODE_PYTHON_BUILD_ROOT`, and `CODE_PYTHON_OUTPUT_ROOT` for Python-specific paths.

## Repository configuration

See [CONFIGURATION.md](CONFIGURATION.md) for shared formatting, lint, dependency-update,
build-profile, cache, linker, and editor conventions. Keep it synchronized with configuration changes.
