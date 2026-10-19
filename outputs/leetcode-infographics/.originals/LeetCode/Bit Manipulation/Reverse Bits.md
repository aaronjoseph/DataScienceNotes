---
tags:
  - leetcode
problem_number: 190
difficulty: "Easy"
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

    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n >> i & 1
            res += bit << 31 - i
        return res
```

## Complexity

$O(32)$ time and $O(1)$ extra space; for variable width `w`, the loop takes $O(w)$ steps. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Reverse all 32 bits of an unsigned integer, including leading zeros.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc190|LeetCode — LC 190]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Initialize the result to zero.
2. For each of the 32 bit positions, extract the input bit with a shift and mask.
3. Place that bit in the mirrored output position and accumulate it.

## Why It Works

Every input position maps uniquely to the corresponding reversed position across the fixed 32-bit word.

## Worked Example

**Illustrative input:** `n = 1`, represented as a 32-bit word.

**Trace:** The least significant input bit becomes the most significant output bit.

**Result:** Return `2147483648`.

## Common Pitfalls

Reverse the full word width, not just the digits of the shortest binary representation. Use unsigned semantics in fixed-width languages.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc190|Coding Practice Index — Reverse Bits]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 190](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0190-reverse-bits.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
