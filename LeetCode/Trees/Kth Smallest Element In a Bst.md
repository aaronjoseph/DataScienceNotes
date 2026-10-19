---
tags:
  - leetcode
problem_number: 230
difficulty: "Medium"
pattern: "Trees"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0230 - Kth Smallest Element In a Bst.png|700]]

## Overview

Return the kth smallest value in a binary search tree using its sorted inorder traversal.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc230|LeetCode — LC 230]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Use a stack to descend the current subtree's left edge.
2. Pop and visit the next node, decrementing k.
3. Return when k reaches zero; otherwise continue from that node's right child.

## Why It Works

Inorder visits BST values in ascending order, so the kth visit is the required order statistic.

## Worked Example

**Illustrative input:** BST root 3 has left subtree 1 with right child 2; `k = 2`.

**Trace:** Inorder visits 1, then 2.

**Result:** Return `2`.

## Common Pitfalls

The problem guarantees a valid k. Maintaining subtree sizes would support repeated order-statistic queries more efficiently.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc230|Coding Practice Index — Kth Smallest Element In a Bst]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations

class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
```

## Complexity

$O(h+k)$ time and $O(h)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 230](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0230-kth-smallest-element-in-a-bst.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
