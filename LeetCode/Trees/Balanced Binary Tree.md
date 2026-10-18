---
tags:
  - leetcode
problem_number: 110
difficulty: "Easy"
pattern: "Trees"
languages:
  - Python
---

Check whether every node's left and right subtree heights differ by at most one.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc110|LeetCode — LC 110]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Recursively return both a balance flag and a height for each subtree.
2. A node is balanced only if both child flags are true and their heights differ by at most one.
3. Return the combined flag and one plus the larger child height.

## Why It Works

The returned pair contains all information a parent needs, so each subtree is evaluated only once.

## Worked Example

**Illustrative input:** A chain of three nodes extends only left.

**Trace:** At the root, the left subtree has height 2 and the right height 0.

**Result:** Return `False`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations
from typing import Optional

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]
            left, right = (dfs(root.left), dfs(root.right))
            balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
```

## Complexity

$O(n)$ time and $O(h)$ recursion space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Balance must hold at every node. Recomputing heights from scratch at each node can take quadratic time.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc110|Coding Practice Index — Balanced Binary Tree]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 110](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0110-balanced-binary-tree.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
