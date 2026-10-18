---
tags:
  - leetcode
problem_number: 133
difficulty: "Medium"
pattern: "Graphs"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge. The judge supplies the problem's node classes; their constructors and attributes follow the problem statement.

```python
from __future__ import annotations

class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None
```

## Complexity

$O(V+E)$ expected time and $O(V)$ auxiliary map/recursion space, excluding copied edges. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Deep-copy the connected graph reachable from a given node, preserving cycles and neighbor links.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc133|LeetCode — LC 133]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Keep a map from each original node to its copy.
2. Create and memoize a copy before recursively cloning its neighbors.
3. Return an existing copy on revisits and return null for an empty starting graph.

## Why It Works

Memoizing before recursion prevents cycles from looping forever and gives every original node exactly one copy.

## Worked Example

**Illustrative input:** Two nodes A and B list each other as neighbors.

**Trace:** Create A′ first, create B′, and reuse A′ when B links back.

**Result:** The copied graph contains the same two-way connection.

## Common Pitfalls

Map node identities, not potentially repeated values. Register a copy before visiting its neighbors.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc133|Coding Practice Index — Clone Graph]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 133](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0133-clone-graph.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
