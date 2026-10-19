---
tags:
  - leetcode
problem_number: 1448
difficulty: "Medium"
pattern: "Trees"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC1448 - Count Good Nodes In Binary Tree.png|700]]

## Overview

Count nodes whose value is at least every value along their path from the root.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc1448|LeetCode — LC 1448]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Carry the greatest value seen on the ancestor path.
2. Count the current node if its value is at least that maximum.
3. Recurse into each child with the updated path maximum and sum the counts.

## Why It Works

The carried maximum exactly summarizes the only ancestors that can disqualify the current node.

## Worked Example

**Illustrative input:** Root 3 has left child 1 and right child 4.

**Trace:** The root qualifies, 1 fails against 3, and 4 exceeds its ancestors.

**Result:** Return `2`.

## Common Pitfalls

Equality qualifies. Keep the maximum local to each root-to-node path rather than sharing it across siblings.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc1448|Coding Practice Index — Count Good Nodes In Binary Tree]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations

class Solution:

    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        return dfs(root, root.val)
```

## Complexity

$O(n)$ time and $O(h)$ recursion space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 1448](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/1448-count-good-nodes-in-binary-tree.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
