---
tags:
  - leetcode
problem_number: 46
difficulty: "Medium"
pattern: "Backtracking"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0046 - Permutations.png|700]]

## Overview

Generate every ordering of distinct values. Recursively choose the final value of each ordering.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc46|LeetCode — LC 46]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Rotate each candidate out of the current list in turn.
2. Recursively permute the remaining list, append the removed value to each returned permutation, and collect them.
3. Restore the removed value before considering the next candidate.

## Why It Works

Each permutation has a unique final value and a unique ordering of the remaining values.

## Worked Example

**Illustrative input:** `nums = [1, 2]`.

**Trace:** Choose 1 as the final value to obtain [2, 1], then 2 to obtain [1, 2].

**Result:** Return both orderings.

## Common Pitfalls

The implementation temporarily mutates the input and restores it. The problem assumes nonempty input; a reusable variant should return `[[]]` for empty input.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc46|Coding Practice Index — Permutations]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
```

## Complexity

$O(n\,n!)$ time and $O(n\,n!)$ transient materialized permutation storage for this implementation, including intermediate results. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 46](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0046-permutations.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
