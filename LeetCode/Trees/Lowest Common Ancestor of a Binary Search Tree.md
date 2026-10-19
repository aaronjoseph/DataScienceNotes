---
tags:
  - leetcode
problem_number: 235
difficulty: "Medium"
pattern: "Trees"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0235 - Lowest Common Ancestor of a Binary Search Tree.png|700]]

## Overview

Find the lowest common ancestor of two existing nodes in a binary search tree.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc235|LeetCode — LC 235]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Start at the root.
2. If both target values are smaller, move left; if both are larger, move right.
3. Return the first node where the target directions split or one target equals the current node.

## Why It Works

While both targets occupy one strict side, their lowest common ancestor must also be in that side.

## Worked Example

**Illustrative input:** BST root 6 has children 2 and 8; the targets are those children.

**Trace:** Their values lie on opposite sides of 6.

**Result:** Return the root node `6`.

## Common Pitfalls

The targets are guaranteed to exist and BST values are unique. Return the node, not only its value.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc235|Coding Practice Index — Lowest Common Ancestor of a Binary Search Tree]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
```

## Complexity

$O(h)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 235](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0235-lowest-common-ancestor-of-a-binary-search-tree.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
