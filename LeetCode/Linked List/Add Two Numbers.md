---
tags:
  - leetcode
  - linked-list
problem_number: 2
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

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
```

## Complexity

- **Time:** $O(\max(n, m))$ worst-case, where $n$ and $m$ are the lengths of `l1` and `l2` (at most $\max(n, m) + 1$ iterations if a final carry creates one extra digit).
- **Auxiliary space:** $O(1)$, excluding the newly created output list of length at most $\max(n, m) + 1$.

## Algorithm at a glance

![[Attachements/LeetCode/LC0002 - Add Two Numbers.png|700]]

## Overview

Add two non-negative integers represented as singly linked lists whose digits are stored in **reverse** order (least significant digit at the head), and return the sum in the same format.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc2|LeetCode — LC 2]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Create a sentinel `dummy = ListNode()`, set `cur = dummy`, and initialise `carry = 0`.
2. Loop `while l1 or l2 or carry:` so mismatched list lengths and a trailing carry are all handled in one loop:
   - Read `v1 = l1.val if l1 else 0` and `v2 = l2.val if l2 else 0`.
   - Compute `val = v1 + v2 + carry`, update `carry = val // 10`, and keep the digit `val % 10`.
   - Append `ListNode(val)` to `cur.next`, advance `cur`, and advance `l1` / `l2` if non-null.
3. Return `dummy.next`.

## Why It Works

Because the lists store digits from least significant to most significant, walking both heads in parallel mirrors elementary right-to-left column addition. Each step computes one decimal place and propagates its overflow (`0` or `1`) to the next place.

## Worked Example

**Inputs:** `l1 = 9 → 9` (represents `99`), `l2 = 1` (represents `1`).

1. **Step 1 (`l1 = 9`, `l2 = 1`, `carry = 0`):** `val = 10` → digit `0`, `carry = 1`. Output: `0`.
2. **Step 2 (`l1 = 9`, `l2 = None`, `carry = 1`):** `val = 9 + 0 + 1 = 10` → digit `0`, `carry = 1`. Output: `0 → 0`.
3. **Step 3 (`l1 = None`, `l2 = None`, `carry = 1`):** `val = 0 + 0 + 1 = 1` → digit `1`, `carry = 0`. Output: `0 → 0 → 1`.
4. **Termination:** `l1`, `l2`, and `carry` are all falsy; loop exits.

**Outcome:** Returns `0 → 0 → 1`, representing `100`.

## Common Pitfalls

- **Forgetting `or carry` in the `while` condition:** Causes inputs like `9 → 9` + `1` or `5` + `5` to drop the most significant carry digit (`1`).
- **Assuming both lists have the same length:** Always guard `l1.val` / `l1.next` and `l2.val` / `l2.next` against `None`.
- **Reversing the order mentally:** Remember that `2 → 4 → 3` represents `342`, not `243`, so no list reversal is needed before adding.

## Related Notes

- [[LeetCode/Linked List/Merge Two Sorted Lists|Merge Two Sorted Lists]] — Uses the same `dummy` sentinel head pattern while traversing two lists.
- [[Job Interviews/Coding Practice Index#^lc2|Coding Practice Index — Add Two Numbers]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 2](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0002-add-two-numbers.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
