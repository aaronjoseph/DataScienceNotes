---
tags:
  - leetcode
problem_number: 43
difficulty: "Medium"
pattern: "Math & Geometry"
languages:
  - Python
---

Multiply two nonnegative decimal strings without converting the complete strings to integers.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc43|LeetCode — LC 43]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Allocate a digit array large enough for the sum of operand lengths.
2. Multiply every pair of digits from least significant to most significant, adding into its aligned result position and carrying upward.
3. Reverse the result digits, remove leading zeros, and join them into a string.

## Why It Works

Each digit pair contributes at its decimal place, and carry propagation preserves the value while keeping digits normalized.

## Worked Example

**Illustrative input:** `num1 = "12"`, `num2 = "13"`.

**Trace:** The aligned partial products are 36 for multiplication by the units digit and 120 for multiplication by the tens digit.

**Result:** Return `"156"`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        if '0' in [num1, num2]:
            return '0'
        res = [0] * (len(num1) + len(num2))
        num1, num2 = (num1[::-1], num2[::-1])
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10
        res, beg = (res[::-1], 0)
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return ''.join(res)
```

## Complexity

$O(mn)$ time and $O(m+n)$ auxiliary space for operand lengths `m` and `n`. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Return `"0"` for a zero operand. Converting individual characters is allowed; converting entire operands bypasses the intended algorithm.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc43|Coding Practice Index — Multiply Strings]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 43](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0043-multiply-strings.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
