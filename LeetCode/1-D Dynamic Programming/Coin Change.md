---
tags:
  - leetcode
problem_number: 322
difficulty: "Medium"
pattern: "1-D Dynamic Programming"
languages:
  - Python
---

Find the fewest coins needed to make an amount, with unlimited use of each positive denomination.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc322|LeetCode — LC 322]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Create a table of best counts, initialized to an unreachable sentinel except amount zero.
2. For each amount in increasing order, try every coin that fits.
3. Improve its count from the smaller amount plus one; return -1 if the target remains unreachable.

## Why It Works

Every optimal nonempty solution has a final coin, and removing it leaves an optimal solution for the remaining smaller amount.

## Worked Example

**Illustrative input:** `coins = [1, 3, 4]`, `amount = 6`.

**Trace:** The table can reach 6 with two 3 coins, beating the greedy 4,1,1 choice.

**Result:** Return `2`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
```

## Complexity

$O(Ac)$ time and $O(A)$ space for amount `A` and `c` coin types. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Greedy largest-first is not generally correct. Positive denominations ensure dependencies point to smaller amounts.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc322|Coding Practice Index — Coin Change]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 322](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0322-coin-change.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
