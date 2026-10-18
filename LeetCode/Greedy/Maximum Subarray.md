---
tags:
  - leetcode
problem_number: 53
difficulty: "Medium"
pattern: "Greedy"
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

    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Find the greatest sum of a nonempty contiguous subarray using Kadane's algorithm.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc53|LeetCode — LC 53]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Start the global best from an actual input value and a running total from zero.
2. Add each value to the running total and update the best.
3. If the total becomes negative, discard that prefix by resetting the total to zero.

## Why It Works

A negative prefix can only reduce the sum of any future extension, so an optimal future subarray can begin after it.

## Worked Example

**Illustrative input:** `nums = [-2, 3, -1, 4, -5]`.

**Trace:** Discard the initial -2; extending 3 through -1 and 4 gives the best segment.

**Result:** Return `6`.

## Common Pitfalls

Update the best before resetting the running total. Initializing the best to zero incorrectly permits an empty answer on all-negative input.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc53|Coding Practice Index — Maximum Subarray]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 53](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0053-maximum-subarray.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
