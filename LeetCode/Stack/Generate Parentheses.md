---
tags:
  - leetcode
problem_number: 22
difficulty: "Medium"
pattern: "Stack"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0022 - Generate Parentheses.png|700]]

## Overview

Generate every balanced string containing n pairs of parentheses. Build only prefixes that could still become valid.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc22|LeetCode — LC 22]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Track the numbers of opened and closed parentheses in a mutable path.
2. Add an opening bracket while fewer than n have been used; add a closing bracket only while closes are fewer than opens.
3. Copy the completed path when both counts reach n, undoing each choice after recursion.

## Why It Works

Every generated prefix is balanced so far, and every valid final string follows one of the permitted choices.

## Worked Example

**Illustrative input:** `n = 2`.

**Trace:** From (, either open again or close; the valid completions are (()) and ()().

**Result:** Return `["(())", "()()"]`.

## Common Pitfalls

Do not generate all bracket strings and filter afterward. Save a copy of a mutable path, not its shared reference.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc22|Coding Practice Index — Generate Parentheses]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append(''.join(stack))
                return
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res
```

## Complexity

$O(nC_n)$ time including output copies, where `C_n` is the nth Catalan number; $O(n)$ auxiliary space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 22](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0022-generate-parentheses.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
