# TODO Reviewed ??-??-2026

# Purpose: Run this Python project with its configured environment and external output directories.
# Usage: Run just --list from this directory to inspect the available recipes.

# Python tasks for cheatsheets.
import 'scripts/env.just'
# py_project_path is repository-relative and scopes source, cache, and output paths.
# py_environment_project selects the locked dependency environment; set it to a shared
# project key when sibling tools should reuse that project's virtual environment.

py_project_path := "."
py_environment_project := "."

# List the available project recipes.
default:
    @just --justfile {{quote(justfile())}} --list

# Format the project Python files with Ruff.
format: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked ruff format .

# Check Python formatting without changing files.
format-check: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked ruff format --check .

# Lint (no changes) the project Python files with Ruff.
lint-check: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked ruff check .

# Lint with autofix: apply Ruff fixes to the project Python files.
lint: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked ruff check --fix .

# Run the project Python tests with pytest.
test: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked python -m unittest discover -s tests -p "test_*.py"

# Build the MkDocs site in the configured external output directory.
docs: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked mkdocs build --site-dir {{quote(MKDOCS_SITE_DIR)}}

# Serve the MkDocs site locally with live reloading.
serve: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked mkdocs serve --site-dir {{quote(MKDOCS_SITE_DIR)}}

# Check Python formatting, lint the code, and run the tests.
check: format-check lint-check test

hooks-run:
    prek run

# Lint repository Markdown with the pinned markdownlint-cli2.
markdownlint *args='':
    npx --yes markdownlint-cli2@0.24.0 {{ args }}

# Format Markdown, JSON, TOML, and YAML with the repository dprint configuration.
format-docs:
    dprint fmt

# Check Markdown, JSON, TOML, and YAML formatting with the repository dprint configuration.
format-docs-check:
    dprint check

# Check external links; network failures are reported separately from broken destinations.
links *args='': _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked python scripts/check_links.py {{ args }}

# Run every local, offline quality gate.
check-all: check format-docs-check markdownlint

# Uniform task names (short aliases; old names kept as aliases).
alias f := format
alias fmt := format
alias fc := format-check
alias fmt-check := format-check
alias fa := format-all
alias l := lint
alias lf := lint
alias lint-fix := lint
alias lc := lint-check
alias la := lint-all
alias c := check
alias ca := check-all
alias p := prep
alias t := test
alias ta := test
alias test-all := test
alias d := docs
alias doc := docs
alias s := serve
alias hi := hooks-install
alias hr := hooks-run

# Format everything.
format-all: format format-docs

# Lint with autofix, then lint Markdown.
lint-all: lint markdownlint

# Run the local CI gates.
ci: check-all

# Before committing: format everything, lint with autofix, then run all checks.
prep: format-all lint check-all
