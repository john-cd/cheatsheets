# syntax=docker/dockerfile:1
# Dockerfile build inputs are required and supplied by Compose from tracked .devcontainer/.env.
# From the repo root pass --env-file .devcontainer/.env and add --env-file .devcontainer/.env.local when present.
# Dockerfile build inputs for cheatsheets.
# TODO Reviewed ??-??-2026


# Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

ARG WORK_DIR

ARG PYTHON_VERSION
ARG UV_VERSION
ARG JUST_VERSION

FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv
FROM ghcr.io/casey/just:${JUST_VERSION} AS just
FROM python:${PYTHON_VERSION}-slim AS base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

COPY --from=uv /uv /uvx /bin/
COPY --from=just /just /usr/local/bin/just

ARG WORK_DIR
WORKDIR $WORK_DIR

# Resolve the locked project environment outside the repository checkout.
COPY pyproject.toml uv.lock justfile ./
COPY scripts/env.just scripts/env.just
RUN just uv sync --locked

## -------------------------------------------------------------
FROM base AS dev

# Install additional OS packages.
# Install git
# Caching per https://docs.docker.com/build/cache/
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends git

ARG USERNAME
ARG USER_UID
ARG USER_GID

# Create a non-privileged user
# See https://docs.docker.com/go/dockerfile-user-best-practices/
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y --no-install-recommends sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && chown -R "${USERNAME}:${USERNAME}" /tmp/python-build /tmp/python-output

# Switch to the non-privileged user.
USER $USERNAME

# Create aliases
RUN <<EOF
  set -ex
  echo 'alias ll="ls -alF"' >> $HOME/.bashrc
  echo 'alias la="ls -A"' >> $HOME/.bashrc
  echo 'alias l="ls -CF"' >> $HOME/.bashrc
EOF

## Install Poetry, if required
## Change some Poetry settings to better deal with working in a container
# ARG WORK_DIR
# RUN --mount=type=cache,target=${WORK_DIR}/.cache \
#   uv tool install poetry \
#   && uv tool update-shell

## Run if necessary:
# poetry self update \
# && poetry config cache-dir "${WORK_DIR}/.cache" \
# && poetry config virtualenvs.in-project true \
# && poetry completions bash >> ~/.bash_completion \
# && poetry install

# `mkdocs serve` uses port 8000
# The EXPOSE instruction doesn't actually publish the port. See compose.override.yaml
EXPOSE 8000

CMD while sleep 1000; do :; done

## -------------------------------------------------------------
FROM base AS ci

# Copy the source code into the container.
COPY . .

ARG WORK_DIR
RUN just uv run mkdocs build

#CMD [ "ci.sh" ]
