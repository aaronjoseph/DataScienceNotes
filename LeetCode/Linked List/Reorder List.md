---
tags:
  - leetcode
  - linked-list
problem_number: 143
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

- **Time:** $O(n)$ worst-case, where $n$ is the number of nodes in the list: one pass to find the midpoint, one half-list pass to reverse the second half, and one pass to weave the two halves.
- **Auxiliary space:** $O(1)$, modifying node pointers in place without allocating an auxiliary array or stack.

## Algorithm at a glance

![[Attachements/LeetCode/LC0143 - Reorder List.png|700]]

## Overview

Reorder a singly linked list `L0 → L1 → … → Ln` in place into `L0 → Ln → L1 → Ln-1 → …` without modifying node values.[^implementation] This problem combines three classic linked-list primitives: fast/slow midpoint finding, in-place reversal ([[LeetCode/Linked List/Reverse Linked List|Reverse Linked List]]), and alternating merge.

Problem link: [[Job Interviews/Coding Practice Index#^lc143|LeetCode — LC 143]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. **Find the midpoint:** Start `slow = head` and `fast = head.next`, then advance `slow` by 1 and `fast` by 2 while `fast and fast.next`. When the loop ends, `slow` sits at the end of the first half (the left middle for even length, the exact middle for odd length).
2. **Split and reverse the second half:** Set `second = slow.next`, break the link with `slow.next = None`, and reverse the list starting at `second` using `prev` (giving reversed head `prev`).
3. **Weave the two halves:** With `first = head` and `second = prev`, repeatedly save `tmp1 = first.next` and `tmp2 = second.next`, link `first.next = second` and `second.next = tmp1`, and advance `first, second = tmp1, tmp2` until `second` is `None`.

## Why It Works

Because `fast` starts at `head.next`, the first half always has length $\lceil n / 2 \rceil$ and the second half has length $\lfloor n / 2 \rfloor$ — so the second half is never longer than the first. Reversing the second half exposes nodes in the exact order `Ln, Ln-1, …`, and stopping on `while second:` leaves any extra middle node at the end of the first half already properly terminated with `None`.

## Worked Example

**Inputs:** `head = 1 → 2 → 3 → 4 → 5`.

1. **Find midpoint:**
   - Start: `slow = 1`, `fast = 2`.
   - Step 1: `slow = 2`, `fast = 4`.
   - Step 2: `slow = 3`, `fast = None` (`4 → 5 → None`). Loop ends.
   - First half: `1 → 2 → 3 → None`; second half: `4 → 5`.
2. **Reverse second half:** `4 → 5` becomes `5 → 4 → None` (`prev = 5`).
3. **Weave (`first = 1`, `second = 5`):**
   - Iteration 1: `1 → 5 → 2`, advance `first = 2`, `second = 4`.
   - Iteration 2: `2 → 4 → 3`, advance `first = 3`, `second = None`. Loop ends.

**Outcome:** The list is modified in place to `1 → 5 → 2 → 4 → 3 → None`.

## Common Pitfalls

- **Forgetting `slow.next = None` before weaving:** Leaving the end of the first half connected to the old start of the second half creates a cycle in the final list.
- **Starting `fast = head` instead of `fast = head.next`:** On even-length lists (e.g., `1 → 2 → 3 → 4`), `fast = head` stops `slow` at `3` instead of `2`, making the second half shorter by 1 and breaking the split unless you adjust the detach step.
- **Not saving both `first.next` and `second.next` before relinking:** Overwriting either pointer first drops the rest of that half.

## Related Notes

- [[LeetCode/Linked List/Reverse Linked List|Reverse Linked List]] — The in-place reversal loop used in Phase 2.
- [[LeetCode/Linked List/Linked List Cycle|Linked List Cycle]] — Uses the same fast/slow pointer pattern.
- [[Job Interviews/Coding Practice Index#^lc143|Coding Practice Index — Reorder List]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 143](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0143-reorder-list.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
