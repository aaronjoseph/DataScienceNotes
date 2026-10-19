---
note_type: concept
search_stage: serving
tags:
  - system-design
  - search-eng
---

## Core idea

**Vector search scales by spreading stored vectors, reducing the work per search, and sharing queries across replicas.** These solve different bottlenecks. [[System_Design/Consistent Hashing|Consistent hashing]] helps with placement; it does not guarantee that a shard will never be overloaded.

This note answers the follow-up from [[System_Design/Consistent Hashing|Consistent Hashing]]. It complements the broader [[System_Design/Vector Database|Vector Database]] design and the algorithm overview in [[Approximate Nearest Neighbours]]. Vendor examples below were checked against official documentation on 19 October 2026; numerical examples are illustrative, not benchmarks.

## Start with a product-search example

Suppose six product vectors are distributed by their IDs:

| Logical shard | Stored products |
|---|---|
| S0 | Hiking boot A, kettle A |
| S1 | Jacket A, kettle B |
| S2 | Hiking boot B, jacket B |

A query for “waterproof hiking boots” can have good neighbours on **S0 and S2**. Hashing that query to S0 would miss boot B. An ID hash spreads ownership without preserving semantic similarity.

With no safe way to exclude a shard, search all three in parallel and merge their candidates. Qdrant documents consistent hashing for automatic sharding and distributed search fan-out.[^qdrant-shards] This is one architecture, not a rule that every vector database uses the same hash ring.

## Infographic

![[Attachements/Vector Search Scaling.png|700]]

Illustrative architecture: the ring assigns IDs to logical shards; a placement map locates their replicas on physical nodes. In the search panel, coloured replicas serve this query and grey replicas are alternatives. The hot-shard rates assume ideal read balancing. Local graphs stand for local HNSW indexes; an engine may maintain several indexes or segments per shard.

## Keep four meanings separate

- **Machine cluster:** servers cooperating to run the database.
- **Logical shard:** an ownership partition containing part of the collection.
- **Replica:** another copy of a shard, usable for availability and read capacity.
- **Vector region or IVF list:** nearby embeddings grouped for search. It need not correspond to a machine or shard.

Weaviate, for example, describes each shard as containing its own vector index, inverted indexes, and object store.[^weaviate] A popular region *inside* that index is not automatically a separate remote server.

## Where consistent hashing fits

In an ID-based design, ingestion chooses a logical shard using the vector’s stable ID; the shard map then identifies its physical replica placements. Similar vectors with unrelated IDs can land on different shards.

Qdrant’s automatic mode uses consistent hashing; its user-defined mode allows targeting chosen shard groups, such as tenant or region groups.[^qdrant-shards] Weaviate documents UUID-based hashing for its ordinary sharding path.[^weaviate] Hashing for placement differs from locality-sensitive hashing, which aims to preserve a notion of similarity.

