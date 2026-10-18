---
tags:
  - leetcode
problem_number: 567
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

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count, s2Count = ([0] * 26, [0] * 26)
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
```

## Complexity

$O(n+m)$ time and $O(1)$ space for the fixed lowercase English alphabet. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Determine whether s2 contains a contiguous permutation of s1. A permutation has the same frequency vector.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc567|LeetCode — LC 567]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Reject when s1 is longer than s2.
2. Count letters in s1 and the first equally sized window of s2.
3. Slide one position at a time, updating the entering and leaving letters; detect equality of all 26 counts.

## Why It Works

Equal-length strings with identical letter counts are permutations of one another.

## Worked Example

**Illustrative input:** `s1 = "ab"`, `s2 = "eidbaooo"`.

**Trace:** Sliding reaches the window ba, whose counts match ab.

**Result:** Return `True`.

## Common Pitfalls

Check the final window too. Update count-match bookkeeping when a count enters or leaves equality.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc567|Coding Practice Index — Permutation In String]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 567](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0567-permutation-in-string.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
