---
tags:
  - leetcode
  - linked-list
problem_number: 146
difficulty: "Medium"
pattern: "Linked List"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.[^implementation]

```python
from __future__ import annotations

class Node:

    def __init__(self, key, val):
        self.key, self.val = (key, val)
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = (Node(0, 0), Node(0, 0))
        self.left.next, self.right.prev = (self.right, self.left)

    def remove(self, node):
        prev, nxt = (node.prev, node.next)
        prev.next, nxt.prev = (nxt, prev)

    def insert(self, node):
        prev, nxt = (self.right.prev, self.right)
        prev.next = nxt.prev = node
        node.next, node.prev = (nxt, prev)

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
```

## Complexity

- **Time:** $O(1)$ expected time for both `get` and `put` (one hash-map lookup plus constant-time doubly linked list pointer updates).
- **Auxiliary space:** $O(C)$ for capacity $C$, storing at most $C$ entries in `self.cache` and $C + 2$ nodes (including the `left` and `right` sentinels) in the doubly linked list.

## Algorithm at a glance

![[Attachements/LeetCode/LC0146 - LRU Cache.png|700]]

## Overview

Design a fixed-capacity Least Recently Used (LRU) cache supporting $O(1)$ `get(key)` and `put(key, value)`, evicting the least recently accessed key when capacity is exceeded.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc146|LeetCode — LC 146]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## Key Concepts

### Why Both a Hash Map and a Doubly Linked List Are Needed

- A **hash map** (`key → Node`) gives $O(1)$ lookup by key, but cannot track recency order or find the oldest entry in $O(1)$.
- A **doubly linked list** maintains recency order (least recent near `self.left`, most recent near `self.right`) and supports $O(1)$ deletion from the middle and $O(1)$ insertion at the tail once you hold the node pointer.
- **Sentinel nodes (`left`, `right`):** Eliminate all `None` checks when removing the only node, removing the LRU head, or inserting into an empty list.
- **Storing `key` inside `Node`:** Required so that when evicting `lru = self.left.next`, you can run `del self.cache[lru.key]` in $O(1)$ time.

## How to Solve

1. Initialise `self.cache = {}` and connect two sentinel nodes `self.left <-> self.right`.
2. Implement two $O(1)$ list helpers:
   - `remove(node)`: splice `node` out by linking `node.prev` and `node.next` to each other.
   - `insert(node)`: place `node` immediately before `self.right` (the most-recent end).
3. On `get(key)`: if `key` is in `self.cache`, call `remove` then `insert` to mark it most recent, and return `node.val`; otherwise return `-1`.
4. On `put(key, value)`:
   - If `key` already exists, `remove` its old node first.
   - Create `Node(key, value)`, store it in `self.cache[key]`, and `insert` it at the most-recent end.
   - If `len(self.cache) > self.cap`, evict `lru = self.left.next` from both the list (`self.remove(lru)`) and the map (`del self.cache[lru.key]`).

## Why It Works

Every `get` hit and every `put` moves the accessed key to the `right` sentinel, so the list is always strictly ordered from least recently used (`left.next`) to most recently used (`right.prev`). Because `self.cache` and the doubly linked list always contain the exact same set of keys, eviction removes the oldest entry from both structures in $O(1)$ time.

## Worked Example

**Inputs:** `LRUCache(2)`, operations: `put(1, 1)`, `put(2, 2)`, `get(1)`, `put(3, 3)`, `get(2)`.

1. **`put(1, 1)`:** List: `left <-> (1:1) <-> right`. Cache keys: `{1}`.
2. **`put(2, 2)`:** List: `left <-> (1:1) <-> (2:2) <-> right`. Cache keys: `{1, 2}`.
3. **`get(1)`:** Returns `1`; moves `(1:1)` to the right end. List: `left <-> (2:2) <-> (1:1) <-> right`.
4. **`put(3, 3)`:** Inserts `(3:3)` at right end; size becomes `3 > 2`, so evict `left.next = (2:2)` from list and cache. List: `left <-> (1:1) <-> (3:3) <-> right`. Cache keys: `{1, 3}`.
5. **`get(2)`:** Key `2` is absent; returns `-1`.

**Outcome:** `get(1)` returns `1`, `put(3, 3)` evicts key `2`, and `get(2)` returns `-1`.

## Common Pitfalls

- **Forgetting to store `key` on `Node`:** Without `lru.key`, you cannot delete the evicted entry from `self.cache` in $O(1)$ time.
- **Not removing the old node on an existing-key `put`:** Overwriting `self.cache[key]` without calling `self.remove(old_node)` leaves a stale duplicate node in the list, which later corrupts evictions.
- **Evicting from the list but forgetting `del self.cache[lru.key]` (or vice versa):** Leaves the map and list out of sync.
- **Treating `put` of an existing key as non-access:** Updating an existing key must refresh its recency to the most-recent end.

## Related Notes

- [[LeetCode/Linked List/Copy List With Random Pointer|Copy List With Random Pointer]] — Another hash-map-plus-linked-list problem.
- [[Search Caching]] — Real-world caching policies (including LRU) in search serving systems.
- [[Job Interviews/Coding Practice Index#^lc146|Coding Practice Index — LRU Cache]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 146](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0146-lru-cache.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
