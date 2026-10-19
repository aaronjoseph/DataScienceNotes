---
tags:
  - leetcode
problem_number: 84
difficulty: "Hard"
pattern: "Stack"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0084 - Largest Rectangle In Histogram.png|700]]

## Overview

Find the largest rectangle formed by consecutive histogram bars. Use increasing heights to discover each bar's widest valid range.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc84|LeetCode — LC 84]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Keep pairs of starting index and height in an increasing stack.
2. When a shorter bar arrives, pop taller bars and evaluate their rectangles ending just before it; carry the earliest popped start forward.
3. Push the new bar, then evaluate remaining stack entries through the histogram's end.

## Why It Works

A popped height has just found its first smaller right boundary; its stored start already excludes smaller bars on the left.

## Worked Example

**Illustrative input:** `heights = [2, 1, 2]`.

**Trace:** The center height 1 spans all three bars; height 2 spans one at either end.

**Result:** Return `3`.

## Common Pitfalls

Carry the popped start into the next push. Remaining bars still need an end-of-array evaluation.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc84|Coding Practice Index — Largest Rectangle In Histogram]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
```

## Complexity

$O(n)$ time and $O(n)$ auxiliary space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 84](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0084-largest-rectangle-in-histogram.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
