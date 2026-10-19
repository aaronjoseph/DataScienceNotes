---
tags:
  - leetcode
problem_number: 329
difficulty: "Hard"
pattern: "2-D Dynamic Programming"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0329 - Longest Increasing Path In a Matrix.png|700]]

## Overview

Find the longest strictly increasing four-directional path in a matrix.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc329|LeetCode — LC 329]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Memoize the longest increasing path beginning at each cell.
2. Try each neighbor with a strictly larger value and keep the best extension.
3. Evaluate every starting cell and return the greatest cached length.

## Why It Works

Strict increases prevent cycles, so the grid induces an acyclic dependency graph and each cell's best suffix is reusable.

## Worked Example

**Illustrative input:** `matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]`.

**Trace:** A valid longest path is 1 → 2 → 6 → 9.

**Result:** Return `4`.

## Common Pitfalls

Equal values cannot extend a path. Avoid a sentinel that assumes all values are positive; the implementation below compares neighbors directly.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc329|Coding Practice Index — Longest Increasing Path In a Matrix]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, columns = len(matrix), len(matrix[0])
        memo = {}
        def visit(row, column):
            if (row, column) in memo:
                return memo[row, column]
            best = 1
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, column + dc
                if (0 <= nr < rows and 0 <= nc < columns
                        and matrix[nr][nc] > matrix[row][column]):
                    best = max(best, 1 + visit(nr, nc))
            memo[row, column] = best
            return best
        return max(visit(r, c) for r in range(rows) for c in range(columns))
```

## Complexity

$O(RC)$ time and $O(RC)$ memo/recursion space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 329](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0329-longest-increasing-path-in-a-matrix.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
