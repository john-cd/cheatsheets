# Python tasks for cheatsheets.
import 'scripts/env.just'

py_project_path := "."
py_environment_project := "."

default:
    @just --justfile {{quote(justfile())}} --list

fmt: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked ruff format .

fmt-check: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked ruff format --check .

lint: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked ruff check .

test: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked python -m unittest discover -s tests -p "test_*.py"

docs: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked mkdocs build --site-dir {{quote(MKDOCS_SITE_DIR)}}

serve: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked mkdocs serve --site-dir {{quote(MKDOCS_SITE_DIR)}}

check: fmt-check lint test
