---
tags:
  - leetcode
problem_number: 138
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

$O(n)$ expected time and $O(n)$ auxiliary map storage, plus the copied nodes. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Deep-copy a linked list whose nodes contain both next and random pointers.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc138|LeetCode — LC 138]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. First create one new node per original and record an original-to-copy map, including null.
2. Walk the original list again and set each copy's next and random through the map.
3. Return the copy corresponding to the original head.

## Why It Works

Creating every destination first lets both forward references and cycles in random pointers resolve to copied nodes.

## Worked Example

**Illustrative input:** Node A points next to B; B.random points to A.

**Trace:** Create copies A′ and B′, then connect B′.random to A′.

**Result:** All copied pointers stay within the copied structure.

## Common Pitfalls

Repeated values do not identify nodes. Never leave a copied pointer referring to an original node.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc138|Coding Practice Index — Copy List With Random Pointer]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 138](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0138-copy-list-with-random-pointer.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
