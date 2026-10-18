---
tags:
  - leetcode
problem_number: 684
difficulty: "Medium"
pattern: "Graphs"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = (find(n1), find(n2))
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
```

## Complexity

$O(n\alpha(n))$ amortized time and $O(n)$ space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Identify the extra edge that creates a cycle in an undirected tree plus one edge.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc684|LeetCode — LC 684]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Create a disjoint-set structure for the labeled vertices.
2. Process edges in input order, finding both endpoint roots.
3. If roots are equal, return that edge; otherwise union the components using size and path compression.

## Why It Works

An edge creates a cycle exactly when its endpoints already have a connecting path.

## Worked Example

**Illustrative input:** Edges `[[1, 2], [1, 3], [2, 3]]`.

**Trace:** The first two edges connect all three vertices; the last joins vertices already connected.

**Result:** Return `[2, 3]`.

## Common Pitfalls

The problem's tree-plus-one-edge contract matters. The detected closing edge satisfies its last-in-input removal tie rule.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc684|Coding Practice Index — Redundant Connection]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 684](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0684-redundant-connection.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
