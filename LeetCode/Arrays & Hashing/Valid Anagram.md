---
tags:
  - leetcode
problem_number: 242
difficulty: "Easy"
pattern: "Arrays & Hashing"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0242 - Valid Anagram.png|700]]

## Overview

Decide whether two strings contain exactly the same characters with the same multiplicities.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc242|LeetCode — LC 242]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Reject unequal lengths.
2. Count each character in each string using two maps.
3. Compare the maps, including the counts.

## Why It Works

Reordering preserves every character count; equal counts are also sufficient to reconstruct the same multiset.

## Worked Example

**Illustrative input:** `s = "aab"`, `t = "aba"`.

**Trace:** Both maps contain two a characters and one b.

**Result:** Return `True`.

## Common Pitfalls

Sets alone lose multiplicity. With a fixed lowercase alphabet the count storage is constant.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc242|Coding Practice Index — Valid Anagram]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = ({}, {})
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
```

## Complexity

$O(n)$ expected time and $O(u)$ space, where `u` is the number of distinct characters. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 242](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0242-valid-anagram.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
