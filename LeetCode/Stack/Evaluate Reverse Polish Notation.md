---
tags:
  - leetcode
problem_number: 150
difficulty: "Medium"
pattern: "Stack"
languages:
  - Python
---

Evaluate a postfix expression using a stack of computed operands.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc150|LeetCode — LC 150]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Push numeric tokens.
2. For an operator, pop the right operand first and then the left, apply the operator, and push the result.
3. Return the only remaining value after all tokens.

## Why It Works

Each operator consumes the two complete expressions immediately before it, which are the stack's latest values.

## Worked Example

**Illustrative input:** `tokens = ["7", "2", "-"]`.

**Trace:** Pop right operand 2 and left operand 7, then subtract.

**Result:** Return `5`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
                continue
            right, left = stack.pop(), stack.pop()
            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            else:
                quotient = abs(left) // abs(right)
                result = -quotient if (left < 0) != (right < 0) else quotient
            stack.append(result)
        return stack[0]
```

## Complexity

$O(n)$ time and $O(n)$ extra space for `n` tokens under bounded-integer arithmetic. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Subtraction and division preserve operand order. Division truncates toward zero; use integer arithmetic to avoid floating-point rounding.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc150|Coding Practice Index — Evaluate Reverse Polish Notation]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 150](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0150-evaluate-reverse-polish-notation.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
