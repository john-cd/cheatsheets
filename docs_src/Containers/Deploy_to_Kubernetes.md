---
title: Deploy to Kubernetes
tags: Kubernetes MiniKube Kubectl
---

using ``kubectl``

### Create ConfigMap from config files

A [ConfigMap]( https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/ ) stores K8s-specific configuration that can be mounted as volume or used in env variables.
It is often used to provide production configuration: application configuration, log settings, etc...  

```shell
kubectl create configmap app-conf --from-file=<path to config files>  # create a ConfigMap from multiple files in the same directory.
```

- Check the ConfigMap

```bash
kubectl get configmap app-conf -o yaml

# or 

kubectl describe configmaps app-conf 
```

### Create a Kubernetes secret

You may need a Secret to store database passwords and secret keys. 

For applications using the [Play Framework]( https://www.playframework.com/ ), generate a secret using: 

```shell
secretText = $(sbt playGenerateSecret)
regex = "Generated new secret: (.+)$"
f [[ $secretText =~ $regex ]]
    then
        secret = "${BASH_REMATCH[1]}"
        echo $secret
		kubectl create secret generic application-secret --from-literal=application_secret=$secret
		kubectl get secrets
	else
        echo "$secretText doesn't match" >&2
    fi
done
```

### Create Resources (Deployment, Service, Ingress, etc...) 

```shell
kubectl create -f <path/to/resource_config.yaml>
```

- Verify proper resource creation

```shell
kubectl get ing
kubectl get service
kubectl get deployment
kubectl get pods
```

- To delete a resource later, in this case a Deployment:

```shell
kubectl delete deployment <deployment name>
```

### Install an Ingress Controller 

- An ingress controller is necessary to make Ingresses work. See the [Ingress doc]( https://kubernetes.io/docs/concepts/services-networking/ingress/ ) 

#### Minikube

- ``minikube`` provides its own ingress controller via the Ingress add-on:

```shell
minikube addons enable ingress
```

Enabling the add-on provisions the following:

- a configMap for the Nginx loadbalancer
- the Nginx ingress controller
- a service that exposes a default Nginx backend pod for handling unmapped requests.


#### Install the nginx ingress controller (non-minikube Kubernetes)

- Install via this [helm chart]( https://hub.kubeapps.com/charts/stable/nginx-ingress )

```shell
#./helm install stable/nginx-ingress
```

or with stat collection enabled for Prometheus

```shell
helm install --name nginx-ingress-release stable/nginx-ingress \
  --set controller.stats.enabled=true \
  --set controller.metrics.enabled=true
```
  
- Verify that the Ingress exists 

```shell
kubectl get ing
```

See [explanations]( https://daemonza.github.io/2017/02/13/kubernetes-nginx-ingress-controller/ ) and [ documentation ]( https://github.com/kubernetes/ingress-nginx )

The nginx ingress controller requires a 404-server like [this]( https://github.com/kubernetes/ingress-nginx/tree/master/images/404-server )


#### Alternative ingress controllers

- Install [https://traefik.io/]( https://traefik.io/ )