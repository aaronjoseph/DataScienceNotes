---
tags:
  - leetcode
problem_number: 72
difficulty: "Medium"
pattern: "2-D Dynamic Programming"
languages:
  - Python
---

Find the minimum insertions, deletions, and replacements needed to transform one string into another.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc72|LeetCode — LC 72]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Build a table for the edit distance between each pair of suffixes.
2. If one suffix is empty, its distance is the other suffix's length.
3. Matching characters advance both for free; otherwise take one plus the minimum of insertion, deletion, and replacement successor states.

## Why It Works

Every optimal edit script begins with a free match or one of the three allowed edits; solving all successor states gives its minimum cost.

## Worked Example

**Illustrative input:** `word1 = "cat"`, `word2 = "cut"`.

**Trace:** Keep c, replace a with u, and keep t.

**Result:** Return `1`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float('inf')] * (len(word2) + 1) for i in range(len(word1) + 1)]
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]
```

## Complexity

$O(mn+m+n)$ time and space for source lengths `m` and `n`. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

This is Levenshtein distance with unit edit costs. Swapping adjacent characters is not an allowed single operation.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc72|Coding Practice Index — Edit Distance]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 72](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0072-edit-distance.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
