---
tags:
  - leetcode
problem_number: 115
difficulty: "Hard"
pattern: "2-D Dynamic Programming"
languages:
  - Python
---

Count how many subsequences of s equal t, distinguishing choices of source positions.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc115|LeetCode — LC 115]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Use a table for each pair of suffix positions.
2. An empty target has one match; an empty source has zero matches for a nonempty target.
3. Always allow skipping the source character; when characters match, also allow consuming both and add the counts.

## Why It Works

Each matching subsequence either uses the current source position or does not, so the two counts are disjoint.

## Worked Example

**Illustrative input:** `s = "babgbag"`, `t = "bag"`.

**Trace:** Different source choices of b, a, and g can spell the same target.

**Result:** Return `5`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        for i in range(len(s) + 1):
            cache[i, len(t)] = 1
        for j in range(len(t)):
            cache[len(s), j] = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[i, j] = cache[i + 1, j + 1] + cache[i + 1, j]
                else:
                    cache[i, j] = cache[i + 1, j]
        return cache[0, 0]
```

## Complexity

$O((m+1)(n+1))$ time and space under bounded-size integer arithmetic. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Count positional subsequences, not distinct resulting strings. The empty target has one selection, not zero.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc115|Coding Practice Index — Distinct Subsequences]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 115](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0115-distinct-subsequences.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
