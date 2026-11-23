---
title: Observability with OpenTelemetry
---

<!-- TODO Reviewed 11-23-2026 -->

# Observability with OpenTelemetry

Observability is the ability to ask useful questions about a system from the
signals it emits. [OpenTelemetry](https://opentelemetry.io/docs/concepts/what-is-opentelemetry/)
provides APIs, SDKs, instrumentation, and a Collector for creating, processing,
and exporting telemetry. It is not a storage or visualization backend: choose
where the exported data will be retained, queried, and governed.

## Choose a signal for the question

| Signal  | What it describes                                           | Useful questions                                                                       |
| ------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Metrics | Numeric measurements aggregated over time and dimensions.   | Is request latency rising? How many errors occurred? Are we close to a capacity limit? |
| Traces  | The operations and relationships involved in a request.     | Which dependency or step made this request slow? Where did it fail?                    |
| Logs    | Timestamped event records with details about what happened. | What input, decision, or error explains this operation?                                |

These signals work together. Metrics help detect a change across a service;
traces show the path of selected requests; logs add event details around an
operation. Use a signal for what it represents: a metric is an aggregate, not
a per-request event log, and a trace is not a substitute for a service-wide
error-rate time series.

## Give telemetry a shared identity

Set a consistent `service.name` for every instance of the same logical service.
Add `service.version` when it helps explain changes between releases. Use
standard semantic conventions for common operations and attributes so libraries
and backends can interpret them consistently. A service name belongs in the
Resource context, which accompanies its telemetry; do not copy it into every
measurement as a high-cardinality dimension.

Instrument the application with an OpenTelemetry SDK or supported
instrumentation library. Auto-instrumentation can cover common framework and
network operations; add manual spans or measurements where they capture
important business steps the automatic instrumentation cannot see. Check for
duplicate instrumentation when both approaches cover the same operation.

## Correlate traces, logs, and metrics

### Trace context across services

A trace is a tree of spans that records work across process and service
boundaries. Instrumentation normally propagates the W3C Trace Context header
`traceparent`: the caller injects its trace and parent span identifiers, and
the receiver creates a child span in that trace. Confirm that HTTP clients,
servers, queues, and gateways preserve or deliberately restart context; a
missing propagation step breaks the end-to-end trace.

### Logs connected to a request

Use structured logs and, where the logging integration supports it, let the
OpenTelemetry SDK or bridge attach the active trace and span identifiers. If a
legacy JSON log format needs explicit fields, the OpenTelemetry convention uses
lowercase, hexadecimal `trace_id` and `span_id` fields:

```json
{
  "message": "Inventory lookup failed",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "span_id": "00f067aa0ba902b7"
}
```

The IDs are examples. A log emitted outside an active span may have no trace
context. Resource attributes identify the emitting service and runtime; trace
IDs connect records from the same request. Keep high-value event details in
logs, but do not add arbitrary user or request identifiers as metric labels.

### Metrics connected to selected traces

Metrics aggregate measurements. A request-duration histogram, for example,
can show that the slow tail is growing without retaining a separate time series
for every request. Avoid labels such as user ID, request ID, session ID, or raw
URL path: every unique attribute combination can create another time series and
increase memory and storage costs.

An [exemplar](https://opentelemetry.io/docs/specs/otel/metrics/data-model/#exemplars)
can attach trace context to a selected measurement in an aggregate metric. When
the SDK, exporter, backend, and UI support exemplars, a user can jump from a
latency bucket or error metric to a representative trace. Exemplars are optional
samples, not a complete list of requests. Do not put trace IDs in metric labels;
that creates unbounded cardinality and defeats aggregation.

## A local Collector pipeline

The OpenTelemetry Collector can receive telemetry, process it, and export it to
one or more destinations. A pipeline is enabled under `service.pipelines`; it
refers to components defined in the top-level `receivers`, `processors`, and
`exporters` sections. Component availability depends on the Collector
distribution you install.

This local example accepts OTLP over gRPC or HTTP, batches each signal, and
writes it to the Collector's debug output. Both listeners bind to loopback, so
the example is suitable for a local smoke check, not a shared or production
endpoint:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 127.0.0.1:4317
      http:
        endpoint: 127.0.0.1:4318

processors:
  batch: {}

exporters:
  debug: {}

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [debug]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [debug]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [debug]
```

Save it as `collector.yaml` and validate it with the binary for the Collector
distribution you run:

```sh
otelcol validate --config=collector.yaml
```

The `debug` exporter is useful for confirming that data reaches the pipeline.
For an application setup, replace it with an exporter supported by your chosen
backend, then configure transport security, authentication, retry/queue
behavior, resource enrichment, and data filtering for that deployment. Consult
the distribution's component list before copying a receiver, processor, or
exporter from another example.

## Roll out in small steps

1. Pick a user-facing reliability question, such as request success or page
   response time, and define the measurement and alert conditions.
2. Give the service a stable name and agree on a small set of resource and
   operation attributes. Follow the relevant semantic conventions.
3. Instrument one service and verify that its spans, metrics, and structured
   logs arrive with the expected resource identity.
4. Propagate trace context through its downstream calls. Check the trace at
   each service boundary and add logs with active trace IDs.
5. Add a Collector when you need shared export, batching, retries, filtering,
   or central routing. Begin with an agent near the application or a small
   gateway, and monitor the Collector itself.
6. Review the emitted data, sampling, cardinality, retention, and cost with
   service owners. Remove attributes and logs that do not help answer a real
   operational question. For application-level evaluation patterns, see
   [AI Engineering](../AI/AI_Engineering.md).

## Privacy and operational checks

- Do not record credentials, session tokens, payment details, or personal data
  unless the collection is necessary and explicitly governed. Review what
  instrumentation emits, not only what application code adds manually.
- Treat incoming trace context and baggage from untrusted callers carefully.
  Baggage is propagated across service boundaries and may be forwarded to
  third-party endpoints; never put secrets or sensitive user data in it.
- Use TLS and authentication for Collector traffic outside a trusted local
  boundary. Store Collector credentials and certificates in a secret manager,
  not in a checked-in configuration file.
- Bound metric attribute cardinality and log volume. Decide how sampling affects
  trace coverage and make sure metrics still provide the aggregate signals
  needed for alerts.
- Check for missing service names, broken trace parents, logs without the
  expected context, Collector queue pressure, and failed exports.

## References

- [OpenTelemetry observability primer](https://opentelemetry.io/docs/concepts/observability-primer/)
- [OpenTelemetry signals](https://opentelemetry.io/docs/concepts/signals/)
- [OpenTelemetry context propagation](https://opentelemetry.io/docs/concepts/context-propagation/)
- [OpenTelemetry metrics and cardinality](https://opentelemetry.io/docs/concepts/signals/metrics/)
- [OpenTelemetry metrics data model and exemplars](https://opentelemetry.io/docs/specs/otel/metrics/data-model/)
- [OpenTelemetry Collector quick start](https://opentelemetry.io/docs/collector/quick-start/)
- [OpenTelemetry Collector configuration](https://opentelemetry.io/docs/collector/configuration/)
- [OpenTelemetry service semantic conventions](https://opentelemetry.io/docs/specs/semconv/registry/attributes/service/)
- [OpenTelemetry sensitive data guidance](https://opentelemetry.io/docs/security/handling-sensitive-data/)
