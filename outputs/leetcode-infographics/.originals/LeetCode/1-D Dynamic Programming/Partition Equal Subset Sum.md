---
tags:
  - leetcode
problem_number: 416
difficulty: "Medium"
pattern: "1-D Dynamic Programming"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        reachable = {0}
        for value in nums:
            reachable = reachable | {
                current + value for current in reachable
                if current + value <= target
            }
            if target in reachable:
                return True
        return target in reachable
```

## Complexity

$O(nT)$ expected time and $O(T)$ space for half-total target `T`; this is pseudo-polynomial in numeric values. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Decide whether positive integers can be partitioned into two equal-sum subsets.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc416|LeetCode — LC 416]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Reject an odd total; otherwise set the target to half the total.
2. Start reachable subset sums with zero.
3. For each number, build a fresh set containing old sums and old sums plus that number, retaining only values at most the target; return whether target is reachable.

## Why It Works

Every subset either excludes or includes the current occurrence, and the fresh set prevents reusing that occurrence twice.

## Worked Example

**Illustrative input:** `nums = [1, 5, 11, 5]`.

**Trace:** The target is 11, reachable either with the 11 alone or with 1,5,5.

**Result:** Return `True`.

## Common Pitfalls

Use only sums from the previous iteration. Positivity justifies discarding sums above the target.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc416|Coding Practice Index — Partition Equal Subset Sum]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 416](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0416-partition-equal-subset-sum.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
