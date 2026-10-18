---
tags:
  - leetcode
problem_number: 1143
difficulty: "Medium"
pattern: "2-D Dynamic Programming"
languages:
  - Python
---

Find the longest subsequence shared by two strings, without requiring consecutive positions.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc1143|LeetCode — LC 1143]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Use a two-dimensional table for the best shared subsequence length of each pair of suffixes.
2. If the current characters match, include one and advance both.
3. Otherwise take the larger result from skipping a character in either string; empty suffixes contribute zero.

## Why It Works

A matching pair can extend an optimal common suffix; with a mismatch, at least one current character must be skipped.

## Worked Example

**Illustrative input:** `text1 = "abcde"`, `text2 = "ace"`.

**Trace:** Matching a, c, and e in order builds a shared sequence of length three.

**Result:** Return `3`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]
```

## Complexity

$O(mn)$ time and $O(mn)$ space for the two string lengths. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

A subsequence may skip characters; a substring may not. Matching characters do not require consecutive indices.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc1143|Coding Practice Index — Longest Common Subsequence]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 1143](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/1143-longest-common-subsequence.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
