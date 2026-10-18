---
tags:
  - leetcode
problem_number: 25
difficulty: "Hard"
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

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Reverse linked-list nodes in full groups of k, preserving a final short group.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc25|LeetCode — LC 25]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Use a dummy head and locate the kth node after the previous group.
2. If fewer than k nodes remain, stop; otherwise save the following group boundary.
3. Reverse pointers up to that boundary, reconnect the new group head, and move the previous-group pointer to the old head.

## Why It Works

Each complete group is reversed independently and reconnected to both untouched neighboring portions.

## Worked Example

**Illustrative input:** List `1 → 2 → 3 → 4 → 5`, `k = 2`.

**Trace:** Reverse groups 1,2 and 3,4; leave the final 5.

**Result:** Return `2 → 1 → 4 → 3 → 5`.

## Common Pitfalls

Verify a complete group before mutating it. Reverse pointers rather than node values.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc25|Coding Practice Index — Reverse Nodes In K Group]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 25](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0025-reverse-nodes-in-k-group.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
