---
tags:
  - leetcode
problem_number: 268
difficulty: "Easy"
pattern: "Bit Manipulation"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0268 - Missing Number.png|700]]

## Overview

Find the missing value when n distinct integers are drawn from the inclusive range zero through n.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc268|LeetCode — LC 268]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Initialize a balance with n.
2. For each index, add that index and subtract the value stored there.
3. Return the final balance.

## Why It Works

Every present value cancels its counterpart in the complete range, leaving only the absent value.

## Worked Example

**Illustrative input:** `nums = [3, 0, 1]`.

**Trace:** The complete range is 0 through 3 and the input omits 2.

**Result:** Return `2`.

## Common Pitfalls

Distinct values and the exact range guarantee correctness. Python avoids fixed-width overflow; an XOR implementation avoids arithmetic overflow elsewhere.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc268|Coding Practice Index — Missing Number]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 268](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0268-missing-number.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
