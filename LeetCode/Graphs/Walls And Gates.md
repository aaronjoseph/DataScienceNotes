---
tags:
  - leetcode
problem_number: 286
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
from collections import deque

class Solution:

    def walls_and_gates(self, rooms: List[List[int]]):
        ROWS, COLS = (len(rooms), len(rooms[0]))
        visit = set()
        q = deque()

        def addRooms(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or ((r, c) in visit) or (rooms[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1
```

## Complexity

$O(RC)$ time and $O(RC)$ auxiliary space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Fill each empty room with its distance to the nearest gate, respecting walls.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc286|LeetCode — LC 286]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Enqueue every gate with distance zero and mark it visited.
2. Run multi-source breadth-first search through non-wall rooms.
3. Assign the current level distance when processing a room; leave unreachable rooms unchanged.

## Why It Works

The first BFS arrival at a room comes from a shortest path from the entire set of gates.

## Worked Example

**Illustrative input:** A row contains `[0, INF, INF, -1]`.

**Trace:** The gate reaches the next two rooms at distances one and two; the wall blocks further travel.

**Result:** The row becomes `[0, 1, 2, -1]`.

## Common Pitfalls

Use the problem's INF sentinel for empty rooms and -1 for walls. Do not search independently from every room.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc286|Coding Practice Index — Walls And Gates]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 286](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0286-walls-and-gates.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
