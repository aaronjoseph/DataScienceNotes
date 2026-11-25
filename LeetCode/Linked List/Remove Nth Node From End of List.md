---
tags:
  - leetcode
  - linked-list
problem_number: 19
difficulty: "Medium"
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

- **Time:** $O(L)$ worst-case, where $L$ is the number of nodes in the list; `right` traverses the list once from `head` to `None`.
- **Auxiliary space:** $O(1)$, using only a sentinel `dummy` node and two pointers (`left`, `right`).

## Algorithm at a glance

![[Attachements/LeetCode/LC0019 - Remove Nth Node From End of List.png|700]]

## Overview

Remove the $n$-th node from the end of a singly linked list in a single forward pass using two pointers separated by a fixed gap.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc19|LeetCode — LC 19]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Create a sentinel node `dummy = ListNode(0, head)` so removing the original `head` needs no special case.
2. Place `left = dummy` and `right = head`, then advance `right` by `n` steps. Now `right` is $n + 1$ edges ahead of `left`.
3. Advance both `left` and `right` one step at a time until `right` becomes `None`.
4. `left` now points to the node immediately **before** the target; bypass the target with `left.next = left.next.next`.
5. Return `dummy.next`.

## Why It Works

Because `left` starts at `dummy` (one step before `head`) and `right` advances `n` steps from `head`, the distance from `left` to `right` is always $n + 1$ steps. Moving both pointers in lockstep preserves that distance, so when `right` reaches `None` (one step past the tail), `left` sits at the $(n + 1)$-th node from the end — directly before the node to delete.

## Worked Example

**Inputs:** `head = 1 → 2 → 3 → None`, `n = 3` (removing the head).

1. **Setup:** `dummy → 1 → 2 → 3 → None`, `left = dummy`, `right = 1`.
2. **Create gap (`n = 3` steps):** `right` moves `1 → 2 → 3 → None`.
3. **Lockstep loop:** `right` is already `None`, so the loop does not run; `left` stays at `dummy`.
4. **Delete:** `dummy.next = dummy.next.next` (`1` is bypassed, so `dummy.next = 2`).

**Outcome:** Returns `dummy.next`, the head of `2 → 3 → None`.

## Common Pitfalls

- **Omitting the `dummy` node:** Without a sentinel before `head`, removing the first node ($n = L$) requires a separate branch because there is no predecessor node.
- **Off-by-one pointer gap:** Starting `left = head` instead of `dummy` lands `left` *on* the target node rather than *before* it, making deletion impossible in a singly linked list.
- **Returning `head` instead of `dummy.next`:** If the original `head` was removed, `head` still points to the deleted node; always return `dummy.next`.

## Related Notes

- [[LeetCode/Linked List/Merge Two Sorted Lists|Merge Two Sorted Lists]] — Another core use of the `dummy` sentinel head pattern.
- [[LeetCode/Linked List/Reorder List|Reorder List]] — Another two-pointer positioning pattern on singly linked lists.
- [[Job Interviews/Coding Practice Index#^lc19|Coding Practice Index — Remove Nth Node From End of List]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 19](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0019-remove-nth-node-from-end-of-list.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
