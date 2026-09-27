---
note_type: concept
search_stage: serving
tags:
  - gcp
  - search-eng
---

Google Cloud compute choices differ in **what runs**, **who operates the infrastructure**, and **how work starts and stops**. A container is a packaging format; it does not by itself choose the hosting platform.

## Service comparison

| Option | Good starting requirement | Main responsibility retained |
|---|---|---|
| [[G Compute Engine (GCE)\|Compute Engine]] | OS and VM configuration control | OS, application fleet and recovery |
| [[G Container Engine\|GKE]] | Kubernetes orchestration | Workload specifications and cluster policy |
| [[Cloud Run]] | Managed container execution | Runtime contract and dependency capacity |
| [[Cloud Functions\|Cloud Run functions]] | Focused HTTP or event handler | Event contract and retry safety |
| [[G App Engine\|App Engine]] | Application fits its platform model | Runtime compatibility and application design |

These are starting points, not mutually exclusive architecture categories. For example, one system can serve requests on Cloud Run and run a specialized batch process on VMs.[^run][^gke]

## Separate three decisions

### 1. Execution shape

An API responds within a request deadline. A job finishes a bounded task. A stream processor continuously tracks progress over incoming events. Choose a platform mode that matches the lifecycle rather than keeping an HTTP request open for arbitrary background work.

### 2. State and failure

Ask where durable data lives, how work resumes, and whether an operation can repeat safely. Managed compute does not make application state durable. Horizontal scaling requires a shared state design or a deliberate partitioning strategy.

### 3. Operating responsibility

More infrastructure control can be necessary, but it adds patching, capacity, and recovery work. Less infrastructure management still leaves application monitoring, access control, dependency limits, and cost ownership with the team.

## Worked selection example

Assume a search application has three workloads:

1. **Online API:** containerized, bounded requests, external state. Evaluate Cloud Run first.
2. **Nightly import:** finite work split into independent shards. Evaluate a managed job; use [[DataProc]] or [[Data Flow]] when the processing model requires them.
3. **Specialized existing binary:** requires OS-level configuration that the managed runtime does not support. Evaluate Compute Engine.

This is a proposed selection process, not a universal recommendation. Validate latency, networking, runtime support, and total cost with a representative workload before committing.

## Failure modes

Avoid choosing GKE merely because Docker is used, assuming VMs cannot run containers, or assuming autoscaling removes database limits. Compare end-to-end behavior, including startup time and recovery, rather than only per-unit compute pricing.

## Exercise

An API's load is small but it requires a large model in memory. Which measurements could change the initial Cloud Run choice? Consider startup, memory, utilization, and latency targets.

## References & Useful Links

[^run]: [Cloud Run overview](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) — Managed execution modes.
[^gke]: [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) — Kubernetes operating model.
