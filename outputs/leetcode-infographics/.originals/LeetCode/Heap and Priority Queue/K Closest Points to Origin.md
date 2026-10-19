---
tags:
  - leetcode
problem_number: 973
difficulty: "Medium"
pattern: "Heap / Priority Queue"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
import heapq

class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            minHeap.append((dist, x, y))
        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append((x, y))
        return res
```

## Complexity

$O(n+k\log n)$ time and $O(n)$ auxiliary space, excluding output. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Return k points nearest to the origin using a heap ordered by squared Euclidean distance.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc973|LeetCode — LC 973]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Compute the squared distance and coordinates for every point.
2. Build a min heap from those records.
3. Pop exactly k points and return their coordinates.

## Why It Works

Squaring preserves distance order for nonnegative distances, so the heap emits nearest points first without square roots.

## Worked Example

**Illustrative input:** `points = [[1, 2], [3, 4], [0, 1]]`, `k = 2`.

**Trace:** Squared distances are 5, 25, and 1; pop the last point, then the first.

**Result:** Return `[[0, 1], [1, 2]]`.

## Common Pitfalls

A heap of every point has different space bounds from a size-k max heap. Output order is unrestricted.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc973|Coding Practice Index — K Closest Points to Origin]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 973](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0973-k-closest-points-to-origin.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
