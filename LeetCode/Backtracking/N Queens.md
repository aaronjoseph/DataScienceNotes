---
tags:
  - leetcode
problem_number: 51
difficulty: "Hard"
pattern: "Backtracking"
languages:
  - Python
---

Place n queens on an n by n board so that no two attack one another.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc51|LeetCode — LC 51]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Place one queen per row and track occupied columns and both diagonal identifiers.
2. Try only columns whose column and diagonals are free.
3. Mark a choice, recurse to the next row, and undo it; copy the completed board after n rows.

## Why It Works

One queen per row removes row conflicts, while column and diagonal sets reject every remaining attack relation.

## Worked Example

**Illustrative input:** `n = 4`.

**Trace:** One valid placement uses columns [1, 3, 0, 2] for successive rows.

**Result:** The search returns this board and its mirror.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [['.'] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or r + c in posDiag or r - c in negDiag:
                    continue
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'
                backtrack(r + 1)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'
        backtrack(0)
        return res
```

## Complexity

A loose search bound is $O(n\,n!+Qn^2)$ time for `Q` solutions; $O(n^2)$ auxiliary board storage. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Undo all three constraint sets after each choice. Diagonals are identified by row-plus-column and row-minus-column.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc51|Coding Practice Index — N Queens]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 51](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0051-n-queens.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
