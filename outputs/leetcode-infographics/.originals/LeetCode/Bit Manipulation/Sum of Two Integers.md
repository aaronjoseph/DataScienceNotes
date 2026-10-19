---
tags:
  - leetcode
problem_number: 371
difficulty: "Medium"
pattern: "Bit Manipulation"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a, b = a & mask, b & mask
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
```

## Complexity

$O(w)$ bit-propagation rounds and $O(1)$ extra word storage for fixed width `w = 32`. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Add two signed integers with bit operations. Use a fixed 32-bit mask to control Python's unlimited sign extension.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc371|LeetCode — LC 371]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Mask both inputs to 32 bits.
2. Use XOR for addition without carry and shifted AND for carry, masking both new states until no carry remains.
3. Interpret the resulting unsigned word as a signed two's-complement integer.

## Why It Works

XOR supplies differing bits and AND identifies the carry-generating positions; repeated propagation completes binary addition.

## Worked Example

**Illustrative input:** `a = -2`, `b = 3`.

**Trace:** Operate on their 32-bit representations and propagate carries until none remain.

**Result:** The signed interpretation is `1`.

## Common Pitfalls

Mask every carry update in Python. The conversion must distinguish a nonnegative word from one with its sign bit set.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc371|Coding Practice Index — Sum of Two Integers]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 371](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0371-sum-of-two-integers.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
