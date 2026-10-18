---
tags:
  - leetcode
problem_number: 105
difficulty: "Medium"
pattern: "Trees"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations
from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        positions = {value: i for i, value in enumerate(inorder)}
        next_root = 0
        def build(left, right):
            nonlocal next_root
            if left > right:
                return None
            value = preorder[next_root]
            next_root += 1
            middle = positions[value]
            node = TreeNode(value)
            node.left = build(left, middle - 1)
            node.right = build(middle + 1, right)
            return node
        return build(0, len(inorder) - 1)
```

## Complexity

$O(n)$ expected time and $O(n)$ auxiliary space for the index map and recursion. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Reconstruct a binary tree from preorder and inorder traversals with distinct values.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc105|LeetCode — LC 105]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Map each inorder value to its position and maintain a pointer into preorder.
2. For an inorder interval, take the next preorder value as its root.
3. Split that interval around the root position, construct the left subtree first, then the right, and return the root.

## Why It Works

Preorder chooses roots before descendants, and inorder uniquely identifies which remaining nodes belong on each side.

## Worked Example

**Illustrative input:** `preorder = [2, 1, 3]`, `inorder = [1, 2, 3]`.

**Trace:** Choose 2 as root, then build interval [1] and interval [3].

**Result:** Recover root 2 with children 1 and 3.

## Common Pitfalls

Distinct values and consistent traversals are required. Repeated slicing and linear index searches can make a simpler implementation quadratic.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc105|Coding Practice Index — Construct Binary Tree From Preorder And Inorder Traversal]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 105](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0105-construct-binary-tree-from-preorder-and-inorder-traversal.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
