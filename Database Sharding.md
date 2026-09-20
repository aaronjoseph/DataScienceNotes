# Database Sharding

#search-eng

## Core Idea

Sharding distributes data partitions across storage or compute nodes, commonly by rows/documents using a shard key. Vertical partitioning splits attributes; replication stores copies. These solve different problems and can be combined.

## Design Choices

Range partitioning can support locality and ordered scans but concentrate hot ranges. Hash partitioning can spread keys while making range access harder. Directory-based routing adds a mapping layer. Choose using measured access patterns and expected growth.

A shard key determines which operations route to one partition and which must fan out. Sharding does not itself make data highly available: replication, failure detection, and recovery policies provide resilience. Rebalancing consumes resources and can temporarily affect latency.

## Search Implications

A coordinator may query multiple shards and merge their local results. Network fan-out, slow shards, filtering, and local candidate limits affect the final list. In a simple global top-k with comparable scores and no later filtering, each shard's top-k is sufficient; additional filters, rescoring, or different score statistics complicate that guarantee. Diagnose partial results explicitly.

## Exercise

Two shards return `[A:10, B:8]` and `[C:9, D:7]`. Global top two are A and C. If A is later found ineligible and only local top-one results were fetched, B is unavailable. Explain why candidate depth and filter placement belong in the correctness design.

See [[System Design]], [[Search Ranking]], [[Index Updates]], and [[Monitoring - MLOPS|Monitoring]].

## References & Useful Links

- [Azure sharding pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/sharding) — Routing, partitioning, and operational tradeoffs.
