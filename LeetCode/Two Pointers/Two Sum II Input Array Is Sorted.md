---
tags:
  - leetcode
problem_number: 167
difficulty: "Medium"
pattern: "Two Pointers"
languages:
  - Python
---

Find two distinct positions summing to a target in an already sorted array; return one-based indices.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc167|LeetCode — LC 167]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Start pointers at both ends.
2. If the sum is too small, move left inward; if too large, move right inward.
3. Return both indices increased by one when the sum matches.

## Why It Works

Sorted order proves that discarded endpoints cannot be part of a matching pair within the remaining range.

## Worked Example

**Illustrative input:** `numbers = [1, 2, 5, 8]`, `target = 7`.

**Trace:** The outer total is too large; reduce the right endpoint, then increase the left.

**Result:** Return `[2, 3]`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = (0, len(numbers) - 1)
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

The input is sorted and a solution exists under the problem contract. Stop while the pointers are distinct.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc167|Coding Practice Index — Two Sum II Input Array Is Sorted]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 167](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0167-two-sum-ii-input-array-is-sorted.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
