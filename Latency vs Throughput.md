# Latency vs Throughput

#search-eng

## Overview

**Latency** is elapsed time for an operation; **throughput** is the number completed per unit time. Define the boundary: end-to-end request latency is different from model inference time. Distributions matter because slow requests can be hidden by averages. [^1]

## Search Example

A service completes 1,000 requests per second, with p50 latency 20 ms and p99 latency 200 ms. These numbers describe different properties. p99 means approximately 99% of observations are at or below that value; it is not the maximum.

A proposed experiment: increase retrieval candidates from 100 to 1,000, then measure both [[Search Evaluation|quality]] and the serving distribution at the same offered load. Do not infer latency from candidate count alone.

## Measurement Checklist

- Report requests/second, p50/p95/p99, error rate, and timeout rate.
- Include queueing and dependency time when measuring user-visible latency.
- Separate successful and failed-request latency so fast failures do not look healthy.
- Track offered load as well as completed throughput.
- Do not add stage p99 values to claim an end-to-end p99; percentile aggregation requires the underlying observations or a valid model. [^1]

Aim for useful throughput within quality, latency, and reliability constraints rather than maximising one quantity independently.

## Related Notes

- [[Monitoring - MLOPS|Monitoring]] — Observability across the pipeline.
- [[Rust and Go]] and [[Go Language|Go]] — Execution costs and runtime design.

## References & Useful Links

[^1]: [Google SRE: Monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/) — Latency distributions, traffic, errors, and saturation.
