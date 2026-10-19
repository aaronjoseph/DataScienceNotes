---
tags:
  - leetcode
problem_number: 202
difficulty: "Easy"
pattern: "Math & Geometry"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0202 - Happy Number.png|700]]

## Overview

Determine whether repeatedly replacing a positive integer by the sum of its squared decimal digits eventually reaches one.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc202|LeetCode — LC 202]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Implement the digit-square transformation with repeated digit extraction.
2. Run slow and fast pointers through this deterministic transformation, one and two steps at a time.
3. When they meet, accept only if the meeting value is one.

## Why It Works

After the first transformation, values lie in a bounded set, so the process must reach one or enter another cycle; Floyd's method detects either.

## Worked Example

**Illustrative input:** `n = 19`.

**Trace:** The transformation sequence is 19 → 82 → 68 → 100 → 1.

**Result:** Return `True`.

## Common Pitfalls

The input is positive. Cycle detection avoids keeping every visited value, but each transformation still processes its digits.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc202|Coding Practice Index — Happy Number]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def isHappy(self, n: int) -> bool:
        slow, fast = (n, self.sumSquareDigits(n))
        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)
        return True if fast == 1 else False

    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output
```

## Complexity

$O(\log n)$ initial digit work plus a bounded number of short-state steps for fixed-width input; $O(1)$ auxiliary space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 202](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0202-happy-number.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
