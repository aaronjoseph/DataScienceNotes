---
note_type: concept
search_stage: serving
---

# Tail Latency

#search-eng

## Overview

Tail latency is the slow end of the response-time distribution: p99, p99.9, and beyond. In systems that fan a request out to many components, rare slow components become common slow requests. Dean and Barroso argue that, as with fault tolerance, large services must build a predictably responsive whole out of less predictable parts.[^1]

Read [[Latency vs Throughput]] first for percentile basics.

## Fan-Out Amplification

If each of $n$ independent parallel calls is slow with probability $p$, and the request waits for all of them:

$$
P(\text{request slow})=1-(1-p)^n.
$$

- $p=0.01$, $n=100$: $1-0.99^{100}\approx0.634$. The paper reports that 63% of such requests take more than one second.[^1]
- $p=10^{-4}$, $n=2000$: $\approx0.181$, "almost one in five".[^1]
- A search request with 12 concurrent recall channels, each slow 1% of the time: $\approx0.114$.

The formula assumes independence. Shared causes such as a hot shard or garbage-collection pauses break that assumption.

The paper also reports a measured service in which the p99 for all leaf requests to finish was 140 ms, but waiting for only 95% of them took 70 ms. The slowest 5% accounted for half of the p99.[^1]

## Causes of Variability

Shared resources, background daemons, maintenance such as compaction and garbage collection, multi-layer queueing, power and thermal throttling, and SSD garbage collection.[^1]

## Tail-Tolerant Techniques

From Dean and Barroso:[^1]

- **Hedged requests:** send a second copy to another replica if the first is slow. Deferring the hedge until the p95 latency limits extra load to about 5%. In a BigTable benchmark, a 10 ms hedge reduced p99.9 from 1,800 ms to 74 ms with 2% more requests.
- **Tied requests:** enqueue on two servers that cancel each other when one starts.
- **Micro-partitions and selective replication:** many small partitions per machine for fine-grained load balancing; extra replicas for hot items.
- **Latency-induced probation:** temporarily exclude a slow server, while still probing it.
- **Good-enough results:** in large retrieval systems, return once enough of the corpus has been searched, and skip nonessential subsystems that miss the deadline.
- **Canary requests:** send a risky request to one or two leaves before fanning out to thousands.

The paper notes that caching does not directly address tail latency unless the whole working set fits in cache.[^1]

## Applying This to a Search Request

- **Run independent stages concurrently.** For example, run recall channels in parallel, and overlap feature lookups with relevance scoring. Latency then follows the slowest branch, so bound each branch.
- **Set per-dependency deadlines.** A timeout without a defined fallback is only a different error.
- **Classify dependencies.** Required ones fail fast with a typed error. Optional signals, such as query-level engagement features, degrade to neutral values and log the fallback.
- **Skip nonessential work.** Prompts, overviews, and analytics events can be dropped or sent asynchronously.
- **Check duplication semantics and capacity before hedging.** Read-only or idempotent work may still be expensive, consume quota, or overload a shared dependency. Writes require explicit duplicate suppression and a verified contract; operation names alone do not establish safety.
- **Keep liveness probes shallow.** Liveness probes that check dependencies can turn a transient dependency outage into a restart loop.
- **Measure per stage and end to end.** Stage percentiles cannot be added to obtain an end-to-end percentile.

## Follow the Critical Path

Suppose parsing precedes two parallel retrieval branches, followed by reranking and response assembly. Ignoring overlap elsewhere, the latency of one request is

$$
T=T_{\mathrm{parse}}+\max(T_{\mathrm{lexical}},T_{\mathrm{dense}})+T_{\mathrm{rerank}}+T_{\mathrm{response}}.
$$

**Stage times for this trace**

- Parsing: 10 ms.
- Lexical retrieval: 30 ms.
- Dense retrieval: 70 ms.
- Reranking: 40 ms.
- Response assembly: 5 ms.

The two retrieval branches run in parallel:

$$
T=10+\max(30,70)+40+5=125\text{ ms}.
$$

Adding both retrieval times would incorrectly give 155 ms.

This is a calculation for one trace; adding stage percentiles still does not produce an end-to-end percentile.

Carry the remaining request deadline forward. With a 200 ms total budget and 125 ms already elapsed, at most 75 ms remain, including response assembly and network time. Starting a dependency with its usual 200 ms timeout ignores the request budget.

> [!example]- Answer the fan-out exercise
> **Original configuration:** eight recall channels and one reranker.
>
> $$
> P(\text{at least one slow})=1-0.995^8\times0.99\approx4.89\%
> $$
>
> **Remove two recall channels:**
>
> $$
> P(\text{at least one slow})=1-0.995^6\times0.99\approx3.93\%
> $$
>
> **Instead, reduce only the reranker's slow probability to 0.001:**
>
> $$
> P(\text{at least one slow})=1-0.995^8\times0.999\approx4.03\%
> $$
>
> Under these assumptions, removing two channels produces the slightly lower probability. That does not establish the better product decision: it may remove relevant candidates, while hedging adds load. These are probabilities of at least one slow component, not a complete model of whether the end-to-end deadline is missed.

Track timeout and fallback rates alongside latency. Returning fewer candidates sooner can make the latency graph look better while lowering [[Candidate Generation|candidate coverage]] or [[NDCG]].

## Exercise

A request fans out to 8 recall channels (each slow 0.5% of the time), then 1 reranker call (slow 1%).

Assuming independence, what fraction of requests has at least one slow component?

Which single change reduces it most: removing two channels, or hedging the reranker so its slow rate becomes 0.1%?

## References & Useful Links

[^1]: [Dean and Barroso, "The Tail at Scale", Communications of the ACM 56(2), 2013](https://cacm.acm.org/research/the-tail-at-scale/) — Fan-out amplification, causes of variability, hedged and tied requests, good-enough results, canary requests, and the caching caveat. [Author-hosted full text](https://www.barroso.org/publications/TheTailAtScale.pdf).
