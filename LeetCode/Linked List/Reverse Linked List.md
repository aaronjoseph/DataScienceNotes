---
tags:
  - leetcode
  - linked-list
problem_number: 206
difficulty: "Easy"
pattern: "Linked List"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.[^implementation]

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

- **Time:** $O(n)$ worst-case, where $n$ is the number of nodes in the list; every node is visited once.
- **Auxiliary space:** $O(1)$, using only pointer variables (`prev`, `curr`, `temp`) and modifying links in place (excludes the input list). A recursive version takes $O(n)$ call-stack space.

## Algorithm at a glance

![[Attachements/LeetCode/LC0206 - Reverse Linked List.png|700]]

## Overview

Reverse a singly linked list in place by redirecting every node's `next` pointer to its predecessor and returning the new head.[^implementation] This three-pointer reversal loop is a core building block reused inside [[LeetCode/Linked List/Reorder List|Reorder List]] (LC 143) and [[LeetCode/Linked List/Reverse Nodes In K Group|Reverse Nodes In K Group]] (LC 25).

Problem link: [[Job Interviews/Coding Practice Index#^lc206|LeetCode — LC 206]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Maintain two pointers: `prev` (head of the already-reversed prefix, starting at `None`) and `curr` (head of the remaining unreversed suffix, starting at `head`).
2. While `curr` is not `None`:
   - Save `temp = curr.next` so the rest of the list is not lost.
   - Reverse the link: `curr.next = prev`.
   - Advance both pointers: `prev = curr`, `curr = temp`.
3. When `curr` becomes `None`, `prev` points to the new head; return `prev`.

## Why It Works

At the start of every iteration, `prev` heads a valid reversed list of all nodes strictly before `curr`, and `curr` heads the untouched remainder of the original list. Each step moves one node from the front of the suffix onto the front of the reversed prefix, preserving all remaining links via `temp`.

## Worked Example

**Inputs:** `head = 1 → 2 → 3 → None`.

1. **Initial:** `prev = None`, `curr = 1`.
2. **Step 1:** Save `temp = 2`, set `1.next = None`, advance to `prev = 1`, `curr = 2`. Reversed prefix: `1 → None`.
3. **Step 2:** Save `temp = 3`, set `2.next = 1`, advance to `prev = 2`, `curr = 3`. Reversed prefix: `2 → 1 → None`.
4. **Step 3:** Save `temp = None`, set `3.next = 2`, advance to `prev = 3`, `curr = None`. Loop ends.

**Outcome:** Returns `prev`, the head of `3 → 2 → 1 → None`.

## Common Pitfalls

- **Overwriting `curr.next` before saving it:** Always store `temp = curr.next` first, or the remaining suffix becomes unreachable.
- **Returning `curr` instead of `prev`:** When the loop exits, `curr` is `None`; `prev` is the new head.
- **Empty or single-node list:** If `head` is `None`, the loop never runs and `prev` (`None`) is returned cleanly. If there is one node, it points to `None` and is returned unchanged.

## Related Notes

- [[LeetCode/Linked List/Reorder List|Reorder List]] — Reverses the second half of a list using this exact loop.
- [[LeetCode/Linked List/Reverse Nodes In K Group|Reverse Nodes In K Group]] — Applies bounded reversal to each group of $k$ nodes.
- [[Job Interviews/Coding Practice Index#^lc206|Coding Practice Index — Reverse Linked List]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 206](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0206-reverse-linked-list.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
