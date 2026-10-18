---
tags:
  - leetcode
problem_number: 261
difficulty: "Medium"
pattern: "Graphs"
languages:
  - Python
---

Check whether an undirected graph is a tree: connected and acyclic.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc261|LeetCode — LC 261]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Build an adjacency list and start a depth-first search from vertex zero.
2. Track the parent so the immediate reverse of a tree edge is skipped.
3. Reject a revisit through any other edge, and finally require every vertex to have been reached.

## Why It Works

The search detects cycles, while the final visited count independently checks connectivity.

## Worked Example

**Illustrative input:** `n = 4`, edges `[[0, 1], [1, 2]]`.

**Trace:** The component containing zero has no cycle, but vertex 3 is unreachable.

**Result:** Return `False`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def validTree(self, n, edges):
        if not n:
            return True
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        return dfs(0, -1) and n == len(visit)
```

## Complexity

$O(V+E)$ time and $O(V+E)$ space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

The problem uses a nonempty simple undirected graph. Parent-edge handling and connectivity are both necessary.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc261|Coding Practice Index — Graph Valid Tree]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 261](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0261-graph-valid-tree.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
