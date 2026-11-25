# GitHub Actions workflows

<!-- workflow-operations-reference:start -->

<!-- TODO Reviewed ??-??-2026. -->

## Workflow operations reference

The workflow YAML files own execution behavior. Their inline comments explain the purpose and
the boundaries that must survive future refactoring. This reference records the current job map;
repository-level Actions enable/disable settings remain independent of these tracked definitions.

### Changes in this review

- ci.yaml: Bound deploy to 30 minutes.
- ci.yaml: Bound validate to 30 minutes.
- ci.yaml: Consolidated Markdown lint and repository hooks into the existing validation job; removed the duplicate markdown-lint.yml setup (no required check used the removed jobs).

### [ci](ci.yaml)

Events: `push, workflow_dispatch, pull_request`. Branch/path filters and manual defaults are defined in the linked file.

| Job      | Runs on / reuse | Dependencies | Guard                                                                                                    | Main checks or side effects                                                                                                                                                                                                                                                                                                                                                                    |
| -------- | --------------- | ------------ | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| validate | "ubuntu-latest" | []           | Successful dependencies (default)                                                                        | Install Just; actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1; actions/setup-python@6d4fd22b20465ccc0f7354476588e8df7c9ca0e0; actions/setup-node@949feb2413d6458794dcd2491c4babbbce0c15c1; Install uv; just sync; just uv tool install prek; dprint/check@371a959e3c77f34a76a03d2c50df2e3f2302d016; just hooks; just markdownlint; just test; node --test tests/*.test.js; just docs |
| deploy   | "ubuntu-latest" | "validate"   | github.event_name == 'push' && (github.ref == 'refs/heads/main' \|\| github.ref == 'refs/heads/develop') | Install Just; actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1; Configure Git Credentials; actions/setup-python@6d4fd22b20465ccc0f7354476588e8df7c9ca0e0; Install uv; just sync; just uv run mkdocs gh-deploy --force                                                                                                                                                                 |

### Caches, permissions and failures

- Keep package downloads and compiler outputs separate. Match cache keys to compiler, OS, dependency locks, build profiles and features; a cache is an optimization, not a prerequisite for correctness.
- Matrix jobs start on separate machines. Build/test commands in one job reuse local outputs; moving them to separate jobs requires an explicit compatible artifact handoff.
- Read-only validation and live publication have different lifecycles. Preserve existing credentials, event/ref conditions, environments and non-cancelling deployment groups.
- Timeouts bound hung or unexpectedly expensive runs. Diagnose a timeout before increasing it; never convert a failed check into an unconditional success.
- A queued/disabled/billing-blocked run is not a passed check. Record hosted results separately from local workflow parsing/format validation.

### Local validation

```sh
actionlint
git diff --check
```

Use the repository formatter for edited YAML/Markdown. Run the commands named by the affected
jobs when their executable behavior changes; platform/container/credential-dependent checks
must be reported at the scope actually executed. Do not run publishing commands merely to test
a comment or validation-only change.

<!-- workflow-operations-reference:end -->
