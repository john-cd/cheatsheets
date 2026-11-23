---
title: Incident Response and Postmortems
tags: Incident Response Reliability Operations
---

<!-- TODO Reviewed ??-??-2026 -->

# Incident Response and Postmortems

Use a shared response process when an outage, security event, data problem, or
other operational failure affects users or could grow into a significant
impact. The goal during response is to limit harm, restore the service, and
keep people informed. Afterward, record what happened and turn useful findings
into owned, verifiable work.

This page is a starting template, not an incident plan for a specific
organization. Define severity thresholds, escalation contacts, communication
channels, legal and regulatory duties, and postmortem triggers before an event.
For suspected security or privacy incidents, involve the designated security,
privacy, legal, and communications teams; preserve evidence and follow the
organization's restricted-access procedures. This operational checklist does
not replace those plans.

## Prepare before an incident

- Define what user or business impact starts an incident and how responders
  assign severity. Severity labels differ; write impact-based criteria rather
  than relying on a number alone.
- Publish an on-call path, escalation contacts, and a reliable incident
  channel. Keep essential runbooks and status tools available if the affected
  service or identity provider is unavailable.
- Name the people who can declare an incident, approve risky mitigations,
  notify affected users, and engage security or legal response.
- Write down the service's user-visible symptoms, dependencies, dashboards,
  safe mitigations, rollback steps, and recovery checks.
- Decide which incidents require a postmortem, who owns follow-up, and where
  the write-up and actions will be tracked.
- Practice the process with a tabletop or failure exercise. Update runbooks
  when the exercise exposes a missing contact, permission, or decision.

## Coordinate the response

Assign explicit roles as the incident grows. One person can cover more than one
role for a small event, but the current incident commander and operational
decision maker must be clear to everyone.

| Role                    | Responsibility                                                                                              |
| ----------------------- | ----------------------------------------------------------------------------------------------------------- |
| Incident commander      | Owns the response state, sets priorities, delegates work, and decides when to escalate or resolve.          |
| Operations lead         | Coordinates diagnosis and mitigations. Keep production changes coordinated and record what changed and why. |
| Communications lead     | Maintains the incident record and sends scheduled updates to responders, stakeholders, and affected users.  |
| Scribe or planning lead | Records the timeline, tracks requests and action items, and prepares handoffs.                              |

These roles are adaptable; a small team can combine them. As an incident
becomes longer or spans teams, split the roles so the operations lead can focus
on safe mitigation while the commander coordinates and the communications
lead handles updates. See Google's [incident management guide](https://sre.google/sre-book/managing-incidents/)
for one example of role-based incident command.

## A response sequence

1. **Confirm the symptom and protect people.** Check user-facing service
   indicators, reports, and recent changes. For safety, privacy, or security
   risks, use the organization's designated emergency path.
2. **Declare and scope.** If the impact meets a pre-agreed trigger, declare an
   incident early. Record the start time, affected functions and regions,
   known user impact, severity, and what is still unknown. Reassess severity as
   evidence changes.
3. **Open a shared record.** Start a durable incident document and channel.
   Put the current impact, incident commander, operations lead, next actions,
   and next update time at the top.
4. **Reduce impact.** Prefer a safe, reversible mitigation that restores the
   user-visible service. State the hypothesis and expected effect before
   acting; record the change and check whether it helped. Preserve logs and
   evidence when security or data integrity may be involved.
5. **Communicate on a cadence.** Tell affected people what is known, what is
   unknown, what they can do, and when the next update will arrive. Do not wait
   for a confirmed root cause to acknowledge an impact.
6. **Hand off explicitly.** Transfer the impact summary, current state, open
   risks, recent changes, and next steps. The new commander should acknowledge
   the handoff in the shared channel before the prior commander leaves.
7. **Verify recovery.** Check customer-facing indicators, error rates, queued
   work, data integrity, and dependent services. Keep monitoring through the
   agreed recovery window before resolving the incident.
8. **Close and follow up.** Record the resolution time and remaining risks.
   Create tracked follow-up items and start a postmortem when the event meets
   the organization's criteria.

### Status update example

