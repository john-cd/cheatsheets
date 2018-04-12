---
title: Helm Chart Creation
tags: Kubernetes MiniKube Kubectl
---

## Links

[How to create your first Helm chart]( https://docs.bitnami.com/kubernetes/how-to/create-your-first-helm-chart/ )

## Steps

```shell
./helm create <folder containing chart>

./helm lint <folder>

./helm install --dry-run --debug <folder>
```

### To create dependencies between charts

Create ``requirements.yaml``

Add a remote repo

```shell
./helm repo add stable https://kubernetes-charts.storage.googleapis.com
```

and, from the chart directory, run:

```
../helm dependency update
```
