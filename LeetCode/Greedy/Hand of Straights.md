---
tags:
  - leetcode
problem_number: 846
difficulty: "Medium"
pattern: "Greedy"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0846 - Hand of Straights.png|700]]

## Overview

Partition cards into groups of consecutive values of a fixed size.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc846|LeetCode — LC 846]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Reject if the number of cards is not divisible by the group size.
2. Count values and keep the smallest remaining value in a min heap.
3. Start a group there and consume each consecutive required value; reject missing values or inconsistent depletion order.

## Why It Works

The smallest remaining card must begin some group, so consuming that forced group cannot exclude a different valid partition.

## Worked Example

**Illustrative input:** `hand = [1, 2, 3, 2, 3, 4]`, `groupSize = 3`.

**Trace:** Build groups [1,2,3] and [2,3,4].

**Result:** Return `True`.

## Common Pitfalls

Counts matter when duplicate cards exist. A missing number breaks a group even if enough larger cards remain.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc846|Coding Practice Index — Hand of Straights]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
import heapq

class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
```

## Complexity

$O(n\log(u+1))$ conservative time and $O(u)$ space for `u` distinct values. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 846](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0846-hand-of-straights.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
