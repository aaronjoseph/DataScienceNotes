---
tags:
  - leetcode
  - linked-list
problem_number: 141
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

- **Time:** $O(n)$ worst-case, where $n$ is the number of nodes in the list. If there is no cycle, `fast` reaches `None` in at most $\lceil n / 2 \rceil$ steps; if there is a cycle of length $C$, once `slow` enters it, `fast` closes the gap by $1$ node per step and meets `slow` within at most $C$ additional steps.
- **Auxiliary space:** $O(1)$, using only two pointers (`slow`, `fast`), improving on the $O(n)$-space hash-set approach.

## Algorithm at a glance

![[Attachements/LeetCode/LC0141 - Linked List Cycle.png|700]]

## Overview

Determine whether a singly linked list contains a cycle using Floyd's tortoise-and-hare (fast/slow pointer) algorithm in $O(1)$ extra space.[^implementation] The same cycle-detection foundation extends to finding the cycle entry in [[LeetCode/Linked List/Find The Duplicate Number|Find The Duplicate Number]] (LC 287).

Problem link: [[Job Interviews/Coding Practice Index#^lc141|LeetCode — LC 141]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Initialise `slow = head` and `fast = head`.
2. While `fast` and `fast.next` are both non-null:
   - Advance `slow` by one step (`slow = slow.next`).
   - Advance `fast` by two steps (`fast = fast.next.next`).
   - If `slow == fast`, a cycle exists — return `True`.
3. If the loop terminates (`fast` or `fast.next` is `None`), the list ends and has no cycle — return `False`.

## Why It Works

- **No cycle:** `fast` moves strictly ahead of `slow` and reaches `None` without ever meeting `slow`.
- **Cycle exists:** Both pointers eventually enter the cycle. Let the clockwise distance from `fast` to `slow` inside the cycle be $d$. Each iteration moves `fast` by $+2$ and `slow` by $+1$, reducing $d$ by $1$ per step (never jumping over `slow`). Thus $d$ reaches $0$ in at most one full lap of the cycle.

## Worked Example

**Inputs:** `1 → 2 → 3 → 2…` (node `3.next` points back to node `2`).

1. **Initial:** `slow = 1`, `fast = 1`.
2. **Step 1:** `slow = 2`, `fast = 3`. Not equal.
3. **Step 2:** `slow = 3`, `fast = 3` (`3 → 2 → 3`). `slow == fast`.

**Outcome:** Returns `True`.

## Common Pitfalls

- **Comparing values (`slow.val == fast.val`) instead of node references (`slow == fast`):** Different nodes can share the same integer value without forming a cycle.
- **Checking only `while fast:` without `and fast.next`:** Calling `fast.next.next` raises `AttributeError` when `fast` is at the last node of an acyclic list.
- **Checking `if slow == fast:` before advancing:** Both pointers start at `head`, so checking before moving would falsely report a cycle on every non-empty list.

## Related Notes

- [[LeetCode/Linked List/Find The Duplicate Number|Find The Duplicate Number]] — Uses Floyd's cycle detection plus a second phase to locate the exact cycle entry.
- [[LeetCode/Linked List/Reorder List|Reorder List]] — Uses the same fast/slow pointer technique to locate the list midpoint.
- [[Job Interviews/Coding Practice Index#^lc141|Coding Practice Index — Linked List Cycle]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 141](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0141-linked-list-cycle.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
