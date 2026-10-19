---
tags:
  - leetcode
problem_number: 153
difficulty: "Medium"
pattern: "Binary Search"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0153 - Find Minimum In Rotated Sorted Array.png|700]]

## Overview

Find the minimum value in a rotated strictly increasing array. Compare the midpoint with the right endpoint.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc153|LeetCode — LC 153]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Track a candidate interval and the smallest value inspected.
2. If the midpoint exceeds the right endpoint, search strictly to its right.
3. Otherwise record the midpoint and search to its left; include the final remaining value.

## Why It Works

With distinct values, comparison to the right endpoint identifies the rotation-containing half; saving discarded midpoints preserves a possible minimum.

## Worked Example

**Illustrative input:** `nums = [4, 5, 1, 2, 3]`.

**Trace:** The midpoint already contains 1; retain it while narrowing the remaining interval.

**Result:** Return `1`.

## Common Pitfalls

This solution assumes distinct values. A first-true variant uses `hi = mid` instead; do not mix boundary rules between templates.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc153|Coding Practice Index — Find Minimum In Rotated Sorted Array]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.
- [[LeetCode/Binary Search/Binary Search|Binary Search]] — Search templates and boundary invariants.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def findMin(self, nums: List[int]) -> int:
        start, end = (0, len(nums) - 1)
        curr_min = float('inf')
        while start < end:
            mid = start + (end - start) // 2
            curr_min = min(curr_min, nums[mid])
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        return min(curr_min, nums[start])
```

## Complexity

$O(\log n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 153](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0153-find-minimum-in-rotated-sorted-array.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
