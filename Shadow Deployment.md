---
note_type: concept
search_stage: serving
---

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
2. Instrument both versions to record outputs with a shared request ID. Traffic mirroring alone does not retain the discarded shadow response for comparison.
3. Compare them offline: equality, overlap, rank agreement, error rates, and latency distributions.
4. Investigate differences, fix them, and repeat before a [[Canary Deployment|canary]] or full rollout.

## Search Example: Migration Parity

When a search pipeline is reimplemented, for example from Python to Rust, shadowing lets both versions process identical queries.

- Compare per-stage candidate IDs and final result lists, not only status codes.
- Use overlap@k and [[Kendall's Tau]] on shared items to quantify ranking differences.
- Expect benign differences from tie-breaking and floating-point order; make ordering deterministic before comparing. See [[Search Architecture#Migration and Parity Checks|parity checks]].
- Verify which build each side is running before treating a difference as a defect.

## Build a Comparable Request Record

For each mirrored request, keep the input and eligibility context, both build identifiers, model/configuration versions, index versions, per-stage item IDs, scores, timings, and terminal status. A comparison with missing shadow results must be reported as missing or failed, not silently removed from the denominator.

First check whether both sides evaluated the same task. Then compare in order:

1. Parsed intent and hard constraints.
2. Eligible candidates per source, including source-specific caps.
3. The deduplicated union and selected reranking set.
4. Features, score sources, and raw model outputs.
5. Business rules and final ordering.

Stop at the first unexplained difference. A final ranking change caused by a missing candidate should be investigated at retrieval before adjusting ranking weights.

### Coverage changes the interpretation

**Inputs**

- Mirrored requests: 1,000.
- Requests completed on both sides: 900.
- Completed pairs with identical top-10 lists: 828.

**Agreement among completed pairs:**

$$
\frac{828}{900}=92\%
$$

**Paired completion rate:**

$$
\frac{900}{1000}=90\%
$$

The remaining 100 requests are unassessed for list equality. Report both rates and the missing-result reasons.

For two complete lists of exactly $k$ distinct IDs, overlap@k can be defined as $|A_k\cap B_k|/k$.

It measures membership, not order.

If a list has fewer than $k$ items, declare how underfilled lists affect the metric.

Rank correlation restricted to shared items cannot detect the quality of missing items.

Shadow agreement supports migration confidence, but agreement with the incumbent is not proof of relevance. Deliberate improvements may differ and still need judgments or a user-facing experiment.

## Limitations and Pitfalls

- **Side effects.** A shadow must not write orders, publish events, charge payments, or pollute caches and analytics. Stub or isolate writes.
- **Load.** Mirroring all traffic can roughly double shared dependency work when both versions perform similar operations; different fan-out or cache behaviour can change that factor. Start with a bounded sample and measure actual amplification.
- **No user feedback.** Users never see the shadow's results, so shadowing cannot measure clicks or conversions. Use [[Interleaving]] or an [[AB Testing|A/B test]] for that.
- **Divergent state.** If the shadow reads different caches or configuration, differences reflect the environment rather than the code.

## Exercise

A shadow ranker matches production's top 10 exactly for 92% of queries.

List three checks you would run on the other 8% before deciding whether each difference is a defect, a benign tie, or an improvement.

## Search Connections

- [[Search Engineering]] — Learning map and review status.
- [[Latency vs Throughput|Latency and throughput]]
- [[Information Retrieval|Retrieval pipeline]]
- [[Deployment Patterns]] — Other rollout strategies.

## References & Useful Links

[^1]: [Istio: Mirroring](https://istio.io/latest/docs/tasks/traffic-management/mirroring/) — Traffic mirroring (shadowing), mirror percentages, the `-shadow` host suffix, and discarded "fire and forget" responses. Accessed 23 September 2026.
