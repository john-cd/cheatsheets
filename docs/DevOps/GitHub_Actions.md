---
title: Advanced GitHub Actions
---

<!-- TODO Reviewed 11-23-2026 -->

# Advanced GitHub Actions

Use reusable workflows when several repositories or workflows need the same
job sequence. Use a matrix when one job should run for several platforms or
versions. Cache dependencies that can be downloaded again; publish artifacts
when later jobs or people need the output.

Start with [the basic workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
and the repository's [Git cheatsheet](Git.md). The examples below use
full-length action commit SHAs; review the upstream action and update each pin
through the repository's normal dependency review.

## Reusable workflows

A reusable workflow is a YAML file in `.github/workflows/` that declares
`on.workflow_call`. A caller invokes it at the job level with `uses`. The
called workflow can contain multiple jobs. A composite action groups steps
inside one job, so use it when the shared unit is a sequence of steps rather
than a workflow with its own runner, permissions, or job graph.

Declare typed inputs and only the secrets the called workflow needs. Pass
secrets by name instead of using `secrets: inherit` unless every caller secret
is intentionally available to the called workflow. A workflow chain passes a
secret only to the next workflow when that workflow explicitly forwards it.

Caller workflow:

```yaml
name: Python checks

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  tests:
    uses: ./.github/workflows/reusable-python-tests.yml
    with:
      python-version: "3.13"
```

Reusable workflow:

```yaml
name: Reusable Python tests

on:
  workflow_call:
    inputs:
      python-version:
        description: Python version to test
        required: true
        type: string

jobs:
  tests:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
      - uses: actions/setup-python@6d4fd22b20465ccc0f7354476588e8df7c9ca0e0 # v7.1.0
        with:
          python-version: ${{ inputs.python-version }}
          cache: pip
          cache-dependency-path: requirements*.txt
      - run: python -m unittest discover -s tests -p "test_*.py"
```

For a workflow in another repository, use
`OWNER/REPOSITORY/.github/workflows/FILE.yml@REF`. Pin the reference to a
reviewed commit SHA when immutable workflow content is required. Keep the
caller and called workflow permissions explicit; the called workflow cannot
gain permissions that the caller did not grant.

## Matrix builds

A matrix creates one job for each combination of its values. Two operating
systems and two Python versions produce four jobs:

```yaml
name: Test matrix

on:
  pull_request:

permissions:
  contents: read

jobs:
  tests:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      max-parallel: 4
      matrix:
        os: [ubuntu-latest, windows-latest]
        python-version: ["3.12", "3.13"]
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
      - uses: actions/setup-python@6d4fd22b20465ccc0f7354476588e8df7c9ca0e0 # v7.1.0
        with:
          python-version: ${{ matrix.python-version }}
          cache: pip
          cache-dependency-path: requirements*.txt
      - run: python -m unittest discover -s tests -p "test_*.py"
```

Use `matrix.include` to add a configuration or attach extra values to
matching configurations. Use `matrix.exclude` to remove combinations that the
project does not support. Exclusions are applied before inclusions. Keep the
matrix small: a workflow can create at most 256 jobs from one matrix.

`fail-fast` defaults to `true`, which cancels queued and running matrix jobs
after a failure. Set it to `false` when results from every platform are
useful. Use `max-parallel` to limit concurrent jobs when runner capacity,
service limits, or cost require it. Mark only an explicitly experimental
configuration `continue-on-error`; required platform combinations should
still fail the workflow.

## Dependency caching

Prefer a language setup action's cache option when it covers the package
manager. In the examples above, `setup-python` caches pip downloads using the
requirements files as inputs. For package managers without built-in support,
use `actions/cache` with a key that includes the operating system,
architecture, tool version, and lockfile hash. Add restore-key prefixes only
when older dependency caches remain safe to reuse.

A cache is disposable input that can speed up a later run. An artifact is an
output to retain or pass between jobs, such as a binary, test report, or
deployment bundle. A job must still succeed when its dependency cache is
missing or unusable. Never put credentials, private datasets, or other
sensitive material in a cache.

Cache access is scoped by branch and trigger trust. A pull request from a fork
can read eligible caches, so restored files must be treated as untrusted.
GitHub's current cache controls default low-trust jobs to read-only access.
Avoid granting write access to a job that checks out or executes untrusted
pull-request code; a poisoned cache can later affect a more privileged job.
For reusable workflows, set the caller's `cache-mode` explicitly when the
called workflow should not write caches.

## Review checklist

- Give the workflow and each job only the `GITHUB_TOKEN` permissions it needs.
- Pin actions to full commit SHAs and keep a version comment beside each pin.
- Use typed inputs for reusable workflows and pass secrets by name.
- Bound matrix size and parallelism; keep required combinations separate from
  optional experiments.
- Cache dependencies, not secrets or deliverables, and include lockfiles in
  cache keys.
- Upload build outputs and test reports as artifacts instead of relying on a
  dependency cache.
- Confirm that a cache miss, cache eviction, or disabled cache does not break
  correctness.

## References

- [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [Reuse workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows)
- [Run job variations with a matrix](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations)
- [Dependency caching](https://docs.github.com/en/actions/concepts/workflows-and-actions/dependency-caching)
- [Dependency caching reference](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching)
- [Secure use of GitHub Actions](https://docs.github.com/en/actions/reference/security/secure-use)
- [actions/setup-python caching](https://github.com/actions/setup-python#caching-packages)
