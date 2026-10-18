---
tags:
  - leetcode
problem_number: 543
difficulty: "Easy"
pattern: "Trees"
languages:
  - Python
---

Find the greatest number of edges on any path between two tree nodes.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc543|LeetCode — LC 543]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Return subtree height in nodes, using zero for an empty subtree.
2. At each node, update the global diameter from its left and right heights.
3. Return one plus the larger height for use by the parent.

## Why It Works

Every longest path has a highest node; adding the two child heights counts the edges of the path turning there.

## Worked Example

**Illustrative input:** Root 1 has children 2 and 3; node 2 has left child 4.

**Trace:** The longest path is 4 → 2 → 1 → 3.

**Result:** Return `3` edges.

## Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations
from typing import Optional

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return res
```

## Complexity

$O(n)$ time and $O(h)$ recursion space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

The diameter counts edges and need not pass through the root. Height and diameter are different quantities.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc543|Coding Practice Index — Diameter of Binary Tree]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 543](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0543-diameter-of-binary-tree.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
