---
tags:
  - leetcode
problem_number: 853
difficulty: "Medium"
pattern: "Stack"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0853 - Car Fleet.png|700]]

## Overview

Count car fleets reaching a target without passing. Process cars from nearest to the target to farthest.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc853|LeetCode — LC 853]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Sort position-speed pairs by descending position.
2. Compute each car's solo arrival time.
3. If its time is no greater than the fleet immediately ahead, merge it; otherwise begin another fleet.

## Why It Works

A trailing car catches the fleet ahead exactly when it would arrive no later without obstruction.

## Worked Example

**Illustrative input:** `target = 12`, positions `[10, 8, 0]`, speeds `[2, 4, 1]`.

**Trace:** The first two cars both arrive after one unit of time and merge; the last takes twelve.

**Result:** Return `2`.

## Common Pitfalls

Equal arrival times form one fleet, including meeting at the target. Preserve each car's position-speed pairing.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc853|Coding Practice Index — Car Fleet]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
```

## Complexity

$O(n\log n)$ time and $O(n)$ space for sorted pairs and the fleet stack. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 853](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0853-car-fleet.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
