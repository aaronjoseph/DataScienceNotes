---
tags:
  - leetcode
problem_number: 78
difficulty: "Medium"
pattern: "Backtracking"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0078 - Subsets.png|700]]

## Overview

Generate all subsets of distinct input values by deciding whether to include each position.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc78|LeetCode — LC 78]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Maintain a mutable subset and a current index.
2. Recurse once including the current value, then undo that choice and recurse excluding it.
3. At the end of the input, append a copy of the current subset.

## Why It Works

Each binary decision sequence identifies exactly one subset, so all subsets are generated without duplicates.

## Worked Example

**Illustrative input:** `nums = [1, 2]`.

**Trace:** The include/exclude paths select both, only 1, only 2, or neither.

**Result:** Return `[[], [1], [2], [1, 2]]` in any order.

## Common Pitfalls

Include the empty subset. Copy the path at a leaf so later mutations do not change saved results.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc78|Coding Practice Index — Subsets]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
```

## Complexity

$O(n2^n)$ time including copies and $O(n)$ auxiliary recursion/path space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 78](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0078-subsets.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
