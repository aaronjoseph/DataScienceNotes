---
tags:
  - leetcode
problem_number: 238
difficulty: "Medium"
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

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
```

## Complexity

$O(n)$ time and $O(1)$ auxiliary space, excluding the required output. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

For each position, return the product of every other element without division. Combine a product from the left with one from the right.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc238|LeetCode — LC 238]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Fill the output with prefix products, excluding the current element.
2. Walk backward while maintaining a suffix product.
3. Multiply each stored prefix by the suffix, then include the current value in the suffix.

## Why It Works

The left and right ranges are disjoint and together contain every position except the current one.

## Worked Example

**Illustrative input:** `nums = [2, 3, 4]`.

**Trace:** Prefixes are `[1, 2, 6]`; the reverse pass supplies products to their right.

**Result:** Return `[12, 8, 6]`.

## Common Pitfalls

Use 1 for an empty product. This handles zeros naturally; fixed-width languages must respect product bounds.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc238|Coding Practice Index — Product of Array Except Self]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 238](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0238-product-of-array-except-self.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
