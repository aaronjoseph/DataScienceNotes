---
tags:
  - leetcode
problem_number: 746
difficulty: "Easy"
pattern: "1-D Dynamic Programming"
languages:
  - Python
---

Pay each visited stair's cost and reach just beyond the final stair, starting at index zero or one.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc746|LeetCode — LC 746]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Work backward, replacing each earlier cost with the cheapest total cost from that stair.
2. Add the cheaper of the next two already solved stair totals.
3. Return the smaller total from the two allowed starting stairs.

## Why It Works

After paying at a stair, the only choices are advancing one or two stairs, and both suffix costs are already optimal.

## Worked Example

**Illustrative input:** `cost = [10, 15, 20]`.

**Trace:** Starting at stair 1 and jumping beyond the last stair costs only 15.

**Result:** Return `15`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])
```

## Complexity

$O(n)$ time and $O(1)$ extra space because this implementation overwrites the input array. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

The destination is beyond the final index. This implementation assumes at least two costs and mutates them.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc746|Coding Practice Index — Min Cost Climbing Stairs]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 746](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0746-min-cost-climbing-stairs.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
