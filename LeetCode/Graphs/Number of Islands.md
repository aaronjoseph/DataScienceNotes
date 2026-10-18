---
tags:
  - leetcode
problem_number: 200
difficulty: "Medium"
pattern: "Graphs"
languages:
  - Python
---

Count connected islands of land in a grid using horizontal and vertical adjacency.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc200|LeetCode — LC 200]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Scan all cells and keep a visited set.
2. Whenever an unvisited land cell is found, increment the island count and flood-fill its connected land.
3. Mark each cell before exploring neighbors so it cannot be counted again.

## Why It Works

Each flood fill marks exactly one connected land component, and every island eventually supplies one starting cell.

## Worked Example

**Illustrative input:** `grid = [["1", "0"], ["0", "1"]]`.

**Trace:** The two land cells touch only diagonally, so each starts its own flood fill.

**Result:** Return `2`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        islands = 0
        visit = set()
        rows, cols = (len(grid), len(grid[0]))

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == '0' or ((r, c) in visit):
                return
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands
```

## Complexity

$O(RC)$ expected time and $O(RC)$ space for visited cells and worst-case recursion. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Diagonal contact does not connect islands. Recursive flood fill can exhaust Python's stack on a large connected component.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc200|Coding Practice Index — Number of Islands]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 200](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0200-number-of-islands.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
