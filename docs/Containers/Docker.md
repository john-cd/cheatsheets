---
title: Docker Cheatsheet
category: devops
---

# Docker Cheatsheet

## Useful Links

[Docker Cheat Sheet](https://github.com/wsargent/docker-cheat-sheet)

[Docker Documentation](https://docs.docker.com/)

[Docker Tutorials and Labs](https://github.com/docker/labs)

[Docker + Jenkins](https://www.toptal.com/java/java-continuous-integration-setup-tutorial) (Update Note: Link unreachable)

[Docker Hub](https://hub.docker.com/)

## Concepts

A Docker image is a read-only template. For example, an image could contain an Ubuntu operating system with Apache and your web application installed. Images are used to create Docker containers. Docker provides a simple way to build new images or update existing images, or you can download Docker images that other people have already created. Docker images are the buildcomponent of Docker.

Docker registries hold images. For orchestration, see [Kubernetes Concepts](Kubernetes_Concepts.md).

## Cheatsheet

To show only running containers, use the following command.

```bash
docker ps
```

To show all containers, use the following command.

```bash
docker ps -a
```

To show the last started container, use the following command.

```bash
docker ps -l
```

To download an image from Docker Hub, use the `docker pull` command.

```bash
docker pull centos
```

Create then start a container: `docker run [OPTIONS] IMAGE [COMMAND] [ARG...]`
    * [Docker run reference](https://docs.docker.com/engine/reference/run/)

```bash
docker run hello-world
```

Run with interactive terminal (i = interactive t = terminal):

```bash
docker run -it ubuntu bash
```

Start then detach the container (daemonize):

```bash
docker run -d -p8088:80 --name webserver nginx
```

If you want a transient container, `docker run --rm` will remove the container after it stops.

To look inside the container, use the logs command. You can also use `-f` to act like `tail -f`.

```bash
docker logs <container name>
```

Stop container:

```bash
docker stop <container name>   # Container ID or name.
```

Delete container:

```bash
docker rm <container name>
```

To check the environment:

```bash
docker run -it alpine env
```

Docker version / info:

```bash
docker version
docker info
```

## Port Mapping

``-p 80:5000``  would map port 80 on our local host to port 5000 inside our container.

```bash
docker run -d -p 80:5000 training/webapp python app.py
```

Full format: ip:hostPort:containerPort | ip::containerPort | hostPort:containerPort | containerPort

```bash
docker run -d -p 127.0.0.1:80:5000 training/webapp python app.py
```

Both hostPort and containerPort can be specified as a range of ports. When specifying ranges for both, the number of container ports in the range must match the number of host ports in the range, for example: ``-p1234-1236:1234-1236/tcp``

The ``-P`` flag tells Docker to map any required network ports inside our container to our host (using random ports).

```bash
docker run -d -P training/webapp python app.py
```

## Linking

``--link <name or id>:alias`` where *name* is the name of the container we’re linking to and *alias* is an alias for the link name.
The ``--link`` flag also takes the form: ``--link <name or id>``

```bash
docker run -d --name myES -p 9200:9200 -p 9300:9300 elasticsearch
docker run --name myK --link myES:elasticsearch  -p 5601:5601 -d docker-kibana-sense
```

## Networks

```bash
docker network ls
```

Find out the container’s IP address:

```bash
docker network inspect bridge
```

## Data Volumes

Create a new volume inside a container at /webapp:

```bash
docker run -d -P --name web -v /webapp training/webapp python app.py
docker inspect web
```

You can also use the VOLUME instruction in a Dockerfile to add one or more new volumes to any container created from that image.

Mount the host directory, ``/src/webapp``, into the container at ``/opt/webapp``.

```bash
docker run -d -P --name web -v /src/webapp:/opt/webapp training/webapp python app.py
```

On Windows, use:  ``docker run -v /c/Users/<path>:/<container path> ...``

## Example Dockerfile

```bash
vim Dockerfile
```

```docker
FROM docker/whalesay:latest
RUN apt-get -y update && apt-get install -y fortunes
CMD /usr/games/fortune -a | cowsay
```

```bash
docker build -t docker-whale .
```

## Multi-stage Build Example

The following is a Dockerfile example showing a multi-stage build. Multi-stage builds are useful to optimize image sizes, separating the build environment from the runtime environment.

```dockerfile
# Build stage.
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN go build -o myapp .

# Final stage.
FROM alpine:latest
WORKDIR /root/
COPY --from=builder /app/myapp .
CMD ["./myapp"]
```

## Docker Compose Example

`compose.yaml` (or `compose.yaml`) to define and run multi-container applications:

```yaml
version: '3.8'

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - api

  api:
    build: ./api
    environment:
      - DB_HOST=db
      - DB_USER=postgres
    ports:
      - "5000:5000"

  db:
    image: postgres:16-alpine
    environment:
      - POSTGRES_PASSWORD=secret
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

Run compose:

```bash
docker compose up -d
docker compose down
```

## Docker Cleanup Commands

To remove all unused or dangling images, containers, volumes, and networks:

```bash
docker system prune -a --volumes
```

## Multi-architecture Builds

Use `buildx` to build for multiple architectures (e.g., AMD64 and ARM64):

```bash
docker buildx create --use
docker buildx build --platform linux/amd64,linux/arm64 -t myrepo/myimage:latest --push .
```
