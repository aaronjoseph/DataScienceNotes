---
tags:
  - leetcode
  - linked-list
problem_number: 21
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

- **Time:** $O(n + m)$ worst-case, where $n$ and $m$ are the lengths of `list1` and `list2`. Each loop iteration advances one of the two pointers by one node, and attaching the leftover tail is $O(1)$.
- **Auxiliary space:** $O(1)$, reusing the existing input nodes and allocating only one sentinel `dummy` node (a recursive merge uses $O(n + m)$ call-stack space).

## Algorithm at a glance

![[Attachements/LeetCode/LC0021 - Merge Two Sorted Lists.png|700]]

## Overview

Merge two sorted singly linked lists into a single sorted list by splicing their existing nodes together in ascending order.[^implementation] This is the core subroutine reused inside [[LeetCode/Linked List/Merge K Sorted Lists|Merge K Sorted Lists]] (LC 23).

Problem link: [[Job Interviews/Coding Practice Index#^lc21|LeetCode — LC 21]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Create a sentinel `dummy = ListNode()` and a tail pointer `node = dummy` so you never need a special case for the first output node.
2. While both `list1` and `list2` are non-empty:
   - Compare `list1.val` and `list2.val`.
   - Attach the smaller node to `node.next` and advance that input pointer.
   - Advance `node = node.next`.
3. Once one list is exhausted, attach the entire remaining suffix in one pointer assignment (`node.next = list1 or list2`).
4. Return `dummy.next`.

## Why It Works

Both input lists are sorted, so the smaller of the two current heads is guaranteed to be the smallest unmerged element remaining across both lists. Appending it maintains sorted order, and once one list becomes empty, every node in the other list is already sorted and greater than or equal to everything merged so far.

## Worked Example

**Inputs:** `list1 = 1 → 4`, `list2 = 2 → 3`.

1. **Step 1:** Compare `1 < 2`. Attach `1`, advance `list1` to `4`. Merged: `dummy → 1`.
2. **Step 2:** Compare `4 < 2` (false). Attach `2`, advance `list2` to `3`. Merged: `dummy → 1 → 2`.
3. **Step 3:** Compare `4 < 3` (false). Attach `3`, advance `list2` to `None`. Merged: `dummy → 1 → 2 → 3`.
4. **Tail attachment:** `list2` is `None`, so set `node.next = list1` (`4 → None`).

**Outcome:** Returns `dummy.next`, the head of `1 → 2 → 3 → 4`.

## Common Pitfalls

- **Returning `dummy` instead of `dummy.next`:** The sentinel node holds a placeholder value and must not be part of the returned list.
- **Forgetting to advance `node`:** If `node = node.next` is omitted, every iteration overwrites `dummy.next`.
- **Looping through the leftover tail unnecessarily:** Because the remaining list is already linked and sorted, `node.next = list1 or list2` attaches it in $O(1)$ time.
- **In-place mutation:** This implementation reuses and relinks the original input nodes rather than allocating fresh copies.

## Related Notes

- [[LeetCode/Linked List/Merge K Sorted Lists|Merge K Sorted Lists]] — Repeatedly calls this two-list merge in pairwise divide-and-conquer rounds.
- [[LeetCode/Linked List/Add Two Numbers|Add Two Numbers]] — Another sentinel-head (`dummy`) traversal over two lists.
- [[Job Interviews/Coding Practice Index#^lc21|Coding Practice Index — Merge Two Sorted Lists]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 21](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0021-merge-two-sorted-lists.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
