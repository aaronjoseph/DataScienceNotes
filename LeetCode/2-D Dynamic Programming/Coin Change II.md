---
tags:
  - leetcode
problem_number: 518
difficulty: "Medium"
pattern: "2-D Dynamic Programming"
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
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0] * (amount + 1)
        ways[0] = 1
        for coin in coins:
            for subtotal in range(coin, amount + 1):
                ways[subtotal] += ways[subtotal - coin]
        return ways[amount]
```

## Complexity

$O(Ac)$ time and $O(A)$ space for amount `A` and `c` coin types. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Count order-independent ways to make an amount with unlimited use of positive coin denominations.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc518|LeetCode — LC 518]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Initialize a one-dimensional count table with one way to make amount zero.
2. Process one coin denomination at a time.
3. For each coin, scan amounts upward and add the count for the amount reduced by that coin.

## Why It Works

Processing coin types in an outer loop counts each multiset once; increasing amounts permits repeated use of the current coin.

## Worked Example

**Illustrative input:** `coins = [1, 2]`, `amount = 3`.

**Trace:** The combinations are three 1 coins, or one 1 plus one 2.

**Result:** Return `2`; reversing coin order does not create another combination.

## Common Pitfalls

Swapping loop order counts ordered sequences instead. Amount zero has one combination: choosing no coins.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc518|Coding Practice Index — Coin Change II]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 518](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0518-coin-change-ii.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
