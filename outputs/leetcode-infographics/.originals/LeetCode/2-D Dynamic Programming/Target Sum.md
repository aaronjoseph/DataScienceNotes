---
tags:
  - leetcode
problem_number: 494
difficulty: "Medium"
pattern: "2-D Dynamic Programming"
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

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[i, total]
            dp[i, total] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])
            return dp[i, total]
        return backtrack(0, 0)
```

## Complexity

$O(n(S+1))$ time and space as a range-based upper bound for total absolute sum `S`; the recursion also uses $O(n)$ stack space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Count assignments of plus or minus signs to all numbers that reach a target.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc494|LeetCode — LC 494]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Memoize by the current index and accumulated total.
2. Branch by adding the current number and by subtracting it.
3. After every number has a sign, return one for a matching total and zero otherwise; add branch counts.

## Why It Works

Each sign assignment follows exactly one branch sequence, and identical index-total states have identical remaining choices.

## Worked Example

**Illustrative input:** `nums = [0, 1]`, `target = 1`.

**Trace:** Both +0+1 and -0+1 are valid distinct sign assignments.

**Result:** Return `2`.

## Common Pitfalls

Zeros still produce two sign choices. The target may be negative, and repeated values remain distinct positions.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc494|Coding Practice Index — Target Sum]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 494](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0494-target-sum.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
