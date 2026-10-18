---
tags:
  - leetcode
problem_number: 424
difficulty: "Medium"
pattern: "Sliding Window"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            if r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
        return r - l + 1
```

## Complexity

$O(n)$ expected time and $O(u)$ space; the uppercase alphabet bounds `u` by 26. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Find the longest substring that can become one repeated character after at most k replacements.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc424|LeetCode — LC 424]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Count characters as the right endpoint advances and track the greatest frequency seen.
2. If the window length exceeds that historical frequency plus k, move its left endpoint once.
3. Return the final nondecreasing window size.

## Why It Works

A historical frequency can keep an invalid window temporarily, but the window cannot grow beyond a size supported by a previously achievable replacement budget.

## Worked Example

**Illustrative input:** `s = "AABABBA"`, `k = 1`.

**Trace:** The window AABA can become AAAA by replacing its B.

**Result:** Return `4`.

## Common Pitfalls

A historical maximum supports computing the length, not reporting the current window as a valid answer. Use fresh counts if extracting the substring.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc424|Coding Practice Index — Longest Repeating Character Replacement]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 424](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0424-longest-repeating-character-replacement.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
