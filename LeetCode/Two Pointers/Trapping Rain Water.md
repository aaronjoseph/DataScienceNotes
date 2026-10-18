---
tags:
  - leetcode
problem_number: 42
difficulty: "Hard"
pattern: "Two Pointers"
languages:
  - Python
---

Compute trapped water above bars. Finalize the side with the smaller known boundary height.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc42|LeetCode — LC 42]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Maintain pointers and maximum heights seen from both ends.
2. Advance the side with the smaller running maximum.
3. Update that side's maximum and add its nonnegative difference from the current bar.

## Why It Works

The opposite boundary is already high enough to support the smaller side, so unseen bars cannot change that side's water level.

## Worked Example

**Illustrative input:** `height = [3, 0, 2, 3]`.

**Trace:** The interior bars retain 3 and 1 units respectively.

**Result:** Return `4`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = (0, len(height) - 1)
        leftMax, rightMax = (height[l], height[r])
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Count water above individual bars, not the area of one container. Update the running maximum before accumulating.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc42|Coding Practice Index — Trapping Rain Water]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 42](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0042-trapping-rain-water.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
