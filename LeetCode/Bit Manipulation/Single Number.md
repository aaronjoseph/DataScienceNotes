---
tags:
  - leetcode
problem_number: 136
difficulty: "Easy"
pattern: "Bit Manipulation"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0136 - Single Number.png|700]]

## Overview

Find the one value appearing once when every other value appears exactly twice.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc136|LeetCode — LC 136]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Initialize an accumulator to zero.
2. XOR each array value into the accumulator.
3. Return the final accumulator.

## Why It Works

XOR is associative and commutative, equal pairs cancel to zero, and zero leaves the unique value unchanged.

## Worked Example

**Illustrative input:** `nums = [4, 1, 4]`.

**Trace:** The two occurrences of 4 cancel even though they are separated.

**Result:** Return `1`.

## Common Pitfalls

The exactly-twice condition is essential. This does not solve the version where other values appear three times.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc136|Coding Practice Index — Single Number]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 136](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0136-single-number.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
