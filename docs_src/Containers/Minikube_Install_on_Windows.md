---
title: Minikube Install on Windows
tags: Kubernetes MiniKube Kubectl
---

## Install ``minikube`` on Windows

[Minikube]( https://kubernetes.io/docs/tasks/tools/install-minikube/ ) runs a single-node Kubernetes cluster inside a VM on your laptop for users looking to try out Kubernetes or develop with it day-to-day.

- For Windows, install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) or Hyper-V first.
- Minikube is distributed in binary form: [ GitHub Repo ]( https://github.com/kubernetes/minikube/releases ). Download the minikube-installer.exe file, and execute the installer. This should automatically add minikube.exe to your path with an uninstaller available as well.
- If needed, add ``C:\Program Files (x86)\Kubernetes\minikube`` or similar to the PATH (in ``System Settings`` > ``Environment Variables``)
- Test that minikube works:

```shell
$ minikube
```

More info at [Getting Started]( https://kubernetes.io/docs/getting-started-guides/minikube/ )


## Install ``kubectl``

Use a version of [kubectl]( https://kubernetes.io/docs/tasks/tools/install-kubectl/ ) that is the same version as your server or later. Using an older ``kubectl`` with a newer server might produce validation errors.

On Windows 10 (using Git Bash):

```shell
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.10.0/bin/windows/amd64/kubectl.exe
```

OR

[Install Choco]( https://chocolatey.org/install )

Then 

```shell
choco install kubernetes-cli
```

Run kubectl version to verify that the version you’ve installed is sufficiently up-to-date.

```shell
kubectl version
```

### Configure ``kubectl``

Configure ``kubectl`` to use a remote Kubernetes cluster

- If ``~/.kube`` config does not exist (it should have been created by ``minikube``), enter the following in Powershell: 

```shell
cd C:\users\<yourusername>
mkdir .kube
cd .kube
New-Item config -type file
```

- Edit the config file with a text editor of your choice.

- Check that ``kubectl`` is properly configured by getting the cluster state:

```shell
kubectl cluster-info
```

- Enable auto-completion (if you use Git Bash)

```shell
echo "source <(kubectl completion bash)" >> ~/.bashrc
```

- You must have appropriate permissions to list, create, edit and delete pods in your cluster: 

```shell
kubectl auth can-i list pods
kubectl auth can-i create pods
kubectl auth can-i edit pods
kubectl auth can-i delete pods
```

### Run ``kubectl`` from the Ubuntu on Windows command line 

If installed by ``choco``

```shell
export PATH=$PATH:/mnt/c/ProgramData/chocolatey/bin/kubectl

# then use: 
kubectl.exe
```


## Run ``minikube``

[Running Kubernetes Locally via Minikube]( https://kubernetes.io/docs/getting-started-guides/minikube/ )

- Install [curl]( https://curl.haxx.se/)

```shell
choco install curl
```

- Test curl

```shell
curl http://google.com 
```

- Start minikube

```shell
minikube start
```
- List hosts

```shell
kubectl get nodes
```

- Test by deploying a container (creates a deployment / pod automatically)

```shell
kubectl run hello-minikube --image=k8s.gcr.io/echoserver:1.4 --port=8080
```

- Provide a dynamic port to the container (creates a service automatically)

```shell
kubectl expose deployment hello-minikube --type=NodePort
``` 
 
We have now launched an echoserver pod but we have to wait until the pod is up before curling/accessing it via the exposed service.
To check whether the pod is up and running we can use the following:

```shell
kubectl get pod
```

Once the pod is running, curl it:

```shell
curl $(minikube service hello-minikube --url)
```

- Cleanup:

```shell
kubectl delete deployment hello-minikube
```

```shell
kubectl delete service hello-minikube
```

```shell
minikube stop
```

## Install [Helm]( https://helm.sh/ )

Helm is a package manager for Kubernetes. Download a binary release of the Helm client from [here]( https://github.com/kubernetes/helm/releases )

- Once you have Helm ready, you can initialize the local CLI and also install Tiller into your Kubernetes cluster in one step:

```shell
$ helm init
```

This will install Tiller (the helm server) into the current Kubernetes cluster (as listed in ``kubectl config current-context``).

- Install a test Helm chart, then clean up

```shell
helm repo update              # Make sure we get the latest list of charts
helm install stable/mysql
helm ls
helm status <release name>
helm delete <release name>
```
