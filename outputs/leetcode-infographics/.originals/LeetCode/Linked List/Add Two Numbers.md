---
tags:
  - leetcode
problem_number: 2
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

$O(\max(n,m))$ time and $O(1)$ auxiliary space, excluding the output nodes. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Add two numbers represented by linked lists of decimal digits in reverse order.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc2|LeetCode — LC 2]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Walk both lists with a carry, treating a missing digit as zero.
2. Add the current digits and carry, append the units digit, and retain the tens carry.
3. Continue until both lists and the carry are exhausted.

## Why It Works

Each iteration computes one decimal column and passes exactly its overflow to the next column.

## Worked Example

**Illustrative input:** Lists `9 → 9` and `1`.

**Trace:** The first two columns produce zeros and carry; the final carry adds 1.

**Result:** Return `0 → 0 → 1`, representing 100.

## Common Pitfalls

The least significant digit comes first. A final carry may require an additional node.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc2|Coding Practice Index — Add Two Numbers]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 2](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0002-add-two-numbers.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
