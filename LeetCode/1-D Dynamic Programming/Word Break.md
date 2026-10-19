---
tags:
  - leetcode
problem_number: 139
difficulty: "Medium"
pattern: "1-D Dynamic Programming"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0139 - Word Break.png|700]]

## Overview

Decide whether a string can be segmented into dictionary words. Solve suffix feasibility from the end.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc139|LeetCode — LC 139]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Set the empty suffix to feasible.
2. For each starting position moving backward, try each dictionary word that matches there.
3. Mark the suffix feasible if the matched word is followed by a feasible remaining suffix; stop searching that position once successful.

## Why It Works

Any valid segmentation consists of a first dictionary word and a valid segmentation of the remainder.

## Worked Example

**Illustrative input:** `s = "applepenapple"`, dictionary `["apple", "pen"]`.

**Trace:** The suffix apple is feasible, which makes penapple feasible, then the full string.

**Result:** Return `True`.

## Common Pitfalls

This is exact segmentation with reusable words, not substring presence. Greedily choosing the longest matching word can fail.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc139|Coding Practice Index — Word Break]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
```

## Complexity

$O(nDL)$ worst-case time for `D` words of maximum length `L`, accounting for Python slicing/comparison; $O(n+L)$ auxiliary space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 139](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0139-word-break.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
