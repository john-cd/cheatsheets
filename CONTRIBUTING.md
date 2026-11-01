# Contributing

## Setup

Install Just, Python 3.15, `uv`, and `prek`. Windows Just recipes use Git Bash. From the repository root:

```powershell
just env
just sync
just uv tool install prek
just hooks-install
```

The committed `uv.lock` owns dependency resolution and `.python-version` selects Python. `scripts/env.just` defines project environments, caches, and generated output roots; change those roots through the documented `CODE_*` environment variables rather than writing generated files into the checkout.

## Checks

```powershell
just fmt
just lint
just check
just test
just docs
just hooks
```

`just --list` shows all recipes. `just check` runs formatting checks, Ruff, and unit tests. `just docs` builds MkDocs into the configured external output directory. Run `node --test tests/*.test.js` for the maintained JavaScript tests.

## Configuration and documentation

`pyproject.toml` owns Python dependencies and Ruff policy; `uv.lock` records the resolved environment; `prek.toml` owns repository hooks; `mkdocs.yml` and `docs/` own the published site. Keep the README, `CONTRIBUTING.md`, MkDocs navigation, and command examples synchronized when setup or tooling changes. Validate documentation links and build the site before changing published documentation.
