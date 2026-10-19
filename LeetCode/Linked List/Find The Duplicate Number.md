---
tags:
  - leetcode
problem_number: 287
difficulty: "Medium"
pattern: "Linked List"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0287 - Find The Duplicate Number.png|700]]

## Overview

Find the repeated value in an array of n+1 integers drawn from 1 through n, without modifying the array.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc287|LeetCode — LC 287]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Interpret each index as pointing to the index stored in that array position.
2. Run Floyd's slow/fast cycle detection from index zero.
3. After a meeting, start another pointer at zero and advance both one step until they meet at the cycle entry.

## Why It Works

The value range creates a reachable functional-graph cycle; the cycle entry has repeated incoming references and is the duplicate value.

## Worked Example

**Illustrative input:** `nums = [1, 3, 4, 2, 2]`.

**Trace:** The index walk is 0 → 1 → 3 → 2 → 4 → 2.

**Result:** The cycle entry identifies value `2`.

## Common Pitfalls

These value-range and single-duplicate assumptions are essential. The meeting point from the first phase is not necessarily the duplicate.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc287|Coding Practice Index — Find The Duplicate Number]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = (0, 0)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 287](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0287-find-the-duplicate-number.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
