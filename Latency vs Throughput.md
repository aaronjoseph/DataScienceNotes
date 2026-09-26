---
note_type: concept
search_stage: serving
---

# Latency vs Throughput

#search-eng

## Overview

**Latency** is elapsed time for an operation; **throughput** is the number completed per unit time. Define the boundary: end-to-end request latency is different from model inference time. Distributions matter because slow requests can be hidden by averages. [^1]

## Search Example

A service completes 1,000 requests per second, with p50 latency 20 ms and p99 latency 200 ms.

These numbers describe different properties. p99 means approximately 99% of observations are at or below that value; it is not the maximum.

A proposed experiment: increase retrieval candidates from 100 to 1,000, then measure both [[Search Evaluation|quality]] and the serving distribution at the same offered load.

Do not infer latency from candidate count alone.

## Measurement Checklist

- Report requests/second, p50/p95/p99, error rate, and timeout rate.
- Include queueing and dependency time when measuring user-visible latency.
- Separate successful and failed-request latency so fast failures do not look healthy.
- Track offered load as well as completed throughput.
- Do not add stage p99 values to claim an end-to-end p99; percentile aggregation requires the underlying observations or a valid model. [^1]

Aim for useful throughput within quality, latency, and reliability constraints rather than maximising one quantity independently.

## Relate Latency to Work in Progress

For a stable system with finite long-run averages, define:

- $L$: average requests in the system.
- $\lambda$: effective arrival rate.
- $W$: average time in the system.

Little's law relates these quantities:[^little]

$$
L=\lambda W.
$$

Use the same population and boundary in all three quantities.

For an admitted request stream in steady state, effective arrivals match departures.

Include time spent waiting if $L$ counts both waiting and executing requests.

A queue-only boundary instead relates waiting requests to waiting time.

This is a relation between averages, not between throughput and p99.

### Convert the units

**Inputs:** 1,000 completed requests/second and mean latency 50 ms.

Convert latency to seconds before multiplying:

$$
L=1000\times0.050=50\text{ requests}.
$$

At the same throughput but mean latency 200 ms:

$$
L=1000\times0.200=200\text{ requests}.
$$

This does not mean 200 CPU cores are required: requests may be waiting on I/O, sharing processors, or queued. It also does not prove that allowing 200 concurrent requests will deliver the target throughput.

## Find the Sustainable Operating Point

Compare offered requests, accepted requests, completions, errors, and queue depth over the same interval. A service can report steady completion throughput while its queue grows without bound. Increasing concurrency may initially improve utilisation, then increase contention and latency after a bottleneck saturates.

A useful load comparison holds the query mix, candidate depth, cache state, payload sizes, and deployed versions as steady as practical. Report the range where quality and latency targets are met, including behaviour when demand exceeds that range.

## Related Notes

- [[Monitoring - MLOPS|Monitoring]] — Observability across the pipeline.
- [[Tail Latency]] — Fan-out amplification and tail-tolerant techniques.
- [[Rust and Go]] and [[Go Language|Go]] — Execution costs and runtime design.

## References & Useful Links

[^1]: [Google SRE: Monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/) — Latency distributions, traffic, errors, and saturation.

[^little]: [MIT 1.041/1.200: Queuing models, Spring 2026](https://web.mit.edu/1.041/www/lectures/L8-queuing-models-2026sp.pdf) — Little's law, system boundaries, and stable long-run averages.
