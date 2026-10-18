---
tags:
  - leetcode
problem_number: 787
difficulty: "Medium"
pattern: "Advanced Graphs"
languages:
  - Python
---

Find the cheapest flight route with at most k intermediate stops, so at most k+1 edges may be used.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc787|LeetCode — LC 787]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Initialize source cost to zero and every other cost to infinity.
2. Perform k+1 rounds of edge relaxation, writing into a fresh copy of the previous round's costs.
3. After the final round, return the destination cost or -1 if still unreachable.

## Why It Works

Each round extends paths from the previous round by at most one edge, preserving the edge-count limit.

## Worked Example

**Illustrative input:** Flights `[[0, 1, 1], [1, 2, 1], [0, 2, 5]]`, source 0, destination 2, `k = 0`.

**Trace:** Only one edge is allowed, so the cheap two-edge path cannot be used.

**Result:** Return `5`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float('inf') else prices[dst]
```

## Complexity

$O((k+1)(V+E))$ time, including array copies, and $O(V)$ auxiliary space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Do not update the same cost array in place within a round; that could use too many edges. Stops count excludes source and destination.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc787|Coding Practice Index — Cheapest Flights Within K Stops]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 787](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0787-cheapest-flights-within-k-stops.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
