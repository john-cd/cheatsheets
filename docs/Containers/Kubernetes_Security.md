---
title: Kubernetes Security
tags: Kubernetes Security
---

<!-- TODO Reviewed ??-??-2026 -->

# Kubernetes Security: PSA/PSS, RBAC, and NetworkPolicy

Use admission controls, workload identities, and network isolation together. These controls address different risks; none replaces image review, secret handling, node hardening, or runtime monitoring.

The manifests are example starting points, not evidence that a particular cluster has these controls enabled. Adapt and test them against your cluster before enforcement.

## Pod Security Standards and Admission (PSS/PSA)

The Pod Security Standards define three policy levels:

| Level        | Use                                                                             |
| ------------ | ------------------------------------------------------------------------------- |
| `privileged` | Unrestricted behavior for trusted system workloads.                             |
| `baseline`   | Blocks known privilege escalations while allowing common workloads.             |
| `restricted` | Applies the stronger isolation settings expected for ordinary application Pods. |

Pod Security Admission applies these standards through namespace labels. Its modes have different effects: `enforce` rejects noncompliant Pods, `warn` returns a client warning, and `audit` records an audit annotation. Start with warning and audit modes to find workloads that need changes before enabling enforcement.

This namespace starts in that review stage. The example pins checks to Kubernetes `v1.37`; use the policy version for your cluster's Kubernetes minor release and keep it consistent with your rollout plan.

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: app
  labels:
    pod-security.kubernetes.io/warn: restricted
    pod-security.kubernetes.io/warn-version: v1.37
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/audit-version: v1.37
```

Apply the namespace and workloads, then review warnings and audit records:

```shell
kubectl apply -f namespace.yaml
kubectl apply -f deployment.yaml
kubectl get events -n app --sort-by=.metadata.creationTimestamp
```

Before changing the namespace to enforce `restricted`, ask the API server to evaluate the change without saving it. If the warnings are resolved, repeat the command without `--dry-run=server`:

```shell
kubectl label --dry-run=server --overwrite namespace app \
  pod-security.kubernetes.io/enforce=restricted \
  pod-security.kubernetes.io/enforce-version=v1.37
```

Enforcement applies when Pods are admitted; it does not rewrite existing Pods. Controllers may fail to replace a noncompliant Pod after enforcement changes, so check existing workloads before promoting a namespace.

### A restricted Linux workload

This Deployment shows common settings accepted by the `restricted` profile. Replace the example image and numeric IDs with values supported by your image and cluster. The application does not call the Kubernetes API, so its Pod does not need an automatically mounted service-account token.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
  namespace: app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      automountServiceAccountToken: false
      securityContext:
        runAsNonRoot: true
        runAsUser: 10001
        runAsGroup: 10001
        fsGroup: 10001
        seccompProfile:
          type: RuntimeDefault
      containers:
        - name: api
          image: registry.example.com/team/api:1.2.3
          ports:
            - name: http
              containerPort: 8080
              protocol: TCP
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 256Mi
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop:
                - ALL
          volumeMounts:
            - name: tmp
              mountPath: /tmp
      volumes:
        - name: tmp
          emptyDir: {}
```

`runAsNonRoot`, the seccomp profile, disabled privilege escalation, and dropping all Linux capabilities are part of the restricted profile. A read-only root filesystem is an additional hardening choice; mount writable paths explicitly when the application needs them. The profile does not decide which images are trustworthy or whether their contents are patched.

For a migration, the older `PodSecurityPolicy` API was removed in Kubernetes v1.25. Use Pod Security Admission for the built-in profiles, or evaluate a separate admission policy when your requirements need custom rules.

## RBAC: grant only the API access a workload needs

RBAC roles grant verbs on API resources. A `Role` is scoped to one namespace; a `ClusterRole` can grant cluster-wide access or be reused by a namespaced binding. A `RoleBinding` grants permissions within its namespace. A `ClusterRoleBinding` grants a `ClusterRole` across the cluster.

This example lets one service account read one ConfigMap in namespace `app`:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: config-reader
  namespace: app
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: config-reader
  namespace: app
rules:
  - apiGroups: [""]
    resources:
      - configmaps
    resourceNames:
      - app-settings
    verbs:
      - get
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: config-reader
  namespace: app
