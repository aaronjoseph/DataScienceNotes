---
tags:
  - leetcode
problem_number: 130
difficulty: "Medium"
pattern: "Graphs"
languages:
  - Python
---

Replace O regions fully enclosed by X while preserving any O connected to a boundary.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc130|LeetCode — LC 130]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Flood-fill O cells reachable from any border and mark them safe.
2. Scan the board again.
3. Turn every unmarked O into X, leaving safe cells unchanged.

## Why It Works

An O region is not surrounded exactly when it has a four-directional path to a boundary O.

## Worked Example

**Illustrative input:** `board = [["X", "O", "X"], ["X", "O", "X"], ["X", "X", "X"]]`.

**Trace:** The middle O connects to the top-border O.

**Result:** Both O cells remain unchanged.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def solve(self, board: List[List[str]]) -> None:
        rows, cols = (len(board), len(board[0]))
        flag = set()

        def dfs(r, c):
            if not (r in range(rows) and c in range(cols)) or board[r][c] != 'O' or (r, c) in flag:
                return
            flag.add((r, c))
            return (dfs(r + 1, c), dfs(r - 1, c), dfs(r, c + 1), dfs(r, c - 1))
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows - 1 or (c == cols - 1)) and board[r][c] == 'O':
                    dfs(r, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in flag:
                    board[r][c] = 'X'
```

## Complexity

$O(RC)$ time and $O(RC)$ auxiliary space for the safe set and recursion. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Start from every border, not only the corners. Changes are in place; the function returns no board.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc130|Coding Practice Index — Surrounded Regions]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 130](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0130-surrounded-regions.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
