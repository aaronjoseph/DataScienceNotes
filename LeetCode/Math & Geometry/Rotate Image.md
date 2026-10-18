---
tags:
  - leetcode
problem_number: 48
difficulty: "Medium"
pattern: "Math & Geometry"
languages:
  - Python
---

Rotate a square matrix ninety degrees clockwise in place by cycling groups of four cells.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc48|LeetCode — LC 48]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Process the outer square layer, then move inward.
2. For each offset along a layer's top edge, save the top-left cycle value.
3. Move bottom-left to top-left, bottom-right to bottom-left, top-right to bottom-right, and the saved value to top-right.

## Why It Works

The four-way cycles move every layer cell to its clockwise destination exactly once.

## Worked Example

**Illustrative input:** `matrix = [[1, 2], [3, 4]]`.

**Trace:** Cycle the four corner values clockwise.

**Result:** The matrix becomes `[[3, 1], [4, 2]]`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = (0, len(matrix) - 1)
        while l < r:
            for i in range(r - l):
                top, bottom = (l, r)
                topLeft = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1
```

## Complexity

$O(n^2)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

The input must be square. Save one overwritten value before starting each four-cell cycle.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc48|Coding Practice Index — Rotate Image]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 48](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0048-rotate-image.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
