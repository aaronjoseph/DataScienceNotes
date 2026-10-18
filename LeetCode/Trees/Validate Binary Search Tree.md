---
tags:
  - leetcode
problem_number: 98
difficulty: "Medium"
pattern: "Trees"
languages:
  - Python
---

Verify that every node satisfies all binary-search-tree ordering constraints, including those imposed by distant ancestors.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc98|LeetCode — LC 98]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Recursively pass strict lower and upper allowed values.
2. Reject a node outside those bounds.
3. For the left child, tighten the upper bound to the node value; for the right child, tighten the lower bound.

## Why It Works

Each propagated bound encodes every ancestor restriction relevant to that subtree.

## Worked Example

**Illustrative input:** Root 5 has right child 7, whose left child is 4.

**Trace:** The 4 is below its parent, but it violates the inherited lower bound 5.

**Result:** Return `False`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations

class Solution:

    def isValidBST(self, root: TreeNode) -> bool:

        def valid(node, left, right):
            if not node:
                return True
            if not left < node.val < right:
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float('-inf'), float('inf'))
```

## Complexity

$O(n)$ time and $O(h)$ recursion space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Checking only immediate children misses ancestor violations. Strict bounds reject duplicate values.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc98|Coding Practice Index — Validate Binary Search Tree]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 98](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0098-validate-binary-search-tree.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
