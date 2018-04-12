---
title: Kubernetes Cheatsheet
tags: Kubernetes MiniKube Kubectl
---

### ``minikube``

- To access the Kubernetes Dashboard, run this command in a shell after starting Minikube to get the address:

```shell
minikube dashboard
```

- The minikube VM is exposed to the host system via a host-only IP address, that can be obtained with the ``minikube ip`` command

### ``kubectl``

[kubectl Cheat Sheet]( https://kubernetes.io/docs/reference/kubectl/cheatsheet/ )

- Run a particular image on the cluster (creates a deployment automatically)

```shell
kubectl run hello-world --replicas=2 --labels="run=load-balancer-example" --image=gcr.io/google-samples/node-hello:1.0  --port=8080
```

- ``kubectl get`` - list resources.
    - ``kubectl get deployment`` to get all deployments
	- ``kubectl get pods -l app=nginx`` to get pods with label "app: nginx"
- ``kubectl describe`` - show detailed information about a resource
- ``kubectl logs`` - print the logs from a container in a pod
- ``kubectl exec`` - execute a command on a container in a pod


### Using the Docker daemon in the Minikube VM

When using a single VM of Kubernetes, it’s really handy to reuse the minikube’s built-in Docker daemon

```shell
eval $(minikube docker-env)
# test with 
docker ps
```

Just make sure you tag your Docker image with something other than ‘latest’ and use that tag while you pull the image. 
Otherwise, if you do not specify version of your image, it will be assumed as ``:latest``, with pull image policy of ``Always`` correspondingly, which may eventually result in ErrImagePull as you may not have any versions of your Docker image out there in the default docker registry (usually DockerHub) yet.

A Docker client is required to publish built docker images to the Docker daemon running inside of minikube. 
See [installing Docker]( https://docs.docker.com/install/ ) for instructions for your platform.



