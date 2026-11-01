# Worktrees

Updated 2026-10-31 (America/Los_Angeles). This file describes the managed layout;
use `git worktree list --porcelain` and `git status --short` for live state.

- The primary checkout stays on `develop` and uses cache slot `main`.
- `main` is an independent empty root commit, with no development history.
- Auxiliary checkouts must be direct children of `.worktrees/`, named with one
  lowercase letter: a through j only. Reuse clean slots and preserve their caches.
- Before moving a detached checkout, preserve its unique commits on a named
  branch and push that branch. Dirty work must be committed before switching.
- Squash related unpublished commits, rebase or fast-forward to synchronize
  `develop`, and never introduce synchronization merge commits.
- Keep backup branches until their unique commits are integrated or deliberately
  retired. Delete ordinary topic branches only after verifying they are merged.

## Storage roots

Override the `CODE_*_ROOT` environment variables before invoking tooling.
Windows defaults are `CODE_REPOS_ROOT=D:/code`,
`CODE_TEMP_ROOT=D:/temp` (`C:/temp` fallback),
`CODE_PACKAGES_ROOT=D:/packages`, and `CODE_TOOLS_ROOT=C:/tools`.
Unix uses native home/cache/temp directories. Root overrides do not move existing
installations or rewrite independent package-manager settings.

## Python

Use each Python project's `justfile`; its imported `scripts/env.just` configures
the environment directly. Run `just --justfile <project>/justfile env` to inspect
it. `CODE_PYTHON_ENV_ROOT`, `CODE_PYTHON_BUILD_ROOT`, and
`CODE_PYTHON_OUTPUT_ROOT` select external per-project/per-worktree locations.
See the README for this repository's project paths and commands.
