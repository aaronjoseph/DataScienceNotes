---
tags:
  - leetcode
problem_number: 215
difficulty: "Medium"
pattern: "Heap / Priority Queue"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0215 - Kth Largest Element In An Array.png|700]]

## Overview

Find the kth largest occurrence in an unsorted array. A size-k min heap keeps only the current top k.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc215|LeetCode — LC 215]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Scan the values and push each into a min heap.
2. Whenever the heap contains more than k values, pop its smallest.
3. Return the root after all values have been processed.

## Why It Works

Discarding the smallest among k+1 candidates preserves exactly the k largest occurrences of the scanned prefix.

## Worked Example

**Illustrative input:** `nums = [3, 1, 5, 5, 2]`, `k = 2`.

**Trace:** The retained top two values are both 5.

**Result:** Return `5`.

## Common Pitfalls

This is kth largest with duplicates included, not kth distinct. Quickselect has expected linear time but a different worst-case bound.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc215|Coding Practice Index — Kth Largest Element In An Array]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = []
        for value in nums:
            heapq.heappush(largest, value)
            if len(largest) > k:
                heapq.heappop(largest)
        return largest[0]
```

## Complexity

$O(n\log(k+1))$ time and $O(k)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 215](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0215-kth-largest-element-in-an-array.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
