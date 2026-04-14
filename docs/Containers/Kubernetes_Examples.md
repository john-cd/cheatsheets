---
title: Kubernetes Examples
tags: Kubernetes
---

# Service + Deployment example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: p2p-robot-service
spec:
  selector:
    app: p2p-robot
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: http # can a text label (port name) or port number
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: p2p-robot-deployment
spec:
  selector:
    matchLabels:
      app: p2p-robot
  replicas: 2          # tells deployment to run 2 pods matching the template
  template:            # create pods using pod definition in this template
    metadata:
      # the name is not included in the meta data as a unique name is
      # generated from the deployment name
      labels:
        app: p2p-robot # label used above in matchLabels
    spec:
        containers:
        - name: p2p-robot
          image: "johncd/p2p-robot:1.0.0"
          imagePullPolicy: IfNotPresent
          ports:
          - containerPort: 9000
            name: http
          env:
          - name: APPLICATION_SECRET    #  Place the application secret in an environment variable, which is read in application.conf
            valueFrom:
                secretKeyRef:
                  name: application-secret
                  key: application_secret
          volumeMounts:
          - name: conf-volume
            mountPath: /usr/local/etc
        volumes:
        - name: conf-volume
          configMap:            # The configMap resource provides a way to inject configuration data into Pods.
            name: app-conf
```

## Ingress example

```yaml
# Ingress
# https://kubernetes.io/docs/concepts/services-networking/ingress/
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: test
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx      # Use the nginx-ingress Ingress controller
  tls:
  - secretName: ingresssecret  # Referencing this secret in an Ingress will tell the Ingress controller to secure the channel from the client to the loadbalancer using TLS
  rules:
  - http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: s1
            port:
              number: 80
---
# Secure the Ingress by specifying a secret that contains a TLS private key and certificate.
apiVersion: v1
data:
  tls.crt: base64 encoded cert
  tls.key: base64 encoded key
kind: Secret
metadata:
  name: ingresssecret
  namespace: default
type: Opaque
---

### Custom Resource Definition (CRD) Example

CustomResourceDefinitions allow you to extend the Kubernetes API with your own custom objects.

First, you define the CRD:

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  # name must match the spec fields below, and be in the form: <plural>.<group>
  name: crontabs.stable.example.com
spec:
  group: stable.example.com
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                cronSpec:
                  type: string
                image:
                  type: string
  scope: Namespaced
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
    shortNames:
    - ct
```

Once the CRD is created in the cluster, you can create instances of your new Custom Resource (CR):

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  cronSpec: "* * * * */5"
  image: my-awesome-cron-image
```
