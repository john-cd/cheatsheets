# Shared Python environment configuration, imported by each Python project's justfile.
set shell := ["bash", "-uc"]
set windows-shell := ["C:/Program Files/Git/bin/bash.exe", "-uc"]

py_repo_root := parent_directory(source_directory())
py_main_repo := if file_name(parent_directory(py_repo_root)) == ".worktrees" { parent_directory(parent_directory(py_repo_root)) } else { py_repo_root }
py_repo_name := file_name(py_main_repo)
py_raw_slot := if file_name(parent_directory(py_repo_root)) == ".worktrees" { file_name(py_repo_root) } else { "main" }
py_slot := if py_raw_slot =~ '^(main|[a-j])$' { py_raw_slot } else { error("Invalid Python worktree slot: " + py_raw_slot) }
py_project_dir := join(py_repo_root, py_project_path)
py_project_key := if py_project_path == "." { join(py_repo_name, py_slot) } else { join(py_repo_name, py_project_path, py_slot) }
py_environment_key := if py_environment_project == "." { join(py_repo_name, py_slot) } else { join(py_repo_name, py_environment_project, py_slot) }

export CODE_REPOS_ROOT := env("CODE_REPOS_ROOT", if os() == "windows" { "D:/code" } else { join(home_directory(), "code") })
export CODE_TEMP_ROOT := env("CODE_TEMP_ROOT", if os() == "windows" { if path_exists("D:/temp") == "true" { "D:/temp" } else { "C:/temp" } } else { env("TMPDIR", "/tmp") })
export CODE_PACKAGES_ROOT := env("CODE_PACKAGES_ROOT", if os() == "windows" { "D:/packages" } else { join(home_directory(), ".local/share") })
export CODE_TOOLS_ROOT := env("CODE_TOOLS_ROOT", if os() == "windows" { "C:/tools" } else { join(home_directory(), ".local/tools") })
export CODE_PYTHON_ENV_ROOT := env("CODE_PYTHON_ENV_ROOT", join(CODE_PACKAGES_ROOT, "uv/environments"))
export CODE_PYTHON_BUILD_ROOT := env("CODE_PYTHON_BUILD_ROOT", join(CODE_TEMP_ROOT, "python-build"))
export CODE_PYTHON_OUTPUT_ROOT := env("CODE_PYTHON_OUTPUT_ROOT", join(CODE_TEMP_ROOT, "python-output"))
export CODE_PYTHON_BUILD_DIR := replace(join(CODE_PYTHON_BUILD_ROOT, py_project_key), "\\", "/")
export CODE_PYTHON_OUTPUT_DIR := replace(join(CODE_PYTHON_OUTPUT_ROOT, py_project_key), "\\", "/")
export UV_PROJECT_ENVIRONMENT := replace(join(CODE_PYTHON_ENV_ROOT, py_environment_key), "\\", "/")
export UV_CACHE_DIR := replace(join(CODE_PACKAGES_ROOT, "uv/cache"), "\\", "/")
export UV_PYTHON_INSTALL_DIR := replace(join(CODE_TOOLS_ROOT, "uv/python"), "\\", "/")
export UV_TOOL_DIR := replace(join(CODE_TOOLS_ROOT, "uv/tools"), "\\", "/")
export UV_TOOL_BIN_DIR := replace(join(CODE_TOOLS_ROOT, "uv/bin"), "\\", "/")
export UV_LINK_MODE := "copy"
export PIP_CACHE_DIR := replace(join(CODE_PACKAGES_ROOT, "pip"), "\\", "/")
export PREK_HOME := replace(join(CODE_PACKAGES_ROOT, "prek"), "\\", "/")
export PYTHONPYCACHEPREFIX := CODE_PYTHON_BUILD_DIR + "/pycache"
export RUFF_CACHE_DIR := CODE_PYTHON_BUILD_DIR + "/ruff"
export PYTEST_ADDOPTS := trim(env("PYTEST_ADDOPTS", "") + ' -o "cache_dir=' + CODE_PYTHON_BUILD_DIR + '/pytest"')
export MKDOCS_SITE_DIR := CODE_PYTHON_OUTPUT_DIR + "/site"
export PATH := UV_TOOL_BIN_DIR + (if os() == "windows" { ";" } else { ":" }) + env("PATH")
export TEMP := if os() == "windows" { CODE_TEMP_ROOT } else { env("TEMP", "/tmp") }
export TMP := if os() == "windows" { CODE_TEMP_ROOT } else { env("TMP", "/tmp") }
export TMPDIR := if os() == "windows" { CODE_TEMP_ROOT } else { env("TMPDIR", "/tmp") }

