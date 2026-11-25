---
tags:
  - leetcode
  - linked-list
problem_number: 25
difficulty: "Hard"
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

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            prev, curr = (kth.next, groupPrev.next)
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
```

## Complexity

- **Time:** $O(n)$ worst-case, where $n$ is the number of nodes in the list. Every node in a complete group is visited twice (once by `getKth` and once by the reversal loop); nodes in a trailing short group are visited once.
- **Auxiliary space:** $O(1)$, using only a sentinel `dummy` node and pointer variables (`groupPrev`, `kth`, `groupNext`, `prev`, `curr`, `tmp`).

## Algorithm at a glance

![[Attachements/LeetCode/LC0025 - Reverse Nodes In K Group.png|700]]

## Overview

Reverse a singly linked list in contiguous groups of $k$ nodes by rewiring pointers in place; if fewer than $k$ nodes remain at the end, leave that trailing group untouched.[^implementation] This generalizes [[LeetCode/Linked List/Reverse Linked List|Reverse Linked List]] (LC 206) with boundary bookkeeping around each reversed block.

Problem link: [[Job Interviews/Coding Practice Index#^lc25|LeetCode — LC 25]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## Key Concepts

### Four Boundary Pointers per Group

For each group of $k$ nodes, track four positions before mutating anything:

- `groupPrev`: the node immediately **before** the current group (starts at `dummy`).
- `groupPrev.next`: the **old head** of the group, which becomes the **new tail** after reversal.
- `kth`: the $k$-th node of the group, which becomes the **new head** after reversal.
- `groupNext = kth.next`: the first node of the **next** group (the stop boundary).

Initialising `prev = kth.next` (i.e., `groupNext`) before reversing means the old head automatically points to `groupNext` on the very first reversal step, keeping the list continuously connected!

## How to Solve

1. Create `dummy = ListNode(0, head)` and set `groupPrev = dummy`.
2. Repeat:
   - Call `kth = getKth(groupPrev, k)` to find the $k$-th node ahead of `groupPrev`.
   - If `kth` is `None`, fewer than $k$ nodes remain — `break` without modifying them.
   - Save `groupNext = kth.next`.
   - Reverse the group in place with `prev, curr = groupNext, groupPrev.next` until `curr == groupNext`.
   - Reconnect the preceding list to the new group head: save `tmp = groupPrev.next` (the new group tail), set `groupPrev.next = kth`, and advance `groupPrev = tmp`.
3. Return `dummy.next`.

## Why It Works

Checking `getKth(groupPrev, k)` before any pointer edits guarantees a partial trailing group is never reversed. Setting `prev = groupNext` links the reversed group's tail directly to the next group, and setting `groupPrev.next = kth` links the previous group's tail directly to the reversed group's head, preserving a single valid list after every iteration.

## Worked Example

**Inputs:** `head = 1 → 2 → 3 → 4 → 5`, `k = 2`.

1. **Group 1 (`groupPrev = dummy`):**
   - `kth = 2`, `groupNext = 3`.
   - Reverse `1 → 2` with `prev = 3`: `1.next = 3`, `2.next = 1`.
   - Reconnect: `dummy.next = 2`; advance `groupPrev = 1`.
   - List is now `dummy → 2 → 1 → 3 → 4 → 5`.
2. **Group 2 (`groupPrev = 1`):**
   - `kth = 4`, `groupNext = 5`.
   - Reverse `3 → 4` with `prev = 5`: `3.next = 5`, `4.next = 3`.
   - Reconnect: `1.next = 4`; advance `groupPrev = 3`.
   - List is now `dummy → 2 → 1 → 4 → 3 → 5`.
3. **Group 3 (`groupPrev = 3`):**
   - `getKth(3, 2)` returns `None` (only node `5` remains) → `break`.

**Outcome:** Returns `dummy.next`, the head of `2 → 1 → 4 → 3 → 5`.

## Common Pitfalls

- **Reversing before checking whether $k$ nodes exist:** Always run `getKth` first; otherwise a trailing short group gets reversed and would need to be reversed back.
- **Setting `prev = None` instead of `prev = groupNext`:** Breaks the link between the reversed group's tail and the rest of the list unless you reattach it manually afterward.
- **Updating `groupPrev.next = kth` before saving `tmp = groupPrev.next`:** Loses the pointer to the old group head (the new tail), so you cannot advance `groupPrev` to the right position for the next group.
- **Swapping node values instead of pointers:** The problem explicitly forbids modifying node values.

## Related Notes

- [[LeetCode/Linked List/Reverse Linked List|Reverse Linked List]] — The core three-pointer reversal loop used inside each group.
- [[LeetCode/Linked List/Reorder List|Reorder List]] — Another multi-pointer in-place list rewiring problem.
- [[Job Interviews/Coding Practice Index#^lc25|Coding Practice Index — Reverse Nodes In K Group]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 25](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0025-reverse-nodes-in-k-group.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
