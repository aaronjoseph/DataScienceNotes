---
tags:
  - leetcode
problem_number: 994
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
import collections

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = (r + dr, c + dc)
                    if row in range(len(grid)) and col in range(len(grid[0])) and (grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
```

## Complexity

$O(RC)$ time and $O(RC)$ queue space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Compute the minutes needed for all reachable fresh oranges to rot, with all rotten oranges spreading simultaneously.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc994|LeetCode — LC 994]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Enqueue every initially rotten orange and count fresh ones.
2. Run breadth-first search in complete levels, turning neighboring fresh oranges rotten when enqueuing them.
3. Count elapsed levels until no fresh oranges remain; return -1 if the queue empties while fresh oranges remain.

## Why It Works

Queue levels represent equal arrival times from the nearest initially rotten source.

## Worked Example

**Illustrative input:** `grid = [[2, 1, 1]]`.

**Trace:** The middle orange rots after one minute, then the last after two.

**Result:** Return `2`.

## Common Pitfalls

Use all sources at time zero. Mark newly rotten cells immediately to prevent duplicate enqueues; no fresh oranges initially means zero minutes.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc994|Coding Practice Index — Rotting Oranges]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 994](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0994-rotting-oranges.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
