# cheatsheets agent instructions

## Central build outputs and worktrees

- Keep auxiliary Git worktrees under .worktrees/ and name them with one lowercase letter from a through j. A through j are reserved here.
- Keep the main worktree on this repository’s configured integration branch (usually `develop`; use `main` or `master` when that is the configured integration branch). Keep topic branches in auxiliary worktrees.
- Windows: target outputs go to D:/target/cheatsheets/slot and intermediate build outputs go to C:/code_build/cheatsheets/slot. C: is NTFS; D: is ReFS.
- Linux/macOS: target outputs go to the XDG cache folder (or ~/.cache) under cargo-target/cheatsheets/<slot>; intermediate outputs go under cargo-build/cheatsheets/<slot>.
- This repository has no Cargo workspace, so it has no Cargo target directory or sccache base directory.
- No Cargo workspace or sccache configuration is present.
- sccache base directories: not applicable.
