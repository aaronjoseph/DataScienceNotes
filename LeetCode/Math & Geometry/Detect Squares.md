---
tags:
  - leetcode
problem_number: 2013
difficulty: "Medium"
pattern: "Math & Geometry"
languages:
  - Python
---

Support adding points and counting axis-aligned squares using a query as one corner, with duplicate points counted separately.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc2013|LeetCode — LC 2013]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Keep both a list of added point occurrences and a coordinate-frequency map.
2. For a query, examine each stored point as a possible opposite corner; require equal nonzero horizontal and vertical distances.
3. For a valid opposite corner occurrence, multiply the counts of the two other required corners and add the contribution.

## Why It Works

Every axis-aligned square has exactly one corner diagonally opposite the query, so the scan enumerates each square with its multiplicity.

## Worked Example

**Illustrative input:** Add `[0, 1]`, `[1, 0]`, and `[1, 1]`; query `[0, 0]`.

**Trace:** The opposite corner [1,1] finds the two required side corners.

**Result:** Return `1`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if abs(py - y) != abs(px - x) or x == px or y == py:
                continue
            res += self.ptsCount[x, py] * self.ptsCount[px, y]
        return res
```

## Complexity

Add takes expected amortized $O(1)$ time; count takes expected $O(N)$ time. Stored-point space is $O(N)$, with possible zero-valued map entries for queried missing corners in this defaultdict implementation. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

The query point need not have been added. Skip zero side lengths and preserve duplicate-corner multiplicities.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc2013|Coding Practice Index — Detect Squares]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 2013](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/2013-detect-squares.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
