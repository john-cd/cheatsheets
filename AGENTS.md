# cheatsheets agent instructions

## Central build outputs and worktrees

- Keep auxiliary Git worktrees under .worktrees/ and name them with one lowercase letter from a through j. A through j are reserved here.
- Keep the main worktree on this repository’s configured integration branch (usually `develop`; use `main` or `master` when that is the configured integration branch). Keep topic branches in auxiliary worktrees.
- Windows: target outputs go to CODE_TARGET_ROOT/cheatsheets/<slot> and intermediate build outputs go to CODE_BUILD_ROOT/cheatsheets/slot. Keep CODE_BUILD_ROOT on an NTFS volume; do not use a ReFS volume for builds.
- Linux/macOS: target outputs go to the XDG cache folder (or ~/.cache) under cargo-target/cheatsheets/<slot>; intermediate outputs go under cargo-build/cheatsheets/<slot>.
- This repository has no Cargo workspace, so it has no Cargo target directory or sccache base directory.
- No Cargo workspace or sccache configuration is present.
- sccache base directories: not applicable.

## Machine storage roots

- On Windows, use `CODE_TEMP_ROOT` for temporary and staging files, setting `TEMP`, `TMP`, and `TMPDIR` as needed. Use `C:\temp` only when `CODE_TEMP_ROOT` is unavailable.
- Keep package-manager data, library caches, and package installations under `CODE_PACKAGES_ROOT`, including Cargo, npm, NuGet, pip/uv, vcpkg, and similar data. Do not store standalone tool distributions there.
- Keep portable developer tools and SDKs under `CODE_TOOLS_ROOT`, in a named subdirectory per tool (for example NASM, Oracle Instant Client, Cap'n Proto, Flutter, Pandoc, Tectonic, and repository tool bundles). Update PATH and installer/config references when relocating a tool. Leave package-manager-managed tools in their managed roots unless replacing them with a portable installation.
- In WSL, keep temporary files on the distribution's configured temp paths. Keep package data in `CODE_PACKAGES_ROOT` (default `~/.local/share`) and portable tools in `CODE_TOOLS_ROOT` (default `~/.local/tools`); avoid Windows drive mounts for these roots unless a tool requires them.

## Portable storage-root configuration

The current Windows defaults below can be overridden per machine or shell with environment variables. The per-repository Rust Justfile or Cargo Make helper, when present, reads these variables. Non-Rust repositories do not need a Cargo build runner; use the environment roots only for tools or scripts that consume them.

- CODE_REPOS_ROOT: D:/code on Windows; ~/code by default on Unix.
- CODE_BUILD_ROOT: C:/code_build on Windows; XDG cache or ~/.cache/cargo-build by default on Unix. Keep Windows build output on NTFS.
- CODE_TARGET_ROOT: D:/target on Windows; XDG cache or ~/.cache/cargo-target by default on Unix.
- CODE_SCCACHE_ROOT: D:/sccache on Windows; XDG cache or ~/.cache/sccache by default on Unix.
- CODE_TEMP_ROOT: D:/temp on Windows, with C:/temp as a fallback where a script needs one; Unix uses the existing TMPDIR or /tmp.
- CODE_PACKAGES_ROOT: D:/packages on Windows; ~/.local/share by default on Unix.
- CODE_TOOLS_ROOT: C:/tools on Windows; ~/.local/tools by default on Unix.

Windows drive paths elsewhere in this file are defaults. Set a root variable to relocate the corresponding directory. WSL must keep its distribution temp behavior and must not redirect temp variables to a Windows drive mount.
