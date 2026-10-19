---
tags:
  - leetcode
problem_number: 155
difficulty: "Medium"
pattern: "Stack"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0155 - Min Stack.png|700]]

## Overview

Design a stack supporting push, pop, top, and minimum queries in constant time.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc155|LeetCode — LC 155]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Store pushed values in one stack and the minimum so far in a parallel stack.
2. On push, append the smaller of the new value and previous minimum.
3. Pop both stacks together; answer top and minimum from their respective tops.

## Why It Works

The minimum stack records the correct answer for every surviving stack prefix.

## Worked Example

**Illustrative input:** Push 3, then 1, then 1.

**Trace:** After one pop, a 1 remains and its matching prefix minimum is still 1.

**Result:** `getMin()` returns `1`.

## Common Pitfalls

Duplicate minima need separate history entries. The judge guarantees valid operations on nonempty stacks.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc155|Coding Practice Index — Min Stack]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
```

## Complexity

$O(1)$ time per operation and $O(n)$ storage for `n` pushed values. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 155](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0155-min-stack.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
