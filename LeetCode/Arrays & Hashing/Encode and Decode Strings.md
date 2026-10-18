---
tags:
  - leetcode
problem_number: 271
difficulty: "Medium"
pattern: "Arrays & Hashing"
languages:
  - Python
---

Encode a list of strings into one string and decode it exactly, even when the strings contain separators.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc271|LeetCode — LC 271]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Encode each string as its character length, a # separator, and the string itself.
2. While decoding, scan digits up to the next # and parse the length.
3. Read exactly that many characters, append the recovered string, and continue.

## Why It Works

The length determines the payload boundary, so separators inside a payload cannot confuse the decoder.

## Worked Example

**Illustrative input:** `strs = ["a#", ""]`.

**Trace:** Encode as `"2#a#0#"`, then consume payload lengths 2 and 0.

**Result:** Recover `["a#", ""]`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def encode(self, strs):
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return ''.join(res)

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
```

## Complexity

$O(L+n)$ time and output space for `L` payload characters and `n` strings, including length headers. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Distinguish an empty list from a list containing an empty string. Character counts and byte counts must use the same convention.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc271|Coding Practice Index — Encode and Decode Strings]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 271](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0271-encode-and-decode-strings.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
