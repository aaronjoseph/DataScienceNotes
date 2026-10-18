---
tags:
  - leetcode
problem_number: 15
difficulty: "Medium"
pattern: "Two Pointers"
languages:
  - Python
---

Find all unique value triplets summing to zero. Sort first, then solve a two-pointer pair search for each fixed value.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc15|LeetCode — LC 15]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Sort the values and skip duplicate fixed values.
2. For each fixed position, place pointers immediately after it and at the end.
3. Move the left pointer for a negative total or the right for a positive total; record zero totals and skip duplicate pairs.

## Why It Works

Sorted order identifies which pointer can move toward zero, while duplicate skipping emits each value triplet once.

## Worked Example

**Illustrative input:** `nums = [-2, 0, 0, 2, 2]`.

**Trace:** Fix -2 and find 0 with 2; later identical pairs are skipped.

**Result:** Return `[[-2, 0, 2]]`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = (i + 1, len(nums) - 1)
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
```

## Complexity

$O(n^2)$ time; Python sorting can use $O(n)$ auxiliary space, excluding output. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Use three distinct indices. Sorting mutates the input, and duplicate output values require explicit handling.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc15|Coding Practice Index — 3Sum]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 15](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0015-3sum.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
