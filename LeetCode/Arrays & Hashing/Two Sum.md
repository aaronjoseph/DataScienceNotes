---
tags:
  - leetcode
problem_number: 1
difficulty: "Easy"
pattern: "Arrays & Hashing"
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

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
```

## Complexity

$O(n)$ expected time and $O(n)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Return the indices of two distinct numbers whose sum is the target. Search earlier values for the missing partner.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc1|LeetCode — LC 1]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Maintain a map from value to an earlier index.
2. For each current value, subtract it from the target and look up that complement.
3. If found, return the earlier index and current index; otherwise record the current value.

## Why It Works

Every pair is checked when its later element is visited, and looking up before inserting prevents reusing one element.

## Worked Example

**Illustrative input:** `nums = [4, 2, 7]`, `target = 9`.

**Trace:** Record 4 and 2. At 7, the needed partner 2 is at index 1.

**Result:** Return `[1, 2]`.

## Common Pitfalls

Return indices, not values. Repeated values can form a pair if they occupy different positions.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc1|Coding Practice Index — Two Sum]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 1](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0001-two-sum.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
