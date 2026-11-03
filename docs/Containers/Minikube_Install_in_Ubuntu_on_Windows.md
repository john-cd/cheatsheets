---
title: Minikube Install in Ubuntu on Windows
tags: Kubernetes MiniKube Kubectl
---

<!-- TODO Reviewed ??-??-2026 -->

# Minikube Install in Ubuntu on Windows

## Install `kubectl` in Ubuntu on Windows

```shell
cd ~
mkdir bin
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl
# Optionally
sudo mv ./kubectl /usr/local/bin/kubectl
# Then test
kubectl get all
# Enable autocompletion
source <(kubectl completion bash)
echo "source <(kubectl completion bash)" >> ~/.bashrc
```

If necessary, install [socat](https://www.cyberciti.biz/faq/linux-unix-tcp-port-forwarding/)

```shell
sudo apt-get update && sudo apt-get install socat
```

In order for `kubectl` to find and access a Kubernetes cluster, it needs a `kubeconfig` file, which is created automatically when you create a cluster using `kube-up.sh` or successfully deploy a Minikube cluster.

Check that `kubectl` is properly configured by getting the cluster state:

```shell
kubectl cluster-info
```

Minikube installations in Windows and WSL keep separate configuration. Use the Linux-side configuration for WSL-native tools and keep it on the Linux filesystem.
