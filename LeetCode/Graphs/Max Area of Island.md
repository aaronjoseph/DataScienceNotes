---
tags:
  - leetcode
problem_number: 695
difficulty: "Medium"
pattern: "Graphs"
languages:
  - Python
---

Find the greatest area of any four-directionally connected island of 1 cells.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc695|LeetCode — LC 695]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Scan all cells and maintain visited land.
2. A flood fill returns zero for water, out-of-bounds cells, or visited cells.
3. For new land, mark it and return one plus the areas reached in four directions; keep the largest component area.

## Why It Works

Each newly visited land cell contributes exactly once to its connected island's area.

## Worked Example

**Illustrative input:** `grid = [[1, 1, 0], [0, 1, 1]]`.

**Trace:** All four land cells connect through horizontal or vertical neighbors.

**Result:** Return `4`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = (len(grid), len(grid[0]))
        visit = set()

        def dfs(r, c):
            if r < 0 or r == ROWS or c < 0 or (c == COLS) or (grid[r][c] == 0) or ((r, c) in visit):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area
```

## Complexity

$O(RC)$ time and $O(RC)$ auxiliary space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Mark before recursive calls to avoid revisits. No land means the answer is zero.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc695|Coding Practice Index — Max Area of Island]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 695](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0695-max-area-of-island.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
