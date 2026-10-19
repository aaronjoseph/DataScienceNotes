---
tags:
  - leetcode
problem_number: 141
difficulty: "Easy"
pattern: "Linked List"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0141 - Linked List Cycle.png|700]]

## Overview

Detect a cycle without storing all visited nodes. Move two pointers at different speeds.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc141|LeetCode — LC 141]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Start slow and fast at the head.
2. Move slow once and fast twice while two fast steps exist.
3. Return true if they meet; return false if fast reaches the end.

## Why It Works

Inside a cycle, the relative distance changes by one each iteration and must eventually reach zero.

## Worked Example

**Illustrative input:** List `1 → 2 → 3 → 2…`.

**Trace:** Both pointers enter the loop between nodes 2 and 3 and eventually meet.

**Result:** Return `True`.

## Common Pitfalls

Compare node identity, not repeated values. Check fast and fast.next before taking two steps.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc141|Coding Practice Index — Linked List Cycle]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations

class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = (head, head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 141](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0141-linked-list-cycle.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
