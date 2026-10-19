---
tags:
  - leetcode
problem_number: 338
difficulty: "Easy"
pattern: "Bit Manipulation"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0338 - Counting Bits.png|700]]

## Overview

Return the number of set bits for every integer from zero through n using previously solved smaller values.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc338|LeetCode — LC 338]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Initialize all counts to zero and track the greatest power of two no larger than the current value.
2. Advance that power when the next value reaches the next power of two.
3. The current count is one for its leading bit plus the stored count after removing that power.

## Why It Works

Removing the highest set bit leaves a smaller number whose count has already been computed.

## Worked Example

**Illustrative input:** `n = 5`.

**Trace:** Counts for 4 and 5 reuse counts for 0 and 1, adding their leading bit.

**Result:** Return `[0, 1, 1, 2, 1, 2]`.

## Common Pitfalls

Keep zero's count at zero. Update the tracked power exactly when the current value reaches the next power of two.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc338|Coding Practice Index — Counting Bits]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
```

## Complexity

$O(n)$ time and $O(1)$ auxiliary space beyond the required $O(n)$ output table. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 338](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0338-counting-bits.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
