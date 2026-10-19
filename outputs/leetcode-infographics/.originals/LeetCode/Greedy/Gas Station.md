---
tags:
  - leetcode
problem_number: 134
difficulty: "Medium"
pattern: "Greedy"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, balance, start = 0, 0, 0
        for index, (supply, expense) in enumerate(zip(gas, cost)):
            difference = supply - expense
            total += difference
            balance += difference
            if balance < 0:
                start = index + 1
                balance = 0
        return start if total >= 0 else -1
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Find a starting gas station from which a full circular trip is possible, or return -1.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc134|LeetCode — LC 134]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Track the total gas-minus-cost balance and the balance since the current candidate start.
2. If the candidate balance becomes negative at an edge, discard every start through that edge and begin after it.
3. Return the surviving candidate if the overall balance is nonnegative; otherwise return -1.

## Why It Works

If a candidate fails at an edge, any later start inside its failed segment has no greater fuel on reaching that edge and also fails.

## Worked Example

**Illustrative input:** `gas = [1, 2, 3]`, `cost = [2, 3, 1]`.

**Trace:** Starts 0 and 1 fail at a deficit; start 2 accumulates enough fuel to pass both.

**Result:** Return `2`.

## Common Pitfalls

A locally feasible prefix does not prove a full circuit. Check the total balance before accepting the final candidate.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc134|Coding Practice Index — Gas Station]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 134](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0134-gas-station.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
