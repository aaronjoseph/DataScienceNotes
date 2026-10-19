---
tags:
  - leetcode
problem_number: 11
difficulty: "Medium"
pattern: "Two Pointers"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0011 - Container With Most Water.png|700]]

## Overview

Choose two vertical lines that hold the most water. Begin with the widest container and discard its limiting side.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc11|LeetCode — LC 11]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Set pointers at the first and last lines.
2. Compute the area from width and the shorter height; update the best area.
3. Move a pointer on the shorter side inward and repeat.

## Why It Works

Keeping the shorter side while reducing width cannot improve its area, so discarding that endpoint is safe.

## Worked Example

**Illustrative input:** `height = [1, 3, 2, 4]`.

**Trace:** The outer pair holds 3 units. Moving left gives the pair at indices 1 and 3.

**Result:** Return `6`.

## Common Pitfalls

Use index distance for width. The container is limited by the shorter line, not the taller one.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc11|Coding Practice Index — Container With Most Water]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def maxArea(self, height: List[int]) -> int:
        l, r = (0, len(height) - 1)
        res = 0
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return res
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 11](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0011-container-with-most-water.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
