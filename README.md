# Cheatsheets

[John's Cheatsheets](https://john-cd.com/cheatsheets/)

[John's Main Website](https://john-cd.com)

## Repo structure

This website is generated using [MkDocs](https://mkdocs.org) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

The source Markdown files are found in the `docs` folder. The generated HTML / JS is written to the external output path configured by `scripts/dev_env.py`. There is also a `drafts` folder for Markdown files that are not ready for publication.

`.devcontainer` contains the [Dev Container](https://code.visualstudio.com/docs/devcontainers/containers) file and associated [Docker Compose](https://docs.docker.com/compose/) and [Dockerfile](https://docs.docker.com/reference/dockerfile/) setup. `github/workflows` contains the GitHub Action continuous deployment workflow.

## Contributing

### Install

If you use [Visual Studio Code](https://code.visualstudio.com/), install the [Dev Container extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). Otherwise, consider the [Dev Container CLI](https://containers.dev/supporting#devcontainer-cli). `Dev Container` allows you to edit and test the web site within a `Docker` container.

Alternatively, install Python 3.15, `uv`, and [Docker](https://www.docker.com/) on your development machine.

```powershell
python scripts/dev_env.py env
python scripts/dev_env.py uv sync --locked
python scripts/dev_env.py uv tool install prek
python scripts/dev_env.py prek install
```

### Basic MkDocs Commands

- `python scripts/dev_env.py uv run mkdocs serve` starts the live-reloading docs server.
- `python scripts/dev_env.py uv run mkdocs build` builds the documentation site.
- `python scripts/dev_env.py uv run mkdocs --help` prints the command help.

### Validation and tests

```bash
python scripts/dev_env.py prek run --all-files
python scripts/dev_env.py uv run python -m unittest discover -s tests -p "test_*.py"
node --test tests/*.test.js
python scripts/dev_env.py uv run mkdocs build
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
`uv.lock` pins the MkDocs environment and `.python-version` selects Python 3.15. Use `python scripts/dev_env.py env` to display the active worktree, Python environment, cache, build, output, uv, prek, and temporary-directory settings.

Python caches and generated outputs use per-repository, per-project, per-worktree subdirectories under `CODE_PYTHON_BUILD_ROOT` and `CODE_PYTHON_OUTPUT_ROOT`; MkDocs writes to the configured output subdirectory for the active worktree. Python environments and package caches use `CODE_PYTHON_ENV_ROOT` and `CODE_PACKAGES_ROOT`. The roots are configurable through environment variables. Windows defaults are `D:\packages\uv\environments`, `D:\temp\python-build`, `D:\temp\python-output`, `D:\packages`, `C:\tools`, and `D:\temp` (with `C:\temp` as fallback); Unix-like defaults use native home directories and the existing `TMPDIR` or `/tmp`. `CODE_BUILD_ROOT`, `CODE_TARGET_ROOT`, and `CODE_SCCACHE_ROOT` are reserved for Rust/Cargo tooling.

## Consistent Python and hook tooling

Use `uv` for Python dependencies and commands. Each standalone Python project
commits `uv.lock` and `.python-version`; uv workspace members share their root's
lockfile and Python pin. Run `uv sync --locked` before development.

Use `prek` with `prek.toml`: run `prek install` and `prek run --all-files`.
Keep linked worktrees in `.worktrees/a` through `.worktrees/j`; inspect existing
checkouts before reusing a slot and preserve active or dirty work.

Run tools through `python scripts/dev_env.py` (use `--project <directory>`
before the command for a nested Python project). For example,
`python scripts/dev_env.py uv sync --locked` and
`python scripts/dev_env.py prek run --all-files`. `env` displays resolved paths.
The helper sets `PIP_CACHE_DIR`, `UV_CACHE_DIR`, and `PREK_HOME` under
`CODE_PACKAGES_ROOT` (default `D:/packages`), reserved for packages, crates, and
library caches. Python interpreters and installed tools use `CODE_TOOLS_ROOT`
(default `C:/tools`): `UV_PYTHON_INSTALL_DIR` is `C:/tools/uv/python`,
`UV_TOOL_DIR` is `C:/tools/uv/tools`, and `UV_TOOL_BIN_DIR` is `C:/tools/uv/bin`. Environments are isolated by
repository, project, and worktree under `CODE_PYTHON_ENV_ROOT`; its default follows
`CODE_PACKAGES_ROOT/uv/environments`. Python caches and outputs use
`CODE_PYTHON_BUILD_ROOT` and `CODE_PYTHON_OUTPUT_ROOT` under `CODE_TEMP_ROOT`.
These settings leave Rust build, target, and sccache directories to Rust tooling.
