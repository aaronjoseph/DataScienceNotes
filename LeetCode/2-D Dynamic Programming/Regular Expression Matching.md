---
tags:
  - leetcode
problem_number: 10
difficulty: "Hard"
pattern: "2-D Dynamic Programming"
languages:
  - Python
---

Match an entire string against a pattern containing dot and star, where star repeats its preceding character zero or more times.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc10|LeetCode — LC 10]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Define suffix-match states for a string position and pattern position; only both empty suffixes match by default.
2. If the next pattern character is star, either skip the character-star pair or consume one matching string character while keeping that pair.
3. Otherwise require a current-character match and advance both positions; fill the table backward.

## Why It Works

The star cases exhaust zero occurrences and one-or-more occurrences, while ordinary tokens must consume one character.

## Worked Example

**Illustrative input:** `s = "aa"`, `p = "a*"`.

**Trace:** Consume a twice through the star branch, then skip the pair to match empty suffixes.

**Result:** Return `True`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        cache = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        cache[len(s)][len(p)] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                if j + 1 < len(p) and p[j + 1] == '*':
                    cache[i][j] = cache[i][j + 2]
                    if match:
                        cache[i][j] = cache[i + 1][j] or cache[i][j]
                elif match:
                    cache[i][j] = cache[i + 1][j + 1]
        return cache[0][0]
```

## Complexity

$O((m+1)(n+1))$ time and space for string and pattern lengths. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Star is not a standalone wildcard and does not mean arbitrary text. Matching is for the whole string, not a contained substring.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc10|Coding Practice Index — Regular Expression Matching]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 10](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0010-regular-expression-matching.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
