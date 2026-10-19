---
tags:
  - leetcode
problem_number: 347
difficulty: "Medium"
pattern: "Arrays & Hashing"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0347 - Top K Frequent Elements.png|700]]

## Overview

Return the k most frequent distinct values. Bucket values by their occurrence counts.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc347|LeetCode — LC 347]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Count each value with a map.
2. Create frequency buckets from zero through the input length and place each distinct value in its bucket.
3. Scan buckets from largest frequency downward and collect values until k have been chosen.

## Why It Works

The descending scan visits every higher-frequency value before any lower-frequency value.

## Worked Example

**Illustrative input:** `nums = [1, 1, 1, 2, 2, 3]`, `k = 2`.

**Trace:** Buckets 3 and 2 hold 1 and 2.

**Result:** Return `[1, 2]`.

## Common Pitfalls

The problem guarantees a unique top-k set. A general version with ties should stop after k individual values.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc347|Coding Practice Index — Top K Frequent Elements]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            res += freq[i]
            if len(res) == k:
                return res
```

## Complexity

$O(n)$ expected time and $O(n)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 347](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0347-top-k-frequent-elements.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
