---
tags:
  - leetcode
problem_number: 49
difficulty: "Medium"
pattern: "Arrays & Hashing"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0049 - Group Anagrams.png|700]]

## Overview

Group strings that are anagrams. Use a character-count tuple as a dictionary key.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc49|LeetCode — LC 49]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. For each word, build 26 counts for lowercase English letters.
2. Convert the count list to an immutable tuple and append the word to that group.
3. Return the dictionary's groups.

## Why It Works

Two words share a count tuple exactly when their letter multiplicities match.

## Worked Example

**Illustrative input:** `strs = ["eat", "tea", "bat"]`.

**Trace:** The first two words share a signature; bat has another.

**Result:** Return groups `[["eat", "tea"], ["bat"]]` in any order.

## Common Pitfalls

The 26-slot implementation assumes lowercase English letters. Dictionary keys must be immutable.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc49|Coding Practice Index — Group Anagrams]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
import collections

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
```

## Complexity

$O(L)$ expected time for `L` total characters; $O(g)$ signature storage for `g` groups with a fixed alphabet, plus $O(n)$ word references. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 49](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0049-group-anagrams.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
