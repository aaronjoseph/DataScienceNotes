---
tags:
  - leetcode
problem_number: 1046
difficulty: "Easy"
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

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])
```

## Complexity

$O(n\log n)$ time and $O(n)$ extra space for the negated heap. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Repeatedly smash the two heaviest stones and return the final remaining weight.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc1046|LeetCode — LC 1046]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Represent a max heap by negating stone weights and heapify.
2. Pop the two heaviest; discard both if equal or push their positive weight difference in negated form.
3. Continue until at most one stone remains; return its weight or zero.

## Why It Works

Each heap operation implements the problem's required choice of the two current heaviest stones.

## Worked Example

**Illustrative input:** `stones = [2, 7, 4]`.

**Trace:** Smash 7 with 4 to obtain 3, then smash 3 with 2 to obtain 1.

**Result:** Return `1`.

## Common Pitfalls

Python's ordinary heap is a min heap. Track signs consistently when computing the difference.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc1046|Coding Practice Index — Last Stone Weight]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 1046](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/1046-last-stone-weight.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
