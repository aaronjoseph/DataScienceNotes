---
tags:
  - leetcode
problem_number: 19
difficulty: "Medium"
pattern: "Linked List"
languages:
  - Python
---

Remove the nth node from the end of a singly linked list in one forward traversal.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc19|LeetCode — LC 19]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Use a dummy node before the head.
2. Advance a right pointer n nodes ahead of a left pointer positioned at the dummy.
3. Move both until right reaches null; bypass the node after left and return dummy.next.

## Why It Works

The fixed gap leaves left immediately before the node to remove when right reaches the end.

## Worked Example

**Illustrative input:** List `1 → 2 → 3`, `n = 3`.

**Trace:** The right pointer reaches null after the initial gap; left remains at the dummy.

**Result:** Return `2 → 3`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations

class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
```

## Complexity

$O(L)$ time and $O(1)$ extra space for list length `L`. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

The dummy handles removing the head. The problem guarantees n is within the list length.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc19|Coding Practice Index — Remove Nth Node From End of List]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 19](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0019-remove-nth-node-from-end-of-list.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
