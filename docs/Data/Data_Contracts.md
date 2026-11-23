---
title: Data Contracts and Schema Evolution
---

<!-- TODO Reviewed 11-23-2026 -->

# Data Contracts and Schema Evolution

A schema describes a data shape. A data contract also explains what that data
means, who produces and consumes it, what quality and delivery behavior to
expect, and how changes are released. Treat a contract as an interface shared
by independently deployed systems, not just as a registry entry.

## Write down the contract

Record these decisions where producers and consumers can find them:

| Area                    | Specify                                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------------------- |
| Identity and ownership  | Stable contract name, accountable team, contact path, and change process.                                |
| Use and lifecycle       | What a record or event means, when it is emitted, retention, replay, and deletion behavior.              |
| Producers and consumers | Known writers and readers, including batch jobs, exports, dashboards, and backfills.                     |
| Fields                  | Type, presence, null meaning, units, timezone, allowed values, and whether order matters.                |
| Quality and delivery    | Required invariants, uniqueness or deduplication key, freshness, ordering, lateness, and retry behavior. |
| Privacy and access      | Classification, permitted uses, access rules, retention, and handling of sensitive fields.               |
| Change policy           | Compatibility direction, retained versions, deprecation window, and migration owner.                     |

A machine-readable schema helps validate structure. It cannot tell whether a
timestamp means event time or ingestion time, whether an amount is dollars or
cents, or whether a producer is allowed to emit a particular event. Define
those semantics and test them separately.

## Make presence and meaning explicit

For each field, distinguish:

- **Absent:** the producer did not provide a value. A consumer may treat this as
  unknown, not applicable, or not yet computed; choose one meaning.
- **Null:** the producer explicitly sent no value. Do not assume every format or
  client treats it the same as an absent field.
- **Empty or zero:** a real value such as an empty string, an empty collection,
  `false`, or `0`. These are not substitutes for missing data unless the
  contract says so.
- **Default:** a value supplied by a reader, a producer, or a transformation.
  Name which component applies it and when.

Document units and time conventions alongside types. For example, state whether
an amount is an integer in the currency's minor unit, whether timestamps are
UTC, and whether a duration is measured in seconds or milliseconds. Keep the
same meaning when renaming or widening a field; a structural compatibility
check cannot detect a semantic change.

## Example: add an optional event field

