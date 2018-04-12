---
title: Minikube Install in Ubuntu on Windows
tags: Kubernetes MiniKube Kubectl
---

### Install ``kubectl`` in Ubuntu on Windows

```shell
cd ~
mkdir bin
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl
# optionally 
sudo mv ./kubectl /usr/local/bin/kubectl
# then test
kubectl get all
# enable autocompletion
source <(kubectl completion bash)
echo "source <(kubectl completion bash)" >> ~/.bashrc
```

- If necessary, install [socat]( https://www.cyberciti.biz/faq/linux-unix-tcp-port-forwarding/ )

```shell
sudo apt-get update && sudo apt-get install socat
```

- In order for kubectl to find and access a Kubernetes cluster, it needs a kubeconfig file, which is created automatically when you create a cluster using ``kube-up.sh`` or successfully deploy a Minikube cluster. 

Check that kubectl is properly configured by getting the cluster state:

```shell
kubectl cluster-info
```

Beware that you may have two different config files in ``~/.kube/`` and ``/mnt/c/Users/<user name>/.kube`` if you installed ``minikube`` in Windows.


