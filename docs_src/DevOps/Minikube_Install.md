---
title: Install Minikube
tags: Kubernetes MiniKube Kubectl
---

## [Install Minikube]( https://kubernetes.io/docs/tasks/tools/install-minikube/ )

Minikube runs a single-node Kubernetes cluster inside a VM on your laptop for users looking to try out Kubernetes or develop with it day-to-day.

- For Windows, install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) or Hyper-V first.
- Minikube is distributed in binary form: [ GitHub Repo ]( https://github.com/kubernetes/minikube/releases ). Download the minikube-installer.exe file, and execute the installer. This should automatically add minikube.exe to your path with an uninstaller available as well.
- If needed, add "C:\Program Files (x86)\Kubernetes\minikube" or similar to the PATH (in System Settings > Environment Variables)
- Test that minikube works

```shell
$ minikube
```

More info at [Getting Started]( https://kubernetes.io/docs/getting-started-guides/minikube/ )


## [Install kubectl]( https://kubernetes.io/docs/tasks/tools/install-kubectl/ )


- Install kubectl

Use a version of kubectl that is the same version as your server or later. Using an older kubectl with a newer server might produce validation errors.

On Windows 10:

```shell
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.10.0/bin/windows/amd64/kubectl.exe
```

OR

[Install Choco]( https://chocolatey.org/install )

then 

```shell
choco install kubernetes-cli
```

Run kubectl version to verify that the version you’ve installed is sufficiently up-to-date.

```shell
kubectl version
```

### Configure kubectl

Configure kubectl to use a remote Kubernetes cluster

- If .kube config does not exist (should be created by minikube): 

```shell
cd C:\users\yourusername
mkdir .kube
cd .kube
New-Item config -type file
```

- Edit the config file with a text editor of your choice.

- Check that kubectl is properly configured by getting the cluster state:

```shell
kubectl cluster-info
```

- Enable auto-completion

```shell
echo "source <(kubectl completion bash)" >> ~/.bashrc
```

- You must have appropriate permissions to list, create, edit and delete pods in your cluster. 
You can verify that you can list these resources by running kubectl auth can-i <list|create|edit|delete> pods.

```shell
kubectl auth can-i list pods
kubectl auth can-i create pods
kubectl auth can-i edit pods
kubectl auth can-i delete pods
```


## [Run Minikube]( https://kubernetes.io/docs/getting-started-guides/minikube/ )

- Install [curl]( https://curl.haxx.se/)

```shell
choco install curl

# Test
curl http://google.com 
```

```shell
$ minikube start

# List hosts
$ kubectl get nodes

# Test by deploying a container  (creates a deployment / pod automatically)
$ kubectl run hello-minikube --image=k8s.gcr.io/echoserver:1.4 --port=8080

# Provide a dynamic port to the container (creates a service)
$ kubectl expose deployment hello-minikube --type=NodePort
 
# We have now launched an echoserver pod but we have to wait until the pod is up before curling/accessing it
# via the exposed service.
# To check whether the pod is up and running we can use the following:

$ kubectl get pod

# We can see that the pod is now Running and we will now be able to curl it:
$ curl $(minikube service hello-minikube --url)

$ kubectl delete deployment hello-minikube

$ kubectl delete service hello-minikube

$ minikube stop
```

## Install [Helm]( https://helm.sh/ )

Helm is a package manager for Kubernetes

Download a binary release of the Helm client from [here]( https://github.com/kubernetes/helm/releases )

Once you have Helm ready, you can initialize the local CLI and also install Tiller into your Kubernetes cluster in one step:

```shell
$ helm init
```

This will install Tiller (the helm server) into the Kubernetes cluster you saw with kubectl config current-context.

Install a test Helm chart

```shell
helm repo update              # Make sure we get the latest list of charts
helm install stable/mysql
helm ls
helm status <release name>
helm delete <release name>
```

## Kubernetes Concepts

- Pods - This is the basic unit for all of the workloads you run on Kubernetes. These workloads, such as Deployments and Jobs, are composed of one or more Pods.
A Pod is a Kubernetes abstraction that represents a group of one or more application containers (such as Docker or rkt), and some shared resources for those containers. Those resources include:

Shared storage, as Volumes
Networking, as a unique cluster IP address
Information about how to run each container, such as the container image version or specific ports to use

- Nodes: A Pod always runs on a Node. A Node is a worker machine in Kubernetes and may be either a virtual or a physical machine, depending on the cluster. Each Node is managed by the Master. A Node can have multiple pods, and the Kubernetes master automatically handles scheduling the pods across the Nodes in the cluster. 

- Deployment - The most common way of running X copies (Pods) of your application. Supports rolling updates to your container images.

- Service - By itself, a Deployment can’t receive traffic. Setting up a Service is one of the simplest ways to configure a Deployment to receive and loadbalance requests. Depending on the type of Service used, these requests can come from external client apps or be limited to apps within the same cluster. A Service is tied to a specific Deployment using label selection.

- Labels - Identifying metadata that you can use to sort and select sets of API objects. Labels have many applications, including the following:

* To keep the right number of replicas (Pods) running in a Deployment. The specified label is used to stamp the Deployment’s newly created Pods (as the value of the spec.template.labels configuration field), and to query which Pods it already manages (as the value of spec.selector.matchLabels).
* To tie a Service to a Deployment using the selector field.
* To look for specific subset of Kubernetes objects, when you are using kubectl. For instance, the command kubectl get deployments --selector=app=nginx only displays Deployments from the nginx app.


## Minikube / kubectl command examples

- To access the Kubernetes Dashboard, run this command in a shell after starting Minikube to get the address:

```shell
minikube dashboard
```

- The minikube VM is exposed to the host system via a host-only IP address, that can be obtained with the ``minikube ip`` command

- Deploy

```shell
kubectl run hello-world --replicas=2 --labels="run=load-balancer-example" --image=gcr.io/google-samples/node-hello:1.0  --port=8080
```

- ``kubectl get`` - list resources. ``kubectl get deployment`` to get all deployments; ``kubectl get pods -l app=nginx`` to get pods with label "app: nginx"

- ``kubectl describe`` - show detailed information about a resource
- ``kubectl logs`` - print the logs from a container in a pod
- ``kubectl exec`` - execute a command on a container in a pod


### Reusing the Docker daemon

When using a single VM of Kubernetes, it’s really handy to reuse the minikube’s built-in Docker daemon; as this means you don’t have to build a docker registry on your host machine and push the image into it - you can just build inside the same docker daemon as minikube which speeds up local experiments. Just make sure you tag your Docker image with something other than ‘latest’ and use that tag while you pull the image. Otherwise, if you do not specify version of your image, it will be assumed as :latest, with pull image policy of Always correspondingly, which may eventually result in ErrImagePull as you may not have any versions of your Docker image out there in the default docker registry (usually DockerHub) yet.

To be able to work with the docker daemon on your mac/linux host use the docker-env command in your shell:

```shell
eval $(minikube docker-env)
docker ps
```

A Docker client is required to publish built docker images to the Docker daemon running inside of minikube. 
See [installing Docker]( https://docs.docker.com/install/ ) for instructions for your platform.
