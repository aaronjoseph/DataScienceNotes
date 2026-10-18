---
tags:
  - leetcode
problem_number: 4
difficulty: "Hard"
pattern: "Binary Search"
languages:
  - Python
---

Find the median of two sorted arrays without merging them. Binary search a partition in the shorter array.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc4|LeetCode — LC 4]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Choose a left partition containing half the combined elements; its split in the shorter array determines the split in the other.
2. Treat missing boundary elements as negative or positive infinity.
3. If either left boundary exceeds the opposite right boundary, move the shorter-array split; otherwise derive the median from the middle boundaries.

## Why It Works

A correct partition puts every left-side value before every right-side value while fixing the number of values on each side.

## Worked Example

**Illustrative input:** `nums1 = [1, 3]`, `nums2 = [2]`.

**Trace:** A valid split leaves 1 on the left and 2, 3 on the right.

**Result:** The odd-length median is `2`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = (nums1, nums2)
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(B) < len(A):
            A, B = (B, A)
        l, r = (0, len(A) - 1)
        while True:
            i = (l + r) // 2
            j = half - i - 2
            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i + 1] if i + 1 < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j + 1] if j + 1 < len(B) else float('infinity')
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
```

## Complexity

$O(\log(\min(m,n)+1))$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Both arrays must be sorted and cannot both be empty. The even-length median averages the two boundary middle values.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc4|Coding Practice Index — Median of Two Sorted Arrays]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.
- [[LeetCode/Binary Search/Binary Search|Binary Search]] — Search templates and boundary invariants.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 4](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0004-median-of-two-sorted-arrays.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
