---
tags:
  - leetcode
problem_number: 20
difficulty: "Easy"
pattern: "Stack"
languages:
  - Python
---

Check whether brackets are balanced and properly nested. Match each closing bracket with the latest unmatched opener.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc20|LeetCode — LC 20]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Push every opening bracket onto a stack.
2. For a closing bracket, reject an empty stack or a mismatching top; otherwise pop.
3. Accept only when the final stack is empty.

## Why It Works

Nested brackets must close in reverse order of opening, exactly matching stack order.

## Worked Example

**Illustrative input:** `s = "([)]"`.

**Trace:** When ) arrives, the top opener is [ rather than (.

**Result:** Return `False`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def isValid(self, s: str) -> bool:
        bracketMap = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c not in bracketMap:
                stack.append(c)
                continue
            if not stack or stack[-1] != bracketMap[c]:
                return False
            stack.pop()
        return not stack
```

## Complexity

$O(n)$ time and $O(n)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

An equal number of openers and closers is insufficient. Reject unmatched closing and leftover opening brackets.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc20|Coding Practice Index — Valid Parentheses]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 20](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0020-valid-parentheses.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
