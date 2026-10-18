---
tags:
  - leetcode
problem_number: 91
difficulty: "Medium"
pattern: "1-D Dynamic Programming"
languages:
  - Python
---

Count decodings of a digit string under the mapping 1 to A through 26 to Z.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc91|LeetCode — LC 91]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Memoize the number of decodings starting at each index; the fully consumed suffix has one decoding.
2. A leading zero at the current index contributes no decoding.
3. Try one digit, and also try two digits when they form a value from 10 through 26; sum the results.

## Why It Works

Every decoding starts with either a valid one-digit letter or a valid two-digit letter, and those cases cannot overlap.

## Worked Example

**Illustrative input:** `s = "226"`.

**Trace:** The valid splits are 2

**Result:** 2

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)
```

## Complexity

$O(n)$ time and $O(n)$ memo/recursion space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Zero cannot stand alone, while 10 and 20 are valid pairs. Memoization does not remove Python recursion-depth limits.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc91|Coding Practice Index — Decode Ways]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 91](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0091-decode-ways.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
