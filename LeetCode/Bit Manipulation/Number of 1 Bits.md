---
tags:
  - leetcode
problem_number: 191
difficulty: "Easy"
pattern: "Bit Manipulation"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0191 - Number of 1 Bits.png|700]]

## Overview

Count set bits in a nonnegative integer by clearing its lowest set bit repeatedly.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc191|LeetCode — LC 191]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Initialize a counter to zero.
2. While the integer is nonzero, replace it with the bitwise AND of itself and one less than itself.
3. Increment the counter for each cleared bit and return it.

## Why It Works

Subtracting one flips the lowest set bit and all lower bits; AND removes exactly that one set bit.

## Worked Example

**Illustrative input:** `n = 12`, binary `1100`.

**Trace:** The transformations are 1100 → 1000 → 0000.

**Result:** Return `2`.

## Common Pitfalls

Assume a nonnegative input or explicitly mask a signed value to the intended width. Python negative integers do not terminate under this loop.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc191|Coding Practice Index — Number of 1 Bits]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
```

## Complexity

$O(b)$ time for `b` set bits and $O(1)$ extra space under fixed-width arithmetic. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 191](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0191-number-of-1-bits.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
