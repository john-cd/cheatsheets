---
title: Spark 2.3 on Kubernetes
tags: Kubernetes MiniKube Kubectl Spark
---

## Background

[Introduction to Spark on Kubernetes](https://banzaicloud.github.io/blog/spark-k8s/)


## Running Spark on Kubernetes

[Main Page]( https://spark.apache.org/docs/latest/running-on-kubernetes.html ) 

Prerequisites:

- A runnable distribution of Spark 2.3 or above.
- A running Kubernetes cluster at version >= 1.6 with access configured to it using kubectl. If you do not already have a working Kubernetes cluster, you may setup a test cluster on your local machine using minikube.
We recommend using the latest release of minikube with the DNS addon enabled.
- Be aware that the default minikube configuration is not enough for running Spark applications. We recommend 3 CPUs and 4g of memory to be able to start a simple Spark application with a single executor.
- You must have appropriate permissions to list, create, edit and delete pods in your cluster. You can verify that you can list these resources by running kubectl auth can-i <list|create|edit|delete> pods.
The service account credentials used by the driver pods must be allowed to create pods, services and configmaps.
- You must have Kubernetes DNS configured in your cluster.

###  Steps

- Need Kubernetes version 1.6 and above.
To check the version, enter ``kubectl version``.

- The cluster must be configured to use the kube-dns addon. Check with

```shell
minikube addons list
```

[Kubernetes DNS Page]( https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/ )


- Start minikube with the recommended configuration for Spark

```shell
minikube start --cpus 3 --memory 4096
```

- Submit a Spark job using: 

```shell
$ bin/spark-submit \
    --master k8s://https://<k8s-apiserver-host>:<k8s-apiserver-port> \
    --deploy-mode cluster \
    --name spark-pi \
    --class org.apache.spark.examples.SparkPi \
    --conf spark.executor.instances=3 \
    --conf spark.kubernetes.container.image=<spark-image> \
    local:///path/to/examples.jar
```

Use ``kubectl cluster-info`` to get the K8s API server URL

Spark (starting with version 2.3) ships with a Dockerfile in the ``kubernetes/dockerfiles/`` directory.

- Access logs:

```shell
$ kubectl -n=<namespace> logs -f <driver-pod-name>
```

- Accessing Driver UI:

```shell
$ kubectl port-forward <driver-pod-name> 4040:4040
```

Then go to [ http://localhost:4040 ]( http://localhost:4040 )


## Alternatives

[Helm Chart for Spark]( https://github.com/kubernetes/charts/tree/master/stable/spark )

[The same on KubeApps ]( https://hub.kubeapps.com/charts/stable/spark )

```shell
helm install --name my-spark-release --version 0.1.12 stable/spark
```
