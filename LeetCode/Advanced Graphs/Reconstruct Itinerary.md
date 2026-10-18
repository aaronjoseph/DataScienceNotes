---
tags:
  - leetcode
problem_number: 332
difficulty: "Hard"
pattern: "Advanced Graphs"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        destinations = defaultdict(list)
        for source, destination in tickets:
            destinations[source].append(destination)
        for options in destinations.values():
            options.sort(reverse=True)
        stack, reverse_route = ["JFK"], []
        while stack:
            source = stack[-1]
            if destinations[source]:
                stack.append(destinations[source].pop())
            else:
                reverse_route.append(stack.pop())
        route = reverse_route[::-1]
        return route if len(route) == len(tickets) + 1 else []
```

## Complexity

$O(E\log E)$ time and $O(E+V)$ storage. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Use every flight ticket exactly once to construct the lexicographically smallest valid itinerary starting at JFK.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc332|LeetCode — LC 332]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Store destinations for each departure in reverse lexical order.
2. Use an explicit stack to consume the smallest available destination from its end.
3. When an airport has no outgoing tickets left, append it to a reverse route; reverse the completed route.

## Why It Works

Hierholzer's method builds an Eulerian trail by splicing exhausted routes; ordered edge consumption selects the lexical itinerary under the valid-itinerary contract.

## Worked Example

**Illustrative input:** Tickets `[["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]`.

**Trace:** The apparent KUL dead end is placed at the end during route reversal.

**Result:** Return `["JFK", "NRT", "JFK", "KUL"]`.

## Common Pitfalls

Tickets are edges, and duplicate tickets are separate usable edges. Appending an airport when first visited can choose an unusable greedy route.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc332|Coding Practice Index — Reconstruct Itinerary]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 332](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0332-reconstruct-itinerary.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
