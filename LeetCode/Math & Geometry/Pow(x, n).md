---
tags:
  - leetcode
problem_number: 50
difficulty: "Medium"
pattern: "Math & Geometry"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0050 - Pow(x, n).png|700]]

## Overview

Compute a real base raised to an integer exponent using exponentiation by squaring.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc50|LeetCode — LC 50]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Solve the absolute exponent, returning one when it is zero.
2. Recurse on the squared base and half the exponent.
3. If the exponent is odd, multiply the recursive result by the current base; take the reciprocal for a negative original exponent.

## Why It Works

Halving an exponent and squaring the base preserves its power, with one extra factor for odd exponents.

## Worked Example

**Illustrative input:** `x = 2`, `n = -3`.

**Trace:** Compute the positive power 8 by halving the exponent, then take its reciprocal.

**Result:** Return `0.125`.

## Common Pitfalls

A negative exponent requires a nonzero base. Fixed-width languages must widen before negating the smallest signed exponent; floating-point results are approximate.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc50|Coding Practice Index — Pow(x, n)]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(base, exponent):
            if exponent == 0:
                return 1.0
            result = power(base * base, exponent // 2)
            return base * result if exponent % 2 else result
        result = power(x, abs(n))
        return result if n >= 0 else 1.0 / result
```

## Complexity

$O(\log(|n|+1))$ arithmetic steps and recursion space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 50](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0050-powx-n.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
