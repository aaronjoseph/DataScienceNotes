---
tags:
  - leetcode
problem_number: 295
difficulty: "Hard"
pattern: "Heap / Priority Queue"
languages:
  - Python
---

Support adding numbers and querying their median using two heaps.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc295|LeetCode — LC 295]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Keep the lower half in a max heap, represented by negatives, and the upper half in a min heap.
2. Insert into the appropriate half and rebalance so sizes differ by at most one.
3. Read the larger heap's top for odd size, or average both tops for even size.

## Why It Works

All lower-half values remain at most all upper-half values, and balanced sizes place the median at the heap boundaries.

## Worked Example

**Illustrative input:** Add 1 and 5, then add 2.

**Trace:** After rebalancing, the ordered halves are [1, 2] and [5].

**Result:** The median changes from `3` to `2`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
import heapq

class MedianFinder:

    def __init__(self):
        self.small, self.large = ([], [])

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
```

## Complexity

Insertion takes $O(\log n)$ time, median lookup $O(1)$, and storage $O(n)$. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Use a max-heap representation for the lower half. The judge calls median only after at least one insertion.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc295|Coding Practice Index — Find Median From Data Stream]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 295](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0295-find-median-from-data-stream.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
