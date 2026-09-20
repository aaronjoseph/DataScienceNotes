# System Design

#search-eng

## Begin with Requirements

State the workload, data size and growth, latency and availability targets, correctness requirements, and cost constraints before selecting technology. “SQL for structured data, NoSQL for unstructured data” is too coarse: compare access patterns, transactions, indexes, consistency, and operations.

## Components and Tradeoffs

- **Caching:** saves repeated work but needs key design, invalidation, bounded memory, and a staleness policy.
- **Queues:** absorb bursts and decouple stages; sustained input above service capacity still grows backlog. Bound queues and define overload behaviour.
- **Replication:** maintains copies for resilience or reads, depending on the system; replication lag and failover semantics matter.
- **[[Database Sharding|Sharding]]:** distributes partitions; hot keys, fan-out, rebalancing, and cross-partition operations add cost.
- **Timeouts and retries:** use deadlines, bounded retries, backoff, and idempotency. Retrying overload can amplify it.

## Search Request Example

A query passes through [[Query Understanding]], retrieval, filtering, [[Search Ranking|ranking]], and response construction. Decide where eligibility is enforced and what happens if one retrieval source times out. A fallback changes candidate coverage, so record that outcome in [[Monitoring - MLOPS|Monitoring]].

Index updates take a separate path from serving requests. Define the freshness target and correctness checks in [[Index Updates]]. Capacity planning must include indexing and background work, not only query traffic.

## Exercise

Suppose incoming traffic is 120 requests/s and capacity is 100 requests/s. Under this simple constant-rate model, backlog grows by 20 requests/s. Explain why adding a queue does not close the capacity gap. Then propose measured scaling, load shedding, or bounded degradation. Connect this to [[Latency vs Throughput]] and [[Big O]].

## References & Useful Links

- [Google SRE overload](https://sre.google/sre-book/handling-overload/) — Queues, retries, and overload handling.
- [Azure sharding pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/sharding) — Partitioning tradeoffs.