This illustrative JSON Schema is version 2 of an `OrderPlaced` event. Version 1
contains the first five fields. Version 2 adds `coupon_code`, which may be
omitted or explicitly `null`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.example.com/orders/order-placed/v2",
  "title": "OrderPlaced",
  "type": "object",
  "properties": {
    "event_id": { "type": "string", "minLength": 1 },
    "occurred_at": { "type": "string", "format": "date-time" },
    "order_id": { "type": "string", "minLength": 1 },
    "amount_minor": { "type": "integer", "minimum": 0 },
    "currency": { "type": "string", "pattern": "^[A-Z]{3}$" },
    "coupon_code": { "type": ["string", "null"], "minLength": 1 }
  },
  "required": [
    "event_id",
    "occurred_at",
    "order_id",
    "amount_minor",
    "currency"
  ],
  "additionalProperties": true
}
```

For this example, `amount_minor` uses the exponent for the ISO currency code;
production contracts should state the unit and validate the relationship
between amount and currency. The schema's `format` keyword may be an annotation
only unless the selected validator is configured to assert it. JSON Schema's
`default` is also an annotation: validation does not insert a missing value.

An old event has no coupon field:

```json
{
  "event_id": "evt-1042",
  "occurred_at": "2026-11-23T18:00:00Z",
  "order_id": "ord-72",
  "amount_minor": 1250,
  "currency": "USD"
}
```

A new event can include the optional field:

```json
{
  "event_id": "evt-1043",
  "occurred_at": "2026-11-23T18:05:00Z",
  "order_id": "ord-73",
  "amount_minor": 980,
  "currency": "USD",
  "coupon_code": "WELCOME"
}
```

The new schema accepts the old event because `coupon_code` is not required. An
old consumer can process the new event only if its parser ignores unknown
properties; the old schema accepting extra properties does not guarantee that
application code behaves that way. `additionalProperties` is `true` by default,
but setting it to `false` can make an otherwise additive field change fail for
old validators. Check both the schema and the actual consumer behavior.

## Choose a compatibility direction

Compatibility describes which version of a reader can process data written by
which version of a producer. Confirm the exact rules for the chosen format,
registry, serializer, and validator; the labels are not a substitute for testing
real clients.

| Policy     | Reader/writer question                                                                       | Typical deployment order                                                                             |
| ---------- | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Backward   | Can a reader using the new schema read data written with the old schema?                     | Upgrade readers before writers begin emitting the new shape.                                         |
| Forward    | Can a reader using the old schema read data written with the new schema?                     | Upgrade writers first; move readers after old data is drained or outside the required replay window. |
| Full       | Can both old and new readers process data from both versions?                                | Either side can usually move first, subject to application and semantic checks.                      |
| Transitive | Is the change compatible with every retained prior version, rather than only the latest one? | Use when old data, snapshots, or replay paths can contain any retained version.                      |

For example, Confluent Schema Registry calls a new reader reading old-writer
data backward compatibility and documents `BACKWARD` as its default. That
default is not transitive and is specific to that product. Other registries and
formats may use different defaults and compatibility rules. Do not select a
policy until you know which producer and reader versions must coexist.

## Common format-specific cautions

### JSON Schema

- Properties are optional unless listed in `required`. An optional property and
  a nullable property are separate choices.
- By default, extra object properties are allowed. Setting
  `additionalProperties: false` is useful for strict validation, but can make
  old validators reject new fields.
- `default` does not fill in missing values during validation. Add application
  code or a transformation if a missing value must be materialized.
- Enable and test `format` assertions explicitly if values such as timestamps
  must be rejected when malformed.

### Avro

Avro data is read using a writer schema and a reader schema. Schema resolution
matches record fields by name; a reader can ignore writer fields it does not
know. If a new reader field is absent from old writer data, the reader needs an
Avro default for that field. Test the actual writer/reader pairs used during
deployment and replay.

### Protocol Buffers

Field numbers are part of the wire format. Do not renumber a field or reuse a
deleted tag. Reserve deleted numbers and names; reserve removed enum numbers and
names too. A wire-compatible addition can still break source code, for example
when an exhaustive application switch encounters a new enum value.

## Roll out a change safely

1. Inventory writers, readers, generated clients, sinks, exports, stored
   snapshots, and replay or backfill jobs. Include clients that are not deployed
   every day.
2. Choose the versions and compatibility direction that must overlap. Decide
   whether checks compare only with the latest schema or all retained versions.
3. Prefer an additive change. Make new fields optional or provide a deliberate
   reader default, keep old meanings stable, and ensure consumers handle
   unrecognized fields and enum values.
4. Check the schema with the same dialect and validator used in production.
   Check compatibility against the required historical versions. Validate
   representative old and new records, business invariants, generated clients,
   and consumer behavior.
5. Deploy in the order required by the compatibility direction. Watch parse or
   validation failures, null and default rates, unknown fields, freshness,
   duplicates, and downstream data quality.
6. Deprecate before removal. Stop writing the old field, observe that supported
   consumers no longer read it, wait through retention and replay windows, then
   remove it. Reserve deleted Protobuf identifiers.

For a breaking change that cannot be rolled out compatibly, use an explicit
migration boundary such as a new topic, table, endpoint, or versioned contract.
Dual-read or dual-write only where needed, backfill and reconcile the data,
measure cutover, and keep a rollback path until the old contract's retention
window has elapsed. Do not disable registry checks merely to get an incompatible
change accepted.

## Contract review checklist

- [ ] Owner, producers, consumers, purpose, retention, and replay behavior are
      recorded.
- [ ] Field presence, null meaning, units, time basis, sensitive-data handling,
      and business constraints are explicit.
- [ ] Old and new schema pairs are checked in the required direction, including
      every retained version when historical reads are supported.
- [ ] Producer examples and consumer fixtures cover absent fields, nulls,
      unknown fields or enum values, and invalid business states.
- [ ] Rollout order, monitoring, deprecation period, and rollback boundary are
      agreed before release.

## References

- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12)
- [JSON Schema object properties and `required`](https://json-schema.org/understanding-json-schema/reference/object)
- [JSON Schema annotations, defaults, and examples](https://json-schema.org/understanding-json-schema/reference/annotations)
- [Apache Avro specification: schema resolution](https://avro.apache.org/docs/1.12.0/specification/#schema-resolution)
- [Protocol Buffers proto3 guide](https://protobuf.dev/programming-guides/proto3/)
- [Protocol Buffers best practices](https://protobuf.dev/programming-guides/dos-donts/)
- [Confluent Schema Registry: schema evolution and compatibility](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html)
