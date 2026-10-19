---
tags:
  - leetcode
problem_number: 226
difficulty: "Easy"
pattern: "Trees"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0226 - Invert Binary Tree.png|700]]

## Overview

Mirror a binary tree by swapping left and right children at every node.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc226|LeetCode — LC 226]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Return null for an empty subtree.
2. Swap the current node's children.
3. Recursively invert both resulting child subtrees and return the current root.

## Why It Works

A mirrored tree has the original right subtree mirrored on the left and the original left subtree mirrored on the right.

## Worked Example

**Illustrative input:** Tree root 1 has left child 2 and right child 3.

**Trace:** Swap the two children and process their empty descendants.

**Result:** The result has left child 3 and right child 2.

## Common Pitfalls

The code mutates the original tree. A skewed tree can exceed Python's recursion limit.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc226|Coding Practice Index — Invert Binary Tree]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations
from typing import Optional

class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = (root.right, root.left)
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```

## Complexity

$O(n)$ time and $O(h)$ recursion space for tree height `h`. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 226](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0226-invert-binary-tree.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
