---
tags:
  - leetcode
problem_number: 23
difficulty: "Hard"
pattern: "Linked List"
languages:
  - Python
---

Merge k sorted linked lists efficiently by merging pairs in rounds.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc23|LeetCode — LC 23]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Pair adjacent lists and merge each pair with an iterative two-list merge.
2. Carry an unpaired final list forward.
3. Repeat until only one list remains; return null when the input collection is empty.

## Why It Works

Every round preserves sortedness and halves the number of lists, while visiting each node only once per round.

## Worked Example

**Illustrative input:** Lists `[1 → 4, 2 → 5, 3]`.

**Trace:** Merge the first pair, carry 3, then merge the two remaining lists.

**Result:** Return `1 → 2 → 3 → 4 → 5`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations
from typing import List

class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
```

## Complexity

$O(N\log(k+1))$ time for `N` total nodes; $O(k)$ auxiliary list references while reusing nodes. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Distinguish the number of lists from the total nodes. Preserve an odd unpaired list.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc23|Coding Practice Index — Merge K Sorted Lists]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 23](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0023-merge-k-sorted-lists.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
