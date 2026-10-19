---
tags:
  - leetcode
problem_number: 55
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

    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Decide whether the final array position is reachable when each value gives a maximum forward jump.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc55|LeetCode — LC 55]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Treat the final index as the current goal.
2. Scan backward; whenever an index can reach the current goal, make that index the new goal.
3. Return whether index zero becomes the goal.

## Why It Works

An index that reaches any known-good position can also reach the end; the backward scan collects exactly such positions.

## Worked Example

**Illustrative input:** `nums = [2, 0, 1]`.

**Trace:** Index zero can jump directly to the final index even though the middle position cannot move.

**Result:** Return `True`.

## Common Pitfalls

Values are maximum jump lengths, so shorter jumps are allowed. A zero blocks only routes that must land there.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc55|Coding Practice Index — Jump Game]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 55](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0055-jump-game.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
