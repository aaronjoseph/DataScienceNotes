---
tags:
  - leetcode
problem_number: 213
difficulty: "Medium"
pattern: "1-D Dynamic Programming"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0213 - House Robber II.png|700]]

## Overview

Choose nonadjacent houses arranged in a circle, where the first and last houses are also neighbors.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc213|LeetCode — LC 213]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Handle a single house directly.
2. Solve the linear house-robber problem once excluding the first house and once excluding the last.
3. Return the larger result.

## Why It Works

A valid solution cannot include both endpoints, so at least one of the two linear cases contains every optimal circular solution.

## Worked Example

**Illustrative input:** `nums = [2, 3, 2]`.

**Trace:** Excluding either endpoint leaves a two-house linear problem whose best value is 3.

**Result:** Return `3`.

## Common Pitfalls

The linear recurrence is constant-space, but slicing is not. A range-indexed helper can remove the extra allocation.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc213|Coding Practice Index — House Robber II]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = (0, 0)
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
```

## Complexity

$O(n)$ time and $O(n)$ extra space in this Python implementation because both linear cases use slices. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 213](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0213-house-robber-ii.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
