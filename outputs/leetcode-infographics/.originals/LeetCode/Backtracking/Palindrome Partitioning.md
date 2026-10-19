---
tags:
  - leetcode
problem_number: 131
difficulty: "Medium"
pattern: "Backtracking"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def partition(self, s: str) -> List[List[str]]:
        res, part = ([], [])

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = (l + 1, r - 1)
        return True
```

## Complexity

$O(n2^n)$ conservative worst-case time including palindrome checks and output; $O(n)$ path and recursion storage excluding results. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Split a string into all possible lists of palindromic substrings.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc131|LeetCode — LC 131]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. From the current start index, try every possible ending index.
2. Use a two-pointer check to decide whether that substring is a palindrome.
3. If valid, append it, recurse from its end, then undo; record a copied partition when the string is fully consumed.

## Why It Works

Every valid partition has a palindromic first piece, and recursion enumerates exactly its valid suffix partitions.

## Worked Example

**Illustrative input:** `s = "aab"`.

**Trace:** Choose a then a then b, or choose aa then b.

**Result:** Return `[["a", "a", "b"], ["aa", "b"]]`.

## Common Pitfalls

A palindrome must read the same in both directions. The partition must cover every character with no overlap or gaps.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc131|Coding Practice Index — Palindrome Partitioning]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 131](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0131-palindrome-partitioning.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
