---
title: Kubernetes Examples 
tags: Kubernetes
---

### Service + Deployment example

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
    targetPort: http	# can a text label (port name) or port number
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

### Ingress example

```yaml
# Ingress 
# https://kubernetes.io/docs/concepts/services-networking/ingress/
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: test
  annotations:
    ingress.kubernetes.io/rewrite-target: /
    kubernetes.io/ingress.class: nginx      # Use the nginx-ingress Ingress controller
spec:
  tls:
  - secretName: ingresssecret  # Referencing this secret in an Ingress will tell the Ingress controller to secure the channel from the client to the loadbalancer using TLS
  rules:
  - http:
      paths:
      - path: /api
        backend:
          serviceName: s1
          servicePort: 80
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
```
