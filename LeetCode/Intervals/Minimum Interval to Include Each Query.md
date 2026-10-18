---
tags:
  - leetcode
problem_number: 1851
difficulty: "Hard"
pattern: "Intervals"
languages:
  - Python
---

For each query point, return the size of the smallest closed interval containing it, or -1.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc1851|LeetCode — LC 1851]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Sort intervals by start and process queries in increasing order.
2. Push all intervals whose start is at most the query into a heap keyed by interval size.
3. Remove heap tops ending before the query, then answer from the smallest valid top and restore original query order.

## Why It Works

Every newly eligible interval is inserted, while expired top intervals are removed until the heap's smallest remaining candidate actually covers the query.

## Worked Example

**Illustrative input:** `intervals = [[1, 4], [2, 3]]`, queries `[3, 5]`.

**Trace:** At 3, the interval [2,3] is smallest; at 5, all candidates have expired.

**Result:** Return `[2, -1]`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
import heapq

class Solution:

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
```

## Complexity

$O(n\log n+q\log q+(n+q)\log(n+1))$ time and $O(n+q)$ auxiliary space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Closed interval size includes both endpoints. Restore query order, and reuse answers safely for duplicate queries.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc1851|Coding Practice Index — Minimum Interval to Include Each Query]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 1851](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/1851-minimum-interval-to-include-each-query.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
