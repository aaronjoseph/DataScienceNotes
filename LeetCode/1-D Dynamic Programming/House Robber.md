---
tags:
  - leetcode
problem_number: 198
difficulty: "Medium"
pattern: "1-D Dynamic Programming"
languages:
  - Python
---

Choose nonadjacent houses with the greatest total value. Keep the best totals for the previous one and two positions.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc198|LeetCode — LC 198]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Initialize both rolling totals to zero.
2. At each house, choose between skipping it or taking its value plus the best total before the previous house.
3. Shift the rolling totals and return the latest best.

## Why It Works

An optimal selection either excludes the current house or includes it and necessarily excludes its neighbor.

## Worked Example

**Illustrative input:** `nums = [2, 7, 9, 3, 1]`.

**Trace:** The best totals for successive prefixes are 2, 7, 11, 11, and 12.

**Result:** Return `12`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = (0, 0)
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Do not choose houses greedily by individual value. Read the old two rolling states before overwriting them.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc198|Coding Practice Index — House Robber]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 198](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0198-house-robber.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
