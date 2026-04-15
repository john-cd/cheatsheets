---
title: Debug Kubernetes
tags: Kubernetes MiniKube Kubectl
---

# Run a test Docker container

```shell
docker run --rm -p <port>:<port> <docker image>:<tag>
docker ps
# cleanup
docker kill <container>
```

To override the entrypoint, use:

```shell
winpty docker run --rm -p <port>:<port> -it --entrypoint bash <docker image>:<tag>
```

The above assumes you are using cygwin / git bash on Windows.

## Run a test K8s pod

```shell
kubectl run <deployment name> --image=<docker image>:<tag>
```

Useful options:

- `--restart=Never`

- if the pod has a console: `-i --tty  --command -- bash`

- Attach to the (first) container in the Pod:

```shell
kubectl attach <pod name> -i -t
```

If there are multiple containers in the pod, use: `-c <container name>`

- Get a shell to a running Container:

```shell
kubectl exec -it <pod name> -- bash
```

- Delete test pod:

```shell
kubectl delete pod <pod name>
```

## Ephemeral Debug Containers

Starting with Kubernetes 1.25, `kubectl debug` allows you to attach an ephemeral container to a running pod for troubleshooting, which is especially useful if the pod's image doesn't contain debugging utilities (like `bash` or `curl`).

```shell
# Add an interactive busybox container to a running pod
kubectl debug -it <pod_name> --image=busybox --target=<container_name>

# Debug a node by creating a privileged pod on it
kubectl debug node/<node_name> -it --image=ubuntu
```

## Useful Links

- [Official K8s Troubleshooting Guide](https://kubernetes.io/docs/tasks/debug/)
