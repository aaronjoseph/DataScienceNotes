---
tags:
  - leetcode
problem_number: 76
difficulty: "Hard"
pattern: "Sliding Window"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0076 - Minimum Window Substring.png|700]]

## Overview

Find the shortest substring of s containing all characters of t, including repeated requirements.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc76|LeetCode — LC 76]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Count required characters and maintain window counts.
2. Expand right until every required character count is met.
3. While valid, record the window and shrink left; stop shrinking when a required count falls short.

## Why It Works

For each right endpoint, shrinking explores its shortest valid window before any necessary character is lost.

## Worked Example

**Illustrative input:** `s = "ADOBECODEBANC"`, `t = "ABC"`.

**Trace:** After obtaining coverage, repeated shrinking eventually finds BANC.

**Result:** Return `"BANC"`.

## Common Pitfalls

Count multiplicities, not just distinct letters. Return an empty string when coverage is impossible.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc76|Coding Practice Index — Minimum Window Substring]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        countT, window = ({}, {})
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = (0, len(countT))
        res, resLen = ([-1, -1], float('infinity'))
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if resLen != float('infinity') else ''
```

## Complexity

$O(n+m)$ expected time and $O(u)$ space for the two string lengths and tracked alphabet, excluding the returned substring. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 76](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0076-minimum-window-substring.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
