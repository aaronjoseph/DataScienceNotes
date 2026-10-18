---
tags:
  - leetcode
problem_number: 3
difficulty: "Medium"
pattern: "Sliding Window"
languages:
  - Python
---

Find the longest contiguous substring with no repeated characters. Maintain a window whose characters are unique.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc3|LeetCode — LC 3]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Track the current window in a set.
2. When the next character is already present, remove leftmost characters until that duplicate leaves.
3. Insert the new character and update the best window length.

## Why It Works

After shrinking, the window is the longest valid suffix ending at the current right endpoint.

## Worked Example

**Illustrative input:** `s = "abba"`.

**Trace:** The second b forces both a and the earlier b out; the final window is ba.

**Result:** Return `2`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
```

## Complexity

$O(n)$ expected time and $O(u)$ space for distinct characters in the window. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Remove characters in a loop, not only once. A substring must be contiguous.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc3|Coding Practice Index — Longest Substring Without Repeating Characters]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 3](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0003-longest-substring-without-repeating-characters.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
