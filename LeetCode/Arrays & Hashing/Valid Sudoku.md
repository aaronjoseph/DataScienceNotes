---
tags:
  - leetcode
problem_number: 36
difficulty: "Medium"
pattern: "Arrays & Hashing"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0036 - Valid Sudoku.png|700]]

## Overview

Check whether the filled cells of a 9 by 9 Sudoku violate any row, column, or 3 by 3 box rule.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc36|LeetCode — LC 36]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Keep a set for each row, column, and box.
2. Skip empty cells. Locate a box using integer division of both coordinates by 3.
3. Reject a repeated digit in any associated set; otherwise insert it in all three.

## Why It Works

Each filled digit is checked against every constraint that contains it.

## Worked Example

**Illustrative input:** Two 5 digits occupy different cells of the first row.

**Trace:** The second 5 is found in that row's set.

**Result:** Return `False`.

## Common Pitfalls

Validity of the current cells does not establish that the puzzle is solvable. Ignore dots rather than recording them.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc36|Coding Practice Index — Valid Sudoku]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
import collections

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r // 3, c // 3]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r // 3, c // 3].add(board[r][c])
        return True
```

## Complexity

$O(1)$ time and space for the fixed 81-cell board. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 36](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0036-valid-sudoku.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