This fictional example shows the level of detail for a brief update; replace
the times and impact with evidence from the actual event:

```text
Status: Investigating
Impact: Some report-generation requests are timing out. No data loss is confirmed.
Started: 14:05 UTC, based on the first verified customer symptom.
Action: The operations lead paused the worker rollout while checking queue health.
Next update: 14:30 UTC, or sooner if impact changes.
```

Separate confirmed facts from hypotheses. If a fact changes, correct the
shared record rather than leaving contradictory updates in different channels.

## Write a useful postmortem

A postmortem is a learning record, not a verdict about a person. Agree on
triggers such as material user impact, data loss or exposure, emergency
rollback, a prolonged recovery, or a monitoring failure before an incident
occurs. Not every alert needs a full postmortem; the team should still record
small events when a pattern or a missing safeguard is worth learning from.

Write while evidence is available, using the review window defined by the
organization. Focus on what the system and team knew at each point, the
conditions that shaped decisions, and how safeguards performed. Blameless
writing does not hide mistakes or remove accountability: it explains how
interfaces, tools, alerts, procedures, staffing, and information affected the
outcome, then assigns improvements that can be verified.

### Postmortem template

```markdown
# [Short incident title]

- Status: Draft / Reviewed
- Incident ID and severity: [link and impact-based level]
- Service and owner: [service, team, incident commander]
- Incident window: [start and end, including timezone]
- Authors and review date: [names or roles, date]

## Summary

[What users experienced, for how long, and how the service recovered.]

## Impact

[Affected users, functions, regions, data, SLOs, and known limits of the estimate.]

## Detection and response

[How the event was detected, how the response worked, and what mitigations changed.]

## Timeline

| Time (UTC) | Observation or action | Evidence |
| ---------- | --------------------- | -------- |

## Trigger and contributing conditions

[Known trigger, causal chain, system behavior, missing signals, and assumptions that shaped decisions. Record uncertainty instead of forcing a single root cause.]

## What helped / what hindered

[Tools, procedures, coordination, and communications that affected the outcome.]

## Follow-up actions

| Action and intended effect | Type | Owner | Priority | Tracking link | Due or review date | Verifiable completion |
| -------------------------- | ---- | ----- | -------- | ------------- | ------------------ | --------------------- |

## Open questions and risks

[What remains unknown, who owns it, and when it will be revisited.]
```

Use a timeline with absolute timestamps and a timezone so responders can
correlate alerts, deployments, customer reports, and mitigation actions. Cite
the dashboard, log, ticket, or message behind important claims, and distinguish
measured impact from estimates.

### Make actions verifiable

Split large efforts into trackable actions. A useful action has an owner, a
priority, a due or review date, a tracking link, and an observable completion
condition. Include prevention, detection, mitigation, and response improvements
when the incident shows gaps in more than one area. Review open actions in the
normal team planning process; publishing a postmortem does not complete its
actions.

| Illustrative proposal                                          | Type       | Verifiable end state                                                                                          |
| -------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------- |
| Add a user-facing latency alert for the report-generation SLO. | Detection  | The alert fires in a staging exercise when the agreed threshold is crossed and links to the response runbook. |
| Add a documented worker-rollout pause and rollback step.       | Mitigation | A responder can follow the step in a staging exercise without production access from the author.              |

These are example proposals, not changes deployed to a real service. A team
should approve and track its own actions, then record evidence when each one is
completed.

For additional operational context, see [Observability with OpenTelemetry](../Observability/OpenTelemetry.md),
[Platform Engineering](Platform_Engineering.md), and [Cloud Workload FinOps](../Cloud/Cloud_Workload_FinOps.md).

## References

- [NIST SP 800-61 Rev. 3: Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — cybersecurity guidance published April 2025; apply with your organization's incident and reporting requirements.
- [Google SRE: Managing Incidents](https://sre.google/sre-book/managing-incidents/) — response roles, the incident record, and handoffs.
- [Google SRE Workbook: Incident Response](https://sre.google/workbook/incident-response/) — incident coordination practices.
- [Google SRE Workbook: Postmortem Culture](https://sre.google/workbook/postmortem-culture/) — postmortem practice, templates, and follow-up.
