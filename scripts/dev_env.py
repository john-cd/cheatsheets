#!/usr/bin/env python3
"""Run uv or prek with the repository's configurable external storage paths."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def _path(value: str | None, fallback: Path) -> Path:
    if not value:
        return fallback.expanduser().resolve()
    return Path(os.path.expandvars(value)).expanduser().resolve()


def _storage_roots() -> dict[str, Path]:
    home = Path.home()
    windows = os.name == "nt"
    if windows:
        temp_default = Path("D:/temp") if Path("D:/temp").exists() else Path("C:/temp")
        temp_root = _path(os.environ.get("CODE_TEMP_ROOT"), temp_default)
        defaults = {
            "CODE_REPOS_ROOT": Path("D:/code"),
            "CODE_TEMP_ROOT": temp_root,
            "CODE_PACKAGES_ROOT": Path("D:/packages"),
            "CODE_PYTHON_ENV_ROOT": Path("D:/packages/uv/environments"),
            "CODE_PYTHON_BUILD_ROOT": temp_root / "python-build",
            "CODE_PYTHON_OUTPUT_ROOT": temp_root / "python-output",
            "CODE_TOOLS_ROOT": Path("C:/tools"),
        }
    else:
        temp_default = Path(os.environ.get("TMPDIR") or "/tmp")
        temp_root = _path(os.environ.get("CODE_TEMP_ROOT"), temp_default)
        defaults = {
            "CODE_REPOS_ROOT": home / "code",
            "CODE_TEMP_ROOT": temp_root,
            "CODE_PACKAGES_ROOT": home / ".local/share",
            "CODE_PYTHON_ENV_ROOT": home / ".local/share/uv/environments",
            "CODE_PYTHON_BUILD_ROOT": temp_root / "python-build",
            "CODE_PYTHON_OUTPUT_ROOT": temp_root / "python-output",
            "CODE_TOOLS_ROOT": home / ".local/tools",
        }

    roots = {key: _path(os.environ.get(key), value) for key, value in defaults.items()}
    if not os.environ.get("CODE_PYTHON_ENV_ROOT"):
        roots["CODE_PYTHON_ENV_ROOT"] = (
            roots["CODE_PACKAGES_ROOT"] / "uv" / "environments"
        )
    return roots


def _checkout_identity() -> tuple[str, str]:
    if REPO_ROOT.parent.name == ".worktrees":
        slot = REPO_ROOT.name
        if slot not in set("abcdefghij"):
            raise SystemExit(
                f"Unsupported worktree slot {slot!r}; use one letter from a through j."
            )
        return REPO_ROOT.parent.parent.name, slot
    return REPO_ROOT.name, "main"


def _project_directory(raw: str | None) -> tuple[Path, tuple[str, ...]]:
    project_dir = (REPO_ROOT / (raw or ".")).resolve()
    try:
        relative = project_dir.relative_to(REPO_ROOT)
    except ValueError as error:
        raise SystemExit(
            "The Python project must be inside this repository."
        ) from error
    parts = () if str(relative) == "." else relative.parts
    return project_dir, parts


def _prepare_environment(
    project_parts: tuple[str, ...], slot: str
) -> tuple[dict[str, str], dict[str, Path]]:
    env = os.environ.copy()
    roots = _storage_roots()
    for key, value in roots.items():
        env[key] = str(value)

    repo_name, _ = _checkout_identity()
    project_key = (repo_name, *project_parts)
    build_dir = roots["CODE_PYTHON_BUILD_ROOT"].joinpath(*project_key, slot)
    output_dir = roots["CODE_PYTHON_OUTPUT_ROOT"].joinpath(*project_key, slot)
    package_root = roots["CODE_PACKAGES_ROOT"]
    tools_root = roots["CODE_TOOLS_ROOT"]
    python_env_root = roots["CODE_PYTHON_ENV_ROOT"]

    env["UV_CACHE_DIR"] = str(package_root / "uv" / "cache")
    env["UV_PYTHON_INSTALL_DIR"] = str(tools_root / "uv" / "python")
    env["UV_TOOL_DIR"] = str(tools_root / "uv" / "tools")
    env["UV_TOOL_BIN_DIR"] = str(tools_root / "uv" / "bin")
    env["UV_LINK_MODE"] = "copy"
    # Each repo, Python project, and worktree gets its own environment. This
    # overrides inherited values that might point into a checkout or collide.
    env["UV_PROJECT_ENVIRONMENT"] = str(python_env_root.joinpath(*project_key, slot))
    env["PIP_CACHE_DIR"] = str(package_root / "pip")
    env["PREK_HOME"] = str(package_root / "prek")

    tool_bin = str(_path(env.get("UV_TOOL_BIN_DIR"), tools_root / "uv" / "bin"))
    path_entries = env.get("PATH", "").split(os.pathsep)
    if not any(entry.casefold() == tool_bin.casefold() for entry in path_entries):
        env["PATH"] = os.pathsep.join([tool_bin, *path_entries])

    env["CODE_PYTHON_BUILD_DIR"] = str(build_dir)
    env["CODE_PYTHON_OUTPUT_DIR"] = str(output_dir)
    env["MKDOCS_SITE_DIR"] = str(output_dir / "site")
    env["PYTHONPYCACHEPREFIX"] = str(build_dir / "pycache")
    env["RUFF_CACHE_DIR"] = str(build_dir / "ruff")
    existing_pytest = env.get("PYTEST_ADDOPTS", "").strip()
    pytest_cache = f'-o "cache_dir={build_dir / "pytest"}"'
    if pytest_cache not in existing_pytest:
        env["PYTEST_ADDOPTS"] = f"{existing_pytest} {pytest_cache}".strip()

    if os.name == "nt":
        temp_dir = roots["CODE_TEMP_ROOT"]
        env["TEMP"] = str(temp_dir)
        env["TMP"] = str(temp_dir)
        env["TMPDIR"] = str(temp_dir)

    paths = {
        **roots,
        "PYTHON_BUILD_DIR": build_dir,
        "PYTHON_OUTPUT_DIR": output_dir,
        "UV_CACHE_DIR": Path(env["UV_CACHE_DIR"]),
        "UV_PROJECT_ENVIRONMENT": Path(env["UV_PROJECT_ENVIRONMENT"]),
        "UV_PYTHON_INSTALL_DIR": Path(env["UV_PYTHON_INSTALL_DIR"]),
        "UV_TOOL_DIR": Path(env["UV_TOOL_DIR"]),
        "UV_TOOL_BIN_DIR": Path(env["UV_TOOL_BIN_DIR"]),
        "PIP_CACHE_DIR": Path(env["PIP_CACHE_DIR"]),
        "PREK_HOME": Path(env["PREK_HOME"]),
    }
    return env, paths


def _route_outputs(args: list[str], output_dir: Path) -> list[str]:
    routed = list(args)
    if (
        routed
        and routed[0] == "build"
        and "--out-dir" not in routed
        and "-o" not in routed
    ):
        routed.extend(["--out-dir", str(output_dir / "dist")])
    return routed


def _show_environment(
    project_dir: Path, slot: str, env: dict[str, str], paths: dict[str, Path]
) -> int:
    print(f"WORKTREE_DIR={REPO_ROOT}")
    print(f"WORKTREE_SLOT={slot}")
    print(f"PYTHON_PROJECT_DIR={project_dir}")
    for key, value in paths.items():
        print(f"{key}={value}")
    for key in (
        "UV_PROJECT_ENVIRONMENT",
        "UV_CACHE_DIR",
        "UV_PYTHON_INSTALL_DIR",
        "UV_TOOL_DIR",
        "UV_TOOL_BIN_DIR",
        "UV_LINK_MODE",
        "PREK_HOME",
        "PIP_CACHE_DIR",
        "PYTHONPYCACHEPREFIX",
        "RUFF_CACHE_DIR",
        "CODE_PYTHON_BUILD_DIR",
        "CODE_PYTHON_OUTPUT_DIR",
        "MKDOCS_SITE_DIR",
        "TEMP",
        "TMP",
        "TMPDIR",
    ):
        print(f"{key}={env.get(key, '')}")
    return 0


def main() -> int:
    args = sys.argv[1:]
    project_arg = None
    if args[:1] == ["--project"]:
        if len(args) < 2:
            raise SystemExit(
                "Usage: dev_env.py [--project <path>] [env | uv <args...> | prek <args...>]"
            )
        project_arg, args = args[1], args[2:]

    project_dir, project_parts = _project_directory(project_arg)
    repo_name, slot = _checkout_identity()
    env, paths = _prepare_environment(project_parts, slot)

    if not args or args == ["env"]:
        return _show_environment(project_dir, slot, env, paths)

    program, command_args = (args[0], args[1:])
    if program not in {"uv", "prek"}:
        program, command_args = "uv", args
    uv_tool_command = program == "uv" and command_args[:1] == ["tool"]
    if (
        program == "uv"
        and not uv_tool_command
        and not (project_dir / "pyproject.toml").is_file()
    ):
        raise SystemExit(
            f"No pyproject.toml found at {project_dir}; pass --project <path>."
        )

    executable = shutil.which(program, path=env.get("PATH"))
    if executable is None:
        raise SystemExit(f"{program} is not installed or is not on PATH.")

    for key in ("PYTHON_BUILD_DIR", "PYTHON_OUTPUT_DIR", "CODE_TEMP_ROOT"):
        paths[key].mkdir(parents=True, exist_ok=True)
    command_args = _route_outputs(command_args, paths["PYTHON_OUTPUT_DIR"])
    return subprocess.run(
        [executable, *command_args], cwd=project_dir, env=env, check=False
    ).returncode


if __name__ == "__main__":
    raise SystemExit(main())
