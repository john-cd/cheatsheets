---
title: Spark on Kubernetes
tags: Kubernetes MiniKube Kubectl Spark
---

# Spark on Kubernetes


## Running Spark on Kubernetes

[Official Documentation](https://spark.apache.org/docs/latest/running-on-kubernetes.html)

Prerequisites:

- A runnable distribution of Spark 3.x or 4.x.
- A running Kubernetes cluster at version >= 1.20 with access configured via `kubectl`.
- For local testing, use `minikube` or `kind`.
- Appropriate RBAC permissions to create, edit, and delete pods, services, and configmaps.

### Steps for Native Submission

- Check Kubernetes version: `kubectl version`.
- Ensure DNS is working (CoreDNS).
- Start `minikube` with sufficient resources:

```shell
minikube start --cpus 4 --memory 8192
```

- Submit a Spark job using `spark-submit`:

```shell
$ bin/spark-submit \
    --master k8s://https://<k8s-apiserver-host>:<k8s-apiserver-port> \
    --deploy-mode cluster \
    --name spark-pi \
    --class org.apache.spark.examples.SparkPi \
    --conf spark.executor.instances=3 \
    --conf spark.kubernetes.container.image=apache/spark:3.5.0 \
    local:///opt/spark/examples/jars/spark-examples_2.12-3.5.0.jar
```

Use `kubectl cluster-info` to get the K8s API server URL.

- Access logs:

```shell
kubectl -n <namespace> logs -f <driver-pod-name>
```

- Accessing Driver UI:

```shell
kubectl port-forward <driver-pod-name> 4040:4040
```

Then go to [https://localhost:4040](https://localhost:4040)

## Alternatives: Spark Kubernetes Operator

The recommended, declarative way to run Spark on Kubernetes is using the Spark Operator. It uses Custom Resource Definitions (CRDs) to manage the lifecycle of Spark applications.

[Spark Kubernetes Operator (Google Cloud Platform)](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator)

### Installation via Helm 3

```shell
helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator
helm install my-release spark-operator/spark-operator --namespace spark-operator --create-namespace
```

### Example CRD (SparkApplication)

```yaml
apiVersion: "sparkoperator.k8s.io/v1beta2"
kind: SparkApplication
metadata:
  name: spark-pi
  namespace: default
spec:
  type: Scala
  mode: cluster
  image: "apache/spark:3.5.0"
  imagePullPolicy: Always
  mainClass: org.apache.spark.examples.SparkPi
  mainApplicationFile: "local:///opt/spark/examples/jars/spark-examples_2.12-3.5.0.jar"
  sparkVersion: "3.5.0"
  driver:
    cores: 1
    coreLimit: "1200m"
    memory: "512m"
    labels:
      version: 3.5.0
    serviceAccount: spark
  executor:
    cores: 1
    instances: 1
    memory: "512m"
    labels:
      version: 3.5.0
```

Deploy the application:

```shell
kubectl apply -f spark-pi.yaml
```
