---
tags:
  - leetcode
problem_number: 79
difficulty: "Medium"
pattern: "Backtracking"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0079 - Word Search.png|700]]

## Overview

Determine whether a word can be traced through horizontally or vertically adjacent board cells without reusing a cell.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc79|LeetCode — LC 79]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Start a depth-first search at each cell matching the first letter.
2. At each step, check bounds, the expected character, and path-local visitation.
3. Mark the cell, try four neighbors for the next character, and unmark it on return.

## Why It Works

Backtracking enumerates all admissible adjacent paths while preventing repeated use of a cell within one candidate path.

## Worked Example

**Illustrative input:** `board = [["A", "B"], ["C", "D"]]`, `word = "ABD"`.

**Trace:** Follow top-left A, top-right B, then bottom-right D.

**Result:** Return `True`.

## Common Pitfalls

Visited state must be undone after failed paths. Diagonal movement is not allowed; starting from the rarer endpoint is an optional pruning heuristic.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc79|Coding Practice Index — Word Search]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
from collections import Counter

class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = (len(board), len(board[0]))
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (word[i] != board[r][c]) or ((r, c) in path):
                return False
            path.add((r, c))
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            path.remove((r, c))
            return res
        count = sum(map(Counter, board), Counter())
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
```

## Complexity

A conservative bound is $O(RC\,4^L)$ time and $O(L)$ path space for word length `L`. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 79](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0079-word-search.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
