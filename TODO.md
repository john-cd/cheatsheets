# TODO

## Plan for moving to Zola + Rust

1. **Install Zola:** Download via `brew install zola` or directly from the GitHub releases page.
2. **Initialize a new Zola site:** Run `zola init site` to create the project structure.
3. **Port configuration:** Translate the configuration from `mkdocs.yml` to `config.toml` in Zola.
4. **Migrate Content:** Move Markdown files from `docs/` to `content/` and update front matter for Zola compatibility.
5. **Theme Selection:** Find or create a suitable Zola theme (e.g., `zola-theme-book`).
6. **Update CI/CD:** Update GitHub Actions to use Zola for build and deployment.
