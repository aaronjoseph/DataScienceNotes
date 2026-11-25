---
tags:
  - leetcode
  - binary-search
problem_number: 33
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

- **Time:** $O(\log n)$ worst-case, where $n$ is the length of `nums`. Every iteration either finds `target` or discards at least half of the remaining search interval.
- **Auxiliary space:** $O(1)$, using only pointer variables (`l`, `r`, `mid`); excludes the input array and the scalar return value.

> [!warning] Duplicates break the $O(\log n)$ guarantee
> This bound relies on all elements in `nums` being **distinct**. If duplicates are allowed (LeetCode 81), `nums[l] == nums[mid] == nums[r]` makes it impossible to tell which half is sorted without shrinking the boundaries one step at a time, degrading worst-case time to $O(n)$.

## Algorithm at a glance

![[Attachements/LeetCode/LC0033 - Search In Rotated Sorted Array.png|700]]

## Overview

Return the index of `target` in a rotated sorted array `nums` of **distinct** integers, or `-1` if it is not present (also listed as *Find Target in Rotated Sorted Array* in NeetCode 150).[^neetcode] Even though the array is no longer globally sorted, splitting it at any midpoint `mid` guarantees that **at least one half is strictly sorted**, which is enough to discard half the search space each step.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc33|LeetCode — LC 33]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## Key Concepts

### Structure of a Rotated Sorted Array

Rotating a strictly increasing array splits it into at most two ascending segments:

- **Left (high) segment:** values from the original tail that were moved to the front.
- **Right (low) segment:** values from the original head, all strictly smaller than every value in the left segment.

When the array is rotated by $0$ (or a multiple of $n$), there is only a single ascending segment.

### Why At Least One Half Is Always Sorted

There is at most **one** drop (pivot) where `nums[i] > nums[i + 1]`. Splitting `[l, r]` at `mid` puts that drop in either `[l, mid]` or `[mid, r]` — never both. Therefore:

- If `nums[l] <= nums[mid]`, the drop cannot lie strictly inside `[l, mid]`, so **`[l, mid]` is sorted**.
- Otherwise (`nums[l] > nums[mid]`), the drop lies in `[l, mid]`, so **`[mid, r]` is sorted**.

Once you know which half is sorted, a simple range check tells you whether `target` can lie inside that sorted half. If it can, search that half; if it cannot, `target` can only be in the opposite half.

## How to Solve

1. Initialise inclusive bounds `l = 0` and `r = len(nums) - 1`.
2. While `l <= r`, compute `mid = (l + r) // 2`. If `nums[mid] == target`, return `mid`.
3. Check whether the left half `[l, mid]` is sorted (`nums[l] <= nums[mid]`):
   - If `target` falls outside `[nums[l], nums[mid])` — i.e., `target > nums[mid]` or `target < nums[l]` — discard the left half (`l = mid + 1`).
   - Otherwise, `target` must lie in the sorted left half, so discard the right half (`r = mid - 1`).
4. Otherwise, the right half `[mid, r]` is sorted:
   - If `target` falls outside `(nums[mid], nums[r]]` — i.e., `target < nums[mid]` or `target > nums[r]` — discard the right half (`r = mid - 1`).
   - Otherwise, `target` must lie in the sorted right half, so discard the left half (`l = mid + 1`).
5. If the loop terminates without finding `target`, return `-1`.

## Why It Works

At every iteration, `nums[mid]` is checked first and then excluded from both successor ranges (`mid + 1` or `mid - 1`), so the search interval strictly shrinks and the loop always terminates. Because range comparisons are only performed against the **sorted** half, any discarded subarray is provably incapable of containing `target`, preserving the invariant that if `target` exists in `nums`, its index remains within `[l, r]`.

## Worked Example

### Example 1: Target in the Unsorted Half

**Inputs:** `nums = [4, 5, 6, 1, 2, 3]`, `target = 2`.

1. **Step 1 (`l = 0`, `r = 5`):** `mid = 2`, `nums[mid] = 6`.
   - `nums[l] <= nums[mid]` (`4 <= 6`), so left half `[4, 5, 6]` is sorted.
   - `target = 2 < nums[l] = 4`, so `2` cannot be in `[4, 5, 6]`.
   - Discard left half: set `l = 3`.
