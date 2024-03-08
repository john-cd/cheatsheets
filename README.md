# Cheatsheets

[John's Cheatsheets](https://john-cd.com/cheatsheets/)

[John's Main Website](https://john-cd.com)

## Repo structure

This website is generated using [MkDocs](https://mkdocs.org) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

The source Markdown files are found in the `docs` folder. The resulting HTML / JS is found in `site`. There is also a `drafts` folder for Markdown files that are not ready for publication.

`.devcontainer` contains the [Dev Container](https://code.visualstudio.com/docs/devcontainers/containers) file and associated [Docker Compose](https://docs.docker.com/compose/) and [Dockerfile](https://docs.docker.com/reference/dockerfile/) setup. `github/workflows` contains the GitHub Action continuous deployment workflow.

## Contributing

### Install

If you use [Visual Studio Code](https://code.visualstudio.com/), install the [Dev Container extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). Otherwise, consider the [Dev Container CLI](https://containers.dev/supporting#devcontainer-cli). `Dev Container` allows you to edit and test the web site within a `Docker` container.

Alternatively, install the required tools on your development machine directly, including [Python](https://www.python.org/), []

```shell
python -m pip install mkdocs --user
python -m pip install mkdocs-material --user
```

### Basic MkDocs Commands

- ``mkdocs new [dir-name]`` - Create a new project.
- ``mkdocs serve`` - Start the live-reloading docs server.
- ``mkdocs build`` - Build the documentation site.
- ``mkdocs help`` - Print the help message.

Within a Dev Container, you may need to use `mkdocs serve --dev-addr 0.0.0.00:8000`.

### Docker Compose

To test the Docker Compose setup, try

```bash
docker compose -f .devcontainer/compose.yaml -f .devcontainer/compose.override.yaml up --build
docker compose down
```

and

```bash
docker compose -f .devcontainer/compose.yaml -f .devcontainer/compose-ci.yaml up --build
docker compose down
```

You may also build the image directly, e.g.: `docker build --file .devcontainer/Dockerfile --target dev --tag john-cd/cheatsheets:latest .`
To push an image to your registry, use `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/) docs for more detail on building and pushing.
