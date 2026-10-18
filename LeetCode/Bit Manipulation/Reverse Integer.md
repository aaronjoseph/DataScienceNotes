---
tags:
  - leetcode
problem_number: 7
difficulty: "Medium"
pattern: "Bit Manipulation"
languages:
  - Python
---

Reverse a signed 32-bit integer's decimal digits and return zero if the reversed value overflows.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc7|LeetCode — LC 7]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Remember the sign and process the absolute magnitude digit by digit.
2. Before appending a digit, compare the partial result with the signed result's permitted magnitude boundary.
3. Return zero on overflow; otherwise append the digit and restore the original sign.

## Why It Works

Each extracted units digit becomes the next most significant digit of the reversed number, and the precheck rejects overflow before multiplication.

## Worked Example

**Illustrative input:** `x = -120`.

**Trace:** Extract digits 0, then 2, then 1; leading zero disappears in the constructed number.

**Result:** Return `-21`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        remaining = abs(x)
        limit = 2147483648 if negative else 2147483647
        reversed_value = 0
        while remaining:
            remaining, digit = divmod(remaining, 10)
            if reversed_value > (limit - digit) // 10:
                return 0
            reversed_value = reversed_value * 10 + digit
        return -reversed_value if negative else reversed_value
```

## Complexity

$O(\log(|x|+1))$ time and $O(1)$ extra space under the 32-bit input contract. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Positive and negative limits differ by one. Avoid floating-point division and language-dependent negative remainder behavior.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc7|Coding Practice Index — Reverse Integer]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 7](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0007-reverse-integer.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
