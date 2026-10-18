---
tags:
  - leetcode
problem_number: 678
difficulty: "Medium"
pattern: "Greedy"
languages:
  - Python
---

Check whether a parentheses string can be balanced when each star may be an opening bracket, closing bracket, or empty.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc678|LeetCode — LC 678]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Maintain the smallest and largest feasible counts of unmatched opening brackets.
2. An opening bracket raises both, a closing bracket lowers both, and a star widens the possible range.
3. Reject if the maximum becomes negative, clamp the minimum at zero, and accept at the end only if the minimum is zero.

## Why It Works

The interval captures every feasible unmatched-open count after the prefix; zero at the end means at least one complete balanced assignment exists.

## Worked Example

**Illustrative input:** `s = "(*)"`.

**Trace:** The star can be empty, leaving the balanced string ().

**Result:** Return `True`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = (0, 0)
        for c in s:
            if c == '(':
                leftMin, leftMax = (leftMin + 1, leftMax + 1)
            elif c == ')':
                leftMin, leftMax = (leftMin - 1, leftMax - 1)
            else:
                leftMin, leftMax = (leftMin - 1, leftMax + 1)
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Clamp only the lower bound. A negative upper bound means the prefix has too many closing brackets under every interpretation.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc678|Coding Practice Index — Valid Parenthesis String]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 678](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0678-valid-parenthesis-string.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
