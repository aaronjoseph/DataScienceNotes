---
tags:
  - leetcode
problem_number: 124
difficulty: "Hard"
pattern: "Trees"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0124 - Binary Tree Maximum Path Sum.png|700]]

## Overview

Find the greatest sum of any nonempty simple path in a binary tree. A path may turn at one node.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc124|LeetCode — LC 124]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Recursively obtain each child's best downward gain and discard negative gains.
2. Update a global best with the current node plus both nonnegative child gains.
3. Return the node plus only the larger child gain to its parent.

## Why It Works

A complete path may use two branches at its highest node, but a path extended to a parent can use only one child branch.

## Worked Example

**Illustrative input:** Root -10 has left child 9 and right subtree rooted at 20 with children 15 and 7.

**Trace:** The best path turns at 20 and joins 15 to 7.

**Result:** Return `42`.

## Common Pitfalls

Initialize the global answer from a real node so all-negative trees work. Do not return a two-branch path upward.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc124|Coding Practice Index — Binary Tree Maximum Path Sum]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations

class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
```

## Complexity

$O(n)$ time and $O(h)$ recursion space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 124](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0124-binary-tree-maximum-path-sum.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