subjects:
  - kind: ServiceAccount
    name: config-reader
    namespace: app
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: config-reader
```

Bind this service account only to the workload that needs the ConfigMap. Workloads that do not call the Kubernetes API should set `automountServiceAccountToken: false`; workloads that do need API access should use a dedicated identity and only its required permissions.

Check the intended permissions. Impersonation requires the caller to have permission to impersonate the service account:

```shell
kubectl auth can-i get configmap/app-settings -n app \
  --as=system:serviceaccount:app:config-reader
kubectl auth can-i list secrets -n app \
  --as=system:serviceaccount:app:config-reader
```

The first check should return `yes`; the second should return `no`. Avoid wildcard verbs and resources, broad bindings to `default` service accounts, and unnecessary access to Secrets. Review who can create or change Roles and RoleBindings: those permissions can enable privilege escalation.

## NetworkPolicy: isolate traffic by workload and namespace

NetworkPolicies are namespaced allow rules. Without a policy selecting a Pod, ingress and egress are allowed by default. Policies that select a Pod isolate only the directions they list; applicable policies add their allowed traffic together. For a Pod-to-Pod connection to work, the source's egress rules and destination's ingress rules must both allow it.

The following example denies all traffic in namespace `app`, then permits DNS and the `frontend` to `api` flow on TCP port 8080:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: app
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-ingress-to-api
  namespace: app
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-egress-to-api
  namespace: app
spec:
  podSelector:
    matchLabels:
      app: frontend
  policyTypes:
    - Egress
  egress:
    - to:
        - podSelector:
            matchLabels:
              app: api
      ports:
        - protocol: TCP
          port: 8080
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-dns-egress
  namespace: app
spec:
  podSelector: {}
  policyTypes:
    - Egress
  egress:
    - to:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: kube-system
          podSelector:
            matchLabels:
              k8s-app: kube-dns
      ports:
        - protocol: UDP
          port: 53
        - protocol: TCP
          port: 53
```

In the DNS rule, the namespace and Pod selectors appear in one peer, so they are combined: traffic must go to a `kube-dns` Pod in `kube-system`. Check your cluster's DNS labels before applying this rule; distributions and NodeLocal DNSCache configurations can differ. A default-deny egress policy also blocks every other dependency, so add narrow rules for each required destination and port before rollout.

If `frontend` is in another namespace, add a `namespaceSelector` beside its `podSelector` in the API ingress rule. In one peer these selectors mean “Pods with this label in namespaces with that label”; separate peer entries mean either source. If the frontend namespace isolates egress, add a matching egress rule there. Add a separate ingress rule for any ingress controller that must reach the frontend. For external endpoints, use maintained CIDR ranges and account for address rewriting by your CNI and Service implementation.

Verify that the cluster's CNI plugin implements NetworkPolicy before relying on these objects; creating a policy without a supporting plugin has no effect. Inspect the applied selectors and test both an allowed and a denied connection from a disposable debug Pod using an approved image:

```shell
kubectl get networkpolicy -n app
kubectl describe networkpolicy -n app default-deny-all
kubectl get pods -n app --show-labels
```

NetworkPolicy operates at Layer 4 and has no explicit deny rule. It does not provide TLS inspection, service-name targeting, or logging of accepted and blocked connections. Use a service mesh, firewall, or another control when those behaviors are required.

## Rollout checklist

1. Put workloads with different trust needs in separate namespaces.
2. Start Pod Security Admission with `warn` and `audit`; review all workload templates and events.
3. Set non-root identities and required security contexts, then test with server-side dry runs.
4. Grant each workload a dedicated service account and minimal Role; disable token mounting when API access is unnecessary.
5. Confirm CNI support, map service flows, and add NetworkPolicies before enabling default-deny egress.
6. Promote the namespace to `enforce` only after warnings are resolved and replacement Pods can start.
7. Recheck policy versions, RBAC bindings, namespace labels, and actual network reachability during upgrades.

## References

- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/)
- [Enforce Pod Security Standards with namespace labels](https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-namespace-labels/)
- [RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [RBAC good practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)
- [Service accounts](https://kubernetes.io/docs/concepts/security/service-accounts/)
- [NetworkPolicies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
