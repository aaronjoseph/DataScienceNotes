---
tags:
  - leetcode
problem_number: 217
difficulty: "Easy"
pattern: "Arrays & Hashing"
languages:
  - Python
---

Return whether an integer appears more than once. Remember values already seen in a hash set.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc217|LeetCode — LC 217]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Start with an empty set.
2. For each value, return true if it is already in the set; otherwise insert it.
3. Return false after scanning all values.

## Why It Works

Before each lookup, the set contains exactly the earlier values, so a hit proves a repeated occurrence.

## Worked Example

**Illustrative input:** `nums = [4, 7, 4]`.

**Trace:** Insert 4, then 7. The final 4 is already present.

**Result:** Return `True`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
```

## Complexity

$O(n)$ expected time and $O(n)$ extra space for `n` values. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Use value equality, and check before inserting. Hash lookup bounds are expected, rather than worst-case guarantees.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc217|Coding Practice Index — Contains Duplicate]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 217](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0217-contains-duplicate.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
