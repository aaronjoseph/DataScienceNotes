---
tags:
  - leetcode
problem_number: 54
difficulty: "Medium"
pattern: "Math & Geometry"
languages:
  - Python
---

Return matrix values in clockwise spiral order by shrinking four boundaries.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc54|LeetCode — LC 54]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Traverse the top row and right column, then shrink those boundaries.
2. Check that an interior rectangle remains before traversing the bottom row and left column.
3. Shrink again and repeat until either dimension is exhausted.

## Why It Works

Each pass removes one perimeter without revisiting it; the boundaries always describe the remaining unvisited rectangle.

## Worked Example

**Illustrative input:** `matrix = [[1, 2, 3], [4, 5, 6]]`.

**Trace:** Read 1,2,3 across the top, then 6 down the right, then 5,4 across the bottom.

**Result:** Return `[1, 2, 3, 6, 5, 4]`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = (0, len(matrix[0]))
        top, bottom = (0, len(matrix))
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
```

## Complexity

$O(RC)$ time and $O(1)$ auxiliary space, excluding output. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Recheck boundaries before traversing the bottom and left edges, especially for one-row or one-column inputs.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc54|Coding Practice Index — Spiral Matrix]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 54](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0054-spiral-matrix.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
