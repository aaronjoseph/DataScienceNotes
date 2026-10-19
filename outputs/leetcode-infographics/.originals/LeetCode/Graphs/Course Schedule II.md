---
tags:
  - leetcode
problem_number: 210
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

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        output = []
        visit, cycle = (set(), set())

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
```

## Complexity

$O(V+E)$ time and $O(V+E)$ storage. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Return an ordering that completes all course prerequisites before each course, or an empty list if impossible.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc210|LeetCode — LC 210]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Build a course-to-prerequisites graph.
2. Depth-first search each course, distinguishing active-path nodes from fully completed nodes.
3. Append a course only after all its prerequisites finish; reject any active-path revisit.

## Why It Works

Postorder on prerequisite edges places every prerequisite before its dependent course, provided there is no directed cycle.

## Worked Example

**Illustrative input:** Prerequisites `[[1, 0], [2, 1]]` for three courses.

**Trace:** DFS finishes 0, then 1, then 2.

**Result:** Return `[0, 1, 2]`.

## Common Pitfalls

This edge orientation already gives the desired append order; reversing it would be wrong. A valid order need not be unique.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc210|Coding Practice Index — Course Schedule II]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 210](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0210-course-schedule-ii.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
