<!-- TODO Reviewed ??-??-2026 -->

# cheatsheets agent instructions

## Human review markers

- `TODO Reviewed ??-??-<year>` and `Reviewed <date>` comments are for human review only. Preserve existing markers verbatim during edits; do not remove them or treat them as software TODOs.
- When modifying a file that contains a `Reviewed <date>` marker without `TODO`, preserve that marker and add a separate `TODO Reviewed ??-??-<year>` comment to request fresh human review.

## Communication

- Keep answers concise, use American spelling, use Unix-style line endings.

## Python environments and output paths

- Keep auxiliary worktrees under `.worktrees/`, named with one lowercase letter from `a`, `b`, or `c`. Keep the main worktree on the configured integration branch.
- Keep Python environments, build caches, and generated outputs outside the repository. Use `CODE_PYTHON_ENV_ROOT`, `CODE_PYTHON_BUILD_ROOT`, and `CODE_PYTHON_OUTPUT_ROOT`; the Justfile assigns repository/project/worktree-specific subdirectories.
- Use the committed `uv.lock` and `.python-version`. Run Python commands through `just`: `env`, `uv sync --locked`, `uv run ...`, and `prek run --all-files`.
- Configure roots with `CODE_*_ROOT` variables. Windows defaults are `D:/code`, `D:/packages/uv/environments`, `D:/temp/python-build`, `D:/temp/python-output`, `D:/packages`, `C:/tools`, and `D:/temp` (falling back to `C:/temp`). Unix-like defaults use native home directories, XDG cache settings where applicable, and `TMPDIR` or `/tmp`.

## Machine storage roots

- On Windows, use `CODE_TEMP_ROOT` for temporary and staging files, setting `TEMP`, `TMP`, and `TMPDIR` as needed. Use `C:\temp` only when `CODE_TEMP_ROOT` is unavailable.
- Keep package-manager data, library caches, and package installations under `CODE_PACKAGES_ROOT`, including npm, NuGet, pip/uv, vcpkg, and similar data. Do not store standalone tool distributions there.
- Keep portable developer tools and SDKs under `CODE_TOOLS_ROOT`, in a named subdirectory per tool (for example NASM, Oracle Instant Client, Cap'n Proto, Flutter, Pandoc, Tectonic, and repository tool bundles). Update PATH and installer/config references when relocating a tool. Leave package-manager-managed tools in their managed roots unless replacing them with a portable installation.
- In WSL, keep temporary files on the distribution's configured temp paths. Keep package data in `CODE_PACKAGES_ROOT` (default `~/.local/share`) and portable tools in `CODE_TOOLS_ROOT` (default `~/.local/tools`); avoid Windows drive mounts for these roots unless a tool requires them.

## Portable storage-root configuration

The current Windows defaults below can be overridden per machine or shell with environment variables. Python projects use the project Justfile for uv environments, Python caches, and generated output paths.

- CODE_REPOS_ROOT: D:/code on Windows; ~/code by default on Unix.
- CODE_TEMP_ROOT: D:/temp on Windows, with C:/temp as a fallback where a script needs one; Unix uses the existing TMPDIR or /tmp.
- CODE_PACKAGES_ROOT: D:/packages on Windows; ~/.local/share by default on Unix.
- CODE_TOOLS_ROOT: C:/tools on Windows; ~/.local/tools by default on Unix.
- CODE_PYTHON_ENV_ROOT: D:/packages/uv/environments on Windows; ~/.local/share/uv/environments by default on Unix.
- CODE_PYTHON_BUILD_ROOT: D:/temp/python-build on Windows; TMPDIR-or-/tmp/python-build by default on Unix.
- CODE_PYTHON_OUTPUT_ROOT: D:/temp/python-output on Windows; TMPDIR-or-/tmp/python-output by default on Unix.

Windows drive paths elsewhere in this file are defaults. Set a root variable to relocate the corresponding directory. WSL must keep its distribution temp behavior and must not redirect temp variables to a Windows drive mount.

## Required repository storage and Git policy

- Keep the primary checkout on `develop`. Keep `main` as an independent empty root commit; do not merge development history into it.
- Auxiliary worktrees must be direct children of `.worktrees/` and use slots `a`, `b`, or `c` only. Never use task-named or external worktree paths.
- Preserve unique commits on named branches before moving a detached checkout. Keep history linear, squash unpublished related changes, and never rewrite published history without explicit authorization.
- Use `CODE_TEMP_ROOT` for Windows temp files: `D:/temp` when available, otherwise `C:/temp`. Unix uses its native `TMPDIR` or `/tmp`.
- Use `CODE_PACKAGES_ROOT` for package data (Windows `D:/packages`) and `CODE_TOOLS_ROOT` for portable tools (Windows `C:/tools`). Existing tool-specific environment overrides take precedence; changing a root does not move installed packages.

## Configuration consistency

Follow [CONFIGURATION.md](CONFIGURATION.md) when changing repository tooling. Use American
spelling and LF line endings; keep README, contributor instructions, and configuration comments
synchronized. Preserve documented platform, domain, and teaching-example exceptions.

## Branch and worktree reporting

- Whenever you change the active branch or worktree, immediately state the current branch name and worktree path in your next update.

## Required worktree workflow

- Keep the primary checkout (`main` worktree) on `develop`. Do task work in the primary checkout or in direct
  children of `.worktrees/` named `a`, `b`, or `c`. Never use task-named directories, other slots, or
  external locations. Reuse a clean, inactive permitted slot whenever possible.
- Before reusing a slot, inspect `git worktree list`, branch, status, ownership, and active build
  processes. Never reset, overwrite, move, or remove a dirty or active worktree. If no permitted slot is
  available, stop and ask; do not create another slot or custom path.

- For each issue or task, implement in its worktree, lint the changes, format the changed files, and
  make a focused commit. Keep the worktree clean; make a WIP commit if needed. Wait until the task is
  complete to integrate into `develop` linearly. Then lint and format the whole repository and commit
  integration fixes. Do not leave dirty worktrees.
- Detach a clean, unused worktree and retain its slot and build directory. Delete topic branches only
  after confirming they are fully merged; never delete `develop`.
- Always keep the primary checkout's build directory. Preserve build directories for slots `a`, `b`, and
  `c` when disk space allows. When disk space is low, inspect active worktrees and build processes; remove
  the oldest obsolete build directories first. Then clean task-owned temporary directories and obsolete
  `build`/`target` directories. Do not remove directories used by active checkouts or processes.
- Other OS or Docker validation is not a blocker gate; create a follow-up issue or task when that validation is unavailable.
