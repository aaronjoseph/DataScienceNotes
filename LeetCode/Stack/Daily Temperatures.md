---
tags:
  - leetcode
problem_number: 739
difficulty: "Medium"
pattern: "Stack"
languages:
  - Python
---

For each day, report how many days until a strictly warmer temperature. Keep unresolved days in a decreasing stack.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc739|LeetCode — LC 739]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Scan temperatures from left to right.
2. While today's temperature exceeds the stack's top temperature, pop that earlier day and store its index distance.
3. Push today; unresolved entries retain zero in the result.

## Why It Works

The first later warmer day resolves each popped index, because earlier scanned days did not exceed its temperature.

## Worked Example

**Illustrative input:** `temperatures = [70, 70, 72]`.

**Trace:** The final day resolves both earlier days, with waits of 2 and 1.

**Result:** Return `[2, 1, 0]`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
```

## Complexity

$O(n)$ time and $O(n)$ auxiliary space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Equal temperatures do not count as warmer. Store indices so waiting times can be computed.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc739|Coding Practice Index — Daily Temperatures]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 739](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0739-daily-temperatures.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
