---
tags:
  - leetcode
problem_number: 146
difficulty: "Medium"
pattern: "Linked List"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

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

$O(1)$ expected time per operation and $O(C)$ space for capacity `C`. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Implement a least recently used cache with constant-time lookup, update, and eviction.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc146|LeetCode — LC 146]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Map each key to its node in a doubly linked list with sentinel endpoints.
2. On get or an existing-key put, detach that node and move it to the most-recent end.
3. On insertion beyond capacity, remove the least-recent real node and delete its map entry.

## Why It Works

The map locates nodes directly while list order records exactly the access recency needed for eviction.

## Worked Example

**Illustrative input:** Capacity 2: put keys 1 and 2, get 1, then put 3.

**Trace:** Accessing 1 moves it to the recent end, so insertion evicts 2.

**Result:** A later get of 2 returns `-1`.

## Common Pitfalls

Update both map and list on eviction. Existing-key writes count as use and must not leave duplicate nodes.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc146|Coding Practice Index — LRU Cache]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 146](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0146-lru-cache.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
