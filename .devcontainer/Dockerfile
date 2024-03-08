# syntax=docker/dockerfile:1

# Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

ARG WORK_DIR="/code"

ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

RUN pip install mkdocs \
    && pip install mkdocs-material
## https://github.com/byrnereese/mkdocs-minify-plugin
#RUN pip install mkdocs-minify-plugin
## https://github.com/mkdocs/mkdocs-redirects
#RUN pip install mkdocs-redirects

ARG WORK_DIR
WORKDIR $WORK_DIR

## -------------------------------------------------------------
FROM base AS dev

# Install additional OS packages.
# Install pix
# Caching per https://docs.docker.com/build/cache/
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends git pipx

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create a non-privileged user
# See https://docs.docker.com/go/dockerfile-user-best-practices/
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

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
#   pipx install poetry \
#   && pipx ensurepath

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
RUN rm -rf $WORK_DIR/site/ && mkdocs build

#CMD [ "ci.sh" ]
