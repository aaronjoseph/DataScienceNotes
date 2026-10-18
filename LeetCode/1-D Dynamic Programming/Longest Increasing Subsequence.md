---
tags:
  - leetcode
problem_number: 300
difficulty: "Medium"
pattern: "1-D Dynamic Programming"
languages:
  - Python
---

Find the length of a strictly increasing subsequence; selected elements need not be contiguous.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc300|LeetCode — LC 300]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Initialize a best length of one starting at every position.
2. Process positions backward, testing each later larger value as the next element.
3. Set the current best from one plus a later best and return the greatest table entry.

## Why It Works

Every increasing subsequence starting here either stops immediately or chooses some later larger next element.

## Worked Example

**Illustrative input:** `nums = [3, 1, 2, 4]`.

**Trace:** The subsequence 1,2,4 has three elements even though 3 precedes it.

**Result:** Return `3`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
```

## Complexity

$O(n^2)$ time and $O(n)$ space for this dynamic-programming implementation. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Use strict inequality; equal values cannot extend the sequence. An alternative tails-array method achieves logarithmic search per value.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc300|Coding Practice Index — Longest Increasing Subsequence]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 300](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0300-longest-increasing-subsequence.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
