---
tags:
  - leetcode
problem_number: 17
difficulty: "Medium"
pattern: "Backtracking"
languages:
  - Python
---

List all letter strings represented by a sequence of telephone keypad digits from 2 through 9.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc17|LeetCode — LC 17]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Map each digit to its keypad letters.
2. Recursively choose one letter for the current digit and advance one position.
3. Append a completed string after all digits have been consumed; return an empty list for empty input.

## Why It Works

Choosing one option independently per digit enumerates the Cartesian product of all keypad letter sets.

## Worked Example

**Illustrative input:** `digits = "23"`.

**Trace:** Choose a, b, or c first, and d, e, or f second.

**Result:** Return nine strings, from ad through cf in keypad order.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
        if digits:
            backtrack(0, '')
        return res
```

## Complexity

$O(L4^L)$ worst-case time including string creation and output; $O(L^2)$ live prefix-string space in this immutable-string recursion. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Digits 0 and 1 are outside this problem's contract. The letters for 7 are pqrs; output order is unrestricted.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc17|Coding Practice Index — Letter Combinations of a Phone Number]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 17](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0017-letter-combinations-of-a-phone-number.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
