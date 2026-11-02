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
fmt: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked ruff format .

# Check Python formatting without changing files.
fmt-check: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked ruff format --check .

# Lint the project Python files with Ruff.
lint: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked ruff check .

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
check: fmt-check lint test

hooks-run:
    prek run
