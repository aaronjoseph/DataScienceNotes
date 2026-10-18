---
tags:
  - leetcode
problem_number: 323
difficulty: "Medium"
pattern: "Graphs"
languages:
  - Python
---

Count connected components in an undirected graph. Merge sets when an edge joins different components.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc323|LeetCode — LC 323]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Initialize a disjoint-set parent and size for every vertex; start the component count at n.
2. For each edge, find both roots using path compression.
3. If roots differ, attach the smaller component to the larger and decrement the count.

## Why It Works

Each successful union merges exactly two previously separate components, reducing their number by one.

## Worked Example

**Illustrative input:** `n = 5`, edges `[[0, 1], [1, 2], [3, 4]]`.

**Trace:** Three successful unions reduce five initial components to two.

**Result:** Return `2`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent, size = list(range(n)), [1] * n
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        components = n
        for first, second in edges:
            a, b = find(first), find(second)
            if a == b:
                continue
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
            components -= 1
        return components
```

## Complexity

$O((V+E)\alpha(V))$ amortized time and $O(V)$ extra space with path compression and union by size. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Include isolated vertices in the initial count. Do not decrement the count for an edge already inside one component.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc323|Coding Practice Index — Number of Connected Components In An Undirected Graph]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 323](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0323-number-of-connected-components-in-an-undirected-graph.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