2. **Step 2 (`l = 3`, `r = 5`):** `mid = 4`, `nums[mid] = 2`.
   - `nums[mid] == target` (`2 == 2`), so return `4`.

**Outcome:** Returns index `4` in 2 comparisons.

### Example 2: Two-Element Edge Case (`<=` vs `<`)

**Inputs:** `nums = [3, 1]`, `target = 1`.

1. **Step 1 (`l = 0`, `r = 1`):** `mid = 0`, `nums[mid] = 3`.
   - Here `l == mid`, so `nums[l] == nums[mid] = 3`.
   - Because the check uses `nums[l] <= nums[mid]`, the single-element left half `[3]` is treated as sorted.
   - `target = 1 < nums[l] = 3`, so discard the left half: set `l = 1`.
2. **Step 2 (`l = 1`, `r = 1`):** `mid = 1`, `nums[mid] = 1`.
   - `nums[mid] == target`, so return `1`.

**Outcome:** Returns index `1`. If the sorted-half test had used strict `<` (`nums[l] < nums[mid]`), Step 1 would have treated the right branch as sorted, checked `target < nums[mid]` (`1 < 3`), and moved `r = mid - 1 = -1`, wrongly returning `-1`.

## Alternative Approach: Pivot + Binary Search

You can also solve this in two passes with the same $O(\log n)$ time and $O(1)$ auxiliary space:

1. Find the rotation pivot (index of the minimum element) using the method in [[LeetCode/Binary Search/Find Minimum In Rotated Sorted Array|Find Minimum In Rotated Sorted Array]].
2. Compare `target` against `nums[-1]` (or `nums[0]`) to choose either `[0, pivot - 1]` or `[pivot, n - 1]`.
3. Run standard exact-match binary search from [[LeetCode/Binary Search/Binary Search|Binary Search]] on that single sorted segment.

This two-pass version is slightly more code, but it separates the rotation logic from the target search and can be easier to verify under interview pressure.

## Common Pitfalls

- **Using `<` instead of `<=` in `nums[l] <= nums[mid]`:** When `l == mid` (a 2-element subarray), `[l, mid]` has one element and is trivially sorted. Strict `<` misclassifies it and discards the valid right element (see Example 2 above).
- **Wrong endpoint comparisons when testing the sorted half:** Remember that `nums[l]` and `nums[r]` can equal `target` (we only checked `nums[mid]` so far). That is why the exclusion conditions are strict (`target < nums[l]` and `target > nums[r]`), keeping `nums[l]` and `nums[r]` inside the sorted half when `target` equals an endpoint.
- **Assuming duplicates work without modification:** Distinct values are required. With duplicates (LC 81), `nums[l] == nums[mid]` no longer proves `[l, mid]` is sorted (e.g., `[1, 0, 1, 1, 1]`).
- **Special-casing unrotated arrays unnecessarily:** When `nums` is already sorted (0 rotations), `nums[l] <= nums[mid]` is always true and the algorithm reduces cleanly to standard binary search.

## Related Notes

- [[LeetCode/Binary Search/Binary Search|Binary Search]] — Core binary search templates, monotonicity, and boundary invariants.
- [[LeetCode/Binary Search/Find Minimum In Rotated Sorted Array|Find Minimum In Rotated Sorted Array]] — Companion problem (LC 153) for locating the rotation pivot.
- [[Big O]] — Logarithmic time complexity analysis.
- [[Job Interviews/Coding Practice Index#^lc33|Coding Practice Index — Search In Rotated Sorted Array]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 33](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0033-search-in-rotated-sorted-array.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative examples are written for this vault. Code is adapted where needed for the stated approach.
[^neetcode]: [NeetCode 150 — Find Target in Rotated Sorted Array](https://neetcode.io/problems/find-target-in-rotated-sorted-array/question?list=neetcode150) — Problem statement and NeetCode 150 practice entry corresponding to LeetCode 33.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
