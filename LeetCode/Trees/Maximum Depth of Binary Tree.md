---
tags:
  - leetcode
problem_number: 104
difficulty: "Easy"
pattern: "Trees"
languages:
  - Python
---

Return the number of nodes on the longest root-to-leaf path.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc104|LeetCode — LC 104]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Assign depth zero to an empty subtree.
2. Recursively obtain both child depths.
3. Return one plus the larger child depth.

## Why It Works

Every root-to-leaf path chooses exactly one child subtree; choosing its maximum depth gives the longest path.

## Worked Example

**Illustrative input:** A root has one child, which has one child.

**Trace:** The leaf contributes depth 1; its ancestors contribute depths 2 and 3.

**Result:** Return `3`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations

class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

## Complexity

$O(n)$ time and $O(h)$ recursion space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Depth counts nodes here. Recursion space can be linear for a skewed tree.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc104|Coding Practice Index — Maximum Depth of Binary Tree]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 104](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0104-maximum-depth-of-binary-tree.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
