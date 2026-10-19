---
tags:
  - leetcode
problem_number: 62
difficulty: "Medium"
pattern: "2-D Dynamic Programming"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
```

## Complexity

$O(mn)$ time and $O(n)$ auxiliary space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Count paths across an m by n grid when each move goes only right or down.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc62|LeetCode — LC 62]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Maintain a row of path counts, initialized to one along an edge.
2. Fill each earlier row from right to left, combining the count to the right with the count below.
3. Return the count at the upper-left cell.

## Why It Works

Every path starts with either a right move or a down move, giving disjoint choices whose counts add.

## Worked Example

**Illustrative input:** `m = 2`, `n = 3`.

**Trace:** The paths correspond to placing one down move among the three moves.

**Result:** Return `3`.

## Common Pitfalls

This version has no blocked cells. Edge rows and columns have exactly one remaining route.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc62|Coding Practice Index — Unique Paths]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 62](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0062-unique-paths.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
