---
tags:
  - leetcode
problem_number: 70
difficulty: "Easy"
pattern: "1-D Dynamic Programming"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = (2, 3)
        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2
```

## Complexity

$O(n)$ time and $O(1)$ auxiliary space under bounded-integer accounting. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Count ways to climb n stairs when each move climbs either one or two stairs.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc70|LeetCode — LC 70]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Use the small cases directly.
2. Maintain the number of ways to reach the previous two stair counts.
3. For each next stair count, add those two counts and advance the rolling state.

## Why It Works

Every path ends in either a one-step move or a two-step move, producing disjoint and exhaustive cases.

## Worked Example

**Illustrative input:** `n = 4`.

**Trace:** The previous counts are 2 ways for two stairs and 3 ways for three stairs.

**Result:** Return `5`.

## Common Pitfalls

This problem starts at positive n. For a reusable recurrence, define zero stairs as one empty sequence.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc70|Coding Practice Index — Climbing Stairs]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 70](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0070-climbing-stairs.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
