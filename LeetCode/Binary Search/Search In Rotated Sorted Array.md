---
tags:
  - leetcode
problem_number: 33
difficulty: "Medium"
pattern: "Binary Search"
languages:
  - Python
---

Return a target's index in a rotated sorted array with distinct values. At least one half around a midpoint remains sorted.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc33|LeetCode — LC 33]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Check the midpoint for equality.
2. Determine whether the left half is sorted; otherwise the right half is sorted.
3. Test whether the target lies inside that sorted half and discard the opposite half, or search the unsorted half when it does not.

## Why It Works

Range comparisons exclude a half only when sorted order proves the target cannot be there.

## Worked Example

**Illustrative input:** `nums = [4, 5, 6, 1, 2, 3]`, `target = 2`.

**Trace:** The sorted left half excludes 2, so search the right half.

**Result:** Return index `4`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l, r = (0, len(nums) - 1)
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        return -1
```

## Complexity

$O(\log n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

The distinct-value assumption matters. Include the correct endpoint equalities when testing sorted halves.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc33|Coding Practice Index — Search In Rotated Sorted Array]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.
- [[LeetCode/Binary Search/Binary Search|Binary Search]] — Search templates and boundary invariants.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 33](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0033-search-in-rotated-sorted-array.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
