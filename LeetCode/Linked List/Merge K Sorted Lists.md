---
tags:
  - leetcode
  - linked-list
problem_number: 23
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

- **Time:** $O(N \log k)$ worst-case (or $O(N \log(k + 1))$ to stay well-defined for $k = 0, 1$), where $N$ is the total number of nodes across all $k$ lists. There are $\lceil \log_2 k \rceil$ merge rounds, and each round visits every node at most once.
- **Auxiliary space:** $O(k)$ for the `mergedLists` reference array each round, while reusing all existing list nodes in place (excluding the input lists). A min-heap alternative also runs in $O(N \log k)$ time and $O(k)$ space.

## Algorithm at a glance

![[Attachements/LeetCode/LC0023 - Merge K Sorted Lists.png|700]]

## Overview

Merge $k$ ascending singly linked lists into one sorted linked list using bottom-up pairwise divide-and-conquer, reusing the two-list merge from [[LeetCode/Linked List/Merge Two Sorted Lists|Merge Two Sorted Lists]] (LC 21).[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc23|LeetCode — LC 23]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## Key Concepts

### Why Pairwise Merging Beats Sequential Merging

- **Sequential merge** (merging list 1 into list 2, then list 3, ..., up to list $k$) re-traverses the growing accumulator up to $k - 1$ times, costing $O(N k)$ in the worst case.
- **Pairwise (divide-and-conquer) merge** halves the number of lists in every round ($k \to \lceil k/2 \rceil \to \dots \to 1$), so each node is touched only $\lceil \log_2 k \rceil$ times, reducing total work to $O(N \log k)$.
- **Alternative (min-heap):** Pushing the head of each non-empty list into a min-heap of size at most $k$ also gives $O(N \log k)$ time and $O(k)$ space, though in Python you must store a tie-breaker index `(node.val, idx, node)` because `ListNode` does not define `<`.

## How to Solve

1. Handle the empty input edge case: if `not lists`, return `None`.
2. While `len(lists) > 1`:
   - Initialise `mergedLists = []`.
   - Step through `lists` in pairs (`i = 0, 2, 4, ...`), taking `l1 = lists[i]` and `l2 = lists[i + 1]` if in bounds (else `None`).
   - Merge `l1` and `l2` with `mergeList` and append the result to `mergedLists`.
   - Replace `lists = mergedLists`.
3. Return `lists[0]`.

## Why It Works

Each round preserves the sorted invariant within every merged list and strictly halves the number of lists (carrying any odd last list forward via `mergeList(l1, None)`). After $\lceil \log_2 k \rceil$ rounds, a single sorted list containing all $N$ nodes remains.

## Worked Example

**Inputs:** `lists = [1 → 4, 2 → 5, 3]`.

1. **Round 1 (`len(lists) = 3`):**
   - Pair `(0, 1)`: merge `1 → 4` and `2 → 5` → `1 → 2 → 4 → 5`.
   - Pair `(2, None)`: merge `3` and `None` → `3`.
   - `lists` becomes `[1 → 2 → 4 → 5, 3]`.
2. **Round 2 (`len(lists) = 2`):**
   - Pair `(0, 1)`: merge `1 → 2 → 4 → 5` and `3` → `1 → 2 → 3 → 4 → 5`.
   - `lists` becomes `[1 → 2 → 3 → 4 → 5]`. Loop ends.

**Outcome:** Returns `1 → 2 → 3 → 4 → 5`.

## Common Pitfalls

- **Confusing $N$ and $k$ in complexity:** $k$ is the number of lists, while $N$ is the *total* number of nodes across all lists — not nodes per list.
- **Dropping the last list when `len(lists)` is odd:** Always guard `lists[i + 1]` with `if i + 1 < len(lists) else None`.
- **Empty input `[]` vs list of empty lists `[None, None]`:** `not lists` returns `None` immediately for `[]`; `[None, None]` runs through `mergeList(None, None)` and returns `None` cleanly.

## Related Notes

- [[LeetCode/Linked List/Merge Two Sorted Lists|Merge Two Sorted Lists]] — The $O(n + m)$ two-list merge subroutine used inside every round.
- [[Big O]] — Logarithmic factor from halving $k$ each round.
- [[Job Interviews/Coding Practice Index#^lc23|Coding Practice Index — Merge K Sorted Lists]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 23](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0023-merge-k-sorted-lists.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
