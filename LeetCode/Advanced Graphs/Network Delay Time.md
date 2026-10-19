---
tags:
  - leetcode
problem_number: 743
difficulty: "Medium"
pattern: "Advanced Graphs"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0743 - Network Delay Time.png|700]]

## Overview

Find when a signal starting at one graph node reaches every node along fastest directed paths.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc743|LeetCode — LC 743]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Build directed weighted adjacency lists.
2. Run Dijkstra's algorithm with a min heap of accumulated arrival times; finalize each node only once.
3. Track the greatest finalized arrival time; return it if all nodes were reached, otherwise -1.

## Why It Works

Nonnegative edge weights guarantee the next unvisited node removed from the heap has its shortest arrival time.

## Worked Example

**Illustrative input:** Edges `[[1, 2, 2], [2, 3, 3], [1, 3, 9]]`, start 1.

**Trace:** Node 3 is reached through node 2 in time 5, beating the direct edge.

**Result:** Return `5`.

## Common Pitfalls

Edges are directed and weights must be nonnegative. A visited flag belongs at heap removal, not at first discovery in a general weighted graph.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc743|Coding Practice Index — Network Delay Time]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
import collections
import heapq

class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1
```

## Complexity

$O(V+E\log(E+1))$ time and $O(V+E)$ storage for adjacency and lazy heap entries. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 743](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0743-network-delay-time.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
