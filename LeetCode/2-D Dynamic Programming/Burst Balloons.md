---
tags:
  - leetcode
problem_number: 312
difficulty: "Hard"
pattern: "2-D Dynamic Programming"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0312 - Burst Balloons.png|700]]

## Overview

Choose an order of bursting balloons that maximizes coins. Solve each interval by deciding which balloon bursts last.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc312|LeetCode — LC 312]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Pad the input with boundary balloons of value one.
2. For every open interval, try each interior balloon as its final burst.
3. Combine the best left and right subinterval totals with that final burst's boundary product, processing shorter intervals first.

## Why It Works

The final balloon has fixed surviving interval boundaries, making the left and right earlier burst problems independent.

## Worked Example

**Illustrative input:** `nums = [3, 1]`.

**Trace:** Bursting 1 first earns 3, then bursting 3 earns another 3.

**Result:** Return `6`.

## Common Pitfalls

Choosing the first burst leaves changing neighbors and overlapping decisions. The useful interval decision is the final burst.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc312|Coding Practice Index — Burst Balloons]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        nums = [1] + nums + [1]
        for offset in range(2, len(nums)):
            for left in range(len(nums) - offset):
                right = left + offset
                for pivot in range(left + 1, right):
                    coins = nums[left] * nums[pivot] * nums[right]
                    coins += cache.get((left, pivot), 0) + cache.get((pivot, right), 0)
                    cache[left, right] = max(coins, cache.get((left, right), 0))
        return cache.get((0, len(nums) - 1), 0)
```

## Complexity

$O(n^3)$ time and $O(n^2)$ space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 312](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0312-burst-balloons.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
