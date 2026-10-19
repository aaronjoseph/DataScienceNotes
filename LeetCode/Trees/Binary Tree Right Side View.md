---
tags:
  - leetcode
problem_number: 199
difficulty: "Medium"
pattern: "Trees"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0199 - Binary Tree Right Side View.png|700]]

## Overview

Return the values visible when viewing a binary tree from its right side.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc199|LeetCode — LC 199]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Traverse the tree level by level using a queue.
2. Visit each level's nodes in left-to-right order and remember the last real node.
3. Append that node's value to the result.

## Why It Works

The last node in a level is its rightmost existing node, regardless of which parent owns it.

## Worked Example

**Illustrative input:** Root 1 has left child 2, and node 2 has right child 5.

**Trace:** The three levels have rightmost nodes 1, 2, and 5.

**Result:** Return `[1, 2, 5]`.

## Common Pitfalls

The view is not just the chain of right-child pointers. Handle an empty root.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc199|Coding Practice Index — Binary Tree Right Side View]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations
from typing import List
import collections

class Solution:

    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        q = collections.deque([root])
        while q:
            rightSide = None
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
```

## Complexity

$O(n)$ time and $O(w)$ auxiliary queue space, excluding output. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 199](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0199-binary-tree-right-side-view.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
