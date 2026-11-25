---
tags:
  - leetcode
  - linked-list
problem_number: 138
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

    def copyRandomList(self, head: 'Node') -> 'Node':
        oldToCopy = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
```

## Complexity

- **Time:** $O(n)$ expected time, where $n$ is the number of nodes in the list (two linear passes with $O(1)$ expected hash-map lookups/insertions).
- **Auxiliary space:** $O(n)$ for the `oldToCopy` hash map, excluding the $n$ newly allocated output nodes. An alternative node-interweaving approach achieves $O(1)$ auxiliary space by temporarily splicing each copy immediately after its original node.

## Algorithm at a glance

![[Attachements/LeetCode/LC0138 - Copy List With Random Pointer.png|700]]

## Overview

Deep-copy a linked list where each node carries both a `next` pointer and an arbitrary `random` pointer (which may point to any node in the list, to itself, or to `None`).[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc138|LeetCode — LC 138]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Initialise a hash map `oldToCopy = {None: None}` so null pointers map cleanly to `None` without `if` checks.
2. **Pass 1 (allocate nodes):** Walk the original list; for each node `cur`, create `Node(cur.val)` and store `oldToCopy[cur] = copy`.
3. **Pass 2 (wire pointers):** Walk the original list again; for each `cur`, set `oldToCopy[cur].next = oldToCopy[cur.next]` and `oldToCopy[cur].random = oldToCopy[cur.random]`.
4. Return `oldToCopy[head]` (which safely returns `None` if `head` is `None`).

## Why It Works

A single pass cannot easily wire `random` pointers because `cur.random` may point forward to a node that has not been created yet (or backward into a cycle). Separating allocation (Pass 1) from wiring (Pass 2) guarantees every target node already exists in `oldToCopy`, keyed by **node identity** rather than node value.

## Worked Example

**Inputs:** Two nodes: `A(val=7)` with `A.next = B`, `A.random = None`; `B(val=7)` with `B.next = None`, `B.random = A`.

1. **Pass 1:** Create `A'(7)` and `B'(7)`; map `{None: None, A: A', B: B'}`.
2. **Pass 2:**
   - For `A`: `A'.next = oldToCopy[B] = B'`, `A'.random = oldToCopy[None] = None`.
   - For `B`: `B'.next = oldToCopy[None] = None`, `B'.random = oldToCopy[A] = A'`.

**Outcome:** Returns `A'`. Every `next` and `random` pointer stays strictly inside the copied list, even though `A` and `B` share the same value `7`.

## Common Pitfalls

- **Keying the map by `cur.val` instead of `cur`:** Multiple nodes can have identical values; always key by the node object reference.
- **Forgetting `{None: None}` in `oldToCopy`:** Without it, `oldToCopy[cur.next]` at the tail, `oldToCopy[cur.random]` when `random` is `None`, or `oldToCopy[head]` on an empty list raises `KeyError`.
- **Leaving a copied pointer pointing to an original node:** Every `copy.next` and `copy.random` must go through `oldToCopy[...]`.

## Related Notes

- [[LeetCode/Linked List/LRU Cache|LRU Cache]] — Another classic hash-map-plus-linked-list design.
- [[LeetCode/Graphs/Clone Graph|Clone Graph]] — The exact same original-to-copy hash-map deep-copy pattern generalized to arbitrary graphs.
- [[Job Interviews/Coding Practice Index#^lc138|Coding Practice Index — Copy List With Random Pointer]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 138](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0138-copy-list-with-random-pointer.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
