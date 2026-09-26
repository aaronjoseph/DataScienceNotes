# Shadow Deployment

#search-eng

## Overview

In a shadow deployment, a new version receives a copy of real production traffic but its outputs are **not** served. The existing version still answers every user. Engineers compare the two versions' outputs, errors, and latency, which exposes the new version to realistic inputs with little user risk. Istio describes the underlying traffic mirroring as sending a copy of live traffic to a mirrored service out of band of the primary request path; mirrored responses are discarded.[^1]

## Two Meanings

- **Human-in-the-loop shadow mode.** A human provides the response while an ML model performs the same task without making any decision. Comparing the two measures model performance relative to human performance before automating. It is the step after "human only" in the [[Deployment - MLOPs#Spectrum of Automation|spectrum of automation]].
- **Service shadowing.** A new service version receives mirrored requests while the current version serves them. It is used for rewrites, migrations, and capacity testing.

Both share the key property: the new decision-maker's output does not reach the user.

## How It Works

1. Mirror all or a percentage of requests to the shadow version. Istio supports a mirror percentage and marks mirrored requests by appending `-shadow` to the Host or Authority header.[^1]
2. Record both versions' outputs with a shared request ID.
3. Compare them offline: equality, overlap, rank agreement, error rates, and latency distributions.
4. Investigate differences, fix them, and repeat before a [[Canary Deployment|canary]] or full rollout.

## Search Example: Migration Parity

When a search pipeline is reimplemented, for example from Python to Rust, shadowing lets both versions process identical queries.

- Compare per-stage candidate IDs and final result lists, not only status codes.
- Use overlap@k and [[Kendall's Tau]] on shared items to quantify ranking differences.
- Expect benign differences from tie-breaking and floating-point order; make ordering deterministic before comparing. See [[Search Architecture#Migration and Parity Checks|parity checks]].
- Verify which build each side is running before treating a difference as a defect.

## Limitations and Pitfalls

- **Side effects.** A shadow must not write orders, publish events, charge payments, or pollute caches and analytics. Stub or isolate writes.
- **Load.** Mirroring doubles work on shared dependencies such as databases and model endpoints. Mirror a percentage first.
- **No user feedback.** Users never see the shadow's results, so shadowing cannot measure clicks or conversions. Use [[Interleaving]] or an [[AB Testing|A/B test]] for that.
- **Divergent state.** If the shadow reads different caches or configuration, differences reflect the environment rather than the code.

## Exercise

A shadow ranker matches production's top 10 exactly for 92% of queries. List three checks you would run on the other 8% before deciding whether each difference is a defect, a benign tie, or an improvement.

## Search Connections

- [[Search Engineering]] — Learning map and review status.
- [[Latency vs Throughput|Latency and throughput]]
- [[Information Retrieval|Retrieval pipeline]]
- [[Deployment Patterns]] — Other rollout strategies.

## References & Useful Links

[^1]: [Istio: Mirroring](https://istio.io/latest/docs/tasks/traffic-management/mirroring/) — Traffic mirroring (shadowing), mirror percentages, the `-shadow` host suffix, and discarded "fire and forget" responses. Accessed 23 September 2026.
