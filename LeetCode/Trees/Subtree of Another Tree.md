---
tags:
  - leetcode
problem_number: 572
difficulty: "Easy"
pattern: "Trees"
languages:
  - Python
---

Check whether one tree contains another as a complete rooted subtree.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc572|LeetCode — LC 572]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. At each node of the larger tree, compare the entire candidate subtree using structural equality.
2. If it fails, recursively try each child as the next candidate root.
3. Accept a successful exact match; reject when all candidate roots are exhausted.

## Why It Works

Every possible subtree root is examined, and structural comparison verifies all its descendants.

## Worked Example

**Illustrative input:** The larger tree has root 3 with subtree rooted at 4 containing children 1 and 2.

**Trace:** Compare the candidate rooted at 4 with that same structure.

**Result:** Return `True`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations
from typing import Optional

class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and (not q):
            return True
        if p and q and (p.val == q.val):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
```

## Complexity

$O(nm)$ worst-case time for tree sizes `n` and `m`; $O(h_n+h_m)$ recursion space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

A matching prefix is insufficient if the larger candidate has extra descendants. The helper accepts an empty target subtree.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc572|Coding Practice Index — Subtree of Another Tree]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 572](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0572-subtree-of-another-tree.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
