---
tags:
  - leetcode
problem_number: 417
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

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = (len(heights), len(heights[0]))
        pac, atl = (set(), set())

        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or r < 0 or c < 0 or (r == ROWS) or (c == COLS) or (heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
```

## Complexity

$O(RC)$ time and $O(RC)$ space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Find cells from which water can reach both oceans. Search backward from each ocean's boundary.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc417|LeetCode — LC 417]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Start one flood fill from the top and left edges and another from the bottom and right edges.
2. Move backward only to equal or higher neighboring cells.
3. Return the intersection of cells reached by the two searches.

## Why It Works

A reversed uphill path to a cell corresponds exactly to an allowed downhill path from that cell to the ocean.

## Worked Example

**Illustrative input:** `heights = [[1, 2], [4, 3]]`.

**Trace:** The top-right and bottom-left cells touch both ocean boundary sets; the bottom-right can flow toward both.

**Result:** Return `[[0, 1], [1, 0], [1, 1]]` in any order.

## Common Pitfalls

Reverse the movement inequality when starting at oceans. Equal heights permit flow, and each ocean needs its own visited set.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc417|Coding Practice Index — Pacific Atlantic Water Flow]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 417](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0417-pacific-atlantic-water-flow.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
