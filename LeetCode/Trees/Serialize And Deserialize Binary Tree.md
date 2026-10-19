---
tags:
  - leetcode
problem_number: 297
difficulty: "Hard"
pattern: "Trees"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0297 - Serialize And Deserialize Binary Tree.png|700]]

## Overview

Encode and decode a binary tree while preserving both values and shape.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc297|LeetCode — LC 297]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Serialize preorder values, adding an explicit null marker for every absent child.
2. Split the serialized stream into tokens and consume it with an iterator.
3. For each non-null token, create a node and recursively decode its left and right children.

## Why It Works

Null markers make subtree boundaries unambiguous; the decoder consumes exactly the structure emitted by preorder.

## Worked Example

**Illustrative input:** Root 1 has no left child and right child 2.

**Trace:** Serialization is `1,N,2,N,N`; decoding consumes a left-null marker before building 2.

**Result:** Recover the same shape.

## Common Pitfalls

Preorder values alone are ambiguous. Removing tokens from the front of a list can make decoding quadratic; use an iterator.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc297|Coding Practice Index — Serialize And Deserialize Binary Tree]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations

class Codec:
    def serialize(self, root):
        tokens = []
        def visit(node):
            if node is None:
                tokens.append("N")
                return
            tokens.append(str(node.val))
            visit(node.left)
            visit(node.right)
        visit(root)
        return ",".join(tokens)

    def deserialize(self, data):
        tokens = iter(data.split(","))
        def build():
            value = next(tokens)
            if value == "N":
                return None
            node = TreeNode(int(value))
            node.left = build()
            node.right = build()
            return node
        return build()
```

## Complexity

$O(n)$ time and $O(n)$ storage including tokens, output, and recursion under bounded-size values. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 297](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0297-serialize-and-deserialize-binary-tree.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
