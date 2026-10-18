---
tags:
  - leetcode
problem_number: 1584
difficulty: "Medium"
pattern: "Advanced Graphs"
languages:
  - Python
---

Connect all points with minimum total Manhattan-distance cost using a minimum spanning tree.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc1584|LeetCode — LC 1584]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Build the complete weighted graph using each pair's Manhattan distance.
2. Run Prim's algorithm from any point, always accepting the cheapest edge to an unvisited point.
3. Add that edge cost and expose its outgoing edges until all points join the tree.

## Why It Works

The minimum edge crossing the visited/unvisited cut is safe to include in a minimum spanning tree.

## Worked Example

**Illustrative input:** Points `[[0, 0], [2, 0], [2, 2]]`.

**Trace:** Choose the two edges of cost 2 rather than the diagonal-distance edge of cost 4.

**Result:** Return total cost `4`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
import heapq

class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        res = 0
        visit = set()
        minH = [[0, 0]]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res
```

## Complexity

$O(n^2\log n)$ time and $O(n^2)$ storage for this explicit complete graph and heap. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Use Manhattan distance, not Euclidean distance. An implicit dense-Prim variant improves this to quadratic time and linear auxiliary space.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc1584|Coding Practice Index — Min Cost to Connect All Points]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 1584](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/1584-min-cost-to-connect-all-points.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
