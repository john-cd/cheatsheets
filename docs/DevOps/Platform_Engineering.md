---
title: Platform Engineering
---

<!-- TODO Reviewed 11-23-2026 -->

# Platform Engineering

Platform engineering is the practice of designing and operating shared
capabilities as an internal product for application teams. The product includes
people, processes, policies, interfaces, and technology; a developer portal is
only one possible interface. Start with a real user problem and a small
workflow, not a large platform build. The [CNCF maturity model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)
describes platform work as contextual and recommends improving the aspects
that matter to the organization rather than pursuing a level for its own sake.

An internal developer platform may combine a catalog, templates, build and
deployment paths, environment provisioning, identity, security controls,
observability, and support. It should reduce repeated decisions and waiting
while making ownership and operational expectations clear.

For a deeper guide to signals and cross-signal correlation, see
[Observability with OpenTelemetry](../Observability/OpenTelemetry.md).

## Start with a user journey

Choose a frequent task that crosses team boundaries. Examples include:

| Journey             | Useful first improvement                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------ |
| Start a service     | Create a repository with ownership, build, test, and deploy defaults.                            |
| Make a safe release | Provide a documented, self-service deployment path with visible status and rollback guidance.    |
| Add a dependency    | Offer approved service templates with a clear owner, lifecycle, and support contract.            |
| Debug production    | Put logs, traces, dashboards, recent deployments, and the owning team in one discoverable place. |

Interview the people who do the task. Record where they wait, repeat work, ask
for help, or work around existing tooling. Define the desired outcome and a
baseline before choosing a portal or product. A useful first platform slice can
be documentation, an API, a template, or an automated workflow.

## Golden paths

A golden path is a supported, self-service route through a common workflow.
It packages tested defaults and makes the next step discoverable. A good path
still allows validated choices and a documented route for legitimate needs it
does not cover.

For a new service, a path could connect:

1. A template that creates the repository and ownership metadata.
2. A build and test workflow with least-privilege permissions.
3. A deployment workflow with environment-specific policy and rollback steps.
4. Default dashboards, logging, tracing, and an on-call or support owner.
5. A catalog entry that links the service to its documentation and runtime.

The path is a product with maintainers, support, release notes, compatibility
expectations, and a deprecation process. Keep it small enough to update when
the underlying tools change. Avoid turning it into a mandatory one-size-fits-all
framework: an inflexible path can push teams toward workarounds. DORA describes
ticket-driven platform teams, big-bang launches, and rigid “golden cages” as
common pitfalls in its [platform engineering guidance](https://dora.dev/capabilities/platform-engineering/).

## Templates and a software catalog

Templates reduce setup work; a catalog helps people find software and its
owners. These are implementation choices, not requirements for every platform.
The Backstage [Software Catalog](https://backstage.io/docs/features/software-catalog/)
uses metadata files stored with source code. The example below is a
Backstage-specific component descriptor, not a universal catalog format:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: payments-api
  description: Payments HTTP API
  annotations:
    github.com/project-slug: acme/payments-api
spec:
  type: service
  lifecycle: production
  owner: group:payments
```

The catalog should expose the concepts people need to discover and own services.
Keep rapidly changing deployment or dependency details in the systems that own
them, and link those views from the catalog when useful. Backstage documents
that its catalog mirrors source metadata and can organize related tooling
through plugins.

Backstage [Software Templates](https://backstage.io/docs/features/software-templates/adding-templates/)
are one way to create consistent service repositories. A template can collect
validated inputs, fetch a skeleton, publish a repository, and register the
result. Treat templates as maintained code: review their generated files,
test changes, identify an owner, and publish migration guidance when outputs
change.

For workflow details, see the [advanced GitHub Actions guide](GitHub_Actions.md).

## Measure outcomes with a scorecard

The scorecard below is an illustrative proposal, not a standard or a built-in
Backstage schema. Adapt the measures to the journey and agree on definitions
with platform users before setting targets.

| Outcome                | Example measure                                                                       | Guardrail                                                             |
| ---------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Faster onboarding      | Median time from repository creation to first healthy deployment.                     | Include failed attempts and compare the same workflow.                |
| More self-service      | Share of eligible tasks completed without a platform-team handoff.                    | Keep a reason for each handoff so missing capabilities are visible.   |
| Better task experience | Task completion rate and a short user satisfaction question.                          | Sample different roles and experience levels.                         |
| Reliable delivery      | Change lead time, deployment frequency, change failure percentage, and recovery time. | Review reliability alongside speed; do not optimize one metric alone. |
| Sustainable platform   | Support requests, operational toil, and upgrade completion for platform capabilities. | Include the maintenance cost of the golden path.                      |

Take a baseline before launch, then review results with the teams using the
path. DORA recommends combining software delivery measures with developer
satisfaction and task-success signals in its [platform measurement guidance](https://dora.dev/capabilities/platform-engineering/).
The [CNCF maturity model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)
also treats measurement and user feedback as parts of platform development.
Use a scorecard to prompt investigation and improvement, not to rank teams or
turn adoption into a compliance target.

## A small rollout checklist

- Name the internal users and the task the platform should improve.
- Map the current workflow and record a baseline.
- Start with one common path and a small pilot group.
- Document inputs, outputs, access boundaries, ownership, support, and failure recovery.
- Offer clear feedback, safe defaults, and an escape hatch for uncommon cases.
- Measure task success, user experience, delivery outcomes, and platform maintenance.
- Keep a roadmap and deprecation policy; revisit the path with its users.

## References

- [CNCF Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)
- [CNCF Platforms White Paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)
- [Backstage Software Catalog](https://backstage.io/docs/features/software-catalog/)
- [Backstage: Adding software templates](https://backstage.io/docs/features/software-templates/adding-templates/)
- [DORA: Platform engineering](https://dora.dev/capabilities/platform-engineering/)
