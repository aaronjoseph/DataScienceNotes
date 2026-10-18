---
tags:
  - leetcode
problem_number: 90
difficulty: "Medium"
pattern: "Backtracking"
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

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, [])
        return res
```

## Complexity

$O(n2^n)$ worst-case time including copies; $O(n)$ auxiliary space including sorting and recursion. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Generate unique subsets when input values may repeat. Sort and skip duplicate exclusion branches.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc90|LeetCode — LC 90]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Sort values so equal items are adjacent.
2. At an index, first explore subsets including that occurrence.
3. After undoing the inclusion, skip all remaining identical occurrences before exploring exclusion.

## Why It Works

Including successive copies controls multiplicity, while excluding a value skips every equivalent route to the same subset.

## Worked Example

**Illustrative input:** `nums = [1, 2, 2]`.

**Trace:** The 2 block contributes zero, one, or two copies to subsets with or without 1.

**Result:** Return six unique subsets.

## Common Pitfalls

Do not remove duplicate values from the input entirely: subsets with multiple copies are valid.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc90|Coding Practice Index — Subsets II]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 90](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0090-subsets-ii.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
