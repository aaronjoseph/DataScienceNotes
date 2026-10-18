---
tags:
  - leetcode
problem_number: 143
difficulty: "Medium"
pattern: "Linked List"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations

class Solution:

    def reorderList(self, head: ListNode) -> None:
        slow, fast = (head, head.next)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first, second = (head, prev)
        while second:
            tmp1, tmp2 = (first.next, second.next)
            first.next = second
            second.next = tmp1
            first, second = (tmp1, tmp2)
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Reorder a list by alternating its first and last remaining nodes, modifying pointers in place.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc143|LeetCode — LC 143]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Use slow and fast pointers to locate the midpoint.
2. Detach the second half and reverse it.
3. Weave nodes alternately from the first half and reversed second half, saving both next pointers before relinking.

## Why It Works

The reversed second half exposes last, second-last, and later nodes in exactly the order needed for interleaving.

## Worked Example

**Illustrative input:** List `1 → 2 → 3 → 4 → 5`.

**Trace:** Split after 3, reverse the tail to 5 → 4, then weave.

**Result:** The list becomes `1 → 5 → 2 → 4 → 3`.

## Common Pitfalls

Detach the halves to avoid cycles. The first half may contain one additional node.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc143|Coding Practice Index — Reorder List]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 143](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0143-reorder-list.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
