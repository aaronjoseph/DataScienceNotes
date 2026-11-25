---
tags:
  - leetcode
  - binary-search
problem_number: 153
difficulty: "Medium"
pattern: "Binary Search"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.[^implementation]

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

- **Time:** $O(\log n)$ worst-case, where $n$ is the length of `nums`. Each iteration discards at least half of the remaining search range.
- **Auxiliary space:** $O(1)$, using only pointer and accumulator variables (`start`, `end`, `mid`, `curr_min`); excludes the input array and scalar return value.

## Algorithm at a glance

![[Attachements/LeetCode/LC0153 - Find Minimum In Rotated Sorted Array.png|700]]

## Overview

Find the minimum value in a rotated strictly increasing array of **distinct** integers. Comparing the midpoint `nums[mid]` against the right endpoint `nums[end]` reveals which half contains the rotation drop (and therefore the minimum).[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc153|LeetCode — LC 153]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## Key Concepts

### Monotonic View (`first_true` Connection)

In a rotated sorted array with distinct elements, every element in the left (high) segment is strictly greater than `nums[n - 1]`, while every element in the right (low) segment is less than or equal to `nums[n - 1]`. Testing `nums[i] <= nums[n - 1]` produces a monotonic `F F F T T T` pattern across the array, where the **first `T`** is the minimum element:

```text
nums:              4  5  1  2  3
nums[i] <= nums[4]: F  F  T  T  T
                          ^ minimum (pivot)
```

This matches the **First True** template in [[LeetCode/Binary Search/Binary Search|Binary Search]] (which uses `hi = mid` when `nums[mid] <= nums[hi]`). The reference implementation above achieves the same result while excluding `mid` on both branches (`end = mid - 1`) by saving `nums[mid]` into `curr_min` before shrinking `end`.

## How to Solve

1. Track a candidate interval `[start, end]` and `curr_min`, the smallest value inspected so far.
2. While `start < end`, compute `mid = start + (end - start) // 2` and update `curr_min = min(curr_min, nums[mid])`.
3. If `nums[mid] > nums[end]`, `mid` lies in the higher left segment, so the minimum must be strictly to its right (`start = mid + 1`).
4. Otherwise (`nums[mid] <= nums[end]`), `mid` lies in the sorted right segment; since `nums[mid]` is already saved in `curr_min`, search strictly to its left (`end = mid - 1`).
5. After the loop exits, return `min(curr_min, nums[start])` to include the final remaining element.

## Why It Works

With distinct values, comparing `nums[mid]` to `nums[end]` unambiguously identifies which side holds the rotation drop:

- If `nums[mid] > nums[end]`, the drop occurs strictly after `mid`, so nothing in `[start, mid]` can be the minimum.
- If `nums[mid] <= nums[end]`, `[mid, end]` is strictly increasing, so nothing strictly to the right of `mid` can be smaller than `nums[mid]`. Recording `nums[mid]` in `curr_min` makes `end = mid - 1` safe.

When the array is unrotated (0 rotations), `nums[mid] <= nums[end]` holds on every step and the search moves left to `nums[0]`.

## Worked Example

**Inputs:** `nums = [4, 5, 1, 2, 3]`.

1. **Step 1 (`start = 0`, `end = 4`):** `mid = 2`, `nums[mid] = 1`.
   - Update `curr_min = min(inf, 1) = 1`.
   - `nums[2] = 1 <= nums[4] = 3`, so set `end = mid - 1 = 1`.
2. **Step 2 (`start = 0`, `end = 1`):** `mid = 0`, `nums[mid] = 4`.
   - Update `curr_min = min(1, 4) = 1`.
   - `nums[0] = 4 <= nums[1] = 5`, so set `end = mid - 1 = -1`.
3. **Termination:** `start < end` (`0 < -1`) is false; return `min(curr_min, nums[0]) = min(1, 4) = 1`.

**Outcome:** Returns `1`, because `curr_min` preserved `nums[2]` even after `end` moved past it.

## Common Pitfalls

- **Mixing boundary rules between templates:** The `curr_min` implementation above uses `end = mid - 1`, whereas a `first_true` variant without `curr_min` must use `hi = mid` (otherwise it can skip the minimum when `mid` lands on it). Do not mix the two.
- **Comparing against `nums[start]` instead of `nums[end]`:** In an unrotated subarray (e.g., `[1, 2, 3]`), `nums[mid] >= nums[start]` is true, which would wrongly push you right if you assumed that meant you were in the high segment. Comparing against `nums[end]` handles both rotated and unrotated subarrays cleanly.
- **Duplicates:** This solution assumes distinct values. With duplicates (LeetCode 154), `nums[mid] == nums[end]` is ambiguous and requires shrinking `end -= 1`, giving $O(n)$ worst-case time.

## Related Notes

- [[LeetCode/Binary Search/Binary Search|Binary Search]] — Core binary search templates (`first_true`) and rotated-array patterns.
- [[LeetCode/Binary Search/Search In Rotated Sorted Array|Search In Rotated Sorted Array]] — Companion problem (LC 33) searching for a target in the same array structure.
- [[Big O]] — Logarithmic time complexity analysis.
- [[Job Interviews/Coding Practice Index#^lc153|Coding Practice Index — Find Minimum In Rotated Sorted Array]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 153](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0153-find-minimum-in-rotated-sorted-array.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
