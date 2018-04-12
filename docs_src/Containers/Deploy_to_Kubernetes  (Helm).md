---
title: Deploy to Kubernetes (Helm)
tags: Kubernetes MiniKube Kubectl
---

## Useful Links

[Deploying scala sbt microservice to Kubernetes]( https://steveking.site/blog/2017/deploying-scala-sbt-microservices-to-kubernetes/ )

[SBT Native Packager - Docker]( https://sbt-native-packager.readthedocs.io/en/latest/formats/docker.html )

[OpenSSL]( https://www.openssl.org/ )

[Helm]( https://helm.sh/ )


## Deployment of a ``sbt``-built app on Kubernetes (MiniKube)

### Test packaging without Kubernetes first

- Stage all Play files in a local directory and verify

```shell
sbt stage 
```

- For direct deployment, create a distribution in ``target/universal``
 
```shell
sbt dist
```

The ``dist`` task builds a binary version of your application that you can deploy to a server without any dependency on SBT, the only thing the server needs is a Java installation.

### Deploy a Helm chart to Kubernetes

Prerequisites: ``minikube``, ``kubectl``, ``docker`` client and ``helm`` should be installed 

- Generate the Dockerfile and environment prepared for creating a Docker image

```shell
sbt docker:stage
```

- Verify the output under ``target/docker`` 

- Start ``minikube``

```shell
minikube start
```

- Enable Ingress

```shell
minikube addons list
minikube addons enable ingress
```

Also consider enabling ``heapster``

- List available nodes to verify that ``kubectl`` is properly configured

```shell
kubectl get nodes
```

It should return one node. 

- Connect the Docker client to the Docker daemon in the K8s VM

```shell
eval $(minikube docker-env)
```

Just make sure you tag your Docker image with something other than ‘latest’ and use that tag while you pull the image.
Otherwise, if you do not specify version of your image, it will be assumed as ``:latest``, with pull image policy of ``Always`` correspondingly, which may eventually result in ErrImagePull as you may not have any versions of your Docker image out there in the default docker registry (usually DockerHub) yet.

- If needed, remove previously built images from the local Docker server with ``sbt docker:clean`` or ``docker rmi <image>``. 
To view the list of Docker images, run ``docker images``

- Build the Docker image and publish it to Kubernetes' Docker server. 

```shell
sbt docker:publishLocal
```

- Deploy the Helm chart

``` shell
./helm install --dry-run --debug <helm chart folder> &> output.txt
```

and if that looks OK

``` shell
./helm install <helm chart folder>
```

or specify a release name:

```shell
./helm install --name <release name> <helm chart folder> 
```

- Verify the Helm deployment to ``minikube``

```shell
./helm list
./helm status <release name>
```

More details via:

```shell
kubectl get ing
kubectl get service
kubectl get deployment
kubectl get pods
```

- Test the deployment by forwarding a local port to a port on the pod

```shell
kubectl get pods
kubectl port-forward <pod name> 8080:<target port on pod> 
curl -v http://localhost:8080/api
```

``kubectl port-forward`` also allows using resource name, such as a service name, to select a matching pod to port forward to

```shell
kubectl port-forward svc/<service name>  8080:<service port> 
curl -v http://localhost:8080/
```

- When needed, delete the release with 

```shell
helm ls
helm delete <release name>
```

### If you want to deploy / not deploy an Ingress

- Update ``values.yaml`` in the Helm chart root folder

```yaml
ingress:
  enabled: true  # or: false; true by default
```

- If true, make sure the minikube Ingress add-on is enabled

```shell
minikube addons enable ingress
```

- Deploy on Kubernetes as above

See [Blog]( https://medium.com/@Oskarr3/setting-up-ingress-on-minikube-6ae825e98f82 )


### SSL Termination (TO DO)

[IBM Ingress TLS tutorial]( https://www.ibm.com/support/knowledgecenter/en/SS5PWC/front_end_tls_ingress_task.html )

- Generate a x509, pem encoded, RSA 2048 certificate with [OpenSSL]( https://www.openssl.org/ )

```shell
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ${KEY_FILE} -out ${CERT_FILE} -subj "/CN=${HOST}/O=${HOST}"

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=john-cd.com"
```

Note: To find myhost.com for minikube, run the following commands:

```shell
 $ minikube ssh
 $ echo $HOSTNAME
 minikube
```

- Create a Kubernetes secret

```shell
kubectl create secret tls ${CERT_NAME} --key ${KEY_FILE} --cert ${CERT_FILE}

kubectl create secret tls my-secret --key tls.key --cert tls.crt
```

Add under ``spec:`` in 

```yaml
  tls:
  - hosts:
    - myhost.com
    secretName: my-secret
```

Find and delete all nginx pods to force the ``nginx.conf`` to update and reflect the ingress changes. Find the ingress pods with the following:

```shell
kubectl get pods --all-namespaces
kubectl delete pods --namespace=kube-system [ingress pod]
```
