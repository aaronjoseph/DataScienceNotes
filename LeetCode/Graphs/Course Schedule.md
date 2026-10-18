---
tags:
  - leetcode
problem_number: 207
difficulty: "Medium"
pattern: "Graphs"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
```

## Complexity

$O(V+E)$ time and $O(V+E)$ storage for the graph and traversal. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Determine whether all courses can be completed when prerequisites form a directed graph.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc207|LeetCode — LC 207]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Build a course-to-prerequisites adjacency list.
2. Use depth-first search with a set of courses on the current recursion path.
3. Reject an edge back into that active path; mark completed courses safe so later searches can skip them.

## Why It Works

A directed cycle is precisely a prerequisite dependency that cannot be resolved; completed acyclic subgraphs can be reused.

## Worked Example

**Illustrative input:** Two courses require each other: `[[0, 1], [1, 0]]`.

**Trace:** Searching prerequisites revisits an active course before it can finish.

**Result:** Return `False`.

## Common Pitfalls

An already completed course differs from a currently active course. Check every course, including disconnected components.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc207|Coding Practice Index — Course Schedule]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 207](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0207-course-schedule.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
