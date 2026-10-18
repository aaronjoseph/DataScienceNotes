---
tags:
  - leetcode
problem_number: 102
difficulty: "Medium"
pattern: "Trees"
languages:
  - Python
---

Return binary-tree values grouped by depth using breadth-first search.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc102|LeetCode — LC 102]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Put the root in a queue if it exists.
2. At each level, process exactly the queue length measured before that level starts.
3. Collect those values and enqueue their children for the next level.

## Why It Works

Queue order ensures all nodes at the current depth are consumed before any node at the next depth.

## Worked Example

**Illustrative input:** Tree root 1 has children 2 and 3; node 2 has child 4.

**Trace:** Process batches of sizes 1, 2, and 1.

**Result:** Return `[[1], [2, 3], [4]]`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations
from typing import List
import collections

class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)
        while q:
            val = []
            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res
```

## Complexity

$O(n)$ time and $O(w)$ auxiliary queue space for maximum width `w`, excluding output. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Measure the level size before enqueuing children. Use deque rather than repeatedly removing the first list element.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc102|Coding Practice Index — Binary Tree Level Order Traversal]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 102](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0102-binary-tree-level-order-traversal.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
