---
tags:
  - leetcode
problem_number: 21
difficulty: "Easy"
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

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return dummy.next
```

## Complexity

$O(n+m)$ time and $O(1)$ extra space for iterative node reuse. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Merge two ascending linked lists by repeatedly linking the smaller remaining head.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc21|LeetCode — LC 21]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Create a dummy head and a tail pointer.
2. While both lists are nonempty, attach the smaller head and advance that list and the tail.
3. Attach the entire remaining suffix and return dummy.next.

## Why It Works

The smaller head is the smallest unmerged value, so the growing output stays sorted.

## Worked Example

**Illustrative input:** Lists `1 → 4` and `2 → 3`.

**Trace:** Choose 1, 2, and 3, then attach the remaining 4.

**Result:** Return `1 → 2 → 3 → 4`.

## Common Pitfalls

The implementation reuses and relinks input nodes. An empty input is handled by attaching the other list.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc21|Coding Practice Index — Merge Two Sorted Lists]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 21](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0021-merge-two-sorted-lists.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