Virtual tokens, as explained in [[System_Design/Consistent Hashing#Why virtual nodes help|Consistent Hashing]], can smooth ownership imbalance. They do not add CPU or divide a popular key’s traffic. Also distinguish **adding a machine**, **moving an existing shard replica**, and **splitting a logical shard**: these are different operations, with engine-specific support. A new empty machine provides no serving benefit until useful data or replicas are placed there.

## How a distributed query runs

For the three-shard example:

1. A coordinator receives the query vector, filters, and requested result count $k$.
2. It identifies relevant shards. With ID-based placement and an unrestricted query, that means all three.
3. It chooses a healthy, sufficiently fresh replica of each shard and sends searches in parallel.
4. Each replica searches its local index or segments and returns candidates.
5. The coordinator merges candidates using comparable scores and returns the global result.

Qdrant’s default search reads one replica per shard; stronger read consistency or delayed extra requests can query more replicas.[^qdrant-reads][^consistency] Replication usually distributes **different queries** across equivalent copies; it does not require searching every copy for every query.

For exact local search, local top $k$ is sufficient for global top $k$ under a common metric, snapshot, eligibility rule, and tie-break. With ANN, missed local neighbours remain missed globally. Later filtering, grouping, or reranking can also require deeper candidate pools; see [[System_Design/Vector Database#Query execution, candidates, and reranking|Query execution and merging]].

## How KNN, HNSW, and IVF reduce or distribute work

### Exact KNN: parallelise a complete search

Here, **k-nearest-neighbour (KNN) search** means finding the closest vectors, rather than the classification or regression procedure in [[KNN]]. A flat exact search compares the query with every eligible vector. Sharding divides that work; batching and GPUs can accelerate it.[^indexes][^gpu]

For $N$ vectors of dimension $d$, the distance work for an unfiltered scan is $O(Nd)$. Dividing it across machines does not remove the total distance work. Real speedup is limited by memory bandwidth, networking, and the slowest required shard. Faiss explicitly distinguishes sharding a dataset across GPUs from replicating it for throughput.[^gpu]

### HNSW: navigate a graph inside each local index

**Hierarchical Navigable Small World (HNSW)** search starts in sparse upper graph layers, moves toward promising vectors, then explores a more detailed neighbourhood below. This avoids a full scan in useful operating regimes, while allowing missed neighbours.[^hnsw]

In the illustrated sharded design, HNSW operates locally. It does not discover the correct remote shard or balance requests across servers. Many queries may visit the same local graph entry point without making that point a separate network service.

Increasing `efSearch` widens local exploration, typically spending more work for better neighbour recall. `M` and `efConstruction` affect graph construction and memory.[^indexes] There is no universal latency or logarithmic-search guarantee for every dataset, filter, and load. See [[System_Design/Vector Database#ANN approach 1: HNSW|HNSW construction and tuning]].

### IVF: search selected vector regions

An **inverted file (IVF)** index assigns vectors to lists around coarse centroids; `nprobe` controls how many lists a query searches. Unvisited lists can contain true neighbours. More probing increases coverage and work.[^indexes]

This selection often happens *within each shard*. Only a design that deliberately maps semantic partitions to machines and routes by them turns popular vector regions into selectively hot remote partitions. An approximate shard router then adds a separate source of recall loss. Skipping a shard based on proven tenant ownership differs from guessing that its vectors are too distant to matter.

## Why some shards or regions still get overloaded

Your concern applies differently to two layouts:

- **Hash shards with all-shard search:** even repeated “hiking boots” queries reach every shard. Popular results do not alone imply one hot storage shard; per-query graph work, filters, or hardware can still differ.
- **Tenant or semantic routing:** many queries can target the same tenant or region. Balanced vector counts do not imply balanced traffic or query cost.

The following are design responses to investigate, rather than automatic guarantees of consistent hashing:

| Observed bottleneck | Response to consider | Main cost or limit |
|---|---|---|
| Too much data on one node | Move replicas; split or rebalance shards | Transfer and index-build work |
| Read-heavy shard | Add replicas and distribute reads | Extra memory, storage, and writes |
| One popular tenant or routed region | Isolate it; add replicas or subdivide its data | Routing complexity and possible extra fan-out |
| Expensive local ANN queries | Tune effort; index filters; cache repeated work | Recall and freshness tradeoffs |
| Sustained demand above capacity | Quotas, bounded queues, admission control | Explicit throttling or rejection |

Weaviate documents moving shard replicas to rebalance load and distinguishes sharding for dataset size from replication for query throughput.[^weaviate] Qdrant likewise describes replicas sharing reads and notes their replication cost.[^qdrant-reads] Neither establishes a universal linear speedup.

Dense or duplicated vectors can also make an index inefficient: Faiss documents difficulties for both IVF and HNSW with large numbers of identical or near-identical vectors.[^faq] That is an index-work problem as well as any traffic-placement problem. De-duplicate only when identity and retrieval semantics allow it.

Caching needs the full query context, filters, model version, and freshness policy; see [[Search Caching]]. A cheaper cached result must still respect eligibility.

## Worked example: more shards versus more replicas

**Inputs:** 3 logical shards, 600 client queries/s, 2 replicas per shard, all-shard search, and one chosen replica per shard per query. Assume ideal balancing, equivalent hardware, no retries, and no extra consistency reads.

**1. Total shard searches per second**

$$
Q_{\mathrm{total}} = 600 \times 3 = 1{,}800
$$

Every logical shard receives 600 searches/s, even if most users ask about boots.

**2. Average searches per replica**

$$
Q_{\mathrm{replica}} = \frac{600}{2} = 300
$$

Two copies share one shard’s reads. They each store that shard’s data.

**3. Increase to 6 shards, keeping 2 replicas per shard**

$$
Q_{\mathrm{total,new}} = 600 \times 6 = 3{,}600
$$

Each shard still receives 600 searches/s. Balanced shards hold less data, which may reduce local work, but fan-out doubles. This alone does not establish higher throughput.

**4. Instead increase to 3 replicas per shard**

$$
Q_{\mathrm{replica,new}} = \frac{600}{3} = 200
$$

This shares reads across more copies, provided hardware and routing support it. It costs additional replicated storage and write work. Losing one of those copies restores the ideal average to 300 searches/s on each survivor.

## What to measure before scaling

Compare per-shard bytes, queries/s, CPU, queue time, local search work, and p95/p99 latency. Slice by tenant, filter, and popular query region. Equal queries/s can hide very different request costs.

Measure ANN neighbour recall against exact search over the **same vectors, metric, filters, IDs, and snapshot**, separately from human relevance. Include fan-out, missing-shard outcomes, updates, and a failed replica in the workload; see [[Approximate Nearest Neighbours#Build a Fair Exact Baseline|Exact-baseline rules]], [[Filtered Vector Search]], and [[System_Design/Vector Database#Benchmark against exact KNN|Service benchmarking]].

**Exercise:** 80% of requests target one tenant. Explain why merely moving its only shard to a new machine may relocate the bottleneck, then compare replication with splitting that tenant across several shards. State the effect on read capacity, write cost, and fan-out.

## References & Useful Links

[^qdrant-shards]: [Qdrant — Horizontal Scaling](https://qdrant.tech/documentation/scaling/horizontal-scaling/) — Start here for a concrete vector database using consistent hashing, user-defined sharding, query fan-out, and shard replication.
[^weaviate]: [Weaviate — Horizontal Scaling](https://docs.weaviate.io/weaviate/concepts/cluster) — Shard-local indexes, UUID-based placement, replica movement, and the different motivations for sharding and replication.
[^qdrant-reads]: [Qdrant — Low-Latency Search](https://qdrant.tech/documentation/search/low-latency-search/) — Read load across replicas, the default one-replica-per-shard path, and delayed fan-out for slow responses.
[^consistency]: [Qdrant — Consistency Guarantees](https://qdrant.tech/documentation/scaling/consistency-guarantees/) — Why stronger read consistency can contact additional replicas and increase work.
[^hnsw]: [Yu. A. Malkov and D. A. Yashunin — Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs](https://arxiv.org/abs/1603.09320) — Original HNSW paper, submitted in 2016; explains the graph hierarchy and search mechanics.
[^indexes]: [Faiss — Faiss Indexes](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes) — Flat exact search, HNSW parameters, and IVF lists and probing. Read this after separating shard routing from local index search.
[^gpu]: [Faiss — Faiss on the GPU](https://github.com/facebookresearch/faiss/wiki/Faiss-on-the-GPU) — Concrete parallel-search implementations and the throughput versus capacity tradeoff between replicas and shards.
[^faq]: [Faiss — FAQ: Searching Duplicate Vectors Is Slow](https://github.com/facebookresearch/faiss/wiki/FAQ#searching-duplicate-vectors-is-slow) — Explains why concentrated or repeated vectors can make IVF and HNSW costly even before distributed routing is considered.
