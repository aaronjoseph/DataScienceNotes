---
tags:
  - leetcode
problem_number: 74
difficulty: "Medium"
pattern: "Binary Search"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0074 - Search a 2D Matrix.png|700]]

## Overview

Search a matrix whose rows are sorted and whose next row starts after the previous row ends.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc74|LeetCode — LC 74]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Binary search rows using their first and last values.
2. If no row can contain the target, return false.
3. Binary search within the candidate row and return whether the target is found.

## Why It Works

The row ordering excludes entire rows, then ordinary sorted-array search excludes columns within the surviving row.

## Worked Example

**Illustrative input:** `matrix = [[1, 3, 5], [7, 9, 11]]`, `target = 9`.

**Trace:** Select the second row, then find its middle value.

**Result:** Return `True`.

## Common Pitfalls

This requires global row-to-row ordering. A matrix sorted independently by row and column is a different problem.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc74|Coding Practice Index — Search a 2D Matrix]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.
- [[LeetCode/Binary Search/Binary Search|Binary Search]] — Search templates and boundary invariants.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = (len(matrix), len(matrix[0]))
        top, bot = (0, ROWS - 1)
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not top <= bot:
            return False
        row = (top + bot) // 2
        l, r = (0, COLS - 1)
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
```

## Complexity

$O(\log r+\log c)$ time and $O(1)$ extra space for `r` rows and `c` columns. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 74](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0074-search-a-2d-matrix.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
