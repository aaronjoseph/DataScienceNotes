---
tags:
  - leetcode
problem_number: 647
difficulty: "Medium"
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

    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and (s[l] == s[r]):
            res += 1
            l -= 1
            r += 1
        return res
```

## Complexity

$O(n^2)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Count all palindromic substrings, counting different positions separately even if their text is identical.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc647|LeetCode — LC 647]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. For each position, expand once around that character and once around the following gap.
2. Count every successful matching expansion.
3. Sum across all centers.

## Why It Works

Every palindromic occurrence has one unique center and radius, so it is counted exactly once.

## Worked Example

**Illustrative input:** `s = "aaa"`.

**Trace:** There are three one-character palindromes, two aa occurrences, and one aaa.

**Result:** Return `6`.

## Common Pitfalls

Count occurrences rather than unique strings. Single characters are palindromes.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc647|Coding Practice Index — Palindromic Substrings]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 647](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0647-palindromic-substrings.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
