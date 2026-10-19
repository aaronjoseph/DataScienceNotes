---
tags:
  - leetcode
problem_number: 269
difficulty: "Hard"
pattern: "Advanced Graphs"
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

    def alienOrder(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}
        for i in range(len(words) - 1):
            w1, w2 = (words[i], words[i + 1])
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ''
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]
            visited[char] = True
            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True
            visited[char] = False
            res.append(char)
        for char in adj:
            if dfs(char):
                return ''
        res.reverse()
        return ''.join(res)
```

## Complexity

$O(S+V+E)$ time and $O(V+E)$ auxiliary space for total input characters `S`. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Infer a valid character order from lexicographically sorted words in an unknown alphabet.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc269|LeetCode — LC 269]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Create graph vertices for every character, including isolated ones.
2. For each adjacent word pair, add an ordering edge at the first differing position; reject a longer word preceding its exact prefix.
3. Topologically sort with active-path cycle detection and reverse DFS finishing order.

## Why It Works

Only the first differing position constrains lexicographic order, and any topological order satisfies all such constraints.

## Worked Example

**Illustrative input:** Words `["za", "zb", "ca", "cb"]`.

**Trace:** Adjacent comparisons imply a before b and z before c.

**Result:** Any order satisfying both relations is valid.

## Common Pitfalls

A prefix violation is invalid even without a graph cycle. Preserve unconstrained characters and deduplicate edges.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc269|Coding Practice Index — Alien Dictionary]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 269](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0269-alien-dictionary.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
