---
title: Kubernetes Concepts
tags: Kubernetes
---

- Pods - A Pod is a Kubernetes abstraction that represents a group of one or more application containers (such as Docker or rkt), and some shared resources for those containers. 
Kubernetes workloads, such as Deployments and Jobs, are composed of one or more Pods.
Shared pod resources include:
    - Shared storage, as Volumes
    - Networking, as a unique cluster IP address
    - Information about how to run each container, such as the container image version or specific ports to use

- Nodes: A Pod always runs on a Node. A Node is a worker machine in Kubernetes and may be either a virtual or a physical machine, depending on the cluster. Each Node is managed by the Master. A Node can have multiple pods, and the Kubernetes master automatically handles scheduling the pods across the Nodes in the cluster. 

- Deployment - The most common way of running X copies (Pods) of your application. Supports rolling updates to your container images.

- Service - By itself, a Deployment can’t receive traffic. Setting up a Service is one of the simplest ways to configure a Deployment to receive and loadbalance requests. Depending on the type of Service used, these requests can come from external client apps or be limited to apps within the same cluster. A Service is tied to a specific Deployment using label selection.

- Labels - Identifying metadata that you can use to sort and select sets of API objects. Labels have many applications, including the following:

	* To keep the right number of replicas (Pods) running in a Deployment. The specified label is used to stamp the Deployment’s newly created Pods (as the value of the ``spec.template.labels`` configuration field), and to query which Pods it already manages (as the value of ``spec.selector.matchLabels``).
	* To tie a Service to a Deployment using the selector field.
	* To look for specific subset of Kubernetes objects, when you are using kubectl. For instance, the command kubectl get deployments --selector=app=nginx only displays Deployments from the nginx app.
