---
tags:
  - leetcode
problem_number: 73
difficulty: "Medium"
pattern: "Math & Geometry"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0073 - Set Matrix Zeroes.png|700]]

## Overview

Set an entire row and column to zero whenever its original matrix contains a zero, using constant extra space.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc73|LeetCode — LC 73]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Use the first row and first column as markers; retain a separate flag for whether the first row originally needs zeroing.
2. Scan original entries and mark their associated row and column.
3. Zero the interior from markers, then handle the first column and first row last.

## Why It Works

Markers record original zero locations without needing separate row and column arrays, while delayed clearing preserves that information.

## Worked Example

**Illustrative input:** `matrix = [[1, 2, 3], [4, 0, 6]]`.

**Trace:** The zero marks its row and middle column.

**Result:** The matrix becomes `[[1, 0, 3], [0, 0, 0]]`.

## Common Pitfalls

Do not zero rows immediately during discovery, or newly written zeros can spread incorrectly. The shared top-left marker needs careful handling.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc73|Coding Practice Index — Set Matrix Zeroes]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = (len(matrix), len(matrix[0]))
        rowZero = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
```

## Complexity

$O(RC)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 73](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0073-set-matrix-zeroes.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
