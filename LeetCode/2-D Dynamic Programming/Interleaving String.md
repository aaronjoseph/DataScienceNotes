---
tags:
  - leetcode
problem_number: 97
difficulty: "Medium"
pattern: "2-D Dynamic Programming"
languages:
  - Python
---

Determine whether a third string interleaves two source strings while preserving each source's internal order.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc97|LeetCode — LC 97]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Reject if the two source lengths do not sum to the target length.
2. Use a table indexed by the next unconsumed position in each source.
3. At each state, consume a matching next character from either source if its successor state succeeds; the fully consumed state is true.

## Why It Works

The two source positions determine the next target position and enumerate exactly the allowed order-preserving choices.

## Worked Example

**Illustrative input:** `s1 = "ab"`, `s2 = "cd"`, `s3 = "acbd"`.

**Trace:** Take a from s1, c from s2, b from s1, then d from s2.

**Result:** Return `True`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
```

## Complexity

$O((m+1)(n+1))$ time and space for source lengths `m` and `n`. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Matching total character counts alone does not preserve order. If both next characters match, either branch may be needed.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc97|Coding Practice Index — Interleaving String]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 97](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0097-interleaving-string.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
