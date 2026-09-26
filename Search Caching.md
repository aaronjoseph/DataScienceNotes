# Search Caching

#search-eng

## Overview

A search request repeats a lot of deterministic work: embedding the same popular queries, parsing the same query again on page two, fetching the same product metadata. Caching stores those results under a key so later requests can reuse them. It reduces average cost and load on dependencies, but it introduces **staleness**, **consistency**, and **failure-mode** questions that must be designed explicitly.

## What to Cache in a Search Pipeline

| Cached value | Key | Freshness concern | Stage |
|---|---|---|---|
| Query embedding (dense or sparse) | Normalised query + model version | Model change | [[Dense Retrieval]], [[SPLADE]] |
| Parsed entities and intent | Search or session ID | Query changes within a session | [[Named Entity Recognition]], [[Query Intent Classification]] |
| Query rewrite | Normalised original query | Curated list updates | [[Query Understanding#Query Rewriting\|Query rewriting]] |
| Relevance score | Query + item ID + item text version + model version | Item text or model change | [[Cross-Encoder]] |
| Product metadata | Item ID | Price, availability, engagement | Reranking features |
| Small reference maps | Loaded at startup or refreshed in the background | Refresh interval | Type ranks, location lookups |
| Result pages | Query + filters + user context + ranker version | Everything upstream | Response |

Caching full result pages is the riskiest option, because every upstream change and every personalisation input must be part of the key.

## Key Design

- **Normalise consistently.** Lowercase and trim before hashing if the computation treats those forms identically. Normalise the same way at read and write.
- **Version the key.** Include the model, schema, or ranker version, so a deployment cannot read values produced by an incompatible producer.
- **Include every input that changes the output.** Missing a filter or user context in the key serves one user's results to another.
- **Hash long keys** but keep the unhashed inputs in logs for debugging.

## Expiry and Invalidation in Redis

Redis semantics verified against the `EXPIRE` documentation on 23 September 2026:[^1]

- `EXPIRE key seconds` sets a time to live (TTL); the key is deleted after it expires.
- Overwriting a key with `SET` **clears** its TTL, so a naive overwrite can make a cached value permanent. Set the TTL in the same write, for example `SET key value EX 86400`.
- Commands that alter a value in place, such as `HSET`, `INCR`, or `LPUSH`, **keep** the existing TTL.
- Expired keys are removed both passively, when accessed, and actively, by periodic random sampling. Replicas wait for the primary's synthesised `DEL` instead of expiring keys independently.

Choose TTLs from the data's change rate. Session state might live for hours; product availability may need seconds or a live lookup instead of a cache.

## Failure Behaviour

- **Cache errors are misses, not request failures**, for optional caches. Log them and fall through to the source.
- **Fallback chains** such as cache, then database, should be explicit and observable. Record which source served each value.
- **Client timeouts are behaviour.** Client libraries have default connect and response timeouts. Changing a library, for example during a language migration, can silently change when fallbacks trigger. Set timeouts deliberately.
- **Isolate connections** for independent components when one component's heavy traffic could starve another's cache access.
- **Stampedes.** When a popular key expires, many requests may recompute it at once. Common mitigations include request coalescing and slightly randomised TTLs; measure before adding them.

## Worked Example

Query embedding takes 40 ms; a cache lookup takes 1 ms. With an 80% hit rate:

$$\text{mean latency}=0.8(1)+0.2(1+40)=9\text{ ms}.$$

The mean drops from about 40 ms to 9 ms. The p99 does not: 20% of requests still miss, so more than 1% of requests pay about 41 ms. Caching improves averages and throughput, but does not directly address tail latency unless essentially the whole working set is cached.[^2] See [[Tail Latency]].

## Limitations and Pitfalls

- **Stale relevance.** A cached score or embedding outlives an item update or model change if the key lacks a version.
- **Hidden personalisation.** Result caches without user context leak or mis-serve results.
- **Evaluation skew.** Offline replays that bypass caches may not reproduce production behaviour; record cache hits in logs.
- **Cache as source of truth.** Values with no TTL and no rebuild path become an unversioned database.

## Exercise

Design the cache key for a cross-encoder score. List every input that can change the score, then describe what happens after a model upgrade if one of them is missing from the key.

## References & Useful Links

[^1]: [Redis: EXPIRE](https://redis.io/docs/latest/commands/expire/) — TTL semantics, which commands clear or keep a timeout, passive and active expiry, and replication behaviour.
[^2]: [Dean and Barroso, "The Tail at Scale", CACM 2013](https://cacm.acm.org/research/the-tail-at-scale/) — Caching does not directly address tail latency unless the entire working set fits in cache.
