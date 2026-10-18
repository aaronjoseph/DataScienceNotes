---
tags:
  - leetcode
problem_number: 309
difficulty: "Medium"
pattern: "2-D Dynamic Programming"
languages:
  - Python
---

Maximize stock profit with unlimited transactions but a mandatory one-day cooldown after selling.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc309|LeetCode — LC 309]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Memoize the best future profit by day and whether the next action may be a buy.
2. At each state, consider waiting or taking the permitted buy/sell action.
3. Buying advances one day; selling advances two days to enforce the cooldown; return the better branch.

## Why It Works

Day and holding state determine all legal future actions, and the cooldown is fully captured by skipping the day after a sale.

## Worked Example

**Illustrative input:** `prices = [1, 2, 3, 0, 2]`.

**Trace:** Buy at 1, sell at 2, wait one day, buy at 0, and sell at 2.

**Result:** Return `3`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[i, buying]
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[i, buying] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[i, buying] = max(sell, cooldown)
            return dp[i, buying]
        return dfs(0, True)
```

## Complexity

$O(n)$ time and $O(n)$ memo/recursion space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

The two-day jump applies after selling, not buying. This is a different contract from the one-transaction stock problem.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc309|Coding Practice Index — Best Time to Buy And Sell Stock With Cooldown]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 309](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0309-best-time-to-buy-and-sell-stock-with-cooldown.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
