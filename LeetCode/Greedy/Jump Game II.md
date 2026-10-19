---
tags:
  - leetcode
problem_number: 45
difficulty: "Medium"
pattern: "Greedy"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0045 - Jump Game II.png|700]]

## Overview

Find the fewest forward jumps to reach the final position. Treat reachable ranges as breadth-first-search levels.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc45|LeetCode — LC 45]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Maintain the interval reachable with the current number of jumps.
2. Scan every position in that interval to find the farthest next reach.
3. Advance to the next interval and increment the jump count until the end is covered.

## Why It Works

Every interval contains exactly the newly reachable positions for one jump count, so the first interval covering the end uses the fewest jumps.

## Worked Example

**Illustrative input:** `nums = [2, 3, 1, 1, 4]`.

**Trace:** The first jump reaches indices 1–2; from there the next jump can reach index 4.

**Result:** Return `2`.

## Common Pitfalls

The problem guarantees reachability. A reusable version must detect a nonexpanding frontier to avoid an infinite loop.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc45|Coding Practice Index — Jump Game II]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def jump(self, nums: List[int]) -> int:
        l, r = (0, 0)
        res = 0
        while r < len(nums) - 1:
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 45](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0045-jump-game-ii.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
