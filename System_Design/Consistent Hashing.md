---
note_type: concept
search_stage: serving
tags:
  - system-design
  - search-eng
---

## Core idea

**Consistent hashing assigns keys to servers so that adding or removing a server changes only part of the assignment.** This is useful for distributed caches and [[Database Sharding|sharded storage]] whose membership changes.[^lecture]

Study companion for Alex Xu’s *System Design Interview*, Volume 1, Chapter 5, “Design Consistent Hashing”. The official chapter reference list confirms the topic.[^chapter] The full chapter was unavailable during preparation; these explanations use its linked primary sources and original examples, rather than claiming to reproduce every chapter detail.

Back to [[Action-Plan Kanban#System Design Backlog|System Design Backlog]].

## Start with three cache servers

Imagine product descriptions cached on servers A, B, and C. A request should find its cache owner without asking every server.

A simple approach hashes the product key and takes the remainder after division by the server count.[^lecture] Define $k$ as the key, $h$ as a stable hash function, and $n$ as the server count:

$$
\operatorname{serverIndex}(k) = h(k) \bmod n
$$

**Illustrative inputs:** a product key has hash value $10$, and server indices are A = 0, B = 1, C = 2; a new server D has index 3.

**Before adding D:**

$$
10 \bmod 3 = 1
$$

The request goes to B.

**After adding D:**

$$
10 \bmod 4 = 2
$$

The same key now goes to C. Changing the divisor can remap many keys, including between existing servers, producing cache misses or data transfers.[^lecture]

## Put servers and keys on a ring

Hash both into the same fixed space. Choose the first server clockwise from the key, wrapping around at the end.[^lecture] Here, a key exactly on a server position belongs to that server.

**Illustrative inputs:** positions run from 0 to 99; A is at 10, B at 40, C at 80. The key positions below are chosen for explanation, not computed hashes.

```text
Clockwise order, with wraparound:
0 → A:10 → B:40 → C:80 → 99 → 0
```

| Key position | First server clockwise | Owner |
|---|---|---|
| 5 | A at 10 | A |
| 25 | B at 40 | B |
| 55 | C at 80 | C |
| 90 | A at 10 after wrapping | A |

![[Attachements/Consistent Hashing - Ring Routing.png|700]]

### Add D at position 60

D takes positions greater than 40 through 60 from C. The key at 55 moves from C to D; the other three example keys stay put.

### Remove B from the original ring

Treat this as a separate case, without D. Positions greater than 10 through 40 now belong to C. The key at 25 changes owner; the other example keys stay put.

These are ownership changes. If B failed, assigning its range to C does not recover B’s stored values.

![[Attachements/Consistent Hashing - Server Changes.png|700]]

## Why virtual nodes help

One position per physical server can leave uneven intervals. **Virtual nodes** give each physical server multiple ring positions, such as `A:0`, `A:1`, and `A:2`. They are routing tokens, not extra machines or extra data copies. More positions reduce imbalance statistically; higher-capacity servers can receive more tokens.[^dynamo]

For example, A can own positions 10 and 65 while B owns 30 and 85. A key at 50 routes to A’s token at 65. Both A tokens still depend on the same physical machine.

The tradeoff is more routing metadata. Balanced key counts also do not guarantee balanced request rates: one popular key can dominate traffic.

![[Attachements/Consistent Hashing - Virtual Nodes.png|700]]

The ownership bars illustrate these token positions under uniformly hashed keys; they show key distribution, not a guarantee about request traffic.

## Implementation and operational boundaries

- **Lookup:** keep token positions sorted and find the successor of the key’s hash. With $T$ tokens, binary search takes $O(\log T)$ time; routing metadata takes $O(T)$ space. This describes lookup, not data-migration cost.[^lecture]
- **Replication:** separately place copies on distinct physical hosts. Consecutive virtual tokens may share a host, so they cannot automatically count as independent replicas.[^dynamo]
- **Membership:** routers need compatible ring membership, hash function, and key encoding; otherwise the same key can route differently.
- **Migration:** decide how reads and concurrent writes behave while ownership changes. A cache can refill misses; persistent storage needs a safe transfer and recovery policy.[^dynamo]
- **Hot keys:** consider replication, request coalescing, or workload-specific caching; adding tokens alone does not split one key’s traffic.

“Consistent” here describes stable placement across membership changes, not strong read/write consistency.

For search serving, this can route product IDs to metadata-cache owners. It does not determine relevance ranking or whether a query must fan out across index shards. Connect this distinction to [[Search Caching]] and [[Database Sharding]].

> [!question] How do vector databases scale search and handle hot shards?
> See [[System_Design/Vector Search Scaling|Vector Search Scaling]] for an infographic and worked examples connecting consistent hashing, HNSW, exact KNN, query fan-out, and hot-spot handling.

## Revision exercise

Using the original A:10, B:40, C:80 ring, add E at 95. Where do keys at 90 and 5 go? If E fails with no replica, can the ring recover a value stored only on E?

> [!example]- Check your answer
> Position 90 moves from A to E; position 5 stays on A. Removing E sends position 90 back to A, but routing alone cannot restore the lost value. A cache may reload it from the source; durable storage requires another recovery mechanism.

## References & Useful Links

[^chapter]: [Alex Xu / ByteByteGo — Volume 1 chapter references](https://github.com/alex-xu-system/bytebytego/blob/main/system_design_links.md#chapter-5-design-consistent-hashing) — Confirms Chapter 5’s topic and lists the Stanford lecture and Dynamo paper below. This is the reference list, not the chapter text.
[^lecture]: [Tim Roughgarden and Gregory Valiant — CS168 Lecture 1: Introduction and Consistent Hashing](https://theory.stanford.edu/~tim/s16/l/l1.pdf) — Modulo routing, clockwise ownership, membership changes, and successor lookup.
[^dynamo]: [Giuseppe DeCandia et al. — Dynamo: Amazon’s Highly Available Key-value Store (2007)](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf) — Sections 4.2–4.3 explain virtual nodes, capacity weighting, and replication on distinct physical hosts; the broader architecture separates placement from recovery and consistency.