# Create only the external directories needed by tools.
_python-prepare:
    @mkdir -p {{quote(CODE_PYTHON_BUILD_DIR)}} {{quote(CODE_PYTHON_OUTPUT_DIR)}} {{quote(CODE_TEMP_ROOT)}}

# Synchronize the committed dependency lockfile.
sync: _python-prepare
    uv --directory {{quote(py_project_dir)}} sync --locked

# Forward uv arguments without losing argument boundaries; keep build outputs external.
[positional-arguments]
uv +args: _python-prepare
    @args=("$@"); \
        if [[ $1 == build ]]; then \
            explicit_output=false; \
            for arg in "$@"; do \
                case "$arg" in -o|--out-dir|--out-dir=*|-o?*) explicit_output=true ;; esac; \
            done; \
            if [[ $explicit_output == false ]]; then \
                args+=(--out-dir {{quote(CODE_PYTHON_OUTPUT_DIR + "/dist")}}); \
            fi; \
        fi; \
        uv --directory {{quote(py_project_dir)}} "${args[@]}"

# Run an application or tool in the locked project environment.
[positional-arguments]
run +args: _python-prepare
    uv --directory {{quote(py_project_dir)}} run --locked "$@"

# Run repository hooks from the Git repository root.
[positional-arguments]
prek +args: _python-prepare
    cd {{quote(py_repo_root)}} && prek "$@"

hooks-install: _python-prepare
    cd {{quote(py_repo_root)}} && prek install

hooks: _python-prepare
    cd {{quote(py_repo_root)}} && prek run --all-files

# Display the selected project and the environment exported to child processes.
env:
    @printf 'WORKTREE_DIR=%s\nWORKTREE_SLOT=%s\nPYTHON_PROJECT_DIR=%s\n' {{quote(py_repo_root)}} {{quote(py_slot)}} {{quote(py_project_dir)}}
    @printf 'CODE_REPOS_ROOT=%s\n' {{quote(CODE_REPOS_ROOT)}}
    @printf 'CODE_TEMP_ROOT=%s\n' {{quote(CODE_TEMP_ROOT)}}
    @printf 'CODE_PACKAGES_ROOT=%s\n' {{quote(CODE_PACKAGES_ROOT)}}
    @printf 'CODE_TOOLS_ROOT=%s\n' {{quote(CODE_TOOLS_ROOT)}}
    @printf 'CODE_PYTHON_ENV_ROOT=%s\n' {{quote(CODE_PYTHON_ENV_ROOT)}}
    @printf 'CODE_PYTHON_BUILD_ROOT=%s\n' {{quote(CODE_PYTHON_BUILD_ROOT)}}
    @printf 'CODE_PYTHON_OUTPUT_ROOT=%s\n' {{quote(CODE_PYTHON_OUTPUT_ROOT)}}
    @printf 'CODE_PYTHON_BUILD_DIR=%s\n' {{quote(CODE_PYTHON_BUILD_DIR)}}
    @printf 'CODE_PYTHON_OUTPUT_DIR=%s\n' {{quote(CODE_PYTHON_OUTPUT_DIR)}}
    @printf 'UV_PROJECT_ENVIRONMENT=%s\n' {{quote(UV_PROJECT_ENVIRONMENT)}}
    @printf 'UV_CACHE_DIR=%s\n' {{quote(UV_CACHE_DIR)}}
    @printf 'UV_PYTHON_INSTALL_DIR=%s\n' {{quote(UV_PYTHON_INSTALL_DIR)}}
    @printf 'UV_TOOL_DIR=%s\n' {{quote(UV_TOOL_DIR)}}
    @printf 'UV_TOOL_BIN_DIR=%s\n' {{quote(UV_TOOL_BIN_DIR)}}
    @printf 'UV_LINK_MODE=%s\n' {{quote(UV_LINK_MODE)}}
    @printf 'PIP_CACHE_DIR=%s\n' {{quote(PIP_CACHE_DIR)}}
    @printf 'PREK_HOME=%s\n' {{quote(PREK_HOME)}}
    @printf 'PYTHONPYCACHEPREFIX=%s\n' {{quote(PYTHONPYCACHEPREFIX)}}
    @printf 'RUFF_CACHE_DIR=%s\n' {{quote(RUFF_CACHE_DIR)}}
    @printf 'PYTEST_ADDOPTS=%s\n' {{quote(PYTEST_ADDOPTS)}}
    @printf 'MKDOCS_SITE_DIR=%s\n' {{quote(MKDOCS_SITE_DIR)}}
    @printf 'TEMP=%s\n' {{quote(TEMP)}}
    @printf 'TMP=%s\n' {{quote(TMP)}}
    @printf 'TMPDIR=%s\n' {{quote(TMPDIR)}}
