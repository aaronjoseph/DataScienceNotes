---
tags:
  - leetcode
problem_number: 703
difficulty: "Easy"
pattern: "Heap / Priority Queue"
languages:
  - Python
---

Maintain the kth largest value as numbers arrive. Retain only the k largest values seen so far.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc703|LeetCode — LC 703]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Heapify the starting values and remove the smallest until at most k remain.
2. On add, push the new value and pop the smallest if the heap exceeds k.
3. Return the heap root when the stream has at least k values.

## Why It Works

The heap contains the k largest occurrences; its smallest member is therefore the kth largest overall.

## Worked Example

**Illustrative input:** `k = 2`, initial values `[4, 1]`; add 3.

**Trace:** The heap discards 1 and retains 3 and 4.

**Result:** Return `3`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = (nums, k)
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
```

## Complexity

Initialization takes $O(n+(n-k)_+\log(n+1))$ time for this heapify-and-trim implementation; each add takes $O(\log(k+1))$ time, with $O(k)$ retained storage. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Duplicates count as separate ranked occurrences. The constructor mutates the supplied list, and kth-largest queries assume enough elements.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc703|Coding Practice Index — Kth Largest Element In a Stream]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 703](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0703-kth-largest-element-in-a-stream.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
