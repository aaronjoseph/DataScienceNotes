---
tags:
  - leetcode
problem_number: 5
difficulty: "Medium"
pattern: "1-D Dynamic Programming"
languages:
  - Python
---

Find the longest contiguous palindromic substring by expanding around every possible center.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc5|LeetCode — LC 5]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. For each character position, consider both an odd-length center and the gap after it as an even-length center.
2. Expand outward while the two characters match.
3. Track only the best boundaries and slice the answer once after all centers are checked.

## Why It Works

Every palindrome has exactly one character center or between-character center, so some expansion discovers the longest one.

## Worked Example

**Illustrative input:** `s = "cbbd"`.

**Trace:** The gap between the two b characters expands to bb and stops at mismatched c and d.

**Result:** Return `"bb"`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_start, best_length = 0, 0
        for center in range(len(s)):
            for left, right in ((center, center), (center, center + 1)):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left + 1 > best_length:
                        best_start, best_length = left, right - left + 1
                    left -= 1
                    right += 1
        return s[best_start:best_start + best_length]
```

## Complexity

$O(n^2)$ time and $O(1)$ auxiliary space, excluding the final returned substring. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Check both center types. Repeatedly slicing every improved candidate can add avoidable copying.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc5|Coding Practice Index — Longest Palindromic Substring]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 5](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0005-longest-palindromic-substring.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
