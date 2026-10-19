---
tags:
  - leetcode
problem_number: 100
difficulty: "Easy"
pattern: "Trees"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0100 - Same Tree.png|700]]

## Overview

Determine whether two binary trees have identical shapes and matching values at corresponding nodes.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc100|LeetCode — LC 100]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Accept a pair of null subtrees.
2. Reject if only one node is null or their values differ.
3. Recursively require equality of both corresponding child pairs.

## Why It Works

The root value and the two child structures fully determine equality of a binary tree.

## Worked Example

**Illustrative input:** One tree has root 1 with left child 2; the other has root 1 with right child 2.

**Trace:** The root matches, but the corresponding left children do not.

**Result:** Return `False`.

## Common Pitfalls

Matching traversal values without null positions can hide structural differences.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc100|Coding Practice Index — Same Tree]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations
from typing import Optional

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and (not q):
            return True
        if p and q and (p.val == q.val):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
```

## Complexity

$O(n+m)$ worst-case time bound and $O(h)$ recursion space across the compared trees. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 100](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0100-same-tree.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
