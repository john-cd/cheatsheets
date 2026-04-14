---
title: Helm Chart Creation
tags: Kubernetes MiniKube Kubectl
---

# Helm Chart Creation

## Links

- [Helm Charts Documentation](https://helm.sh/docs/topics/charts/)
- [How to create your first Helm chart](https://docs.bitnami.com/kubernetes/how-to/create-your-first-helm-chart/)

## Steps

To create a new Helm chart, use the built-in command. This will generate a scaffold directory with the required Helm 3 structure.

```shell
# Create a new chart directory with the default scaffold.
helm create <chart-name>

# Lint the chart to ensure it follows best practices and has valid formatting.
helm lint <chart-name>

# Render the templates locally without installing them to verify the output.
helm install <release-name> <chart-name> --dry-run --debug
```

## Create dependencies between charts

Create ``requirements.yaml``

Add a remote repo

```shell
./helm repo add stable https://kubernetes-charts.storage.googleapis.com
```

and, from the chart directory, run:

```bash
../helm dependency update
```
