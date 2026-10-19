---
tags:
  - leetcode
problem_number: 206
difficulty: "Easy"
pattern: "Linked List"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0206 - Reverse Linked List.png|700]]

## Overview

Reverse a singly linked list by rewiring each node's next pointer.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc206|LeetCode — LC 206]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Maintain a reversed prefix ending at prev and an unread suffix beginning at curr.
2. Save curr.next before redirecting curr.next to prev.
3. Advance both pointers and return prev when the unread suffix is empty.

## Why It Works

Each iteration transfers exactly one node from the unread suffix to the reversed prefix without losing the remaining list.

## Worked Example

**Illustrative input:** List `1 → 2 → 3`.

**Trace:** First make 1 point to null, then 2 to 1, then 3 to 2.

**Result:** Return the head of `3 → 2 → 1`.

## Common Pitfalls

Save the original next pointer before changing it. An empty list returns null.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc206|Coding Practice Index — Reverse Linked List]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations

class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = (None, head)
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 206](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0206-reverse-linked-list.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
