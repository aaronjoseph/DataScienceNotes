---
tags:
  - leetcode
problem_number: 778
difficulty: "Hard"
pattern: "Advanced Graphs"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
import heapq

class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = (r + dr, c + dc)
                if neiR < 0 or neiC < 0 or neiR == N or (neiC == N) or ((neiR, neiC) in visit):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
```

## Complexity

$O(n^2\log(n+1))$ time and $O(n^2)$ space for an `n` by `n` grid. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Find the smallest water level allowing travel from the top-left to bottom-right cell. A path's cost is its greatest elevation.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc778|LeetCode — LC 778]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Push the starting cell with its elevation as the path cost.
2. Expand the lowest-cost frontier cell using a heap.
3. For each neighbor, use the larger of the current path cost and neighbor elevation; return when the destination is popped.

## Why It Works

This minimax form of Dijkstra finalizes the smallest possible maximum elevation needed to reach the destination.

## Worked Example

**Illustrative input:** `grid = [[0, 2], [1, 3]]`.

**Trace:** Either route must enter elevation 3 at the destination.

**Result:** Return `3`.

## Common Pitfalls

Include both endpoint elevations. This grid-specific implementation marks neighbors on insertion; do not generalize that shortcut to arbitrary weighted Dijkstra problems.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc778|Coding Practice Index — Swim In Rising Water]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 778](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0778-swim-in-rising-water.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
