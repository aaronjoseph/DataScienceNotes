---
tags:
  - leetcode
problem_number: 66
difficulty: "Easy"
pattern: "Math & Geometry"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        one = 1
        i = 0
        digits = digits[::-1]
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(one)
                one = 0
            i += 1
        return digits[::-1]
```

## Complexity

$O(n)$ time and $O(n)$ extra space in this implementation because it reverses with slices. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Add one to an integer represented as most-significant-first decimal digits.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc66|LeetCode — LC 66]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Work from the least significant digit, propagating a carry.
2. Turn a 9 into zero and continue; otherwise increment the digit and stop the carry.
3. If every digit overflowed, add a leading one and return digits in original order.

## Why It Works

The carry behaves exactly like decimal column addition and stops at the first digit below nine.

## Worked Example

**Illustrative input:** `digits = [9, 9]`.

**Trace:** Both digits become zero and the remaining carry adds a new leading 1.

**Result:** Return `[1, 0, 0]`.

## Common Pitfalls

All-nine input grows by one digit. A backward in-place scan can reduce auxiliary storage apart from a possible expanded output.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc66|Coding Practice Index — Plus One]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 66](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0066-plus-one.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
