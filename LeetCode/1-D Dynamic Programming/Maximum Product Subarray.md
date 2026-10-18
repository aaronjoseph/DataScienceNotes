---
tags:
  - leetcode
problem_number: 152
difficulty: "Medium"
pattern: "1-D Dynamic Programming"
languages:
  - Python
---

Find the greatest product of a nonempty contiguous subarray. Track both the smallest and largest products ending at each position.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc152|LeetCode — LC 152]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Start the global best from a real input value.
2. For each value, consider starting a new subarray and extending either previous extreme.
3. Save both new extremes before overwriting state, then update the global maximum.

## Why It Works

A negative multiplier swaps the roles of smallest and largest previous products, so both extremes are necessary and sufficient.

## Worked Example

**Illustrative input:** `nums = [-2, 3, -4]`.

**Trace:** The negative product ending at 3 becomes a positive product after multiplication by -4.

**Result:** Return `24`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = (1, 1)
        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Keeping only the maximum loses negative products that can become optimal later. Zeros naturally permit a fresh start.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc152|Coding Practice Index — Maximum Product Subarray]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 152](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0152-maximum-product-subarray.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
