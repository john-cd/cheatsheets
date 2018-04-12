---
title: Debug Kubernetes
tags: Kubernetes MiniKube Kubectl
---

### Run a test Docker container

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

### Run a test K8s pod

```shell
kubectl run <deployment name> --image=<docker image>:<tag>
```

Useful options:
- ``--restart=Never`` 
- if the pod has a console: ``-i --tty  --command -- bash``


- Attach to the (first) container in the Pod: 

```shell
kubectl attach <pod name> -i -t
```

If there are multiple containers in the pod, use: ``-c <container name>``

- Get a shell to a running Container:

```shell
kubectl exec -it <pod name> -- bash
```

- Delete test pod:

```shell
kubectl delete pod <pod name>
```