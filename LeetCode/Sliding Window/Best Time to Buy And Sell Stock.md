---
tags:
  - leetcode
problem_number: 121
difficulty: "Easy"
pattern: "Sliding Window"
languages:
  - Python
---

Find the maximum profit from one buy followed by one sell. Remember the cheapest price seen so far.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc121|LeetCode — LC 121]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Initialize the cheapest price from the first day and best profit to zero.
2. For each later day, update the cheapest price and the profit available by selling today.
3. Return the largest nonnegative profit.

## Why It Works

For a fixed sell day, the cheapest earlier buy is always optimal.

## Worked Example

**Illustrative input:** `prices = [7, 2, 5, 1, 4]`.

**Trace:** Buying at 2 and selling at 5 earns 3; buying later at 1 and selling at 4 also earns 3.

**Result:** Return `3`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

You cannot sell before buying. A decreasing price sequence returns zero, not a negative profit.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc121|Coding Practice Index — Best Time to Buy And Sell Stock]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 121](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0121-best-time-to-buy-and-sell-stock.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
