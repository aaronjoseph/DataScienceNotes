---
tags:
  - leetcode
problem_number: 128
difficulty: "Medium"
pattern: "Arrays & Hashing"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0128 - Longest Consecutive Sequence.png|700]]

## Overview

Find the length of the longest sequence of consecutive integer values, regardless of their input order.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc128|LeetCode — LC 128]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Put all values in a set to remove duplicates.
2. Start a walk only at a value whose immediate predecessor is absent.
3. Count consecutive successors and keep the longest length.

## Why It Works

Every run has exactly one starting value, so each distinct value is walked at most once.

## Worked Example

**Illustrative input:** `nums = [10, 3, 1, 2, 2]`.

**Trace:** Start at 1 and walk through 2 and 3; 10 is a separate run.

**Result:** Return `3`.

## Common Pitfalls

Iterate over the set, not repeated input values, or duplicate starts can repeat long walks.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc128|Coding Practice Index — Longest Consecutive Sequence]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
```

## Complexity

$O(n)$ expected time and $O(n)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 128](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0128-longest-consecutive-sequence.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
